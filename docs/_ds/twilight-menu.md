---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases
downloads:
  TWiLightMenu-3DS.7z:
    size: 34183007
    size_str: 32 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.2.1/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 34200208
    size_str: 32 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.2.1/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 47303050
    size_str: 45 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.2.1/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 47479393
    size_str: 45 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.2.1/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
image: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/logo.png
image_length: 142608
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    TWiLightMenu-3DS.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-3DS.7z
    TWiLightMenu-DSi.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-DSi.7z
    TWiLightMenu-Flashcard.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Flashcard.7z
    TWiLightMenu.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu.7z
priority: true
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: "<p>Check here on how to update <strong>TW</strong>i<strong>L</strong>ight\
  \ Menu++:</p>\n<ul>\n<li><a href=\"https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html\"\
  \ rel=\"nofollow\">Flashcard</a></li>\n<li><a href=\"https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html\"\
  \ rel=\"nofollow\">DSi</a></li>\n<li><a href=\"https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html\"\
  \ rel=\"nofollow\">3DS</a></li>\n</ul>\n<p>Includes <a href=\"https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.40.2\"\
  >nds-bootstrap v0.40.2</a></p>\n<p><strong>What's removed?</strong></p>\n<ul>\n\
  <li>The <code>Last played ROM</code> feature has unfortunately been removed from\
  \ the settings menu, but you can still start it on boot by holding B.\n<ul>\n<li>Why\
  \ this was removed is because a lot of users didn't pay attention to the setting\
  \ description while enabling it. :P</li>\n</ul>\n</li>\n</ul>\n<p><strong>Improvement</strong></p>\n\
  <ul>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated translations.</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n<ul>\n<li>Fixed\
  \ DS\u207D\u2071\u207EWare saves with hex characters A-F in the size being created\
  \ incorrectly without a header.\n<ul>\n<li>You'll need to manually delete the DS\u207D\
  \u2071\u207EWare save, if the game still shows a save data/filesystem/download/system\
  \ memory error.</li>\n</ul>\n</li>\n<li>Fixed launching DS\u207D\u2071\u207EWare\
  \ (copied to SD) from flashcards booted in DS mode, where originally, launching\
  \ would reboot TWLMenu++.</li>\n<li>The flashcard DS\u207D\u2071\u207EWare in a\
  \ temporary SD location is now copied back to the flashcard only once, unless when\
  \ restarting the game on TWLMenu++ boot.</li>\n<li>Fixed <code>cheatData.bin</code>\
  \ not being created for DS\u207D\u2071\u207EWare.\n<ul>\n<li>Also fixed widescreen\
  \ cheats not being activated for DS\u207D\u2071\u207EWare on flashcards, if copied\
  \ to console SD.</li>\n</ul>\n</li>\n<li>Fixed WiFi being broken when running Slot-1\
  \ carts.</li>\n<li><strong>DS Classic Menu:</strong> The correct ROM directory is\
  \ now set when launching a game from either the SD card or flashcard.</li>\n<li>Fixed\
  \ Greek and Russian language text being in one line.</li>\n</ul>"
updated: '2021-05-19T08:10:54Z'
version: v20.2.1
version_title: v20.2.1
wiki: https://wiki.ds-homebrew.com/twilightmenu
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu) for help installing.