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
    url: https://downloads.scummvm.org/frs/scummvm/2026.4.0/scummvm-2026.4.0-3ds-3dsx.zip
  scummvm-cia.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2026.4.0/scummvm-2026.4.0-3ds-cia.zip
  scummvm-ds.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2026.4.0/scummvm-2026.4.0-ds.zip
eval_downloads: true
github: scummvm/scummvm
icon: https://raw.githubusercontent.com/scummvm/scummvm/master/backends/platform/3ds/app/icon.png
image: https://raw.githubusercontent.com/scummvm/scummvm/master/backends/platform/3ds/app/banner.png
image_length: 17658
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
nightly:
  download_page: https://buildbot.scummvm.org/dailybuilds/master/
  downloads:
    3ds-master-latest.zip:
      url: https://buildbot.scummvm.org/dailybuilds/master/3ds-master-latest.zip
    nds-master-latest.zip:
      url: https://buildbot.scummvm.org/dailybuilds/master/nds-master-latest.zip
source: https://github.com/scummvm/scummvm
stars: 2865
systems:
- 3DS
- DS
title: scummvm
unique_ids:
- '0xFF321'
update_notes: '<p dir="auto">It is hard to believe, but a quarter-century and a couple
  of days ago, the ScummVM Project saw its first public commit by Ludvig Strigeus
  aka ludde.</p>

  <p dir="auto">So many things have changed, and we continue to follow our new release
  cadence. Without further ado, let''s discuss what is coming with the 2026.4.0 release.</p>

  <h2 dir="auto">New games:</h2>

  <ul dir="auto">

  <li>Added support for Mortadelo y Filemón: Una Aventura de Cine Edición Original.</li>

  <li>Added support for Mortadelo y Filemón: Dos vaqueros chapuceros.</li>

  <li>Added support for Mortadelo y Filemón: Terror, Espanto y Pavor.</li>

  <li>Added support for Mortadelo y Filemón: La Sexta Secta.</li>

  <li>Added support for Mortadelo y Filemón: Operación Moscú.</li>

  <li>Added support for Mortadelo y Filemón: El Escarabajo de Cleopatra.</li>

  <li>Added support for Mortadelo y Filemón: La Banda de Corvino.</li>

  <li>Added support for Mortadelo y Filemón: Balones y Patadones.</li>

  <li>Added support for Mortadelo y Filemón: Mamelucos a la Romana.</li>

  <li>Added support for Dracula: Resurrection.</li>

  <li>Added support for Dracula 2: The Last Sanctuary.</li>

  <li>Added support for Amerzone: The Explorer''s Legacy.</li>

  <li>Added support for The Cameron Files: The Secret at Loch Ness.</li>

  <li>Added support for The Messenger / Louvre: The Final Curse.</li>

  <li>Added support for Nancy Drew: The Secret of Shadow Ranch.</li>

  <li>Added support for Nancy Drew: Curse of Blackmoor Manor.</li>

  <li>Added support for Nancy Drew: Secret of the Old Clock.</li>

  <li>Added support for Nancy Drew: Last Train to Blue Moon Canyon.</li>

  <li>Added support for Nancy Drew: Danger by Design.</li>

  <li>Added support for Nancy Drew: The Creature of Kapu Cave.</li>

  <li>Added support for Chamber of the Sci-Mutant Priestess.</li>

  <li>Added support for Star Wars: Rebel Assault.</li>

  <li>Added support for Star Wars: Rebel Assault II: The Hidden Empire.</li>

  <li>Added support for Dragonsphere.</li>

  <li>Added support for Return of the Phantom.</li>

  <li>Added support for Once Upon a Forest.</li>

  <li>Added support for Alpha Polaris.</li>

  <li>Added support for Art of Murder: FBI Confidential.</li>

  <li>Added support for Barrow Hill - The Dark Path.</li>

  <li>Added support for Dark Fall: Lost Souls.</li>

  <li>Added support for Devil In The Capital.</li>

  <li>Added support for Dirty Split.</li>

  <li>Added support for Face Noir.</li>

  <li>Added support for Ghost in the Sheet.</li>

  <li>Added support for Hamlet.</li>

  <li>Added support for The Lost Crown - A Ghost-Hunting Adventure.</li>

  <li>Added support for Murder In Tehran''s Alleys 2016.</li>

  <li>Added support for Murder In Tehran''s Alleys 1933.</li>

  <li>Added support for Reversion series.</li>

  <li>Added support for Rhiannon: Curse of the Four Branches.</li>

  <li>Added support for Shadows on the Vatican series.</li>

  <li>Added support for other Wintermute engine games, over 140 titles.</li>

  <li>Added support for Der Schatz im Silbersee (Treasure of the Silver Lake).</li>

  <li>Added support for The Fool''s Errand.</li>

  <li>Added support for Harvester.</li>

  <li>Added support for Lord Avalot d''Argent.</li>

  <li>Added support for Dungeon Master.</li>

  <li>Added support for Eagle Eye Mysteries.</li>

  <li>Added support for Eagle Eye Mysteries in London.</li>

  </ul>

  <h2 dir="auto">General:</h2>

  <ul dir="auto">

  <li>Optimised mixing and rate converters, for better performance.</li>

  <li>Implemented ImGui-based interface for the Event Recorder.</li>

  <li>Fixed bug with inability to specify game overrides for MIDI and MT-32<br>

  devices.</li>

  <li>Switched Nuked-OPL3 AdLib emulator to Nuked-OPL3-fast fork.</li>

  <li>Added support for "obfuscated" InstallShield files. This mainly affected<br>

  certain Nancy Drew games, that can now be run without having to run the<br>

  Windows installer first.</li>

  </ul>

  <h2 dir="auto">Asylum:</h2>

  <ul dir="auto">

  <li>Fixed missing or incorrect walking sounds in some scenes.</li>

  </ul>

  <h2 dir="auto">AWE:</h2>

  <ul dir="auto">

  <li>Fix sound code crash in OpenBSD.</li>

  </ul>

  <h2 dir="auto">Bagel:</h2>

  <ul dir="auto">

  <li>Fix saving options for Hodj n'' Podj''s Th Gesng Gme.</li>

  </ul>

  <h2 dir="auto">GLK:</h2>

  <ul dir="auto">

  <li>Fixed saved font selections not being applied correctly in some games.</li>

  <li>Added support for loading ZX Spectrum games directly from TAP/TZX tape images.</li>

  </ul>

  <h2 dir="auto">Freescape:</h2>

  <ul dir="auto">

  <li>Added support for loading ZX Spectrum games directly from TAP/TZX tape images.</li>

  </ul>

  <h2 dir="auto">Hopkins:</h2>

  <ul dir="auto">

  <li>Added the missing underwater base 3D first-person shooter.</li>

  <li>Optional quality-of-life HUD for underwater base shooter with map and autopilot.</li>

  </ul>

  <h2 dir="auto">Kyra:</h2>

  <ul dir="auto">

  <li>Added support for Korean fan-translation of kyra1 (added in 2026.3.0).</li>

  <li>Restored non-Korean kyra1 games which got broken ("You''re missing the ''KYRA.DAT''<br>

  engine data file or it got corrupted..." message).</li>

  <li>Added an optional automap overlay for Eye of the Beholder 1 and 2.</li>

  </ul>

  <h2 dir="auto">Lure:</h2>

  <ul dir="auto">

  <li>Improved character pathfinding.</li>

  <li>Fix being unable to talk to characters after a one-sided conversation.</li>

  </ul>

  <h2 dir="auto">M4:</h2>

  <ul dir="auto">

  <li>Numerous Riddle of Master Lu fixes for crashes, missing functionality, and game
  bugs.</li>

  <li>Fixed original game bug where conversations with Wolf could freeze the game.</li>

  <li>Added original game cheat codes for bypassing the maze.</li>

  <li>Added translation of message log entries.</li>

  </ul>

  <h2 dir="auto">MM:</h2>

  <ul dir="auto">

  <li>Fix multiple M&amp;M1 classic combat crashes.</li>

  <li>Implement M&amp;M1 classic PC speaker sound.</li>

  <li>Fix stale view close handling causing crash.</li>

  <li>Fix M&amp;M1 spelling mistakes.</li>

  <li>Improved M&amp;M1 Enhanced mouse support, character generation, and general
  in-game UI.</li>

  <li>Fixed cutscene subtitle rendering.</li>

  <li>Added Xeen French translation.</li>

  <li>Fix Pharaoh voice line repeating in Dark Side of Xeen intro.</li>

  </ul>

  <h2 dir="auto">NANCY:</h2>

  <ul dir="auto">

  <li>Generic flags are no longer cleared when saving or auto-saving. Clearing<br>

  them introduced issues when auto-saving was done in some scenes.</li>

  <li>Loading from the GMM is now possible before starting a new scene.</li>

  <li>It''s now possible to skip cutscenes and dialog lines with escape.</li>

  <li>Mouse wheel functionality has been added to several UI widgets.</li>

  <li>Fixed issues with the memory puzzle in Nancy9.</li>

  <li>Fixed issues with the "I can''t" item sound.</li>

  <li>Answers entered in password kind of puzzles are now more forgiving (e.g.<br>

  "Xoc" and "Lady Xoc" are now both acceptable answers).</li>

  </ul>

  <h2 dir="auto">SCUMM:</h2>

  <ul dir="auto">

  <li>Improved cursor scale in early Windows HE games.</li>

  <li>Added option to use PAL timing for SID audio in C64 games. This slows<br>

  down the music, but that''s how many non-US players would have heard it.</li>

  </ul>

  <h2 dir="auto">Sherlock:</h2>

  <ul dir="auto">

  <li>Vertical movement delta fix for Rose Tattoo.</li>

  </ul>

  <h2 dir="auto">SLUDGE:</h2>

  <ul dir="auto">

  <li>Added detection for Shape-Shift Escape.</li>

  </ul>

  <h2 dir="auto">TsAGE:</h2>

  <ul dir="auto">

  <li>Added General MIDI and MT-32 support to the games.</li>

  <li>Improved Sound Blaster sample playback.</li>

  <li>Sound is properly paused when the engine is paused.</li>

  </ul>

  <h2 dir="auto">V-Cruise:</h2>

  <ul dir="auto">

  <li>Fixed time-based puzzles sometimes getting stuck after restarting ScummVM.</li>

  </ul>

  <h2 dir="auto">Voyeur:</h2>

  <ul dir="auto">

  <li>Match original first person movement with mouse when looking at mansion.</li>

  </ul>

  <h2 dir="auto">Android port:</h2>

  <ul dir="auto">

  <li>Support Android 17.</li>

  <li>Add TTS support.</li>

  <li>Add external MIDI device support.</li>

  </ul>

  <h2 dir="auto">Atari port:</h2>

  <ul dir="auto">

  <li>Added integration with nFM library.</li>

  </ul>

  <h1 dir="auto">Merged Pull Requests</h1>

  <ul dir="auto">

  <li>PHOENIXVR: Add Dracula Resurrection variants by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4707789540"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7589"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7589/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7589">#7589</a></li>

  <li>DIRECTOR: Seed RNG from system time instead of a fixed value by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/zberry92/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zberry92">@zberry92</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4701431127"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7584"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7584/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7584">#7584</a></li>

  <li>AUDIO: Optimise mixing and rate converters by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4187183336"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7385"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7385/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7385">#7385</a></li>

  <li>AUDIO : Atari TOS hardware / software OPL2 / 3 (YM262 / YM3812) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/n0kturnal/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/n0kturnal">@n0kturnal</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4213567630"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7405"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7405/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7405">#7405</a></li>

  <li>DM: Fix Crashes and logical bugs  by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4712135801"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7592"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7592/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7592">#7592</a></li>

  <li>GUI: Add ImGui interface for Event Recorder by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/1SHAMAY1/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/1SHAMAY1">@1SHAMAY1</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4589347268"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7555"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7555/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7555">#7555</a></li>

  <li>AUDIO: Change asound_fm.h include by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4695900738"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7583"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7583/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7583">#7583</a></li>

  <li>CHAMBER: Week3 fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4703055234"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7586"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7586/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7586">#7586</a></li>

  <li>GUI: Fix MIDI / MT-32 device selection in Game Options override by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Kartik257354/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Kartik257354">@Kartik257354</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4704967837"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7588"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7588/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7588">#7588</a></li>

  <li>DIRECTOR: work on XTRAs for Terzio &amp; Tivola games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lariaa/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lariaa">@Lariaa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4710746129"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7590"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7590/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7590">#7590</a></li>

  <li>GUI: Fix bitmap rendering with RGB332 overlays by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4712250570"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7593"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7593/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7593">#7593</a></li>

  <li>FREESCAPE: Move the sound code into separate classes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3979039301"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7256"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7256/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7256">#7256</a></li>

  <li>BLADERUNNER: Improve pixel format handling by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4369151698"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7485"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7485/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7485">#7485</a></li>

  <li>SCI: Add detection for the Hebrew fanmade translation of KQ1-SCI&gt; by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4733888097"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7600"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7600/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7600">#7600</a></li>

  <li>SCUMM: Add detection for Indiana Jones and the Quest for Paradise VGA by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4740152821"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7602"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7602/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7602">#7602</a></li>

  <li>AUDIO: Atari TOS hardware / software OPL2 / 3 (YM262 / YM3812) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/n0kturnal/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/n0kturnal">@n0kturnal</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4753350583"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7604"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7604/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7604">#7604</a></li>

  <li>BACKENDS: HAIKU: Add option to build dynamic plugins for Haiku by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Begasus/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Begasus">@Begasus</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4759254867"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7606"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7606/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7606">#7606</a></li>

  <li>NETWORKING/EMSCRIPTEN: Rewrite networking to use timers and add custom timer
  and mixer  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/chkuendig/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/chkuendig">@chkuendig</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3579933933"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7004"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7004/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7004">#7004</a></li>

  <li>DIRECTOR: implement SendSprite/SendAllSprites &amp; quirks for TKKG and Oscar
  games by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lariaa/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lariaa">@Lariaa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4738222430"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7601"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7601/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7601">#7601</a></li>

  <li>DIRECTOR: Add detection entries for Gus Goes to Cyberopolis (Win/Mac) by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4721198058"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7598"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7598/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7598">#7598</a></li>

  <li>DEVTOOLS: COMPANION: Add CCD image conversion support by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/HabibaMahmoud2005/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/HabibaMahmoud2005">@HabibaMahmoud2005</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4771437629"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7609"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7609/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7609">#7609</a></li>

  <li>CHAMBER: Week 4 fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4720165546"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7597"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7597/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7597">#7597</a></li>

  <li>CHAMBER: Add Amiga (EU "Kult") rendering support by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4762474536"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7607"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7607/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7607">#7607</a></li>

  <li>COMMON: Fix incorrect <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/PARAM/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/PARAM">@PARAM</a>
  names in OSystem doc comments by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/eeshsaxena/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/eeshsaxena">@eeshsaxena</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4774174089"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7610"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7610/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7610">#7610</a></li>

  <li>DIRECTOR: Add detection entry for gustown  by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4778537588"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7614"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7614/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7614">#7614</a></li>

  <li>DIRECTOR: DT: Fix script not rendering in script viewer  by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4775896388"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7612"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7612/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7612">#7612</a></li>

  <li>SKY: Port iBASS to ScummVM by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4607402075"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7565"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7565/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7565">#7565</a></li>

  <li>BACKENDS: Allow cursors to be scaled relative to the game screen by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4371724169"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7490"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7490/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7490">#7490</a></li>

  <li>AUDIO: Switch Nuked-OPL3 to Nuked-OPL3-fast fork by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/tgies/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tgies">@tgies</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4567042524"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7543"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7543/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7543">#7543</a></li>

  <li>SLUDGE: Add shape-shift-escape to detection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/polyesterswing/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/polyesterswing">@polyesterswing</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4692623607"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7581"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7581/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7581">#7581</a></li>

  <li>SLUDGE: Replace blendBlitTo with blendBlitFrom and blendFillRect by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4719797931"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7596"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7596/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7596">#7596</a></li>

  <li>AUDIO: Add HMI Infinite Audio DSP library reimplementation by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/AndywinXp/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/AndywinXp">@AndywinXp</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4712062814"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7591"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7591/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7591">#7591</a></li>

  <li>DIRECTOR: Support running with 16bpp pixel formats by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2406273613"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/5930"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/5930/hovercard"
  href="https://github.com/scummvm/scummvm/pull/5930">#5930</a></li>

  <li>DIRECTOR: Fix filmloop shift when swapping cast member with lingo by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4788923610"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7620"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7620/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7620">#7620</a></li>

  <li>ENGINES: resolve various compiler warnings by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4780356911"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7615"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7615/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7615">#7615</a></li>

  <li>BACKENDS: OPENGL: Restore fractional cursor scale by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/tunnelsociety/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4788609519"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7619"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7619/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7619">#7619</a></li>

  <li>DIRECTOR: Make Jewels of the Oracle playable by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/zberry92/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/zberry92">@zberry92</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4804400136"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7626"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7626/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7626">#7626</a></li>

  <li>BACKENDS: ATARI: Build fix by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/n0kturnal/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/n0kturnal">@n0kturnal</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4803918341"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7625"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7625/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7625">#7625</a></li>

  <li>HARVESTER: Address Coverity scan findings by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/alexbevi/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/alexbevi">@alexbevi</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4802053660"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7624"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7624/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7624">#7624</a></li>

  <li>DIRECTOR: Demo detection entries, Tivola&amp; Tivola fixes &amp; CopyProtection
  stub. by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lariaa/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lariaa">@Lariaa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4804697067"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7627"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7627/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7627">#7627</a></li>

  <li>PHOENIXVR: Simplify blitting routines by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4786522172"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7616"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7616/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7616">#7616</a></li>

  <li>SDL: Fix game cursor position at scale factors above 1x by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4809312953"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7628"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7628/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7628">#7628</a></li>

  <li>Support "obfuscated" version of Nancy 10 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4813143730"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7631"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7631/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7631">#7631</a></li>

  <li>Documentation Modification by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Kartik257354/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Kartik257354">@Kartik257354</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4813141160"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7630"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7630/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7630">#7630</a></li>

  <li>DOCS: Fix broken images by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Kartik257354/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Kartik257354">@Kartik257354</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4818095938"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7632"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7632/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7632">#7632</a></li>

  <li>DM: Replace raw thing-data casts with typed struct arrays by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4712287212"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7594"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7594/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7594">#7594</a></li>

  <li>DM: Fixes and support for extended saves by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4832005266"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7637"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7637/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7637">#7637</a></li>

  <li>NANCY: Fix buffer overread in HamRadioPuzzle by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4841374818"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7638"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7638/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7638">#7638</a></li>

  <li>DIRECTOR: Add Opera Fatal Italian Windows detection entry by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4797740466"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7622"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7622/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7622">#7622</a></li>

  <li>MM: XEEN: Fix cutscene subtitle rendering by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/nikaiw/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/nikaiw">@nikaiw</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4828829521"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7635"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7635/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7635">#7635</a></li>

  <li>DIRECTOR: Fixes for true-colour mode by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4851301282"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7639"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7639/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7639">#7639</a></li>

  <li>SKY: Implement text chooser for ibass by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4826179310"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7634"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7634/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7634">#7634</a></li>

  <li>DIRECTOR: D7 loading/parsing fixes (Lscr/Lnam, MCsL, VWCF, sound) + Italian
  Physikus detection by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/M0Rf30/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4797350162"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7621"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7621/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7621">#7621</a></li>

  <li>SKY: Skip check for sky.dnr in iBASS by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4852474371"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7640"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7640/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7640">#7640</a></li>

  <li>DIRECTOR: DT: Fix crashes, stale state and navigation in the debugger by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4857996031"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7646"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7646/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7646">#7646</a></li>

  <li>Bump mistune from 3.2.1 to 3.3.0 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4859341965"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7650"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7650/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7650">#7650</a></li>

  <li>CHEWY: Fix losing active inventory item, bug #16622 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4858259442"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7648"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7648/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7648">#7648</a></li>

  <li>AUDIO: Atari TOS hardware / software OPL2 / 3 (YM262 / YM3812) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/n0kturnal/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/n0kturnal">@n0kturnal</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4801983784"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7623"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7623/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7623">#7623</a></li>

  <li>CHEWY: Fix #16946 (Cannot interact at all after leaving first room) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4861998129"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7651"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7651/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7651">#7651</a></li>

  <li>CHEWY: Rename startSetAILWait -&gt; startDetailWait by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4862894805"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7653"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7653/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7653">#7653</a></li>

  <li>CHEWY: Fix #16948 (non-responsive state in room 05) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4863416657"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7655"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7655/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7655">#7655</a></li>

  <li>HARVESTER: add support for the Harvester demo by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/alexbevi/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/alexbevi">@alexbevi</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4862376871"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7652"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7652/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7652">#7652</a></li>

  <li>CHEWY: Fix left mouse clicks being ignored after a lingering Return key by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4864242780"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7656"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7656/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7656">#7656</a></li>

  <li>CHEWY: Fix non-responsive states in room 07 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4864324154"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7657"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7657/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7657">#7657</a></li>

  <li>ANDROID: Update for Android 17 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4762934328"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7608"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7608/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7608">#7608</a></li>

  <li>LURE: Fix being unable to talk to characters after a one-sided conversation
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4856815369"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7645"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7645/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7645">#7645</a></li>

  <li>SCI: Add detection for the Hebrew fanmade translation of QFG1 EGA Ver… by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4867313813"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7658"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7658/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7658">#7658</a></li>

  <li>ALL: Use override keyword where appropriate by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4863261651"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7654"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7654/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7654">#7654</a></li>

  <li>SCI: Update detection for the Hebrew fanmade translation of QFG1 EGA by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4869051164"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7659"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7659/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7659">#7659</a></li>

  <li>PHOENIXVR: Use RGB565 for DCT VR rendering by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4775208347"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7611"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7611/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7611">#7611</a></li>

  <li>ENGINES: Add hotspot display feature by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/margorski/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/margorski">@margorski</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3796533698"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7135"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7135/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7135">#7135</a></li>

  <li>DIRECTOR: Fix cast member mapping regression from MCsL libResourceId widening
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4875035260"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7663"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7663/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7663">#7663</a></li>

  <li>DIRECTOR: Fix Physicus/Physikus boot blockers (Xtra stubs, CD detection, SIGFPE
  guards) by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4875917783"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7666"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7666/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7666">#7666</a></li>

  <li>VIDEO: Support audio-only AVI files by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4877236619"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7670"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7670/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7670">#7670</a></li>

  <li>CHEWY: Add missing talking animation in room 11 with terminal by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4876940189"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7669"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7669/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7669">#7669</a></li>

  <li>CHEWY: Add 3x missing talking animations in room 12 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4877704190"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7671"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7671/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7671">#7671</a></li>

  <li>SKY: Fix transparency issue in inventory icon in ibass by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Priyanshu3820/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4852881786"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7641"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7641/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7641">#7641</a></li>

  <li>SDL: Work around stale mouse positions on macOS 26 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/rlanday/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/rlanday">@rlanday</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4858642400"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7649"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7649/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7649">#7649</a></li>

  <li>DIRECTOR: Reverse ink on colour bitmaps behaves like BackgndTrans by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lariaa/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lariaa">@Lariaa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4876856915"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7667"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7667/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7667">#7667</a></li>

  <li>DIRECTOR: Asset Xtra cast member registry and prepareFrame dispatch fix by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4876884690"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7668"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7668/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7668">#7668</a></li>

  <li>DIRECTOR: LINGO: Map D5+ objcall bytecodes to cb_call by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4881766987"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7672"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7672/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7672">#7672</a></li>

  <li>COMMON: Add move-assign operator to DisposablePtr by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Helco/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Helco">@Helco</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4885705448"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7673"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7673/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7673">#7673</a></li>

  <li>DIRECTOR: LINGO: Register budapi32 filename for the BuddyAPI Xtra by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4887859145"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7674"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7674/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7674">#7674</a></li>

  <li>DIRECTOR: Use D6 equality table for D7 and D8 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4892360001"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7681"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7681/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7681">#7681</a></li>

  <li>DIRECTOR: Force true color mode for Bioscopia by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4891835863"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7679"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7679/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7679">#7679</a></li>

  <li>DIRECTOR: Read Afterburner-compressed chunks big-endian by default by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4891901567"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7680"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7680/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7680">#7680</a></li>

  <li>SCI: Cleanup LZW view/pic decompressors, others by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4888085850"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7675"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7675/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7675">#7675</a></li>

  <li>DIRECTOR: Add the scale digital-video member property (D7) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4893881356"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7683"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7683/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7683">#7683</a></li>

  <li>DIRECTOR: add director game title to USED IN section by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4893930029"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7684"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7684/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7684">#7684</a></li>

  <li>DIRECTOR: Fix mouseUp dispatching to wrong sprite in D4 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4818706245"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7633"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7633/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7633">#7633</a></li>

  <li>DIRECTOR: LINGO: Add the soundDevice entity (D7) by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4895388386"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7687"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7687/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7687">#7687</a></li>

  <li>DIRECTOR: LINGO: Implement BudAPI baReadIni, baWriteIni and baReadRegString
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4895395679"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7688"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7688/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7688">#7688</a></li>

  <li>DIRECTOR: Fix Opera Fatal intro crash and frozen video sequence by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4895821253"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7689"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7689/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7689">#7689</a></li>

  <li>SDL: Preserve events outside ImGui input capture by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/AndywinXp/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/AndywinXp">@AndywinXp</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4893264521"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7682"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7682/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7682">#7682</a></li>

  <li>DIRECTOR: DT: Call-stack highlighting, Cast window improvements, and paused
  redraw by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4896541599"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7690"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7690/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7690">#7690</a></li>

  <li>DM: Fix Issues flagged by Coverity Scan by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4902708814"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7693"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7693/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7693">#7693</a></li>

  <li>DIRECTOR: Guard film loop accessors against unloaded score by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903633006"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7696"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7696/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7696">#7696</a></li>

  <li>DIRECTOR: Add .CCT to the D6+ movie extension search list by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903636488"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7697"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7697/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7697">#7697</a></li>

  <li>GRAPHICS: Remove glow from hotspot renderer by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/margorski/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/margorski">@margorski</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903442955"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7694"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7694/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7694">#7694</a></li>

  <li>STARK: Fix loading PNGs without an alpha channel by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Victor-Gomez/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Victor-Gomez">@Victor-Gomez</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4871527578"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7662"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7662/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7662">#7662</a></li>

  <li>CHAMBER: Support the Amiga US (Chamber) release in the Amiga renderer by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4809466147"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7629"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7629/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7629">#7629</a></li>

  <li>DEVTOOLS: DIRECTOR: Update xobj stub generator, format with black by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4905590002"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7702"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7702/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7702">#7702</a></li>

  <li>DIRECTOR: Night Light xlibs, few new detection entries by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4905483109"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7701"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7701/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7701">#7701</a></li>

  <li>DIRECTOR: Honor Afterburner Fcdr compression types when reading resources by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903641210"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7698"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7698/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7698">#7698</a></li>

  <li>DIRECTOR: Recognize D7 Cursor Asset Xtra cast members by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903626967"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7695"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7695/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7695">#7695</a></li>

  <li>DIRECTOR: Parse Afterburner Fver imap/director versions and version string by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903644226"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7699"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7699/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7699">#7699</a></li>

  <li>DIRECTOR: Include Xtra symbol and cast id in XtraCastMember stub warnings by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4903648092"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7700"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7700/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7700">#7700</a></li>

  <li>AUDIO: Fix infinite loop in RateConverter on a partial upsample group by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/yasuno45/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/yasuno45">@yasuno45</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4855941126"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7643"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7643/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7643">#7643</a></li>

  <li>MACVENTURE: Initialize titlePadding in borderOffsets by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4933216856"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7722"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7722/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7722">#7722</a></li>

  <li>CHAMBER: Enable engine for release by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4915000234"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7705"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7705/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7705">#7705</a></li>

  <li>FOOL: Create MacWindowManager dynamically instead of statically by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4898858551"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7691"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7691/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7691">#7691</a></li>

  <li>DIRECTOR: Fix film loop D4 and D5+ behavior by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4950642048"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7727"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7727/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7727">#7727</a></li>

  <li>DEVTOOLS: Extract MacVenture Steam disk images from the game .exe by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4950365683"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7726"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7726/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7726">#7726</a></li>

  <li>CHAMBER: Honor the selected CGA/EGA variant when both are in one folder by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4951927378"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7728"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7728/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7728">#7728</a></li>

  <li>MM: XEEN: Add French translation by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/nikaiw/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/nikaiw">@nikaiw</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4943832596"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7725"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7725/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7725">#7725</a></li>

  <li>NANCY: replace static Rect definitions with constexpr equivalents by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4955932087"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7730"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7730/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7730">#7730</a></li>

  <li>CHEWY: Add missing animation for Chewy in room 11 (Bork-Bork dialog) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4958803899"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7732"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7732/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7732">#7732</a></li>

  <li>CHEWY: Add missing talking animations in room 17 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4959020015"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7734"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7734/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7734">#7734</a></li>

  <li>CHEWY: Fix hermit animation in room 14 in dialog with translator by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4958882394"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7733"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7733/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7733">#7733</a></li>

  <li>DIRECTOR: Fix shape cast member data size and byte order when saving by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923665564"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7709"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7709/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7709">#7709</a></li>

  <li>DIRECTOR: Fix crash and size mismatch saving rich text cast members by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923673496"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7711"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7711/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7711">#7711</a></li>

  <li>DIRECTOR: Refuse to save Afterburner movies by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923676906"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7712"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7712/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7712">#7712</a></li>

  <li>DIRECTOR: Preserve the member type when duplicating buttons by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923679019"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7713"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7713/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7713">#7713</a></li>

  <li>DIRECTOR: Don''t mark bitmaps runtime-changed at load time by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923681402"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7714"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7714/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7714">#7714</a></li>

  <li>DIRECTOR: Fix saving members created at runtime by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923684147"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7715"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7715/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7715">#7715</a></li>

  <li>CHEWY: Add missing talking animations in rooms 29 and 37 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4959538014"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7736"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7736/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7736">#7736</a></li>

  <li>CHEWY: Add dialog animation for Howard in room 41 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4960235691"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7737"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7737/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7737">#7737</a></li>

  <li>CHAMBER: resolve global constructor in global array by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4955990826"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7731"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7731/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7731">#7731</a></li>

  <li>DIRECTOR: Yield to the backend during long Lingo repeat loops by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/yasuno45/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/yasuno45">@yasuno45</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4855945780"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7644"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7644/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7644">#7644</a></li>

  <li>DIRECTOR: Fix config chunk size and tag when saving movies by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923661898"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7708"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7708/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7708">#7708</a></li>

  <li>DIRECTOR: Fix buffer overflow writing 8bpp bitmaps with padded pitch by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923669838"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7710"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7710/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7710">#7710</a></li>

  <li>DIRECTOR: LINGO: Dispatch prepareFrame to the frame and movie scripts by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4971848668"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7744"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7744/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7744">#7744</a></li>

  <li>DIRECTOR: Release auto-puppet latches when the score reasserts a sprite by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4972234205"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7745"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7745/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7745">#7745</a></li>

  <li>DIRECTOR: Fixes for Math Heads by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4973965853"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7746"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7746/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7746">#7746</a></li>

  <li>MACVENTURE: Macventure iigs by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4975821348"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7748"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7748/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7748">#7748</a></li>

  <li>DIRECTOR: Gate cast member and child-resource save writers on capability by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4923716319"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7717"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7717/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7717">#7717</a></li>

  <li>LIBRETRO: Guard NULL g_system when changing gui_h_res / aspect by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/apexdesk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/apexdesk">@apexdesk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4969632555"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7741"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7741/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7741">#7741</a></li>

  <li>NANCY: Fix SecondaryMovie overread by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4974421450"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7747"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7747/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7747">#7747</a></li>

  <li>NANCY: Add French font characters by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4978086875"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7750"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7750/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7750">#7750</a></li>

  <li>MM: XEEN: Play pharoh1b.voc only once in the intro by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/nikaiw/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/nikaiw">@nikaiw</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4959140655"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7735"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7735/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7735">#7735</a></li>

  <li>AWE: Fix sfx music crash on OpenBSD (or through TSan) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4912552964"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7703"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7703/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7703">#7703</a></li>

  <li>DOCS: Update Saving and loading a game webpage by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Kartik257354/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Kartik257354">@Kartik257354</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4970121089"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7743"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7743/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7743">#7743</a></li>

  <li>COMMON: Add is_assignable, is_constructible and support move-only SWAPs by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Helco/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Helco">@Helco</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4918514171"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7706"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7706/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7706">#7706</a></li>

  <li>GRAPHICS: Add kTTFRenderModeNormalWithGridFitting by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Helco/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Helco">@Helco</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4975947965"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7749"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7749/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7749">#7749</a></li>

  <li>MADS: NEBULAR: Better support DOS demo startup by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4980952922"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7751"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7751/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7751">#7751</a></li>

  <li>LIBRETRO: Pace audio generation against wall time, not frame count by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/apexdesk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/apexdesk">@apexdesk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4969636085"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7742"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7742/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7742">#7742</a></li>

  <li>CHEWY: Fix station employee animation when Howard is around, room 42 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4987315848"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7753"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7753/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7753">#7753</a></li>

  <li>CHEWY: Add missing Chewy animation in room 40 when train passes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4989429592"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7754"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7754/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7754">#7754</a></li>

  <li>AGDS: Default _fastMode to false so the 25 FPS cap actually applies by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/nikaiw/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/nikaiw">@nikaiw</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4924151189"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7719"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7719/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7719">#7719</a></li>

  <li>SCI: Fix RTL text box clipping by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ZvikaZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ZvikaZ">@ZvikaZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4997078903"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7757"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7757/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7757">#7757</a></li>

  <li>AGDS: Character walking by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/nikaiw/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/nikaiw">@nikaiw</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4954978898"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7729"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7729/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7729">#7729</a></li>

  <li>CHEWY: Add missing animation for Chewy and Howard in room 46 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4999736255"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7758"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7758/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7758">#7758</a></li>

  <li>AGS: Add detection, support for Gobliiins 5 v1.0.5 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4925288683"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7721"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7721/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7721">#7721</a></li>

  <li>DIRECTOR: Fixes for event handling by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5034930150"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7764"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7764/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7764">#7764</a></li>

  <li>DIRECTOR: Some detection fixups and new entry by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/besentv/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/besentv">@besentv</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5032512242"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7763"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7763/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7763">#7763</a></li>

  <li>MACVENTURE: Macventure fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5022924948"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7760"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7760/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7760">#7760</a></li>

  <li>BURIED: Update cursor icon after navigation. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/kmh287/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/kmh287">@kmh287</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5043927566"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7771"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7771/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7771">#7771</a></li>

  <li>CHEWY: Fix Chewy and Howard sprite placement on train by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4990697566"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7755"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7755/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7755">#7755</a></li>

  <li>SCI32: Fix right-to-left alignment of scrolled text lines by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ZvikaZ/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZvikaZ">@ZvikaZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5042943160"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7770"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7770/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7770">#7770</a></li>

  <li>GRAPHIC: Hotspots are being displayed on the left side of the marker if gets
  out of the screen on the right side by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/margorski/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/margorski">@margorski</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5028578506"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7762"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7762/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7762">#7762</a></li>

  <li>CHEWY: Ignore next KEYUP when resuming from overlay by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4875217193"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7664"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7664/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7664">#7664</a></li>

  <li>DIRECTOR: Implement movie cast members as parallel interactive movies by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4986776744"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7752"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7752/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7752">#7752</a></li>

  <li>DIRECTOR: Add another optgraph.dll return value by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/besentv/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/besentv">@besentv</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5049952439"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7772"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7772/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7772">#7772</a></li>

  <li>SCI32: Fix right-to-left text with inline style control codes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ZvikaZ/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZvikaZ">@ZvikaZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5059259474"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7774"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7774/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7774">#7774</a></li>

  <li>CGE2: Fix missing dialogue text for bar crook by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5064257643"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7776"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7776/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7776">#7776</a></li>

  <li>MADS: NEBULAR: Add initial Rex Nebular Macintosh release support by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5063358926"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7775"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7775/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7775">#7775</a></li>

  <li>DIRECTOR: Fix trail-sprite erasure and 0x0 digital-video sizing by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5068537955"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7780"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7780/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7780">#7780</a></li>

  <li>CGE2: Restore missing tailor text by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5065928044"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7778"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7778/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7778">#7778</a></li>

  <li>MAD: NEBULAR: Further Macintosh cleanup &amp; updates by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5071242196"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7782"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7782/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7782">#7782</a></li>

  <li>NANCY: move instead of copy surface by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5078373852"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7785"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7785/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7785">#7785</a></li>

  <li>MACVENTURE: Deja Vu playtesting fixes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5053866582"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7773"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7773/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7773">#7773</a></li>

  <li>DM: Add support for DOS version of Dungeon Master by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5064907847"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7777"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7777/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7777">#7777</a></li>

  <li>DIRECTOR: DT: ImGui debugger improvements by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5068569496"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7781"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7781/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7781">#7781</a></li>

  <li>MACVENTURE: Bug Fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5084407738"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7787"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7787/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7787">#7787</a></li>

  <li>GRAPHICS: MACGUI: Fix invalid rectangle when drawing tall scrolled text by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5075376077"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7784"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7784/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7784">#7784</a></li>

  <li>DIRECTOR: Fixes for Noir - A Shadowy Thriller by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5093017617"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7796"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7796/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7796">#7796</a></li>

  <li>BACKENDS: SDL: Preserve SDL text input for active ImGui text fields by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5067973196"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7779"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7779/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7779">#7779</a></li>

  <li>M4: RIDDLE: Restore the trigger mode in Section9Room::escapePressed() by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5089881801"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7795"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7795/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7795">#7795</a></li>

  <li>M4: Fix the MIDI end trigger firing before the machine table exists by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5089875604"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7794"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7794/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7794">#7794</a></li>

  <li>M4: RIDDLE: Fix crash when crossing Moca Moche tree by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5089864548"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7793"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7793/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7793">#7793</a></li>

  <li>M4: RIDDLE: Fix Wolf conversation freeze by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5088600540"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7792"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7792/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7792">#7792</a></li>

  <li>M4: RIDDLE: Fix interacting with exhibits in room 305 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5088478824"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7791"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7791/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7791">#7791</a></li>

  <li>M4: RIDDLE: Make Marshall Matt show up again by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5088434409"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7790"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7790/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7790">#7790</a></li>

  <li>M4: RIDDLE: Fix Sikkim maze typo and restore cheat by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5088378325"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7789"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7789/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7789">#7789</a></li>

  <li>MADS: NEBULAR: Fix Mac GMM save/load and implement original Mac menus by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5086134621"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7788"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7788/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7788">#7788</a></li>

  <li>MADS: NEBULAR: Fix remaining ISOUND/PC Speaker issues by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5042916228"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7769"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7769/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7769">#7769</a></li>

  <li>COMMON: add missing return statement to non-void function by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5097595793"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7798"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7798/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7798">#7798</a></li>

  <li>GRIM: Correct the calculation for attached joints for MI4 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/oliverkuchies/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/oliverkuchies">@oliverkuchies</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5100717985"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7800"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7800/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7800">#7800</a></li>

  <li>M4: RIDDLE: Fix lost walk trigger when fast-forwarding walks by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5101887534"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7802"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7802/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7802">#7802</a></li>

  <li>M4: RIDDLE: Fix crash when returning from options menu to game menu by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5101878924"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7801"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7801/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7801">#7801</a></li>

  <li>MADS: Add Rex Nebular Bonus Disk support by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5098814120"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7799"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7799/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7799">#7799</a></li>

  <li>BURIED: Fix buggy transition in Chateau Gaillard by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/kmh287/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/kmh287">@kmh287</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5103912533"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7803"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7803/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7803">#7803</a></li>

  <li>SHERLOCK: TATTOO: Fix delta.x sign during vertical walks by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/tslmy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tslmy">@tslmy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5116646055"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7808"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7808/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7808">#7808</a></li>

  <li>HOPKINS: Restore the Windows WBASE underwater base sequence by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5110271147"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7806"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7806/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7806">#7806</a></li>

  <li>M4: RIDDLE: Fix blocker in room 603 when trying to take the pole by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5118182770"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7809"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7809/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7809">#7809</a></li>

  <li>M4: RIDDLE: Fix lockup in 605 when taking disk with Twelvetrees present by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5118230714"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7810"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7810/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7810">#7810</a></li>

  <li>M4: RIDDLE: Fix Twelvetrees'' head turn animation loop in room 605 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5118267713"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7812"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7812/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7812">#7812</a></li>

  <li>ENGINES: use ARRAYSIZE macro where applicable by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5119040301"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7814"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7814/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7814">#7814</a></li>

  <li>MACVENTURE: Sign the diploma and page the console with click to continue by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5114773843"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7807"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7807/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7807">#7807</a></li>

  <li>GLK: ALAN3: use ASIZE macro where applicable by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5119000548"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7813"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7813/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7813">#7813</a></li>

  <li>MADS: Improve or add sound overlays for three games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5126643908"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7817"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7817/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7817">#7817</a></li>

  <li>MADS: NEBULAR: Fix most of Macintosh Rex Nebular  by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5126913254"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7818"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7818/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7818">#7818</a></li>

  <li>ASYLUM: Possible fix for incorrect walk sounds by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4875557755"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7665"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7665/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7665">#7665</a></li>

  <li>WATCHMAKER: make more structs constexpr-capable by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5145785291"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7827"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7827/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7827">#7827</a></li>

  <li>MADS: NEBULAR: Improve original Macintosh functionality by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5144885965"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7826"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7826/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7826">#7826</a></li>

  <li>SHERLOCK: Fix Tattoo scale zone fallback by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/tslmy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tslmy">@tslmy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5144008152"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7824"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7824/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7824">#7824</a></li>

  <li>MACVENTURE: dejavu2 fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5131142399"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7820"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7820/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7820">#7820</a></li>

  <li>M4: RIDDLE: Fix looping sound in room 806 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5154288370"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7831"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7831/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7831">#7831</a></li>

  <li>MADS: NEBULAR: Fix Macintosh text rendering issues by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5151018639"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7829"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7829/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7829">#7829</a></li>

  <li>TSAGE: Add MIDI support and improve Sound Blaster playback by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5150246958"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7828"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7828/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7828">#7828</a></li>

  <li>SKY: Restore partial screen updates by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5159625785"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7836"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7836/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7836">#7836</a></li>

  <li>VOYEUR: Lock the mouse when viewing the mansion as per the original by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/NigeNigeNige/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NigeNigeNige">@NigeNigeNige</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5154611769"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7833"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7833/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7833">#7833</a></li>

  <li>MADE: Unload music data when stopping playback by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/synacktic/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/synacktic">@synacktic</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5183301646"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7846"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7846/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7846">#7846</a></li>

  <li>MADS: NEBULAR: Fix other minor Macintosh issues by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5165992513"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7838"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7838/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7838">#7838</a></li>

  <li>NANCY: Fix chroma-keyed Bink videos not being keyed by @fedossayenko in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5135162906" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7823" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7823/hovercard" href="https://github.com/scummvm/scummvm/pull/7823">#7823</a></li>

  <li>MADE: Report selected synthesiser type by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/synacktic/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/synacktic">@synacktic</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5183301164"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7845"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7845/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7845">#7845</a></li>

  <li>ENGINES: enhancementEnabled should be const by @mgerhardy in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5206050679" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7857" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7857/hovercard" href="https://github.com/scummvm/scummvm/pull/7857">#7857</a></li>

  <li>SLUDGE: self-contained headers by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5201223468"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7856"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7856/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7856">#7856</a></li>

  <li>SCUMM: RA: IO7: Fix virtual controller for Rebel Assault games by @larsamannen
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5192796618"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7852"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7852/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7852">#7852</a></li>

  <li>GOB: add kFeaturesTrueColor to ADI4 variants by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5214291717"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7860"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7860/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7860">#7860</a></li>

  <li>GUI: Prevent use-after-free in <code class="notranslate">_tooltip</code> by
  @greg-kennedy in <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="5224424735" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7863"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7863/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7863">#7863</a></li>

  <li>GOB: add german adi4anglais1213 addon variant to tables by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5225890286"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7864"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7864/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7864">#7864</a></li>

  <li>ANDROID: Add TTS support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5109587077"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7805"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7805/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7805">#7805</a></li>

  <li>DIRECTOR: Fix Lingo point/rect operations and bitmap picture assignment by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5196355202"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7854"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7854/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7854">#7854</a></li>

  <li>DIRECTOR: Share sound channels across the Stage and MIAWs by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5144365837"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7825"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7825/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7825">#7825</a></li>

  <li>AVALANCHE: Bug fixes and Implement missing features by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5165875648"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7837"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7837/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7837">#7837</a></li>

  <li>SKY: Add CgBI decoder and hint system for ibass by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5118251300"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7811"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7811/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7811">#7811</a></li>

  <li>SCUMM: HE: Baseball2001 Hacks Being Removed by @Vissery in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5127438887" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7819" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7819/hovercard" href="https://github.com/scummvm/scummvm/pull/7819">#7819</a></li>

  <li>SKY: Add hotspots in ibass by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5193694008"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7853"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7853/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7853">#7853</a></li>

  <li>SCI: Fix eos() check by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5242302563"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7866"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7866/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7866">#7866</a></li>

  <li>KYRA: EOB: Add an optional automap overlay by @adjioev in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4750812137" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7603" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7603/hovercard" href="https://github.com/scummvm/scummvm/pull/7603">#7603</a></li>

  <li>DIRECTOR: DT: Add a Lingo execution tracer to the visual debugger by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5125354898"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7816"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7816/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7816">#7816</a></li>

  <li>MADS: Fix additional sound problems by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5240227130"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7865"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7865/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7865">#7865</a></li>

  <li>GUI: Fix event recorder build without ImGui by @MerrittFranzmann in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5262693786" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7870" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7870/hovercard" href="https://github.com/scummvm/scummvm/pull/7870">#7870</a></li>

  <li>GOB: mark Addi Simule as stable by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5222326672"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7862"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7862/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7862">#7862</a></li>

  <li>GOB: add german adi4anglais1314 addon to detection by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5266935365"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7872"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7872/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7872">#7872</a></li>

  <li>ULTIMA: Remove shared/std/containers.h by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5302489895"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7890"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7890/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7890">#7890</a></li>

  <li>Bump mistune from 3.3.0 to 3.3.3 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5326650533"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7897"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7897/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7897">#7897</a></li>

  <li>ENGINES: use references instead of copying for loop variables by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5316012862"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7894"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7894/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7894">#7894</a></li>

  <li>KYRA: move HaleStorm sound driver to audio/mac by @greg-kennedy in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5289864210" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7884" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7884/hovercard" href="https://github.com/scummvm/scummvm/pull/7884">#7884</a></li>

  <li>TITANIC: Drop the unreachable second diff &gt;= 0 branch in LiftbotScript by
  @darkdi in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="5309972453" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7891"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7891/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7891">#7891</a></li>

  <li>PHOENIXVR: Add initial support for the Pharaoh''s Curse demo by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5313893074"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7892"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7892/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7892">#7892</a></li>

  <li>PHOENIXVR: Use simpleBlitFrom() for rendering cursors with alpha transparency
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5314138258"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7893"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7893/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7893">#7893</a></li>

  <li>STARK: Save the palette when extracting textures by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5301057592"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7888"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7888/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7888">#7888</a></li>

  <li>STARK: Reduce surface copying when creating viewport screenshots by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5301143602"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7889"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7889/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7889">#7889</a></li>

  <li>LIBRETRO: wii u - replace mwup with <strong>wiiu</strong> by @cscd98 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5348150180" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7898" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7898/hovercard" href="https://github.com/scummvm/scummvm/pull/7898">#7898</a></li>

  <li>GUI: Shadow fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5272870890"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7873"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7873/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7873">#7873</a></li>

  <li>ANDROID: Add MIDI driver support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5247900660"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7869"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7869/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7869">#7869</a></li>

  <li>AGS: Move include for wchar.h before scummsys.h in ALFONT by @antoniou79 in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5360021666"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7899"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7899/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7899">#7899</a></li>

  <li>GOB: Add save files of Adi4/Euro application by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5363745830"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7900"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7900/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7900">#7900</a></li>

  <li>KINGDOM: Play stereo music in stereo mode by @antoniou79 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5222028320" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7861" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7861/hovercard" href="https://github.com/scummvm/scummvm/pull/7861">#7861</a></li>

  <li>MACVENTURE: Macventure release by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5154020467"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7830"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7830/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7830">#7830</a></li>

  <li>MACVENTURE: Promote the Macintosh releases to testing by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5155086332"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7834"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7834/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7834">#7834</a></li>

  <li>COMMON: Fix VS compiler warnings in core by @elasota in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5382062089" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7912" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7912/hovercard" href="https://github.com/scummvm/scummvm/pull/7912">#7912</a></li>

  <li>SURFACESDL: Fix setting the colour key and blend mode with SDL3 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5376971372"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7904"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7904/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7904">#7904</a></li>

  <li>DIRECTOR: Ignore unrelated NET.EXE projectors by @ied206 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5381976834" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7911" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7911/hovercard" href="https://github.com/scummvm/scummvm/pull/7911">#7911</a></li>

  <li>GUI: Fix ScrollContainerWidget and various other simplifications in the GUI
  code by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5293403369"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7886"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7886/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7886">#7886</a></li>

  <li>M4: RIDDLE: fix logic/animation in Room 407 by @vorph999 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5364403511" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7901" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7901/hovercard" href="https://github.com/scummvm/scummvm/pull/7901">#7901</a></li>

  <li>GUI: Don''t restore a widget''s shadow over its neighbour by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mikrosk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5369866731"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7903"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7903/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7903">#7903</a></li>

  <li>TETRAEDGE: Do not string format an awry float for debug print by @antoniou79
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5398620457"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7914"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7914/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7914">#7914</a></li>

  <li>EEM: Fix sign-comparison warnings in mystery.cpp by @uj404 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5404535504" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7917" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7917/hovercard" href="https://github.com/scummvm/scummvm/pull/7917">#7917</a></li>

  <li>FREESCAPE: Fix sign-comparision warnings in Dark Atari by @uj404 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5427696822" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7921" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7921/hovercard" href="https://github.com/scummvm/scummvm/pull/7921">#7921</a></li>

  <li>CHAMBER: Fix format specifier warning in SCR_TRAP by @uj404 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5426991947" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7920" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7920/hovercard" href="https://github.com/scummvm/scummvm/pull/7920">#7920</a></li>

  <li>MADS: PHANTOM: Fix main menu pokeable eyes gag, restore missing content by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5414849786"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7918"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7918/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7918">#7918</a></li>

  <li>WME: GLSL ''int'' precision fix up by @aquadran in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5423127592" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7919" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7919/hovercard" href="https://github.com/scummvm/scummvm/pull/7919">#7919</a></li>

  <li>ALL: use arrow dereferencing operator by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5404364240"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7916"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7916/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7916">#7916</a></li>

  <li>VIDEO: Make loadStream function of video decoders free stream in case of failure
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5432971674"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7935"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7935/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7935">#7935</a></li>

  <li>SCUMM: Match getSaveStateName() to makeSavegameName() by @TRusselo in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5435614165" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7945" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7945/hovercard" href="https://github.com/scummvm/scummvm/pull/7945">#7945</a></li>

  <li>GUI: Enable CJK fonts in RichTextWidget by @ied206 in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5381803091" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7908" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7908/hovercard" href="https://github.com/scummvm/scummvm/pull/7908">#7908</a></li>

  <li>MADE: support games "Richard Scarry''s B* Neighborhood Disc Ever!" by @greg-kennedy
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5199373784"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7855"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7855/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7855">#7855</a></li>

  <li>GUI: Let Ctrl and Alt hotkeys through when a list has focus by @ObjectInSpace
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5210161884"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7858"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7858/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7858">#7858</a></li>

  <li>CI: Add a Github Action to check commit authors by @mduggan in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5460829766" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7949" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7949/hovercard" href="https://github.com/scummvm/scummvm/pull/7949">#7949</a></li>

  <li>ALL: add missing include guards by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5186088631"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7851"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7851/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7851">#7851</a></li>

  <li>CHAMBER: Take the Hercules blit path only for Hercules by @TRusselo in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5435614399" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7946" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7946/hovercard" href="https://github.com/scummvm/scummvm/pull/7946">#7946</a></li>

  <li>SCUMM: Add option for using PAL timing for the C64 music (bug #17201) by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5496038459"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7953"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7953/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7953">#7953</a></li>

  <li>RECORDER: Improve playback timing, modal dialogs, and EOF handling by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/alexbevi/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/alexbevi">@alexbevi</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5510630217"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7955"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7955/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7955">#7955</a></li>

  <li>COMMON: Don''t hang when vsnprintf fails by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5518968802"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7957"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7957/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7957">#7957</a></li>

  <li>MACVENTURE: fix assertion failure when decoding huffman data by @vorph999 in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5528681541"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7958"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7958/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7958">#7958</a></li>

  <li>SCI: Rename "Hoyle School House Math" to "Hoyle School House" by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5509018849"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7954"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7954/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7954">#7954</a></li>

  <li>IOS7: Update touch settings, add wintermute shaders to Xcode project and update
  target versions  by @larsamannen in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5531896020" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7959"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7959/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7959">#7959</a></li>

  <li>DIRECTOR: Fixes for Bananas in Pyjamas by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5587001341"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7960"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7960/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7960">#7960</a></li>

  <li>IMAGE: Refactor CDToons decoder by @ied206 in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5381735588" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7907" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7907/hovercard" href="https://github.com/scummvm/scummvm/pull/7907">#7907</a></li>

  <li>DOCS: Update AI guidelines in light of recent developments by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5604422650"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7962"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7962/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7962">#7962</a></li>

  <li>MOHAWK: Add loop support on tSND playback by @ied206 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5381945584" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7910" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7910/hovercard" href="https://github.com/scummvm/scummvm/pull/7910">#7910</a></li>

  <li>AGOS: 25th anniversary patch for Simon 1 and 2 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/1SHAMAY1/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/1SHAMAY1">@1SHAMAY1</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5105772385"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7804"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7804/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7804">#7804</a></li>

  <li>DIRECTOR: Fixes for film loops by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5680002649"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7965"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7965/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7965">#7965</a></li>

  <li>MADS: FOREST: Fix incorrect flag indices by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5683956670"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7966"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7966/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7966">#7966</a></li>

  <li>Bump urllib3 from 2.7.0 to 2.8.0 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5715556443"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7968"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7968/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7968">#7968</a></li>

  <li>HPL1: Fix default keybinding of glowstick action by @uj404 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5736170676" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7971" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7971/hovercard" href="https://github.com/scummvm/scummvm/pull/7971">#7971</a></li>

  <li>MADS: PHANTOM: Fix MT-32 problems &amp; room 101-&gt;202 crash. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5752735047"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7973"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7973/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7973">#7973</a></li>

  <li>MADS: Fix some unaligned accesses in quote handling code by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5778986700"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7977"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7977/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7977">#7977</a></li>

  <li>HOPKINS: Add QoL enhancements to underwater base FPS segment by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/fusefib/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/fusefib">@fusefib</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5760642884"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7974"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7974/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7974">#7974</a></li>

  <li>DRAGONS: Fix out of bounds crash after actor resourceID change by @AmigaMaster
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5789903470"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7980"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7980/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7980">#7980</a></li>

  </ul>

  <h1 dir="auto">New Contributors</h1>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/n0kturnal/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/n0kturnal">@n0kturnal</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4213567630" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7405"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7405/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7405">#7405</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Kartik257354/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Kartik257354">@Kartik257354</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4704967837" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7588"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7588/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7588">#7588</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/HabibaMahmoud2005/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/HabibaMahmoud2005">@HabibaMahmoud2005</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4771437629" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7609"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7609/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7609">#7609</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/eeshsaxena/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eeshsaxena">@eeshsaxena</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4774174089" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7610"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7610/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7610">#7610</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/tgies/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tgies">@tgies</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4567042524" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7543"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7543/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7543">#7543</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M0Rf30/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M0Rf30">@M0Rf30</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4797740466" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7622"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7622/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7622">#7622</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/nikaiw/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/nikaiw">@nikaiw</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4828829521" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7635"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7635/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7635">#7635</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/maxhgerlach/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/maxhgerlach">@maxhgerlach</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4858259442" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7648"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7648/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7648">#7648</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/margorski/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/margorski">@margorski</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3796533698" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7135"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7135/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7135">#7135</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/rlanday/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/rlanday">@rlanday</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4858642400" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7649"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7649/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7649">#7649</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Victor-Gomez/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Victor-Gomez">@Victor-Gomez</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4871527578" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7662"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7662/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7662">#7662</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/yasuno45/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/yasuno45">@yasuno45</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4855941126" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7643"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7643/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7643">#7643</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/apexdesk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/apexdesk">@apexdesk</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4969632555" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7741"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7741/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7741">#7741</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/kmh287/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/kmh287">@kmh287</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5043927566" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7771"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7771/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7771">#7771</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xtsnoops/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xtsnoops">@xtsnoops</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5089881801" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7795"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7795/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7795">#7795</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/oliverkuchies/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/oliverkuchies">@oliverkuchies</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5100717985" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7800"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7800/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7800">#7800</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/tslmy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tslmy">@tslmy</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5116646055" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7808"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7808/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7808">#7808</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/synacktic/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/synacktic">@synacktic</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5183301646" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7846"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7846/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7846">#7846</a></li>

  <li>@fedossayenko made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5135162906" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7823" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7823/hovercard" href="https://github.com/scummvm/scummvm/pull/7823">#7823</a></li>

  <li>@adjioev made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4750812137" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7603" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7603/hovercard" href="https://github.com/scummvm/scummvm/pull/7603">#7603</a></li>

  <li>@MerrittFranzmann made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5262693786" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7870" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7870/hovercard" href="https://github.com/scummvm/scummvm/pull/7870">#7870</a></li>

  <li>@darkdi made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5309972453" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7891" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7891/hovercard" href="https://github.com/scummvm/scummvm/pull/7891">#7891</a></li>

  <li>@ied206 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5381976834" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7911" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7911/hovercard" href="https://github.com/scummvm/scummvm/pull/7911">#7911</a></li>

  <li>@uj404 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5404535504" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7917" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7917/hovercard" href="https://github.com/scummvm/scummvm/pull/7917">#7917</a></li>

  <li>@TRusselo made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5435614165" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7945" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7945/hovercard" href="https://github.com/scummvm/scummvm/pull/7945">#7945</a></li>

  <li>@ObjectInSpace made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5210161884" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7858" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7858/hovercard" href="https://github.com/scummvm/scummvm/pull/7858">#7858</a></li>

  <li>@AmigaMaster made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5789903470" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7980" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7980/hovercard" href="https://github.com/scummvm/scummvm/pull/7980">#7980</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2026.3.0...v2026.4.0"><tt>v2026.3.0...v2026.4.0</tt></a></p>'
updated: '2026-10-11T18:04:33Z'
version: v2026.4.0
version_title: ScummVM 2026.4.0 "Never-slop"
---
ScummVM allows you to play classic graphic point-and-click adventure games, text adventure games, and RPGs, as long as you already have the game data files. ScummVM replaces the executable files shipped with the games, which means you can now play your favorite games on all your favorite devices.

While ScummVM was originally designed to run LucasArts’ SCUMM games, over time support has been added for many other games: see the full list [on our wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Noteworthy titles include Broken Sword, Myst and Blade Runner, although there are countless other hidden gems to explore.

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>[git] scummvm.3dsx</summary>
<ol>
<li>Download <code>3ds-master-latest.zip</code></li>
<li>Extract <code>/3ds-master-[//]+/scummvm.3dsx</code> from the zip to <code>/3ds/scummvm.3dsx</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[git] scummvm.cia</summary>
<ol>
<li>Download <code>3ds-master-latest.zip</code></li>
<li>Extract <code>/3ds-master-[//]+/scummvm.cia</code> from the zip to <code>/cias/scummvm.cia</code> on your SD card</li>
<li>Insert your SD card back into your 3DS and turn it on</li>
<li>Install and delete <code>/cias/scummvm.cia</code> using FBI or GodMode9</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[git] scummvm.nds</summary>
<ol>
<li>Download <code>nds-master-latest.zip</code></li>
<li>Extract <code>/nds-master-[//]+/scummvm.ds</code> from the zip to <code>/nds-master-[^/]+/scummvm.ds</code> on your SD card</li>
</ol>
</details>

