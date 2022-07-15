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
    size: 450342
    size_str: 439 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.61.3/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1082496
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.61.3/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Will be included in an upcoming version of <strong>TW</strong>i<strong>L</strong>ight
  Menu++.</p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Do you have Memory Pit installed, but still want to use the <em>Nintendo DSi
  Camera</em> application normally at the same time? Well now you can!<br>

  If the Memory Pit exploit is detected in <code class="notranslate">pit.bin</code>,
  <em>Nintendo DSi Camera</em> will be redirected to instead read <code class="notranslate">tip.bin</code>.

  <ul dir="auto">

  <li>This requires a ROM dump of <em>Nintendo DSi Camera</em>.</li>

  <li>If you backed up your <code class="notranslate">pit.bin</code> file before this
  release, make a copy of it, rename the copy to <code class="notranslate">tip.bin</code>,
  and add it to <code class="notranslate">sd:/private/ds/app/484E494A/</code>.</li>

  </ul>

  </li>

  <li>Added support for two DSiWare titles to be played on DS Debug console units!

  <ul dir="auto">

  <li>101 Pinball World</li>

  <li>Robot Rescue 2</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed four DSiWare <em>Rytmik</em> titles to not crash. This is achieved by
  not loading the in-game menu and cheat engine for those titles.

  <ul dir="auto">

  <li>Hip Hop King: Rytmik Edition</li>

  <li>Rytmik Retrobits</li>

  <li>Rytmik Rock Edition</li>

  <li>Rytmik World Music</li>

  </ul>

  </li>

  </ul>'
updated: '2022-07-15T06:56:01Z'
version: v0.61.3
version_title: 'v0.61.3: TWL Summer Release #5'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.