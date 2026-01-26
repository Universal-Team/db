#!/usr/bin/env python3
from __future__ import annotations

import functools
import json
import pathlib
import re
from colorsys import hsv_to_rgb, rgb_to_hsv
from io import BytesIO
from os import system
from shutil import copyfile
from textwrap import shorten
from typing import Any, Dict, List, Optional, TextIO, Tuple

import click
import discord
import numpy
import qrcode
import requests
import yaml
from bs4 import BeautifulSoup
from dateutil import parser
from markdownify import markdownify
from PIL import Image, ImageDraw, ImageFile
from PIL.PngImagePlugin import PngImageFile
from requests.utils import requote_uri

from img2tdx import img2tdx
from unistore import StoreEntry, UniStore, ICONS_PER_SHEET
from utils import (format_to_web_name, format_traceback, get_matching_app,
                   to_friendly_bytes, was_recently_updated)

DOWNLOAD_BLACKLIST = r"(\.3ds$|\.apk|\.appimage|\.flatpak|\.dmg|\.dol|\.exe|\.ipa|\.love|\.nro|\.opk|\.pkg|\.smdh|\.vpk|\.xz|armhf|elf|linux|macos|osx|PS3|PSP|switch|ubuntu|vita|wii|win|x86_64|xbox)"
DOCS_DIR: Optional[pathlib.Path] = None
PRIORITY_MODE = True
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
TEMP_DIR = SCRIPT_DIR / "temp"
BG_IMAGE = None


def saveIcon(img: Image.Image, index: int, ds: bool,
			 *, location: Optional[str] = None) -> Tuple[Image.Image, str]:
	location = location or str(TEMP_DIR)
	loc_path = pathlib.Path(location)
	if not loc_path.exists():
		loc_path.mkdir(parents=True)

	if img.mode == "P":
		pal = img.palette.palette
		img = img.convert("RGBA")
		data = numpy.array(img)
		r, g, b, a = data.T
		transparent = (r == pal[2]) & (g == pal[1]) & (b == pal[0])
		data[...][transparent.T] = (0, 0, 0, 0)
		img = Image.fromarray(data)
	elif img.mode != "RGBA":
		img = img.convert("RGBA")

	img.thumbnail((48, 48))
	forty_eight = loc_path / "48"
	if not forty_eight.exists():
		forty_eight.mkdir(parents=True, exist_ok=True)

	img.save((forty_eight / f"{index}.png"))

	if ds:
		imgDS = img.copy()
		imgDS.thumbnail((32, 32))
		data = numpy.array(imgDS)
		r, g, b, a = data.T
		transparent = a < 0xFF
		data[...][transparent.T] = (0xFF, 0, 0xFF, 0xFF)
		imgDS = Image.fromarray(data)
		imgDS = imgDS.quantize()
		thirty_two = loc_path / "32"
		if not thirty_two.exists():
			thirty_two.mkdir(parents=True, exist_ok=True)
		imgDS.save((thirty_two / f"{index}.png"))

	color = img.copy()
	color.thumbnail((1, 1))
	color = color.getpixel((0, 0))
	return img, f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def retroarchUniStore() -> None:
	"""Generates the RetroArch Cores UniStore"""

	print("Generating RetroArch UniStore")

	unistoreRA = UniStore(
		"RetroArch Cores",
		"Libretro",
		"RetroArch cores",
		"https://db.universal-team.net/unistore/retroarch.unistore",
		["https://db.universal-team.net/unistore/retroarch.t3x"]
	)

	iconIndexRA = -1

	# Add everything to the RetroArch UniStore
	r = requests.get("https://buildbot.libretro.com/nightly/nintendo/3ds/latest/3dsx/.index-extended")
	for app in r.text.strip().split("\n"):
		name = app.split(" ")[2][:-9]
		print(name)

		href = f"https://buildbot.libretro.com/nightly/nintendo/3ds/latest/3dsx/{name}.3dsx.zip"

		# Get metadata
		info = {}
		for item in requests.get(f"https://raw.githubusercontent.com/libretro/libretro-core-info/master/{name}.info").text.strip().split("\n"):
			matches = re.findall(r'(.*?) *= *"(.*)"', item)
			if matches:
				info[matches[0][0]] = matches[0][1]

		img = requests.get(f"https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/{name[:-9]}.png")
		if img.status_code == 200:
			iconIndexRA += 1
			saveIcon(Image.open(BytesIO(img.content)), iconIndexRA, False, location=str(TEMP_DIR.joinpath("ra")))

		notes = ""
		if "description" in info and len(info["description"]) > 200:
			notes += f"### Description\n{info['description']}\n\n"
		if "notes" in info:
			notes += "### Notes\n" + info["notes"].replace("|", "\n")

		entry = StoreEntry(
			info["display_name"] if "display_name" in info else name,
			info["authors"].replace("|", ", ") if "authors" in info else "libretro",
			shorten(info["description"], 200, placeholder="...") if "description" in info else "",
			info["display_version"] if "display_version" in info else "nightly",
			categories=info["categories"].split("|") if "categories" in info else ["emulator"],
			consoles=["3DS"],
			releaseNotes=notes,
			license=info["license"] if "license" in info else "",
			iconIndex=iconIndexRA if img.status_code == 200 else -1
		)

		entry.addDownloadScript(f"{name}.3dsx", f"{name}.zip", href, archive=(f"{name}.3dsx",))
		entry.addDownloadScript(f"{name}.cia", f"{name}.zip", href.replace("3dsx", "cia"), archive=(f"{name}.cia",), retroarch=True)

		unistoreRA.append(entry)

	# Make t3x
	with TEMP_DIR.joinpath("ra", "48", "icons.t3s").open("w", encoding="utf8") as file:
		file.write("--atlas -f rgba -z auto\n\n")
		for i in range(iconIndexRA):
			file.write(f"{i}.png\n")
	system(f"tex3ds -i {TEMP_DIR.joinpath('ra', '48', 'icons.t3s')} -o {DOCS_DIR.joinpath('unistore', 'retroarch.t3x')}")

	unistoreRA.save(DOCS_DIR.joinpath("unistore", "retroarch.unistore"))


