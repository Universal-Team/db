---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 401707
    size_str: 392 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.53.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 968647
    size_str: 945 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.53.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 140
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v23.3.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v23.3.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto"><strong>Improvements</strong></p>

  <ul dir="auto">

  <li>Retail DSi consoles now load the complete AP-fix .ips file while in DSi mode.

  <ul dir="auto">

  <li>DSi mode heap has shrunken further to make room for AP-patched overlays.</li>

  </ul>

  </li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations.</li>

  </ul>

  <p dir="auto"><strong>Bug fix</strong></p>

  <ul dir="auto">

  <li>Part of RAM is now restored after taking screenshots while in DSi mode.</li>

  </ul>

  <p dir="auto"><strong>Bug fix / Regression</strong></p>

  <ul dir="auto">

  <li>SDK5.4 &amp; 5.5 games have reverted to the slow soft-reset method (due to crashing,
  apparently from timing issues), but can be worked around by enabling either TWL
  clock speed or DSi mode.</li>

  </ul>'
updated: '2021-12-27T22:49:14Z'
version: v0.53.1
version_title: v0.53.1 (hotfix)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.