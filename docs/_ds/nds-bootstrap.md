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
    size: 785689
    size_str: 767 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.3.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1912120
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.3.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.7.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.7.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> 10 prototype builds of <em>Shantae: Risky''s Revenge</em>
  are now supported on DS and DS Lite!

  <ul dir="auto">

  <li>03/06/09 build</li>

  <li>Three 04/15/10 builds</li>

  <li>06/23/10 build</li>

  <li>Two 10/27/10 builds</li>

  <li>Ubisoft Build</li>

  <li>Review Build</li>

  <li>Ubisoft Review Build</li>

  </ul>

  </li>

  <li><code class="notranslate">SCSD</code> string is now checked within the DLDI
  name for SuperCard MiniSD support as well.</li>

  <li>NDMA is now used to clear RAM before booting DS homebrew.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed not being able to boot ROMs which place the arm9 binary above offset 0x4000.

  <ul dir="auto">

  <li>This makes some Chinese-translated ROMs boot again.</li>

  </ul>

  </li>

  <li>Fixed support for homebrew which give shared WRAM to arm9.

  <ul dir="auto">

  <li>The fix will not apply to DSiWarehax users.</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> Fixed various bugs related to running from Slot-2
  flashcards.</li>

  <li>Attempted to fix crashing issues in Japanese Rev A version of <em>Castlevania:
  Portrait of Ruin</em>.</li>

  <li>Attempted to fix HGSS crashing issues on boot on DSi/3DS by keeping cluster
  table cache uncompressed.</li>

  <li><strong>B4DS mode:</strong> Fixed <em>Metroid Prime Pinball</em> not booting.</li>

  <li>Fixed <em>Nintendo DS Browser</em> not booting on 3DS consoles.</li>

  </ul>'
updated: '2024-03-07T03:51:11Z'
version: v1.3.0
version_title: v1.3.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.