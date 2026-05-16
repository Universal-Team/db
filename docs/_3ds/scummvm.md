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
    url: https://downloads.scummvm.org/frs/scummvm/2026.2.0/scummvm-2026.2.0-3ds-3dsx.zip
  scummvm-cia.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2026.2.0/scummvm-2026.2.0-3ds-cia.zip
  scummvm-ds.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2026.2.0/scummvm-2026.2.0-ds.zip
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
stars: 2694
systems:
- 3DS
- DS
title: scummvm
unique_ids:
- '0xFF321'
update_notes: '<p dir="auto">Three months have passed since the last release, and
  here we are again, with our new release approach. We are both worried and excited,
  but hope that in the current reality of the absence of pre-release testing, with
  more frequent releases, we will be able to deliver critical fixes faster.</p>

  <p dir="auto">Let''s talk about the release scope. Three months have passed, but
  the amount of new features is <em>very</em> noticeable.</p>

  <h2 dir="auto">Newly Supported Games:</h2>

  <ul dir="auto">

  <li><em>Necronomicon: The Dawning of Darkness</em></li>

  <li><em>Crime Patrol</em></li>

  <li><em>Crime Patrol 2: Drug Wars</em></li>

  <li><em>The Last Bounty Hunter</em></li>

  <li><em>Mad Dog McCree</em></li>

  <li><em>Mad Dog II: The Lost Gold</em></li>

  <li><em>Space Pirates</em></li>

  <li><em>Who Shot Johnny Rock?</em></li>

  </ul>

  <p dir="auto">And - as usual - there are a couple of "one more things"!</p>

  <h1 dir="auto">Changelog</h1>

  <h2 dir="auto">New games:</h2>

  <ul dir="auto">

  <li>Added support for Necronomicon: The Dawning of Darkness.</li>

  <li>Added ALG engine for DOS versions of American Laser Games:<br>

  Crime Patrol, Crime Patrol 2: Drug Wars, The Last Bounty Hunter,<br>

  Mad Dog McCree, Mad Dog II: The Lost Gold, Space Pirates<br>

  and Who Shot Johnny Rock?</li>

  </ul>

  <h2 dir="auto">General:</h2>

  <ul dir="auto">

  <li>Improved PC-Speaker emulation.</li>

  <li>Implemented multiselect in the GUI launcher games list.</li>

  <li>Updated ImGui library to 1.92.6-docker.</li>

  <li>Fixed Smart Search in the Icons Grid view in the launcher.</li>

  <li>Simulate MT-32 display for on-screen messages.</li>

  <li>Added possibility to load GUI translations from the local <code class="notranslate">po/</code>
  directory. Useful for translators since it does not require regeneration of the
  translations.dat file.</li>

  <li>Significantly reduced compilation time and memory usage when building the TinyGL
  component.</li>

  <li>Added Help button to the main interface and improved the dialog speed.</li>

  <li>Added possibility to run unpacked GUI themes.</li>

  </ul>

  <h2 dir="auto">AGOS:</h2>

  <ul dir="auto">

  <li>Added music support for the Atari ST releases of Elvira 1 and 2.</li>

  <li>Improved support of the Acorn releases of Simon the Sorcerer. Original cursor
  is now implemented, along with support of the Desktop Tracker format used for music.</li>

  <li>Improved font rendering accuracy for DOS Personal Nightmare and the Amiga Elvira
  1 demo.</li>

  <li>Implemented original cursors for the Amiga release of Personal Nightmare.</li>

  <li>Fixed Personal Nightmare ''Wait'' command being far too quick on modern systems.</li>

  <li>Fixed inventory icon colors in the Amiga and Atari ST releases of Personal Nightmare.</li>

  <li>Fixed Simon''s sprite having no color in the Acorn floppy demo of Simon the
  Sorcerer 1.</li>

  </ul>

  <h2 dir="auto">Alcachofa:</h2>

  <ul dir="auto">

  <li>Added support for earlier Spanish CD variant of Mortadelo y Filemón: Una Aventura
  de Cine - Edición Especial.</li>

  <li>Added support for Russian variant of Mort &amp; Phil: A Movie Adventure (Секретные
  агенты: Киномонстры атакуют).</li>

  </ul>

  <h2 dir="auto">Bagel:</h2>

  <ul dir="auto">

  <li>Fixed Enter/Escape keys in The Guessing Game guess dialog.</li>

  <li>Fixed using Enter key to close info dialogs.</li>

  <li>Fixed shell animations in Mankala minigame.</li>

  <li>Fixed incorrect evolution logic in Game of Life.</li>

  <li>Hopeful fix for occasional crash entering boardgame stores.</li>

  <li>Fixed crash when hiding boardgame turn start spinner.</li>

  <li>Fixed Poker minigame bet icons rendering over game over dialog.</li>

  <li>Made in-progress speech stop when closing a minigame exit dialog.</li>

  <li>Fixed using Enter key after typing savegame name to save it.</li>

  </ul>

  <h2 dir="auto">Freescape:</h2>

  <ul dir="auto">

  <li>Added sound emulation for Driller, Dark Side, Total Eclipse and<br>

  Castle Master on CPC, C64 and Amiga.</li>

  <li>Added music support for Total Eclipse on Atari ST.</li>

  <li>Added WASD movement option with shift for run.</li>

  <li>Improved touchscreen controls and alternative input mappings for mobile devices.</li>

  <li>Added a debugger with position and area commands.</li>

  <li>Implemented compressed data loading for Driller on Atari ST.</li>

  <li>Fixed rendering artifacts and culling issues.</li>

  <li>Fixed various UI element positions and score rendering across multiple releases.</li>

  </ul>

  <h2 dir="auto">Gob:</h2>

  <ul dir="auto">

  <li>Optimized the number of screen blits, making Gobliiins and Ween noticeably more
  responsive on weaker platforms. Other Gob games are also positively affected.</li>

  </ul>

  <h2 dir="auto">M4:</h2>

  <ul dir="auto">

  <li>Added music support in Ripley.</li>

  <li>Fixed numerous bugs in Ripley.</li>

  <li>Fixed some bugs in Orion Burger.</li>

  </ul>

  <h2 dir="auto">MM:</h2>

  <ul dir="auto">

  <li>Fixed M&amp;M1 memory corruption on exit.</li>

  <li>Fixed M&amp;M1 display issues/corruption getting items from treasure chests.</li>

  <li>Fixed M&amp;M1 showing incorrect name for attacking monsters in combat.</li>

  </ul>

  <h2 dir="auto">MYST3:</h2>

  <ul dir="auto">

  <li>Restored ambient sounds for harmonic frequencies puzzle in Amateria.</li>

  <li>Fixed resetting animations for turntable puzzle in Amateria.</li>

  <li>Fixed synchronization of videos that play consecutively.</li>

  <li>Fixed skipping frames in some looping videos.</li>

  <li>Fixed frame-triggered ambient sounds in scripted movies.</li>

  <li>Various tweaks for displaying subtitles and inventory in widescreen mod.</li>

  <li>Fixed scaling issues for subtitles, draggable items, inventory bar and<br>

  main menu in widescreen mod.</li>

  </ul>

  <h2 dir="auto">QdEngine:</h2>

  <ul dir="auto">

  <li>Fixed pathfinding bugs on Windows optimized (release) build.</li>

  </ul>

  <h2 dir="auto">SCUMM:</h2>

  <ul dir="auto">

  <li>Added support for original splash screens in Maniac Mansion NES (when playing
  from PRG files).</li>

  <li>Added support for the playback feature of the non-interactive demos of Monkey
  Island 1, Monkey Island 2, and Fate of Atlantis.</li>

  <li>Implemented original cursor for the Apple II release of Maniac Mansion.</li>

  <li>Fixed Maniac Mansion NES logo scroll getting stuck during the intro.</li>

  </ul>

  <h2 dir="auto">Sherlock:</h2>

  <ul dir="auto">

  <li>Fixed occasional crash when using inventory items in Rose Tattoo.</li>

  <li>Fixed crash when using keyboard keys while playing darts in Rose Tattoo.</li>

  <li>Fixed score board layout and logic for dart games in Rose Tattoo.</li>

  </ul>

  <h2 dir="auto">SLUDGE:</h2>

  <ul dir="auto">

  <li>Fixed crash at start of Nathan''s Second Chance game.</li>

  </ul>

  <h2 dir="auto">Sword1:</h2>

  <ul dir="auto">

  <li>Fixed music from the original Broken Sword 1 release being played at a wrong
  sample rate on PS3, Wii and OSXPPC.</li>

  </ul>

  <h2 dir="auto">Sword2:</h2>

  <ul dir="auto">

  <li>Fixed crash with some DXA movies, such as the ones played in the intro.</li>

  </ul>

  <h2 dir="auto">Teenagent:</h2>

  <ul dir="auto">

  <li>Fixed ''could not locate language block'' error when starting the Polish and
  Russian versions.</li>

  </ul>

  <h2 dir="auto">Tinsel:</h2>

  <ul dir="auto">

  <li>Implemented proper palette mapping for the PSX versions of Discworld 1. Before
  this, the screen wasn''t turning black when using the blindfold in Act 3.</li>

  <li>Made it possible to skip the entire introduction (by pressing Escape) in all
  Discworld 1 versions.</li>

  <li>Fixed Amazon speech accidentally stopped by the Starfish flicking a coin, in
  Act 2 of all Discworld 1 releases having this original script bug.</li>

  <li>Fixed "calculate odds" button not always erased from the screen when asking
  the guard for probabilities, in Act 3 of early Discworld 1 releases (original script
  bug).</li>

  <li>Fixed crash when trying to interact with (invisible) City Guards in Act 4 of
  Discworld 1, due to an original script oversight in early releases.</li>

  <li>Fixed dragon appearing too early in town square in Act 4 of Discworld 1 (original
  script bug in early releases).</li>

  <li>Fixed conversation window not closing when being done talking with the barman
  in Discworld 1 L-Space (original script bug in early releases).</li>

  </ul>

  <h2 dir="auto">WAGE:</h2>

  <ul dir="auto">

  <li>Implemented combat system.</li>

  <li>Numerous visual fixes.</li>

  <li>Implemented mouse scrolling of text window.</li>

  <li>Implemented way to show startup screen and play startup sound for games what
  have those files. There will be new items in the About menu.</li>

  </ul>

  <h2 dir="auto">Atari port:</h2>

  <ul dir="auto">

  <li>Included out-of-tree m68k code optimizations for the SCUMM engine and audio
  mixing to gather user feedback.</li>

  </ul>

  <h2 dir="auto">macOS port:</h2>

  <ul dir="auto">

  <li>Added support for the newer Text-to-Speech API of macOS 10.14+.</li>

  <li>Restored Help menu and Copy from clipboard features for macOS 10.4-10.5.</li>

  </ul>

  <h2 dir="auto">iOS port:</h2>

  <ul dir="auto">

  <li>Added support for Text-to-Speech.</li>

  <li>Ported the CoreMIDI macOS feature to the iOS/tvOS ports, allowing the use of
  external MIDI devices for output.</li>

  </ul>

  <hr>

  <h2 dir="auto">Merged PRs</h2>

  <ul dir="auto">

  <li>EMI: Show subtitles of judges during Marco''s dive by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/chkr-private/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/chkr-private">@chkr-private</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3572102231"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6994"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6994/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6994">#6994</a></li>

  <li>GRIM: EMI: Don''t enable lighting when drawing shadows by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/chkr-private/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/chkr-private">@chkr-private</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3572729549"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6995"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6995/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6995">#6995</a></li>

  <li>KYRA: (EOB) - Better thrown weapon reloading by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/vrza/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/vrza">@vrza</a> in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3617707762"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7028"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7028/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7028">#7028</a></li>

  <li>SCI: (PQ2/PC98) - fix bug no. 16329 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/athrxx/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/athrxx">@athrxx</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3608797865"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7022"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7022/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7022">#7022</a></li>

  <li>TESTBED: Add shader compatibility tests and remove incompatible shaders from
  Emscripten build by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/chkuendig/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/chkuendig">@chkuendig</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3566592379"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6990"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6990/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6990">#6990</a></li>

  <li>ULTIMA: Reduce sharing of container classes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3597042819"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7014"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7014/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7014">#7014</a></li>

  <li>Add webOS to Makefile and fix engines.awk PATH by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/cscd98/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cscd98">@cscd98</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3608718421"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7021"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7021/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7021">#7021</a></li>

  <li>NUVIE: Remove dependency on Shared::EventsManager by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3597487443"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7016"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7016/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7016">#7016</a></li>

  <li>PRIVATE: Fix drug bag inventory item by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3628729490"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7031"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7031/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7031">#7031</a></li>

  <li>PRIVATE: Play phone calls in correct order by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3628796845"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7032"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7032/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7032">#7032</a></li>

  <li>PRIVATE: Fix Police Station by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3629299851"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7033"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7033/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7033">#7033</a></li>

  <li>HYPNO: Fix various memory leaks by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3628614209"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7030"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7030/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7030">#7030</a></li>

  <li>GRAPHICS: Add generic alpha blitting routines and use them with NGI by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3515837953"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6973"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6973/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6973">#6973</a></li>

  <li>TINYGL: Clamp viewport coordinates to INT_MAX and INT_MIN to avoid overflow/underflow
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/neuromancer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/neuromancer">@neuromancer</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3633226341"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7035"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7035/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7035">#7035</a></li>

  <li>PRIVATE: Wait for police bust audio to complete by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3639915835"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7036"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7036/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7036">#7036</a></li>

  <li>TETRAEDGE: Increase drawCallMemorySize for TinyGl renderer by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3630515335"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7034"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7034/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7034">#7034</a></li>

  <li>PRIVATE: Show cursor for safe digits by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3640214408"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7037"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7037/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7037">#7037</a></li>

  <li>PRIVATE: Fix wall safe initialization, transparency by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3640658086"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7038"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7038/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7038">#7038</a></li>

  <li>PRIVATE: Fix PhoneClip variable decrementing by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3641347757"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7039"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7039/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7039">#7039</a></li>

  <li>IOS7: Do not enable USE_OPENGL_GAME in iOS and tvOS when using create_project  by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3597682271"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7017"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7017/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7017">#7017</a></li>

  <li>TOON: Load subtitles by base file name by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3649459761"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7044"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7044/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7044">#7044</a></li>

  <li>COMMON: Make <code class="notranslate">RBTree::erase</code> return a valid iterator
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Botje/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Botje">@Botje</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3652089484"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7046"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7046/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7046">#7046</a></li>

  <li>PRIVATE: Implement LoseInventory() by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3645461354"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7043"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7043/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7043">#7043</a></li>

  <li>PRIVATE: Implement Take/Leave sounds by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3645099677"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7042"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7042/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7042">#7042</a></li>

  <li>EMI: Don''t overwrite global actor alpha when drawing sprites by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/chkr-private/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/chkr-private">@chkr-private</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3652945888"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7047"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7047/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7047">#7047</a></li>

  <li>GROOVIE: Avoid crash in Clandestiny finale video by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3652952374"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7048"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7048/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7048">#7048</a></li>

  <li>GRIM: Handle SayLine Lua call with nil parameter by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/chkr-private/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/chkr-private">@chkr-private</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655089111"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7050"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7050/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7050">#7050</a></li>

  <li>PRIVATE: Finish implementing PoliceBust and BustMovie by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655124933"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7051"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7051/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7051">#7051</a></li>

  <li>PRIVATE: Fix addMemory crash when helping Mavis by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655308616"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7052"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7052/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7052">#7052</a></li>

  <li>PRIVATE: Clear diary page exits by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655822244"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7056"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7056/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7056">#7056</a></li>

  <li>PRIVATE: Dossier navigation details by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3656471293"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7057"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7057/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7057">#7057</a></li>

  <li>PRIVATE: Add mapping for Japanese Windows cursors by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3656591522"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7058"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7058/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7058">#7058</a></li>

  <li>PRIVATE: New save format, versioning by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3659669746"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7060"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7060/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7060">#7060</a></li>

  <li>NEWS: Update PRIVATE news by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655420451"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7053"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7053/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7053">#7053</a></li>

  <li>PS3: Disable windowed and iconify features by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3657444728"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7059"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7059/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7059">#7059</a></li>

  <li>VIDEO: Don''t hardcode expected channels in PSX decoder by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655636408"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7054"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7054/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7054">#7054</a></li>

  <li>DIRECTOR: Last minute fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3643388725"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7040"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7040/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7040">#7040</a></li>

  <li>JANITORIAL: add pre-commit configuration file by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/whoozle/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/whoozle">@whoozle</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3578571076"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7000"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7000/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7000">#7000</a></li>

  <li>NGI: Fix use-after-free (Trac#16268) by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655775651"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7055"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7055/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7055">#7055</a></li>

  <li>DIRECTOR: add new detection entries for: by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Lariaa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Lariaa">@Lariaa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3484940775"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6962"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6962/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6962">#6962</a></li>

  <li>GRIM: LUA: Fix lua_error() ''noreturn'' warning on some platforms by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3676611767"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7062"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7062/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7062">#7062</a></li>

  <li>PRIVATE: Misc code cleanup by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3678583493"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7066"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7066/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7066">#7066</a></li>

  <li>AGI: Fix RTL display for wrapped strings by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sam-mfb/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sam-mfb">@sam-mfb</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3674393551"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7061"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7061/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7061">#7061</a></li>

  <li>PRIVATE: Update PhoneClip implementation by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3696861101"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7071"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7071/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7071">#7071</a></li>

  <li>GOB: add french ADI5 addon to detection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3701351105"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7074"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7074/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7074">#7074</a></li>

  <li>Bump urllib3 from 2.5.0 to 2.6.0 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3701021479"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7073"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7073/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7073">#7073</a></li>

  <li>COMMON: Add Canadian French language by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sdelamarre/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sdelamarre">@sdelamarre</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3692261115"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7070"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7070/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7070">#7070</a></li>

  <li>STARK: Add support for OpenGL without NPOT by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3677754855"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7064"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7064/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7064">#7064</a></li>

  <li>MM: MM1: Fix crashes when monsters advance during combat by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lili1228/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lili1228">@Lili1228</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3677146363"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7063"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7063/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7063">#7063</a></li>

  <li>AGI: Add game detection entry for SQ2 Hebrew localization by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sam-mfb/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sam-mfb">@sam-mfb</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3702178559"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7076"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7076/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7076">#7076</a></li>

  <li>SCI: Reduce stack usage in Console::cmdShowInstruments() by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3707848828"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7079"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7079/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7079">#7079</a></li>

  <li>PRIVATE: Fully implement AMRadioClip and PoliceClip by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3703948329"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7078"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7078/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7078">#7078</a></li>

  <li>PRIVATE: Fix exit area on epilogue screens by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3711840405"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7080"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7080/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7080">#7080</a></li>

  <li>PRIVATE: Enable pausing when police bust is enabled by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3713013494"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7082"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7082/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7082">#7082</a></li>

  <li>PRIVATE: Resume background music after pausing by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3714119323"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7083"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7083/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7083">#7083</a></li>

  <li>AGI: Detect WORDS.TOK.EXTENDED, Remove GF_EXTCHAR by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3720935557"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7084"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7084/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7084">#7084</a></li>

  <li>AGI: funmade hebrew translation KQ3 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/SegMash/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3726435659"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7086"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7086/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7086">#7086</a></li>

  <li>JANITORIAL: resolve signed/unsigned conflicts by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3692141368"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7069"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7069/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7069">#7069</a></li>

  <li>IOS7: Disable bounces of the ScrollView containing the toolbar by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3735151379"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7089"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7089/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7089">#7089</a></li>

  <li>CREATE_PROJECT: Do not set SCUMMVM_NEON for all iOS/tvOS targets by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3712738457"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7081"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7081/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7081">#7081</a></li>

  <li>PRIVATE: Sound fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3728199893"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7088"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7088/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7088">#7088</a></li>

  <li>JANITORIAL: TOT: resolve signed/unsigned conflicts by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3749834727"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7094"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7094/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7094">#7094</a></li>

  <li>SCI: [RFC] Add Behind the Developer''s Shield as a separate "game" by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3749739432"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7093"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7093/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7093">#7093</a></li>

  <li>HUGO: Fix HUGO2 DOS parser by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3754931211"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7098"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7098/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7098">#7098</a></li>

  <li>HUGO: Fix HUGO2 parrot priority by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3764143981"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7100"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7100/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7100">#7100</a></li>

  <li>GOB: add french Adibou1 CD variant by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3765496689"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7104"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7104/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7104">#7104</a></li>

  <li>SHERLOCK: SCALPEL: Add missing JOY_A mappings for controller support by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/zafos/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zafos">@zafos</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3767121876"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7106"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7106/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7106">#7106</a></li>

  <li>GOB: add filesize version number langcode to GOB games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3772231427"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7109"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7109/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7109">#7109</a></li>

  <li>M4: Add subtitles for Orion Burger and Riddle of Master Lu by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/bluegr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/bluegr">@bluegr</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3740854722"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7090"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7090/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7090">#7090</a></li>

  <li>HUGO: Fix direction handling by retaining keycodes. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3765041988"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7102"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7102/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7102">#7102</a></li>

  <li>SCUMM: Fix HENetworkGameOptionsDialog layout not being defined by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3775013019"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7112"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7112/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7112">#7112</a></li>

  <li>JANITORIAL: Fix "orignal" typo in comment by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3776483329"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7114"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7114/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7114">#7114</a></li>

  <li>JANITORIAL: Fix "cant" typo in comment by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3776485511"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7116"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7116/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7116">#7116</a></li>

  <li>libretro: specify location of engines.awk by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/cscd98/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cscd98">@cscd98</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3703921999"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7077"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7077/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7077">#7077</a></li>

  <li>GRAPHICS: MACGUI: Fix Beam cursor gets stuck after editing editable widget by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SandhuAmy35/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SandhuAmy35">@SandhuAmy35</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3777343501"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7118"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7118/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7118">#7118</a></li>

  <li>JANITORIAL: Fix spelling of ''Writing'' in comments by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/raziel-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3776481858"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7113"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7113/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7113">#7113</a></li>

  <li>JANITORIAL: Fix some mispellings by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/raziel-/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/raziel-">@raziel-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3776488071"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7117"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7117/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7117">#7117</a></li>

  <li>HUGO: Implement DOS displayFrame() by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3768243955"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7108"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7108/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7108">#7108</a></li>

  <li>GRAPHICS: MACGUI: Fix: Adjust scroll position for editable MacText using kConHPadding
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Al-HassanIbrahim/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Al-HassanIbrahim">@Al-HassanIbrahim</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3565881217"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6987"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6987/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6987">#6987</a></li>

  <li>WAGE: Fix Commands menu not resetting on scene change (bug #16294) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Al-HassanIbrahim/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Al-HassanIbrahim">@Al-HassanIbrahim</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3650616651"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7045"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7045/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7045">#7045</a></li>

  <li>GUI: Translate the default OK button in message boxes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3778452911"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7122"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7122/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7122">#7122</a></li>

  <li>JANITORIAL: Small build fixes in graphics and emscripten port by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Mataniko/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Mataniko">@Mataniko</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3778757876"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7124"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7124/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7124">#7124</a></li>

  <li>GUI: Restore Hindi font overrides by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3778585010"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7123"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7123/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7123">#7123</a></li>

  <li>DEVTOOLS: added script that executes event recorder tests for configured demos
  and record files by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mgerhardy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mgerhardy">@mgerhardy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3777353202"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7119"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7119/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7119">#7119</a></li>

  <li>WINTERMUTE: sotv1/sotv2 improvements by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/darioscarpa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/darioscarpa">@darioscarpa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3780045999"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7125"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7125/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7125">#7125</a></li>

  <li>CREATE_PROJECT: add support for SLNX files by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3781177286"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7127"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7127/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7127">#7127</a></li>

  <li>PRIVATE: fix #16423 subtitles are restored. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/dhruv0154/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3765936408"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7105"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7105/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7105">#7105</a></li>

  <li>GUI: Enable multi-selection and multi-removal in list and grid view by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3751490295"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7096"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7096/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7096">#7096</a></li>

  <li>DEVTOOLS: Add LLDB pretty-printers by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Botje/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Botje">@Botje</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3748469788"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7091"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7091/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7091">#7091</a></li>

  <li>GUI: Add missing filter matcher to grid widget by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/jaskaran-singh-77/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/jaskaran-singh-77">@jaskaran-singh-77</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3788975243"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7132"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7132/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7132">#7132</a></li>

  <li>BLADERUNNER: Avoid overflow errors with VQA files by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3778437773"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7121"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7121/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7121">#7121</a></li>

  <li>DIRECTOR: add Greveholm 3 to detection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3780614582"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7126"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7126/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7126">#7126</a></li>

  <li>AGDS: Add detection for the demo version of Black Mirror by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3785678649"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7131"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7131/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7131">#7131</a></li>

  <li>Bump urllib3 from 2.6.0 to 2.6.3 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3791527409"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7133"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7133/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7133">#7133</a></li>

  <li>HUGO: Implement DOS user interface by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3799079641"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7136"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7136/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7136">#7136</a></li>

  <li>DIRECTOR: Fixes for Welcome to the Future by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3795216054"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7134"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7134/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7134">#7134</a></li>

  <li>WINTERMUTE: fix sotv1 package paths by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/darioscarpa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/darioscarpa">@darioscarpa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825020694"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7142"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7142/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7142">#7142</a></li>

  <li>WINTERMUTE: fix subtitles not shown on video by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/darioscarpa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/darioscarpa">@darioscarpa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825071196"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7143"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7143/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7143">#7143</a></li>

  <li>GOB: add new detection entries by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825616121"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7147"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7147/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7147">#7147</a></li>

  <li>GOB: use FR_CAN for French Canadian Adibou2 variant by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825671201"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7148"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7148/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7148">#7148</a></li>

  <li>ULTIMA: NUVIE: rework detection of the known SE Versions by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Henne/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Henne">@Henne</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825973190"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7150"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7150/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7150">#7150</a></li>

  <li>AGI: Add detection for SQ1 Hebrew version by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sam-mfb/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sam-mfb">@sam-mfb</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825371610"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7145"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7145/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7145">#7145</a></li>

  <li>VIDEO: fix TheoraDecoder handling of dup frames by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/darioscarpa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/darioscarpa">@darioscarpa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3825093760"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7144"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7144/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7144">#7144</a></li>

  <li>3DS: Fix versioning scheme by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3826666496"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7151"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7151/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7151">#7151</a></li>

  <li>DC: Fix version scheme by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3826719439"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7152"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7152/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7152">#7152</a></li>

  <li>ULTIMA: NUVIE: detect all versions of MD V1.4 correctly by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Henne/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Henne">@Henne</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3827021391"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7153"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7153/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7153">#7153</a></li>

  <li>GRAPHICS: MACGUI: Fix scrolling behaviors, dialog layouts, and some other bugs.
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/dhruv0154/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3765114476"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7103"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7103/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7103">#7103</a></li>

  <li>CREATE_PROJECT: Cmake multi-config and /opt/homebrew by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Botje/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Botje">@Botje</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3804529962"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7139"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7139/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7139">#7139</a></li>

  <li>AUDIO: Reduce the volume for the PC Speaker emulator by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3831326670"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7155"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7155/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7155">#7155</a></li>

  <li>WAGE: Fixed some bugs in step by step design debugger. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dhruv0154/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3838296016"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7157"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7157/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7157">#7157</a></li>

  <li>Janitorial: Fixed typo ''teh'' in hpl1 comments by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/TejeshwarDivekar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TejeshwarDivekar">@TejeshwarDivekar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3841111111"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7158"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7158/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7158">#7158</a></li>

  <li>BAKCEND: SDL3: Swap language and country in locale formatting by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BeWorld2018/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BeWorld2018">@BeWorld2018</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3842823997"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7160"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7160/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7160">#7160</a></li>

  <li>ANDROID: Updates to the build system and some cleanups by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3827129926"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7154"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7154/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7154">#7154</a></li>

  <li>NDS: Make some parts of ScummVM go to the secondary ROM by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3751114726"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7095"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7095/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7095">#7095</a></li>

  <li>GUI: Restrict max width of scaled pictures in Help by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/gulraiznoorbari/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gulraiznoorbari">@gulraiznoorbari</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3856712663"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7169"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7169/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7169">#7169</a></li>

  <li>BACKENDS: MACOS: Various small fixes/improvements for Tiger/Leopard by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3837654726"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7156"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7156/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7156">#7156</a></li>

  <li>Configure: Update MorphOS part by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BeWorld2018/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BeWorld2018">@BeWorld2018</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3843258926"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7161"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7161/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7161">#7161</a></li>

  <li>SCI32: Remove GK2 fan subtitle suggestion by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3853951096"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7167"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7167/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7167">#7167</a></li>

  <li>GRAPHICS: MACGUI: fix active window while scrolling by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dhruv0154/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3863603524"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7172"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7172/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7172">#7172</a></li>

  <li>SAGA: IHNM: Add detection for french fan translation by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DarkCenobyte/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DarkCenobyte">@DarkCenobyte</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3853799682"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7166"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7166/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7166">#7166</a></li>

  <li>GUI: Multi-Selection and List Widget Improvements by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3852888971"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7165"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7165/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7165">#7165</a></li>

  <li>WINTERMUTE: fix culling in Setup2D by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/darioscarpa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/darioscarpa">@darioscarpa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3879404742"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7179"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7179/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7179">#7179</a></li>

  <li>PRIVATE: Fix subtitle restoration in main menu and prevent SFX interruption
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/dhruv0154/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3816196916"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7140"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7140/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7140">#7140</a></li>

  <li>AGOS: Implement font squeezing routine for DOS Personal Nightmare and the Amiga
  Elvira 1 demo by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3866666618"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7174"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7174/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7174">#7174</a></li>

  <li>WAGE: fix #16293. by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/dhruv0154/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3878509647"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7178"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7178/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7178">#7178</a></li>

  <li>GUI: Properly restore last selected game in launchers by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3881619386"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7181"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7181/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7181">#7181</a></li>

  <li>VIDEO: Fix seeking to a keyframe in BINK videos by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3880443475"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7180"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7180/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7180">#7180</a></li>

  <li>DIRECTOR: Add language to quality table message by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3873420835"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7176"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7176/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7176">#7176</a></li>

  <li>IMAGE: Make more codecs into optional components by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3783188454"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7130"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7130/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7130">#7130</a></li>

  <li>AUDIO: Make the SID emulator a subclass of Audio::Chip by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2459716555"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6039"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6039/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6039">#6039</a></li>

  <li>TTS: MACOS, IOS: Implement Text to Speech using AVSpeechSynthesizer  by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/criezy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/criezy">@criezy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3862730267"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7171"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7171/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7171">#7171</a></li>

  <li>SCI: Adding Hebrew translation for KQ4 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3887659354"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7184"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7184/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7184">#7184</a></li>

  <li>GUI: Lists clear and cls in the gui console debugger''s instructions by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lwcorp/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lwcorp">@lwcorp</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3887615186"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7183"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7183/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7183">#7183</a></li>

  <li>IMAGE: Improve support for writing image files with palettes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3783115426"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7129"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7129/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7129">#7129</a></li>

  <li>JANITORIAL: SCUMM: HE: do not cast away constness by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3897745914"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7188"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7188/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7188">#7188</a></li>

  <li>JANITORIAL: AGS: add missing override keyword by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3897853313"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7189"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7189/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7189">#7189</a></li>

  <li>JANITORIAL: ULTIMA: make some constants constexpr by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3898264287"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7192"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7192/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7192">#7192</a></li>

  <li>JANITORIAL: LAB: remove redundant parentheses by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3898885626"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7193"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7193/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7193">#7193</a></li>

  <li>JANITORIAL: ALCACHOFA: add missing overrides by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3898256554"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7191"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7191/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7191">#7191</a></li>

  <li>FREESCAPE: Implement missing Driller sounds for ZX Spectrum and Amstrad CPC
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/neuromancer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/neuromancer">@neuromancer</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3677775111"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7065"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7065/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7065">#7065</a></li>

  <li>JANITORIAL: WAGE: resolve signed/unsigned mismatches by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3897423784"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7187"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7187/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7187">#7187</a></li>

  <li>PRINCE: Do not show subtiles if they are disabled from GUI by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3902965329"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7194"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7194/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7194">#7194</a></li>

  <li>JANITORIAL: DEVTOOLS: remove unused loop variables by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3909830847"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7199"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7199/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7199">#7199</a></li>

  <li>NEVERHOOD: Fix radio music playing when radio is not enabled by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Player701/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Player701">@Player701</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3907272609"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7197"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7197/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7197">#7197</a></li>

  <li>ALCACHOFA: fix "conatins" typo in graphics.cpp by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3910202462"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7202"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7202/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7202">#7202</a></li>

  <li>ULTIMA: Replace Std::string, Std::vector and Std::list with common equivalents
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3908505049"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7198"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7198/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7198">#7198</a></li>

  <li>SHERLOCK: TATTOO: Fix bug <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3596822771" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7012"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7012/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7012">#7012</a> volume controls for
  MIDI music by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Miguel-Herrero/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Miguel-Herrero">@Miguel-Herrero</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3801198614"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7138"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7138/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7138">#7138</a></li>

  <li>3DS: Use official button names from 3DS manual by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3904173945"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7195"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7195/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7195">#7195</a></li>

  <li>JANITORIAL: CREATE_PROJECT: disable MD5 deprecation warning by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3909834417"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7200"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7200/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7200">#7200</a></li>

  <li>SCUMM: MI2 DOS NI demo - Minor script patch to prevent crash at startup by following
  the correct script path. by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3876866324"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7177"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7177/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7177">#7177</a></li>

  <li>3DS: Fix d-pad direction case by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3912393250"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7205"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7205/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7205">#7205</a></li>

  <li>FREESCAPE: add a debugger. by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/dhruv0154/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3911138792"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7203"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7203/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7203">#7203</a></li>

  <li>GUI: Adding Help button to GMM and Browser dialog by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sev-/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sev-">@sev-</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3858226547"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7170"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7170/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7170">#7170</a></li>

  <li>COMMON: make Common::Pair constexpr by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3898247963"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7190"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7190/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7190">#7190</a></li>

  <li>JANITORIAL: DEVTOOLS: replace sprintf with snprintf by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3909841044"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7201"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7201/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7201">#7201</a></li>

  <li>BAGEL: MFC: Move MFC into graphics/ by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/dreammaster/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/dreammaster">@dreammaster</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3889843954"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7186"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7186/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7186">#7186</a></li>

  <li>SCUMM: MMNES - Add support for playback of title screens. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3915775783"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7206"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7206/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7206">#7206</a></li>

  <li>BLADERUNNER: Drop ''long double'' usage by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3921351383"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7210"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7210/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7210">#7210</a></li>

  <li>DIRECTOR: add MacJapanese pre-6 equality table by @mistydemeo in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3923167168" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7212" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7212/hovercard" href="https://github.com/scummvm/scummvm/pull/7212">#7212</a></li>

  <li>CREATE_PROJECT: use C++11-style for each loops instead of iterators by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3923687744"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7213"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7213/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7213">#7213</a></li>

  <li>DREAMCAST: Automatically launch when single game detected by @mark-temporary
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3917277626"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7208"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7208/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7208">#7208</a></li>

  <li>JANITORIAL: NUVIE: resolve global constructor by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3925376010"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7214"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7214/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7214">#7214</a></li>

  <li>COMMON: Move file search in current working directory to backends by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3881755306"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7182"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7182/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7182">#7182</a></li>

  <li>BACKENDS: SDL: Set getImGuiTexture filtering to nearest by @sronsse in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3919270173" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7209" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7209/hovercard" href="https://github.com/scummvm/scummvm/pull/7209">#7209</a></li>

  <li>GUI: Add scrollable removal confirmation dialog by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3917103660"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7207"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7207/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7207">#7207</a></li>

  <li>GRAPHICS: FONTS: Add allowCharClipping parameter by @AndywinXp in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3872630205" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7175" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7175/hovercard" href="https://github.com/scummvm/scummvm/pull/7175">#7175</a></li>

  <li>GUI: Fix the List scrolling with up/down keys by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3930974299"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7216"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7216/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7216">#7216</a></li>

  <li>JANITORIAL: M4: add missing constructors to Buffer struct by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3930783510"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7215"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7215/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7215">#7215</a></li>

  <li>JANITORIAL: M4: restore default initializers to Buffer struct by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3932301882"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7217"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7217/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7217">#7217</a></li>

  <li>DIRECTOR: Fixes for Incarnatia by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3933625534"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7219"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7219/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7219">#7219</a></li>

  <li>SCUMM: Introduce ScummEditor by @sronsse in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3933527627" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7218" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7218/hovercard" href="https://github.com/scummvm/scummvm/pull/7218">#7218</a></li>

  <li>GUI: Fix Arrow key navigation in Grouped List by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3935121241"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7220"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7220/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7220">#7220</a></li>

  <li>GUI: Fix arrow key navigation with collapsed groups in List by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3938366773"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7223"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7223/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7223">#7223</a></li>

  <li>SCUMM: Add getEncByte helper method by @sronsse in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3938144349" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7222" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7222/hovercard" href="https://github.com/scummvm/scummvm/pull/7222">#7222</a></li>

  <li>SCUMM: MM NES - Workaround to fix intro logo scroll hang with 256px viewport
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3935331224"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7221"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7221/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7221">#7221</a></li>

  <li>FREESCAPE: Fix DOS/CGA rendering and palettes for Total Eclipse by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SandhuAmy35/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SandhuAmy35">@SandhuAmy35</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3941000041"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7225"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7225/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7225">#7225</a></li>

  <li>Move and update the ImGui MemoryEditor component by @sronsse in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3942548403" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7229" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7229/hovercard" href="https://github.com/scummvm/scummvm/pull/7229">#7229</a></li>

  <li>FREESCAPE: remove temp file from freescape engine by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944035263"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7230"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7230/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7230">#7230</a></li>

  <li>DEVTOOLS: PYCDLIB: Allow None encoding in <em>get</em>*_entry functions, add
  encoding fallback in walk by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3912388279"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7204"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7204/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7204">#7204</a></li>

  <li>JANITORIAL: ULTIMA: use ARRAYSIZE macro by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944861300"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7232"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7232/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7232">#7232</a></li>

  <li>JANITORIAL: HPL1: use ARRAYSIZE macro by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944866496"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7233"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7233/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7233">#7233</a></li>

  <li>JANITORIAL: GRIM: use ARRAYSIZE macro by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944869183"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7234"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7234/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7234">#7234</a></li>

  <li>JANITORIAL: ENGINES: use ARRAYSIZE macro by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944873334"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7235"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7235/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7235">#7235</a></li>

  <li>JANITORIAL: DEVTOOLS: use common ARRAYSIZE macro definition by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944877093"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7236"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7236/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7236">#7236</a></li>

  <li>JANITORIAL: use common ARRAYSIZE macro by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944881742"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7237"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7237/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7237">#7237</a></li>

  <li>AGS: Update beyondowlsgard entry by @menschel in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3944720807" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7231" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7231/hovercard" href="https://github.com/scummvm/scummvm/pull/7231">#7231</a></li>

  <li>Fix JSON library IntegerNumber handling by @sronsse in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3944923570" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7239" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7239/hovercard" href="https://github.com/scummvm/scummvm/pull/7239">#7239</a></li>

  <li>AGOS: Simon 1 Acorn - Implement Acorn cursor for Simon 1 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3953526651"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7245"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7245/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7245">#7245</a></li>

  <li>SCUMM: EDITOR: Introduce settings by @sronsse in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3951036507" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7244" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7244/hovercard" href="https://github.com/scummvm/scummvm/pull/7244">#7244</a></li>

  <li>BASE: Fix --md5 warning about Mac resources when used on a non-Mac file by @elasota
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3949141460"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7242"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7242/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7242">#7242</a></li>

  <li>SCUMM: MM Apple II - Use the original Apple II cursor like we do for the other
  platforms. by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3957216987"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7247"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7247/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7247">#7247</a></li>

  <li>SCUMM: MI2 NI DOS Demo - Add support for original demo.rec playback file by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3950302306"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7243"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7243/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7243">#7243</a></li>

  <li>GRIM: Delete Set pool objects <em>after</em> deleting Actor pool objects by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3948864035"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7241"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7241/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7241">#7241</a></li>

  <li>FREESCAPE: Fix minor UI color palette for DOS/EGA Total Eclipse. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SandhuAmy35/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SandhuAmy35">@SandhuAmy35</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3971698523"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7250"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7250/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7250">#7250</a></li>

  <li>AGOS: Simon1 - Support for the Desktop Tracker(DskT) format compressed mods
  used for music by Simon 1 for Acorn Archimedes. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3941636151"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7227"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7227/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7227">#7227</a></li>

  <li>GOB: improve detection entries comments by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3971802090"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7251"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7251/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7251">#7251</a></li>

  <li>Fix starting Teenagent Polish and Russian versions by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/criezy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/criezy">@criezy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3965867017"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7249"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7249/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7249">#7249</a></li>

  <li>GUI: Enable rich syntax search in Grid View by @phyulwin in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3956456999" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7246" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7246/hovercard" href="https://github.com/scummvm/scummvm/pull/7246">#7246</a></li>

  <li>BACKENDS: avoid Windows ARRAYSIZE definition by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3944911453"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7238"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7238/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7238">#7238</a></li>

  <li>SCUMM: Introduce Resource class to ScummEditor by @sronsse in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3979283366" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7257" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7257/hovercard" href="https://github.com/scummvm/scummvm/pull/7257">#7257</a></li>

  <li>COMMON, WIN32: Printing support improvements by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sdelamarre/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sdelamarre">@sdelamarre</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3986371361"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7259"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7259/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7259">#7259</a></li>

  <li>FREESCAPE: Fix DOS Castle Master lightning effect by @AndreiRV1 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3972340176" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7252" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7252/hovercard" href="https://github.com/scummvm/scummvm/pull/7252">#7252</a></li>

  <li>NANCY: Fix off-by-one error in TableIndexSetValueHS correctness check by @flipkick
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3991903620"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7260"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7260/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7260">#7260</a></li>

  <li>AGI: Migrate Apple II and CoCo3 sound code to Audio::PCSpeaker by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3978417365"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7255"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7255/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7255">#7255</a></li>

  <li>AGOS: Simon1 Acorn Floppy Demo - Fix for Simon appearing black in the Acorn
  Floppy Demo. by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3992409871"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7263"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7263/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7263">#7263</a></li>

  <li>NANCY: Fix TurningPuzzle animation speed scaling with frame count by @flipkick
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3993598321"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7264"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7264/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7264">#7264</a></li>

  <li>AGOS: Simon1 - More accurate Acorn cursor. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3975635007"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7254"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7254/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7254">#7254</a></li>

  <li>CHAMBER: Refactor splash screen for Hercules by @11-andy-11 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3997613958" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7267" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7267/hovercard" href="https://github.com/scummvm/scummvm/pull/7267">#7267</a></li>

  <li>Feature/new debugger gui by @ramyak-sharma in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3995528601" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7265" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7265/hovercard" href="https://github.com/scummvm/scummvm/pull/7265">#7265</a></li>

  <li>GRAPHICS: Move Hercules palettes to global graphics manager by @11-andy-11 in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4001403092"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7270"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7270/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7270">#7270</a></li>

  <li>DIRECTOR: Fixes for Journeyman Project by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4001713605"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7272"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7272/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7272">#7272</a></li>

  <li>Introduce Explorer window to ScummEditor by @sronsse in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3992067172" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7262" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7262/hovercard" href="https://github.com/scummvm/scummvm/pull/7262">#7262</a></li>

  <li>DIRECTOR: DT: Add scrolling and labels by @ramyak-sharma in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4004904387" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7273" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7273/hovercard" href="https://github.com/scummvm/scummvm/pull/7273">#7273</a></li>

  <li>AUDIO: MT32: Simulate original MT-32 green LCD display in OSD by @artemnutbov
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3986264574"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7258"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7258/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7258">#7258</a></li>

  <li>ALG Engine: ready for testing by @dckone in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3999482839" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7269" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7269/hovercard" href="https://github.com/scummvm/scummvm/pull/7269">#7269</a></li>

  <li>FREESCAPE: Depth rendering based on the original implementation by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/neuromancer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/neuromancer">@neuromancer</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3655067904"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7049"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7049/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7049">#7049</a></li>

  <li>IOS7: Integrate CoreMIDI into the iOS &amp; tvOS backends by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3997428391"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7266"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7266/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7266">#7266</a></li>

  <li>COMMON: I18N: Load <code class="notranslate">.po</code> files near <code class="notranslate">translations.dat</code>
  by @sh3boly in <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="3991975543" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7261"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7261/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7261">#7261</a></li>

  <li>Make buildbots happy again by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4007627432"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7274"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7274/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7274">#7274</a></li>

  <li>BASE: Do not register COREMIDI plugin for tvOS by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4007760145"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7275"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7275/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7275">#7275</a></li>

  <li>ALG: fix static code analysis issues, add credits.pl, add extended saves support
  by @dckone in <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="4009149582" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7278"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7278/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7278">#7278</a></li>

  <li>NANCY: Fix TurningPuzzle solve animation timing by @flipkick in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4008821798" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7277" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7277/hovercard" href="https://github.com/scummvm/scummvm/pull/7277">#7277</a></li>

  <li>ALG: bugfix for unregisterScriptFunctions by @dckone in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4011663830" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7281" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7281/hovercard" href="https://github.com/scummvm/scummvm/pull/7281">#7281</a></li>

  <li>AGOS: Simon1 Acorn - Fix playback of mods for the full version of Simon 1 Acorn
  Floppy. by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4011726651"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7282"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7282/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7282">#7282</a></li>

  <li>TINSEL: Discworld 1 Script Patches by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4009249935"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7279"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7279/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7279">#7279</a></li>

  <li>ALG: add remaining missing initializers. CID 1609033, CID 1609028 by @dckone
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4019483634"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7283"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7283/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7283">#7283</a></li>

  <li>WAGE: Support custom File menu by @1SHAMAY1 in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4022236476" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7285" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7285/hovercard" href="https://github.com/scummvm/scummvm/pull/7285">#7285</a></li>

  <li>GUI: Fix lag and Implement Anti-aliasing in Rich Text by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4021576727"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7284"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7284/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7284">#7284</a></li>

  <li>BACKENDS: OPENGL: Unpanic warning by @orgads in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4023898462" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7286" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7286/hovercard" href="https://github.com/scummvm/scummvm/pull/7286">#7286</a></li>

  <li>DIRECTOR: DT: Implement Cast Details by @avnishkirnalli in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4027699157" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7288" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7288/hovercard" href="https://github.com/scummvm/scummvm/pull/7288">#7288</a></li>

  <li>GIT: Add vcpkg_installed to .gitignore by @Krish2882005 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4029810831" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7290" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7290/hovercard" href="https://github.com/scummvm/scummvm/pull/7290">#7290</a></li>

  <li>DIRECTOR: DT: Add Light theme and refactor themes by @Krish2882005 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4029739302" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7289" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7289/hovercard" href="https://github.com/scummvm/scummvm/pull/7289">#7289</a></li>

  <li>KYRA: EOB: fix compass after spellbook abort by @btb in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4025210534" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7287" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7287/hovercard" href="https://github.com/scummvm/scummvm/pull/7287">#7287</a></li>

  <li>DIRECTOR: DT: Score: Add Center button, QOL changes by @ramyak-sharma in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4031259579"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7291"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7291/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7291">#7291</a></li>

  <li>PHOENIXVR: Fix some leaks by @tunnelsociety in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4032007353" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7292" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7292/hovercard" href="https://github.com/scummvm/scummvm/pull/7292">#7292</a></li>

  <li>GUI: Fix leak of cached RichText surface by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4032065275" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7293" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7293/hovercard" href="https://github.com/scummvm/scummvm/pull/7293">#7293</a></li>

  <li>FREESCAPE: Fix minor UI fixes in Darkside CGA and global palettes for… by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SandhuAmy35/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SandhuAmy35">@SandhuAmy35</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4038248396"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7296"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7296/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7296">#7296</a></li>

  <li>QDENGINE: Fix Broken Pathfinding in Pilot Brothers 3D by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4039218806"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7297"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7297/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7297">#7297</a></li>

  <li>TINSEL: Add support for PSX .LFI/.LFD archive files by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4040291683"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7298"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7298/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7298">#7298</a></li>

  <li>AGOS: Elvira 1/2 Atari ST - Music support. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4038156654"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7295"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7295/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7295">#7295</a></li>

  <li>DIRECTOR: DT: Debugger UI QoL updates and ImGui crash fix by @Krish2882005 in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4041924053"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7299"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7299/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7299">#7299</a></li>

  <li>SCUMM: Unify AkosRenderer and ClassicCostumeRenderer RLE code by @mikrosk in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3011928649"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6565"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6565/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6565">#6565</a></li>

  <li>SCUMM: MI1 SEGA CD - Add the option to use the original ''wait'' cursor on the
  pause menu by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4007861204"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7276"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7276/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7276">#7276</a></li>

  <li>TINSEL: Fix DW1 Act 4 dragon appearing before finale by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4047651872"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7300"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7300/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7300">#7300</a></li>

  <li>AUDIO: fix vorbis seek callback return value by @flipkick in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4048611105" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7302" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7302/hovercard" href="https://github.com/scummvm/scummvm/pull/7302">#7302</a></li>

  <li>WAGE: add ability to display Startup Image and play Startup Sound by @roby405
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4051534171"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7303"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7303/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7303">#7303</a></li>

  <li>TINSEL: Fix multibyte strings by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4053601893"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7304"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7304/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7304">#7304</a></li>

  <li>GUI: Refactor PopUpDialog::findItem by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4061334230" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7310" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7310/hovercard" href="https://github.com/scummvm/scummvm/pull/7310">#7310</a></li>

  <li>DIRECTOR: DT: Add variable watch logging and script search by @ramyak-sharma
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4058271110"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7306"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7306/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7306">#7306</a></li>

  <li>CHAMBER: Implement Hercule scaling by @11-andy-11 in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4033995625" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7294" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7294/hovercard" href="https://github.com/scummvm/scummvm/pull/7294">#7294</a></li>

  <li>NANCY: Fix RippedLetterPuzzle crash after save by @flipkick in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4061588316" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7311" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7311/hovercard" href="https://github.com/scummvm/scummvm/pull/7311">#7311</a></li>

  <li>WAGE: Fix character encoding in Apple menu game name by @1SHAMAY1 in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4064797764" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7312" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7312/hovercard" href="https://github.com/scummvm/scummvm/pull/7312">#7312</a></li>

  <li>DEVTOOLS: PYCDLIB: Explicitly pass encoding only when it is not None by @npjg
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4073282564"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7314"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7314/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7314">#7314</a></li>

  <li>NANCY: Fix HIS Vorbis rewind-to-zero by @flipkick in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4060489375" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7309" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7309/hovercard" href="https://github.com/scummvm/scummvm/pull/7309">#7309</a></li>

  <li>NANCY: Fix RaycastPuzzle typo. PVS-Studio V501 by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4077321175" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7316" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7316/hovercard" href="https://github.com/scummvm/scummvm/pull/7316">#7316</a></li>

  <li>NANCY: Fix PianoPuzzle multi-key edge case by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4077618017" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7317" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7317/hovercard" href="https://github.com/scummvm/scummvm/pull/7317">#7317</a></li>

  <li>SCUMM: Remove broken ARM costume renderer by @mikrosk in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4075434422" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7315" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7315/hovercard" href="https://github.com/scummvm/scummvm/pull/7315">#7315</a></li>

  <li>MTROPOLIS: resolve key mapping mismatch for ARROWDOWN and DEL by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4078735579"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7320"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7320/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7320">#7320</a></li>

  <li>JANITORIAL: resolve signed/unsigned conflicts by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4078938716"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7321"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7321/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7321">#7321</a></li>

  <li>TINSEL: New DW1 introduction skip technique by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4078661423"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7319"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7319/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7319">#7319</a></li>

  <li>DIRECTOR: Fixes for D6 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4068368931"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7313"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7313/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7313">#7313</a></li>

  <li>GUI: Update print preview on dialog resize by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4079841232" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7323" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7323/hovercard" href="https://github.com/scummvm/scummvm/pull/7323">#7323</a></li>

  <li>SCUMM: HE: Avoid Wiz left shift of negative value by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4079057327" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7322" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7322/hovercard" href="https://github.com/scummvm/scummvm/pull/7322">#7322</a></li>

  <li>SCUMM: Implement UI and functionality for loading original playback files for
  FoA, MI1 and MI2. by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4058447368"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7307"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7307/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7307">#7307</a></li>

  <li>SLUDGE: Fix data file encoding and restore CP1252 validation by @AzzurraSuffia
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4091648512"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7328"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7328/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7328">#7328</a></li>

  <li>GUI: Improve rendering time of cloud and keyboard tabs in help dialog by @StoneVerve
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4078052126"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7318"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7318/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7318">#7318</a></li>

  <li>GUI: Parse unpacked themes by @sh3boly in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4059805493" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7308" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7308/hovercard" href="https://github.com/scummvm/scummvm/pull/7308">#7308</a></li>

  <li>WAYNESWORLD: Add detection object by @flipkick in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4102432762" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7337" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7337/hovercard" href="https://github.com/scummvm/scummvm/pull/7337">#7337</a></li>

  <li>TINSEL: Fix DW1 Sega Saturn graphics by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4102322968"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7336"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7336/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7336">#7336</a></li>

  <li>SCI: Add detection for the Hebrew fanmade translation of KQ5 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4093450543"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7329"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7329/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7329">#7329</a></li>

  <li>SHERLOCK: Fall back to AdLib for General MIDI in Serrated Scalpel by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4097696633"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7332"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7332/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7332">#7332</a></li>

  <li>DIRECTOR: Fixes for Journeyman Project by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4103350558"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7339"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7339/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7339">#7339</a></li>

  <li>AGOS: Personal Nightmare - Fix palette for Amiga and Atari ST inventory icons
  and fix the ''ROOM'' button. by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4095763738"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7331"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7331/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7331">#7331</a></li>

  <li>AGOS: Personal Nightmare - wait command fixes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4098213503"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7333"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7333/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7333">#7333</a></li>

  <li>AGOS: Personal Nightmare Amiga - Add Amiga specific info and hand cursors by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4104173073"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7340"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7340/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7340">#7340</a></li>

  <li>BUILD: Drop clang -Wno-sign-compare by @tunnelsociety in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4098584917" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7334" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7334/hovercard" href="https://github.com/scummvm/scummvm/pull/7334">#7334</a></li>

  <li>TINSEL: Fix DW1 PSX palette mapping, image clipping by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4113910842"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7343"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7343/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7343">#7343</a></li>

  <li>WAYNESWORLD: Add WAYNESWORLD engine (which is accidentally already in Master)
  by @Strangerke in <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="4103341054" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7338"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7338/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7338">#7338</a></li>

  <li>DIRECTOR: Add detection and xlibs for The Legend of Lotus Spring by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4085495956"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7325"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7325/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7325">#7325</a></li>

  <li>GOB: Performance optimisations by @mikrosk in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4106946321" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7341" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7341/hovercard" href="https://github.com/scummvm/scummvm/pull/7341">#7341</a></li>

  <li>GUI: RemovalConfirmationDialog improvements before release by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4123263010"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7350"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7350/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7350">#7350</a></li>

  <li>GUI: Fix ListWidget SHIFT+UP multi-selection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4131970950"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7357"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7357/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7357">#7357</a></li>

  <li>SLUDGE: Fix missing text and dynamic graphics during hardScroll by @AzzurraSuffia
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4134403603"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7358"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7358/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7358">#7358</a></li>

  <li>DRASCULA: Fix for original walk/talk bug <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1231955887" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/3871" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/3871/hovercard" href="https://github.com/scummvm/scummvm/pull/3871">#3871</a>
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4136091719"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7361"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7361/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7361">#7361</a></li>

  <li>AGOS: Further fixes for PN ''wait'' command by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4130409296"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7354"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7354/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7354">#7354</a></li>

  <li>IOS7: Make tvOS run again by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4116069119"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7345"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7345/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7345">#7345</a></li>

  <li>KYRA: Add Korean fan translation support for Hand of Fate by @colus001 in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4100296167"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7335"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7335/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7335">#7335</a></li>

  <li>Bump requests from 2.32.5 to 2.33.0 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4145777413"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7369"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7369/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7369">#7369</a></li>

  <li>GUI: Fix mouse dragging issue with scrollbar in help menu by @moetez00 in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4130917953"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7356"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7356/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7356">#7356</a></li>

  <li>LAUNCHER: Remove temporary game ID when detection fails. by @moetez00 in <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4136324536"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7363"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7363/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7363">#7363</a></li>

  <li>IOS7: Fix airplay mirroring to external displays by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/larsamannen/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/larsamannen">@larsamannen</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4141567536"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7366"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7366/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7366">#7366</a></li>

  <li>NEWS: add latest GOB changes to NEUES.md by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4158299720"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7373"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7373/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7373">#7373</a></li>

  </ul>

  <h2 dir="auto">New Contributors: Welcome!</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/cscd98/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cscd98">@cscd98</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3608718421" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7021"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7021/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7021">#7021</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/whoozle/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/whoozle">@whoozle</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3578571076" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7000"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7000/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7000">#7000</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/sam-mfb/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sam-mfb">@sam-mfb</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3674393551" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7061"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7061/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7061">#7061</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lili1228/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lili1228">@Lili1228</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3677146363" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7063"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7063/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7063">#7063</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/zafos/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zafos">@zafos</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3767121876" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7106"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7106/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7106">#7106</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SandhuAmy35/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SandhuAmy35">@SandhuAmy35</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3777343501" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7118"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7118/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7118">#7118</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/dhruv0154/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dhruv0154">@dhruv0154</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3765936408" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7105"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7105/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7105">#7105</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3751490295" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7096"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7096/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7096">#7096</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/jaskaran-singh-77/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/jaskaran-singh-77">@jaskaran-singh-77</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3788975243" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7132"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7132/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7132">#7132</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/TejeshwarDivekar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TejeshwarDivekar">@TejeshwarDivekar</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3841111111" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7158"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7158/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7158">#7158</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gulraiznoorbari/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gulraiznoorbari">@gulraiznoorbari</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3856712663" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7169"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7169/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7169">#7169</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DarkCenobyte/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DarkCenobyte">@DarkCenobyte</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3853799682" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7166"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7166/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7166">#7166</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Miguel-Herrero/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Miguel-Herrero">@Miguel-Herrero</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3801198614" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7138"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7138/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7138">#7138</a></li>

  <li>@mark-temporary made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3917277626" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7208" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7208/hovercard" href="https://github.com/scummvm/scummvm/pull/7208">#7208</a></li>

  <li>@menschel made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3944720807" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7231" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7231/hovercard" href="https://github.com/scummvm/scummvm/pull/7231">#7231</a></li>

  <li>@phyulwin made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3956456999" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7246" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7246/hovercard" href="https://github.com/scummvm/scummvm/pull/7246">#7246</a></li>

  <li>@AndreiRV1 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3972340176" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7252" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7252/hovercard" href="https://github.com/scummvm/scummvm/pull/7252">#7252</a></li>

  <li>@flipkick made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3991903620" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7260" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7260/hovercard" href="https://github.com/scummvm/scummvm/pull/7260">#7260</a></li>

  <li>@11-andy-11 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3997613958" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7267" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7267/hovercard" href="https://github.com/scummvm/scummvm/pull/7267">#7267</a></li>

  <li>@ramyak-sharma made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3995528601" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7265" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7265/hovercard" href="https://github.com/scummvm/scummvm/pull/7265">#7265</a></li>

  <li>@artemnutbov made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3986264574" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7258" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7258/hovercard" href="https://github.com/scummvm/scummvm/pull/7258">#7258</a></li>

  <li>@sh3boly made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3991975543" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7261" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7261/hovercard" href="https://github.com/scummvm/scummvm/pull/7261">#7261</a></li>

  <li>@1SHAMAY1 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4022236476" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7285" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7285/hovercard" href="https://github.com/scummvm/scummvm/pull/7285">#7285</a></li>

  <li>@avnishkirnalli made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4027699157" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7288" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7288/hovercard" href="https://github.com/scummvm/scummvm/pull/7288">#7288</a></li>

  <li>@btb made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4025210534" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7287"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7287/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7287">#7287</a></li>

  <li>@roby405 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4051534171" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7303" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7303/hovercard" href="https://github.com/scummvm/scummvm/pull/7303">#7303</a></li>

  <li>@AzzurraSuffia made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4091648512" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7328" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7328/hovercard" href="https://github.com/scummvm/scummvm/pull/7328">#7328</a></li>

  <li>@StoneVerve made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4078052126" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7318" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7318/hovercard" href="https://github.com/scummvm/scummvm/pull/7318">#7318</a></li>

  <li>@colus001 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4100296167" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7335" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7335/hovercard" href="https://github.com/scummvm/scummvm/pull/7335">#7335</a></li>

  <li>@moetez00 made their first contribution in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4130917953" data-permission-text="Title
  is private" data-url="https://github.com/scummvm/scummvm/issues/7356" data-hovercard-type="pull_request"
  data-hovercard-url="/scummvm/scummvm/pull/7356/hovercard" href="https://github.com/scummvm/scummvm/pull/7356">#7356</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2026.1.0...v2026.2.0"><tt>v2026.1.0...v2026.2.0</tt></a></p>'
updated: '2026-03-28T21:27:36Z'
version: v2026.2.0
version_title: 'ScummVM 2026.2.0: "Railmonicon"'
website: https://www.scummvm.org
---
ScummVM allows you to play classic graphic point-and-click adventure games, text adventure games, and RPGs, as long as you already have the game data files. ScummVM replaces the executable files shipped with the games, which means you can now play your favorite games on all your favorite devices.

While ScummVM was originally designed to run LucasArts’ SCUMM games, over time support has been added for many other games: see the full list [on our wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Noteworthy titles include Broken Sword, Myst and Blade Runner, although there are countless other hidden gems to explore.