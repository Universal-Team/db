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
    size: 767234
    size_str: 749 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.0.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1858761
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.0.1/nds-bootstrap.zip
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
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.1.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.1.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li>Slightly improved boot times on DSi/3DS in DSi mode.

  <ul dir="auto">

  <li>NDMA is now used to clear memory.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed the Chinese (iQue) &amp; Korean versions of <em>Super Mario 64 DS</em>
  not booting.</li>

  <li>Implemented ROM and save mirroring.

  <ul dir="auto">

  <li>Fixes compatibility in some lesser-known DS games, such as <em>My Stop Smoking
  Coach</em>.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> Fixed games containing overlays crashing with an Expansion
  Pak inserted.</li>

  <li>Improved region determination for region-free DSiWare titles.

  <ul dir="auto">

  <li>If TWLCFG or the country setting within isn''t detected, it''ll determine region
  based on the currently set language.</li>

  <li>Fixes DS WiFi Settings standalone ROM displaying Japanese on flashcards even
  with a region other than Japan set.</li>

  </ul>

  </li>

  <li>Ported RTC fix to B4DS mode.

  <ul dir="auto">

  <li>Should hopefully fix the crashes in the Pokemon Gen 4 games, the time changing
  in <em>Animal Crossing: Wild World</em> and other time-related issues on DS flashcards.</li>

  </ul>

  </li>

  <li>Patched RAM mirror checking in an attempt to make the launched game not use
  more than 4MB of RAM.

  <ul dir="auto">

  <li>DS mode and DSi mode will set the proper value, the latter of which allows games
  to use up to 8MB of RAM.</li>

  <li>Does not apply to SDK5 games, as those are already working fine.</li>

  <li>Fixes <em>Jump Super Stars</em> not booting in DS mode.</li>

  </ul>

  </li>

  </ul>'
updated: '2023-09-25T23:42:06Z'
version: v1.0.1
version_title: v1.0.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.