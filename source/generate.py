#!/usr/bin/env python3

import json
import numpy
import qrcode
import re
import requests
import yaml

from argparse import ArgumentParser, FileType
from bs4 import BeautifulSoup
from colorsys import hsv_to_rgb, rgb_to_hsv
from datetime import datetime, timezone
from dateutil import parser
from img2tdx import img2tdx
from io import BytesIO
from markdownify import markdownify
from os import listdir, makedirs, path, system
from PIL import Image, ImageDraw
from PIL.PngImagePlugin import PngImageFile
from requests.utils import requote_uri
from shutil import copyfile
from textwrap import shorten
from typing import Tuple
from unidecode import unidecode
from unistore import StoreEntry, UniStore

DOWNLOAD_BLACKLIST = r"(\.3ds$|\.apk|\.appimage|\.dmg|\.exe|\.ipa|\.love|\.nro|\.opk|\.pkg|\.smdh|\.vpk|\.xz|armhf|elf|linux|macos|osx|PS3|PSP|switch|ubuntu|vita|wii|win|x86_64|xbox)"


def webName(name: str) -> str:
	"""Convert names to lowercase alphanumeric, underscore, and hyphen"""

	name = unidecode(name).lower()
	out = ""
	for letter in name:
		if letter in "abcdefghijklmnopqrstuvwxyz0123456789-_":
			out += letter
		elif letter in ". ":
			out += "-"
	return out


def byteCount(bytes: int) -> str:
	"""Converts an int number of bytes to a str with the largest appropriate unit"""

	if bytes == 1:
		return "1 Byte"
	elif bytes < (1 << 10):
		return f"{bytes} Bytes"
	elif bytes < (1 << 20):
		return f"{bytes // (1 << 10)} KiB"
	elif bytes < (1 << 30):
		return f"{bytes // (1 << 20)} MiB"
	else:
		return f"{bytes // (1 << 30)} GiB"


def saveIcon(img: Image, tempDir: str, index: int, ds: bool) -> Tuple[PngImageFile, str]:
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
	img.save(path.join(tempDir, "48", f"{index}.png"))

	if ds:
		imgDS = img.copy()
		imgDS.thumbnail((32, 32))
		data = numpy.array(imgDS)
		r, g, b, a = data.T
		transparent = a < 0xFF
		data[...][transparent.T] = (0xFF, 0, 0xFF, 0xFF)
		imgDS = Image.fromarray(data)
		imgDS = imgDS.quantize()
		imgDS.save(path.join(tempDir, "32", f"{index}.png"))

	color = img.copy()
	color.thumbnail((1, 1))
	color = color.getpixel((0, 0))
	return img, f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def retroarchUniStore(docsDir: str, tempDir: str) -> None:
	"""Generates the RetroArch Cores UniStore"""

	print("Generating RetroArch UniStore")

	if not path.exists(path.join(tempDir, "ra", "48")):
		makedirs(path.join(tempDir, "ra", "48"))

	unistoreRA = UniStore(
		"RetroArch Cores",
		"Libretro",
		"RetroArch cores",
		"https://db.universal-team.net/unistore/retroarch.unistore",
		"https://db.universal-team.net/unistore/retroarch.t3x"
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
			saveIcon(Image.open(BytesIO(img.content)), path.join(tempDir, "ra"), iconIndexRA, False)

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
			consoles=["3ds"],
			releaseNotes=notes,
			license=info["license"] if "license" in info else "",
			iconIndex=iconIndexRA if img.status_code == 200 else -1
		)

		entry.addDownloadScript(f"{name}.3dsx", f"{name}.zip", href, archive=(f"{name}.3dsx",))
		entry.addDownloadScript(f"{name}.cia", f"{name}.zip", href.replace("3dsx", "cia"), archive=(f"{name}.cia",), retroarch=True)

		unistoreRA.append(entry)

	# Make t3x
	with open(path.join(tempDir, "ra", "48", "icons.t3s"), "w", encoding="utf8") as file:
		file.write("--atlas -f rgba -z auto\n\n")
		for i in range(iconIndexRA):
			file.write(f"{i}.png\n")
	system(f"tex3ds -i {path.join(tempDir, 'ra', '48', 'icons.t3s')} -o {path.join(docsDir, 'unistore', 'retroarch.t3x')}")

	unistoreRA.save(path.join(docsDir, "unistore", "retroarch.unistore"))


