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
    size: 1076406
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.9.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1554997
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.9.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1316
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed an overlooked bug where reads/writes of NAND saves would not work properly
  for DSi/3DS SD card users (or flashcard users running with unlocked SCFG), and would
  cause <em>WarioWare: DIY</em> and possibly other games which use NAND saves to not
  boot.</li>

  </ul>'
updated: '2025-10-25T21:36:28Z'
version: v2.9.1
version_title: v2.9.1 (hotfix)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.