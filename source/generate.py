#!/usr/bin/env python3

from bs4 import BeautifulSoup
from dateutil import parser
import io
import json
from markdownify import markdownify
import numpy
import os
from PIL import Image, ImageDraw
import qrcode
import re
import requests
from shutil import copyfile
import sys
import yaml

# No py 2
if(sys.version_info.major != 3):
	print("This is Python %d!\nPlease use Python 3!" % sys.version_info.major)
	exit()

# Convert names to lowercase alphanumeric + underscore and hyphen
def webName(name):
	name = name.lower()
	out = ""
	for letter in name:
		if letter in "abcdefghijklmnopqrstuvwxyz0123456789-_":
			out += letter
		elif letter in ". ":
			out += "-"
	return out

def ucs2Name(string):
	return "".join(list(filter(lambda c: ord(c) < 0xFFFF, string))).strip()

# Convert names to lowercase alphanumeric + underscore and hyphen
def byteCount(bytes):
	if(type(bytes) != int):
		bytes = int(bytes)

	if bytes == 1:
		return "%d Byte" % bytes
	elif bytes < (1 << 10):
		return "%d Bytes" % bytes
	elif bytes < (1 << 20):
		return "%d KiB" % (bytes // (1 << 10))
	elif bytes < (1 << 30):
		return "%d MiB" % (bytes // (1 << 20))
	else:
		return "%d GiB" % (bytes // (1 << 30))

def downloadScript(file, url, message, archive):
	script = []
	archiveItem = [item for item in archive if re.findall(item, file)] if archive else None
	if archive and len(archiveItem) > 0:
		script = [
			{
				"type": "downloadFile",
				"file": url,
				"output": f"/{file}",
				"message": f"Downloading {file}..."
			}
		]
		
		for item in archive[archiveItem[0]]:
			if item[item.rfind(".") + 1:].lower() == "3dsx":
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"%3DSX%/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {item[item.rfind('/') + 1:]}..."
				})
			elif item[item.rfind(".") + 1:].lower() in ["nds", "dsi"]:
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"%NDS%/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {file}..."
				})
			elif item[item.rfind(".") + 1:].lower() == "cia":
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {file}..."
				})

				script.append({
					"type": "installCia",
					"file": f"/{item}",
					"message": f"Installing {item}..."
				})

				script.append({
					"type": "deleteFile",
					"file": f"/{item}",
					"message": f"Deleting {item}..."
				})
			elif item == "boot.firm":
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {item[item.rfind('/') + 1:]}..."
				})
			elif item[item.rfind(".") + 1:].lower() == "firm":
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"%FIRM%/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {item[item.rfind('/') + 1:]}..."
				})
			else:
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"/{item}",
					"message": f"Extracting {item}..."
				})

		script.append({
			"type": "deleteFile",
			"file": f"/{file}",
			"message": f"Deleting {file}..."
		})
	else:
		if file[file.rfind(".") + 1:].lower() == "3dsx":
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"%3DSX%/{file}",
					"message": f"Downloading {file}..."
				}
			]
		elif file[file.rfind(".") + 1:].lower() in ["nds", "dsi"]:
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"%NDS%/{file}",
					"message": f"Downloading {file}..."
				}
			]
		elif file[file.rfind(".") + 1:].lower() == "cia":
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"/{file}",
					"message": f"Downloading {file}..."
				},
				{
					"type": "installCia",
					"file": f"/{file}",
					"message": f"Installing {file}..."
				},
				{
					"type": "deleteFile",
					"file": f"/{file}",
					"message": f"Deleting {file}..."
				}
			]
		elif file == "boot.firm":
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"/{file}",
					"message": f"Downloading {file}..."
				}
			]
		elif file[file.rfind(".") + 1:].lower() == "firm":
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"%FIRM%/{file}",
					"message": f"Downloading {file}..."
				}
			]
		elif file[file.rfind(".") + 1:].lower() in ["zip", "7z", "rar"]:
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"/{file}",
					"message": f"Downloading {file}..."
				},
				{
					"type": "extractFile",
					"file": f"/{file}",
					"input": "",
					"output": f"%ARCHIVE_DEFAULT%/{file[0:file.find('.')]}/",
					"message": f"Extracting {file}..."
				},
				{
					"type": "deleteFile",
					"file": f"/{file}",
					"message": f"Deleting {file}..."
				}
			]
		else:
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"/{file}",
					"message": f"Downloading {file}..."
				}
			]

	if message:
		if type(message) == str:
			script.append({
				"type": "promptMessage",
				"message": message
			})
		elif type(message) == dict and len(re.findall(message["for"], file)) > 0:
			msg = {
				"type": "promptMessage",
				"message": message["message"],
				"count": message["count"] if "count" in message else 0
			}
			if message["at"] == "end":
				script.append(msg)
			else:
				script.insert(0, msg)

	return script

