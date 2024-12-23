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
    url: https://downloads.scummvm.org/frs/scummvm/2.9.0/scummvm-2.9.0-3ds-3dsx.zip
  scummvm-cia.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.9.0/scummvm-2.9.0-3ds-cia.zip
  scummvm-ds.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2.9.0/scummvm-2.9.0-ds.zip
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
stars: 2338
systems:
- 3DS
- DS
title: scummvm
unique_ids:
- '0xFF321'
update_notes: '<p dir="auto">Almost one year after the last major release, and just
  in time for Christmas, ScummVM 2.9.0 - "Close Encounters of the 2.9th Kind" has
  landed. Amongst its gifts, you will find 15 newly supported games and a new supported
  platform.</p>

  <h2 dir="auto">New games:</h2>

  <ul dir="auto">

  <li>Added support for Orion Burger.</li>

  <li>Added support for Total Eclipse and Total Eclipse 2.</li>

  <li>Added support for Thimbleweed Park.</li>

  <li>Added support for The Space Bar.</li>

  <li>Added support for Moonbase Commander.</li>

  <li>Added support for Backyard Basketball.</li>

  <li>Added support for Unrest.</li>

  <li>Added support for Rise of the Dragon.</li>

  <li>Added support for Castle Master.</li>

  <li>Added support for Wait for it! Issue 3. Song for a Hare.</li>

  <li>Added support for Mask Show.</li>

  <li>Added support for Marvellous Mice Adventures: Meeting Sea Rat.</li>

  <li>Added support for The Adventures of the Good Soldier Schweik.</li>

  <li>Added support for Marvellous Mice Adventures: Sea Rat''s Birthday.</li>

  </ul>

  <h2 dir="auto">New platforms:</h2>

  <ul dir="auto">

  <li>Added SailfishOS port.</li>

  </ul>

  <h2 dir="auto">General:</h2>

  <ul dir="auto">

  <li>Fixed GLSL version parsing on some OpenGL ES2 platforms.</li>

  <li>The "Aspect ratio correction" option within the Global Options section<br>

  is now active by default.</li>

  <li>There is now a checkbox for the --copy-protection command-line option.</li>

  <li>Reduced memory usage on platforms with dynamic detection plugins.</li>

  <li>Improved GUI usability on small screens.</li>

  <li>Added optional dependency for libopenmpt for sound.</li>

  <li>Added optional dependency for libmpcdec (musepack) for sound.</li>

  </ul>

  <h2 dir="auto">ADL:</h2>

  <ul dir="auto">

  <li>Added Apple II checkerboard cursor as a visual option.</li>

  <li>Removed broken strings in Time Zone.</li>

  <li>Fixed picking up all items via "GET ALL" from a scene.</li>

  <li>Fixed restoring the state of unvisited rooms.</li>

  </ul>

  <h2 dir="auto">AGI:</h2>

  <ul dir="auto">

  <li>Apple II games are now detected. Although not supported yet, most can be started.</li>

  <li>Fixed duration of timed text boxes. They were shown only half as long as<br>

  they should be, making e.g. the King''s Quest III intro hard to read.</li>

  <li>The predictive input dialog popup when clicking on the prompt line or in an
  input field<br>

  is now an optional game setting, disabled by default.</li>

  <li>Fixed Black Cauldron witches not disappearing at end of game.</li>

  <li>Fixed King''s Quest III mice event not occurring after listening to fish.</li>

  <li>Fixed Mixed-Up Mother Goose crash after nursery rhyme on certain platforms.</li>

  <li>Fixed Gold Rush game clock in Apple IIgs version.</li>

  <li>Fixed Donald Duck''s Playground audio bugs in PC booter version.</li>

  <li>Improved detection for PC booter games.</li>

  <li>Added support for sound in CoCo3 games.</li>

  <li>Fixed many bugs in Winnie The Pooh In The Hundred Acre Wood, including<br>

  Tigger never appearing and Eeyore not accepting his balloon.</li>

  </ul>

  <h2 dir="auto">AGOS:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  <li>Fixed timer handling in savegames, addressing issues such as crashing in<br>

  Waxworks Egypt Level 3 and Power Points not regenerating in Elvira 2.</li>

  </ul>

  <h2 dir="auto">AGS:</h2>

  <ul dir="auto">

  <li>Syncronized with upstream AGS 3.6.1.30.</li>

  <li>Added commandline --language option to specify the game language overriding
  the GUI.</li>

  <li>Fixed glitchy staircase in old Maniac Mansion Mania episodes, caused by<br>

  imperfect pathfinding.</li>

  <li>Fixed savescreen not accepting keyboard input in a few games (e.g. An English
  Haunting).</li>

  <li>Fixed colorless texts in games using the SpriteFont plugin (e.g. Detective Gallo).</li>

  <li>Updated .mod playback and fixed looping not working in rare occasions.</li>

  <li>Fixed misbehaving legacy upscaler in old games.</li>

  <li>Fixed rare incorrect tinting when using AVX2 optimizations.</li>

  <li>Added a few checks for unsupported videos to prevent crashes.</li>

  <li>Multiple updates to the detection tables.</li>

  </ul>

  <h2 dir="auto">Asylum:</h2>

  <ul dir="auto">

  <li>Implemented moving with the arrow keys.</li>

  </ul>

  <h2 dir="auto">BBVS:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Bladerunner:</h2>

  <ul dir="auto">

  <li>Fixed a soft-lock case for Izo at Hawker''s Circle.</li>

  <li>The "Designers cut" setting can be set in advance and persist for a new game.</li>

  <li>Improved, reliable application of custom random seeds.</li>

  </ul>

  <h2 dir="auto">Chewy:</h2>

  <ul dir="auto">

  <li>Fixed cyber crown state before Surimy attack.</li>

  <li>Fixed changing hotspot subtexts.</li>

  <li>Fixed keyboard handling in the inventory screen.</li>

  <li>Fixed unlocked cutscenes in cinema screen.</li>

  <li>Fixed music in harbor during the second visit.</li>

  <li>Fixed movement of Chewy''s boat during the boat race.</li>

  <li>Fixed room placement of Nichelle after Kong attack.</li>

  </ul>

  <h2 dir="auto">Cine:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Composer:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Cruise:</h2>

  <ul dir="auto">

  <li>Added support for Russian fan-translation.</li>

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Draci:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Dreamweb:</h2>

  <ul dir="auto">

  <li>Fixed crash when changing scenes, while holding some non-essential game<br>

  items.</li>

  </ul>

  <h2 dir="auto">EFH:</h2>

  <ul dir="auto">

  <li>Fixed various crashes when exiting in the middle of an interaction.</li>

  </ul>

  <h2 dir="auto">Freescape:</h2>

  <ul dir="auto">

  <li>Added support for Atari/Amiga releases of Dark Side.</li>

  <li>Added "authentic graphics" mode.</li>

  <li>Fixed several glitches in the different render modes.</li>

  <li>Improved keymapper support coverage.</li>

  <li>Correctly implement aspect ratio correction following dosbox implementation.</li>

  </ul>

  <h2 dir="auto">GLK/ADVSYS:</h2>

  <ul dir="auto">

  <li>Fixed parsing for input commands.</li>

  </ul>

  <h2 dir="auto">Gob:</h2>

  <ul dir="auto">

  <li>Fixed Blount becoming inactive in the Gob3 brain level.</li>

  <li>Fixed flickering cursor during some videos in Gob3 and Lost in Time.</li>

  </ul>

  <h2 dir="auto">Groovie:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Hopkins:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Hugo:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Hypno:</h2>

  <ul dir="auto">

  <li>Fixed lagging cursor on some platforms.</li>

  </ul>

  <h2 dir="auto">Illusions:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Kyra:</h2>

  <ul dir="auto">

  <li>(EOB) Added a "Faithful AD&amp;D rules" checkbox, to enable improvements and<br>

  fixes to original Eye of the Beholder I and II game code.</li>

  <li>(EOB) Fixed an issue where multi-class characters might gain incorrect HP<br>

  due to round-off errors.</li>

  <li>(EOB) Corrected projectile weapon damage (as per AD&amp;D 2nd Edition rules).</li>

  <li>(EOB) Elves get +1 to hit with swords and bows (according to the official<br>

  game manual).</li>

  <li>Fixed NPCs Ileria (female) and Beohram (paladin) in Eye of the Beholder I.</li>

  <li>(EOB) Fixed a few small bugs.</li>

  </ul>

  <h2 dir="auto">Lure:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">M4:</h2>

  <ul dir="auto">

  <li>Fixed restoring conversation state.</li>

  </ul>

  <h2 dir="auto">MADE:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">MADS:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">MM:</h2>

  <ul dir="auto">

  <li>Added MT32/LAPC-1 support for Xeen engine.</li>

  <li>Fixed Xeen regression which caused some sound effects to stop abruptly.</li>

  <li>Fixed spell SP/gem requirements in MM1 enhanced mode, and actually remove<br>

  spell points &amp; gems when spells are cast.</li>

  </ul>

  <h2 dir="auto">NANCY:</h2>

  <ul dir="auto">

  <li>Fixed a startup crash and some broken puzzles in The Vampire Diaries.</li>

  <li>Fixed a crash when trying to play the Russian versions of early Nancy Drew games.</li>

  </ul>

  <h2 dir="auto">NGI:</h2>

  <ul dir="auto">

  <li>Added support for Lithuanian version of fullpipe.</li>

  </ul>

  <h2 dir="auto">PINK:</h2>

  <ul dir="auto">

  <li>Fixed crash after the girl turns into a mermaid.</li>

  </ul>

  <h2 dir="auto">SAGA:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  <li>Prevent reaching an unwinnable state when not performing key actions in<br>

  Nimdok''s chapter in IHNM.</li>

  </ul>

  <h2 dir="auto">SCI:</h2>

  <ul dir="auto">

  <li>Added CGA (4 colors and black/white) and Hercules render modes for most<br>

  SCI 0 DOS games. Also added an EGA dithering mode and a VGA gray scale<br>

  mode for many SCI 1 DOS games, a 16 colors mode for KQ6 Windows and<br>

  8 colors modes for all PC-98 games.</li>

  <li>Added Gabriel Knight 1 CD speech repair by AllTinker.<br>

  Fixes the majority of pops and clicks in the DPCM8 speech audio.</li>

  <li>Improved PCjr audio.</li>

  <li>Improved KQ6 CD settings. The DOS platform now defaults to DOS behavior.</li>

  <li>Better support for Mac KQ6.</li>

  <li>Implemented KQ5 FM Towns save/restore UI.</li>

  <li>Numerous script fixes to different games.</li>

  <li>Fixed SCI1.1 picture scaling inaccuracies.</li>

  <li>Fixed fallback detection for unknown fan games.</li>

  <li>Added support for Spanish SQ3.</li>

  <li>Added support for Russian Camelot, Laura Bow, PQ2.</li>

  <li>Added support for Russian fan-translation of QFG3.</li>

  </ul>

  <h2 dir="auto">SCUMM:</h2>

  <ul dir="auto">

  <li>Added map generator from Moonbase Console for Moonbase Commander.</li>

  <li>Improved graphics support for Macintosh MI1, MI2 and Fate of Atlantis.</li>

  <li>Improved audio support for Macintosh Loom, Last Crusade, and MI1.</li>

  </ul>

  <h2 dir="auto">Sherlock:</h2>

  <ul dir="auto">

  <li>Added support for Russian translation of Rose Tattoo.</li>

  </ul>

  <h2 dir="auto">Stark:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Sword1:</h2>

  <ul dir="auto">

  <li>Added a "Windows audio engine" mode available within the ScummVM game<br>

  options, in which we simulate the DirectSound audio drivers powering the<br>

  Windows 95 executable.<br>

  This makes the game use softer (logarithmic) audio curves, but removes<br>

  fade-in and fade-out for sound effects, fade-in for music, and automatic<br>

  music volume attenuation for when speech is playing. By default the setting<br>

  is off, since the game was developed with DOS and AIL sound drivers in mind,<br>

  and it is also not available for Macintosh and PSX versions.</li>

  <li>Added keymapper support.</li>

  <li>Improved support on big-endian systems.</li>

  <li>Added more game variants.</li>

  <li>Restored the ability to choose language of subtitles on PC versions.</li>

  </ul>

  <h2 dir="auto">Sword25:</h2>

  <ul dir="auto">

  <li>Fixed looping scene background sounds.</li>

  <li>Fixed actor lighting when walking.</li>

  </ul>

  <h2 dir="auto">Teenagent:</h2>

  <ul dir="auto">

  <li>Added support for Polish floppy version.</li>

  </ul>

  <h2 dir="auto">Tinsel:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Titanic:</h2>

  <ul dir="auto">

  <li>Fixed crash if the word ''that'' was used in a conversation.</li>

  </ul>

  <h2 dir="auto">Tony:</h2>

  <ul dir="auto">

  <li>Fix crash with rapid cursor switching.</li>

  </ul>

  <h2 dir="auto">TsAGE:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  <li>Added support for Russian CD fan-translation for Ringworld.</li>

  <li>Added support for Russian CD fan-translation for Blue Force.</li>

  </ul>

  <h2 dir="auto">Toon:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Touche:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Trecision:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  </ul>

  <h2 dir="auto">Tucker:</h2>

  <ul dir="auto">

  <li>Added keymapper support.</li>

  <li>Fixed being unable to enter the Lower Hall in 2nd Chapter.</li>

  </ul>

  <h2 dir="auto">TwinE:</h2>

  <ul dir="auto">

  <li>Several collision related fixes.</li>

  </ul>

  <h2 dir="auto">Ultima:</h2>

  <ul dir="auto">

  <li>Fix pathfinding not detecting some doors in Ultima VI.</li>

  <li>Alter Ultima VIII default gamepad bindings.</li>

  <li>Improved Ultima VIII keybind player movement.</li>

  <li>Alter Ultima VIII target gump to no longer pause game.</li>

  <li>Alter Ultima VIII minimap to use game palette.</li>

  <li>Fixed Ultima VIII item splitting &amp; merging on game map.</li>

  <li>Fixed Ultima VIII animation, audio, and scene transition issues.</li>

  </ul>

  <h2 dir="auto">Voyeur:</h2>

  <ul dir="auto">

  <li>Added Interplay logo animation.</li>

  </ul>

  <h2 dir="auto">ZVision:</h2>

  <ul dir="auto">

  <li>Improved support of RTL languages.</li>

  </ul>

  <h2 dir="auto">Android port:</h2>

  <ul dir="auto">

  <li>Add support for Android 15.</li>

  <li>Add game shortcuts support on Android home screen either from a long press<br>

  on the ScummVM icon or from the launcher widgets selector.</li>

  <li>Rework the gamepad input mode with an improved UI. Add more virtual buttons.</li>

  <li>Scale UI according to display density.</li>

  <li>Various stability fixes.</li>

  </ul>

  <h2 dir="auto">macOS port:</h2>

  <ul dir="auto">

  <li>Autoupdates now use Sparkle 2.x.</li>

  <li>Changed default savegame path to use the Application Support folder.</li>

  </ul>

  <h2 dir="auto">3DS port:</h2>

  <ul dir="auto">

  <li>Integrated the port-specific options dialog with the main GUI.</li>

  <li>Increased available memory on the Old 3DS.</li>

  <li>Fixed crashes in new 3DS models due to different memory handling.</li>

  </ul>

  <h2 dir="auto">iOS/iPadOS port:</h2>

  <ul dir="auto">

  <li>Add Apple Pencil support.</li>

  <li>Add app icons for “Dark” and “Tinted” modes.</li>

  <li>Various stability fixes.</li>

  </ul>

  <p dir="auto">Full Changelog: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2.8.1...v2.9.0"><tt>v2.8.1...v2.9.0</tt></a></p>'
updated: '2024-12-22T20:40:59Z'
version: v2.9.0
version_title: 'ScummVM 2.9.0: "Close Encounters of the 2.9th Kind"'
website: https://www.scummvm.org
---
ScummVM allows you to play classic graphic point-and-click adventure games, text adventure games, and RPGs, as long as you already have the game data files. ScummVM replaces the executable files shipped with the games, which means you can now play your favorite games on all your favorite devices.

While ScummVM was originally designed to run LucasArts’ SCUMM games, over time support has been added for many other games: see the full list [on our wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Noteworthy titles include Broken Sword, Myst and Blade Runner, although there are countless other hidden gems to explore.