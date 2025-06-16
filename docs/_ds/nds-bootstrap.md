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
    size: 1058716
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.5.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1533760
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.5.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1263
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.14.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.14.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> Added support for color LUTs/screen filters (located
  in <code class="notranslate">sd:/_nds/colorLut/</code>)!

  <ul dir="auto">

  <li>Not compatible with the Memory Pit exploit.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> DS Phat colors can now be displayed! Some early DS
  games may benefit from this feature.

  <ul dir="auto">

  <li>Also not compatible with the Memory Pit exploit, due to it using the color LUT
  applying system.</li>

  <li>If you''re using <strong>TW</strong>i<strong>L</strong>ight Menu++ and/or forwarders,
  it can be set per-game.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> 6 more DSiWare titles can now be played on DS Phat &amp;
  DS Lite consoles! (474 -&gt; 480 DSiWare titles now supported!)

  <ul dir="auto">

  <li>Cake Ninja: XMAS

  <ul dir="auto">

  <li>Previously only worked on debug/dev consoles.</li>

  <li>Audio is disabled on regular/retail consoles due to memory limitations.</li>

  </ul>

  </li>

  <li>California Super Sports

  <ul dir="auto">

  <li>Crashes on regular/retail consoles when selecting either Dodgeball or Rollerblade.</li>

  </ul>

  </li>

  <li>Crazy Cheebo: Puzzle Party</li>

  <li>Curling Super Championship</li>

  <li>Electroplankton: Lumiloop

  <ul dir="auto">

  <li>Previously only worked on debug/dev consoles.</li>

  <li>Title intro music has been reduced from Stereo to Mono on regular/retail consoles
  due to memory limitations.</li>

  <li>An SDK5 VRAM-WiFi Donor ROM (ex. <em>Lufia: Curse of the Sinistrals</em>) is
  required to run this title on regular/retail consoles.</li>

  </ul>

  </li>

  <li>Ice Hockey Slovakia 2011

  <ul dir="auto">

  <li>Sound effects are disabled on regular/retail consoles due to memory limitations.</li>

  </ul>

  </li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>The color LUT applying system (also activated by enabling DS Phat colors) will
  not work properly with some games, due to 3D color blending, briefly showing the
  original colors for a frame, and/or bitmap graphics displaying. It can also cause
  certain games to crash and/or not boot.

  <ul dir="auto">

  <li>Plenty of the problematic games have been blacklisted from using the color LUT
  system, but some other games may still have those issues.</li>

  <li>The system is also incompatible with homebrew titles.</li>

  </ul>

  </li>

  </ul>'
updated: '2025-05-24T02:57:05Z'
version: v2.5.0
version_title: v2.5.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.