#!/usr/bin/env python3

import datetime
from dateutil import parser
import io
import json
import numpy
import os
from PIL import Image, ImageDraw
import qrcode
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

def downloadScript(file, url):
	if file[file.rfind(".") + 1:].lower() == "3dsx":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/3ds/" + file,
				"message": "Downloading " + file + "..."
			}
		]
	elif file[file.rfind(".") + 1:].lower() == "cia":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/" + file,
				"message": "Downloading " + file + "..."
			},
			{
				"type": "installCia",
				"file": "/" + file,
				"message": "Installing " + file + "..."
			},
			{
				"type": "deleteFile",
				"file": "sdmc:/" + file,
				"message": "Deleting " + file + "."
			}
		]
	elif file[file.rfind(".") + 1:].lower() == "firm":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/luma/payloads/" + file,
				"message": "Downloading " + file + "..."
			}
		]
	elif file[file.rfind(".") + 1:].lower() in ["zip", "7z", "rar"]:
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/" + file,
				"message": "Downloading " + file + "..."
			},
			{
				"type": "extractFile",
				"file": "sdmc:/" + file,
				"input": "",
				"output": "/" + file[0:file.find(".")] + "/",
				"message": "Extracting " + file + "..."
			},
			{
				"type": "deleteFile",
				"file": "sdmc:/" + file,
				"message": "Deleting " + file +"..."
			}
		]
	else:
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/" + file,
				"message": "Downloading " + file + "..."
			}
		]

# Read json
with open("source.json", "r", encoding="utf8") as file:
	source = json.load(file)

# Read version from old unistore
with open(os.path.join("..", "unistore", "universal-db.unistore"), "r", encoding="utf8") as file:
	unistoreOld = json.load(file)

# Create UniStore base
unistore = {
	"storeInfo": {
		"title": "Universal-DB",
		"author": "Universal-Team",
		"url": "https://db.universal-team.net/unistore/universal-db.unistore",
		"file": "sdmc:/3ds/Universal-Updater/stores/Universal-DB.unistore",
		"sheet": "sdmc:/3ds/Universal-Updater/stores/Universal-DB.t3x",
		"sheetURL": "https://db.universal-team.net/unistore/universal-db.t3x",
		"description": "Universal DB - An online database of 3DS and DS homebrew",
		"categories": [],
		"authors": [],
		"consoles": [],
		"barLight": "#395472",
		"barDark": "#395472",
		"bgDark": "#262c4d",
		"bgLight": "#60a8c0",
		"textDark": "#ffffff",
		"textLight": "#000000",
		"boxDark": "#313131",
		"boxLight": "#f7f7f7",
		"outlineDark": "#f00000",
		"outlineLight": "#f00000",
		"version": 2,
		"revision": 0 if not "revision" in unistoreOld["storeInfo"] else unistoreOld["storeInfo"]["revision"]
	},
	"storeContent": [],
}

# Output json
output = []

# Old data json
oldData = None

with open(os.path.join("..", "data", "full.json"), "r", encoding="utf8") as file:
	oldData = json.load(file)

# Icons array
icons = []
iconIndex = 0

# Auth header
header = None
if len(sys.argv) > 1:
	header = {"Authorization": "token " + sys.argv[1]}

