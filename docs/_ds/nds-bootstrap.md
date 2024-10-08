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
    size: 802248
    size_str: 783 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.0.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1147611
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.0.2/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1176
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.10.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.10.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Two DSiWare apps, <em>Animal Crossing Calculator</em>
  &amp; <em>Mario Calculator</em> now boot on DS and DS Lite consoles!

  <ul dir="auto">

  <li>Either a Memory Expansion Pak or a DS Debug/Dev console is required.</li>

  <li>The European/Australian version of <em>Animal Crossing Calculator</em> only
  works on a DS Debug/Dev console.</li>

  </ul>

  </li>

  <li>For a tiny speed boost during CPU ROM reads from DSi/3DS SD card, the FAT code
  has been moved back to ARM9, along with the IPC Sync IRQ on ARM7 doing SD sector
  reads again.

  <ul dir="auto">

  <li>No new wireless communication issues have been found so far. The same issues
  that have occurred since the release which has improved wireless stability will
  still occur.</li>

  <li>DMA ROM reads and NAND save R/W will still have arm7 run the FAT code while
  on the main loop.</li>

  </ul>

  </li>

  <li>NitroFS FNT/FAT info will now pre-load into DSi WRAM when available.</li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Fixed a bug which could cause low quality sound
  output on DSi/3DS consoles.

  <ul dir="auto">

  <li>Also fixes mic. test in Pokemon B&amp;W 1&amp;2 (and possibly other games) on
  DSi.</li>

  </ul>

  </li>

  </ul>'
updated: '2024-10-03T23:58:11Z'
version: v2.0.2
version_title: v2.0.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.