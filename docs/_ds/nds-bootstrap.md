---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 431935
    size_str: 421 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.54.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1044251
    size_str: 1019 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.54.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 141
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
update_notes: "<p dir=\"auto\">Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.1.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v24.1.0</a></p>\n<p dir=\"auto\"\
  >Instructions:</p>\n<ol dir=\"auto\">\n<li>Download the <code>.7z</code> file.</li>\n\
  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n\
  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p dir=\"auto\"><strong>What's new?</strong></p>\n<ul dir=\"auto\">\n<li>Added\
  \ support for two DS games!\n<ul dir=\"auto\">\n<li>Pok\xE9mon Dash</li>\n<li>Tropix!\
  \ Your Island Getaway</li>\n</ul>\n</li>\n</ul>\n<p dir=\"auto\"><strong>Improvements</strong></p>\n\
  <ul dir=\"auto\">\n<li>The card read DMA implementation has been improved further,\
  \ using code implemented by original developer <a class=\"user-mention\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ahezard/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ahezard\">@ahezard</a>,\
  \ and should fix sound issues and be less prone to crashes!\n<ul dir=\"auto\">\n\
  <li>Card Read DMA now works in DSi-Enhanced/Exclusive games in DSi mode as well.</li>\n\
  </ul>\n</li>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated translations.</li>\n</ul>\n<p dir=\"auto\"><strong>Bug fix</strong></p>\n\
  <ul dir=\"auto\">\n<li><em>Nintendo DS Browser</em> no longer shows the Memory Expansion\
  \ Pak message. (Does not apply to B4DS mode.)</li>\n</ul>\n<p dir=\"auto\"><strong>Known\
  \ bugs</strong></p>\n<ul dir=\"auto\">\n<li><em>Tropix! Your Island Getaway</em>\
  \ will tend to crash with card read DMA turned on. (TWLMenu++ will blacklist the\
  \ game from using it.)</li>\n<li><em>Tropix! Your Island Getaway</em> does not seem\
  \ to boot in B4DS mode.</li>\n<li><em>Nintendo DS Browser</em> crashes after the\
  \ logos on DSi consoles.</li>\n</ul>\n<p dir=\"auto\"><strong>FAQ</strong></p>\n\
  <ul dir=\"auto\">\n<li><strong>Q:</strong> What about <em>Golden Sun: Dark Dawn</em>?\
  \ Does that work now too?\n<ul dir=\"auto\">\n<li><strong>A:</strong> Nope. We still\
  \ don't know how to fix it. What's currently known, is that the crash occurs in\
  \ one of the ROM's overlays.<br>\nAs always, you can (1.) play the demo version\
  \ of the game, (2.) play from a flashcard, or (3.) play on the original cartridge.</li>\n\
  </ul>\n</li>\n</ul>"
updated: '2022-02-21T16:45:30Z'
version: v0.54.1
version_title: v0.54.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.