# Fetch info for GitHub apps and output
for app in source:
	if "github" in app:
		print("GitHub")
		api = requests.get("https://api.github.com/repos/" + app["github"], headers = header if header else None).json()
		releases = requests.get("https://api.github.com/repos/" + app["github"] + "/releases", headers = header if header else None).json()
		release = None
		prerelease = None
		if len(releases) > 0 and releases[0]["prerelease"]:
			prerelease = releases[0]
		for r in releases:
			if not r["prerelease"]:
				release = r
				break

		if not "title" in app:
			app["title"] = api["name"]

		if not "author" in app:
			app["author"] = api["owner"]["login"]

		if not "description" in app and api["description"] != "" and api["description"] != None:
			app["description"] = api["description"]

		if not "image" in app:
			app["image"] = api["owner"]["avatar_url"]

		if not "source" in app:
			app["source"] = api["html_url"]

		if not "created" in app:
			app["created"] = api["created_at"]

		if not "website" in app and api["homepage"] != "" and api["homepage"] != None:
			app["website"] = api["homepage"]

		if not "wiki" in app and api["has_wiki"]:
			app["wiki"] = api["html_url"] + "/wiki"

		if release:
			if not "download_page" in app:
				app["download_page"] = release["html_url"]

			if not "version" in app:
				app["version"] = release["tag_name"]

			if not "version_title" in app and release["name"] != "" and release["name"] != None:
				app["version_title"] = release["name"]

			if not "updated" in app:
				app["updated"] = release["published_at"]

			if not "downloads" in app:
				app["downloads"] = {}
			for asset in release["assets"]:
				if not asset["name"] in app["downloads"]:
					app["downloads"][asset["name"]] = asset["browser_download_url"]

		if prerelease:
			if not "prerelease" in app:
				app["prerelease"] = {}

			if not "download_page" in app:
				app["download_page"] = prerelease["html_url"]
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

			if not "updated" in app:
				app["updated"] = prerelease["published_at"]
			if not "updated" in app["prerelease"]:
				app["prerelease"]["updated"] = prerelease["published_at"]

			if not "downloads" in app["prerelease"]:
				app["prerelease"]["downloads"] = {}
			for asset in prerelease["assets"]:
				if not asset["name"] in app["prerelease"]["downloads"]:
					app["prerelease"]["downloads"][asset["name"]] = asset["browser_download_url"]

	if "bitbucket" in app:
		print("Bitbucket")
		api = requests.get("https://api.bitbucket.org/2.0/repositories/" + app["bitbucket"]["repo"]).json()

		if not "title" in app:
			app["title"] = api["name"]

		if not "author" in app:
			app["author"] = api["owner"]["display_name"]

		if not "description" in app:
			app["description"] = api["description"]

		if not "image" in app:
			app["image"] = api["links"]["avatar"]["href"]

		if not "source" in app:
			app["source"] = api["links"]["html"]["href"]

		if not "created" in app:
			app["created"] = api["created_on"]

		if not "downloads" in app:
			app["downloads"] = {}
		for download in app["bitbucket"]["files"]:
			fileAPI = requests.get("https://api.bitbucket.org/2.0/repositories/" + app["bitbucket"]["repo"] + "/src/master/" + download + "?format=meta").json()
			if not download in app["downloads"]:
				app["downloads"][download] = fileAPI["links"]["self"]["href"]

			if not "download_page" in app:
				app["download_page"] = "https://bitbucket.org/" + app["bitbucket"]["repo"] +"/src/master/" + download

			if not "version" in app:
				app["version"] = fileAPI["commit"]["hash"][:7]

			if not "updated" in app:
				commit = requests.get(fileAPI["commit"]["links"]["self"]["href"]).json()
				app["updated"] = commit["date"]


	if "title" in app:
		print(webName(app["title"]))
	print("=" * 80)

	# Make icon for UniStore and QR
	img = None
	if "icon" in app or "image" in app:
		if not os.path.exists("temp"):
			os.mkdir("temp")

		if "icon" in app:
			r = requests.get(app["icon"])
		else:
			r = requests.get(app["image"])

		with Image.open(io.BytesIO(r.content)) as img:
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
			img.save(os.path.join("temp", str(iconIndex) + ".png"))
			icons.append(str(iconIndex) + ".png")
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
				qr = qrcode.make(app["downloads"][item], box_size = 5).convert("RGBA")
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
				qr.save(os.path.join("..", "assets", "images", "qr", webName(item) + ".png"))
				if not "qr" in app:
					app["qr"] = {}
				app["qr"][item] = "https://db.universal-team.net/assets/images/qr/" + webName(item) + ".png"

	if "nightly" in app:
		for item in app["nightly"]["downloads"]:
			if item[item.rfind(".") + 1:] == "cia":
				qr = qrcode.make(app["nightly"]["downloads"][item], box_size = 5).convert("RGBA")
				data = numpy.array(qr)
				r, g, b, a = data.T
				black = (r == 0) & (g == 0) & (b == 0)
				data[...][black.T] = (0, 0, 0xC0, 0xFF)
				qr = Image.fromarray(data)
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
				qr.save(os.path.join("..", "assets", "images", "qr", "nightly", webName(item) + ".png"))
				if not "qr" in app["nightly"]:
					app["nightly"]["qr"] = {}
				app["nightly"]["qr"][item] = "https://db.universal-team.net/assets/images/qr/nightly/" + webName(item) + ".png"

	# Add to output json
	output.append(app)

	# Website file
	web = app.copy()
	web["layout"] = "app"
	if "long_description" in web:
		web.pop("long_description")
	if not "systems" in web:
		web["systems"] = ["3DS"] # default to 3DS
	if not "updated" in web:
		web["updated"] = "---"
	for system in web["systems"]:
		if "title" in web:
			with open(os.path.join("..", "_" + webName(system), webName(web["title"]) + ".md"), "w", encoding="utf8") as file:
				file.write("---\n" + yaml.dump(web) + "---\n")
				if "long_description" in app:
					file.write(app["long_description"])

	# Create copy with filler items for UniStore base
	appCopy = app.copy()
	if not "title" in app:
		appCopy["title"] = ""
	if not "version" in app:
		appCopy["version"] = ""
	if not "author" in app:
		appCopy["author"] = ""
	if not "categories" in app:
		appCopy["categories"] = [""]
	if not "systems" in app:
		appCopy["systems"] = [""]
	if not "description" in app:
		appCopy["description"] = ""

	# Add entry for UniStore
	uni = {
		"info": {
			"title": appCopy["title"],
			"version": appCopy["version"],
			"author": appCopy["author"],
			"category": " / ".join(appCopy["categories"]),
			"console": " / ".join(appCopy["systems"]),
			"icon_index": len(icons) - 1 if "icon" in app or "image" in app else -1,
			"description": appCopy["description"],
		}
	}
	if "updated" in app:
		uni["info"]["last_updated"] = parser.parse(app["updated"]).strftime("%Y-%m-%d at %H:%M (UTC)")

	# If scripts are specified, use those instead of the release files
	if "scripts" in app:
		for script in app["scripts"]:
			uni[script] = app["scripts"][script]
	else:
		if "downloads" in app:
			for file in app["downloads"]:
				uni["Download " + file] = downloadScript(file, app["downloads"][file])

		if "prerelease" in app:
			for file in app["prerelease"]["downloads"]:
				uni["[prerelease] Download " + file] = downloadScript(file, app["prerelease"]["downloads"][file])

		if "nightly" in app:
			for file in app["nightly"]["downloads"]:
				uni["[nightly] Download " + file] = downloadScript(file, app["nightly"]["downloads"][file])

	unistore["storeContent"].append(uni)

	# Add authors, categories, and systems are to the unistore in not already in
	for category in app["categories"]:
		if not category in unistore["storeInfo"]["categories"]:
			unistore["storeInfo"]["categories"].append(category)

	if "author" in app and not app["author"] in unistore["storeInfo"]["authors"]:
		unistore["storeInfo"]["authors"].append(app["author"])

	for system in app["systems"]:
		if not system in unistore["storeInfo"]["consoles"]:
			unistore["storeInfo"]["consoles"].append(system)

