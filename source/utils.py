from __future__ import annotations

import traceback
from datetime import datetime, timezone
from typing import Any, Dict, Union, List

from dateutil import parser
from unidecode import unidecode


def format_traceback(exc: Exception):
	etype = type(exc)
	trace = exc.__traceback__

	return ''.join(traceback.format_exception(etype, exc, trace))


def was_recently_updated(app: Dict[str, Any]) -> bool:
	if "updated" not in app:
		return False

	last_updated = parser.parse(app["updated"])
	days_since = (datetime.now(tz=timezone.utc) - last_updated).days
	return days_since <= 30


def get_matching_app(app: Dict[str, Any], old_data: List[Dict[str, Any]]) -> Union[Dict[str, Any], None]:
	"""Returns an app from old_data if exists, else None"""
	keys = [
		("github", lambda x: "github" in x and "github" in app and x["github"] == app["github"]),
		("gbatemp", lambda x: "gbatemp" in x and "gbatemp" in app and x["gbatemp"] == app["gbatemp"]),
		("bitbucket", lambda x: "bitbucket" in x and "bitbucket" in app and x["bitbucket"]["repo"] == app["bitbucket"]["repo"]),
		("gitlab", lambda x: "gitlab" in x and "gitlab" in app and x["gitlab"] == app["gitlab"]),
		("manual", lambda x: "title" in x and "author" in x and "title" in app and "author" in app and x["title"] == app["title"] and x["author"] == app["author"])
	]
	for key, func in keys:
		if match := list(filter(func, old_data)):
			return match[0]

	return None


def format_to_web_name(name: str) -> str:
	"""Convert names to lowercase alphanumeric, underscore, and hyphen"""
	name = unidecode(name).lower()
	out = ""
	for letter in name:
		if letter in "abcdefghijklmnopqrstuvwxyz0123456789-_":
			out += letter
		elif letter in ". ":
			out += "-"
	return out


def to_friendly_bytes(bytes: int) -> str:
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

def format_source_path(path):
	"""Formats a source path for installation instructions"""

	source = path.replace("^", "/").replace(".*", "*").replace("\\", "")

	if source == "":
		source = "everything"
	elif source.endswith("/"):
		source = f"the contents of <code>{source}</code>"
	else:
		source = f"<code>{source}</code>"

	return source

def format_destination_path(path):
	"""Formats a destination path for installation instructions"""

	dest = path.replace("%3DSX%", "/3ds").replace("%FIRM%", "/luma/payloads")
	if dest.endswith(".cia"):
		dest = "/cias" + dest

	if "%NDS%" in dest:
		dest = "where you keep NDS files on your SD card"
	elif dest == "/":
		dest = "the root of your SD card"
	else:
		dest = f"<code>{dest}</code> on your SD card"

	return dest

def create_installation_instructions(script):
	"""Creates HTML installation instructions based on a Universal-Updater script"""

	i = 0
	deferedSteps = []
	instructions = "<ol>\n"

	for step in script:
		i += 1

		if step["type"] == "copy":
			instructions += f"<li>Copy <code>{step['source']}</code> to <code>{step['destination']}</code></li>\n"

		elif step["type"] == "downloadRelease" or step["type"] == "downloadFile":
			# Clean up regex
			file = step['file'].replace(".*", "*").replace("\\", "")
			file = file[file.rfind("/") + 1:]
			output = step["output"]

			if output.endswith(".zip") or output.endswith(".7z"):
				instructions += f"<li>Download <code>{file}</code></li>\n"
			else:
				instructions += f"<li>Download <code>{file}</code> to {format_destination_path(output)}</li>\n"

		elif step["type"] == "exit":
			instructions += f"<li>You're done!</li>\n"

		elif step["type"] == "extractFile":
			file = step["file"].replace("/", "")
			file = f"the {file[file.rfind('.') + 1:]}"

			source = format_source_path(step["input"])
			dest = format_destination_path(step["output"])

			instructions += f"<li>Extract {source} from {file} to {dest}</li>\n"

		elif step["type"] == "installCia":
			deferedSteps.append(step)
			i -= 1

		elif step["type"] == "mkdir":
			instructions += f"<li>Create the folder <code>{step['directory']}</code></li>\n"

		elif step["type"] == "mkdir":
			instructions += f"<li>Move <code>{step['old']}</code> to <code>{step['new']}</code></li>\n"

		elif step["type"] == "promptMessage":
			message = step["message"].replace("\n", " ")
			count = step["count"] if "count" in step else 0

			if count > 0:
				if (i + count + 1 >= len(script)) and len(deferedSteps) == 0:
					message += " If not, you're done!"
				else:
					message += f" If not, skip to step {i + count + 1}"

			instructions += f"<li>{message}</li>\n"

		elif step["type"] == "skip":
			instructions += f"<li>skip to step {i + step['count'] + 1}</li>\n"

		else:
			i -= 1  # Step was ignored

	if len(deferedSteps) > 0:
		i += 1
		instructions += f"<li>Insert your SD card back into your 3DS and turn it on</li>\n"

		for step in deferedSteps:
			i += 1

			if step["type"] == "installCia":
				instructions += f"<li>Install and delete <code>/cias{step['file']}</code> using FBI or GodMode9</li>\n"

	return instructions + "</ol>"
