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
    size: 430387
    size_str: 420 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.59.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1035347
    size_str: 1011 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.59.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 139
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.10.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.10.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>When connecting to Wii using a Pokemon Gen 4 title, the received SRL file is
  now booted!</li>

  <li>Homebrew bootloader has moved to NitroFS in order for loaders such as TWLMenu++
  to load it directly.</li>

  <li>You can now exit directly to TWLMenu++ without rebooting, when running a DSi-Enhanced/Exclusive
  title in DSi mode!</li>

  <li>Patch offset cache files have been renamed from <code class="notranslate">romname.bin</code>
  to TID &amp; CRC (ex. <code class="notranslate">VSOE-82A2.bin</code>).

  <ul dir="auto">

  <li>This allows .nds/.srl files launched from within one to have it''s own patch
  offset cache file.</li>

  </ul>

  </li>

  <li>ARM9i and ARM7i binaries of homebrew are now loaded.</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Soft-resetting in B4DS mode no longer turns off or reboots the console.</li>

  <li>DSi SD DLDI driver has been moved to the HB bootloader to cut down the HB build
  filesize.</li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed battery level showing as blank when first opening in-game menu.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>The received SRL file from a Pokemon Wii title cannot connect to the Wii after
  being booted. It is unknown how to fix this.

  <ul dir="auto">

  <li>Additionally, when connecting using Platinum, the save data cannot be read.</li>

  <li>Additionally (again), when connecting using HGSS, a red screen crash will occur
  (apparently due to attempting to read non-existing Diamond/Pearl/Platinum ROM data).</li>

  </ul>

  </li>

  </ul>'
updated: '2022-06-21T21:48:17Z'
version: v0.59.0
version_title: 'v0.59.0: TWL Summer Solstice Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.