# Make t3x
with open(os.path.join("temp", "icons.t3s"), "w", encoding="utf8") as file:
	file.write("--atlas -f rgba -z auto\n\n")
	for icon in icons:
		file.write(icon + "\n")
os.system("tex3ds -i " + os.path.join("temp", "icons.t3s") + " -o " + os.path.join("..", "unistore", "universal-db.t3x"))

# Increment revision if not the same
if unistore != unistoreOld:
	unistore["storeInfo"]["revision"] += 1

# Write unistore to file
with open(os.path.join("..", "unistore", "universal-db.unistore"), "w", encoding="utf8") as file:
	file.write(json.dumps(unistore, sort_keys=True))

# Write output file
with open(os.path.join("..", "data", "full.json"), "w", encoding="utf8") as file:
	file.write(json.dumps(output, sort_keys=True))

# RSS feed
feedItems = []
latestUpdate = None
output.sort(key=lambda item: item["updated"] if "updated" in item else "---", reverse=True)
for item in output:
	if "updated" in item and (latestUpdate == None or parser.parse(item["updated"]) > latestUpdate):
		latestUpdate = parser.parse(item["updated"])

	if "updated" in item and (datetime.datetime.now(datetime.timezone.utc) - parser.parse(item["updated"])).days < 30:
		feedItems.append(rfeed.Item(
			title = "New " + item["title"] + " update",
			link = "https://db.universal-team.net/" + webName(item["systems"][0]) + "/" + webName(item["title"]),
			description = item["version_title"] if "version_title" in item else item["version"],
			author = item["author"],
			guid = rfeed.Guid("https://db.universal-team.net/" + webName(item["systems"][0]) + "/" + webName(item["title"])),
			pubDate = parser.parse(item["updated"]),
			categories = item["systems"],
			extensions = [
				rfeed.Enclosure(
					url = item["image"],
					length = len(requests.get(item["image"]).content),
					type = "image/png"
				) if "image" in item else None
			]
		))

