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
    size: 368790
    size_str: 360 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.45.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 895664
    size_str: 874 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.45.0/nds-bootstrap.zip
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
  </ol>\n<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v21.2.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v21.2.0</a></p>\n<p><strong>Bug\
  \ fixes</strong></p>\n<ul>\n<li>Infrared (IR) features now partially work again!\n\
  <ul>\n<li>As always, a DS game card with a built-in IR port is required.</li>\n\
  </ul>\n</li>\n<li><em>Pok\xE9mon HeartGold &amp; SoulSilver</em> will no longer\
  \ crash on black screens when trying to load save data.</li>\n<li>The traditional\
  \ patching method is now used for the DSiWare title, <em>Castle Conqueror: Against</em>,\
  \ in order for it to boot.</li>\n</ul>\n<p><strong>Known bugs</strong></p>\n<ul>\n\
  <li>Pok\xE9walker still doesn't connect.</li>\n<li>Due to the fix applied for <em>Castle\
  \ Conqueror: Against</em>, the game will not save, and the help menu will crash\
  \ the game.</li>\n</ul>"
updated: '2021-07-24T06:35:37Z'
version: v0.45.0
version_title: v0.45.0
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.