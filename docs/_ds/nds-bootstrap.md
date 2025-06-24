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
    size: 1069228
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.6.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1538309
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.6.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1265
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.15.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.15.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <p dir="auto">Below changes only apply to DSi &amp; 3DS users.</p>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Added ROM pre-load settings (automatically activated) for more games for improved
  ROM reading:

  <ul dir="auto">

  <li>Dragon Ball: Origins (Sound data)</li>

  <li>Dragon Ball: Origins 2 (Sound data)</li>

  <li>Dragon Ball Z: Supersonic Warriors 2 (Character sprites and sound data, the
  latter for 3DS)</li>

  <li><strong>3DS:</strong> Kamen Rider: Dragon Knight (Everything except sound data)</li>

  </ul>

  </li>

  <li>A DSi-Exclusive/DSiWare ROM can now be used as a donor ROM in order to increase
  the cluster cache from 6KB (0x17B0) to 12KB (0x3000) when running a DSi-Enhanced
  game in DSi mode. This can be useful if nds-bootstrap shows <code class="notranslate">An
  error has occurred.</code> due to ROM cluster fragmentation, and you don''t feel
  like reformatting the SD card to de-fragment the ROM.

  <ul dir="auto">

  <li>If you are using a DSi, then TWLMenu++ has already set a donor ROM automatically
  after booting for the first time.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed crashing with a communication error when selecting anything after connecting
  to <em>My Pokemon Ranch</em> on Wii.

  <ul dir="auto">

  <li>The crash was caused by not reading the sound data due to the pre-loaded ROM
  data map getting cleared after selecting the <code class="notranslate">Connect to
  Wii</code> option in the Gen 4 Pokemon games.</li>

  </ul>

  </li>

  <li>Fixed a bug which lasted since v1.0.0, where the "Wanted!" feature in <em>Assassin''s
  Creed II: Discovery</em> would crash with both screens nearly white, and no DSi/3DS
  camera image on the top screen.</li>

  </ul>'
updated: '2025-06-23T18:26:42Z'
version: v2.6.1
version_title: v2.6.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.