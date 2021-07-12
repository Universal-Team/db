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
    size: 367530
    size_str: 358 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.44.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 893244
    size_str: 872 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.44.0/nds-bootstrap.zip
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
  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v21.1.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v21.1.0</a></p>\n<p><strong>What's\
  \ new?</strong></p>\n<ul>\n<li>.nds/.srl files within the currently launched one,\
  \ can now be booted!\n<ul>\n<li>This allows Pok\xE9mon Gen 4 to proceed to the Wii\
  \ connection menu.</li>\n</ul>\n</li>\n</ul>\n<p><strong>What's new? / Bug fix</strong></p>\n\
  <ul>\n<li>Partial Cloneboot support has been implemented.\n<ul>\n<li>As this is\
  \ partial, it only works in some games (tested and working in <em>Mario Party DS</em>\
  \ and <em>Mario &amp; Sonic at the Olympic Winter Games</em>).</li>\n<li>The guest\
  \ console will require a patched Download Play mode, in order to avoid crashing\
  \ on the Nintendo logo.<br>\nDS/DS lite users can install <strong>FlashMe</strong>.<br>\n\
  Flashcard/DSi/3DS users can follow <a href=\"https://gbatemp.net/threads/rsa-patch-for-dsi-download-play.538078/\"\
  \ rel=\"nofollow\">this</a> guide.<br>\nThe requirement will (hopefully) be removed\
  \ when full Cloneboot support is implemented.</li>\n</ul>\n</li>\n</ul>\n<p><strong>Improvement</strong></p>\n\
  <ul>\n<li>FAT table cache read/write speed have been improved, so games may boot\
  \ slightly faster.\n<ul>\n<li>FAT table cache size is now stored.</li>\n<li>This\
  \ does not affect B4DS mode users.</li>\n</ul>\n</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n\
  <ul>\n<li>Fixed a regression which made some DS\u207D\u2071\u207EWare not boot.</li>\n\
  <li>Chances of the 3DS returning to the HOME Menu when either soft-resetting or\
  \ exiting the game to TWLMenu++ have been lowered.\n<ul>\n<li>This may not affect\
  \ some O3DS models, which always return to the HOME Menu as a result.</li>\n</ul>\n\
  </li>\n</ul>\n<p><strong>Known bug</strong></p>\n<ul>\n<li>When Pok\xE9mon Gen 4\
  \ attempts to connect to the Wii, it'll crash on white screens.</li>\n</ul>"
updated: '2021-07-12T07:36:49Z'
version: v0.44.0
version_title: v0.44.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.