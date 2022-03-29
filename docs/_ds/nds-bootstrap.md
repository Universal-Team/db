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
    size: 430129
    size_str: 420 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.55.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1038180
    size_str: 1013 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.55.2/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.3.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.3.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li>The cursor in the in-game menu is now wrapped.</li>

  </ul>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li><strong>SD users:</strong> Card data of around the exact length is no longer
  loaded all at once, fixing weird crashes in some games.</li>

  <li>Fixed some areas of RAM not being dumped in certain games.</li>

  <li><strong>B4DS:</strong> Fixed <em>Frogger Returns</em> not showing publisher
  &amp; developer logos on boot.</li>

  </ul>

  <p dir="auto"><strong>Regression</strong></p>

  <ul dir="auto">

  <li><em>Dragon Quest V</em> now loops back to the company logos before playing the
  opening music.

  <ul dir="auto">

  <li>TWL clock speed may fix the issue.</li>

  </ul>

  </li>

  </ul>'
updated: '2022-03-27T02:53:22Z'
version: v0.55.2
version_title: v0.55.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.