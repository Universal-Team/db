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
