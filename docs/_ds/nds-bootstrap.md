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
    size: 835216
    size_str: 815 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.13.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1202918
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.13.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1335
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.22.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.22.0</a><br>

  Re-released to fix <code class="notranslate">Quit Game</code> opening the system
  menu instead of Unlaunch/TWLMenu++/<code class="notranslate">boot.nds</code>.</p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Buttons can now be remapped to other buttons (ex. pressing <code class="notranslate">SELECT</code>
  can instead function as the <code class="notranslate">L</code> button)!</li>

  <li>The DS(i) screen refresh rate can now be changed in the in-game menu, and will
  affect game speed!

  <ul dir="auto">

  <li>Can be set to as low as 29.9 Hz for slow speed, or as high as 74.9 Hz for fast
  speed.</li>

  <li>Why isn''t this called <code class="notranslate">Game Speed</code> then? Because
  the setting works differently in certain games (ex. <em>MegaMan Star Force 2 &amp;
  3</em> run slower if it''s either less than or more than 59.9 Hz).</li>

  <li>Does not affect B4DS mode (on DS flashcards) and DSi-Enhanced/Exclusive games
  running in DSi mode.</li>

  </ul>

  </li>

  <li>Added descriptions for the options in the in-game menu.</li>

  <li>A confirmation message will now appear after selecting either <code class="notranslate">Reset
  Game</code> or <code class="notranslate">Quit Game</code> in the in-game menu.</li>

  <li>Reduced cheat data size limit from 32KB to 16KB.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed slowdown issues in <em>Sonic Rush</em> by not hooking SWI Halt.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/taxicat1/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/taxicat1">@taxicat1</a>:
  Fixed AP-fixes for <em>Puppy Palace</em> (Europe &amp; Japan) and <em>Inazuma Eleven
  3: The Ogre</em>.</li>

  <li>Patched sleep mode to work for EZ-Flash Parallel flashcards.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>Button remapping does not affect the DS WiFi Settings menu.</li>

  <li>Due to a hardware limitation, setting the refresh rate higher than 59.9 Hz will
  cause the 3D engine to not function.</li>

  </ul>'
updated: '2026-01-21T06:30:36Z'
version: v2.13.0
version_title: v2.13.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.