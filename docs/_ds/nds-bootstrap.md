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
    size: 575677
    size_str: 562 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.68.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1335974
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.68.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.7.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.7.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <h4 dir="auto">DS &amp; DS lite (B4DS mode)</h4>

  <ul dir="auto">

  <li>Special thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Gericom/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Gericom">@Gericom</a>:
  Added a huge compatibility improvement, making a lot more DS games compatible!

  <ul dir="auto">

  <li>Compatibility is now near the level of DSi/3DS SD card.</li>

  </ul>

  </li>

  <li>Added support for 4 more DSiWare titles!

  <ul dir="auto">

  <li>Scroll down to see which titles are now supported.</li>

  <li>Click &gt;<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/184d8e864c9e70c20fdab0a600411e6bb4dfe18b/universal/include/compatibleDSiWareMap.h">here</a>&lt;
  for the full list of supported titles.</li>

  </ul>

  </li>

  <li>A few more DSiWare titles can now open the manual screen.

  <ul dir="auto">

  <li>Certain ones will require a Memory Expansion Pak to open it.</li>

  </ul>

  </li>

  <li>A standalone donor arm7 binary from a DSi-Enhanced ROM can now be loaded from
  <code class="notranslate">fat:/_nds/nds-bootstrap/</code> for running DSiWare.

  <ul dir="auto">

  <li>File must be named <code class="notranslate">b4dsTwlDonor.bin</code>.</li>

  <li>This saves space compared to setting an individual DSi-Enhanced ROM as a donor.</li>

  </ul>

  </li>

  <li>You can now properly exit back to TWiLight Menu++ using the <code class="notranslate">Quit
  Game</code> option in the in-game menu!</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed <em>Yoshi Touch &amp; Go</em> (Europe) not booting.

  <ul dir="auto">

  <li>An SDK2.0 donor ROM is now required for it to boot.</li>

  </ul>

  </li>

  <li>Fixed saving not working in <em>Eigo ga Nigate na Otona no DS Training: Eigo
  Zuke</em>.</li>

  </ul>

  <h4 dir="auto">DS &amp; DS lite (B4DS mode)</h4>

  <ul dir="auto">

  <li>Fixed static sound playing for certain users.</li>

  </ul>

  <h4 dir="auto">DSi &amp; 3DS</h4>

  <ul dir="auto">

  <li>Fixed dev/debug TWL ROMs not booting.</li>

  <li>Fixed <code class="notranslate">TWLFontTable.dat</code> being opened on non-CHN/KOR
  consoles.</li>

  </ul>

  <h3 dir="auto">Known bug (B4DS mode)</h3>

  <ul dir="auto">

  <li>The <code class="notranslate">Quit Game</code> option may not work after using
  the <code class="notranslate">Reset Game</code> option.</li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite</h3>

  <ul dir="auto">

  <li>Goooooal America

  <ul dir="auto">

  <li>Audio is disabled to fit within RAM limitations</li>

  </ul>

  </li>

  <li>Music on: Electric Guitar</li>

  <li>Music on: Electronic Keyboard</li>

  <li>Snakenoid Deluxe

  <ul dir="auto">

  <li>Audio is disabled to fit within RAM limitations</li>

  </ul>

  </li>

  </ul>'
updated: '2022-12-25T04:10:54Z'
version: v0.68.0
version_title: 'v0.68.0: TWL Christmas release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.