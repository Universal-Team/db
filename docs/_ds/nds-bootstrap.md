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
    size: 791198
    size_str: 772 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.5.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1920736
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.5.2/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.2.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.2.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed crash in <em>Zelda: Phantom Hourglass</em> when attempting to move a statue.</li>

  <li>Added failsafe checks for the files <code class="notranslate">screenshots.tar</code>,
  <code class="notranslate">ramDump.bin</code>, and <code class="notranslate">apFixOverlays.bin</code>
  placed in <code class="notranslate">sd:/_nds/nds-bootstrap/</code>. On boot, if
  one of those files are not created properly, it''ll first delete one before recreating
  the file. If the file then isn''t created properly, it''ll display an error message.</li>

  </ul>'
updated: '2024-05-10T05:28:24Z'
version: v1.5.2
version_title: v1.5.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.