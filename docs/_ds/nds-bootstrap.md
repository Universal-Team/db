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
    size: 465208
    size_str: 454 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.63.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1114155
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.63.2/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.2.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.2.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Because of the bug fix from v0.63.1, <em>Mario Kart DS</em> and <em>Mario Party
  DS</em> are now pre-loadable into RAM on 3DS consoles again!

  <ul dir="auto">

  <li><em>Mario Kart DS</em> requires <code class="notranslate">EXTENDED_MEMORY</code>
  setting to be set in <code class="notranslate">sd:/_nds/nds-bootstrap.ini</code>,
  or <code class="notranslate">Ex. ROM Space in RAM</code> in TWLMenu++ per-game settings
  menu.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed screen flickers in <em>Animal Crossing: Wild World</em> (and possibly
  other games that have been affected by the same bug).</li>

  <li>Fixed AP-patched overlays not being cached properly when running a TWL title
  in DSi mode on DSi consoles.

  <ul dir="auto">

  <li><em>KORG DS-10+ Synthesizer</em> no longer crashes with a red screen.</li>

  </ul>

  </li>

  <li>Worked around unexpected issues with card read DMA in DSi mode, by using the
  regular card read code in place.

  <ul dir="auto">

  <li>The proper DMA code is still used with ROMs pre-loaded into RAM on 3DS consoles.</li>

  </ul>

  </li>

  <li>More minor bug fixes.</li>

  </ul>'
updated: '2022-08-12T05:00:20Z'
version: v0.63.2
version_title: v0.63.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.