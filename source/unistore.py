import json
import re

from os import path


class StoreEntry:
	"""
	UniStore entry class

	Parameters
	----------
	title
		The title of the entry
	author
		The author of the entry
	description
		The description of the entry
	version
		The version of the entry
	lastUpdated
		(optional) The last update date as a string, YYYY-MM-DD recommended
	categories
		(optional) List of categories for the entry
	consoles
		(optional) List of consoles the entry is for
	screenshots
		(optional) List of URLs to screenshots in PNG format
	releaseNotes
		(optional) Release notes for the entry
	license
		(optional) The license of the entry
	wiki
		(optional) URL to the entry's wiki
	iconIndex
		(optional) The entry's icon's index in the spritesheet
	"""

	@staticmethod
	def _bmpOnly(string: str) -> str:
		"""Filters a string to only use characters in the Basic Multilingual Plane"""

		return "".join([c for c in string if ord(c) < 0xFFFF]).strip()

	def __init__(self, title: str, author: str, description: str, version: str, lastUpdated: str = "", categories: list = [], consoles: list = [], screenshots: list = [], releaseNotes: str = "", license: str = "", wiki: str = "", iconIndex: int = -1):
		self._entry = {
			"info": {
				"title": self._bmpOnly(title),
				"author": self._bmpOnly(author),
				"description": self._bmpOnly(description),
				"version": self._bmpOnly(version),
				"last_updated": self._bmpOnly(lastUpdated),
				"category": [self._bmpOnly(x) for x in categories],
				"console": [self._bmpOnly(x) for x in consoles],
				"screenshots": screenshots,
				"releasenotes": self._bmpOnly(releaseNotes),
				"license": self._bmpOnly(license),
				"wiki": wiki,
				"icon_index": iconIndex,
			}
		}

	def addScript(self, scriptName: str, script: list):
		"""Adds the given script"""

		self._entry[scriptName] = script

	def addDownloadScript(self, scriptName: str, file: str, url: str, message: str = None, archive: tuple = None, size: str = None, releaseType: str = None, retroarch: bool = False) -> None:
		"""Generates a script to download the given file"""

		if releaseType not in (None, "nightly", "prerelease"):
			raise Exception('Invalid releaseType, must be None, "nightly", or "prerelease".')

		if archive:
			script = [
				{
					"type": "downloadFile",
					"file": url,
					"output": f"/{file}"
				}
			]

			for item in archive:
				if item[item.rfind(".") + 1:].lower() == "3dsx":
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"{item}",
						"output": f"%3DSX%/{item[item.rfind('/') + 1:]}"
					})
				elif item[item.rfind(".") + 1:].lower() in ["nds", "dsi"]:
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"{item}",
						"output": f"%NDS%/{item[item.rfind('/') + 1:]}"
					})
				elif item[item.rfind(".") + 1:].lower() == "cia":
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"{item}",
						"output": f"/{item[item.rfind('/') + 1:]}"
					})

					script.append({
						"type": "installCia",
						"file": f"/{item[item.rfind('/') + 1:]}"
					})

					if retroarch:
						script.append({
							"type": "move",
							"old": f"/{item[item.rfind('/') + 1:]}",
							"new": f"/retroarch/cores/{item[item.rfind('/') + 1:]}"
						})
					else:
						script.append({
							"type": "deleteFile",
							"file": f"/{item[item.rfind('/') + 1:]}"
						})
				elif item.endswith("boot.firm"):
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"{item}",
						"output": f"/{item[item.rfind('/') + 1:]}"
					})
				elif item[item.rfind(".") + 1:].lower() == "firm":
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"{item}",
						"output": f"%FIRM%/{item[item.rfind('/') + 1:]}"
					})
				else:
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"{item}",
						"output": f"/{item}"
					})

			script.append({
				"type": "deleteFile",
				"file": f"/{file}"
			})
		else:
			if file[file.rfind(".") + 1:].lower() == "3dsx":
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"%3DSX%/{file}"
					}
				]
			elif file[file.rfind(".") + 1:].lower() in ["nds", "dsi"]:
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"%NDS%/{file}"
					}
				]
			elif file[file.rfind(".") + 1:].lower() == "cia":
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"/{file}"
					},
					{
						"type": "installCia",
						"file": f"/{file}"
					},
					{
						"type": "deleteFile",
						"file": f"/{file}"
					}
				]
			elif file == "boot.firm":
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"/{file}"
					}
				]
			elif file[file.rfind(".") + 1:].lower() == "firm":
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"%FIRM%/{file}"
					}
				]
			elif file[file.rfind(".") + 1:].lower() in ["zip", "7z", "rar"]:
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"/{file}"
					},
					{
						"type": "extractFile",
						"file": f"/{file}",
						"input": "",
						"output": f"%ARCHIVE_DEFAULT%/{file[0:file.find('.')]}/"
					},
					{
						"type": "deleteFile",
						"file": f"/{file}"
					}
				]
			else:
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": f"/{file}"
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

		if releaseType:
			script = {
				"type": releaseType if releaseType else "",
				"script": script
			}

			scriptName = f"[{releaseType}] {scriptName}"

		if size:
			if type(script) == dict:  # Already made into dict by release type
				script["size"] = size
			else:
				script = {
					"size": size,
					"script": script
				}

		self.addScript(scriptName, script)


