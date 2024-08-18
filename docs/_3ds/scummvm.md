---
author: ScummVM
avatar: https://avatars.githubusercontent.com/u/365181?v=4
categories:
- emulator
color: '#507f20'
color_bg: '#507f20'
created: '2011-02-12T15:50:57Z'
description: Point-and-click adventure game engines
download_page: https://www.scummvm.org/downloads/
downloads:
  scummvm-3dsx.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.8.1/scummvm-2.8.1-3ds-3dsx.zip
  scummvm-cia.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.8.1/scummvm-2.8.1-3ds-cia.zip
  scummvm-ds.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.8.1/scummvm-2.8.1-ds.zip
eval_downloads: true
github: scummvm/scummvm
icon: https://raw.githubusercontent.com/scummvm/scummvm/master/backends/platform/3ds/app/icon.png
image: https://raw.githubusercontent.com/scummvm/scummvm/master/backends/platform/3ds/app/banner.png
image_length: 17658
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://buildbot.scummvm.org/dailybuilds/master/
  downloads:
    3ds-master-latest.zip:
      url: https://buildbot.scummvm.org/dailybuilds/master/3ds-master-latest.zip
    nds-master-latest.zip:
      url: https://buildbot.scummvm.org/dailybuilds/master/nds-master-latest.zip
