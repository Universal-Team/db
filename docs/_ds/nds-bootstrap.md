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
    size: 432087
    size_str: 421 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.55.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1042445
    size_str: 1018 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.55.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.2.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.2.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto"><strong>Improvements</strong></p>

  <ul dir="auto">

  <li>Card data of around the exact length is now loaded at once, whenever possible.</li>

  <li>FAT code has been optimized further.

  <ul dir="auto">

  <li>FAT table cache is no longer saved to a file.</li>

  </ul>

  </li>

  <li>Other minor improvements.</li>

  </ul>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Fixed THUMB games not booting (ex. <em>SEGA Superstars
  Tennis</em>, <em>GTA: Chinatown Wars</em> (MEP required), <em>Domo</em> games, etc.).</li>

  <li>Fixed DSi mode not working on flashcards (with either unlocked SCFG or if TWLMenu++
  runs in DSi mode).</li>

  <li><em>Nintendo DS Browser</em> no longer crashes on DSi consoles!</li>

  <li>Fixed <em>Dragon Quest V</em> going back to the company logo screens before
  the opening music first plays.

  <ul dir="auto">

  <li>If it still occurs, make sure the ROM read LEDs are turned off, or it may be
  caused by SD speed.</li>

  </ul>

  </li>

  <li>Master brightness is now cleared when an exception error occurs.</li>

  <li>Fixed DSi mode heap shrink on DSi consoles to avoid overwriting the AP-patched
  overlays.</li>

  <li><strong>B4DS mode:</strong> Fixed file writes not working correctly.</li>

  </ul>'
updated: '2022-03-11T01:31:35Z'
version: v0.55.0
version_title: v0.55.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.