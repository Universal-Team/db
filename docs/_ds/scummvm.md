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
    url: https://downloads.scummvm.org/frs/scummvm/2.9.1/scummvm-2.9.1-3ds-3dsx.zip
  scummvm-cia.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.9.1/scummvm-2.9.1-3ds-cia.zip
  scummvm-ds.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.9.1/scummvm-2.9.1-ds.zip
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
stars: 2599
systems:
- 3DS
- DS
title: scummvm
unique_ids:
- '0xFF321'
update_notes: '<p dir="auto">Get ready to jam and slap da BASS!</p>

  <p dir="auto">Yes, it is this time of the year again! Please welcome the first ScummVM
  release of the year: ScummVM 2.9.1.</p>

  <p dir="auto">This maintenance release mainly focused on fixing bugs that our developers
  and users have uncovered since our last stable release.</p>

  <h1 dir="auto">AGI:</h1>

  <ul dir="auto">

  <li>Added support for early version of Christmas Card 1986 with advertisements<br>

  for Tandy hardware.</li>

  <li>Fixed many graphics bugs and improved responsiveness in Mickey''s Space<br>

  Adventure, Winnie The Pooh In The Hundred Acre Wood, and Troll''s Tale.</li>

  <li>Save games in Mickey''s Space Adventure now restore to the planet they<br>

  were saved on instead of Earth.</li>

  </ul>

  <h1 dir="auto">AGS:</h1>

  <ul dir="auto">

  <li>Added official support for Old Skies and Rosewater.</li>

  <li>Added support for sound clip speed variation, used in some games to<br>

  slow down background music or other audio effects.</li>

  <li>Fixed some audio volume changes not being triggered in some situations<br>

  (e.g. automatic music volume drop during dev commentary or when a<br>

  characters speaks, in the Blackwell series).</li>

  <li>Added/updated detection entries for various AGS games.</li>

  </ul>

  <h1 dir="auto">Asylum:</h1>

  <ul dir="auto">

  <li>Fixed crash in Sanitarium main menu, when moving the cursor to the<br>

  top part of the screen.</li>

  </ul>

  <h1 dir="auto">BAGEL:</h1>

  <ul dir="auto">

  <li>Fixed crash when inserting the credit card in the slot machine.</li>

  </ul>

  <h1 dir="auto">Bladerunner:</h1>

  <ul dir="auto">

  <li>Fixed 2x scaling and fullscreen support in non-interactive demo.</li>

  <li>Fixed memory leaks that could cause Out of Memory issues on some<br>

  ports.</li>

  <li>Fixed a path finding issue that could cause soft-lock in some rare cases.</li>

  </ul>

  <h1 dir="auto">Hopkins:</h1>

  <ul dir="auto">

  <li>Fixed a crash when using the elevator to go to other floors.</li>

  </ul>

  <h1 dir="auto">MADS:</h1>

  <ul dir="auto">

  <li>Fixed Rex Nebular inventory and verb area UIs not updating.</li>

  </ul>

  <h1 dir="auto">NGI:</h1>

  <ul dir="auto">

  <li>Optimized game resource loading, improving the performance on<br>

  Android.</li>

  </ul>

  <h1 dir="auto">SCI:</h1>

  <ul dir="auto">

  <li>Fixed KQ6 CD crash when talking to Rotten Tomato from inventory window in<br>

  high-resolution mode. (ScummVM 2.9.0 bug)</li>

  <li>Fixed KQ4 Amiga skipping title screen. (ScummVM 2.8.0 bug)</li>

  <li>Fixed QFG4 v1.0 crash in Thieves'' Guild. (ScummVM 2.1.0 bug)</li>

  <li>Fixed messages disappearing every 18.2 minutes in BRAIN1, LSL5, and SQ1.<br>

  (Original game bug)</li>

  <li>Fixed SQ5 introduction comets not appearing on machines faster than a 386.<br>

  (Original game bug)</li>

  <li>Fixed LSL1 lockup when entering casino. (Original game bug)</li>

  <li>Fixed LSL6 crash when entering hotel. (Original game bug)</li>

  <li>Fixed LSL6-HIRES tram disappearing after restarting game.<br>

  (Original game bug)</li>

  <li>Fixed LSL6 help cursor not appearing. (Original game bug)</li>

  <li>Fixed QFG1 EGA lockup when tripping over trip wire. (Original game bug)</li>

  <li>Fixed KQ1 lockup when drowning in cave. (Original game bug)</li>

  <li>Fixed GK1 day 5 phone lockup in all game versions at all speeds.<br>

  (Original game bug)</li>

  <li>Fixed incorrect blue dither pattern in EGA vector pictures.<br>

  (All SCI tools since SCI Decoder in 1992)</li>

  </ul>

  <h1 dir="auto">SCUMM:</h1>

  <ul dir="auto">

  <li>Restored the ScummVM 2.7.0 behavior of allowing all the DOS v2-v4<br>

  (i.e. Maniac Mansion to Monkey1) EGA titles to be played with the<br>

  Amiga palette again, using the Render mode game option.</li>

  <li>Fixed most of the iMUSE tracks being silent in the Booty Store,<br>

  in Monkey2.</li>

  <li>Fixed an accuracy issue with some character positioning in SCUMMv2<br>

  and below. This would happen when interacting with the devotee at<br>

  the airport in Zak McKracken (all releases but the FM-TOWNS one),<br>

  for instance.</li>

  <li>Fixed Moonbase Commander multiplayer mode crashing guests when<br>

  starting the game.</li>

  <li>Fixed pops in Sega CD Monkey1 sound effects.</li>

  <li>Fixed saving over an existing save in COMI.</li>

  <li>Fixed excessive MIDI messages being sent during iMUSE music volume<br>

  reduction (e.g. in the Sam &amp; Max intro), which could cause<br>

  slowed-down, garbled speech when using older, real MIDI hardware.</li>

  <li>Fixed an iMUSE crash when loading an older savegame with a sound<br>

  fade in progress.</li>

  <li>Fixed the Jolly Roger enhancement for Monkey1; enabling this<br>

  enhancement would prevent this flag from appearing when it should<br>

  no longer be visible anymore, but the fix was incomplete in some<br>

  VGA floppy releases.</li>

  <li>Fixed the enhancement for Smirk''s cigar smoke in Monkey1 FM-TOWNS.</li>

  </ul>

  <h1 dir="auto">Sky:</h1>

  <ul dir="auto">

  <li>Fixed a crash in the intro of Beneath a Steel Sky on some platforms,<br>

  such as Android.</li>

  </ul>

  <h1 dir="auto">Sword1:</h1>

  <ul dir="auto">

  <li>Fixed audio balance issue when using the Windows executable option.</li>

  </ul>

  <h1 dir="auto">Tetraedge:</h1>

  <ul dir="auto">

  <li>Improved OpenGL vs. software rendering support, preventing the<br>

  engine from erroring out on Android and some other platforms.</li>

  </ul>

  <h1 dir="auto">Tinsel:</h1>

  <ul dir="auto">

  <li>Fixed Discworld Save/Load menu becoming inaccessible.</li>

  </ul>

  <h1 dir="auto">Tucker:</h1>

  <ul dir="auto">

  <li>Fixed skipping cutscenes, when the Esc key is mapped.</li>

  </ul>

  <h1 dir="auto">TwinE:</h1>

  <ul dir="auto">

  <li>Fixed crash when restarting a game from the launcher a second time.</li>

  <li>Fixed pressing Space in normal mode not triggering Use/Talk action.</li>

  <li>Fixed meca penguin movement.</li>

  <li>Fixed sound related issues.</li>

  </ul>

  <h1 dir="auto">TWP:</h1>

  <ul dir="auto">

  <li>Added an error message when trying to play Thimbleweed Park on<br>

  platforms not having support for OpenGL with shaders.</li>

  </ul>

  <h1 dir="auto">3DS port:</h1>

  <ul dir="auto">

  <li>Fix top screen not fully rendering in some cases.</li>

  </ul>

  <h1 dir="auto">Android port:</h1>

  <ul dir="auto">

  <li>Added a feature to let users backup and restore their configuration<br>

  and saves.</li>

  <li>Enabled NEON support by default, resulting in better performance for<br>

  the vast majority of older Android devices.</li>

  <li>Worked around a bug in ARMv7a Android 6.0 and below, which could<br>

  cause some game options to be missing, for example.</li>

  <li>Increased stack allocation for Android Java thread, benefiting game<br>

  engines that heavily use the stack.</li>

  </ul>

  <h1 dir="auto">Atari port:</h1>

  <ul dir="auto">

  <li>Fixed sending of SysEx MIDI messages.</li>

  <li>Fixed crash and distorted audio with certain audio settings.</li>

  <li>Fixed performance issues with SCI32 games like Phantasmagoria or<br>

  KQ7.</li>

  <li>Various GUI / backend fixes and optimizations.</li>

  </ul>

  <h1 dir="auto">iOS/iPadOS port:</h1>

  <ul dir="auto">

  <li>Fixed Fluidsynth soundfont existence check failing with sandboxed<br>

  filesystems.</li>

  </ul>

  <h1 dir="auto">macOS port:</h1>

  <ul dir="auto">

  <li>Fixed ScummVM failing to start when the monitor settings are not<br>

  set to "Millions of colors", on older macOS releases.</li>

  <li>Fixed Audio CD support when playing from original discs on Snow<br>

  Leopard and earlier.</li>

  </ul>

  <h1 dir="auto">Windows port:</h1>

  <ul dir="auto">

  <li>Restored FLAC support in the Windows 9x port.</li>

  </ul>

  <hr>

  <p dir="auto">Thanks to all contributors, supporters, testers, bug-reporters, and
  fans for helping build yet another great release!</p>

  <hr>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2.9.0...v2.9.1"><tt>v2.9.0...v2.9.1</tt></a></p>'
updated: '2025-05-25T14:33:34Z'
version: v2.9.1
version_title: 'ScummVM 2.9.1: "Slappin da BASS"'
website: https://www.scummvm.org
---
ScummVM allows you to play classic graphic point-and-click adventure games, text adventure games, and RPGs, as long as you already have the game data files. ScummVM replaces the executable files shipped with the games, which means you can now play your favorite games on all your favorite devices.

While ScummVM was originally designed to run LucasArts’ SCUMM games, over time support has been added for many other games: see the full list [on our wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Noteworthy titles include Broken Sword, Myst and Blade Runner, although there are countless other hidden gems to explore.