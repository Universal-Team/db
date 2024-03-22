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
    size: 790133
    size_str: 771 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.4.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1919441
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.4.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.8.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.8.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>A long awaited and overdue DS homebrew compatibility update has been implemented!

  <ul dir="auto">

  <li>Homebrew titles which have not booted in prior versions such as <em>Moonshell</em>
  v2.10 and <em>Tetris: The Grand Master</em> now boot properly!</li>

  <li>SD read speeds have improved, by using 512KB of DSi WRAM (or for Memory Pit
  users, 96KB of Main RAM) as a LRU cache!

  <ul dir="auto">

  <li>Before (Moonshell v1.71): 8 seconds</li>

  <li>After (Moonshell v1.71): 2.5 seconds</li>

  </ul>

  </li>

  <li>DPG playback in <em>Moonshell</em> is also working properly!</li>

  </ul>

  </li>

  <li>To slightly speed-up memcpy operations for LRU cache and pre-loaded ROM reads,
  tonccpy has been replaced with the memcpy code from BlocksDS!</li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed where reading both the last and first parts of the save file at the same
  time would cause a game to crash.

  <ul dir="auto">

  <li>This fixes where <em>Gormiti: The Lords of Nature!</em> would crash on the save
  initialization screen, if the save file is 64KB.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li><em>Moonshell</em> v1.71 may crash later on for some DPG files. It is recommended
  to use v2.10 instead.</li>

  <li><em>Moonshell</em> v2.10 will crash if <code class="notranslate">logbuf.txt</code>
  exists in the <code class="notranslate">moonshl2</code> folder.</li>

  </ul>'
updated: '2024-03-22T03:27:26Z'
version: v1.4.0
version_title: v1.4.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.