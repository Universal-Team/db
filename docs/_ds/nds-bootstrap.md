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
    size: 723309
    size_str: 706 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.72.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1732879
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.72.0/nds-bootstrap.zip
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
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.10.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.10.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><em>2006-Nen 10-Gatsu Taikenban Soft</em> now boots!</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>NDMA is now only used for SD reads aligned by 4-bytes. CPU is used for non-aligned
  reads.

  <ul dir="auto">

  <li>NAND saving (used by <em>WW: DIY</em>, <em>Jam with the Band</em>, and <em>Face
  Training</em>) should now be working properly again.</li>

  <li>Should improve compatibility with certain homebrew, in the case of those using
  non-aligned reads.</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> Audio glitching should no longer occur when reading
  or writing save data.

  <ul dir="auto">

  <li>Tested with R4(i) Ultra and R4i-SDHC. Not tested with Ace3DS+ (which was known
  to have the bug).</li>

  </ul>

  </li>

  </ul>'
updated: '2023-06-05T20:38:47Z'
version: v0.72.0
version_title: v0.72.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.