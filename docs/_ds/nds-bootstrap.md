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
    size: 1110524
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.3.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1664358
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.3.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1195
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.12.3"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.12.3</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <p dir="auto">Merry TWL Christmas!<br>

  Here are some presents to unwrap for this release! 🎁</p>

  <ul dir="auto">

  <li>Support for <em>Pokémon</em> Wii connection has been completely fixed! Any Gen
  4 game will now connect with <em>Pokémon Battle Revolution</em> and/or <em>My Pokémon
  Ranch</em>! (Patch code by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Gericom/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Gericom">@Gericom</a>)</li>

  <li>For improved DSiWare compatibility flashcards, they will now run with the SDMMC
  mode redirected to DLDI R/W code, if the SDMMC register is enabled on ARM7, and
  if the flashcard is running in (full) DSi mode. (Patch code by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Gericom/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Gericom">@Gericom</a>)

  <ul dir="auto">

  <li>As a result, all NAND file reads are redirected to the flashcard.</li>

  <li>If you''re using TWLMenu++, DSiWare is copied to a temp location on DSi/3DS
  SD card by default, and saves will not work if the save location is set to the TWLMenu++
  folder while running from DSi/3DS SD card.</li>

  </ul>

  </li>

  <li>Expanded the pre-loadable ROM size limit to use 128KB more of the main RAM,
  32KB more of the DSi WRAM (making 512KB used), and now, the shared RAM (freed up
  from ARM7 by how the DSi WRAM is mapped)!

  <ul dir="auto">

  <li>Total limit is now 12.4MB for DSi consoles, and 28.4MB for 3DS consoles!</li>

  </ul>

  </li>

  <li>Reverted back from SWI Halt/main loop hooking to IPC Sync hooking for when reading
  ROM from DSi/3DS SD card.

  <ul dir="auto">

  <li>No issues with wireless communications have been noticed so far in <em>Mario
  Kart DS</em> &amp; <em>Metroid Prime Hunters</em> during single-card play. Same
  issues from prior versions may still occur.</li>

  <li>Should fix occasional freezing in <em>Pokémon B&amp;W 1&amp;2</em>.</li>

  </ul>

  </li>

  <li>Fixed AP-fix for <em>Rockman EXE: OSS</em> English translation not applying.

  <ul dir="auto">

  <li>Requires the ROM to be opened and saved with the latest TinkeDSi nightly build.</li>

  <li>Fixes Star Colosseum causing a crash when opening.</li>

  </ul>

  </li>

  <li>Fixed <em>Tetris Party Deluxe</em> not booting on 3DS consoles.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/edo9300/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/edo9300">@edo9300</a>:
  Fixed issues when running on SuperCard Rumble flashcarts.</li>

  <li>Removed some duplicate cardEngine9i binaries to reduce nds-bootstrap''s file
  size.</li>

  </ul>'
updated: '2024-12-25T08:49:21Z'
version: v2.3.0
version_title: 'v2.3.0: TWL Christmas Release 🎄'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.