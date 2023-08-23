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
    size: 757852
    size_str: 740 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.73.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1814764
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.73.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.0.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.0.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>LRU cache size now takes up almost the whole extra RAM space after the first
  4MB!

  <ul dir="auto">

  <li>The ROM pre-load size limit has also been affected to do the same.</li>

  </ul>

  </li>

  <li>When starting an NTR-type game in DSi mode, the heap size is now increased from
  4MB to 8MB!

  <ul dir="auto">

  <li>Useful for some ROM hacks that somehow go above the normal heap size.</li>

  <li>Due to a limitation of SDK2.0, it does not affect games made with that SDK version.</li>

  </ul>

  </li>

  </ul>

  <h4 dir="auto">B4DS mode</h4>

  <ul dir="auto">

  <li>Added support for 39 more DSiWare titles to be playable on DS/DS lite (plus
  7 more for debug consoles)!

  <ul dir="auto">

  <li>Scroll down to see which titles are now supported.</li>

  <li>Click &gt;<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/07e8ce7a864f98dbb8637599fbba8ecbe54ebc8c/universal/include/compatibleDSiWareMap.h">here</a>&lt;
  for the full list of supported titles.</li>

  </ul>

  </li>

  <li>Any SDK5 DS game can now be set as a Donor ROM to run DSiWare!

  <ul dir="auto">

  <li>Useful if you don''t have an existing ROM dump of a DSi-Enhanced game.</li>

  <li><em>Lufia: Curse of the Sinistrals</em> (currently known to be the only SDK5
  game to contain a VRAM-WiFi type of arm7 binary) is required by certain DSiWare
  titles (listed below) to use much memory (aka RAM space) as possible. On debug/dev
  consoles, it is not required.

  <ul dir="auto">

  <li>If it''s the only game set as a Donor ROM, DSiWare which use wireless will be
  unable to use those features.</li>

  </ul>

  </li>

  <li><em>Ubongo</em> is the only DSiWare title which still specifically requires
  a DSi-Enhanced game to be set as a Donor ROM.</li>

  </ul>

  </li>

  <li><em>Picture Perfect Hair Salon</em>, one of the few DSi-Exclusives released
  on cartridge, is now playable on DS/DS lite!

  <ul dir="auto">

  <li>Audio does not play outside of debug/dev consoles.</li>

  </ul>

  </li>

  <li>Full version of <em>Digidrive</em> is now supported on debug/dev consoles!</li>

  <li>The Europe/Australia &amp; Japanese versions of <em>Bejeweled Twist</em> are
  now supported!

  <ul dir="auto">

  <li>Europe/Australia version requires <em>Lufia</em> set as a Donor ROM.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>For TWL-type games running in DSi mode on DSi consoles, heap shrink has once
  again been reduced (by 256KB), leaving only 256KB of heap being shrunk.

  <ul dir="auto">

  <li>This should fix more crashes in some of those games.</li>

  </ul>

  </li>

  <li>Fixed &amp; optimized card ID start offset search.

  <ul dir="auto">

  <li>This fixes certain games not booting the first time, and/or with card read DMA
  turned on.</li>

  <li>This seems to fix game compatibility on certain flashcards.</li>

  </ul>

  </li>

  <li><em>The Incredibles: Rise of the Underminer</em> now boots!</li>

  <li>Other minor fixes.</li>

  </ul>

  <h4 dir="auto">B4DS mode</h4>

  <ul dir="auto">

  <li><em>The Legend of Zelda: Four Swords: Anniversary Edition</em> now plays audio
  outside of debug/dev consoles!

  <ul dir="auto">

  <li>Additionally, the crash when completing a stage and before saving data is now
  fixed!</li>

  </ul>

  </li>

  <li>Fixed <em>Oscar in Toyland 2</em> crashing after completing a stage.</li>

  <li><em>Flipper</em> now plays music outside of debug/dev consoles!</li>

  <li>The title screen in <em>Robot Rescue</em> no longer shows a black stripe on
  the bottom screen.</li>

  <li>The weird sound glitch has reportedly been fixed on Ace3DS+ flashcards.

  <ul dir="auto">

  <li>For those with an Ace3DS+ flashcard, please test to confirm.</li>

  </ul>

  </li>

  <li>Certain AP-fixes now work without a Memory Expansion Pak!</li>

  <li>Fixed where the AP-fix for <em>Mario &amp; Luigi: Bowser''s Inside Story</em>
  would get overwritten, causing the AP-fix to not work.</li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite</h3>

  <p dir="auto">Titles marked in <strong>Bold</strong> will only boot on debug/dev
  consoles.</p>

  <ul dir="auto">

  <li><strong>2Puzzle It: Fantasy</strong>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>AiRace: Tunnel

  <ul dir="auto">

  <li>Audio does not play outside of debug/dev consoles</li>

  <li>Crashes when selecting another tunnel after first selecting one, worked around
  by selecting either Credits or Controls (occurs outside of debug/dev consoles)</li>

  </ul>

  </li>

  <li>Drift Street International

  <ul dir="auto">

  <li>Race music does not play outside of debug/dev consoles</li>

  </ul>

  </li>

  <li>Electroplankton: Beatnes

  <ul dir="auto">

  <li>Previously only supported on debug/dev consoles</li>

  </ul>

  </li>

  <li>Electroplankton: Trapy

  <ul dir="auto">

  <li>Previously only supported on debug/dev consoles</li>

  </ul>

  </li>

  <li>G.G Series: Air Pinball Hockey

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: All Breaker

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Altered Weapon

  <ul dir="auto">

  <li>Does not save</li>

  <li>Requires <em>Lufia</em> set as a Donor ROM</li>

  </ul>

  </li>

  <li>G.G Series: Assault Buster

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li>G.G Series: Black x Block

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li>G.G Series: Conveyor Toy Packing

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li>G.G Series: Cosmo Rally!!

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: D-Tank</li>

  <li>G.G Series: Dark Spirits</li>

  <li>G.G Series: Drift Circuit</li>

  <li>G.G Series: Drift Circuit 2

  <ul dir="auto">

  <li>Requires <em>Lufia</em> set as a Donor ROM</li>

  </ul>

  </li>

  <li>G.G Series: Drilling Attack!!

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li>G.G Series: Energy Chain

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li><strong>G.G Series: Exciting River</strong>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Great Whip Adventure

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Hero Puzzle

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: The Hidden Ninja Kagemaru

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Horizontal Bar</li>

  <li>G.G Series: The Last Knight

  <ul dir="auto">

  <li>Does not save</li>

  <li>Requires <em>Lufia</em> set as a Donor ROM</li>

  </ul>

  </li>

  <li>G.G Series: Ninja Karakuri Den</li>

  <li>G.G Series: Ninja Karakuri Den 2</li>

  <li>G.G Series: Nyokki

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Run &amp; Strike

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Score Attacker

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Shadow Army

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: The Spiky Blowfish

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li><strong>G.G Series: Super Hero Ogre</strong></li>

  <li><strong>G.G Series: Super Hero Ogre 2</strong></li>

  <li><strong>G.G Series: Throw Out</strong>

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li>G.G Series: Vector

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>G.G Series: Vertex

  <ul dir="auto">

  <li>Only Japanese version saves</li>

  </ul>

  </li>

  <li>G.G Series: Wonder Land

  <ul dir="auto">

  <li>USA version does not save</li>

  </ul>

  </li>

  <li>G.G Series: Z-One</li>

  <li>G.G Series: Z-One 2</li>

  <li>iSpot Japan

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Korogashi Pazuru: Katamari Damacy</li>

  <li><strong>My Little Restaurant</strong></li>

  <li>Need for Speed: Nitro-X

  <ul dir="auto">

  <li>Previously only supported on debug/dev consoles</li>

  <li>Does not save</li>

  <li>Crashes after a race</li>

  <li>Requires <em>Lufia</em> set as a Donor ROM</li>

  </ul>

  </li>

  <li>Oscar in Movieland</li>

  <li><strong>Oscar''s World Tour</strong></li>

  <li>Phantasy Star 0 Mini

  <ul dir="auto">

  <li>Previously only supported on debug/dev consoles</li>

  <li>To cut down RAM usage, only each one character animation gets loaded for each
  of the three characters. As a result, the animation will not change when switching
  weapons.</li>

  <li>Crashes when progressing through one of the later areas</li>

  <li>Requires <em>Lufia</em> set as a Donor ROM</li>

  </ul>

  </li>

  </ul>'
updated: '2023-08-23T21:16:49Z'
version: v0.73.0
version_title: v0.73.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.