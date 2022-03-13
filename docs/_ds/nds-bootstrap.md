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
    size: 432845
    size_str: 422 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.54.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1045432
    size_str: 1020 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.54.2/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 141
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.1.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.1.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li>Fixed <em>Rabbids Go Home</em> not booting in DSi mode.</li>

  <li>Fixed saving not working in <em>Lufia: Curse of the Sinistrals</em>.</li>

  <li>Pre-loaded ROM hacks containing data beyond the ROM size in the header, now
  has the data loaded.

  <ul dir="auto">

  <li>It is recommended to manually fix the ROM size in the header, to avoid further
  issues.</li>

  </ul>

  </li>

  <li>Fixed <em>Mario''s Holiday</em> versions before Rev 11 not booting on 3DS.</li>

  <li>Fixed exception screen not shown in <em>CTGP Nitro</em>.</li>

  <li>Other minor fixes.</li>

  </ul>'
updated: '2022-02-28T21:25:59Z'
version: v0.54.2
version_title: v0.54.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.