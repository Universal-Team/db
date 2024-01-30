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
    size: 782221
    size_str: 763 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.2.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1905995
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.2.2/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.6.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.6.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>To prevent some crashes, card read DMA has been disabled entirely for DSi-Enhanced/DSi-Exclusive
  games in DSi mode.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><em>Flipnote Studio</em> now boots properly with Memory Pit.</li>

  <li>Fixed a long-standing bug where cloneboot would not work with DSi-Enhanced ROMs
  running in DSi mode.</li>

  <li>Fixed arm7 binary being cleared for DSi mode when running via DSiWarehax, which
  caused an error to appear when booting.</li>

  <li>Proper language bitmask is now used for Australian region.</li>

  </ul>'
updated: '2024-01-30T01:53:05Z'
version: v1.2.2
version_title: v1.2.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.