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
    size: 421334
    size_str: 411 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.57.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1024091
    size_str: 1000 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.57.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.7.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.7.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <p dir="auto"><strong>What''s new? (B4DS mode)</strong></p>

  <ul dir="auto">

  <li>Added support for 5 more DSiWare titles! (Retail unit total: 68 -&gt; 73) (See
  <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/dc9d8897d4819032b9328da93493413948e7b28f/universal/include/incompatibleGameMap.h#L50">here</a>
  for the complete list of supported DSiWare titles.)

  <ul dir="auto">

  <li>Ah! Heaven</li>

  <li>Art Style: Boxlife (All of the <em>Art Style</em> titles except <em>Digidrive</em>
  are now supported!)</li>

  <li>Puzzle League: Express</li>

  <li>Quick Fill Q</li>

  <li>Robot Rescue</li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Improvement/Bug fix (B4DS mode)</strong></p>

  <ul dir="auto">

  <li>With the game''s heap being shrunk by the cardEngine ARM9 binary size, it is
  now shrunk by the FAT table cache size in addition, instead of always shrinking
  by 128KB in total (if no Memory Expansion Pak is inserted).

  <ul dir="auto">

  <li>This fixes some DS games in order for them to boot without a Memory Expansion
  Pak (ex. Pokemon HGSS, GTA Chinatown Wars, CTGP Nitro, etc.)!</li>

  <li>For DSiWare, the FAT table cache is located before the game''s code in RAM,
  in order to avoid having to shrink the heap further, and if the FAT table cache
  is 16KB or less.</li>

  <li>Your flashcard''s SD card needs to be formatted with &gt;= 32KB cluster size
  for this feature to work as best as possible. (You do not need to do anything if
  TWLMenu++ does not show a message about cluster size.)</li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li>Fixed <em>Absolute BrickBuster</em>, <em>Absolute Chess</em>, and <em>Absolute
  Reversi</em> showing save data errors.</li>

  <li>Fixed SDK5.0 DSiWare titles not booting if only SDK5.1+ Donor ROM is set. (Only
  applies to DSiWarehax users.)</li>

  <li>Switched to THUMB code with <code class="notranslate">Os</code> flag for the
  cardenginei binaries, in order to improve speed a tiny bit, as well as trying to
  fix oddball issues.</li>

  <li><strong>B4DS mode:</strong> Attempted to fix crashing in <em>JellyCar 2</em>
  by opening up the heap a bit more.</li>

  </ul>'
updated: '2022-05-06T03:56:24Z'
version: v0.57.0
version_title: 'v0.57.0: 5th Month, 5th Day, and 5 newly supported DSiWare'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.