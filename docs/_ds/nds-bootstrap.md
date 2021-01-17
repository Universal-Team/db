---
author: DS-Homebrew
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.35.1
downloads:
  nds-bootstrap.7z:
    size: 440991
    size_str: 430 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.35.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1088985
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.35.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://raw.githubusercontent.com/DS-Homebrew/nds-bootstrap/master/retail/assets/icon.bmp
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
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p>Instructions:</p>

  <ol>

  <li>Download the .7z file.</li>

  <li>Extract the nds-bootstrap (or B4DS, for DS-mode flashcards) .nds files, to <code>root:/_nds</code>.</li>

  <li>Extract the .ver file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>The FAT table has been relocated from DSi WRAM to Main RAM.<br>

  This removes the need to reboot in DSiWarehax, after creating the FAT table.<br>

  Also works around a mirroring bug in DSi WRAM, and allows running games with DSiWarehax
  without saving the FAT table cache.</li>

  <li>mpuInitOffset is now cached. This should improve boot times slightly.</li>

  </ul>

  <p><strong>Bug fixes (B4DS)</strong></p>

  <ul>

  <li>Fixed Pokemon Gen 4 compatibility.</li>

  <li>FAT table has been moved forward by 8KB, so it is not overwriting DTCM.</li>

  </ul>'
updated: '2020-05-09T19:31:50Z'
version: v0.35.1
version_title: v0.35.1
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.