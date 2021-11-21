---
author: d0k3
avatar: https://avatars.githubusercontent.com/u/12467483?v=4
categories:
- utility
- firm
color: '#130000'
created: '2016-01-22T18:00:30Z'
description: 'GodMode9 Explorer - A full access file browser for the Nintendo 3DS
  console :godmode:'
download_page: https://github.com/d0k3/GodMode9/releases
downloads:
  GodMode9-v2.1.0-20211121131422.zip:
    size: 2583932
    size_str: 2 MiB
    url: https://github.com/d0k3/GodMode9/releases/download/v2.1.0/GodMode9-v2.1.0-20211121131422.zip
github: d0k3/GodMode9
icon_index: 144
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
image_length: 9316
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/d0k3/GodMode9
systems:
- 3DS
title: GodMode9
update_notes: "<p dir=\"auto\">We're early for christmas this year with a new release:\
  \ GodMode9 v2.1.0 comes with several new features and a truckload of bugfixes and\
  \ smaller improvements.</p>\n<p dir=\"auto\">This is new since the last release:</p>\n\
  <ul dir=\"auto\">\n<li>[new] Unicode support, including a special Unicode font created\
  \ for GodMode9 (<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a>)</li>\n\
  <li>[new] Support for mounting <code>certs.db</code>, including improvement of certs\
  \ handling (<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/luigoalma/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/luigoalma\">@luigoalma</a>)</li>\n<li>[new]\
  \ Support for SHA-1 checksums (<a class=\"user-mention\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/aspargas2/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/aspargas2\"\
  >@aspargas2</a>)</li>\n<li>[new] Raw cart dumper, accessible via R+A on cart drive</li>\n\
  <li>[improved] Wider support for flash chips on carts, including ir (<a class=\"\
  user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/dratini0/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/dratini0\">@dratini0</a>)</li>\n<li>[scripting] <code>SDSIZE</code>,\
  \ <code>SDFREE</code> and <code>NANDFREE</code> global variables</li>\n<li>[scripting]\
  \ Added <code>cartdump</code> command</li>\n<li>[fixed] Numerous bugfixes and small\
  \ improvements, too many to list</li>\n</ul>\n<p dir=\"auto\"><strong>Killer Feature:\
  \ Unicode support</strong><br>\nGodMode9 is no longer limited to just displaying\
  \ English, it now has proper support for Unicode text. To facilitate this change\
  \ there's also a new font format, a simple RIFF-based format called FRF, which you\
  \ can easily convert to using the \xB4fontriff.py\xB4 conversion script. The default\
  \ font has been updated to include the common accented Latin letters, Cyrillic for\
  \ Russian, and Hiragana/Katakana for Japanese and there's also a font with complete\
  \ JIS X 0208 support in the resources folder. You can also now type any character\
  \ (up to U+FFFF) in the keyboard by switching to the number input mode, typing the\
  \ codepoint, and pressing the U+ key. (ex. 0411 is \u0411 and 3042 is \u3042).</p>\n\
  <p dir=\"auto\"><strong>How do I update GodMode9?</strong><br>\n(Do I really need\
  \ to add that paragraph everytime?) You wouldn't believe how often we get that question\
  \ when we do a new release. It's actually very simple: Just replace <code>GodMode9.firm</code>\
  \ on your SD card with the file found in the release ZIP. You may also want to update\
  \ scripts, which are found in the <code>./gm9</code> folder inside the archive and\
  \ go to the same folder on your SD card.</p>\n<p dir=\"auto\"><strong>Special thanks</strong><br>\n\
  With the project now being over 5 years old, and all of us working on other stuff,\
  \ additionally to also having a real life(tm), the main devs (<a class=\"user-mention\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/aspargas2/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/aspargas2\">@aspargas2</a>, <a class=\"user-mention\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wolfvak/hovercard\" data-octo-click=\"\
  hovercard-link-click\" data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wolfvak\"\
  >@Wolfvak</a> and me) sometimes take the backseat, only doing smaller features,\
  \ bug fixes and general project maintenance. Gladly the void was filled by other\
  \ developers. Special thanks go to <a class=\"user-mention\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Epicpkmn11\"\
  >@Epicpkmn11</a> for Unicode support,<a class=\"user-mention\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/dratini0/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/dratini0\">@dratini0</a>\
  \ for his continued work on supporting flash chips in the cart dumper and <a class=\"\
  user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/luigoalma/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/luigoalma\">@luigoalma</a> who added support for mounting\
  \ <code>certs.db</code> in this release. It's not only the devs who we have to thank,\
  \ though, it's also the numerous people who point out problems and ask for features,\
  \ as well as everyone who's patient enough to help us out with testing. More special\
  \ thanks go to <a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/TimmSkiller/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/TimmSkiller\">@TimmSkiller</a> and <a\
  \ class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/mariomadproductions/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/mariomadproductions\">@mariomadproductions</a>, who\
  \ both helped us a lot to improve GodMode9. In fact, the people who helped make\
  \ this release a possibility are too numerous to list - thanks, all of you!</p>"
updated: '2021-11-21T12:21:56Z'
version: v2.1.0
version_title: GodMode9 v2.1.0
wiki: https://github.com/d0k3/GodMode9/wiki
---
