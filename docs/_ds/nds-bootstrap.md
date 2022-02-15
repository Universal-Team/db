---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 431370
    size_str: 421 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.54.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1042693
    size_str: 1018 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.54.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 140
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.0.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.0.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto">Happy Valentine''s Day! Here''s a new version of nds-bootstrap filled
  with sweet new features!</p>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Here''s a heart-shaped box &lt;3 full of added support
  for more DSiWare titles on DS/DS lite consoles!<br>

  (For a complete list of supported titles, see this list <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/dca0a8bf0dc3934c5790cfe22ce3072c3bbf14a9/universal/include/incompatibleGameMap.h#L51">here</a>.)

  <ul dir="auto">

  <li>1950s Lawn Mower Kids</li>

  <li>Bomberman Blitz</li>

  <li>Castle Conqueror: Heroes</li>

  <li>Cave Story</li>

  <li>Chuck E. Cheese''s Alien Defense Force</li>

  <li>Chuck E. Cheese''s Arcade Room</li>

  <li>Color Commando</li>

  <li>Crash-Course Domo</li>

  <li>DotMan</li>

  <li>Frogger Returns</li>

  <li>Hard-Hat Domo</li>

  <li>JellyCar 2</li>

  <li>Lola''s Alphabet Train</li>

  <li>Magnetic Joe</li>

  <li>Monster Buster Club</li>

  <li>Number Battle (USA version only)</li>

  <li>GO Series: Portable Shrine Wars</li>

  <li>Pro-Putt Domo</li>

  <li>Rock-n-Roll Domo</li>

  <li>Shantae: Risky''s Revenge</li>

  <li>EA''s Sudoku</li>

  <li>Sudoku 4Pockets</li>

  <li>Wakugumi: Monochrome Puzzle</li>

  <li>White-Water Domo</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> RAM dumping has been added to the in-game menu!</li>

  <li>SWI Halt Hook has been removed, due to issues with slowdown.</li>

  <li>The in-game menu is now accessible in DSiWare titles!

  <ul dir="auto">

  <li>In addition, the title can be exited back into TWLMenu++ without rebooting the
  console!</li>

  </ul>

  </li>

  <li>Version number is now printed in the debug screen (if enabled).</li>

  </ul>

  <p dir="auto"><strong>Improvements</strong></p>

  <ul dir="auto">

  <li>Improvements to the SD and card read DMA code have been made in order to (somewhat/maybe)
  slightly improve speed, as well as fixing (some?) wireless communication errors.</li>

  </ul>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li><em>Nintendo DSi Camera</em> &amp; <em>Nintendo DSi Sound</em> now boot again!</li>

  <li>Fixed soft-reset not working in supported DSiWare titles.</li>

  <li>Certain DSiWare titles should now access the SD card again, instead of giving
  an error or whatever the title does.</li>

  <li>Fixed AP-patching not working properly for ROMs loaded into RAM in DS mode.</li>

  <li>Screen-swapping now works properly again.</li>

  </ul>

  <p dir="auto"><strong>Known bug</strong></p>

  <ul dir="auto">

  <li>In <em>Shantae: Risky''s Revenge</em> (when played in B4DS mode), only the first
  fight is playable. The game cannot go further than that, and music is disabled,
  both due to memory limitations.</li>

  </ul>'
updated: '2022-02-15T01:23:51Z'
version: v0.54.0
version_title: Valentine's Day Release (2022)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.