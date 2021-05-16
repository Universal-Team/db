---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 322845
    size_str: 315 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.40.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 838626
    size_str: 818 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.40.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://raw.githubusercontent.com/DS-Homebrew/nds-bootstrap/master/retail/assets/icon.bmp
image: https://i.imgur.com/BFIu7xX.png
image_length: 5116
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: "<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v20.2.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v20.2.0</a></p>\n<p>Instructions:</p>\n\
  <ol>\n<li>Download the <code>.7z</code> file.</li>\n<li>Extract the nds-bootstrap\
  \ <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n<li>Extract the <code>.ver</code>\
  \ file to <code>root:/_nds/TWiLightMenu</code>.</li>\n</ol>\n<p><strong>What's new?</strong></p>\n\
  <ul>\n<li>DS\u207D\u2071\u207EWare titles on the SD card are now booted the same\
  \ way as Unlaunch and the DS\u207D\u2071\u207E System Menu boot them!\n<ul>\n<li>As\
  \ a result, saving now works, and DS\u207D\u2071\u207EWare compatibility is near-perfect!</li>\n\
  <li>Because no patching is done, you can no longer use the in-game menu button combo\
  \ to exit to TWLMenu++.</li>\n</ul>\n</li>\n<li>DS\u207D\u2071\u207E mode is now\
  \ usable on all flashcards booted in DS mode with SCFG enabled!\n<ul>\n<li>Make\
  \ sure nds-bootstrap is booted with TWL touch mode set (can be done by setting the\
  \ Slot-1 TWL touch option in TWLMenu++ Settings), or else the Camera feature won't\
  \ work, and may cause the game to crash.</li>\n<li>Trying to connect to the internet\
  \ will cause either a lockup, or a crash.</li>\n<li><strong>NOTE:</strong> This\
  \ feature will not make DS\u207D\u2071\u207E mode work on DS Phat/lite consoles.</li>\n\
  </ul>\n</li>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a>) Custom\
  \ in-game menu hotkey can now be set!</li>\n</ul>\n<p><strong>Improvement</strong></p>\n\
  <ul>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated in-game menu translations.</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n\
  <ul>\n<li>The card read DMA alternative is now applied for most games!</li>\n<li>Saving\
  \ now works in the EUR &amp; JAP versions of <em>Kirby Canvas Curse</em>!</li>\n\
  <li>Fixed freezing issue in <em>Pokemon HeartGold &amp; SoulSilver Versions</em>!</li>\n\
  <li>With IR support still being broken, Slot-1 is now disabled, regardless if the\
  \ game uses IR or not.\n<ul>\n<li>Fixes a bug where the game would exit when closing/opening\
  \ the console's lid.</li>\n</ul>\n</li>\n</ul>"
updated: '2021-05-15T22:32:45Z'
version: v0.40.0
version_title: v0.40.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.