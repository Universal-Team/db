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
    size: 763555
    size_str: 745 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.0.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1853636
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.0.2/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>When using wireless features, ROM loading on DSi/3DS SD Card is now slowed down
  once again, in order to prevent errors.</li>

  <li>Fixed ROM mirroring for if ROM size is larger than the device size set in the
  ROM header.

  <ul dir="auto">

  <li>Fixes support for some modified ROMs (ex. translations and ROM hacks).</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> Cheat engine has been moved to arm7 WRAM for <em>Inazuma
  Eleven 1 &amp; 2</em>.

  <ul dir="auto">

  <li>Fixes where opening a menu crashes the game with an AP-fix applied.</li>

  </ul>

  </li>

  <li>Fixed the European version of <em>Yoshi Touch &amp; Go</em> not booting on DSi/3DS
  SD Card.</li>

  <li><strong>B4DS mode:</strong> To prevent bugs, <strong>TW</strong>i<strong>L</strong>ight
  Menu++ must now be used with <code class="notranslate">EZ_FLASH_RAM</code> turned
  on in <code class="notranslate">fat:/_nds/TWiLightMenu/settings.ini</code>, in order
  to use an EZ-Flash Slot-2 cartridge.</li>

  </ul>'
updated: '2023-10-31T18:44:58Z'
version: v1.0.2
version_title: 'v1.0.2: Halloween Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.