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
stars: 2340
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

  <hr>

  <p dir="auto">Thanks to all contributors, supporters, testers, bug-reporters, and
  fans for helping build yet another great release!</p>

  <hr>

  <h2 dir="auto">Merged pull requests since our previous release</h2>

  <ul dir="auto">

  <li>HELP: Added explanation what ScummVM is and where to get help for Android and
  iOS by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/sev-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sev-">@sev-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2054943478"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5553"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5553/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5553">#5553</a></li>

  <li>GOB: Added language to bargon VGA floppy and release dates by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2056410447"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5557"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5557/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5557">#5557</a></li>

  <li>DIRECTOR: Add detection for Gadget: Past as Future Spanish demo by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2042569880"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5527"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5527/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5527">#5527</a></li>

  <li>COMMON: Mark more symbols as const by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2054822634"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5552"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5552/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5552">#5552</a></li>

  <li>M4: Fix English credits and console debug output by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2056355325"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5556"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5556/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5556">#5556</a></li>

  <li>ENGINES: Allow specifying a start position for initGraphicsAny() by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2057785532"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5563"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5563/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5563">#5563</a></li>

  <li>ULTIMA8: Refactor ArchiveFile and derived classes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2038969135"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5521"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5521/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5521">#5521</a></li>

  <li>COMMON: Add API for opening an InstallShield cab archive inside of another archive
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2055813456"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5555"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5555/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5555">#5555</a></li>

  <li>GRAPHICS: Add fast paths for scaleBlit when dstW == srcW by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2057447961"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5561"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5561/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5561">#5561</a></li>

  <li>GOB: add missing filesizes &amp; use for GOB3 detection entry AD_ENTRY2s by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2057260709"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5560"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5560/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5560">#5560</a></li>

  <li>PEGASUS: Fix detection for the DVD demo by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060310794"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5567"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5567/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5567">#5567</a></li>

  <li>PEGASUS: Use OSystem::setShakePos() for shaking the screen by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060271893"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5566"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5566/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5566">#5566</a></li>

  <li>GOB: Switch GOB2 detection entrys to AD_ENTRY by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060261438"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5565"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5565/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5565">#5565</a></li>

  <li>GOB: Mark all Adi 4 versions as 640x480 resolution by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060341062"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5569"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5569/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5569">#5569</a></li>

  <li>MM: Enable engine by default by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lotharsm/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lotharsm">@lotharsm</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060984988"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5573"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5573/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5573">#5573</a></li>

  <li>NEWS: Typo by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2061055208"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5574"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5574/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5574">#5574</a></li>

  <li>CGE: Make ALT+X trigger quit() only on initial keypress by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2061059533"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5575"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5575/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5575">#5575</a></li>

  <li>GOB: Use playtoonsdemo for Non-interactive demo by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2061651925"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5578"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5578/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5578">#5578</a></li>

  <li>IMAGE: PICT: Added rowbytes checking if there is lack of PixMap headers by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/nevernever69/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/nevernever69">@nevernever69</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060484461"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5571"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5571/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5571">#5571</a></li>

  <li>COMMON: Fix translation of error messages by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060397619"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5570"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5570/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5570">#5570</a></li>

  <li>AGS: Disable game scanner when detection is dynamic by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2061809115"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5580"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5580/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5580">#5580</a></li>

  <li>KINGDOM: Supporting returning back to launcher feature by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2061501759"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5576"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5576/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5576">#5576</a></li>

  <li>GOB: add correct langcode and version number to GOB2 Amiga entry by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2062469718"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5583"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5583/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5583">#5583</a></li>

  <li>GOB: add filesizes and correct langcodes for GOB1/GOB2 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2062776929"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5584"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5584/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5584">#5584</a></li>

  <li>SWORD1: Add detection for SoldOut rerelease by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2063107951"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5585"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5585/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5585">#5585</a></li>

  <li>TOON: Support hebrew fan translation by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2056596560"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5559"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5559/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5559">#5559</a></li>

  <li>GOB: add version numbers and langcodes to GOB games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068531904"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5590"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5590/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5590">#5590</a></li>

  <li>GOB: Mark all Woodruff entries as Windows by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068716201"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5591"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5591/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5591">#5591</a></li>

  <li>GOB: Mark urban game entries as Windows games by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068721967"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5592"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5592/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5592">#5592</a></li>

  <li>ENGINES: Use OSystem::copyRectToScreen() and fillScreen() where possible by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060328501"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5568"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5568/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5568">#5568</a></li>

  <li>GOB: Detection improvements for various entries by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2069058487"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5598"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5598/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5598">#5598</a></li>

  <li>DIRECTOR: Fixes for Team Xtreme by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2022386522"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5488"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5488/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5488">#5488</a></li>

  <li>CGE: Add keymaps to the engine by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/adityam003/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/adityam003">@adityam003</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068447739"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5588"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5588/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5588">#5588</a></li>

  <li>GOB: Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2069140318"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5600"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5600/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5600">#5600</a></li>

  <li>DIRECTOR: Add (preliminary) support for Tivola Spring 1999 demo by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lotharsm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lotharsm">@lotharsm</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2069186565"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5603"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5603/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5603">#5603</a></li>

  <li>DIRECTOR: Fixes for tempo/DV playback by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2069192692"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5604"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5604/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5604">#5604</a></li>

  <li>COMMON: Remove use of symbol PI to avoid clashing with system headers by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2069108341"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5599"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5599/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5599">#5599</a></li>

  <li>DIRECTOR: XOBJ: Update MiscX stub by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Nevon/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Nevon">@Nevon</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2069157253"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5602"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5602/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5602">#5602</a></li>

  <li>COMMON: Remove use of fmin/fmax/fminf/fmaxf by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068825028"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5594"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5594/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5594">#5594</a></li>

  <li>CONFIGURE: Check if fopen64 is available before using it by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068830720"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5596"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5596/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5596">#5596</a></li>

  <li>GUI: Fix garbled browser last path on Windows by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068737869"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5593"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5593/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5593">#5593</a></li>

  <li>GRAPHICS: Use target pragmas instead of compiler flags to prevent ODR problems
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2061827944"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5581"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5581/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5581">#5581</a></li>

  <li>COMMON: Miscellaneous string changes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060869785"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5572"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5572/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5572">#5572</a></li>

  <li>GRAPHICS: Allow specifying separate xdpi and ydpi values in loadTTFFont by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2057617529"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5562"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5562/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5562">#5562</a></li>

  <li>GRAPHICS: Use emmintrin.h for SSE2 intrinsics by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2068825991"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5595"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5595/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5595">#5595</a></li>

  <li>ULTIMA8: Interpret book page breaks correctly by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/wjp/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/wjp">@wjp</a> in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2075345056"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5608"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5608/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5608">#5608</a></li>

  <li>AGS: Detect ATOTK German update by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/doZennn/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/doZennn">@doZennn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2076272527"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5609"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5609/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5609">#5609</a></li>

  <li>ULTIMA8: Fix impact of certain spaces on text centering by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/wjp/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/wjp">@wjp</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2077217849"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5611"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5611/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5611">#5611</a></li>

  <li>DIRECTOR: Fixes for Team Xtreme by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2076902096"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5610"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5610/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5610">#5610</a></li>

  <li>GOB: use correct langcodes for various GOB games by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2079078044"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5612"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5612/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5612">#5612</a></li>

  <li>GOB: Improvements for various Detection entries of GOB games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080154533"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5613"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5613/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5613">#5613</a></li>

  <li>ANDROID: Set a different package name for debug builds by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080406493"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5614"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5614/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5614">#5614</a></li>

  <li>PEGASUS: Use quicktime workaround for movies by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080801494"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5620"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5620/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5620">#5620</a></li>

  <li>DIRECTOR: Fix missing comma breaking some detection paths by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2082710157"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5627"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5627/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5627">#5627</a></li>

  <li>COMMON: Extend Tokenizer classes to allow extraction of delimiters around tokens
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/fracturehill/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fracturehill">@fracturehill</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2060191673"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5564"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5564/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5564">#5564</a></li>

  <li>CGE2: Add Keymaps to the engine by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/adityam003/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/adityam003">@adityam003</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2085536727"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5628"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5628/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5628">#5628</a></li>

  <li>STARK: Fix not loading ssn sounds in Steam version by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2088949453"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5632"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5632/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5632">#5632</a></li>

  <li>GOB: Get game types from game IDs by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/bluegr/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/bluegr">@bluegr</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080927971"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5625"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5625/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5625">#5625</a></li>

  <li>DIRECTOR: Fixes for Cosmology of Kyoto by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080710052"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5619"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5619/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5619">#5619</a></li>

  <li>COMMON: Use hashit, hashit_lower, equalsIgnoreCase on Path string by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080810658"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5621"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5621/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5621">#5621</a></li>

  <li>SCUMM: Add workaround for MI2 glitch when diving to the Mad Monkey by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2086969886"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5629"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5629/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5629">#5629</a></li>

  <li>MIYOO: Add a build script for musl variant of miyoo CFW by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/phcoder/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/phcoder">@phcoder</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2092262648"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5637"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5637/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5637">#5637</a></li>

  <li>BASE: Ensure folder path when file path set in command line by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2072008119"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5605"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5605/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5605">#5605</a></li>

  <li>SCUMM: Fix crash when missing TRS file in Full Throttle by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2090961872"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5635"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5635/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5635">#5635</a></li>

  <li>IOS7 Make "Designed for iPad" great again on Macs with Apple Silicon by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080878603"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5623"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5623/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5623">#5623</a></li>

  <li>SCI: Add cyrillic support for text-based games by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/deadman2000/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/deadman2000">@deadman2000</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080440468"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5616"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5616/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5616">#5616</a></li>

  <li>DIRECTOR: Dump bitmap as PNGs when --dump-scripts is invoked by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/kartiksharmakk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/kartiksharmakk">@kartiksharmakk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2093350253"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5639"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5639/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5639">#5639</a></li>

  <li>ANDROID: Get HiDPI density from Android metrics by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080410662"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5615"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5615/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5615">#5615</a></li>

  <li>GRAPHICS: OPENGL: Don''t try to use GLAD aliasing for shaders by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2088944446"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5631"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5631/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5631">#5631</a></li>

  <li>MIYOOMINI: Enable neon and freetype2 in documented compilation script by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/phcoder/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/phcoder">@phcoder</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2104121265"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5645"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5645/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5645">#5645</a></li>

  <li>HYPNO: Add Hebrew detection entry for CD structure by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BLooperZ/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2106588927"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5646"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5646/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5646">#5646</a></li>

  <li>[asylum] added basque fan translation by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/josuigoa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/josuigoa">@josuigoa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2097989686"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5642"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5642/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5642">#5642</a></li>

  <li>[WIP NOMERGE] DIRECTOR: Fixes for Cosmology of Kyoto by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2096652182"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5640"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5640/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5640">#5640</a></li>

  <li>SCUMM: Fix GCC warnings by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/orgads/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/orgads">@orgads</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2108816087"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5647"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5647/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5647">#5647</a></li>

  <li>DOCS: Update Sphinx to latest version by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080897817"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5624"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5624/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5624">#5624</a></li>

  <li>DIRECTOR: Spaceship Warlock fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2115054377"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5650"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5650/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5650">#5650</a></li>

  <li>M4: Orion burger fix for using kibble in test2 and a general sound unload fix
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2127230980"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5654"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5654/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5654">#5654</a></li>

  <li>ICB: compile fix for GCC 14 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/chkr-private/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/chkr-private">@chkr-private</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2128289677"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5655"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5655/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5655">#5655</a></li>

  <li>DIRECTOR: Add detection for Oscar Wilde''s The Selfish Giant by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2122352870"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5653"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5653/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5653">#5653</a></li>

  <li>DIRECTOR: Add detection for Barbie and her Magical House by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/threefins/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/threefins">@threefins</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2116889474"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5652"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5652/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5652">#5652</a></li>

  <li>SURFACESDL: [RFC] Possible fix for scaler crash (bug #14872) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2102938636"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5644"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5644/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5644">#5644</a></li>

  <li>GUI: Add feature to copy text from console by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Darkhood148/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Darkhood148">@Darkhood148</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2113389324"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5649"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5649/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5649">#5649</a></li>

  <li>OPENDINGUX: remove -ffast-math by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/citral23/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/citral23">@citral23</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2129100537"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5657"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5657/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5657">#5657</a></li>

  <li>DIRECTOR: Manage filmloop composed of other filmloops. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/kartiksharmakk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/kartiksharmakk">@kartiksharmakk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2102220099"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5643"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5643/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5643">#5643</a></li>

  <li>CHAMBER: Remove setjmp/longjmp usage by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/kartiksharmakk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/kartiksharmakk">@kartiksharmakk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2128904967"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5656"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5656/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5656">#5656</a></li>

  <li>ULTIMA: NUVIE: Misc fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/PushmePullyu/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/PushmePullyu">@PushmePullyu</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2131018881"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5659"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5659/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5659">#5659</a></li>

  <li>MM: MT32/LAPC-1 support for Xeen and other fixes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/CkNoSFeRaTU/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/CkNoSFeRaTU">@CkNoSFeRaTU</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2133775498"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5660"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5660/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5660">#5660</a></li>

  <li>AUDIO: Add support for MO3 files using libopenmpt by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/polyesterswing/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/polyesterswing">@polyesterswing</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2048138056"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5546"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5546/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5546">#5546</a></li>

  <li>VOYEUR: Add Interplay logo animation sequence (logo8.exe) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/yuv422/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/yuv422">@yuv422</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2147849699"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5667"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5667/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5667">#5667</a></li>

  <li>AMIGAOS: Fix typo and revert default aspect ratio by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2148771069"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5669"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5669/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5669">#5669</a></li>

  <li>IOS7: Overload key input by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2092250690"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5636"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5636/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5636">#5636</a></li>

  <li>ULTIMA: NUVIE: U6 spellbook fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/PushmePullyu/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/PushmePullyu">@PushmePullyu</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2149921160"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5670"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5670/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5670">#5670</a></li>

  <li>AUDIO: Fix problem where fluidsynth soundfont could not be loaded by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2152479315"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5673"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5673/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5673">#5673</a></li>

  <li>GOB: Switch detection entries from GOB3 &amp; onceupon to AD_ENTRY &amp; add
  english version of Adibou 3 to detection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2080692629"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5618"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5618/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5618">#5618</a></li>

  <li>Emscripten: Screenshot and Logfile support and minor bugfixes &amp; improvements
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/chkuendig/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/chkuendig">@chkuendig</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2067656412"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5587"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5587/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5587">#5587</a></li>

  <li>DISTS: Move engine data defs to dedicated files by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2051457015"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5550"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5550/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5550">#5550</a></li>

  <li>COMMON: Add multiple-value IO functions by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2092366723"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5638"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5638/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5638">#5638</a></li>

  <li>DIRECTOR: Correct for invalid loop bounds in D4 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/threefins/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/threefins">@threefins</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2116889118"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5651"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5651/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5651">#5651</a></li>

  <li>AGI: Fix missing words from our dictionary by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2161390893"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5676"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5676/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5676">#5676</a></li>

  <li>GOB: Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2157462435"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5674"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5674/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5674">#5674</a></li>

  <li>COMMON: move mappedEvents declaration out of for loop by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/spleen1981/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/spleen1981">@spleen1981</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2161394517"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5677"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5677/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5677">#5677</a></li>

  <li>DISTS: Fix numerous problems with resource compilation on Win32 MinGW build
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2164348291"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5681"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5681/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5681">#5681</a></li>

  <li>AGI: Restrict AGIMOUSE feature to AGIMOUSE games by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2164928626"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5684"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5684/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5684">#5684</a></li>

  <li>MACVENTURE: Fix loading filenames with unicode characters by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/polyesterswing/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/polyesterswing">@polyesterswing</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2161974153"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5678"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5678/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5678">#5678</a></li>

  <li>MACGUI: Fill in upper-left and upper-right corners with black by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/polyesterswing/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/polyesterswing">@polyesterswing</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2167354826"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5690"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5690/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5690">#5690</a></li>

  <li>AGI: Fix AGIMOUSE implementation by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2167822407"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5691"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5691/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5691">#5691</a></li>

  <li>TWP: Add Thimbleweed Park engine by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/scemino/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2140065220"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5662"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5662/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5662">#5662</a></li>

  <li>CREATE_ENGINE: use the FrameLimiter class in xyzzy template by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mgerhardy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mgerhardy">@mgerhardy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2165475130"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5687"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5687/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5687">#5687</a></li>

  <li>Add More Non-Portable Functions to Forbidden Header by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/digitall/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/digitall">@digitall</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2165763953"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5688"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5688/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5688">#5688</a></li>

  <li>SCUMM: Attempt to fix Mac menu screen corruption (bug #15006) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2175369773"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5693"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5693/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5693">#5693</a></li>

  <li>GRAPHICS: Define Palette class (version 2) by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2165908131"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5689"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5689/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5689">#5689</a></li>

  <li>GUI: Fix backend options tab by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2141149627"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5663"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5663/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5663">#5663</a></li>

  <li>DIRECTOR: Xtra support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2159057289"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5675"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5675/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5675">#5675</a></li>

  <li>GRAPHICS: Move PaletteManager definition to a separate header by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2180455335"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5698"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5698/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5698">#5698</a></li>

  <li>GRAPHICS MACGUI: Process extra long words by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/hecmar007/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/hecmar007">@hecmar007</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2184010297"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5703"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5703/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5703">#5703</a></li>

  <li>AMIGAOS: clean up compiler flags by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2182198885"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5701"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5701/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5701">#5701</a></li>

  <li>GUI: Use Palette class in image album dialog by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2181582223"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5699"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5699/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5699">#5699</a></li>

  <li>GUI: Implement Window border draggability by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2186809337"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5708"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5708/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5708">#5708</a></li>

  <li>IOS7: Various fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2165311949"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5685"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5685/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5685">#5685</a></li>

  <li>AGI: Review games and add new ones by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/catrplr/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/catrplr">@catrplr</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2184863573"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5705"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5705/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5705">#5705</a></li>

  <li>AMIGAOS: (Janitorial) Subsitute mk defines with compiler defines by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2186118048"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5707"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5707/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5707">#5707</a></li>

  <li>AMIGAOS: Cleanup and free signals via atexit(), 2nd attempt  by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/PushmePullyu/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PushmePullyu">@PushmePullyu</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2179724935"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5696"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5696/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5696">#5696</a></li>

  <li>GRAPHICS: OPENGL: Upgrade glad headers by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2164771711"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5683"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5683/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5683">#5683</a></li>

  <li>BACKENDS: IMGUI: Use ScummVM facilities to get function pointers by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2190731526"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5715"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5715/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5715">#5715</a></li>

  <li>AMIGAOS: revert compiler flag and more cleanup by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2190890829"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5720"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5720/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5720">#5720</a></li>

  <li>AGS: Fix AmigaOS crash on exit (#15015) by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/PushmePullyu/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/PushmePullyu">@PushmePullyu</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2190356351"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5713"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5713/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5713">#5713</a></li>

  <li>AGS: Don''t use FSNode but rely on AGS facilities to load sound files by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2190744325"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5716"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5716/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5716">#5716</a></li>

  <li>GRAPHICS: Switch ManagedSurface to use Palette class by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2185219404"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5706"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5706/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5706">#5706</a></li>

  <li>AUDIO: Fix integer sign extension issue in RJP1 envelope scaling by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/segrax/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/segrax">@segrax</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2198824821"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5722"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5722/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5722">#5722</a></li>

  <li>AGI: Implement motion/cycler overwrite behavior by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2195578995"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5721"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5721/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5721">#5721</a></li>

  <li>CREATE_PROJECT: Move resource embeds from MSVC to general project by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/orgads/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/orgads">@orgads</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2190218850"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5712"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5712/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5712">#5712</a></li>

  <li>MTROPOLIS: Add support for MTI Russian version by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/tag2015/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tag2015">@tag2015</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2203829327"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5725"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5725/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5725">#5725</a></li>

  <li>MACVENTURE: Fix loading of MacBinary files by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/polyesterswing/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/polyesterswing">@polyesterswing</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2205527873"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5728"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5728/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5728">#5728</a></li>

  <li>DIRECTOR: fix "stage should not be draggable" by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/s-m33r/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/s-m33r">@s-m33r</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2206627968"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5729"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5729/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5729">#5729</a></li>

  <li>GRAPHICS: MACGUI: Implement submenu scrolling by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Krish2882005/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Krish2882005">@Krish2882005</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2210526900"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5730"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5730/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5730">#5730</a></li>

  <li>GUI: Fix selector position after removing a game. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/kunxl-gg/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/kunxl-gg">@kunxl-gg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2212568096"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5731"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5731/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5731">#5731</a></li>

  <li>DIRECTOR: Fixes for The Seven Colors by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2202125006"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5724"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5724/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5724">#5724</a></li>

  <li>MIDI: load CM32L_<em>.ROM or MT32_</em>.ROM as pairs by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/stephengeorgewest/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/stephengeorgewest">@stephengeorgewest</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2179073823"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5695"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5695/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5695">#5695</a></li>

  <li>IMAGE: Remove palette start from image decoder. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2199063020"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5723"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5723/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5723">#5723</a></li>

  <li>IMAGE: Add support for loading Windows ANI and CUR files by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/elasota/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/elasota">@elasota</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2087254634"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5630"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5630/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5630">#5630</a></li>

  <li>GOB: Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2217170969"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5733"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5733/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5733">#5733</a></li>

  <li>GUI: Skip games during Mass Add by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/hecmar007/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/hecmar007">@hecmar007</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2165437337"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5686"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5686/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5686">#5686</a></li>

  <li>TESTBED: Improve video player support on low resolution platforms by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2229882969"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5741"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5741/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5741">#5741</a></li>

  <li>GOB: Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2229807868"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5739"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5739/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5739">#5739</a></li>

  <li>ANDROID: Fixes on on-screen buttons by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2229909740"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5742"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5742/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5742">#5742</a></li>

  <li>DOCS: Add Thimbleweed Park documentation by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/scemino/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2241407126"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5746"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5746/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5746">#5746</a></li>

  <li>MADE: TeraDrive Manhole by @mistydemeo in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2253593872" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5751" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5751/hovercard" href="https://github.com/scummvm/scummvm/pull/5751">#5751</a></li>

  <li>IMAGE: Various optimisations for dithered Cinepak output by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2229334409"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5738"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5738/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5738">#5738</a></li>

  <li>3DS: Improve performance when converting the screen in software by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2235577380"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5745"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5745/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5745">#5745</a></li>

  <li>ACHIEVEMENTS: Allow to override the default achievements platform by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/scemino/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2258629326"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5757"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5757/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5757">#5757</a></li>

  <li>3DS: Rewrite the options dialog to use OptionsContainerWidget by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2235129627"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5744"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5744/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5744">#5744</a></li>

  <li>DEVTOOLS: updated create-achievement scripts by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mgerhardy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mgerhardy">@mgerhardy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2136070595"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5661"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5661/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5661">#5661</a></li>

  <li>DUMPER: Add feature to extract data from ISO9660 and hybrid disk images by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Darkhood148/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Darkhood148">@Darkhood148</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2164123132"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5679"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5679/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5679">#5679</a></li>

  <li>GRAPHICS: NINEPATCH: Change the way remaining_stretch is distributed by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/polyesterswing/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/polyesterswing">@polyesterswing</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2190775914"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5717"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5717/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5717">#5717</a></li>

  <li>DIRECTOR: LINGO: TEST: Adds lingo test for getNthFileNameInFolder [WIP] by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Darkhood148/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Darkhood148">@Darkhood148</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2216857810"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5732"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5732/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5732">#5732</a></li>

  <li>CHAMBERS: Refactor code for HGA compatibility by @yigithanyigit in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2218882684" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5734" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5734/hovercard" href="https://github.com/scummvm/scummvm/pull/5734">#5734</a></li>

  <li>GRAPHICS: Reduce the size of the YUV to RGB tables by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2219265835"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5736"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5736/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5736">#5736</a></li>

  <li>DIRECTOR: Fixes for Hell Cab by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2227862746"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5737"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5737/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5737">#5737</a></li>

  <li>GUI: Keep caret visible in editable widgets while moving it with the keyboard
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2245122671"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5748"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5748/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5748">#5748</a></li>

  <li>DIRECTOR: add various games to detection tables by @meekee7 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2246772701" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5750" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5750/hovercard" href="https://github.com/scummvm/scummvm/pull/5750">#5750</a></li>

  <li>ULTIMA4: Support pixel formats other than RGB565 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2259495863"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5758"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5758/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5758">#5758</a></li>

  <li>COMMON: clear mappedEvents list only if empty by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/spleen1981/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/spleen1981">@spleen1981</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2261282291"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5760"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5760/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5760">#5760</a></li>

  <li>DEVTOOLS: Raise minimum cmake version to 3.13 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/orgads/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/orgads">@orgads</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2261298573"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5761"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5761/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5761">#5761</a></li>

  <li>ULTIMA: NUVIE: Fix loading custom actor tiles (#14960) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/PushmePullyu/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PushmePullyu">@PushmePullyu</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2182292795"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5702"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5702/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5702">#5702</a></li>

  <li>SCUMM: HE: Rewrite the majority of the graphics system by @AndywinXp in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2254692042" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5752" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5752/hovercard" href="https://github.com/scummvm/scummvm/pull/5752">#5752</a></li>

  <li>DISTS: Set StartupWMClass in .desktop file by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/chkr-private/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/chkr-private">@chkr-private</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2264585799"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5763"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5763/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5763">#5763</a></li>

  <li>WIN32: Ensure that _WIN32_WINNT is set high enough for required defines by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2056487994"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5558"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5558/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5558">#5558</a></li>

  <li>IMGUI: Some cleanups by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2267665919"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5766"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5766/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5766">#5766</a></li>

  <li>CI: Fix macosx build by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2273200477"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5769"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5769/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5769">#5769</a></li>

  <li>ANDROID: Remove deprecation warnings by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2255049796"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5754"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5754/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5754">#5754</a></li>

  <li>KYRA: Fix building lol without eob by @tsoliman in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2276865149" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5773" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5773/hovercard" href="https://github.com/scummvm/scummvm/pull/5773">#5773</a></li>

  <li>BACKENDS: Update setImGuiRenderCallback in OSystem by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/scemino/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2276415539"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5771"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5771/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5771">#5771</a></li>

  <li>BACKENDS: Add the ability to load ScummVM fonts in ImGui by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/scemino/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2278230070"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5774"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5774/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5774">#5774</a></li>

  <li>COMMON: Remove deprecated SeekableSubReadStreamEndian class by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2271175500"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5768"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5768/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5768">#5768</a></li>

  <li>GUI: Implement handleMouseUp for Grid layout by @AndywinXp in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2276569224" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5772" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5772/hovercard" href="https://github.com/scummvm/scummvm/pull/5772">#5772</a></li>

  <li>GRAPHICS: Indeo 3 performance and memory improvements by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2219208157"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5735"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5735/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5735">#5735</a></li>

  <li>GOB: Detection Improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2263931776"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5762"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5762/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5762">#5762</a></li>

  <li>SCUMM: Adjust v80 default cursor palette map. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2203896780"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5726"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5726/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5726">#5726</a></li>

  <li>BASE: Enable aspect ratio correction by default (take 2) by @AndywinXp in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2148727957"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5668"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5668/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5668">#5668</a></li>

  <li>GRAPHICS: MACGUI: TTF support in Markdown by @InariInDream in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2130289440" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5658" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5658/hovercard" href="https://github.com/scummvm/scummvm/pull/5658">#5658</a></li>

  <li>AMIGAOS: Enhance stack cookie and set more default .ini values by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2267663838"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5765"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5765/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5765">#5765</a></li>

  <li>Revert "ENGINES: Allow shouldQuit to return true immediately" by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2278910073"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5776"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5776/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5776">#5776</a></li>

  <li>BAGEL: New engine for Space Bar by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sev-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sev-">@sev-</a> in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2260857254"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5759"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5759/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5759">#5759</a></li>

  <li>GRAPHICS: MACGUI: Improve image quality in markdown documents by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2271171748"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5767"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5767/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5767">#5767</a></li>

  <li>AMIGAOS: rename/update install_deps.rexx/amigaos.mk by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2278804350"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5775"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5775/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5775">#5775</a></li>

  <li>GLK: TADS: detection_tables.h updated by @MarcoBorrini99 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2279607610" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5778" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5778/hovercard" href="https://github.com/scummvm/scummvm/pull/5778">#5778</a></li>

  <li>GUI: Move Mass Add list code into MassAddListWidget by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2288911980"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5782"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5782/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5782">#5782</a></li>

  <li>SCUMM HE: Moonbase Commander Map Generation by @LittleToonCat in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2282692814" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5780" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5780/hovercard" href="https://github.com/scummvm/scummvm/pull/5780">#5780</a></li>

  <li>DIRECTOR: Fixes for Virtual Nightclub by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2273924697"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5770"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5770/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5770">#5770</a></li>

  <li>MTROPOLIS: Fix Obsidian Widescreen Hacks by @rparnas in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2254945392" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5753" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5753/hovercard" href="https://github.com/scummvm/scummvm/pull/5753">#5753</a></li>

  <li>BAGEL: Add ''megawave'' and ''microwave'' Console Commands by @sentrywasbored
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2303641194"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5794"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5794/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5794">#5794</a></li>

  <li>JANITORIAL: Typo squashing phase 1 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2294660400"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5787"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5787/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5787">#5787</a></li>

  <li>DIRECTOR: Fixes for Virtual Nightclub by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2294970652"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5788"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5788/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5788">#5788</a></li>

  <li>GOB: Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2303563404"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5793"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5793/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5793">#5793</a></li>

  <li>SCUMM HE: BYB01 competitive online play mods: hit power change by @shkupfer
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2279558403"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5777"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5777/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5777">#5777</a></li>

  <li>SCUMM: (HE) - fix wiz drawing mem leaks by @athrxx in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2290893736" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5783" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5783/hovercard" href="https://github.com/scummvm/scummvm/pull/5783">#5783</a></li>

  <li>GITIGNORE: use uppercase some words by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2304766978"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5799"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5799/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5799">#5799</a></li>

  <li>ZVISION: Fix addDir after 2.9.0 path changes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2304488033"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5796"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5796/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5796">#5796</a></li>

  <li>ZVISION: Add BiDi text support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2304753289"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5798"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5798/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5798">#5798</a></li>

  <li>MTROPOLIS: move assert after nullptr check by @meekee7 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2306682914" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5801" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5801/hovercard" href="https://github.com/scummvm/scummvm/pull/5801">#5801</a></li>

  <li>DIRECTOR: Fixes for Virtual Nightclub by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2310601075"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5807"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5807/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5807">#5807</a></li>

  <li>Various GLK detection tables updates by @MarcoBorrini99 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2308825286" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5804" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5804/hovercard" href="https://github.com/scummvm/scummvm/pull/5804">#5804</a></li>

  <li>GUI: Fix saveload display of selected empty items by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2293823167"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5786"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5786/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5786">#5786</a></li>

  <li>GUI: Save/Load list input improvements by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2298215880"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5789"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5789/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5789">#5789</a></li>

  <li>AGI: Adds updated versions for "Enclosure" and "Voodoo Girl" by @MarcoBorrini99
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2311598448"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5809"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5809/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5809">#5809</a></li>

  <li>COMMON: Add a log watcher by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/scemino/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2313588385"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5810"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5810/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5810">#5810</a></li>

  <li>MTROPOLIS: support loading cue source as string by @meekee7 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2306866348" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5803" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5803/hovercard" href="https://github.com/scummvm/scummvm/pull/5803">#5803</a></li>

  <li>SCUMM: HE: Update Backyard Baseball 2001 competitive mode by @Vissery in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2292612043"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5784"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5784/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5784">#5784</a></li>

  <li>MTROPOLIS: add ability to play external video files by @meekee7 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2306751667" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5802" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5802/hovercard" href="https://github.com/scummvm/scummvm/pull/5802">#5802</a></li>

  <li>DIRECTOR: Make absolute path coherent with path separator by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2316954887"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5816"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5816/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5816">#5816</a></li>

  <li>DIRECTOR: Fixes for Virtual Nightclub by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2316951685"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5815"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5815/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5815">#5815</a></li>

  <li>JANITORIAL: Fix repetitive warnings about template-id in constructor/destructor
  by @peter277 in <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="2316755573" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5814"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5814/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5814">#5814</a></li>

  <li>JANITORIAL: Add Daily Build link to README by @getaaron in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2316550973" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5813" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5813/hovercard" href="https://github.com/scummvm/scummvm/pull/5813">#5813</a></li>

  <li>AGS: Adds 3 new versions for existing entries by @MarcoBorrini99 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2317670616" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5817" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5817/hovercard" href="https://github.com/scummvm/scummvm/pull/5817">#5817</a></li>

  <li>GOB: add German 5.03 variant of Adi 5 to detection by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2319375530"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5818"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5818/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5818">#5818</a></li>

  <li>SCI: Use correct SCI0/SCI1 cursor colors by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2326200590"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5823"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5823/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5823">#5823</a></li>

  <li>DEVTOOLS: replace non printable characters with printable letters by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2326170901"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5822"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5822/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5822">#5822</a></li>

  <li>ANDROID: Allow to start a game directly from the Android launcher and various
  updates by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2304732636"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5797"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5797/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5797">#5797</a></li>

  <li>GRAPHICS: OPENGL: Don''t patch glad.h by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2329083604"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5826"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5826/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5826">#5826</a></li>

  <li>TINYGL: initial implementation of tglPolygonStipple by @neuromancer in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2303882469" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5795" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5795/hovercard" href="https://github.com/scummvm/scummvm/pull/5795">#5795</a></li>

  <li>DIRECTOR: Add detection and support for "Wellen, Wracks und Wassermänner" by
  @codengine in <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="2328835775" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5824"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5824/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5824">#5824</a></li>

  <li>DIRECTOR: Add detection for Jan Lindblad presenterar den sjungande Fågelboken
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2329589342"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5828"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5828/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5828">#5828</a></li>

  <li>DIRECTOR: Fixes for The Apartment and Lingo Workshop by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Krish2882005/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Krish2882005">@Krish2882005</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2330849363"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5830"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5830/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5830">#5830</a></li>

  <li>BAGEL: Remove default values not used in create functions'' definition… by @Strangerke
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2329368845"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5827"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5827/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5827">#5827</a></li>

  <li>DS: Report the buffer size to the mixer by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2333665052"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5831"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5831/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5831">#5831</a></li>

  <li>ULTIMA8: Expand use of Point3 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/OMGPizzaGuy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2339556185"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5836"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5836/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5836">#5836</a></li>

  <li>AGS: Updates Steam "Beer!" &amp; various free titles by @MarcoBorrini99 in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2347079640"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5837"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5837/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5837">#5837</a></li>

  <li>GOB: Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2350928160"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5839"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5839/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5839">#5839</a></li>

  <li>GUI: Improvements for low-resolution devices by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2334525260"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5832"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5832/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5832">#5832</a></li>

  <li>GUI: Fix crash with ExtraGuiOptionsDialog by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2353960698"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5843"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5843/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5843">#5843</a></li>

  <li>MTROPOLIS: detect international Albert/Ernest games by @meekee7 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2246592587" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5749" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5749/hovercard" href="https://github.com/scummvm/scummvm/pull/5749">#5749</a></li>

  <li>DIRECTOR: Fixes for Virtual Nightclub by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2353753438"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5841"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5841/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5841">#5841</a></li>

  <li>BASE: Fix path parsing in command line by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2336402679"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5833"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5833/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5833">#5833</a></li>

  <li>JANITORIAL: Fix typo in SCI script_patches.cpp by @amytant in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2354863505" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5847" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5847/hovercard" href="https://github.com/scummvm/scummvm/pull/5847">#5847</a></li>

  <li>JANITORIAL: Fix LARRRY typo in access martian_resources.cpp by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2354883805"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5848"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5848/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5848">#5848</a></li>

  <li>BASE: silence clang warning by @mistydemeo in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2355160201" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5849" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5849/hovercard" href="https://github.com/scummvm/scummvm/pull/5849">#5849</a></li>

  <li>DIRECTOR: Add detection table entries for a handful of german titles by @codengine
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2339413221"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5835"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5835/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5835">#5835</a></li>

  <li>MACOSX: Fix macOS builds with plugins (as used for OSX PPC releases) by @dwatteau
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2355398284"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5851"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5851/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5851">#5851</a></li>

  <li>COMPOSER: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2349132180"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5838"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5838/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5838">#5838</a></li>

  <li>GRAPHICS: Add simplified blitting routines to ManagedSurface by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2286487336"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5781"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5781/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5781">#5781</a></li>

  <li>COMMON: Avoid including engine headers in common code for DebugChannelDef by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2362138827"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5861"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5861/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5861">#5861</a></li>

  <li>CONFIGURE: Improve libsonivox checks by @dwatteau in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2355403841" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5852" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5852/hovercard" href="https://github.com/scummvm/scummvm/pull/5852">#5852</a></li>

  <li>ULTIMA6: patch nuvie.cfg parsing by extracting text from child by @yudhiwidyatama
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2360355885"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5858"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5858/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5858">#5858</a></li>

  <li>GOB: add bargon variant to detection and split variables command in own section
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2368455828"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5866"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5866/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5866">#5866</a></li>

  <li>ASYLUM: Refactor input code by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2355809725"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5854"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5854/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5854">#5854</a></li>

  <li>WINTERMUTE: add some Rhiannon variants reported to TRAC by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2370736946"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5870"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5870/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5870">#5870</a></li>

  <li>DEVTOOLS: Director by @rvanlaar in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2379039127" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5876"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5876/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5876">#5876</a></li>

  <li>AGOS: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2326028076"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5821"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5821/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5821">#5821</a></li>

  <li>MADE: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2354819726"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5846"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5846/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5846">#5846</a></li>

  <li>SCUMM: Backyard Baseball 2001 Online Mode Game Balance Changes by @Vissery in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2381289254"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5878"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5878/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5878">#5878</a></li>

  <li>STARTREK: Always use enum values for MIDI and sound effects by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2381720706"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5879"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5879/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5879">#5879</a></li>

  <li>NANCY: Add sound to toggles in Game Setup by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2371046618" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5872" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5872/hovercard" href="https://github.com/scummvm/scummvm/pull/5872">#5872</a></li>

  <li>SCI: Add support for CGA and Hercules render modes to SCI 0 games by @athrxx
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2380824108"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5877"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5877/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5877">#5877</a></li>

  <li>AGS: Parser fixes from upstream by @mausimus in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2362195369" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5862" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5862/hovercard" href="https://github.com/scummvm/scummvm/pull/5862">#5862</a></li>

  <li>GOB: Detection improvements for Goblins 1 and 3 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2368737174"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5868"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5868/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5868">#5868</a></li>

  <li>NANCY: Highlight Done button in Game Setup by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2371039056" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5871" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5871/hovercard" href="https://github.com/scummvm/scummvm/pull/5871">#5871</a></li>

  <li>GRAPHICS: Only invalidate the updated area of the screen in ManagedSurface::blitFrom
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2359930550"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5856"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5856/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5856">#5856</a></li>

  <li>Make "Enable copy protection" a GUI option by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2320146452"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5819"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5819/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5819">#5819</a></li>

  <li>ENGINES: Really split detection from engine plugins by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2330320558"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5829"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5829/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5829">#5829</a></li>

  <li>SCI: fix Hercules and CGA b/w transitions and remove unneeded class by @athrxx
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2382328321"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5882"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5882/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5882">#5882</a></li>

  <li>DETECTION: Use uint32 for ADGameFileDescription file size by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2382336360"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5883"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5883/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5883">#5883</a></li>

  <li>GOB: Copy protection flag cleanup by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2382356030"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5884"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5884/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5884">#5884</a></li>

  <li>ALL: QuickTime Enhancements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Krish2882005/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Krish2882005">@Krish2882005</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2378069086"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5874"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5874/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5874">#5874</a></li>

  <li>GUI: Fix crash in edit game dialog when plugins are unloaded by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2382376413"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5885"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5885/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5885">#5885</a></li>

  <li>DGDS: Engine for Dynamix Game Development System games by @mduggan in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2359692991" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5855" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5855/hovercard" href="https://github.com/scummvm/scummvm/pull/5855">#5855</a></li>

  <li>SCI: disable rgb rendering for CGA/Hercules modes by @athrxx in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2382439391" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5886" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5886/hovercard" href="https://github.com/scummvm/scummvm/pull/5886">#5886</a></li>

  <li>GOB: Engine/Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2383836666"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5887"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5887/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5887">#5887</a></li>

  <li>BACKENDS: OPENGL: Support aspect ratio correction for Hercules games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2381743706"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5880"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5880/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5880">#5880</a></li>

  <li>DGDS: add german variants to detection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2384275020"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5888"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5888/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5888">#5888</a></li>

  <li>HUGO: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2367918590"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5865"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5865/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5865">#5865</a></li>

  <li>GOB: Code Improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2384607539"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5889"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5889/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5889">#5889</a></li>

  <li>GRAPHICS: Deprecate ManagedSurface methods that implicitly copy pixel data by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2360426485"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5859"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5859/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5859">#5859</a></li>

  <li>DGDS: add english variants of china by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2384692704"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5890"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5890/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5890">#5890</a></li>

  <li>GRAPHICS: replace deprecated operator by @mistydemeo in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2387410840" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5892" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5892/hovercard" href="https://github.com/scummvm/scummvm/pull/5892">#5892</a></li>

  <li>SAGA: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2362514712"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5863"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5863/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5863">#5863</a></li>

  <li>JANITORIAL: AGI: Fix comment typos by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2387862436"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5893"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5893/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5893">#5893</a></li>

  <li>JANITORIAL: AGOS: Fix comment typos  by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2387874387"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5894"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5894/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5894">#5894</a></li>

  <li>MTROPOLIS: add fallback palette to MovieElement blitting by @meekee7 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2313720483" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5811" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5811/hovercard" href="https://github.com/scummvm/scummvm/pull/5811">#5811</a></li>

  <li>GUI: rebuild if _aspectCheckbox is expected by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2389471180" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5898" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5898/hovercard" href="https://github.com/scummvm/scummvm/pull/5898">#5898</a></li>

  <li>GRAPHICS: Add move constructors to ManagedSurface by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2389587136"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5899"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5899/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5899">#5899</a></li>

  <li>GRAPHICS: Explicitly handle matching formats in ManagedSurface::simpleBlitFrom
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2389593686"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5900"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5900/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5900">#5900</a></li>

  <li>KYRA: LoK - Fix chat duration by @akorotkov in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2389695044" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5901" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5901/hovercard" href="https://github.com/scummvm/scummvm/pull/5901">#5901</a></li>

  <li>ENGINES: Make use of the ADGF_DVD flag by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2393071400"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5903"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5903/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5903">#5903</a></li>

  <li>DETECTION: Use ADGF_NO_FLAGS instead of 0 in detection entries by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2393078675"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5904"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5904/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5904">#5904</a></li>

  <li>DIRECTOR: Fixes for AMBER and Jungle Park by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2393900394"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5907"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5907/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5907">#5907</a></li>

  <li>DIRECTOR: Fix argument order for setting debug channels by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2393476386"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5905"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5905/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5905">#5905</a></li>

  <li>DIRECTOR: Add remaining detection entries for melements by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lotharsm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lotharsm">@lotharsm</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2395479744"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5915"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5915/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5915">#5915</a></li>

  <li>CREATE_PROJECT: Disable ImGui when creating Xcode project by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2396300803"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5918"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5918/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5918">#5918</a></li>

  <li>AGS: Use a namespace alias to keep std namespace as in original code by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2396264814"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5917"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5917/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5917">#5917</a></li>

  <li>SCI: EGA and VGA grey scale support for SCI1 by @athrxx in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2401617777" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5923" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5923/hovercard" href="https://github.com/scummvm/scummvm/pull/5923">#5923</a></li>

  <li>GOB: Small Detection improvements by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2401775748"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5924"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5924/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5924">#5924</a></li>

  <li>STARTREK: Fixes for the demo versions by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2405836319"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5927"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5927/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5927">#5927</a></li>

  <li>GROOVIE: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2386338933"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5891"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5891/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5891">#5891</a></li>

  <li>KYRA: Remove engine dependencies from the Halestorm driver by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2405857674"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5928"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5928/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5928">#5928</a></li>

  <li>TUCKER: Fix bottom exit for UpperCorridor by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2406876335"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5934"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5934/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5934">#5934</a></li>

  <li>GOB: ADI2 Sierra variants fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2406989067"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5935"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5935/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5935">#5935</a></li>

  <li>DGDS: Dump script from debug console by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2407148035"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5937"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5937/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5937">#5937</a></li>

  <li>DIRECTOR: add mac variants of Adibou by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2407428752"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5938"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5938/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5938">#5938</a></li>

  <li>DIRECTOR: Add detection entry for "Robinson Crusoe" by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lotharsm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lotharsm">@lotharsm</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2397918604"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5920"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5920/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5920">#5920</a></li>

  <li>COMMON: Move huffman.h into common/compression/ by @dreammaster in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2394223436" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5913" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5913/hovercard" href="https://github.com/scummvm/scummvm/pull/5913">#5913</a></li>

  <li>MSVC: Add build configuration for ASan by @SupSuper in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2394041818" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5908" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5908/hovercard" href="https://github.com/scummvm/scummvm/pull/5908">#5908</a></li>

  <li>CI: Use Discord RPC lib in Ubuntu runners by @dwatteau in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2404152213" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5926" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5926/hovercard" href="https://github.com/scummvm/scummvm/pull/5926">#5926</a></li>

  <li>DISTS: Update Swedish nuance in desktop file by @anohren in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2394137186" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5911" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5911/hovercard" href="https://github.com/scummvm/scummvm/pull/5911">#5911</a></li>

  <li>DIRECTOR: Add detection for Mysterious Island; add MystIsle xobj by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2394473448"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5914"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5914/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5914">#5914</a></li>

  <li>Introduce I18N comments and better keymapping labels by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/NabeelShabbir/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2396084073"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5916"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5916/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5916">#5916</a></li>

  <li>IOS7: Add iPad app icons to Info.plist by @anohren in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2394208961" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5912" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5912/hovercard" href="https://github.com/scummvm/scummvm/pull/5912">#5912</a></li>

  <li>CRUISE: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2381832197"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5881"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5881/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5881">#5881</a></li>

  <li>AGS: Reduce the amount of size of the detection entries by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2393653499"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5906"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5906/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5906">#5906</a></li>

  <li>JANITORIAL: AGS: Fix a bunch of typos in comments by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2409210846"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5941"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5941/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5941">#5941</a></li>

  <li>GRAPHICS: Fix a transparency issue when using cursor masks with high-color in
  SurfaceSdl by @sdelamarre in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2406375048" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5932"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5932/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5932">#5932</a></li>

  <li>CINE: Add keymapper support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NabeelShabbir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NabeelShabbir">@NabeelShabbir</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2373938591"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5873"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5873/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5873">#5873</a></li>

  <li>COMMON: Use uninitialized_move when resizing arrays by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2391211711"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5902"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5902/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5902">#5902</a></li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2061059533" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5575"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5575/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5575">#5575</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Nevon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Nevon">@Nevon</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2069157253" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5602"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5602/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5602">#5602</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/josuigoa/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/josuigoa">@josuigoa</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2097989686" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5642"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5642/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5642">#5642</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/threefins/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/threefins">@threefins</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2116889474" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5652"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5652/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5652">#5652</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Darkhood148/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Darkhood148">@Darkhood148</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2113389324" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5649"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5649/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5649">#5649</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/CkNoSFeRaTU/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/CkNoSFeRaTU">@CkNoSFeRaTU</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2133775498" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5660"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5660/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5660">#5660</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/scemino/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2140065220" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5662"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5662/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5662">#5662</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/hecmar007/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/hecmar007">@hecmar007</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2184010297" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5703"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5703/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5703">#5703</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/catrplr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/catrplr">@catrplr</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2184863573" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5705"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5705/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5705">#5705</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/s-m33r/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/s-m33r">@s-m33r</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2206627968" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5729"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5729/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5729">#5729</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/stephengeorgewest/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/stephengeorgewest">@stephengeorgewest</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2179073823" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5695"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5695/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5695">#5695</a></li>

  <li>@yigithanyigit made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2218882684" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5734" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5734/hovercard" href="https://github.com/scummvm/scummvm/pull/5734">#5734</a></li>

  <li>@InariInDream made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2130289440" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5658" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5658/hovercard" href="https://github.com/scummvm/scummvm/pull/5658">#5658</a></li>

  <li>@rparnas made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2254945392" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5753" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5753/hovercard" href="https://github.com/scummvm/scummvm/pull/5753">#5753</a></li>

  <li>@sentrywasbored made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2303641194" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5794" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5794/hovercard" href="https://github.com/scummvm/scummvm/pull/5794">#5794</a></li>

  <li>@Vissery made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2292612043" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5784" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5784/hovercard" href="https://github.com/scummvm/scummvm/pull/5784">#5784</a></li>

  <li>@peter277 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2316755573" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5814" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5814/hovercard" href="https://github.com/scummvm/scummvm/pull/5814">#5814</a></li>

  <li>@getaaron made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2316550973" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5813" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5813/hovercard" href="https://github.com/scummvm/scummvm/pull/5813">#5813</a></li>

  <li>@codengine made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2328835775" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5824" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5824/hovercard" href="https://github.com/scummvm/scummvm/pull/5824">#5824</a></li>

  <li>@amytant made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2354863505" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5847" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5847/hovercard" href="https://github.com/scummvm/scummvm/pull/5847">#5847</a></li>

  <li>@akorotkov made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2389695044" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5901" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5901/hovercard" href="https://github.com/scummvm/scummvm/pull/5901">#5901</a></li>

  <li>@anohren made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2394137186" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/5911" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/5911/hovercard" href="https://github.com/scummvm/scummvm/pull/5911">#5911</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2.8.1...v2.9.0"><tt>v2.8.1...v2.9.0</tt></a></p>'
updated: '2024-12-22T20:40:59Z'
version: v2.9.0
version_title: 'ScummVM 2.9.0: "Close Encounters of the 2.9th Kind"'
website: https://www.scummvm.org
---
ScummVM allows you to play classic graphic point-and-click adventure games, text adventure games, and RPGs, as long as you already have the game data files. ScummVM replaces the executable files shipped with the games, which means you can now play your favorite games on all your favorite devices.

While ScummVM was originally designed to run LucasArts’ SCUMM games, over time support has been added for many other games: see the full list [on our wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Noteworthy titles include Broken Sword, Myst and Blade Runner, although there are countless other hidden gems to explore.