def retroarch(icon_index):
	print("Generating RetroArch UniStore")

	retroarchOld = None
	if os.path.exists(os.path.join("..", "docs", "unistore", "retroarch.unistore")):
		with open(os.path.join("..", "docs", "unistore", "retroarch.unistore"), "r", encoding="utf8") as file:
			retroarchOld = json.load(file)

	retroarch = {
		"storeInfo": {
			"title": "RetroArch Cores",
			"author": "Libretro",
			"url": "https://github.com/Universal-Team/db/raw/master/docs/unistore/retroarch.unistore",
			"file": "retroarch.unistore",
			"sheetURL": "https://github.com/Universal-Team/db/raw/master/docs/unistore/universal-db.t3x",
			"sheet": "universal-db.t3x",
			"dsSheetURL": "https://github.com/Universal-Team/db/raw/master/docs/unistore/universal-db.tdx",
			"dsSheet": "universal-db.tdx",
			"description": "RetroArch cores",
			"version": 3,
			"revision": retroarchOld["storeInfo"]["revision"] if retroarchOld else 0
		},
		"storeContent": [],
	}

	r = requests.get("https://buildbot.libretro.com/nightly/nintendo/3ds/latest/3dsx/")
	soup = BeautifulSoup(r.text, "html.parser")
	for a in soup.find_all("a"):
		if a["href"].startswith("/nightly/nintendo/3ds/latest/"):
			name = re.findall(r"3dsx/(.*)\.3dsx", a["href"])[0]
			retroarch["storeContent"].append({
				"info": {
					"title": ucs2Name(name),
					"version": "nightly",
					"author": "libretro",
					"category": ["emulator"],
					"console": ["3ds"],
					"icon_index": icon_index,
					"description": "",
					"releasenotes": "",
					"screenshots": [],
					"license": "gpl-3.0",
					"wiki": ""
				},
				f"{name}.3dsx": downloadScript(f"{name}.zip", "https://buildbot.libretro.com" + a["href"], None, {f"{name}.zip": [f"{name}.3dsx"]}),
				f"{name}.cia": downloadScript(f"{name}.zip", "https://buildbot.libretro.com" + a["href"].replace("3dsx", "cia"), None, {f"{name}.zip": [f"{name}.cia"]}),
			})

	# Increment revision if not the same
	if retroarch != retroarchOld:
		retroarch["storeInfo"]["revision"] += 1

	# Write unistore to file
	with open(os.path.join("..", "docs", "unistore", "retroarch.unistore"), "w", encoding="utf8") as file:
		file.write(json.dumps(retroarch, sort_keys=True, ensure_ascii=False))

# Read json
with open("source.json", "r", encoding="utf8") as file:
	source = json.load(file)

# Read version from old unistore
with open(os.path.join("..", "docs", "unistore", "universal-db.unistore"), "r", encoding="utf8") as file:
	unistoreOld = json.load(file)