def handle_gbatemp_app(r, app: Dict[str, Any]):
	soup = BeautifulSoup(r.text, "html.parser")

	if "title" not in app:
		app["title"] = soup.find(class_="p-title").h1.find(text=True).strip()

	if "author" not in app:
		app["author"] = soup.find(class_="username").text.strip()

	# if "description" not in app:
	# 	app["description"] = soup.find(class_="tagLine").text.strip()

	if "long_description" not in app:
		app["long_description"] = soup.find(class_="bbWrapper").decode_contents().strip()

	if "avatar" not in app:
		userId = soup.find(class_="username")["data-user-id"].strip()
		app["avatar"] = f"https://gbatemp.net/data/avatars/l/{userId[:3]}/{userId}.jpg"

	if "image" not in app:
		img = soup.find(class_="avatar").img
		if img:
			app["image"] = "https://gbatemp.net" + img["src"].strip()

	if "created" not in app:
		app["created"] = soup.find(class_="u-dt")["datetime"].replace("+0000", "Z")

	if "download_page" not in app:
		app["download_page"] = f"https://gbatemp.net/download/{app['gbatemp']}/"

	if "version" not in app:
		app["version"] = soup.find(class_="p-title").h1.span.text.strip()

	if "version_title" not in app:
		verTitle = soup.select("div.block > div > ol.block-body > li:first-of-type > h3 > a")
		if verTitle:
			app["version_title"] = verTitle[0].text.strip()

	if "updated" not in app:
		app["updated"] = soup.findAll(class_="u-dt")[2]["datetime"].replace("+0000", "Z")

	if "update_notes" not in app or "update_notes_md" not in app:
		if "update_notes" not in app:
			notesSoup = BeautifulSoup(requests.get(f"https://gbatemp.net/download/{app['gbatemp']}/updates").text, "html.parser")
			app["update_notes"] = notesSoup.find(class_="bbWrapper").decode_contents().strip()

		if "update_notes_md" not in app:
			app["update_notes_md"] = markdownify(app["update_notes"], bullets="-")

	if "downloads" not in app:
		app["downloads"] = {}

	head = requests.head(f"https://gbatemp.net/download/{app['gbatemp']}/download")
	if head.status_code == 200:
		if "Content-Disposition" in head.headers:
			name = re.findall('filename="(.*)"', head.headers["Content-Disposition"])
			if len(name) > 0:
				name = name[0]
				if name not in app["downloads"]:
					app["downloads"][name] = {
						"url": head.url,
					}

					if "Content-Length" in head.headers:
						app["downloads"][name]["size"] = int(head.headers["Content-Length"])
						app["downloads"][name]["size_str"] = to_friendly_bytes(app["downloads"][name]["size"])
	return app


def handle_github_app(github: GitHubAPI, app: Dict[str, Any]):
	api = github.session.get(f"https://api.github.com/repos/{app['github']}").json()
	assert "message" not in api, app["github"] + " API Error: " + api["message"]
	releases = github.session.get(f"https://api.github.com/repos/{app['github']}/releases").json()
	assert "message" not in releases, app["github"] + " API Error: " + releases["message"]
	release = None
	prerelease = None
	if len(releases) > 0 and releases[0]["prerelease"]:
		prerelease = releases[0]
	for r in releases:
		if not (r["prerelease"] or r["draft"]):
			# check for usable assets
			for asset in r["assets"]:
				if (len(re.findall(app["download_filter"], asset["name"])) > 0 if "download_filter" in app else len(re.findall(DOWNLOAD_BLACKLIST, asset["name"])) == 0):
					break
					# didn't break (find a usable asset)? skip this release.
				else:
					continue
			release = r
			break

	# If no actual release found on page 1, try /latest
	if not release:
		release = github.session.get(f"https://api.github.com/repos/{app['github']}/releases/latest").json()
		if "message" in release and release["message"] == "Not Found":
			release = None

	if "title" not in app:
		app["title"] = api["name"]

	if "author" not in app:
		username = github.get_username(api['owner']['login'])
		app["author"] = username

	if "description" not in app and api["description"] != "" and api["description"] is not None:
		app["description"] = api["description"]

	if "avatar" not in app:
		app["avatar"] = api["owner"]["avatar_url"]

	if "source" not in app:
		app["source"] = api["html_url"]

	if "created" not in app:
		app["created"] = api["created_at"]

	if "website" not in app and api["homepage"] != "" and api["homepage"] is not None:
		app["website"] = api["homepage"]

	if "wiki" not in app and api["has_wiki"]:
		_req = requests.get(f"https://raw.githubusercontent.com/wiki/{app['github']}/Home.md")
		if _req.status_code != 404:
			app["wiki"] = f"{api['html_url']}/wiki"

	if api["license"]:
		if "license" not in app:
			app["license"] = api["license"]["key"]

		if "license_name" not in app:
			app["license_name"] = api["license"]["name"]

	if api["stargazers_count"]:
		# accumulate incase other apis
		app["stars"] += api["stargazers_count"]

	if release:
		if "download_page" not in app:
			app["download_page"] = f"https://github.com/{app['github']}/releases"

		if "version" not in app:
			app["version"] = release["tag_name"]

		if "version_title" not in app and release["name"] != "" and release["name"] is not None:
			app["version_title"] = release["name"]

		if "update_notes" not in app and release["body"] != "" and release["body"] is not None:
			app["update_notes_md"] = release["body"].replace("\r\n", "\n")
			app["update_notes"] = github.format_markdown(release["body"], mode="gfm", context=app["github"])
			app["update_notes"] = re.sub(r'https:\/\/private-user-images.githubusercontent.com\/\d+\/\d+-([\da-f\-]{36})[^"]*', r'https://github.com/user-attachments/assets/\1', app["update_notes"])

		if "updated" not in app:
			app["updated"] = release["published_at"]

		if "downloads" not in app:
			app["downloads"] = {}
		for asset in release["assets"]:
			if not asset["name"] in app["downloads"] and (len(re.findall(app["download_filter"], asset["name"])) > 0 if "download_filter" in app else len(re.findall(DOWNLOAD_BLACKLIST, asset["name"])) == 0):
				app["downloads"][asset["name"]] = {
					"url": asset["browser_download_url"],
					"size": asset["size"],
					"size_str": to_friendly_bytes(asset["size"])
				}

	if prerelease:
		if "prerelease" not in app:
			app["prerelease"] = {}

		if "downloads" not in app["prerelease"]:
			app["prerelease"]["downloads"] = {}
		for asset in prerelease["assets"]:
			if not asset["name"] in app["prerelease"]["downloads"] and (len(re.findall(app["download_filter"], asset["name"])) > 0 if "download_filter" in app else len(re.findall(DOWNLOAD_BLACKLIST, asset["name"])) == 0):
				app["prerelease"]["downloads"][asset["name"]] = {
					"url": asset["browser_download_url"],
					"size": asset["size"],
					"size_str": to_friendly_bytes(asset["size"])
				}

		if len(app["prerelease"]["downloads"]) > 0:
			if "download_page" not in app:
				app["download_page"] = f"https://github.com/{app['github']}/releases"
			if "download_page" not in app["prerelease"]:
				app["prerelease"]["download_page"] = prerelease["html_url"]

			if "version_title" not in app and "version" not in app and prerelease["name"] != "" and prerelease["name"] is not None:
				app["version_title"] = prerelease["name"]
			if "version_title" not in app["prerelease"] and prerelease["name"] != "" and prerelease["name"] is not None:
				app["prerelease"]["version_title"] = prerelease["name"]

			if "version" not in app:
				app["version"] = prerelease["tag_name"]
			if "version" not in app["prerelease"]:
				app["prerelease"]["version"] = prerelease["tag_name"]

			if "update_notes" not in app["prerelease"] and prerelease["body"] != "" and prerelease["body"] is not None:
				app["prerelease"]["update_notes_md"] = prerelease["body"].replace("\r\n", "\n")
				app["prerelease"]["update_notes"] = github.format_markdown(prerelease["body"], mode="gfm",
															   context=app["github"])
				app["prerelease"]["update_notes"] = re.sub(r'<a target="_blank" rel="noopener noreferrer" href="https:\/\/private-user-images.githubusercontent\.com.*?<\/a>', "", app["prerelease"]["update_notes"])

				if "update_notes" not in app:
					app["update_notes_md"] = app["prerelease"]["update_notes_md"]
					app["update_notes"] = app["prerelease"]["update_notes"]

			if "updated" not in app:
				app["updated"] = prerelease["published_at"]
			if "updated" not in app["prerelease"]:
				app["prerelease"]["updated"] = prerelease["published_at"]

			if not "nightly" in app and re.match(r"^[a-zA-Z]+$", app["prerelease"]["version"]):
				app["nightly"] = app["prerelease"]
				app.pop("prerelease")
		else:
			app.pop("prerelease")

	return app


