from __future__ import annotations

import traceback
from datetime import datetime, timezone
from typing import Any, Dict

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


def get_matching_app(app: Dict[str, Any], old_data):
	keys = [
	    ("github", lambda x: x.get("github") == app.get("github")),
	    ("gbatemp", lambda x: x.get("gbatemp") == app.get("gbatemp")),
	    ("bitbucket", lambda x: x.get("bitbucket", {}).get("repo") == app.get("bitbucket", {}).get("repo")),
	    ("title_author", lambda x: x.get("title") == app.get("title") and x.get("author") == app.get("author")),
	    ("gitlab", lambda x: x.get("gitlab") == app.get("gitlab"))
	]

	for _, match_func in keys:
		if matches := list(filter(match_func, old_data)):
			return matches[0]
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
