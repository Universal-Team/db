#!/usr/bin/env python3

from bs4 import BeautifulSoup
import datetime
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
import rfeed
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
		if letter in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
			out += letter
		elif letter == " ":
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
	if archive and file in archive:
		script = [
			{
				"type": "downloadFile",
				"file": url,
				"output": f"/{file}",
				"message": f"Downloading {file}..."
			}
		]
		for item in archive[file]:
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
					"output": f"sdmc:/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {file}..."
				})

				script.append({
					"type": "installCia",
					"file": f"/{item}",
					"message": f"Installing {item}..."
				})

				script.append({
					"type": "deleteFile",
					"file": f"sdmc:/{item}",
					"message": f"Deleting {item}..."
				})
			elif item == "boot.firm":
				script.append({
					"type": "extractFile",
					"file": f"/{file}",
					"input": f"{item}",
					"output": f"sdmc:/{item[item.rfind('/') + 1:]}",
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
					"output": f"sdmc:/{item[item.rfind('/') + 1:]}",
					"message": f"Extracting {item[item.rfind('/') + 1:]}..."
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
					"output": f"sdmc:/{file}",
					"message": f"Downloading {file}..."
				},
				{
					"type": "installCia",
					"file": f"/{file}",
					"message": f"Installing {file}..."
				},
				{
					"type": "deleteFile",
					"file": f"sdmc:/{file}",
					"message": f"Deleting {file}..."
				}
			]
		elif file == "boot.firm":
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"sdmc:/{file}",
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
					"output": f"sdmc:/{file}",
					"message": f"Downloading {file}..."
				},
				{
					"type": "extractFile",
					"file": f"sdmc:/{file}",
					"input": "",
					"output": f"%ARCHIVE_DEFAULT%/{file[0:file.find('.')]}/",
					"message": f"Extracting {file}..."
				},
				{
					"type": "deleteFile",
					"file": f"sdmc:/{file}",
					"message": f"Deleting {file}..."
				}
			]
		else:
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"sdmc:/{file}",
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
		"url": "https://db.universal-team.net/unistore/universal-db.unistore",
		"file": "universal-db.unistore",
		"sheetURL": "https://db.universal-team.net/unistore/universal-db.t3x",
		"sheet": "universal-db.t3x",
		"description": "Universal-DB - An online database of 3DS and DS homebrew",
		"version": 3,
		"revision": 0 if not "revision" in unistoreOld["storeInfo"] else unistoreOld["storeInfo"]["revision"]
	},
	"storeContent": [],
}

# Output json
output = []

# Old data json
oldData = None

with open(os.path.join("..", "docs", "data", "full.json"), "r", encoding="utf8") as file:
	oldData = json.load(file)

