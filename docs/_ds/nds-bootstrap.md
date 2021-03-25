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
    size: 441863
    size_str: 431 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.38.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1260270
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.38.0/nds-bootstrap.zip
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
update_notes: '<p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v19.1.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v19.1.0</a></p>

  <p>Instructions:</p>

  <ol>

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li>Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p><strong>Changelog</strong></p>

  <ul>

  <li>When reading the ROM, the FAT code is now run on arm9, instead of arm7.

  <ul>

  <li>This saves overhead on arm7, so sound will no longer be delayed on some SD cards
  during reads, and local multiplayer will no longer stop with a communication error.</li>

  <li>arm7 itself still does the sector reading of arm7.</li>

  <li>(<strong>NOTE:</strong> This does not mean that cloneboot support is implemented,
  so games using DLP for multiplayer will still crash on the other console.)</li>

  </ul>

  </li>

  <li>Proper DMA patches have been fixed and re-enabled!

  <ul>

  <li>As a result, game compatibility has been slightly increased, with games such
  as <em>Army Men: Soldiers of Misfortune</em> now booting!</li>

  <li>If this causes local multiplayer to crash the game, you can turn off the card
  read DMA feature in TWLMenu++, in either the settings menu, or the per-game settings
  menu.</li>

  </ul>

  </li>

  <li>Some game compatibility regressions have been fixed, so games such as <em>Dragon
  Quest V</em> and <em>Chrono Trigger</em> now boot again!</li>

  </ul>'
updated: '2021-03-25T05:35:39Z'
version: v0.38.0
version_title: v0.38.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.