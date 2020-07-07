# Run "pip3 install qrcode[pil] requests pyyaml python-dateutil numpy" to install dependencies

import datetime
from dateutil import parser
from PIL import Image, ImageDraw
import io
import json
import numpy
import os
import qrcode
import requests
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
	if file[file.find(".") + 1:].lower() == "3dsx":
		return [
			{
				"type": "downloadFile",
				"file": url,
				"output": "sdmc:/3ds/" + file,
				"message": "Downloading " + file + "..."
			}
		]
	elif file[file.find(".") + 1:].lower() == "cia":
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
	elif file[file.find(".") + 1:].lower() in ["zip", "7z", "rar"]:
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
		api = json.loads(requests.get("https://api.github.com/repos/" + app["github"], headers = header if header else None).content)
		releases = json.loads(requests.get("https://api.github.com/repos/" + app["github"] + "/releases", headers = header if header else None).content)
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
		api = json.loads(requests.get("https://api.bitbucket.org/2.0/repositories/" + app["bitbucket"]["repo"]).content)

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
			fileAPI = json.loads(requests.get("https://api.bitbucket.org/2.0/repositories/" + app["bitbucket"]["repo"] + "/src/master/" + download + "?format=meta").content)
			if not download in app["downloads"]:
				app["downloads"][download] = fileAPI["links"]["self"]["href"]

			if not "download_page" in app:
				app["download_page"] = "https://bitbucket.org/" + app["bitbucket"]["repo"] +"/src/master/" + download

			if not "version" in app:
				app["version"] = fileAPI["commit"]["hash"][:7]

			if not "updated" in app:
				commit = json.loads(requests.get(fileAPI["commit"]["links"]["self"]["href"]).content)
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
			img.thumbnail((48, 48))
			img.save(os.path.join("temp", str(iconIndex) + ".png"))
			icons.append(str(iconIndex) + ".png")
			iconIndex += 1

	# Output website page
	if "downloads" in app:
		for item in app["downloads"]:
			if item[item.find(".") + 1:] == "cia":
				qr = qrcode.make(app["downloads"][item], box_size = 5).convert("RGBA")
				if img:
					draw = ImageDraw.Draw(qr)
					draw.rectangle((((qr.size[0] - img.size[0]) // 2 - 5, (qr.size[1] - img.size[1]) // 2 - 5), ((qr.size[0] + img.size[0]) // 2 + 4, (qr.size[1] + img.size[1]) // 2 + 4)), fill = (255, 255, 255))
					qr.paste(img, ((qr.size[0] - img.size[0]) // 2, (qr.size[1] - img.size[1]) // 2), mask = img if img.mode == "RGBA" else None)
				qr.save(os.path.join("..", "assets", "images", "qr", webName(item) + ".png"))
				if not "qr" in app:
					app["qr"] = {}
				app["qr"][item] = "https://db.universal-team.net/assets/images/qr/" + webName(item) + ".png"
	
	# Add to output json
	output.append(app)

	# Website file
	web = app.copy()
	web["layout"] = "app"
	if "long_description" in web:
		web.pop("long_description")
	if not "systems" in web:
		web["systems"] = ["3DS"] # default to 3DS
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

	if "downloads" in app:
		for file in app["downloads"]:
			uni["Download " + file] = downloadScript(file, app["downloads"][file])

	if "prerelease" in app:
		for file in app["prerelease"]["downloads"]:
			uni["[prerelease] Download " + file] = downloadScript(file, app["prerelease"]["downloads"][file])

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
	file.write(json.dumps(unistore))

# Write output file
with open(os.path.join("..", "data", "full.json"), "w", encoding="utf8") as file:
	file.write(json.dumps(output))
