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
    size: 431334
    size_str: 421 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.56.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1041807
    size_str: 1017 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.56.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.6.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.6.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> and <code>.ver</code> files, to
  <code>root:/_nds</code>.</li>

  </ol>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Added support for 5 more DSiWare titles! (Retail
  unit total: 63 -&gt; 68) (See <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/fb6a3bb2bb14b0db268c03e42d09fc999e9b8671/universal/include/incompatibleGameMap.h#L50">here</a>
  for the complete list of supported DSiWare titles.)

  <ul dir="auto">

  <li>Army Defender</li>

  <li>Calculator</li>

  <li>Flashlight</li>

  <li>Heathcliff: Spot On</li>

  <li>Mighty Milky Way (Audio playback exclusive to DS Debug consoles)</li>

  <li><strong>DS Debug exclusive:</strong> Touch Solitaire (USA version only)</li>

  </ul>

  </li>

  <li>(<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Added showing game manuals in the in-game menu!

  <ul dir="auto">

  <li>Read from <code>MANUAL_PATH</code> in <code>sd:/_nds/nds-bootstrap.ini</code></li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Improvement</strong></p>

  <ul dir="auto">

  <li>(<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations.</li>

  </ul>

  <p dir="auto"><strong>Bug fix (B4DS mode)</strong></p>

  <ul dir="auto">

  <li>Fixed <em>Super Princess Peach</em> not booting and showing an error screen.</li>

  </ul>'
updated: '2022-04-23T00:33:44Z'
version: v0.56.0
version_title: 'v0.56.0: Earth Day Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.