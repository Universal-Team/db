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
    size: 1066869
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.6.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1536400
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.6.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.15.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.15.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>3DS:</strong> Updated ROM pre-load settings for <em>WarioWare: D.I.Y.</em>
  (Europe) to pre-load all data used for the currently set language.</li>

  <li><strong>DSi/3DS:</strong> Added ROM pre-load settings (automatically activated)
  for more games for improved ROM reading:

  <ul dir="auto">

  <li>Dragon Quest IV: Chapters of the Chosen (USA) (English Party Chat v1.2)</li>

  <li>Elite Forces: Unit 77 (DSi)</li>

  <li>Nanostray (DSi)</li>

  <li>Nanostray 2 (DSi)</li>

  <li>Stitch Jam</li>

  <li>Motto! Stitch! DS: Rhythm de Rakugaki Daisakusen</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Screen filter and/or DS Phat colors are now applied
  to Actimagine/Mobiclip videos!

  <ul dir="auto">

  <li>When running with NTR clock speed, video resolution will be reduced in half
  to reduce slowdown.</li>

  </ul>

  </li>

  <li>When starting a game for the first time with this version, the ESRB splash screen
  (if enabled) on the top screen is now displayed at the same time as the "Please
  wait..." message on the bottom screen.</li>

  <li>For some ESRB-rated online games which don''t display the online notice (ex.
  <em>Pokemon Black &amp; White 1 &amp; 2</em>), it can now be displayed on the bottom
  screen (replacing the "Please wait..." message on first boot) below the ESRB splash
  screen.

  <ul dir="auto">

  <li>Online notice flags are stored on TWLMenu++''s side (along with the rating descriptors).</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi:</strong> Due to the pre-load setting addition, <em>Nanostray 2</em>
  no longer crashes when going into gameplay!</li>

  <li>Fixed a (somewhat) long-standing issue where <em>Professor Layton and the Curious
  Village</em> would not reset correctly from nds-bootstrap''s in-game menu, instead
  showing video cutscenes or the puzzle mode.</li>

  <li><strong>DSi/3DS:</strong> <em>Bomberman</em> no longer crashes on opening an
  area when using a screen filter and/or DS Phat colors.</li>

  <li><strong>DSi/3DS:</strong> Fixed card read DMA not being properly patched for
  <em>My Healthy Cooking Coach</em> and possibly some other early DSi-Enhanced games.

  <ul dir="auto">

  <li>The title would crash after boot without the fix.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Fixed games which use SDK 2.1 or later not booting
  from flashcards (without B4DS mode).</li>

  <li><strong>DSi/3DS:</strong> Fixed DSi mode not working on flashcards.</li>

  <li>Yet another attempt to fix the in-game menu not opening on Ace3DS+ flashcards,
  by clearing the WiFi IRQ register on arm7 before boot.

  <ul dir="auto">

  <li>Implemented after a user has found out that the in-game menu opens on <em>Shantae:
  Risky''s Revenge</em> due to the WiFi IRQ register not being checked.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Fixed rebooting after dumping RAM.</li>

  <li><strong>DS:</strong> Fixed SuperCard CF support (not to be confused with SuperCard
  MiniSD).</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>Screen filter and/or DS Phat colors are not applied to all games containing
  Mobiclip videos, as the code which plays the videos may be stored in the overlays
  instead of the main ARM9 code.

  <ul dir="auto">

  <li>Some games where the code is stored in the overlays are supported manually.</li>

  </ul>

  </li>

  <li>Despite the pre-load setting addition, <em>Stitch Jam</em> still randomly soft-locks.
  The cause of the soft-locks is unknown.</li>

  </ul>'
updated: '2025-06-18T05:23:42Z'
version: v2.6.0
version_title: v2.6.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.