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
    size: 793509
    size_str: 774 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.6.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1119968
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.6.2/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1166
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.7.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.7.0</a></p>

  <p dir="auto">Originally released on 8/26/2024, re-released to restore the version
  number in the in-game menu.</p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>For consoles which improperly trigger sleep mode (with opened lid), sleep mode
  can now be disabled!</li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed games which use NAND saves not booting (such as <em>WarioWare: DIY</em>,
  <em>Jam with the Band</em>, and <em>Face Training</em>).</li>

  </ul>

  <h2 dir="auto">v1.6.1 Changelog</h2>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed an overlooked bug which caused 512MB ROMs to not load under Memory Pit.</li>

  </ul>

  <h2 dir="auto">v1.6.0 Changelog</h2>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Improved stability of wireless communications by moving SD R/W operations from
  vBlank &amp; IPC Sync IRQs (of arm7) to main loop (of arm7) (once again, achieved
  by hooking SWI Halt calls)!

  <ul dir="auto">

  <li>This means little to no random connection dropouts (may vary, depending on the
  game).</li>

  <li><em>Mario Kart DS</em> will now properly host a single-card multiplayer game.</li>

  <li>No more slowdowns during ROM reads from the SD card with wireless comms.!</li>

  <li>Compared to prior versions which implemented SWI Halt hooking, some optimizations
  have been made to reduce slowdown from said hooking. No slowdown has been found
  in known games which had those prior, such as <em>CTGP Nitro</em> (v1.0).</li>

  </ul>

  </li>

  <li>Fixed an overlooked bug (which occurred since v1.1.0) which caused a Data Abort
  crash when attempting to connect to PBR via <em>Pokemon Diamond</em>, <em>Pearl</em>,
  or <em>Platinum</em>.

  <ul dir="auto">

  <li>The same disconnection bug will likely persist.</li>

  </ul>

  </li>

  <li><em>Cut the Rope</em> no longer shows black screens for Memory Pit users!</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <p dir="auto">Due to moving SD R/W operations to main loop, the following will occur.</p>

  <ul dir="auto">

  <li>Compared to previous versions, there may be some minor slowdown in certain games
  (such as Pokemon B/W 2, during the title screen).</li>

  <li>On DSi consoles, <em>Nervous Brickdown</em> &amp; <em>Big Bang Mini</em> will
  crash on black screens after the company logos. Both will still run on 3DS consoles,
  as those games are pre-loaded to RAM.</li>

  <li>If you still encounter random connection dropouts, try turning off the <code
  class="notranslate">Card read DMA</code> setting in either TWLMenu++ or the forwarder
  per-game settings menus.</li>

  </ul>'
updated: '2024-08-27T23:18:22Z'
version: v1.6.2
version_title: 'v1.6.2 (hotfix #2)'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.