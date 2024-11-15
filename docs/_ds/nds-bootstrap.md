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
    size: 1132229
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.2.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1733536
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.2.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1192
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.12.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.12.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>AP-fixes are now included instead of having to rely on an external AP-fix from
  TWLMenu++!

  <ul dir="auto">

  <li>User-provided AP-fixes are now read from <code class="notranslate">sd:/_nds/nds-bootstrap/apFix/</code>.</li>

  </ul>

  </li>

  <li>32KB DLDI drivers (such as for N-Card) are now useable outside of B4DS mode!

  <ul dir="auto">

  <li>DSi-Enhanced/Exclusive/Ware games do not work in DSi mode (yet) (same applies
  to 16KB drivers). To play some DSiWare games, you''ll need to activate B4DS mode.</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> To avoid having to shrink the heap for <em>Sonic
  Classic Collection</em> (as well as heap shrink causing issues for that game), the
  DLDI driver has been moved to ITCM.

  <ul dir="auto">

  <li>This applies for &lt;= 16KB DLDI drivers.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed <em>Puppy Palace</em> not booting without resetting the game!</li>

  <li>Fixed a bug which caused pre-loading 28MB DSi-Enhanced ROMs (ex. <em>Bejeweled
  Twist</em>) into RAM on 3DS consoles in DS mode causing a crash.</li>

  <li><strong>B4DS mode:</strong> Fixed <em>Koukou Eitango: Kiho 400 Go Master</em>
  not booting.</li>

  <li><strong>B4DS mode:</strong> Data/instruction cache is now flushed after each
  card read for <em>Pokemon HGSS</em>.

  <ul dir="auto">

  <li>Since it''s been tried before (iirc), it may or may not fix the random crashes
  in those games.</li>

  </ul>

  </li>

  </ul>'
updated: '2024-11-15T22:17:11Z'
version: v2.2.0
version_title: v2.2.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.