def handle_bitbucket_app(app: Dict[str, Any]):
	api = requests.get(f"https://api.bitbucket.org/2.0/repositories/{app['bitbucket']['repo']}").json()

	if "title" not in app:
		app["title"] = api["name"]

	if "author" not in app:
		app["author"] = api["owner"]["display_name"]

	if "description" not in app:
		app["description"] = api["description"].replace("\r\n", "\n")

	if "avatar" not in app:
		app["avatar"] = api["links"]["avatar"]["href"]

	if "source" not in app:
		app["source"] = api["links"]["html"]["href"]

	if "created" not in app:
		app["created"] = api["created_on"]

	if "files" in app["bitbucket"]:
		if "downloads" not in app:
			app["downloads"] = {}
		for download in app["bitbucket"]["files"]:
			fileAPI = requests.get(f"https://api.bitbucket.org/2.0/repositories/{app['bitbucket']['repo']}/src/{(app['bitbucket']['branch'] if 'branch' in app['bitbucket'] else 'master')}/{download.replace(' ', '%20')}?format=meta").json()
			if download not in app["downloads"]:
				app["downloads"][download[download.rfind("/") + 1:]] = {
					"url": fileAPI["links"]["self"]["href"],
					"size": fileAPI["size"],
					"size_str": to_friendly_bytes(fileAPI["size"])
				}

			if "download_page" not in app:
				app["download_page"] = f"https://bitbucket.org/{app['bitbucket']['repo']}/src/{(app['bitbucket']['branch'] if 'branch' in app['bitbucket'] else 'master')}/{download}"

			if "version" not in app:
				app["version"] = fileAPI["commit"]["hash"][:7]

			if "updated" not in app:
				commit = requests.get(fileAPI["commit"]["links"]["self"]["href"]).json()
				app["updated"] = commit["date"]
	
	return app


def handle_gitlab_app(app: Dict[str, Any]):
	gitlab_id = app["gitlab"].replace('/', '%2F')
	endpoint = app.get("gitlab_endpoint", "https://gitlab.com")
	repo = requests.get(f"{endpoint}/api/v4/projects/{gitlab_id}").json()
	releases = requests.get(f"{endpoint}/api/v4/projects/{gitlab_id}/releases?include_html_description=true").json()
	release = releases[0]
	if "title" not in app:
		app["title"] = repo["name"]
	if "author" not in app:
		app["author"] = repo["namespace"]["name"]
	if "description" not in app:
		app["description"] = repo["description"]
	if "avatar" not in app:
		app["avatar"] = repo["avatar_url"]
	if "source" not in app:
		app["source"] = repo["web_url"]
	if "created" not in app:
		app["created"] = repo["created_at"]
	app["stars"] += repo["star_count"]

	if release:
		if "download_page" not in app:
			app["download_page"] = f"{endpoint}/{app['gitlab']}/-/releases"

		if "version" not in app:
			app["version"] = release["tag_name"]

		if "version_title" not in app and release["name"] != "" and release["name"] is not None:
			app["version_title"] = release["name"]

		if "update_notes" not in app and release["description"] != "" and release["description"] is not None:
			app["update_notes_md"] = release["description"].replace("\r\n", "\n")
			if "description_html" in release:
				app["update_notes"] = release["description_html"].replace("\r\n", "\n")
			else:
				app["update_notes"] = release["description"].replace("\r\n", "\n")

		if "updated" not in app:
			app["updated"] = release["released_at"]

		if "downloads" not in app:
			app["downloads"] = {}
		for asset in release["assets"]["links"]:
			if not asset["name"] in app["downloads"] and (len(re.findall(app["download_filter"], asset["name"])) > 0 if "download_filter" in app else len(re.findall(DOWNLOAD_BLACKLIST, asset["name"])) == 0):
				app["downloads"][asset["name"]] = {
					"url": asset["direct_asset_url"]
				}

	return app