if len(feedItems) > 0:
	feed = rfeed.Feed(
		title = "Universal DB",
		link = "https://db.universal-team.net",
		description = "A database of DS and 3DS homebrew",
		language = "en-US",
		lastBuildDate = latestUpdate,
		pubDate = latestUpdate,
		items = feedItems,
		image = rfeed.Image(title = "Universal DB", url = "https://universal-team.net/images/icons/universal-team.png", link = "https://db.universal-team.net"),
	)

	with open(os.path.join("..", "index.rss"), "w", encoding="utf8") as file:
		file.write(feed.rss())

# Push notification
if len(sys.argv) > 3:
	items = []
	for oldItem in oldData:
		for newItem in output:
			if oldItem["title"] == newItem["title"] and oldItem["author"] == newItem["author"] and "version" in oldItem and "version" in newItem and oldItem["version"] != newItem["version"]:
				items.append(newItem)

	if len(items) > 0:
		heading = ""
		content = ""
		path = ""
		segments = []
		if len(items) == 1:
			heading = "New " + items[0]["title"] + " update"
			content = (items[0]["version_title"] + "\n" if "version_title" in items[0] else "") + "Click to open on Universal DB"
			segments = items[0]["systems"]
			path = items[0]["systems"][0] + "/" + webName(items[0]["title"])
			print(heading)
			print(content)
			print(segments)
		elif len(items) > 1:
			for item in items:
				for system in item["systems"]:
					if system not in segments:
						segments.append(system)

			heading = "New " + " and ".join(segments) + " updates"
			content = "Click to open on Universal DB"
			path = segments[0] if len(segments) == 1 else ""
			print(heading)
			print(content)
			print(segments)

		if heading and content and segments:
			headers = {
				"Authorization": "Basic <" + sys.argv[2] + ">",
				"Content-Type": "application/json; charset=utf-8",
			}

			data = {
				"app_id": sys.argv[3],
				"contents": {"en": content},
				"headings": {"en": heading},
				"included_segments": segments,
				"url": "https://db.universal-team.net/" + path
			}

			requests.post("https://onesignal.com/api/v1/notifications", headers=headers, json=data)