# Icons array
icons = []
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
			soup = BeautifulSoup(requests.get(f"https://gbatemp.net/download/{app['gbatemp']}/").text, "html.parser")

			if not "title" in app:
				app["title"] = soup.find(class_="resourceInfo").h1.find(text=True).strip()

			if not "author" in app:
				app["author"] = soup.find(class_="author").dd.a.text.strip()

			if not "description" in app:
				app["description"] = soup.find(class_="tagLine").text.strip()

			if not "long_description" in app:
				app["long_description"] = soup.blockquote.decode_contents().strip()

			if not "avatar" in app:
				app["avatar"] = "https://gbatemp.net/" + re.sub("/s/", "/l/", soup.find(class_="resourceImage").a.img["src"]).strip()

			if not "created" in app:
				app["created"] = parser.parse(soup.find(class_="firstRelease").dd.span["title"]).strftime("%Y-%m-%dT%H:%M:%SZ")

			if not "download_page" in app:
				app["download_page"] = f"https://gbatemp.net/download/{app['gbatemp']}/"

			if not "version" in app:
				app["version"] = soup.find(class_="resourceInfo").h1.span.text.strip()

			if not "version_title" in app:
				app["version_title"] = soup.find(class_="updates").ol.li.a.text.strip()

			if not "update_notes" in app or not "update_notes_md" in app:
				if not "update_notes" in app:
					notesSoup = BeautifulSoup(requests.get("https://gbatemp.net/" + soup.find(class_="updates").ol.li.a["href"]).text, "html.parser")
					app["update_notes"] = notesSoup.blockquote.decode_contents().strip()

				if not "update_notes_md" in app:
					app["update_notes_md"] = markdownify(app["update_notes"], bullets="-")

			if not "updated" in app:
				app["updated"] = parser.parse(soup.find(class_="lastUpdate").dd.span["title"]).strftime("%Y-%m-%dT%H:%M:%SZ")

			if not "downloads" in app:
				app["downloads"] = {}

			head = requests.head("https://gbatemp.net/" + soup.find(class_="downloadButton").a["href"])
			if head.status_code == 200:
				if "Content-Disposition" in head.headers:
					name = re.findall('filename="(.*)"', head.headers["Content-Disposition"])
					if len(name) > 0:
						name = name[0]
						size = None
						if not name in app["downloads"]:
							app["downloads"][name] = {
								"url": head.url,
							}

							if "Content-Length" in head.headers:
								app["downloads"][download]["size"] = int(head.headers["Content-Length"])
								app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])

		if "github" in app:
			print("GitHub")
			api = requests.get(f"https://api.github.com/repos/{app['github']}", headers = header if header else None).json()
			releases = requests.get(f"https://api.github.com/repos/{app['github']}/releases", headers = header if header else None).json()
			release = None
			prerelease = None
			if len(releases) > 0 and releases[0]["prerelease"]:
				prerelease = releases[0]
			for r in releases:
				if not (r["prerelease"] or r["draft"]):
					release = r
					break

			if not "title" in app:
				app["title"] = api["name"]

			if not "author" in app:
				username = api["owner"]["login"]
				if username in names:
					username = names[username]
				else:
					user = requests.get(f"https://api.github.com/users/{username}", headers = header if header else None).json()
					names[username] = user["name"] if user["name"] != None else username
					username = names[username]
				app["author"] = username

			if not "description" in app and api["description"] != "" and api["description"] != None:
				app["description"] = api["description"]

			if not "avatar" in app:
				app["avatar"] = api["owner"]["avatar_url"]

			if not "source" in app:
				app["source"] = api["html_url"]

			if not "created" in app:
				app["created"] = api["created_at"]

			if not "website" in app and api["homepage"] != "" and api["homepage"] != None:
				app["website"] = api["homepage"]

			if not "wiki" in app and api["has_wiki"] and requests.get(f"https://raw.githubusercontent.com/wiki/{app['github']}/Home.md").status_code != 404:
				app["wiki"] = f"{api['html_url']}/wiki"

			if api["license"]:
				if not "license" in app:
					app["license"] = api["license"]["key"]

				if not "license_name" in app:
					app["license_name"] = api["license"]["name"]

			if release:
				if not "download_page" in app:
					app["download_page"] = f"https://github.com/{app['github']}/releases"

				if not "version" in app:
					app["version"] = release["tag_name"]

				if not "version_title" in app and release["name"] != "" and release["name"] != None:
					app["version_title"] = release["name"]

				if not "update_notes" in app and release["body"] != "" and release["body"] != None:
					app["update_notes_md"] = release["body"].replace("\r\n", "\n")
					app["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": release["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

				if not "updated" in app:
					app["updated"] = release["published_at"]

				if not "downloads" in app:
					app["downloads"] = {}
				for asset in release["assets"]:
					if not asset["name"] in app["downloads"] and len(re.findall("(\.nro|\.vpk|\.love|PS3|PSP|vita|switch|wii|osx|ubuntu|win|elf|\.xz)", asset["name"])) == 0:
						app["downloads"][asset["name"]] = {
							"url": asset["browser_download_url"],
							"size": asset["size"],
							"size_str": byteCount(asset["size"])
						}

			if prerelease:
				if not "prerelease" in app:
					app["prerelease"] = {}

				if not "download_page" in app:
					app["download_page"] = f"https://github.com/{app['github']}/releases"
				if not "download_page" in app["prerelease"]:
					app["prerelease"]["download_page"] = prerelease["html_url"]

				if not "version" in app:
					app["version"] = prerelease["tag_name"]
				if not "version" in app["prerelease"]:
					app["prerelease"]["version"] = prerelease["tag_name"]

				if not "version_title" in app and prerelease["name"] != "" and prerelease["name"] != None:
					app["version_title"] = prerelease["name"]
				if not "version_title" in app["prerelease"] and prerelease["name"] != "" and prerelease["name"] != None:
					app["prerelease"]["version_title"] = prerelease["name"]

				if not "update_notes" in app and prerelease["body"] != "" and prerelease["body"] != None:
					app["update_notes_md"] = prerelease["body"].replace("\r\n", "\n")
					app["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text
				if not "update_notes" in app["prerelease"] and prerelease["body"] != "" and prerelease["body"] != None:
					app["prerelease"]["update_notes_md"] = prerelease["body"].replace("\r\n", "\n")
					app["prerelease"]["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": prerelease["body"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

				if not "updated" in app:
					app["updated"] = prerelease["published_at"]
				if not "updated" in app["prerelease"]:
					app["prerelease"]["updated"] = prerelease["published_at"]

				if not "downloads" in app["prerelease"]:
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

			if not "title" in app:
				app["title"] = api["name"]

			if not "author" in app:
				app["author"] = api["owner"]["display_name"]

			if not "description" in app:
				app["description"] = api["description"].replace("\r\n", "\n")

			if not "avatar" in app:
				app["avatar"] = api["links"]["avatar"]["href"]

			if not "source" in app:
				app["source"] = api["links"]["html"]["href"]

			if not "created" in app:
				app["created"] = api["created_on"]

			if not "downloads" in app:
				app["downloads"] = {}
			for download in app["bitbucket"]["files"]:
				fileAPI = requests.get(f"https://api.bitbucket.org/2.0/repositories/{app['bitbucket']['repo']}/src/{(app['bitbucket']['branch'] if 'branch' in app['bitbucket'] else 'master')}/{download}?format=meta").json()
				if not download in app["downloads"]:
					app["downloads"][download] = {
						"url": fileAPI["links"]["self"]["href"],
						"size": fileAPI["size"],
						"size_str": byteCount(fileAPI["size"])
					}

				if not "download_page" in app:
					app["download_page"] = f"https://bitbucket.org/{app['bitbucket']['repo']}/src/{(app['bitbucket']['branch'] if 'branch' in app['bitbucket'] else 'master')}/{download}"

				if not "version" in app:
					app["version"] = fileAPI["commit"]["hash"][:7]

				if not "updated" in app:
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
			if "scripts" in app:
				for script in app["scripts"]:
					for function in app["scripts"][script]:
						if function["type"] == "downloadFile" and type(function["file"]) == str:
							function["file"] = eval(function["file"])
		if "eval_notes_md" in app and app["eval_notes_md"]:
			if "update_notes_md" in app:
				app["update_notes_md"] = eval(app["update_notes_md"])
				if not "update_notes" in app:
					app["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": app["update_notes_md"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

		# Check for screenshots
		if os.path.exists(os.path.join("..", "docs", "assets", "images", "screenshots", webName(app["title"]))):
			if not "screenshots" in app:
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
			app["update_notes"] = requests.post("https://api.github.com/markdown", headers = header if header else None, json = {"text": app["update_notes_md"], "mode": "gfm" if "github" in app else "markdown", "context": app["github"] if "github" in app else None}).text

		# Get missing download sizes
		if "downloads" in app:
			for download in app["downloads"]:
				if not "size" in app["downloads"][download]:
					if app["downloads"][download]["url"][:30] == "https://db.universal-team.net/":
						app["downloads"][download]["size"] = os.path.getsize(f"../docs/{app['downloads'][download]['url'][30:]}")
						app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])
					else:
						r = requests.head(app["downloads"][download]["url"], allow_redirects=True)
						if r.status_code == 200 and "Content-Length" in r.headers:
							app["downloads"][download]["size"] = int(r.headers["Content-Length"])
							app["downloads"][download]["size_str"] = byteCount(app["downloads"][download]["size"])

	if "title" in app:
		print(webName(app["title"]))
	print("=" * 80)

	# Check for local icon / image
	if not "icon" in app and os.path.exists(os.path.join("..", "docs", "assets", "images", "icons", f"{webName(app['title'])}.png")):
		app["icon"] = f"https://db.universal-team.net/assets/images/icons/{webName(app['title'])}.png"

	if not "image" in app and os.path.exists(os.path.join("..", "docs", "assets", "images", "images", f"{webName(app['title'])}.png")):
		app["image"] = f"https://db.universal-team.net/assets/images/images/{webName(app['title'])}.png"
	elif not "image" in app and "avatar" in app:
		app["image"] = app["avatar"]

	# Get image size
	if not "image_length" in app and "image" in app:
		if app["image"][:30] == "https://db.universal-team.net/":
			app["image_length"] = os.path.getsize(f"../docs/{app['image'][30:]}")
		else:
			r = requests.head(app["image"], allow_redirects=True)
			if r.status_code == 200 and "Content-Length" in r.headers:
				app["image_length"] = int(r.headers["Content-Length"])

	# Make icon for UniStore and QR
	img = None
	if "icon" in app or "image" in app:
		if not os.path.exists("temp"):
			os.mkdir("temp")

		url = app["icon"] if "icon" in app else app["image"] if "image" in app else ""
		file = None
		if url[:30] == "https://db.universal-team.net/":
			file = open(f"../docs/{url[30:]}", "rb")
		else:
			file = io.BytesIO(requests.get(url).content)

		if file:
			with Image.open(file) as img:
				if img.mode == "P":
					pal = img.palette.getdata()[1]
					img = img.convert("RGBA")
					data = numpy.array(img)
					r, g, b, a = data.T
					transparent = (r == pal[2]) & (g == pal[1]) & (b == pal[0])
					data[...][transparent.T] = (0, 0, 0, 0)
					img = Image.fromarray(data)
				elif img.mode != "RGBA":
					img = img.convert("RGBA")
				img.thumbnail((48, 48))
				img.save(os.path.join("temp", f"{iconIndex}.png"))
				icons.append(f"{iconIndex}.png")
				iconIndex += 1
				if not "color" in app:
					color = img.copy()
					color.thumbnail((1, 1))
					color = color.getpixel((0, 0))
					app["color"] = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

	# Output website page
	if "downloads" in app:
		for item in app["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["downloads"][item]["url"], box_size = 5, version = 5).convert("RGBA")
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 10 if "version" in app else 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
					if "version" in app:
						draw.text(((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2 + img.height), app["version"][:img.width//6], (0, 0, 0))
				qr.save(os.path.join("..", "docs", "assets", "images", "qr", f"{webName(item)}.png"))
				if not "qr" in app:
					app["qr"] = {}
				app["qr"][item] = f"https://db.universal-team.net/assets/images/qr/{webName(item)}.png"

	if "prerelease" in app:
		for item in app["prerelease"]["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["prerelease"]["downloads"][item]["url"], box_size = 5, version = 5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0xF6, 0x6A, 0x0A, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 10 if "version" in app["prerelease"] else 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
					if "version" in app["prerelease"]:
						draw.text(((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2 + img.height), app["prerelease"]["version"][:img.width//6], (0xF6, 0x6A, 0x0A))
				qr.save(os.path.join("..", "docs", "assets", "images", "qr", "prerelease", f"{webName(item)}.png"))
				if not "qr" in app["prerelease"]:
					app["prerelease"]["qr"] = {}
				app["prerelease"]["qr"][item] = f"https://db.universal-team.net/assets/images/qr/prerelease/{webName(item)}.png"

	if "nightly" in app:
		for item in app["nightly"]["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["nightly"]["downloads"][item]["url"], box_size = 5, version = 5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0, 0, 0xC0, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
				qr.save(os.path.join("..", "docs", "assets", "images", "qr", "nightly", f"{webName(item)}.png"))
				if not "qr" in app["nightly"]:
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
	if not "systems" in web:
		web["systems"] = ["3DS"] # default to 3DS
	if not "updated" in web:
		web["updated"] = "---"
	for system in web["systems"]:
		if "title" in web:
			with open(os.path.join("..", "docs", f"_{webName(system)}", f"{webName(web['title'])}.md"), "w", encoding="utf8") as file:
				file.write(f"---\n{yaml.dump(web)}---\n")
				if "long_description" in app:
					file.write(app["long_description"])

	if not "unistore_exclude" in app or app["unistore_exclude"] == False:
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
				"icon_index": len(icons) - 1 if "icon" in app or "image" in app else -1,
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
		if "autogen_scripts" in app and app["autogen_scripts"] or not "scripts" in app:
			if "downloads" in app:
				for file in app["downloads"]:
					if len(re.findall("(zip|rar|7z|torrent|tar)", file)) == 0 or ("archive" in app and file in app["archive"]):
						uni[app["archive"][file][0] if ("archive" in app and file in app["archive"]) else file] = {
							"script": downloadScript(file, app["downloads"][file]["url"], app["script_message"] if "script_message" in app else None, app["archive"] if "archive" in app else None),
							"size": byteCount(app["downloads"][file]["size"]) if "size" in app["downloads"][file] else "",
						}

			if "prerelease" in app:
				for file in app["prerelease"]["downloads"]:
					if len(re.findall("(zip|rar|7z|torrent)", file)) == 0 or ("archive" in app and file in app["archive"]):
						uni[f"[prerelease] {app['archive'][file][0] if ('archive' in app and file in app['archive']) else file}"] = {
							"script": downloadScript(file, app["prerelease"]["downloads"][file]["url"], app["script_message"] if "script_message" in app else None, app["archive"] if "archive" in app else None),
							"size": byteCount(app["prerelease"]["downloads"][file]["size"]) if "size" in app["prerelease"]["downloads"][file] else "",
						}

			if "nightly" in app:
				for file in app["nightly"]["downloads"]:
					if len(re.findall("(zip|rar|7z|torrent)", file)) == 0 or ("archive" in app and file in app["archive"]):
						uni[f"[nightly] {app['archive'][file][0] if ('archive' in app and file in app['archive']) else file}"] = {
							"script": downloadScript(file, app["nightly"]["downloads"][file]["url"], app["script_message"] if "script_message" in app else None, app["archive"] if "archive" in app else None),
							"size": byteCount(app["nightly"]["downloads"][file]["size"]) if "size" in app["nightly"]["downloads"][file] else "",
						}

		unistore["storeContent"].append(uni)

# Make t3x
with open(os.path.join("temp", "icons.t3s"), "w", encoding="utf8") as file:
	file.write("--atlas -f rgba -z auto\n\n")
	for icon in icons:
		file.write(f"{icon}\n")
os.system(f"tex3ds -i {os.path.join('temp', 'icons.t3s')} -o {os.path.join('..', 'docs', 'unistore', 'universal-db.t3x')}")

# Increment revision if not the same
if unistore != unistoreOld:
	unistore["storeInfo"]["revision"] += 1

# Write unistore to file
with open(os.path.join("..", "docs", "unistore", "universal-db.unistore"), "w", encoding="utf8") as file:
	file.write(json.dumps(unistore, sort_keys=True))

# Write output file
with open(os.path.join("..", "docs", "data", "full.json"), "w", encoding="utf8") as file:
	file.write(json.dumps(output, sort_keys=True))
