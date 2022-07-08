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
    size: 448908
    size_str: 438 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.61.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1080919
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.61.1/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.12.10"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.12.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed an overlooked bug which caused SDK5 titles to not boot in DS mode. (B4DS
  mode has not been affected by the bug.)</li>

  <li>Fixed an overlooked bug which caused the ARM7 SCFG patch registers to overwrite
  the FAT table cache when running a non-DSiWare TWL title in DSi mode (which would
  be noticeable if the SD cluster size is lower than 32KB).</li>

  </ul>'
updated: '2022-07-08T17:02:56Z'
version: v0.61.1
version_title: v0.61.1 (hotfix)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.