def create_web_file(app: Dict[str, Any]):
	web = app.copy()
	web["layout"] = "app"
	# We want unique IDs as hex
	if "unique_ids" in web:
		web["unique_ids"] = [f"0x{uid:X}" for uid in web["unique_ids"]]
	# long description is put as the content
	if "long_description" in web:
		web.pop("long_description")
	# Remove large things that aren't needed
	if "update_notes_md" in web:
		web.pop("update_notes_md")
	if "scripts" in web:
		web.pop("scripts")
	if "archive" in web:
		web.pop("archive")
	if "slug" in web:
		web.pop("slug")
	if "urls" in web:
		web.pop("urls")
	if "icon_index" in web:
		web.pop("icon_index")
	if "installed_files" in web:
		web.pop("installed_files")
	# Add defaults where absolutely needed
	if "systems" not in web:
		web["systems"] = ["3DS"]  # default to 3DS
	if "updated" not in web:
		web["updated"] = "---"
	for sys in web["systems"]:
		if "title" in web:
			with open(DOCS_DIR.joinpath(f"_{format_to_web_name(sys)}", f"{format_to_web_name(web['title'])}.md"), "w", encoding="utf8") as file:
				file.write(f"---\n{yaml.dump(web, sort_keys=True, allow_unicode=True)}---\n")
				if "long_description" in app:
					file.write(app["long_description"])
	
	return web


def handle_screenshots(app_title: str, docs_dir: pathlib.Path):
	screenshots = []
	screenshots_path = docs_dir.joinpath("assets", "images", "screenshots", format_to_web_name(app_title))
	if screenshots_path.exists():
		dirlist = sorted(screenshots_path.iterdir())
		for screenshot in dirlist:
			if screenshot.suffix.lower()[1:] in ["png", "gif", "jpg", "peg", "iff", "bmp"]:
				screenshots.append({
					"url": f"https://db.universal-team.net/assets/images/screenshots/{format_to_web_name(app_title)}/{screenshot.name}",
					"description": screenshot.stem.capitalize().replace("-", " ")
				})

	return screenshots or None


def create_error_report(e, app_name, webhook: discord.SyncWebhook):
	embed = discord.Embed(title="Universal-DB Exception Occurred")
	embed.description = f"```py\n{e}```"
	if app_name:
		embed.add_field(name="App Name", value=app_name)

	webhook.send(embeds=[embed])


def fetch_app_data(app: Dict[str, Any], github_session: GitHubAPI):
	# GBATemp is deprecated.
	# if "gbatemp" in app:
	# click.echo("GBAtemp Download Center")
	# r = requests.get(f"https://gbatemp.net/download/{app['gbatemp']}/")
	# if r.status_code != 200:
	#	click.secho(f"Error {r.status_code:d}, using old data!", fg="yellow")
	#	app = list(filter(lambda x: "gbatemp" in x and x["gbatemp"] == app["gbatemp"], old_data))[0]
	# else:
	#	app = handle_gbatemp_app(r, app)
	if "gbatemp" in app:
		# We don't need to match because we don't pull anything and we'll return prematurely
		click.secho(f'{app["title"] if "title" in app else ""}: Using old data for GBATemp', fg='yellow')
		return app

	if "github" in app:
		click.echo(f'GitHub -- {app["github"]}')
		app = handle_github_app(github_session, app)

	if "bitbucket" in app:
		click.echo(f'Bitbucket -- {app["bitbucket"]["repo"]}')
		app = handle_bitbucket_app(app)

	if "gitlab" in app:
		click.echo(f'GitLab -- {app["gitlab"]}')
		app = handle_gitlab_app(app)

	return app


class FetchAppDataError(Exception):
	def __init__(self, inner: Exception):
		super().__init__("Failed to fetch app data")
		self.inner = inner


