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
    size: 386567
    size_str: 377 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.50.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 937228
    size_str: 915 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.50.2/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> <em>Nintendo DSi + Internet</em> now boots!</li>

  <li>Saving is now stubbed out in a few DSiWare titles in order to proceed further,
  when running from a CycloDS iEvolution.

  <ul dir="auto">

  <li><strong>Known affected games:</strong>

  <ul dir="auto">

  <li>A Little Bit of... Nintendo Touch Golf</li>

  <li>Asphalt 4: Elite Racing</li>

  <li>Aura-Aura Climber</li>

  <li>Brain Challenge</li>

  <li>Cave Story</li>

  <li>Ferrari GT: Evolution</li>

  <li>Plants vs. Zombies</li>

  <li>Puzzle League: Express</li>

  <li>Rayman</li>

  <li>Tetris Party Live</li>

  </ul>

  </li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li>Fixed an overlooked bug due to optimized code, which caused AP-patching to not
  work properly for SDK5 games on DSi.</li>

  <li>Increased the file size limit of AP-fix .ips patches from 192KB to 256KB.

  <ul dir="auto">

  <li>This fixes <em>Rabbids Go Home</em> (Only DS mode tested on DSi).</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> Fixed AP-patching not working properly, when using
  a Memory Expansion Pak.</li>

  <li>Fixed WiFi not working when running from a CycloDS iEvolution.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed ARM7 RAM viewer randomly freezing.</li>

  <li>Fixed an overlooked bug which caused <em>Kirby Canvas Curse</em> to lockup on
  the logos with empty save data and with SWI Halt Hook turned on.</li>

  <li>Fixed EUR version of <em>Hotel Dusk: Room 215</em> not booting.</li>

  </ul>'
updated: '2021-11-12T06:30:22Z'
version: v0.50.2
version_title: v0.50.2
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.