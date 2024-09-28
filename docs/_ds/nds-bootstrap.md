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
    size: 812383
    size_str: 793 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.0.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1167122
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.0.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1172
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.9.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.9.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Removed the preload flag for old DS homebrew, as there are no (known) frontends
  which use it.</li>

  <li>Old versions of some DSi system apps now boot.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>The Singleplayer Nookingtons patch for <em>Animal Crossing: Wild World</em>
  no longer black screens in B4DS mode!</li>

  <li>Fixed wrong placement of the sound frequency flag causing old DS homebrew (as
  well as GBARunner2) to not boot.</li>

  <li>For proper changing of the DSi/3DS sound frequency, the codec is now written
  to.</li>

  <li>Leftover garbage data is now cleared before boot when running from Slot-1 with
  SCFG access.</li>

  <li>Some minor optimizations.</li>

  </ul>'
updated: '2024-09-26T22:08:57Z'
version: v2.0.1
version_title: v2.0.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.