def main(sourceFolder, docsDir: str, ghToken: str, priorityOnlyMode: bool) -> None:
	# Load app list json
	source = []
	for item in listdir(sourceFolder):
		with open(path.join(sourceFolder, item), encoding="utf8") as f:
			source.append(json.load(f))

	# Old data json
	oldData = None
	with open(path.join(docsDir, "data", "full.json"), "r", encoding="utf8") as file:
		oldData = json.load(file)

	output = []
	iconIndex = 0
	names = {}  # GitHub name cache
	tempDir = path.join(path.dirname(sourceFolder), "temp")

	# Create headers and a session for github specific requests
	github_headers = {"Accept": "application/vnd.github+json",
					  "X-GitHub-Api-Version": "2022-11-28"}
	if ghToken:
		github_headers["Authorization"] = f"Bearer {ghToken}"

	gh_req = requests.Session()
	gh_req.headers.update(github_headers)

	unistore = UniStore(
		"Universal-DB",
		"Universal-Team",
		"Universal-DB - An online database of 3DS and DS homebrew",
		"https://db.universal-team.net/unistore/universal-db.unistore",
		"https://db.universal-team.net/unistore/universal-db.t3x",
		"https://db.universal-team.net/unistore/universal-db.tdx",
		"https://db.universal-team.net/unistore/universal-db-info.json"
	)

	# Fetch info for GitHub apps and output
	for i, app in enumerate(source):
		doUpdate = True
		# Only update alternating halves of the list to save API hits
		# doUpdate = ((i % 2) == int((datetime.now().hour % 12) > 5))

		if priorityOnlyMode or not doUpdate:
			temp = list(filter(lambda x: "github" in x and "github" in app and x["github"] == app["github"], oldData))
			if len(temp) == 0:
				temp = list(filter(lambda x: "gbatemp" in x and "gbatemp" in app and x["gbatemp"] == app["gbatemp"], oldData))
			if len(temp) == 0:
				temp = list(filter(lambda x: "bitbucket" in x and "bitbucket" in app and x["bitbucket"]["repo"] == app["bitbucket"]["repo"], oldData))
			if len(temp) == 0:
				temp = list(filter(lambda x: "title" in x and "author" in x and "title" in app and "author" in app and x["title"] == app["title"] and x["author"] == app["author"], oldData))
			if len(temp) == 0:
				temp = list(filter(lambda x: "gitlab" in x and "gitlab" in app and x["gitlab"] == app["gitlab"], oldData))

			# Always treat apps that updated in the last 30 days as priority
			if len(temp) > 0:
				daysSinceUpdate = 1000
				if "updated" in temp[0]:
					daysSinceUpdate = (datetime.now(tz=timezone.utc) - parser.parse(temp[0]["updated"])).days

				doUpdate = daysSinceUpdate <= 30
				if not doUpdate:
					app = temp[0]
			else:
				doUpdate = True

		if doUpdate:
			app["stars"] = 0

			if "gbatemp" in app:
				print("GBAtemp Download Center")
				r = requests.get(f"https://gbatemp.net/download/{app['gbatemp']}/")
				if r.status_code != 200:
					print(f"Error {r.status_code:d}, using old data!")
					app = list(filter(lambda x: "gbatemp" in x and x["gbatemp"] == app["gbatemp"], oldData))[0]
				else:
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
										app["downloads"][name]["size_str"] = byteCount(app["downloads"][name]["size"])

			if "github" in app:
				print("GitHub --", app["github"])
				api = gh_req.get(f"https://api.github.com/repos/{app['github']}").json()
				assert "message" not in api, app["github"] + " API Error: " + api["message"]
				releases = gh_req.get(f"https://api.github.com/repos/{app['github']}/releases").json()
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
					release = gh_req.get(f"https://api.github.com/repos/{app['github']}/releases/latest").json()
					if "message" in release and release["message"] == "Not Found":
						release = None

				if "title" not in app:
					app["title"] = api["name"]

				if "author" not in app:
					username = api["owner"]["login"]
					if username in names:
						username = names[username]
					else:
						user = gh_req.get(f"https://api.github.com/users/{username}").json()
						assert "message" not in user, app["github"] + " API Error: " + user["message"]
						names[username] = user["name"] if user["name"] is not None else username
						username = names[username]
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
						app["update_notes"] = gh_req.post("https://api.github.com/markdown", json={"text": release["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text
						app["update_notes"] = re.sub(r'<a target="_blank" rel="noopener noreferrer" href="https:\/\/private-user-images.githubusercontent\.com.*?<\/a>', "", app["update_notes"])

					if "updated" not in app:
						app["updated"] = release["published_at"]

					if "downloads" not in app:
						app["downloads"] = {}
					for asset in release["assets"]:
						if not asset["name"] in app["downloads"] and (len(re.findall(app["download_filter"], asset["name"])) > 0 if "download_filter" in app else len(re.findall(DOWNLOAD_BLACKLIST, asset["name"])) == 0):
							app["downloads"][asset["name"]] = {
								"url": asset["browser_download_url"],
								"size": asset["size"],
								"size_str": byteCount(asset["size"])
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
								"size_str": byteCount(asset["size"])
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
							app["prerelease"]["update_notes"] = gh_req.post("https://api.github.com/markdown", json={"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text
							app["prerelease"]["update_notes"] = re.sub(r'<a target="_blank" rel="noopener noreferrer" href="https:\/\/private-user-images.githubusercontent\.com.*?<\/a>', "", app["prerelease"]["update_notes"])

							if "update_notes" not in app:
								app["update_notes_md"] = app["prerelease"]["update_notes_md"]
								app["update_notes"] = app["prerelease"]["update_notes"]

						if "updated" not in app:
							app["updated"] = prerelease["published_at"]
						if "updated" not in app["prerelease"]:
							app["prerelease"]["updated"] = prerelease["published_at"]
					else:
						app.pop("prerelease")

			if "bitbucket" in app:
				print("Bitbucket --", app["bitbucket"]["repo"])
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
								"size_str": byteCount(fileAPI["size"])
							}

						if "download_page" not in app:
							app["download_page"] = f"https://bitbucket.org/{app['bitbucket']['repo']}/src/{(app['bitbucket']['branch'] if 'branch' in app['bitbucket'] else 'master')}/{download}"

						if "version" not in app:
							app["version"] = fileAPI["commit"]["hash"][:7]

						if "updated" not in app:
							commit = requests.get(fileAPI["commit"]["links"]["self"]["href"]).json()
							app["updated"] = commit["date"]

			if "gitlab" in app:
				print("Gitlab --", app["gitlab"])
				gitlab_id = app["gitlab"].replace('/', '%2F')
				endpoint = app["gitlab_endpoint"] if "gitlab_endpoint" in app else "https://gitlab.com"
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
						app["update_notes"] = release["description_html"].replace("\r\n", "\n")

					if "updated" not in app:
						app["updated"] = release["released_at"]

					if "downloads" not in app:
						app["downloads"] = {}
					for asset in release["assets"]["links"]:
						if not asset["name"] in app["downloads"] and (len(re.findall(app["download_filter"], asset["name"])) > 0 if "download_filter" in app else len(re.findall(DOWNLOAD_BLACKLIST, asset["name"])) == 0):
							app["downloads"][asset["name"]] = {
								"url": asset["direct_asset_url"]
							}


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
						app["update_notes"] = gh_req.post("https://api.github.com/markdown", json={"text": app["update_notes_md"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

			# If no markdown notes, generate from HTML
			if "update_notes_md" not in app and "update_notes" in app:
				app["update_notes_md"] = markdownify(app["update_notes"], bullets="-")

			# Ensure URLs don't have spaces
			for item in ["avatar", "download_page", "icon", "image", "source", "website", "wiki"]:
				if item in app:
					app[item] = requote_uri(app[item])

			# Check for screenshots
			if path.exists(path.join(docsDir, "assets", "images", "screenshots", webName(app["title"]))):
				if "screenshots" not in app:
					app["screenshots"] = []
				dirlist = listdir(path.join(docsDir, "assets", "images", "screenshots", webName(app["title"])))
				dirlist.sort()
				for screenshot in dirlist:
					if screenshot[-3:] in ["png", "gif", "jpg", "peg", "iff", "bmp"]:
						app["screenshots"].append({
							"url": f"https://db.universal-team.net/assets/images/screenshots/{webName(app['title'])}/{screenshot}",
							"description": screenshot[:screenshot.rfind(".")].capitalize().replace("-", " ")
						})

			# Format update notes with GitHub's API
			if "update_notes_md" in app and "update_notes" not in app:
				app["update_notes"] = gh_req.post("https://api.github.com/markdown", json={"text": app["update_notes_md"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

			# Get missing download sizes
			if "downloads" in app:
				for download in app["downloads"]:
					if "size" not in app["downloads"][download]:
						if app["downloads"][download]["url"][:30] == "https://db.universal-team.net/":
							app["downloads"][download]["size"] = path.getsize(path.join(docsDir, app['downloads'][download]['url'][30:]))
							app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])
						else:
							r = requests.head(app["downloads"][download]["url"], allow_redirects=True)
							if r.status_code == 200 and "Content-Length" in r.headers:
								app["downloads"][download]["size"] = int(r.headers["Content-Length"])
								app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])

			# Check for local icon / image
			for ext in (".png", ".gif"):
				if "icon" not in app and path.exists(path.join(docsDir, "assets", "images", "icons", webName(app['title']) + ext)):
					app["icon"] = f"https://db.universal-team.net/assets/images/icons/{webName(app['title'])}{ext}"

			if "image" not in app and path.exists(path.join(docsDir, "assets", "images", "images", f"{webName(app['title'])}.png")):
				app["image"] = f"https://db.universal-team.net/assets/images/images/{webName(app['title'])}.png"
			elif "image" not in app and "icon" in app:
				app["image"] = app["icon"]
			elif "image" not in app and "avatar" in app:
				app["image"] = app["avatar"]
				if "github" in app["image"]:
					app["image"] += "&size=128"

			# Get image size
			if "image_length" not in app and "image" in app:
				if app["image"][:30] == "https://db.universal-team.net/":
					app["image_length"] = path.getsize(path.join(docsDir, app["image"][30:]))
				else:
					r = requests.head(app["image"], allow_redirects=True)
					if r.status_code == 200 and "Content-Length" in r.headers:
						app["image_length"] = int(r.headers["Content-Length"])

			# Make icon for UniStore and QR
			img = None
			if "icon" in app or "image" in app or "icon_static" in app:
				if not path.exists(path.join(tempDir, "48")):
					makedirs(path.join(tempDir, "48"))
				if not path.exists(path.join(tempDir, "32")):
					makedirs(path.join(tempDir, "32"))

				url = app["icon_static"] if "icon_static" in app else (app["icon"] if "icon" in app else app["image"] if "image" in app else "")
				file = None
				if url[:30] == "https://db.universal-team.net/":
					file = open(path.join(docsDir, url[30:]), "rb")
				else:
					r = requests.get(url)
					if r.status_code == 200:
						file = BytesIO(r.content)
					else:
						print(f"Error {r.status_code} downloading image!")

				if file:
					if priorityOnlyMode:
						old = next((item for item in oldData if item["title"] == app["title"]), {"icon_index": -1})
						app["icon_index"] = old["icon_index"] if "icon_index" in old else -1
					else:
						app["icon_index"] = iconIndex

					with Image.open(file) as img:
						img, color = saveIcon(img, tempDir, iconIndex, True)
						if "color" not in app:
							app["color"] = color
						if "color_bg" not in app:
							# Darken color to a maximum of 50% brightness
							hsv = list(rgb_to_hsv(*[int(x, 16) / 255 for x in re.findall("#(..)(..)(..)", color)[0]]))
							hsv[2] = min(0.5, hsv[2])
							app["color_bg"] = "#%02x%02x%02x" % (*[round(x * 255) for x in hsv_to_rgb(*hsv)],)

					if "icon" in app and app["icon"].endswith(".bmp"):
						copyfile(path.join(tempDir, "48", f"{iconIndex}.png"), path.join(docsDir, "assets", "images", "icons", f"{webName(app['title'])}.png"))
						app["icon"] = f"https://db.universal-team.net/assets/images/icons/{webName(app['title'])}.png"
					elif "icon_static" not in app and "icon" in app and app["icon"].endswith(".gif"):
						copyfile(path.join(tempDir, "48", f"{iconIndex}.png"), path.join(docsDir, "assets", "images", "icons", f"{webName(app['title'])}.png"))
						app["icon_static"] = f"https://db.universal-team.net/assets/images/icons/{webName(app['title'])}.png"

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
						qr.save(path.join(docsDir, "assets", "images", "qr", f"{webName(item)}.png"))
						if "qr" not in app:
							app["qr"] = {}
						app["qr"][item] = f"https://db.universal-team.net/assets/images/qr/{webName(item)}.png"

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
						qr.save(path.join(docsDir, "assets", "images", "qr", "prerelease", f"{webName(item)}.png"))
						if "qr" not in app["prerelease"]:
							app["prerelease"]["qr"] = {}
						app["prerelease"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/prerelease/{webName(item)}.png"

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
						qr.save(path.join(docsDir, "assets", "images", "qr", "nightly", f"{webName(item)}.png"))
						if "qr" not in app["nightly"]:
							app["nightly"]["qr"] = {}
						app["nightly"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/nightly/{webName(item)}.png"

		if "title" in app:
			app["slug"] = webName(app["title"])
			print(app["slug"])

			app["urls"] = []
			for sys in app["systems"]:
				app["urls"].append(f"https://db.universal-team.net/{sys.lower()}/{app['slug']}")

		# Add to output json
		output.append(app)

		# Website file
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
		# Add defaults where absolutely needed
		if "systems" not in web:
			web["systems"] = ["3DS"]  # default to 3DS
		if "updated" not in web:
			web["updated"] = "---"
		for sys in web["systems"]:
			if "title" in web:
				with open(path.join(docsDir, f"_{webName(sys)}", f"{webName(web['title'])}.md"), "w", encoding="utf8") as file:
					file.write(f"---\n{yaml.dump(web, sort_keys=True, allow_unicode=True)}---\n")
					if "long_description" in app:
						file.write(app["long_description"])

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
				app["icon_index"] if "icon_index" in app else -1
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
								scriptMessage = app["script_message"] if "script_message" in app else None
								sizeStr = byteCount(app["downloads"][file]["size"]) if "size" in app["downloads"][file] else None
								entry.addDownloadScript(item, file, app["downloads"][file]["url"], scriptMessage, items[item], sizeStr)

				if "prerelease" in app:
					for file in app["prerelease"]["downloads"]:
						items, match = next(((app["archive"][x], re.findall(x, file)) for x in app["archive"] if re.findall(x, file)), (None, None)) if "archive" in app else (None, None)
						if items and match:
							items = {x.format(*match): [item.format(*match) for item in items[x]] for x in items}
						if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and items):
							if not items:
								items = {file: None}

							for item in items:
								scriptMessage = app["script_message"] if "script_message" in app else None
								sizeStr = byteCount(app["prerelease"]["downloads"][file]["size"]) if "size" in app["prerelease"]["downloads"][file] else None
								entry.addDownloadScript(item, file, app["prerelease"]["downloads"][file]["url"], scriptMessage, items[item], sizeStr, "prerelease")

				if "nightly" in app:
					for file in app["nightly"]["downloads"]:
						items, match = next(((app["archive"][x], re.findall(x, file)) for x in app["archive"] if re.findall(x, file)), (None, None)) if "archive" in app else (None, None)
						if items and match:
							items = {x.format(*match): [item.format(*match) for item in items[x]] for x in items}
						if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and items):
							if not items:
								items = {file: None}

							for item in items:
								scriptMessage = app["script_message"] if "script_message" in app else None
								sizeStr = byteCount(app["nightly"]["downloads"][file]["size"]) if "size" in app["nightly"]["downloads"][file] else None
								entry.addDownloadScript(item, file, app["nightly"]["downloads"][file]["url"], scriptMessage, items[item], sizeStr, "nightly")

			if app["title"] == "RetroArch":
				entry._entry["info"]["description"] += "\n\nCores must be downloaded from their separate UniStore, which can be added in settings."
				if not priorityOnlyMode:
					retroarchUniStore(docsDir, tempDir)

			unistore.append(entry)

		print("=" * 80)

	if not priorityOnlyMode:
		# Make tdx
		with open(path.join(docsDir, "unistore", "universal-db.tdx"), "wb") as tdx:
			img2tdx(("-gb -gB8 -gzl", *[f"{i}.png" for i in range(iconIndex)]), tdx, imgPath=path.join(tempDir, "32"))

		# Make t3x
		with open(path.join(tempDir, "48", "icons.t3s"), "w", encoding="utf8") as file:
			file.write("--atlas -f rgba -z auto\n\n")
			for i in range(iconIndex):
				file.write(f"{i}.png\n")
		system(f"tex3ds -i {path.join(tempDir, '48', 'icons.t3s')} -o {path.join(docsDir, 'unistore', 'universal-db.t3x')}")

	# Write UniStore and metadata
	unistore.save(path.join(docsDir, "unistore", "universal-db.unistore"), path.join(docsDir, "unistore", "universal-db-info.json"))

	# Write output file
	with open(path.join(docsDir, "data", "full.json"), "w", encoding="utf8") as file:
		json.dump(output, file, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
	argParser = ArgumentParser(description="Generates the Universal-DB website and UniStores from a JSON")
	argParser.add_argument("source", metavar="apps", type=str, help="source JSON folder")
	argParser.add_argument("docs", metavar="../docs", type=str, help="location to output to")
	argParser.add_argument("--token", "-t", type=str, help="GitHub API token (to get around rate limit")
	argParser.add_argument("--priority", "-p", action="store_true", help="skips all apps not marked priority/updated within 30 days")

	args = argParser.parse_args()

	main(args.source, args.docs, args.token, args.priority)
