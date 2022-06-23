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
    size: 429852
    size_str: 419 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.59.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1035410
    size_str: 1011 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.59.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 139
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.10.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.10.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Moonshell v2.10 (child Zwai, Direct Boot) no longer shows the ARM9/7 memory
  error.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed <em>Kirby: Canvas Curse</em> not booting by fixing the branches to the
  save data functions.

  <ul dir="auto">

  <li>This should also fix other games which started to not boot in v0.59.0, if they''ve
  been affected by this bug.</li>

  </ul>

  </li>

  <li>SWI functions are now patched for homebrew running in DSi mode, regardless if
  using a RAM disk or not.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>Moonshell v2.10 is stuck on initing the DLDI driver, due to the SD driver not
  running.</li>

  </ul>'
updated: '2022-06-23T01:19:32Z'
version: v0.59.1
version_title: v0.59.1 (hotfix)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.