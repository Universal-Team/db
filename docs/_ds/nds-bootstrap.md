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
    size: 1028275
    size_str: 1004 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.4.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1493773
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.4.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1207
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.12.4"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.12.4</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> New built-in pre-load settings have been added for
  the following games for a minor/major load speed improvement! (Does not apply to
  hacked or translated ROMs, unless when noted.) (Read <a href="https://github.com/DS-Homebrew/nds-bootstrap/blob/ad4f01d2c3c36cb1ad711145cfd9e87cb7da51a6/retail/preLoadSettings/Title%20list.txt">this</a>
  for details on which data is pre-loaded.)

  <ul dir="auto">

  <li>Animal Crossing: Wild World (USA, Japan, and Korean versions only) (3DS)</li>

  <li>Castlevania: Dawn of Sorrow (3DS)</li>

  <li>Castlevania: Portrait of Ruin (3DS)</li>

  <li>Castlevania: Order of Ecclesia (3DS)</li>

  <li>Classic Word Games (3DS, DSi mode)</li>

  <li>Diddy Kong Racing DS (DSi)</li>

  <li>English Training: Have Fun Improving Your Skills (DSi/3DS)</li>

  <li>FabStyle (3DS)</li>

  <li>Geometry Wars: Galaxies (DSi/3DS)</li>

  <li>Juiced 2: Hot Import Nights (DSi)</li>

  <li>Kirby Super Star Ultra (3DS)</li>

  <li>The Legend of Zelda: Phantom Hourglass (3DS)</li>

  <li>Mario Hoops 3 on 3 (USA &amp; Japan versions only) (3DS)</li>

  <li>Mario Kart DS (DSi)</li>

  <li>MegaMan Zero Collection (3DS)</li>

  <li>MegaMan ZX (3DS)</li>

  <li>MegaMan ZX Advent (3DS)</li>

  <li>Metal Slug 7 (DSi/3DS)</li>

  <li>Metroid Prime Hunters (3DS)</li>

  <li>New Super Mario Bros. (DSi)</li>

  <li>Plants vs. Zombies (DSi/3DS)</li>

  <li>Power Rangers: Samurai (3DS)</li>

  <li>Professor Layton and the Curious Village (USA, Japan, and Korean versions only)
  (3DS)</li>

  <li>Sonic Colors (3DS)</li>

  <li>Sonic Rush (3DS)</li>

  <li>Sonic Rush Adventure (3DS)</li>

  <li>Tomodachi Collection (Original and English-translated versions) (DSi/3DS)</li>

  <li>Yoshi Touch &amp; Go (DSi)</li>

  </ul>

  </li>

  <li>AP-fixes for English translations of <em>MapleStory DS</em> have been added!</li>

  <li>Added AP-fix for the <a href="https://github.com/Peppe30brick/Tomodachi-Collection-Ita">Italian
  translation (First Beta!)</a> of <em>Tomodachi Collection</em> (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Peppe30brick/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Peppe30brick">@Peppe30brick</a>).</li>

  <li><strong>DSi/3DS:</strong> When pre-loading a ROM containing overlays, the ARM7
  binary is no longer pre-loaded (as it''s already loaded to the RAM destination).
  This allows some more ROMs around 12MB/28MB to be pre-loadable.</li>

  <li><strong>DSi/3DS:</strong> The shared WRAM is now enabled for ROM pre-loading
  with DSi WRAM disabled.</li>

  <li><strong>DSi/3DS:</strong> Useful for debugging, all of the available RAM is
  now dumpable, regardless of running in DS mode or DSi mode.</li>

  <li><strong>B4DS:</strong> Moved save patches for DSiWare titles from 0/A to C into
  a new pack file within NitroFS. This reduces the filesize of nds-bootstrap by around
  288KB.</li>

  <li><strong>DSi/3DS:</strong> When a crash is encountered in <em>Mario &amp; Luigi:
  Bowser''s Inside Story</em>, the game now reboots instead of showing a Data Abort
  error.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> The old hooking method for reading ROMs from the SD
  card has once again been reverted back from IPC Sync to main loop/SWI Halt in order
  to fix some wireless communication issues.

  <ul dir="auto">

  <li><em>Pokemon Black &amp; White 1 &amp; 2</em> will continue to use the IPC Sync
  hooking method which has fixed the occasional crashing.</li>

  </ul>

  </li>

  <li>Fixed a long-standing bug where <em>Luminous Arc 2</em> would lock up on black
  screens when starting with a newly created save file.</li>

  <li>Updated AP-fix for <em>GoldenEye 007</em> to not crash on boot.</li>

  <li><strong>DSi/3DS:</strong> Fixed where ROM files with it''s clusters fragmented
  in the FAT filesystem would not boot.

  <ul dir="auto">

  <li>Achieved by increasing the (compressed) cluster cache from 0x600 bytes to 0x3000
  bytes for DS mode, and 0x7B0 bytes to 0x17B0 bytes for DSi mode.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Fixed an overlooked bug where no (non-pre-loadable)
  games would boot on flashcards (outside of B4DS mode).</li>

  <li><strong>B4DS:</strong> Fixed where some SDK 5 games which read save data before
  ROM data would not boot. (Based on PR <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2811480010" data-permission-text="Title is private" data-url="https://github.com/DS-Homebrew/nds-bootstrap/issues/1769"
  data-hovercard-type="pull_request" data-hovercard-url="/DS-Homebrew/nds-bootstrap/pull/1769/hovercard"
  href="https://github.com/DS-Homebrew/nds-bootstrap/pull/1769">#1769</a> by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/edo9300/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/edo9300">@edo9300</a>)</li>

  </ul>'
updated: '2025-01-30T09:37:21Z'
version: v2.4.0
version_title: 'v2.4.0: (Late) New Year''s Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.