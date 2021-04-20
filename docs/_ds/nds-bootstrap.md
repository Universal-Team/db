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
    size: 451596
    size_str: 441 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.39.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1282461
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.39.0/nds-bootstrap.zip
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
update_notes: "<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v20.0.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v20.0.0</a></p>\n<p>Instructions:</p>\n\
  <ol>\n<li>Download the <code>.7z</code> file.</li>\n<li>Extract the nds-bootstrap\
  \ <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n<li>Extract the <code>.ver</code>\
  \ file to <code>root:/_nds/TWiLightMenu</code>.</li>\n</ol>\n<p><strong>What's new?</strong></p>\n\
  <ul>\n<li>You asked, we listened, and now the wait is over, and the day has finally\
  \ come!<br>\nAfter years of playing DS\u207D\u2071\u207E-Enhanced games in DS mode,\
  \ whether it be on a flashcard or the console's SD card, DS\u207D\u2071\u207E mode\
  \ has finally been added (with some help from <a class=\"user-mention\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/shutterbug2000/hovercard\" data-octo-click=\"\
  hovercard-link-click\" data-octo-dimensions=\"link_type:self\" href=\"https://github.com/shutterbug2000\"\
  >@shutterbug2000</a>)!\n<ul>\n<li>With DS\u207D\u2071\u207E mode, you can play DS\u207D\
  \u2071\u207E-Enhanced games with features only usable on DS\u207D\u2071\u207E or\
  \ 3DS consoles, such as faster speed, camera, and/or using WPA1/2 networks to connect\
  \ to the internet.</li>\n<li>As a result, you can play all 5 of the physical DS\u207D\
  \u2071\u207E-Exclusive games as ROMs, which are\n<ul>\n<li><em>System Flaw</em></li>\n\
  <li><em>Foto Showdown</em></li>\n<li><em>Picture Perfect Hair Salon</em></li>\n\
  <li>and the rest (which are exclusive to Europe)</li>\n</ul>\n</li>\n<li>Also as\
  \ a result, you can play some DS\u207D\u2071\u207EWare titles, such as\n<ul>\n<li><em>Earthworm\
  \ Jim</em></li>\n<li><em>Shantae: Risky's Revenge</em></li>\n<li><em>The Legend\
  \ of Zelda: Four Swords: Anniversary Edition</em></li>\n<li><em>X-Scape</em></li>\n\
  <li>and more!</li>\n</ul>\n</li>\n<li>NOTE: Due to most of the memory being by the\
  \ game, the in-game menu is disabled, and attempting to open it will cause the game\
  \ to close.</li>\n</ul>\n</li>\n<li>Game region can be set for DS\u207D\u2071\u207E\
  -Exclusive and DS\u207D\u2071\u207EWare titles.\n<ul>\n<li>NOTE: Not all games are\
  \ multi-regional, so the feature won't work for some of them.</li>\n</ul>\n</li>\n\
  </ul>\n<p><strong>Bug fixes</strong></p>\n<ul>\n<li>The missing sprite bug in <em>Mario\
  \ vs. Donkey Kong: Mini-Land Mayhem</em> is fixed by turning on DS\u207D\u2071\u207E\
  \ mode.</li>\n<li><em>Tom Clancy's Splinter Cell: Chaos Theory</em> now saves data.</li>\n\
  <li>Fixed sound in <em>Pokemon Ranger: Shadows of Almia</em>, if using either DSiWareHax\
  \ or forced DS\u207D\u2071\u207E mode.</li>\n<li>Fixed <em>Trauma Center: Under\
  \ the Knife</em> not booting.</li>\n<li>Fixed DMA reads to VRAM not working.</li>\n\
  <li>Fixed a bug causing potential crashes with ROMs loaded into the full extra RAM.</li>\n\
  <li>Minor code optimizations have been applied.</li>\n</ul>\n<p><strong>Known bugs</strong></p>\n\
  <ul>\n<li>DS\u207D\u2071\u207EWare saving currently doesn't work, so some games\
  \ may not start as a result.</li>\n<li>When restarting <em>Face Training</em>, after\
  \ successfully saving, it'll show that the save is corrupted.</li>\n<li>In <em>Hidden\
  \ Photo</em>, while a puzzle loads, it'll crash after some seconds.</li>\n</ul>"
updated: '2021-04-20T06:17:40Z'
version: v0.39.0
version_title: "D\u207D\u2071\u207Erectors' Cut"
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.