# Create UniStore base
unistore = {
	"storeInfo": {
		"title": "Universal-DB",
		"author": "Universal-Team",
		"url": "https://github.com/Universal-Team/db/raw/master/docs/unistore/universal-db.unistore",
		"file": "universal-db.unistore",
		"sheetURL": "https://github.com/Universal-Team/db/raw/master/docs/unistore/universal-db.t3x",
		"sheet": "universal-db.t3x",
		"dsSheetURL": "https://github.com/Universal-Team/db/raw/master/docs/unistore/universal-db.tdx",
		"dsSheet": "universal-db.tdx",
		"description": "Universal-DB - An online database of 3DS and DS homebrew",
		"version": 3,
		"revision": 0 if "revision" not in unistoreOld["storeInfo"] else unistoreOld["storeInfo"]["revision"]
	},
	"storeContent": [],
}

# Output json
output = []

# Old data json
oldData = None

with open(os.path.join("..", "docs", "data", "full.json"), "r", encoding="utf8") as file:
	oldData = json.load(file)

# Icon count
iconIndex = 0

# GitHub name cache
names = {}

# Auth header
header = None
if len(sys.argv) > 1:
	header = {"Authorization": f"token {sys.argv[1]}"}

priorityOnlyMode = len(sys.argv) > 2 and sys.argv[2] == "priority"