def process_app_entry(app: Dict[str, Any], fp: str, icon_idx: int, github_api: GitHubAPI, old_data,
					  *, webhook=None) -> Optional[Tuple[Dict[str, Any], int]]:
	iconIndex = icon_idx
	app["stars"] = 0
	oldData = old_data

	try:
		app = fetch_app_data(app, github_api)
	except Exception as e:
		trace = format_traceback(e)
		if webhook:
			title = app['title'] if "title" in app else fp
			create_error_report(trace, title, webhook)

		click.secho(trace, fg="red")
		raise FetchAppDataError(e)

	# Do not update stars in priority mode
	if PRIORITY_MODE:
		old = next((item for item in oldData if item["title"] == app["title"]), None)
		if old:
			app["stars"] = old["stars"]

	# Process format strings in downloads if needed
	if "eval_downloads" in app and app["eval_downloads"]:
		if "download_page" in app and type(app["download_page"]) == str:
			app["download_page"] = eval(app["download_page"])
		if "downloads" in app:
			for item in app["downloads"]:
				if type(app["downloads"][item]["url"]) == str:
					app["downloads"][item]["url"] = eval(app["downloads"][item]["url"])
	if "eval_scripts" in app and app["eval_scripts"]:
		if "scripts" in app:
			for script in app["scripts"]:
				for function in app["scripts"][script]:
					if function["type"] == "downloadFile" and type(function["file"]) == str:
						function["file"] = eval(function["file"])
	if "eval_notes_md" in app and app["eval_notes_md"]:
		if "update_notes_md" in app:
			app["update_notes_md"] = eval(app["update_notes_md"])
			if "update_notes" not in app:
				app["update_notes"] = github_api.format_markdown(app["update_notes_md"], mode="gfm" if "github" in app else "markdown",
													 			 context=app["github"] if "github" in app else None)

	# If no markdown notes, generate from HTML
	if "update_notes_md" not in app and "update_notes" in app:
		app["update_notes_md"] = markdownify(app["update_notes"], bullets="-")

	# Ensure URLs don't have spaces
	for item in ["avatar", "download_page", "icon", "image", "source", "website", "wiki"]:
		if item in app and app[item] is not None:
			app[item] = requote_uri(app[item])

	# Format update notes with GitHub's API
	if "update_notes_md" in app and "update_notes" not in app:
		app["update_notes"] = github_api.format_markdown(app["update_notes_md"],
												   		 mode="gfm" if "github" in app else "markdown",
												   		 context=app["github"] if "github" in app else None)

	# Prematurely stop here, if no DOCS_DIR.
	# CLI normally checks for DOCS_DIR, if this is the all command
	if not DOCS_DIR:
		return

	# Handle app screenshots
	screenshots = handle_screenshots(app["title"], DOCS_DIR)
	if screenshots:
		app["screenshots"] = screenshots

	# Get missing download sizes
	if "downloads" in app:
		for download in app["downloads"]:
			if "size" not in app["downloads"][download]:
				if app["downloads"][download]["url"][:30] == "https://db.universal-team.net/":
					download_path = DOCS_DIR.joinpath(app['downloads'][download]['url'][30:])
					app["downloads"][download]["size"] = download_path.stat().st_size
					app["downloads"][download]["size_str"] = to_friendly_bytes(app["downloads"][download]["size"])
				else:
					r = requests.head(app["downloads"][download]["url"], allow_redirects=True)
					if r.status_code == 200 and "Content-Length" in r.headers:
						app["downloads"][download]["size"] = int(r.headers["Content-Length"])
						app["downloads"][download]["size_str"] = to_friendly_bytes(app["downloads"][download]["size"])

	# Check for local icon / image
	for ext in (".png", ".gif"):
		if "icon" not in app and DOCS_DIR.joinpath("assets", "images", "icons", format_to_web_name(app['title']) + ext).exists():
			app["icon"] = f"https://db.universal-team.net/assets/images/icons/{format_to_web_name(app['title'])}{ext}"

	if "image" not in app and DOCS_DIR.joinpath("assets", "images", "images", f"{format_to_web_name(app['title'])}.png").exists():
		app["image"] = f"https://db.universal-team.net/assets/images/images/{format_to_web_name(app['title'])}.png"
	elif "image" not in app and "icon" in app:
		app["image"] = app["icon"]
	elif "image" not in app and "avatar" in app:
		app["image"] = app["avatar"]
		if "github" in app["image"]:
			app["image"] += "&size=128"

	# Get image size
	if "image_length" not in app and "image" in app:
		if app["image"][:30] == "https://db.universal-team.net/":
			app["image_length"] = DOCS_DIR.joinpath(app["image"][30:]).stat().st_size
		else:
			r = requests.head(app["image"], allow_redirects=True)
			if r.status_code == 200 and "Content-Length" in r.headers:
				app["image_length"] = int(r.headers["Content-Length"])

	# Make icon for UniStore and QR
	img = None
	if "icon" in app or "image" in app or "icon_static" in app:
		url = app["icon_static"] if "icon_static" in app else (app["icon"] if "icon" in app else app["image"] if "image" in app else "")
		file = None
		if url[:30] == "https://db.universal-team.net/":
			file = DOCS_DIR.joinpath(url[30:]).open("rb")
		else:
			r = requests.get(url)
			if r.status_code == 200:
				file = BytesIO(r.content)
			else:
				click.secho(f"Error {r.status_code} downloading image!", fg="red")

		if file:
			if PRIORITY_MODE:
				old = next((item for item in oldData if item["title"] == app["title"]), {"icon_index": -1})
				app["icon_index"] = old["icon_index"] if "icon_index" in old else -1
			else:
				app["icon_index"] = iconIndex

			with Image.open(file) as img:
				img, color = saveIcon(img, iconIndex, True)
				if "color" not in app:
					app["color"] = color
				if "color_bg" not in app:
					# Darken color to a maximum of 50% brightness
					hsv = list(rgb_to_hsv(*[int(x, 16) / 255 for x in re.findall("#(..)(..)(..)", color)[0]]))
					hsv[2] = min(0.5, hsv[2])
					app["color_bg"] = "#%02x%02x%02x" % (*[round(x * 255) for x in hsv_to_rgb(*hsv)],)

			if "icon" in app and app["icon"].endswith(".bmp"):
				# This is also duplicated
				# TODO: Remove duplication
				tmp = TEMP_DIR.joinpath("48", f"{iconIndex}.png")
				to_src = DOCS_DIR.joinpath("assets", "images", "icons", f"{format_to_web_name(app['title'])}.png")
				copyfile(tmp, to_src)
				app["icon"] = f"https://db.universal-team.net/assets/images/icons/{format_to_web_name(app['title'])}.png"
			elif "icon_static" not in app and "icon" in app and app["icon"].endswith(".gif"):
				tmp = TEMP_DIR.joinpath("48", f"{iconIndex}.png")
				to_src = DOCS_DIR.joinpath("assets", "images", "icons", f"{format_to_web_name(app['title'])}.png")
				copyfile(tmp, to_src)
				app["icon_static"] = f"https://db.universal-team.net/assets/images/icons/{format_to_web_name(app['title'])}.png"

			if "image" in app and app["image"].endswith(".bmp"):
				app["image"] = app["icon"]

			iconIndex += 1

	# Make QR
	if "downloads" in app:
		for item in app["downloads"]:
			if item.endswith(".cia") or item.endswith(".nds") or item.endswith(".dsi"):
				qr = qrcode.make(app["downloads"][item]["url"], box_size=5, version=5).convert("RGBA")
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.width - img.width) // 2 - 5, (qr.height - img.height) // 2 - 10), ((qr.width + img.width) // 2 + 4, (qr.height + img.height) // 2 + 10 if "version" in app else 4)), fill=(255, 255, 255))
					qr.paste(img, ((qr.width - img.width) // 2, (qr.height - img.height) // 2), mask=img if img.mode == "RGBA" else None)
					if item.endswith(".cia"):
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 - 10), "3", (255, 0, 0))
						draw.text(((qr.width - img.width) // 2 + 6, (qr.height - img.height) // 2 - 10), "DS", (0, 0, 0))
					else:
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 - 10), "DSi", (0, 0, 0))
					if "version" in app:
						if img.width == 32 and len(app["version"]) > 5:
							draw.text(((qr.width - img.width) // 2 - 2, (qr.height - img.height) // 2 + img.height), app["version"][:(img.width + 4) // 6], (0, 0, 0))
						else:
							draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 + img.height), app["version"][:img.width // 6], (0, 0, 0))
				qr.save(DOCS_DIR.joinpath("assets", "images", "qr", f"{format_to_web_name(item)}.png"))
				if "qr" not in app:
					app["qr"] = {}
				app["qr"][item] = f"https://db.universal-team.net/assets/images/qr/{format_to_web_name(item)}.png"

	if "prerelease" in app:
		for item in app["prerelease"]["downloads"]:
			if item.endswith(".cia") or item.endswith(".nds") or item.endswith(".dsi"):
				qr = qrcode.make(app["prerelease"]["downloads"][item]["url"], box_size=5, version=5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0xD2, 0x99, 0x22, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.width - img.width) // 2 - 5, (qr.height - img.height) // 2 - 10), ((qr.width + img.width) // 2 + 4, (qr.height + img.height) // 2 + 10 if "version" in app["prerelease"] else 4)), fill=(255, 255, 255))
					qr.paste(img, ((qr.width - img.width) // 2, (qr.height - img.height) // 2), mask=img if img.mode == "RGBA" else None)
					if item.endswith(".cia"):
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 - 10), "3", (255, 0, 0))
						draw.text(((qr.width - img.width) // 2 + 6, (qr.height - img.height) // 2 - 10), "DS", (246, 106, 10))
					else:
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 - 10), "DSi", (246, 106, 10))
					if "version" in app["prerelease"]:
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 + img.height), app["prerelease"]["version"][:img.width // 6], (246, 106, 10))
				qr.save(DOCS_DIR.joinpath("assets", "images", "qr", "prerelease", f"{format_to_web_name(item)}.png"))
				if "qr" not in app["prerelease"]:
					app["prerelease"]["qr"] = {}
				app["prerelease"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/prerelease/{format_to_web_name(item)}.png"

	if "nightly" in app:
		for item in app["nightly"]["downloads"]:
			if item.endswith(".cia") or item.endswith(".nds") or item.endswith(".dsi"):
				qr = qrcode.make(app["nightly"]["downloads"][item]["url"], box_size=5, version=5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0, 0, 0xC0, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.width - img.width) // 2 - 5, (qr.height - img.height) // 2 - 10), ((qr.width + img.width) // 2 + 4, (qr.height + img.height) // 2 + 4)), fill=(255, 255, 255))
					qr.paste(img, ((qr.width - img.width) // 2, (qr.height - img.height) // 2), mask=img if img.mode == "RGBA" else None)
					if item.endswith(".cia"):
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 - 10), "3", (255, 0, 0))
						draw.text(((qr.width - img.width) // 2 + 6, (qr.height - img.height) // 2 - 10), "DS", (0, 0, 192))
					else:
						draw.text(((qr.width - img.width) // 2, (qr.height - img.height) // 2 - 10), "DSi", (0, 0, 192))
				qr.save(DOCS_DIR.joinpath("assets", "images", "qr", "git", f"{format_to_web_name(item)}.png"))
				if "qr" not in app["nightly"]:
					app["nightly"]["qr"] = {}
				app["nightly"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/git/{format_to_web_name(item)}.png"
	
	return app, iconIndex


class GitHubAPI:
	def __init__(self, *, token=None):
		self.session = requests.Session()

		github_headers = {"Accept": "application/vnd.github+json",
					  	  "X-GitHub-Api-Version": "2022-11-28"}
		if token:
			github_headers["Authorization"] = f"Bearer {token}"
		self.session.headers.update(github_headers)

	@functools.cache
	def get_username(self, username: str):
		resp = self.session.get(f"https://api.github.com/users/{username}")
		if resp.status_code != 200:
			resp.raise_for_status()
			return

		r = resp.json()
		# Sometimes a display name is not set so we fallback to login name
		return r['name'] or r['login']
	
	def format_markdown(self, content: str, *, mode: str = "markdown", context: Optional[str]) -> str:
		data = {"text": content, "mode": mode}
		if context:
			data['context'] = context

		resp = self.session.post("https://api.github.com/markdown", json=data)
		if resp.status_code != 200:
			resp.raise_for_status()

		return resp.text


def process_from_folder(sourceFolder: pathlib.Path, ghToken: str, webhook_url: str) -> None:
	# Load app list json
	source: List[Tuple[str, Dict[str, Any]]] = []
	for item in sourceFolder.iterdir():
		with item.open(encoding="utf8") as f:
			source.append((str(item), json.load(f)))
	source.sort(key=lambda x: [x[1][key] for key in ["github", "gitlab", "title"] if key in x[1]][0])

	# Old data json
	oldData = None
	with open(DOCS_DIR.joinpath("data", "full.json"), "r", encoding="utf8") as file:
		oldData = json.load(file)

	output = []
	iconIndex = 1 if BG_IMAGE else 0
	github = GitHubAPI(token=ghToken)

	unistore = UniStore(
		"Universal-DB",
		"Universal-Team",
		"Universal-DB - An online database of 3DS and DS homebrew",
		"https://db.universal-team.net/unistore/universal-db.unistore",
		[f"https://db.universal-team.net/unistore/universal-db-{x}.t3x" for x in range(len(source) // ICONS_PER_SHEET + 1)],
		"https://db.universal-team.net/unistore/universal-db.tdx",
		"https://db.universal-team.net/unistore/universal-db-info.json",
		bool(BG_IMAGE)
	)

	# Fetch info for GitHub apps and output
	for i, (fp, app) in enumerate(source):
		doUpdate = True
		# Only update alternating halves of the list to save API hits
		# doUpdate = ((i % 2) == int((datetime.now().hour % 12) > 5))

		if PRIORITY_MODE or not doUpdate:
			old_app = get_matching_app(app, oldData)

			if old_app:
				doUpdate = was_recently_updated(old_app)  # If old data was found and was recently updated, check it again.
				if not doUpdate:
					app = old_app  # Rely on old data since we're not updating
			else:
				# This is a new app so fetch data for it.
				doUpdate = True

		webhook = discord.SyncWebhook.from_url(webhook_url) if webhook_url else None

		if doUpdate:
			try:
				app, iconIndex = process_app_entry(app, fp, iconIndex, github, oldData, webhook=webhook)
			except FetchAppDataError:
				continue
			except Exception as e:
				trace = format_traceback(e)
				if webhook:
					title = app['title'] if "title" in app else fp
					create_error_report(trace, title, webhook)

				click.secho(trace, fg="red")
				continue

		if "title" in app:
			app["slug"] = format_to_web_name(app["title"])
			click.echo(app["slug"])

			app["urls"] = []
			for sys in app["systems"]:
				app["urls"].append(f"https://db.universal-team.net/{sys.lower()}/{app['slug']}")

		# Add to output json
		output.append(app)

		# Create the website file
		create_web_file(app)

		if "unistore_exclude" not in app or not app["unistore_exclude"]:
			# Move links to end to be more readable in U-U
			notes = app["update_notes_md"] if "update_notes_md" in app else ""
			links = []

			def getLinkReplacement(match, links):
				linkNum = len(links)

				if match.group(2) in links:
					linkNum = links.index(match.group(2))
				else:
					links.append(match.group(2))

				return f"{match.group(1)}[{str(linkNum)}]"

			notes = re.sub(r"(\[.*?\])\((.*?)\)", lambda match: getLinkReplacement(match, links), notes)
			notes = re.sub(r"[0-9a-fA-F]{40}", lambda match: match.group(0)[:7], notes)

			if len(links) > 0:
				notes += "\n"

			for i, link in enumerate(links):
				notes += f"\n[{i}]: {link}"

			# Add entry for UniStore
			entry = StoreEntry(
				app["title"] if "title" in app else "",
				app["author"] if "author" in app else "",
				app["description"] if "description" in app else "",
				app["version"] if "version" in app else "",
				parser.parse(app["updated"]).strftime("%Y-%m-%d at %H:%M (UTC)") if "updated" in app else "",
				app["categories"] if "categories" in app else [],
				app["systems"].copy() if "systems" in app else [],
				[x for x in app["screenshots"] if x["url"].endswith(".png") and "horihd" not in x["url"]] if "screenshots" in app else [],
				notes,
				app["license"] if "license" in app else "",
				app["wiki"] if "wiki" in app else "",
				app["icon_index"] if "icon_index" in app else -1,
				app["color_bg"] if "color_bg" in app else app["color"] if "color" in app else "",
				app["stars"] if "stars" in app else 0,
				app["script_message"] if "script_message" in app else "",
				app["unique_ids"] if "unique_ids" in app else [],
				app["installed_files"] if "installed_files" in app else []
			)

			# Change "DS" to "NDS" so it can be searched for
			if "DS" in entry._entry["info"]["console"]:
				entry._entry["info"]["console"].remove("DS")
				entry._entry["info"]["console"].append("NDS")

			# If scripts are specified, use those instead of the release files
			if "scripts" in app:
				for script in app["scripts"]:
					entry.addScript(script, app["scripts"][script])

			# If autogen_scripts is forced or no scripts, generate scripts from downloads
			if "autogen_scripts" in app and app["autogen_scripts"] or "scripts" not in app:
				if "downloads" in app:
					for file in app["downloads"]:
						items, match = next(((app["archive"][x], re.findall(x, file)) for x in app["archive"] if re.findall(x, file)), (None, None)) if "archive" in app else (None, None)
						if items and match:
							items = {x.format(*match): [item.format(*match) for item in items[x]] for x in items}
						if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and items):
							if not items:
								items = {file: None}

							for item in items:
								sizeStr = to_friendly_bytes(app["downloads"][file]["size"]) if "size" in app["downloads"][file] else None
								entry.addDownloadScript(item, file, app["downloads"][file]["url"], items[item], sizeStr)

				if "prerelease" in app:
					for file in app["prerelease"]["downloads"]:
						items, match = next(((app["archive"][x], re.findall(x, file)) for x in app["archive"] if re.findall(x, file)), (None, None)) if "archive" in app else (None, None)
						if items and match:
							items = {x.format(*match): [item.format(*match) for item in items[x]] for x in items}
						if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and items):
							if not items:
								items = {file: None}

							for item in items:
								sizeStr = to_friendly_bytes(app["prerelease"]["downloads"][file]["size"]) if "size" in app["prerelease"]["downloads"][file] else None
								entry.addDownloadScript(item, file, app["prerelease"]["downloads"][file]["url"], items[item], sizeStr, "prerelease")

				if "nightly" in app:
					for file in app["nightly"]["downloads"]:
						items, match = next(((app["archive"][x], re.findall(x, file)) for x in app["archive"] if re.findall(x, file)), (None, None)) if "archive" in app else (None, None)
						if items and match:
							items = {x.format(*match): [item.format(*match) for item in items[x]] for x in items}
						if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and items):
							if not items:
								items = {file: None}

							for item in items:
								sizeStr = to_friendly_bytes(app["nightly"]["downloads"][file]["size"]) if "size" in app["nightly"]["downloads"][file] else None
								entry.addDownloadScript(item, file, app["nightly"]["downloads"][file]["url"], items[item], sizeStr, "nightly")

			if app["title"] == "RetroArch":
				entry._entry["info"]["description"] += "\n\nCores must be downloaded from their separate UniStore, which can be added in settings."
				if not PRIORITY_MODE:
					retroarchUniStore()

			unistore.append(entry)

		click.echo("=" * 80)

	if not PRIORITY_MODE:
		# Make tdx
		with open(DOCS_DIR.joinpath("unistore", "universal-db.tdx"), "wb") as tdx:
			img2tdx(("-gb -gB8 -gzl", *[f"{i}.png" for i in range(1 if BG_IMAGE else 0, iconIndex)]), tdx, imgPath=str(TEMP_DIR / "32"))

		# Make t3x(s)
		# They can actually fit a bit more than 400 icons,
		# but there's not a huge size cost to not 100% filling them
		# and this is safer
		sheetCount = iconIndex // ICONS_PER_SHEET + 1
		for sheet in range(sheetCount):
			with TEMP_DIR.joinpath("48", f"icons{sheet}.t3s").open("w", encoding="utf8") as file:
				file.write("--atlas -f rgba -z auto\n\n")

				if sheet == 0 and BG_IMAGE:
					file.write(BG_IMAGE + "\n")


				start = max(sheet * ICONS_PER_SHEET, 1 if BG_IMAGE else 0)
				end = min((sheet + 1) * ICONS_PER_SHEET, iconIndex)
				for i in range(start, end):
					file.write(f"{i}.png\n")
			infile = str(TEMP_DIR.joinpath("48", f"icons{sheet}.t3s"))
			outfile = str(DOCS_DIR.joinpath("unistore", f"universal-db-{sheet}.t3x"))
			system(f"tex3ds -i {infile} -o {outfile}")

	# Write UniStore and metadata
	unistore.save(DOCS_DIR.joinpath("unistore", "universal-db.unistore"), DOCS_DIR.joinpath("unistore", "universal-db-info.json"))

	# Write output file
	with DOCS_DIR.joinpath("data", "full.json").open("w", encoding="utf8") as file:
		json.dump(output, file, sort_keys=True, ensure_ascii=False)


def check_for_docs_dir(path: str) -> pathlib.Path:
	docs_path = pathlib.Path(path)
	exists = docs_path.exists()
	if not exists:
		docs_path = click.prompt(text="Unable to find the docs directory, please type a directory in.\nControl-C to cancel this!",
								 type=click.Path(exists=True, file_okay=False))
	
	return docs_path


@click.group()
def main_entry_group():
	# Prematurely make the temp directories, just in case.
	pth = TEMP_DIR
	if pth.exists() is False:
		pth.mkdir()

	if not pth.joinpath("48").exists():
		pth.joinpath("48").mkdir()
	if not pth.joinpath("32").exists():
		pth.joinpath("32").mkdir()

	click.help_option()


@main_entry_group.command(name="all")
@click.argument("source", default=str(SCRIPT_DIR / ("apps")), type=click.Path(exists=True, file_okay=False)) #  help="The folder to find apps in")
@click.argument("docs", default=str(SCRIPT_DIR.parent / "docs"), type=click.Path(file_okay=False)) #  help="The location to output documentation to")
@click.option("--background", "-b", type=click.Path(exists=True, resolve_path=True), help="Background image for UU")
@click.option("--github-token", "-t", help="A GitHub API token", envvar="TOKEN")
@click.option("--priority", "-p", is_flag=True, default=False, help="Skips apps that are not updated within the last 30 days")
@click.option("--error-webhook", "-er", type=str, envvar="WEBHOOK_URL", default=None)
def all_command(source: str, docs: str, background: str, github_token: str, priority: bool, error_webhook: str):
	"""Processes every app in a given directory"""
	docs_path = check_for_docs_dir(docs)
	global DOCS_DIR
	DOCS_DIR = docs_path
	source_path = pathlib.Path(source)

	global BG_IMAGE
	BG_IMAGE = background

	global PRIORITY_MODE
	PRIORITY_MODE = priority

	click.secho("Found the source directory and docs directory", fg='green')
	click.echo(f"Source: {source_path.resolve()}")
	click.echo(f"Docs: {docs_path.resolve()}")
	click.echo(f"Background image: {BG_IMAGE}")
	click.echo(f"Priority Mode: {PRIORITY_MODE}")
	process_from_folder(source_path, github_token, error_webhook)


@main_entry_group.command()
@click.argument("docs", default=str(SCRIPT_DIR.parent / "docs"), type=click.Path(file_okay=False))
def gen_retroarch(docs):
	"""Generates the RetroArch Unistore ONLY"""
	docs_path = check_for_docs_dir(docs)
	global DOCS_DIR
	DOCS_DIR = docs_path

	retroarchUniStore()


@main_entry_group.command()
@click.argument("apps", type=click.File(mode="r"), nargs=-1)
@click.option("--github-token", help="A GitHub API token", envvar="TOKEN")
@click.option("--docs", default=str(SCRIPT_DIR.parent / "docs"), type=click.Path(file_okay=False))
def app_test(apps: TextIO, github_token: Optional[str], docs: str):
	"""Tests individual apps if it is fetchable and workable with for UDB"""
	api = GitHubAPI(token=github_token)
	docs_path = check_for_docs_dir(docs)
	global DOCS_DIR
	DOCS_DIR = docs_path

	if len(apps) < 1:
		click.echo("Please specifiy at least one app")
		exit(1)

	for app in apps:
		content = json.loads(app.read())

		entry = process_app_entry(content, app.name, 0, api, {})
		if not entry:
			click.echo("Unable to process the app!")
			exit(1)
			return

		click.echo(json.dumps(entry[0], indent=4))

if __name__ == "__main__":
	main_entry_group()