class UniStore:
	"""
	UniStore class

	Parameters
	----------
	title
		The title of the UniStore
	author
		Author of the UniStore
	description
		Description of the UniStore
	url
		URL to download UniStore updates from
	sheetURL
		(optional) URL to download the 3DS spritesheet from
	dsSheetURL
		(optional) URL to download the DS spritesheet from
	infoURL
		(optional) URL to storeInfo-only UniStore for quicker update checking
	file
		(optional) Filename to store as, defaults to based on url
	sheet
		(optional) Filename to store 3DS spritesheet as, defaults to based on sheetURL
	dsSheet
		(optional) Filename ot store DS spritesheet as, defaults to based on dsSheetURL
	revision
		(optional) The previous revision of the UniStore, defaults to 0, incremented on save

	"""

	def __init__(self, title: str, author: str, description: str, url: str, sheetURL: str = "", dsSheetURL: str = "", infoURL: str = "", file: str = None, sheet: str = None, dsSheet: str = None) -> None:
		self._unistore = {
			"storeInfo": {
				"title": title,
				"author": author,
				"description": description,
				"url": url,
				"file": file if file else url[url.rfind("/") + 1:],
				"sheetURL": sheetURL,
				"sheet": sheet if sheet else sheetURL[sheetURL.rfind("/") + 1:],
				"dsSheetURL": dsSheetURL,
				"dsSheet": dsSheet if dsSheet else dsSheetURL[dsSheetURL.rfind("/") + 1:],
				"infoURL": infoURL,
				"version": 3,
				"revision": 0
			},
			"storeContent": [],
		}

	def append(self, entry: StoreEntry) -> None:
		"""Appends an entry to the storeConty list"""

		self._unistore["storeContent"].append(entry._entry)

	def save(self, outputPath: str, infoPath: str = None) -> None:
		"""Increments the revision and saves to a file if changed"""

		write = True

		# If the file already exists, read it and increment the revision if changed
		if path.exists(outputPath):
			with open(outputPath, encoding="utf8") as oldFile:
				oldData = json.load(oldFile)
				if "storeInfo" in oldData and "revision" in oldData["storeInfo"]:
					self._unistore["storeInfo"]["revision"] = oldData["storeInfo"]["revision"]
					write = False

				if self._unistore != oldData:
					self._unistore["storeInfo"]["revision"] += 1
					write = True

		if write:
			with open(outputPath, "w", encoding="utf8") as outputFile:
				json.dump(self._unistore, outputFile, sort_keys=True, ensure_ascii=False)

			if infoPath:
				with open(infoPath, "w", encoding="utf8") as infoFile:
					json.dump(self._unistore["storeInfo"], infoFile, sort_keys=True, ensure_ascii=False)
