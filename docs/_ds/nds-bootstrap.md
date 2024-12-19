---
author: DS-Homebrew
avatar: https://private-avatars.githubusercontent.com/u/46971470?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MzQ2MjUyNjAsIm5iZiI6MTczNDYyNDA2MCwicGF0aCI6Ii91LzQ2OTcxNDcwIn0.31_pTtdS7jmVQLxfm0ezSnfmVzyly88I6JpYHxoexbM&v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 1117140
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.2.2/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1667132
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.2.2/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1194
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.12.2"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.12.2</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Attempted to fix occasional crashing in Gen 5 Pokemon games running in DSi mode
  on DSi consoles.

  <ul dir="auto">

  <li>Achieved by shrinking the heap by 2.5MB instead of 512KB, which increases LRU
  cache space as a result.</li>

  </ul>

  </li>

  <li>Fixed <em>Rockman EXE: Operate Shooting Star</em> crashing on 3DS consoles when
  opening Star Colosseum.</li>

  <li><em>Iron Man 2</em> now boots again on DSi/3DS SD Card by fixing an overlooked
  bug which has occurred since v1.6.0.</li>

  <li>Fixed an overlooked bug which caused card read DMA to not work (and as a result,
  possible crashing) for pre-loadable DSi-Exclusive ROMs on 3DS consoles.</li>

  </ul>'
updated: '2024-11-26T07:45:21Z'
version: v2.2.2
version_title: v2.2.2
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.