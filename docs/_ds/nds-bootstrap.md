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
    size: 325476
    size_str: 317 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.41.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 844434
    size_str: 824 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.41.0/nds-bootstrap.zip
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
update_notes: "<p>Instructions:</p>\n<ol>\n<li>Download the <code>.7z</code> file.</li>\n\
  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n\
  <li>Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v20.3.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v20.3.0</a></p>\n<p><strong>What's\
  \ new?</strong></p>\n<ul>\n<li>Cheats can now be used in B4DS mode!</li>\n<li>The\
  \ L+R+DOWN+B button combo to exit a game has been re-added!</li>\n</ul>\n<p><strong>Improvements</strong></p>\n\
  <ul>\n<li>Booting a game in DS\u207D\u2071\u207E mode is now slightly faster!</li>\n\
  <li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated in-game menu translations.</li>\n<li>When soft-resetting a game in B4DS\
  \ mode on DS\u207D\u2071\u207E or 3DS, the console now reboots instead of shutting\
  \ down.</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n<ul>\n<li>Some game compatibility\
  \ has been fixed! (ex. <em>Lunar Knights</em>, <em>Professor Layton</em>, <em>Inazuma\
  \ Eleven</em>, <em>Big Bang Mini</em>, etc.)</li>\n<li>The card read DMA alternative\
  \ (which caused random issues for some users) is no longer used, and has reverted\
  \ back to the regular card read DMA method, while still a bit buggy, is less buggier\
  \ than the alternative.</li>\n</ul>\n<p><strong>Regression</strong></p>\n<ul>\n\
  <li>Due to the DMA alternative no longer being used, there will be a few lags and/or\
  \ screen flickers returning in some games.</li>\n</ul>"
updated: '2021-05-27T02:32:58Z'
version: v0.41.0
version_title: v0.41.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.