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
    size: 1068522
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.8.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1545919
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.8.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1289
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.17.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.17.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Added AP-fixes for the following games:

  <ul dir="auto">

  <li>Captain Tsubasa: New Kick Off (English translation v0.5)</li>

  <li>Captain Tsubasa: New Kick Off (Repacked v1.8) (Patch required from <a href="https://github.com/DS-Homebrew/nds-bootstrap-extras/tree/main/fixedRomPatches">nds-bootstrap-extras</a>)</li>

  <li>Inazuma Eleven 3: The Ogre (Full English Translation) (Patch required from <a
  href="https://github.com/DS-Homebrew/nds-bootstrap-extras/tree/main/fixedRomPatches">nds-bootstrap-extras</a>)</li>

  <li>Pokémon: Refined Gold Overhaul (Coarse) (v4.1.3) (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  <li>Pokémon: Refined Gold Overhaul (Original) (v4.1.3) (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  <li>Pokémon: SoothingSilver Version (v1.4.3) (by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  <li>Pokémon: Storm Silver Version (v1.1.1) (Classic) (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  <li>Pokémon: Storm Silver Version (v1.1.1) (Complete) (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/R-YaTian/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/R-YaTian">@R-YaTian</a>:
  Improved AP-patching system for patches to be applied to some more modified ROMs.</li>

  <li>When trying to load streamable music &amp; videos in some games, card read DMA
  is now forced in order to load them asynchronously. This only applies to DSi/3DS
  SD card users, and currently applies to these games:

  <ul dir="auto">

  <li>Elite Beat Agents</li>

  <li>Osu! Tatakae! Ouendan</li>

  <li>Moero! Nekketsu Rhythm Damashii: Osu! Tatakae! Ouendan 2</li>

  <li>Pokemon Black &amp; White Version 2</li>

  <li>Pokemon Ranger: Guardian Signs</li>

  <li>Sonic Colors</li>

  <li>System Flaw</li>

  </ul>

  </li>

  <li>Added pre-load settings for the following games:

  <ul dir="auto">

  <li>Code Lyoko (3DS): Everything except level-specific sound effects and video cutscenes</li>

  <li>Code Lyoko: Fall of X.A.N.A. (MEP/DSi): Everything except sound data and video
  cutscenes</li>

  <li>Stratego: Next Edition (DSi): Everything except streamed music</li>

  </ul>

  </li>

  <li>If a screen color filter and/or the DS Phat colors setting is enabled, the log
  (if enabled) will now notify you that a screen filter is enabled.</li>

  <li>The log (if enabled) will now print out the nds-bootstrap version on the top.</li>

  <li>Various: Updated in-game menu translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> <em>myNotebook Red, Green, and Blue</em> will no longer
  crash when booted with Memory Pit.</li>

  <li><strong>B4DS:</strong> Fixed <em>Paws &amp; Claws: Pet Resort</em> and <em>Paws
  &amp; Claws: Pet Vet 2</em> not booting due to a missing patch.

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> The added missing patch now allows the nds-bootstrap
  in-game menu to open for those games.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> <em>Clubhouse Games</em> now boots with a screen color
  filter and/or DS Phat colors enabled.</li>

  <li><strong>DSi/3DS:</strong> <em>Flower, Sun and Rain: Murder and Mystery in Paradise</em>
  no longer boots with a screen color filter and/or DS Phat colors due to a crash
  which occurs later on (see <a href="https://github.com/DS-Homebrew/nds-bootstrap/issues/1856"
  data-hovercard-type="issue" data-hovercard-url="/DS-Homebrew/nds-bootstrap/issues/1856/hovercard">this
  page</a> for details).</li>

  <li><strong>DSi/3DS:</strong> Patched out Slot-1 check from sleep mode for known
  certain flashcards. (Moved from TWLMenu++.)</li>

  </ul>'
updated: '2025-08-30T06:36:56Z'
version: v2.8.0
version_title: v2.8.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.