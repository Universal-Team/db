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
    size: 1075481
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.9.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1551463
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.9.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1302
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.18.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.18.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Changelog</h3>

  <ul dir="auto">

  <li>Most games which contain STRM files contained in <code class="notranslate">.sdat</code>
  files and/or Mobiclip will now have those STRM and/or video files be read asynchronously
  to reduce/remove frame drops.</li>

  <li>For many of the SD-related fixes to apply to flashcard users (such as properly
  working card read DMA), the LRU cache system is now used when running games from
  flashcards.

  <ul dir="auto">

  <li>The ROM read LED settings now work on flashcards as a result.</li>

  <li>This can work around crashes for certain flashcards.</li>

  <li>Does not apply to <em>Pokemon Black &amp; White 1 &amp; 2</em> due to the SWI
  Halt function not being hooked for flashcard reads, along with DLDI drivers not
  having asynchronous DMA reads.</li>

  <li>Due to memory limitations, this does not affect users who are running nds-bootstrap''s
  B4DS mode.</li>

  </ul>

  </li>

  <li>If the SD card the game is running from uses 32KB cluster size or more, the
  cluster size of the LRU cache will be increased from 16KB to 32KB, loading a bit
  more data each time a card read occurs.

  <ul dir="auto">

  <li>This is known to fix some crashes in <em>Pokemon Ranger: Guardian Signs</em>.</li>

  </ul>

  </li>

  <li>Fixed NAND save R/W under 512 bytes not working correctly by loading the last
  read data into the LRU cache.

  <ul dir="auto">

  <li>Due to memory limitations, this does not affect users who are running nds-bootstrap''s
  B4DS mode.</li>

  </ul>

  </li>

  <li>Fixed a possible crash which could occur when trying to connect to Wii in <em>Pokemon
  HeartGold &amp; SoulSilver</em>.</li>

  <li>The following games will no longer need to be manually AP-patched first before
  applying a ROM hack:

  <ul dir="auto">

  <li>MegaMan Zero Collection</li>

  <li>Phantasy Star 0</li>

  <li>Solatorobo: Red the Hunter</li>

  <li>Style Savvy</li>

  </ul>

  </li>

  <li>Fixed AP-fix for <em>Phantasy Star 0</em> (Japan).</li>

  <li>Most of the black flickering no longer occurs in the Transformers games developed
  by Vicarious Visions.</li>

  <li>If the DSi Sound app is set as a donor ROM for DSi-Enhanced games and save relocation
  is disabled, the donor ROM will be rejected.</li>

  <li>Fixed <em>Pokemon Black &amp; White 1 &amp; 2</em> not booting if a THUMB ROM
  (such as the standalone DS WiFi Settings ROM) is used as a DSi donor ROM.</li>

  <li>Fixed card read DMA not being patched properly for a few games (such as <em>Planet
  Puzzle League</em>).</li>

  <li>Attempted to fix possible issues occurring in homebrew titles by reverting the
  LRU cache transfer method from <code class="notranslate">__aeabi_memcpy</code> to
  <code class="notranslate">tonccpy</code>.</li>

  <li><em>Yu-Gi-Oh!: Nightmare Troubadour</em> and all <em>Yu-Gi-Oh! World Championship</em>
  games are now blacklisted from using screen color filters and/or the DS Phat color
  setting due to slowdown in some areas and darkening issues from palette cycling.</li>

  <li>Various: Updated in-game menu translations.</li>

  </ul>'
updated: '2025-10-19T00:20:46Z'
version: v2.9.0
version_title: v2.9.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.