from __future__ import annotations

import json
import re
from typing import Optional

import pathlib

ICONS_PER_SHEET = 400


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
	color
		(optional) Accent color for the entry (in the format `#RRGGBB`)
	stars
		(optional) Stars for the entry
	preinstallMessage
		(optional) Pre-install message for the entry
	titleIds
		(optional) Title ID(s) of the app
	installedFiles
		(optional) The files that indicate the app is installed
	"""

	@staticmethod
	def _bmpOnly(string: str) -> str:
		"""Filters a string to only use characters in the Basic Multilingual Plane"""

		return "".join([c for c in string if ord(c) < 0xFFFF]).strip()

	def __init__(self, title: str, author: str, description: str, version: str, lastUpdated: str = "", categories: list = [], consoles: list = [], screenshots: list = [], releaseNotes: str = "", license: str = "", wiki: str = "", iconIndex: int = -1, color: str = "", stars: int = 0, preinstallMessage: str = "", titleIds: list = [], installedFiles: list = []):
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
				"icon_index": iconIndex if iconIndex < 0 else iconIndex % ICONS_PER_SHEET,
				"sheet_index": iconIndex // ICONS_PER_SHEET,
				"stars": stars,
				"preinstall_message": self._bmpOnly(preinstallMessage),
				"title_ids": titleIds,
				"installed_files": installedFiles.copy()
			}
		}
		if color:
			self._entry["info"]["color"] = color

	def addInstalledFile(self, file):
		if file not in self._entry["info"]["installed_files"]:
			self._entry["info"]["installed_files"].append(file)

	def addScript(self, scriptName: str, script: list):
		"""Adds the given script"""

		self._entry[scriptName] = script

	def addDownloadScript(self, scriptName: str, file: str, url: str, archive: tuple = None, size: str = None, releaseType: str = None, retroarch: bool = False) -> None:
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
					output = f"%3DSX%/{item[item.rfind('/') + 1:]}"
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"^{item}",
						"output": output
					})
					self.addInstalledFile(output)
				elif item[item.rfind(".") + 1:].lower() in ["nds", "dsi"]:
					output = f"%NDS%/{item[item.rfind('/') + 1:]}"
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"^{item}",
						"output": output
					})
					self.addInstalledFile(output)
				elif item[item.rfind(".") + 1:].lower() == "cia":
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"^{item}",
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
					output = f"/{item[item.rfind('/') + 1:]}"
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"^{item}",
						"output": output
					})
					self.addInstalledFile(output)
				elif item[item.rfind(".") + 1:].lower() == "firm":
					output = f"%FIRM%/{item[item.rfind('/') + 1:]}"
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"^{item}",
						"output": output
					})
					self.addInstalledFile(output)
				else:
					script.append({
						"type": "extractFile",
						"file": f"/{file}",
						"input": f"^{item}",
						"output": f"/{item}"
					})

			script.append({
				"type": "deleteFile",
				"file": f"/{file}"
			})
		else:
			if file[file.rfind(".") + 1:].lower() == "3dsx":
				output = f"%3DSX%/{file}"
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": output
					}
				]
				self.addInstalledFile(output)
			elif file[file.rfind(".") + 1:].lower() in ["nds", "dsi"]:
				output = f"%NDS%/{file}"
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": output
					}
				]
				self.addInstalledFile(output)
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
				output = f"/{file}"
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": output
					}
				]
				self.addInstalledFile(output)
			elif file[file.rfind(".") + 1:].lower() == "firm":
				output = f"%FIRM%/{file}"
				script = [
					{
						"type": "downloadFile",
						"file": url,
						"output": output
					}
				]
				self.addInstalledFile(output)
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
	bgImage
		(optional) If there is a background image
	"""

	def __init__(self, title: str, author: str, description: str, url: str, sheetURLs: list[str] = "", dsSheetURL: str = "", infoURL: str = "", bgImage: bool = False) -> None:
		self._unistore = {
			"storeInfo": {
				"title": title,
				"author": author,
				"description": description,
				"url": url,
				"file": url[url.rfind("/") + 1:],
				"sheetURL": sheetURLs,
				"sheet": [url[url.rfind("/") + 1:] for url in sheetURLs],
				"dsSheetURL": dsSheetURL,
				"dsSheet": dsSheetURL[dsSheetURL.rfind("/") + 1:],
				"infoURL": infoURL,
				"bg_index": 0 if bgImage else -1,
				"bg_sheet": 0 if bgImage else -1,
				"version": 3,
				"revision": 0
			},
			"storeContent": [],
		}

	def append(self, entry: StoreEntry) -> None:
		"""Appends an entry to the storeConty list"""

		self._unistore["storeContent"].append(entry._entry)

	def save(self, output: pathlib.Path, infoPath: Optional[pathlib.Path] = None) -> None:
		"""Increments the revision and saves to a file if changed"""
		write = True

		# If the file already exists, read it and increment the revision if changed
		if output.exists():
			with output.open(encoding="utf8") as oldFile:
				oldData = json.load(oldFile)
				if "storeInfo" in oldData and "revision" in oldData["storeInfo"]:
					self._unistore["storeInfo"]["revision"] = oldData["storeInfo"]["revision"]
					write = False

				if self._unistore != oldData:
					self._unistore["storeInfo"]["revision"] += 1
					write = True

		if write:
			with output.open("w", encoding="utf8") as outputFile:
				json.dump(self._unistore, outputFile, sort_keys=True, ensure_ascii=False)

			if infoPath:
				with infoPath.open("w", encoding="utf8") as infoFile:
					json.dump(self._unistore["storeInfo"], infoFile, sort_keys=True, ensure_ascii=False)