# Fetch info for GitHub apps and output
for app in source:
	foundExisting = False
	if priorityOnlyMode and not ("priority" in app and app["priority"]):
		temp = list(filter(lambda x: "github" in x and "github" in app and x["github"] == app["github"], oldData))
		if len(temp) == 0:
			temp = list(filter(lambda x: "bitbucket" in x and "bitbucket" in app and x["bitbucket"]["repo"] == app["bitbucket"]["repo"], oldData))
		if len(temp) == 0:
			temp = list(filter(lambda x: "title" in x and "author" in x and "title" in app and "author" in app and x["title"] == app["title"] and x["author"] == app["author"], oldData))

		if len(temp) > 0:
			foundExisting = True
			app = temp[0]
	if not foundExisting or not (priorityOnlyMode and not ("priority" in app and app["priority"])):
		if "gbatemp" in app:
			print("GBAtemp Download Center")
			r = requests.get(f"https://gbatemp.net/download/{app['gbatemp']}/")
			if r.status_code != 200:
				print(f"Error {r.status_code:d}, using old data!")
				app = list(filter(lambda x: "gbatemp" in x and x["gbatemp"] == app["gbatemp"], oldData))[0]
			else:
				soup = BeautifulSoup(r.text, "html.parser")

				if "title" not in app:
					app["title"] = soup.find(class_="resourceInfo").h1.find(text=True).strip()

				if "author" not in app:
					app["author"] = soup.find(class_="author").dd.a.text.strip()

				if "description" not in app:
					app["description"] = soup.find(class_="tagLine").text.strip()

				if "long_description" not in app:
					app["long_description"] = soup.blockquote.decode_contents().strip()

				if "avatar" not in app:
					app["avatar"] = "https://gbatemp.net/" + re.sub("/s/", "/l/", soup.find(class_="resourceImage").a.img["src"]).strip()

				if "created" not in app:
					dd = soup.find(class_="firstRelease").dd
					if dd.span:
						app["created"] = parser.parse(dd.span["title"]).strftime("%Y-%m-%dT%H:%M:%SZ")
					else: # Being shown as "Today at ..." or so
						app["created"] = parser.parse(dd.appr.text).strftime("%Y-%m-%dT%H:%M:%SZ")

				if "download_page" not in app:
					app["download_page"] = f"https://gbatemp.net/download/{app['gbatemp']}/"

				if "version" not in app:
					app["version"] = soup.find(class_="resourceInfo").h1.span.text.strip()

				if "version_title" not in app:
					app["version_title"] = soup.find(class_="updates").ol.li.a.text.strip()

				if "update_notes" not in app or "update_notes_md" not in app:
					if "update_notes" not in app:
						notesSoup = BeautifulSoup(requests.get("https://gbatemp.net/" + soup.find(class_="updates").ol.li.a["href"]).text, "html.parser")
						app["update_notes"] = notesSoup.blockquote.decode_contents().strip()

					if "update_notes_md" not in app:
						app["update_notes_md"] = markdownify(app["update_notes"], bullets="-")

				if "updated" not in app:
					dd = soup.find(class_="lastUpdate").dd
					if dd.span:
						app["updated"] = parser.parse(dd.span["title"]).strftime("%Y-%m-%dT%H:%M:%SZ")
					else: # Being shown as "Today at ..." or so
						app["updated"] = parser.parse(dd.abbr.text).strftime("%Y-%m-%dT%H:%M:%SZ")

				if "downloads" not in app:
					app["downloads"] = {}

				head = requests.head("https://gbatemp.net/" + soup.find(class_="downloadButton").a["href"])
				if head.status_code == 200:
					if "Content-Disposition" in head.headers:
						name = re.findall('filename="(.*)"', head.headers["Content-Disposition"])
						if len(name) > 0:
							name = name[0]
							size = None
							if name not in app["downloads"]:
								app["downloads"][name] = {
									"url": head.url,
								}

								if "Content-Length" in head.headers:
									app["downloads"][name]["size"] = int(head.headers["Content-Length"])
									app["downloads"][name]["size_str"] = byteCount(app["downloads"][name]["size"])

		if "github" in app:
			print("GitHub")
			api = requests.get(f"https://api.github.com/repos/{app['github']}", headers=header if header else None).json()
			releases = requests.get(f"https://api.github.com/repos/{app['github']}/releases", headers=header if header else None).json()
			release = None
			prerelease = None
			if len(releases) > 0 and releases[0]["prerelease"]:
				prerelease = releases[0]
			for r in releases:
				if not (r["prerelease"] or r["draft"]):
					release = r
					break

			if "title" not in app:
				app["title"] = api["name"]

			if "author" not in app:
				username = api["owner"]["login"]
				if username in names:
					username = names[username]
				else:
					user = requests.get(f"https://api.github.com/users/{username}", headers=header if header else None).json()
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

			if "wiki" not in app and api["has_wiki"] and requests.get(f"https://raw.githubusercontent.com/wiki/{app['github']}/Home.md").status_code != 404:
				app["wiki"] = f"{api['html_url']}/wiki"

			if api["license"]:
				if "license" not in app:
					app["license"] = api["license"]["key"]

				if "license_name" not in app:
					app["license_name"] = api["license"]["name"]

			if release:
				if "download_page" not in app:
					app["download_page"] = f"https://github.com/{app['github']}/releases"

				if "version" not in app:
					app["version"] = release["tag_name"]

				if "version_title" not in app and release["name"] != "" and release["name"] is not None:
					app["version_title"] = release["name"]

				if "update_notes" not in app and release["body"] != "" and release["body"] is not None:
					app["update_notes_md"] = release["body"].replace("\r\n", "\n")
					app["update_notes"] = requests.post("https://api.github.com/markdown", headers=header if header else None, json={"text": release["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

				if "updated" not in app:
					app["updated"] = release["published_at"]

				if "downloads" not in app:
					app["downloads"] = {}
				for asset in release["assets"]:
					if not asset["name"] in app["downloads"] and len(re.findall(r"(\.nro|\.vpk|\.love|PS3|PSP|vita|switch|wii|osx|ubuntu|win|elf|\.xz)", asset["name"])) == 0:
						app["downloads"][asset["name"]] = {
							"url": asset["browser_download_url"],
							"size": asset["size"],
							"size_str": byteCount(asset["size"])
						}

			if prerelease:
				if "prerelease" not in app:
					app["prerelease"] = {}

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

				if "update_notes" not in app and prerelease["body"] != "" and prerelease["body"] is not None:
					app["update_notes_md"] = prerelease["body"].replace("\r\n", "\n")
					app["update_notes"] = requests.post("https://api.github.com/markdown", headers=header if header else None, json={"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text
				if "update_notes" not in app["prerelease"] and prerelease["body"] != "" and prerelease["body"] is not None:
					app["prerelease"]["update_notes_md"] = prerelease["body"].replace("\r\n", "\n")
					app["prerelease"]["update_notes"] = requests.post("https://api.github.com/markdown", headers=header if header else None, json={"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

				if "updated" not in app:
					app["updated"] = prerelease["published_at"]
				if "updated" not in app["prerelease"]:
					app["prerelease"]["updated"] = prerelease["published_at"]

				if "downloads" not in app["prerelease"]:
					app["prerelease"]["downloads"] = {}
				for asset in prerelease["assets"]:
					if not asset["name"] in app["prerelease"]["downloads"]:
						app["prerelease"]["downloads"][asset["name"]] = {
							"url": asset["browser_download_url"],
							"size": asset["size"],
							"size_str": byteCount(asset["size"])
						}

		if "bitbucket" in app:
			print("Bitbucket")
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

			if "downloads" not in app:
				app["downloads"] = {}
			for download in app["bitbucket"]["files"]:
				fileAPI = requests.get(f"https://api.bitbucket.org/2.0/repositories/{app['bitbucket']['repo']}/src/{(app['bitbucket']['branch'] if 'branch' in app['bitbucket'] else 'master')}/{download}?format=meta").json()
				if download not in app["downloads"]:
					app["downloads"][download] = {
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

		# Process format strings in downloads if needed
		if "eval_downloads" in app and app["eval_downloads"]:
			if "download_page" in app and type(app["download_page"]) == str:
				app["download_page"] = eval(app["download_page"])
			if "downloads" in app:
				for item in app["downloads"]:
					if(type(app["downloads"][item]["url"]) == str):
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
					app["update_notes"] = requests.post("https://api.github.com/markdown", headers=header if header else None, json={"text": app["update_notes_md"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

		# Check for screenshots
		if os.path.exists(os.path.join("..", "docs", "assets", "images", "screenshots", webName(app["title"]))):
			if "screenshots" not in app:
				app["screenshots"] = []
			dirlist = os.listdir(os.path.join("..", "docs", "assets", "images", "screenshots", webName(app["title"])))
			dirlist.sort()
			for screenshot in dirlist:
				if screenshot[-3:] in ["png", "gif", "jpg", "peg", "iff", "bmp"]:
					app["screenshots"].append({
						"url": f"https://db.universal-team.net/assets/images/screenshots/{webName(app['title'])}/{screenshot}",
						"description": screenshot[:screenshot.rfind(".")].capitalize().replace("-", " ")
					})

		# Format update notes with GitHub's API
		if "update_notes_md" in app and "update_notes" not in app:
			app["update_notes"] = requests.post("https://api.github.com/markdown", headers=header if header else None, json={"text": app["update_notes_md"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

		# Get missing download sizes
		if "downloads" in app:
			for download in app["downloads"]:
				if "size" not in app["downloads"][download]:
					if app["downloads"][download]["url"][:30] == "https://db.universal-team.net/":
						app["downloads"][download]["size"] = os.path.getsize(f"../docs/{app['downloads'][download]['url'][30:]}")
						app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])
					else:
						r = requests.head(app["downloads"][download]["url"], allow_redirects=True)
						if r.status_code == 200 and "Content-Length" in r.headers:
							app["downloads"][download]["size"] = int(r.headers["Content-Length"])
							app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])

		# Check for local icon / image
		if "icon" not in app and os.path.exists(os.path.join("..", "docs", "assets", "images", "icons", f"{webName(app['title'])}.png")):
			app["icon"] = f"https://db.universal-team.net/assets/images/icons/{webName(app['title'])}.png"

		if "image" not in app and os.path.exists(os.path.join("..", "docs", "assets", "images", "images", f"{webName(app['title'])}.png")):
			app["image"] = f"https://db.universal-team.net/assets/images/images/{webName(app['title'])}.png"
		elif "image" not in app and "avatar" in app:
			app["image"] = app["avatar"]

		# Get image size
		if "image_length" not in app and "image" in app:
			if app["image"][:30] == "https://db.universal-team.net/":
				app["image_length"] = os.path.getsize(f"../docs/{app['image'][30:]}")
			else:
				r = requests.head(app["image"], allow_redirects=True)
				if r.status_code == 200 and "Content-Length" in r.headers:
					app["image_length"] = int(r.headers["Content-Length"])

		# Make icon for UniStore and QR
		img = None
		if "icon" in app or "image" in app:
			if not os.path.exists(os.path.join("temp", "48")):
				os.makedirs(os.path.join("temp", "48"))
			if not os.path.exists(os.path.join("temp", "32")):
				os.makedirs(os.path.join("temp", "32"))

			url = app["icon"] if "icon" in app else app["image"] if "image" in app else ""
			file = None
			if url[:30] == "https://db.universal-team.net/":
				file = open(f"../docs/{url[30:]}", "rb")
			else:
				r = requests.get(url)
				if r.status_code == 200:
					file = io.BytesIO(r.content)
				else:
					print(f"Error {r.status_code} downloading image!")

			if file:
				if priorityOnlyMode:
					old = next(item for item in oldData if item["title"] == app["title"])
					app["icon_index"] = old["icon_index"] if "icon_index" in old else -1
				else:
					app["icon_index"] = iconIndex

				with Image.open(file) as img:
					imgPal = None
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
					img.save(os.path.join("temp", "48", f"{iconIndex}.png"))

					imgDS = img.copy()
					imgDS.thumbnail((32, 32))
					data = numpy.array(imgDS)
					r, g, b, a = data.T
					transparent = a < 0xFF
					data[...][transparent.T] = (0xFF, 0, 0xFF, 0xFF)
					imgDS = Image.fromarray(data)
					imgDS = imgDS.quantize()
					imgDS.save(os.path.join("temp", "32", f"{iconIndex}.png"))

					if "color" not in app:
						color = img.copy()
						color.thumbnail((1, 1))
						color = color.getpixel((0, 0))
						app["color"] = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

				if "icon" in app and app["icon"].endswith(".bmp"):
					copyfile(os.path.join("temp", "48", f"{iconIndex}.png"), os.path.join("..", "docs", "assets", "images", "icons", f"{webName(app['title'])}.png"))
					app["icon"] = f"https://db.universal-team.net/assets/images/icons/{webName(app['title'])}.png"

				iconIndex += 1

	if "title" in app:
		print(webName(app["title"]))

	# Make QR
	if not foundExisting or not (priorityOnlyMode and not ("priority" in app and app["priority"])):
		if "downloads" in app:
			for item in app["downloads"]:
				if item[item.rfind(".") + 1:] == "cia":
					qr = qrcode.make(app["downloads"][item]["url"], box_size=5, version=5).convert("RGBA")
					if img:
						draw = ImageDraw.Draw(qr)
						draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 10 if "version" in app else 4)), fill=(255, 255, 255))
						qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask=img if img.mode == "RGBA" else None)
						if "version" in app:
							draw.text(((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2 + img.height), app["version"][:img.width // 6], (0, 0, 0))
					qr.save(os.path.join("..", "docs", "assets", "images", "qr", f"{webName(item)}.png"))
					if "qr" not in app:
						app["qr"] = {}
					app["qr"][item] = f"https://db.universal-team.net/assets/images/qr/{webName(item)}.png"

		if "prerelease" in app:
			for item in app["prerelease"]["downloads"]:
				if item[item.rfind(".") + 1:] == "cia":
					qr = qrcode.make(app["prerelease"]["downloads"][item]["url"], box_size=5, version=5).convert("RGBA")
					data = numpy.array(qr)
					r, g, b, a = data.T
					black = (r == 0) & (g == 0) & (b == 0)
					data[...][black.T] = (0xF6, 0x6A, 0x0A, 0xFF)
					qr = Image.fromarray(data)
					if img:
						draw = ImageDraw.Draw(qr)
						draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 10 if "version" in app["prerelease"] else 4)), fill=(255, 255, 255))
						qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask=img if img.mode == "RGBA" else None)
						if "version" in app["prerelease"]:
							draw.text(((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2 + img.height), app["prerelease"]["version"][:img.width // 6], (0xF6, 0x6A, 0x0A))
					qr.save(os.path.join("..", "docs", "assets", "images", "qr", "prerelease", f"{webName(item)}.png"))
					if "qr" not in app["prerelease"]:
						app["prerelease"]["qr"] = {}
					app["prerelease"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/prerelease/{webName(item)}.png"

		if "nightly" in app:
			for item in app["nightly"]["downloads"]:
				if item[item.rfind(".") + 1:] == "cia":
					qr = qrcode.make(app["nightly"]["downloads"][item]["url"], box_size=5, version=5).convert("RGBA")
					data = numpy.array(qr)
					r, g, b, a = data.T
					black = (r == 0) & (g == 0) & (b == 0)
					data[...][black.T] = (0, 0, 0xC0, 0xFF)
					qr = Image.fromarray(data)
					if img:
						draw = ImageDraw.Draw(qr)
						draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 4)), fill=(255, 255, 255))
						qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask=img if img.mode == "RGBA" else None)
					qr.save(os.path.join("..", "docs", "assets", "images", "qr", "nightly", f"{webName(item)}.png"))
					if "qr" not in app["nightly"]:
						app["nightly"]["qr"] = {}
					app["nightly"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/nightly/{webName(item)}.png"

	# Add to output json
	output.append(app)

	# Website file
	web = app.copy()
	web["layout"] = "app"
	# long description is put as the content
	if "long_description" in web:
		web.pop("long_description")
	# Remove large things that aren't needed
	if "update_notes_md" in web:
		web.pop("update_notes_md")
	if "scripts" in web:
		web.pop("scripts")
	# Add defaults where absolutely needed
	if "systems" not in web:
		web["systems"] = ["3DS"] # default to 3DS
	if "updated" not in web:
		web["updated"] = "---"
	for system in web["systems"]:
		if "title" in web:
			with open(os.path.join("..", "docs", f"_{webName(system)}", f"{webName(web['title'])}.md"), "w", encoding="utf8") as file:
				file.write(f"---\n{yaml.dump(web)}---\n")
				if "long_description" in app:
					file.write(app["long_description"])

	if "unistore_exclude" not in app or not app["unistore_exclude"]:
		# Move links to end to be more readable in U-U
		notes = app["update_notes_md"] if "update_notes_md" in app else ""
		i = 0
		links = []

		def getLinkReplacement(match):
			global i, links
			linkNum = i

			if match.group(2) in links:
				linkNum = links.index(match.group(2))
			else:
				links.append(match.group(2))
				i += 1

			return f"{match.group(1)}[{str(linkNum)}]"

		notes = re.sub(r"(\[.*?\])\((.*?)\)", getLinkReplacement, notes)
		notes = re.sub(r"[0-9a-fA-F]{40}", lambda match: match.group(0)[:7], notes)

		if len(links) > 0:
			notes += "\n"

		for i, link in enumerate(links):
			notes += f"\n[{i}]: {link}"

		# Add entry for UniStore
		uni = {
			"info": {
				"title": ucs2Name(app["title"]) if "title" in app else "",
				"version": ucs2Name(app["version"]) if "version" in app else "",
				"author": ucs2Name(app["author"]) if "author" in app else "",
				"category": app["categories"] if "categories" in app else [],
				"console": app["systems"].copy() if "systems" in app else [],
				"icon_index": app["icon_index"] if "icon_index" in app else -1,
				"description": ucs2Name(app["description"]) if "description" in app else "",
				"releasenotes": notes,
				"screenshots": [],
				"license": app["license"] if "license" in app else "",
				"wiki": app["wiki"] if "wiki" in app else ""
			}
		}

		if "updated" in app:
			uni["info"]["last_updated"] = parser.parse(app["updated"]).strftime("%Y-%m-%d at %H:%M (UTC)")

		if "screenshots" in app:
			for screenshot in app["screenshots"]:
				if screenshot["url"][-3:] == "png" and "horihd" not in screenshot["url"]:
					uni["info"]["screenshots"].append(screenshot)

		if "DS" in uni["info"]["console"]:
			uni["info"]["console"].remove("DS")
			uni["info"]["console"].append("NDS")

		# If scripts are specified, use those instead of the release files
		if "scripts" in app:
			for script in app["scripts"]:
				uni[script] = app["scripts"][script]

		# If autogen_scripts is forced or no scripts, generate scripts from downloads
		if "autogen_scripts" in app and app["autogen_scripts"] or "scripts" not in app:
			if "downloads" in app:
				for file in app["downloads"]:
					if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and len([item for item in app["archive"] if re.findall(item, file)])):
						uni[app["archive"][file][0] if ("archive" in app and file in app["archive"]) else file] = {
							"script": downloadScript(file, app["downloads"][file]["url"], app["script_message"] if "script_message" in app else None, app["archive"] if "archive" in app else None),
							"size": byteCount(app["downloads"][file]["size"]) if "size" in app["downloads"][file] else "",
						}

			if "prerelease" in app:
				for file in app["prerelease"]["downloads"]:
					if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and file in app["archive"]):
						uni[f"[prerelease] {app['archive'][file][0] if ('archive' in app and file in app['archive']) else file}"] = {
							"script": downloadScript(file, app["prerelease"]["downloads"][file]["url"], app["script_message"] if "script_message" in app else None, app["archive"] if "archive" in app else None),
							"size": byteCount(app["prerelease"]["downloads"][file]["size"]) if "size" in app["prerelease"]["downloads"][file] else "",
						}

			if "nightly" in app:
				for file in app["nightly"]["downloads"]:
					if len(re.findall(r"\.(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and file in app["archive"]):
						uni[f"[nightly] {app['archive'][file][0] if ('archive' in app and file in app['archive']) else file}"] = {
							"script": downloadScript(file, app["nightly"]["downloads"][file]["url"], app["script_message"] if "script_message" in app else None, app["archive"] if "archive" in app else None),
							"size": byteCount(app["nightly"]["downloads"][file]["size"]) if "size" in app["nightly"]["downloads"][file] else "",
						}

		if app["title"] == "RetroArch":
			uni["info"]["description"] += "\n\nCores must be downloaded from their separate UniStore, which can be added in settings."
			retroarch(uni["info"]["icon_index"])

		unistore["storeContent"].append(uni)

	print("=" * 80)

if not priorityOnlyMode:
	# Make tdx
	with open(os.path.join("temp", "32", "icons.tds"), "w", encoding="utf8") as file:
		file.write("-gb -gB8 -gzl\n\n")
		for i in range(iconIndex):
			file.write(f"{i}.png\n")
	os.system(f"./img2tdx.py {os.path.join('temp', '32', 'icons.tds')} -o {os.path.join('..', 'docs', 'unistore', 'universal-db.tdx')}")

	# Make t3x
	with open(os.path.join("temp", "48", "icons.t3s"), "w", encoding="utf8") as file:
		file.write("--atlas -f rgba -z auto\n\n")
		for i in range(iconIndex):
			file.write(f"{i}.png\n")
	os.system(f"tex3ds -i {os.path.join('temp', '48', 'icons.t3s')} -o {os.path.join('..', 'docs', 'unistore', 'universal-db.t3x')}")

# Increment revision if not the same
if unistore != unistoreOld:
	unistore["storeInfo"]["revision"] += 1

# Write unistore to file
with open(os.path.join("..", "docs", "unistore", "universal-db.unistore"), "w", encoding="utf8") as file:
	file.write(json.dumps(unistore, sort_keys=True, ensure_ascii=False))

# Write output file
with open(os.path.join("..", "docs", "data", "full.json"), "w", encoding="utf8") as file:
	file.write(json.dumps(output, sort_keys=True, ensure_ascii=False))
