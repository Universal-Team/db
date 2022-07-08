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
    size: 449250
    size_str: 438 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.61.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1081396
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.61.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.12.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.12.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><em>Black Sigil: Blade of the Exiled</em> now boots!</li>

  <li>DSi Donor ROM can now be read from TWLNAND on DSi consoles!</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Soft-resetting when connecting to Wii via Pokemon Gen 4 title is now faster!</li>

  <li>The <code class="notranslate">Expand ROM space in RAM</code> setting (<code
  class="notranslate">EXTENDED_MEMORY</code> in <code class="notranslate">nds-bootstrap.ini</code>)
  now allows wireless to work, as well as card read DMA working properly.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed a regression which made <em>Super Mario Galaxy DS</em> not boot.</li>

  <li>Fixed the mini toy sprites not displaying in <em>Mario vs. Donkey Kong: Mini-Land
  Mayhem</em> while running in DS mode!</li>

  <li>A bug fix port from 3DS to DSi, <em>Hidden Photo</em> (EUR/GER) no longer crashes
  during loading after selecting a photo.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>On DSi, the Word Search and Spot the Difference minigames in <em>Hidden Photo</em>
  (EUR) will crash. This bug does not occur in the German version.</li>

  <li>The issues that occurred after connecting to Wii via Pokemon Gen 4 title will
  still occur.</li>

  </ul>'
updated: '2022-07-08T07:44:56Z'
version: v0.61.0
version_title: 'v0.61.0: TWL Summer Release #4'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.