source: https://github.com/scummvm/scummvm
stars: 2261
systems:
- 3DS
- DS
title: scummvm
unique_ids:
- '0xFF321'
update_notes: '<p dir="auto">The ScummVM Team is proud to announce the first release
  of 2024 - Oh MMy!</p>

  <h3 dir="auto">General:</h3>

  <ul dir="auto">

  <li>Fixed GLSL version parsing on some OpenGL ES2 platforms.</li>

  <li>Don''t try to use shaders on old OpenGL implementations.</li>

  </ul>

  <h3 dir="auto">AGI:</h3>

  <ul dir="auto">

  <li>Fixed Space Quest 1 version 1.0X freezing in the skimmer.</li>

  <li>Fixed Mixed-Up Mother Goose message boxes during nursery rhymes.</li>

  <li>Fixed Mixed-Up Mother Goose graphics in Amiga version.</li>

  <li>Fixed Gold Rush clock time at Fast and Fastest speeds.</li>

  <li>Fixed Atari ST version of Manhunter 1 not starting.</li>

  <li>Fixed Tandy CoCo3 version of Leisure Suit Larry 1 not starting.</li>

  <li>Fixed Tandy CoCo3 unofficial ports not starting.</li>

  <li>Fixed Amiga menus in Space Quest 1, Manhunter 1, and Manhunter 2.</li>

  <li>Fixed Graham facing away from the king in King''s Quest 1.</li>

  <li>Fixed Alexander getting stuck on the stairs in King''s Quest 3.</li>

  <li>Fixed Larry being able to shoplift in Leisure Suit Larry 1.</li>

  <li>Fixed ducks not jumping at the start of Donald Duck''s Playground.</li>

  <li>Fixed instant death in fan game "Phil''s Quest: The Search for Tolbaga".</li>

  <li>Fixed buttons freezing in fan game "DG: The AGIMouse Adventure".</li>

  <li>Fixed unrecognized words in fan game "V - The Graphical Adventure".</li>

  <li>Added detection for Macintosh version of Mixed-Up Mother Goose.</li>

  </ul>

  <h3 dir="auto">AGS:</h3>

  <ul dir="auto">

  <li>Updated detection tables.</li>

  <li>Simplified character import from Sierra games for QfG2 AGDI.</li>

  <li>Fixed graphical glitch affecting Unavowed and Heroine''s Quest.</li>

  <li>Fixed partial outlines for some letters in Kathy Rain.</li>

  <li>Fixed crash in Alum.</li>

  <li>Added stub to prevent crash at the beginning of Falcon City.</li>

  </ul>

  <h3 dir="auto">Broken Sword 2:</h3>

  <ul dir="auto">

  <li>Fixed crash when quitting the game while it was paused.</li>

  </ul>

  <h3 dir="auto">MM:</h3>

  <ul dir="auto">

  <li>Enabled engine, allowing MM1 and Xeen to be compiled.</li>

  <li>Added MT32/LAPC-1 support for Xeen engine.</li>

  <li>Fixed Xeen regression which caused some sound effects to stop abruptly.</li>

  </ul>

  <h3 dir="auto">mTropolis:</h3>

  <ul dir="auto">

  <li>Fixed crash in Muppet Treasure Island on some platforms.</li>

  <li>Fixed jewel puzzle in Muppet Treasure Island not being randomized.</li>

  </ul>

  <h3 dir="auto">NANCY:</h3>

  <ul dir="auto">

  <li>Fixed the telephone hints in Secrets Can Kill.</li>

  <li>Fixed the crashing and drawing issues on ARM machines when playing<br>

  Message in a Haunted Mansion''s maze minigame.</li>

  <li>Fixed the ''M'' keyboard key not working in Message in a Haunted Mansion.</li>

  <li>Allowed general keymaps to be shown in the engine Keymaps menu.</li>

  <li>Virtual keyboard now correctly triggers on/off wherever text input is needed.</li>

  </ul>

  <h3 dir="auto">SCUMM:</h3>

  <ul dir="auto">

  <li>Fix screen corruption (and sometimes even crashes) in Mac Loom and<br>

  Indiana Jones and the Last Crusade, most noticeably when using menu<br>

  shortcut keys.</li>

  <li>Fix enabling/disabling of Open and Save in Mac Indiana Jones and the Last<br>

  Crusade.</li>

  </ul>

  <h3 dir="auto">TWINE:</h3>

  <ul dir="auto">

  <li>Fix ladder climbing regression.</li>

  <li>Fix scenery zoom issue.</li>

  <li>Fix animation glitches after using the holomap.</li>

  </ul>

  <h3 dir="auto">Ultima:</h3>

  <ul dir="auto">

  <li>Fix Ultima VIII hidden minimap blocking keyring use.</li>

  <li>Fix Ultima VIII page breaks in books.</li>

  <li>Fix Ultima VIII text centering for plaques.</li>

  <li>Fix Ultima VIII crash on dragging items to screen edge.</li>

  <li>Fix Ultima VIII unexpected jumping on left click.</li>

  <li>Fix Ultima VIII camera during cutscenes for Shrine of the Ancient Ones.</li>

  <li>Fix Ultima VIII invalid placement of items within containers.</li>

  <li>Fix Ultima VIII never-ending lava sounds.</li>

  </ul>

  <h3 dir="auto">V-Cruise:</h3>

  <ul dir="auto">

  <li>Fixed crash in Reah: Face the Unknown and Schizm: Mysterious Journey<br>

  when music is muted.</li>

  </ul>

  <h3 dir="auto">Android port:</h3>

  <ul dir="auto">

  <li>Fixed crash in built-in help with German language.</li>

  </ul>

  <h3 dir="auto">Atari port:</h3>

  <ul dir="auto">

  <li>Fixed crash when exiting ScummVM.</li>

  <li>Fixed BBVS (and possibly others) gameplay by using more precise math model.</li>

  </ul>

  <h3 dir="auto">macOS port:</h3>

  <ul dir="auto">

  <li>Fixed a problem where some Mac games would not load resources correctly.</li>

  <li>Updated application icon to conform with modern standards.</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2.8.0...v2.8.1"><tt>v2.8.0...v2.8.1</tt></a></p>'
updated: '2024-03-31T19:25:25Z'
version: v2.8.1
version_title: 'ScummVM 2.8.1: "Oh MMy!"'
website: https://www.scummvm.org
---
ScummVM allows you to play classic graphic point-and-click adventure games, text adventure games, and RPGs, as long as you already have the game data files. ScummVM replaces the executable files shipped with the games, which means you can now play your favorite games on all your favorite devices.

While ScummVM was originally designed to run LucasArts’ SCUMM games, over time support has been added for many other games: see the full list [on our wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Noteworthy titles include Broken Sword, Myst and Blade Runner, although there are countless other hidden gems to explore.