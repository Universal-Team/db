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
    size: 324428
    size_str: 316 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.40.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 842414
    size_str: 822 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.40.2/nds-bootstrap.zip
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
  </ol>\n<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v20.2.1\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v20.2.1</a></p>\n<p><strong>Bug\
  \ fixes</strong></p>\n<ul>\n<li>Fixed <em>Final Fantasy Crystal Chronicles: Echoes\
  \ of Time</em> not booting.</li>\n<li>Fixed crashes in <em>Mario &amp; Luigi: Bowser's\
  \ Inside Story</em>.\n<ul>\n<li>This does not fix the bug where loading a save file\
  \ would sometimes crash the game.</li>\n</ul>\n</li>\n<li>Games now boot in B4DS\
  \ mode from flashcards again!</li>\n<li><strong>B4DS mode:</strong> Hi heap has\
  \ been shrunken further, giving more room in RAM for the FAT table, slightly increases\
  \ compatibility, and fixes WiFi crashing the game without a Memory Expansion Pak,\
  \ as a result.</li>\n<li>Fixed bug where some DS\u207D\u2071\u207E-Enhanced games\
  \ (including the <em>Pop Island</em> games) wouldn't start via DSiWarehax.</li>\n\
  </ul>"
updated: '2021-05-19T07:53:32Z'
version: v0.40.2
version_title: v0.40.2
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.