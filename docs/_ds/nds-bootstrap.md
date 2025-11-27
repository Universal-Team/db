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
    size: 1081221
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.10.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1567445
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.10.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1315
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.19.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.19.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>The screen swapping hotkey (hold <code class="notranslate">L</code>+<code class="notranslate">R</code>+<code
  class="notranslate">Up</code>+<code class="notranslate">X</code> for 1 second) has
  been readded!

  <ul dir="auto">

  <li>To avoid continuous writes to the SD card after using the screen swap hotkey,
  the setting will save after 3 seconds. (Does not apply to B4DS mode, where the setting
  only saves via the in-game menu.)</li>

  <li>The hotkey is now customizeable as well! It can be changed within the TWLMenu++
  Settings menu.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> 11 more DSiWare now run on DS and DS Lite consoles, bringing
  the total from 480 to 491!

  <ul dir="auto">

  <li>Absolute BrickBuster

  <ul dir="auto">

  <li>Accessing free play mode causes a crash.</li>

  <li>Does not save.</li>

  </ul>

  </li>

  <li>Discolight</li>

  <li>Hakokoro

  <ul dir="auto">

  <li>Audio disabled on retail DS consoles due to RAM limitation.</li>

  </ul>

  </li>

  <li>Jagged Alliance</li>

  <li>Kuniya Burete Sanga Ari: Hills and Rivers Remain

  <ul dir="auto">

  <li>Both a Memory Expansion Pak and VRAM-WiFi Donor ROM (such as <em>Lufia: Curse
  of the Sinistrals</em>) required. If you have neither, then a debug DS console will
  work.</li>

  </ul>

  </li>

  <li>Libera Wing</li>

  <li>Nintendogs (iQue)</li>

  <li>Puzzle Fever</li>

  <li>Retro Pocket</li>

  <li>Sagittarius-A-Star

  <ul dir="auto">

  <li>Only the options are saved.</li>

  </ul>

  </li>

  <li>Sengoku Tactics

  <ul dir="auto">

  <li>Master volume has been reduced due to the original audio playing loud.</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> Removed Memory Expansion Pak requirement for these DSiWare
  titles by Digital Leisure!

  <ul dir="auto">

  <li>21 Blackjack</li>

  <li>Match Up!</li>

  <li>Mega Words</li>

  <li>Word Searcher (Europe)</li>

  <li>Word Searcher II</li>

  <li>Word Searcher III</li>

  <li>Word Searcher IV</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> Music now plays in <em>Neko Neko Bakery: Pan de Pazurunya!</em>
  on retail DS consoles!

  <ul dir="auto">

  <li>This was achieved by having the game stream the music files from the ROM instead
  of pre-loading the music files to RAM, reducing RAM usage as a result.</li>

  <li>The same method was implemented for the above listed Digital Leisure titles
  in order for them to run without the expansion pak.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> To increase boot speed of DSiWare titles, the patched
  ARM binaries are not written to the page file, since soft-resets are disabled (console
  reboots or turns off instead).</li>

  <li><strong>DSi:</strong> Added ROM pre-load settings for <em>SNK vs. Capcom: Card
  Fighters DS</em> (USA &amp; Japan).</li>

  <li><strong>DSi/3DS:</strong> Added ROM pre-load settings for <em>SNK vs. Capcom:
  Card Fighters DS</em> (Europe).</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> Reverted LRU cache block size from 32KB to 16KB to
  reduce both audio and wireless communication issues.

  <ul dir="auto">

  <li>It''ll be kept as 32KB for <em>Pokemon Ranger: Guardian Signs</em> due to some
  crashes being fixed as a result.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> Fixed a possible bug which could cause <em>Battle/Combat
  of Giants: Mutant Insects</em> to not boot.</li>

  <li><strong>B4DS:</strong> Fixed a long-standing bug which caused <em>Dragon''s
  Lair II</em> (EUR/AUS) to crash on the company logos. Now both the USA and EUR/AUS
  versions boot properly!</li>

  <li><strong>B4DS:</strong> As a result of the MEP requirement being removed for
  <em>Mega Words</em>, some missing graphics have been restored.</li>

  <li><strong>B4DS:</strong> Fixed uncompressed FAT table cache still being created
  when end of file is reached, if an expansion pak is inserted.

  <ul dir="auto">

  <li>Fixes saves not being read if an expansion pak is inserted.</li>

  </ul>

  </li>

  </ul>'
updated: '2025-11-27T06:50:59Z'
version: v2.10.0
version_title: 'v2.10.0: Thanksgiving Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.