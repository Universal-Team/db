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
    size: 33593081
    size_str: 32 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.1.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 33605403
    size_str: 32 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.1.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 46701706
    size_str: 44 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.1.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 46889799
    size_str: 44 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v20.1.0/TWiLightMenu.7z
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
  \ rel=\"nofollow\">3DS</a></li>\n</ul>\n<p>Includes <a href=\"https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.39.1\"\
  >nds-bootstrap v0.39.1</a></p>\n<p><strong>What's new?</strong></p>\n<ul>\n<li><code>DS\u207D\
  \u2071\u207E mode</code> is now the default <code>Run in</code> option!\n<ul>\n\
  <li><code>DS\u207D\u2071\u207E mode</code> will be treated as <code>DS mode</code>\
  \ when launching Slot-1 cartridges, unless if <code>Unlaunch</code> is set as the\
  \ <code>Slot-1 Launch Method</code>.</li>\n<li><strong>NOTE:</strong> If TWLMenu++\
  \ was installed before this version was released, you'll need to manually set the\
  \ option.</li>\n</ul>\n</li>\n<li><strong>DS Classic Menu:</strong> You can now\
  \ set an autorun title on your flashcard, if <code>autorun.inf</code> is on the\
  \ flashcard's SD root, as well as TWLMenu++ running from the console's SD card.\n\
  <ul>\n<li>Add <code>open=fat:/ndspath/game.nds</code> (example path) underneath\
  \ <code>[autorun.twl]</code>.</li>\n<li>After doing so, the set title will be displayed\
  \ as the top option on the bottom screen.</li>\n</ul>\n</li>\n<li>SNES ROMs are\
  \ now visible again when running in DSiWarehax, but attempting to launch one will\
  \ bring up a message, preventing the ROM from booting.</li>\n<li>When exiting a\
  \ game from nds-bootstrap, both the Nintendo DS\u207D\u2071\u207E and TWLMenu++\
  \ splash screens will now be skipped!</li>\n</ul>\n<p><strong>Improvement</strong></p>\n\
  <ul>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated translations.</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n<ul>\n<li>Fixed\
  \ AP-fixes for:\n<ul>\n<li><em>Pokemon Conquest</em>: Now boots in DS\u207D\u2071\
  \u207E mode</li>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/enler/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/enler\">@enler</a>) <em>Pokemon Black\
  \ &amp; White Versions 2</em>: No longer crashes after Professor intro or when loading\
  \ saved data, while in DS\u207D\u2071\u207E mode</li>\n<li>(<a class=\"user-mention\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/R-YaTian/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/R-YaTian\">@R-YaTian</a>) <em>Yuuzai x Muzai</em>: Now\
  \ boots past white screens</li>\n</ul>\n</li>\n<li>Removed old per-game MPU configurations,\
  \ so <em>New Super Mario Bros.</em> and games developed by Inti-Creates (ex. <em>MegaMan\
  \ ZX</em>, <em>ZX Advent</em>, <em>Zero Collection</em>, <em>Crayon Shin-Chan</em>,\
  \ etc.) will now boot in nds-bootstrap again.</li>\n</ul>"
updated: '2021-05-04T00:19:31Z'
version: v20.1.0
version_title: v20.1.0
wiki: https://wiki.ds-homebrew.com/twilightmenu
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu) for help installing.