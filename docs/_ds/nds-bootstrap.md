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
    size: 792714
    size_str: 774 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.4.3/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1923552
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.4.3/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.0.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.0.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new? (B4DS mode)</h3>

  <ul dir="auto">

  <li>Audio in <em>Art Style: Aquia</em> now plays on (retail) DS &amp; DS Lite consoles!

  <ul dir="auto">

  <li>This is achieved by working around a memory limitation, where the game would
  first allocate memory for the compressed sdat file (1.53MB), and then allocate memory
  for the decompressed sdat file (1.63MB), which would fail because of there being
  no memory left for the decompressed data, and as a result would cause the audio
  to not play. nds-bootstrap instead does the decompression job before boot, by only
  allocating memory for the decompressed sdat file, and then streaming over the compressed
  data into the allocated area to form the decompressed data.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Further improved support for certain ROM hacks with compressed arm9 binaries
  (ex. <em>Inazuma Eleven Undub</em>, <em>Pokemon BB2/VW2</em>, etc.) in order for
  them to boot.</li>

  <li><strong>B4DS mode:</strong> Fixed an overlooked bug which caused <em>Shepherd''s
  Crossing 2 DS</em> to open with a red error screen if an Expansion Pak is inserted.</li>

  </ul>'
updated: '2024-04-08T23:57:27Z'
version: v1.4.3
version_title: v1.4.3
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.