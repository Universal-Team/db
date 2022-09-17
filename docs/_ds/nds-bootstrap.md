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
    size: 512884
    size_str: 500 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.64.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1207544
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.64.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
image_length: 5116
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.3.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.3.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Tired of playing <em>Mighty Milky Way</em> and/or
  <em>Shantae: Risky''s Revenge</em> on your DS/DS Lite without music? If so, you
  can now play them with music, by adding music packs for those games to <code class="notranslate">fat:/_nds/nds-bootstrap/musicPacks/</code>.

  <ul dir="auto">

  <li>The pack''s filename must have the TID and CRC from the ROM''s header (ex. <code
  class="notranslate">KS3E-57FE.pck</code>)</li>

  <li>The pack files are currently unavailable, but the creator can be downloaded
  <a href="https://github.com/DS-Homebrew/nds-bootstrap-extras/tree/main/musicPackCreator">here</a>.</li>

  <li>This will only work with those two games. Other games are not supported.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed a regression which caused <em>Pokemon Black/White</em> to crash with a
  red screen.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
  Fixed Japanese font mapping in the in-game menu.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>Music playing from a music pack will have slight lags. Depending on what''s
  happening, the lag may be longer.</li>

  <li>Music playing from a music pack will not pause when the game is paused.</li>

  </ul>'
updated: '2022-09-16T03:33:10Z'
version: v0.64.1
version_title: v0.64.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.