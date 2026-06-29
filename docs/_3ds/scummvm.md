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
    url: https://downloads.scummvm.org/frs/scummvm/2026.3.0/scummvm-2026.3.0-3ds-3dsx.zip
  scummvm-cia.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2026.3.0/scummvm-2026.3.0-3ds-cia.zip
  scummvm-ds.zip:
    size: null
    url: https://downloads.scummvm.org/frs/scummvm/2026.3.0/scummvm-2026.3.0-ds.zip
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
stars: 2725
systems:
- 3DS
- DS
title: scummvm
unique_ids:
- '0xFF321'
update_notes: '<p dir="auto">ScummVM 2026.3.0 "Carousels &amp; Killer Whales" comes
  to fruition. So far, we are able to keep the release cadence. This quarter, the
  team is bringing you a set of new and old, all exciting features!</p>

  <h2 dir="auto">Newly Supported Games:</h2>

  <ul dir="auto">

  <li><em>Nancy Drew: The Haunted Carousel</em></li>

  <li><em>Nancy Drew: Danger on Deception Island</em></li>

  <li><em>Noctropolis</em></li>

  <li><em>Cartoon Carnival</em></li>

  <li><em>Alfred Pelrock: En Busca de un Sueño</em></li>

  <li><em>Pilot Brothers: On the Track of Striped Elephant</em></li>

  <li><em>Pilot Brothers: The Case of Serial Maniac</em> and 5 more games on the same
  engine</li>

  </ul>

  <p dir="auto">But wait, that''s not everything!</p>

  <h1 dir="auto">Changelog</h1>

  <h2 dir="auto">New games:</h2>

  <ul dir="auto">

  <li>Added support for Nancy Drew: The Haunted Carousel.</li>

  <li>Added support for Nancy Drew: Danger on Deception Island.</li>

  <li>Added support for Noctropolis.</li>

  <li>Added support for Cartoon Carnival.</li>

  <li>Added support for Alfred Pelrock: En Busca de un Sueño.</li>

  <li>Added support for Pilot Brothers: On the Track of Striped Elephant,<br>

  Pilot Brothers: The Case of Serial Maniac, and five minor<br>

  games built on the Gamos engine.</li>

  </ul>

  <h2 dir="auto">General:</h2>

  <ul dir="auto">

  <li>Highlight clickable links in the GUI with a cursor change.</li>

  <li>Fixed window size when switching out of fullscreen mode on 3D engines.</li>

  <li>Implemented NULL OPL driver for lower-base systems.</li>

  <li>Implemented kinetic scolling in GUI lists.</li>

  </ul>

  <h2 dir="auto">ACCESS:</h2>

  <ul dir="auto">

  <li>Fixed various script issues in Martian Memorandum.</li>

  </ul>

  <h2 dir="auto">AGOS:</h2>

  <ul dir="auto">

  <li>Added support for language files used by Amiga and Macintosh<br>

  versions of Simon2.</li>

  </ul>

  <h2 dir="auto">GLK:</h2>

  <ul dir="auto">

  <li>Exposed text and engine settings in the GUI.</li>

  </ul>

  <h2 dir="auto">LastExpress:</h2>

  <ul dir="auto">

  <li>The game has been supported for a while now (2026.1.0), we just<br>

  forgot to add a news entry here. Whoops!</li>

  <li>Several inaccuracies from the character logic have been fixed,<br>

  which means that some rare issues concerning characters behavior<br>

  should now be gone.</li>

  </ul>

  <h2 dir="auto">MADS:</h2>

  <ul dir="auto">

  <li>In Rex Nebular fix game being semi-stuck while using binoculars.</li>

  </ul>

  <h2 dir="auto">MM:</h2>

  <ul dir="auto">

  <li>Reworked keymapper for MM1.</li>

  <li>Fixed MM1 Enhanced allowing trading more than the character owned.</li>

  <li>Fixed MM1 Enhanced allowing free temple healing where it shouldn''t.</li>

  <li>MM1 Enhanced most recently played music was restarting after opening and closing
  the GMM.</li>

  </ul>

  <h2 dir="auto">MYST3:</h2>

  <ul dir="auto">

  <li>Fixed a regression for the animation of the control wheel at J''nanin''s shore.</li>

  <li>Camera movement is now free after placing a symbol on the pedestal at the watch
  tower in J''nanin.</li>

  </ul>

  <h2 dir="auto">NANCY:</h2>

  <ul dir="auto">

  <li>Fixed a regression in ripped letter types of puzzles, affecting all the Nancy
  games that feature such puzzles.</li>

  <li>Fixed potential crashes in ripped letter types of puzzles, after loading a saved
  game.</li>

  <li>Show the correct mouse cursor in rotating lock types of puzzles.</li>

  <li>Enter the game scene directly when loading a saved game from the launcher or
  the GMM, instead of starting in the main game menu.</li>

  <li>Properly handle the "Continue Game" button after clicking on the "More Nancy"
  button.</li>

  <li>Fixed an edge case in piano types of puzzles, where clicking on a key while
  another was still down produced a graphical glitch.</li>

  <li>Fixed some sounds stopping prematurely in Nancy Drew: Secret of the Scarlet
  Hand and newer games.</li>

  <li>Fixed animation speed and timing in turning types of puzzles.</li>

  </ul>

  <h2 dir="auto">SLUDGE:</h2>

  <ul dir="auto">

  <li>Added two more games to detection, "Sam and Max Flintlocked" and<br>

  "Full Moon".</li>

  </ul>

  <h2 dir="auto">TwinE:</h2>

  <ul dir="auto">

  <li>Fixed soft lock collision bug with bulldozer.</li>

  <li>Fixed wrong scaling for plasma menu effect.</li>

  <li>Fixed holomap model rendering.</li>

  <li>Disable autosaves while driving a vehicle.</li>

  </ul>

  <h2 dir="auto">Atari port:</h2>

  <ul dir="auto">

  <li>Added native CDDA support.</li>

  <li>Added plugin support (now ScummVM can run with as little as a few megs of RAM).</li>

  <li>Added native YM2149 support (currently usable for Elvira 1 and 2).</li>

  <li>Reworked audio mixer (this fixes the barking poodles in SOMI).</li>

  <li>Autosave is disabled by default as it leads to audible artefacts during gameplay.</li>

  </ul>

  <h2 dir="auto">PS3 port:</h2>

  <ul dir="auto">

  <li>Added support for running ScummVM engines as separate modules/executables.<br>

  This saves about 90 MB of RAM. It is enabled only for release packages.</li>

  </ul>

  <hr>

  <h1 dir="auto">Merged PRs</h1>

  <ul dir="auto">

  <li>AVALANCHE: Implement intro animation in Lord Avalot d''Argent by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4119530064"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7349"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7349/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7349">#7349</a></li>

  <li>Bump pygments from 2.19.2 to 2.20.0 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4173566189"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7379"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7379/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7379">#7379</a></li>

  <li>GUI: Fix cursor jump in GroupedList after game removal by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/anttt194/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/anttt194">@anttt194</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4163710404"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7377"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7377/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7377">#7377</a></li>

  <li>libretro: add webOS to gitlab CI by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/cscd98/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cscd98">@cscd98</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4177842939"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7381"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7381/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7381">#7381</a></li>

  <li>AGOS: Fix Elvira 2 Atari ST noise generation by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4178009754"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7382"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7382/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7382">#7382</a></li>

  <li>README: Update Mass Add instructions. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4163299383"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7375"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7375/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7375">#7375</a></li>

  <li>GUI: Add support for multiple cursor types with index cursor for links by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MarTCM/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MarTCM">@MarTCM</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4200641457"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7389"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7389/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7389">#7389</a></li>

  <li>GLK: Expose GUI options by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4164950903"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7378"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7378/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7378">#7378</a></li>

  <li>JANITORIAL: ENGINES: resolve various compiler warnings by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4200351768"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7387"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7387/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7387">#7387</a></li>

  <li>ULTIMA8: Improve code for changing the screen mode by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4205987509"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7396"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7396/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7396">#7396</a></li>

  <li>KYRA: Return an error code if setting the pixel format fails by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4205248367"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7393"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7393/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7393">#7393</a></li>

  <li>GUI: Improve Tooltip event handling by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4136142927"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7362"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7362/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7362">#7362</a></li>

  <li>MM: Fix warnings about deprecated ManagedSurface copy constructor by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4202437529"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7391"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7391/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7391">#7391</a></li>

  <li>AGOS: Simon2 Mac/Amiga language file support by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4114172097"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7344"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7344/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7344">#7344</a></li>

  <li>SDL: Fix resizing bug when switching off fullscreen with some 3D engines by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4116571360"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7346"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7346/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7346">#7346</a></li>

  <li>3DS: Improve dirty rectangle tracking for emulated pixel formats by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4156429663"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7372"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7372/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7372">#7372</a></li>

  <li>AUDIO: Add a null OPL implementation by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4154132146"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7370"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7370/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7370">#7370</a></li>

  <li>NANCY: Fix warnings about deprecated ManagedSurface copy constructor by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4202019280"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7390"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7390/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7390">#7390</a></li>

  <li>BUILD: BASE: Differentiate Apple Clang from vanilla Clang by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4206970380"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7398"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7398/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7398">#7398</a></li>

  <li>SURFACESDL: Reject true colour pixel formats when _isHwPalette is enabled by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4208276707"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7399"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7399/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7399">#7399</a></li>

  <li>BACKENDS: Move custom fast conversion paths to common code by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4208865766"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7403"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7403/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7403">#7403</a></li>

  <li>ENGINES: resolve warnings about non-trivial copyability by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4200472453"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7388"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7388/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7388">#7388</a></li>

  <li>GLK: Expose GUI options by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4204957134"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7392"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7392/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7392">#7392</a></li>

  <li>CONFIGURE: Don''t define empty plugin prefix/suffix in config.h by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4184884438"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7384"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7384/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7384">#7384</a></li>

  <li>GUI: Provide default title and button label for SaveLoadChooser by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4213738332"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7406"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7406/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7406">#7406</a></li>

  <li>GLK: Replace use of deprecated U32String methods by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4212300487"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7404"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7404/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7404">#7404</a></li>

  <li>PHOENIXVR: Simplify setting true colour screen modes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4206039532"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7397"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7397/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7397">#7397</a></li>

  <li>PLUMBERS: Return an error code if setting the pixel format fails by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4205272731"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7394"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7394/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7394">#7394</a></li>

  <li>ENGINES: Add BOLT (Cartoon Carnival) engine by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/AndywinXp/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/AndywinXp">@AndywinXp</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4047673577"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7301"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7301/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7301">#7301</a></li>

  <li>GUI: Preserve multi-selection when changing grouping by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/anttt194/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/anttt194">@anttt194</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4208765769"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7402"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7402/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7402">#7402</a></li>

  <li>MM: Rework MM1 keymap handling and add shared click actions by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4216581859"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7408"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7408/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7408">#7408</a></li>

  <li>GOB: add spanish Adibou1 addon by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4218977948"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7411"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7411/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7411">#7411</a></li>

  <li>ENGINES: Change SaveStateDescriptor description to use Common::String by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4217093598"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7409"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7409/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7409">#7409</a></li>

  <li>GUI: Add a scrollbar, close button and drag functionality in About dialog by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4227217916"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7413"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7413/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7413">#7413</a></li>

  <li>ZVISION: Support running with different pixel formats by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4235340306"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7417"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7417/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7417">#7417</a></li>

  <li>ANDROID: Move to Oboe for audio by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3851032676"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7164"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7164/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7164">#7164</a></li>

  <li>DIRECTOR: Process timeout events independently of frame cycle by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lotharsm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lotharsm">@lotharsm</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4248232836"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7423"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7423/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7423">#7423</a></li>

  <li>DIRECTOR: Bad Day At The Midway 16bit video rendering fixes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/bleggett/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/bleggett">@bleggett</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4249275514"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7425"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7425/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7425">#7425</a></li>

  <li>AGOS: Fix Elvira 2 Atari ST colours by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4248940721"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7424"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7424/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7424">#7424</a></li>

  <li>AGOS: PN Amiga improvements and prevent quick save/load crash by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4163255121"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7374"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7374/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7374">#7374</a></li>

  <li>BACKENDS: Remove EventsBaseBackend by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4240324107"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7418"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7418/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7418">#7418</a></li>

  <li>AGOS: Fix subtitle rendering for Simon II Amiga by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4256763866"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7428"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7428/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7428">#7428</a></li>

  <li>VIDEO: Check validity of granulepos in TheoraVideoTrack::decodePacket by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/prograhamer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/prograhamer">@prograhamer</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4256740288"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7427"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7427/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7427">#7427</a></li>

  <li>GUI: Use Common::SharedPtr for reusing surfaces, and always use simpleBlitFrom
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4234926229"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7416"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7416/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7416">#7416</a></li>

  <li>AUDIO: do not use memset in constructor, disable copy and move by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4264237535"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7430"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7430/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7430">#7430</a></li>

  <li>TETRAEDGE: disable copy/move in C++11 style for PathNode by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4264206769"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7429"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7429/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7429">#7429</a></li>

  <li>GUI: Add Fluid Scrolling Class and Implement Fluid Scrolling in About dialog
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4264952687"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7432"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7432/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7432">#7432</a></li>

  <li>HDB: Support running with different pixel formats, and use faster blitting routines
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4228320131"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7414"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7414/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7414">#7414</a></li>

  <li>HPL1: Simplify texture format handling by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4234514436"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7415"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7415/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7415">#7415</a></li>

  <li>STARK: Fix dialog aspect ratio by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4270531085"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7434"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7434/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7434">#7434</a></li>

  <li>MM: Fix MM1 enhanced combat mouse hit detection by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4217540798"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7410"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7410/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7410">#7410</a></li>

  <li>DOCS: Add description of engine options for GLK by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Priyanshu3820/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4248171381"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7422"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7422/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7422">#7422</a></li>

  <li>GRIM: Clear controls state after resuming from paused state by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4244578659"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7421"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7421/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7421">#7421</a></li>

  <li>BOLT: Add detection entries for additional Funhouse games by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/beholdnec/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/beholdnec">@beholdnec</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4272903811"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7435"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7435/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7435">#7435</a></li>

  <li>SCI: Improve pixel format selection for AVI and QuickTime videos by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4208296097"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7400"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7400/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7400">#7400</a></li>

  <li>AGOS: Support for FR/DE Elvira Atari ST music. by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4277026773"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7437"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7437/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7437">#7437</a></li>

  <li>AGOS: Fix window height for Amiga PN intro by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4285741870"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7441"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7441/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7441">#7441</a></li>

  <li>DIRECTOR: Fixes for Mission to Planet X by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4278056271"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7438"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7438/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7438">#7438</a></li>

  <li>COMMON: Implement entities parsing in the XML parser by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4289238065"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7445"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7445/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7445">#7445</a></li>

  <li>AD: Skip detection for engines with no matching filenames by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mikrosk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4273465646"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7436"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7436/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7436">#7436</a></li>

  <li>DIRECTOR: DT: Add Filmloop score viewer by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4289232514"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7444"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7444/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7444">#7444</a></li>

  <li>AUDIO: Introduce print_rate by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4140032683"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7365"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7365/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7365">#7365</a></li>

  <li>ACCESS: enable savestate metadata (timestamp &amp; playtime) by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/vorph999/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/vorph999">@vorph999</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4081685174"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7324"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7324/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7324">#7324</a></li>

  <li>AVALANCHE: Added an outro for quit option for Lord Avalot d''Argent by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/YengHer919/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/YengHer919">@YengHer919</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4156234263"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7371"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7371/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7371">#7371</a></li>

  <li>GUI: Add Fluid scrolling in List, Grid, Richtext, Scroll Container widgets by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4297080568"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7450"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7450/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7450">#7450</a></li>

  <li>STARK: Fix dialog buttons width by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4298500510"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7453"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7453/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7453">#7453</a></li>

  <li>AUDIO: Introduce DISABLE_MAME_OPL by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4303564297"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7455"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7455/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7455">#7455</a></li>

  <li>SCUMM: ZAK: Fix sound 49 in C64 version by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/M3wP/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/M3wP">@M3wP</a> in
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4297508255"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7451"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7451/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7451">#7451</a></li>

  <li>AGOS: Implement day/night palette fading for PN Amiga/Atari ST by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4287727900"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7442"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7442/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7442">#7442</a></li>

  <li>DIRECTOR: DT: Add sound castmember audio controls by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4297861474"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7452"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7452/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7452">#7452</a></li>

  <li>DIRECTOR: Fix ImGui cast viewer crash and filmloop animation regression by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4305825278"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7457"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7457/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7457">#7457</a></li>

  <li>VOYEUR: Fix random phone calls not playing by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/antoniou79/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/antoniou79">@antoniou79</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4305871143"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7458"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7458/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7458">#7458</a></li>

  <li>TINSEL: Add support for DW1 PSX Japanese font by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4312411387"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7461"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7461/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7461">#7461</a></li>

  <li>SCI: Add detection for the Hebrew fanmade translation of KQ6 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4311239765"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7460"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7460/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7460">#7460</a></li>

  <li>SCUMM: MONKEY1: Workaround for issue giving room notes to Herman by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4318910729"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7462"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7462/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7462">#7462</a></li>

  <li>AGOS: SIMON1: Remap Amiga CD32 and AGA displayBoxStars color. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4328047051"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7464"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7464/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7464">#7464</a></li>

  <li>AGOS: SIMON2: Correctly detect Mac/Amiga Simon2. Fixes bug #16705 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4328506864"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7466"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7466/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7466">#7466</a></li>

  <li>AGOS: ELVIRA1: Add detection/PRG name for FR Atari ST version. by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4329333916"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7468"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7468/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7468">#7468</a></li>

  <li>CHAMBER: Implement EGA rendering  by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4282360625"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7440"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7440/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7440">#7440</a></li>

  <li>GUI: Don''t close GridItemTray too hastily if mouse is outside of it by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4327924960"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7463"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7463/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7463">#7463</a></li>

  <li>GUI: Don''t redraw all layers when closing tooltip by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/mikrosk/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4250866208"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7426"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7426/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7426">#7426</a></li>

  <li>SDL: Fix bug 16666 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lephilousophe/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4288978642"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7443"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7443/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7443">#7443</a></li>

  <li>BACKENDS: ATARI: Implement plugins by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4289557719"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7446"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7446/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7446">#7446</a></li>

  <li>TOUCHE: Fix uncompletable game on some condition by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Gemba/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Gemba">@Gemba</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4298774823"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7454"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7454/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7454">#7454</a></li>

  <li>NANCY: Fix lathe puzzle sounds by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4331484851"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7470"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7470/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7470">#7470</a></li>

  <li>GOB: add new german Adibou1 variants by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/BJNFNE/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BJNFNE">@BJNFNE</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4331651880"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7471"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7471/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7471">#7471</a></li>

  <li>DIRECTOR: Fix FilmLoop registration offset and minor DT changes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4330533303"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7469"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7469/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7469">#7469</a></li>

  <li>AGOS: SIMON2: Fix Amiga/Mac sounds. Fixes bug #16712 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4334797290"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7472"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7472/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7472">#7472</a></li>

  <li>AGOS: ELVIRA1: Fix Elvira Atari ST driver L0037 behavior Fixes bug #16708 by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4337761659"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7473"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7473/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7473">#7473</a></li>

  <li>DIRECTOR: DT: Add Image and text viewer window by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4339765985"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7475"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7475/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7475">#7475</a></li>

  <li>CHAMBER: Add save/load by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4338568035"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7474"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7474/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7474">#7474</a></li>

  <li>MTROPOLIS: add "Wanna-Be A Dino Finder" to detection by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4346283048"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7477"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7477/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7477">#7477</a></li>

  <li>MTROPOLIS: ignore COPYING.MPL from source tree in main segment search by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4345835632"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7476"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7476/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7476">#7476</a></li>

  <li>DIRECTOR: Fixes for Gus Goes to the Kooky Carnival by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4357825322"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7480"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7480/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7480">#7480</a></li>

  <li>NANCY: Improve MultiBuildPuzzle sounds by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4369807123"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7487"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7487/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7487">#7487</a></li>

  <li>BACKENDS: Restrict direct access to OSystem mouse functions by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4369538123"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7486"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7486/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7486">#7486</a></li>

  <li>ENGINES: Ensure that in-game cursors are scaled on high DPI displays by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4370090333"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7488"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7488/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7488">#7488</a></li>

  <li>GUI: Make OptionsContainerWidget inherit its clipping rectangle by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lephilousophe/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lephilousophe">@lephilousophe</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4368637940"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7484"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7484/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7484">#7484</a></li>

  <li>MM: MM1: Add I18N comments for N and Y keybindings by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4371392747"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7489"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7489/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7489">#7489</a></li>

  <li>CHAMBER: Move splash screen hardcoded filenames to detection flags by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4357395491"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7479"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7479/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7479">#7479</a></li>

  <li>DIRECTOR: Fix In the First Degree demo using \xBC menu separator by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4353760024"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7478"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7478/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7478">#7478</a></li>

  <li>FREESCAPE: Refactor Atari music code to be independent of the YM2149 implementation
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4372413708"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7491"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7491/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7491">#7491</a></li>

  <li>GRAPHICS: MACGUI: Support rendering with any 8/16/32bpp pixel format by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4219853768"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7412"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7412/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7412">#7412</a></li>

  <li>DISTS: Update Sparkle manifest to fix WinSparkle release notes by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/sluicebox/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/sluicebox">@sluicebox</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4380509911"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7493"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7493/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7493">#7493</a></li>

  <li>NANCY: Fix inventory check in early games by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/tunnelsociety/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4381279321"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7495"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7495/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7495">#7495</a></li>

  <li>MM: MM1: resolve global constructors by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4393299456"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7499"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7499/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7499">#7499</a></li>

  <li>Bump mistune from 3.1.4 to 3.2.1 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4411140419"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7502"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7502/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7502">#7502</a></li>

  <li>GUI: Fix ScrollContainerWidget clicks after scrolling by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4409276595"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7501"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7501/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7501">#7501</a></li>

  <li>PSP: Use Graphics::crossBlit for converting unsupported pixel formats by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4242042345"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7419"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7419/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7419">#7419</a></li>

  <li>CONFIGURE: MACOS: Fix TTS &amp; SDK feature checks for Tiger/Leopard by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwatteau/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwatteau">@dwatteau</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4386497023"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7497"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7497/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7497">#7497</a></li>

  <li>SCI: Adding Hebrew Translation For KQ7 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/SegMash/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/SegMash">@SegMash</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4414864520"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7504"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7504/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7504">#7504</a></li>

  <li>NANCY: Add detection for Wii version of nancy16 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4380962080"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7494"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7494/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7494">#7494</a></li>

  <li>Bump urllib3 from 2.6.3 to 2.7.0 in /doc/docportal by <a class="user-mention
  notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4422891324"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7505"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7505/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7505">#7505</a></li>

  <li>Update handling of SDL_MouseWheelEvent by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/criezy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/criezy">@criezy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4424929627"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7506"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7506/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7506">#7506</a></li>

  <li>DIRECTOR: LINGO: Skip D6 mixed compare guard for location lookups by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lotharsm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lotharsm">@lotharsm</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4364055904"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7483"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7483/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7483">#7483</a></li>

  <li>AGOS: Fix issue with detection order for Simon 2. Fixes bug #16803 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/robertmegone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/robertmegone">@robertmegone</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4444417840"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7512"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7512/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7512">#7512</a></li>

  <li>GUI: Possible fix for bug #16698, where launcher searches looked like they were
  empty by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/eriktorbjorn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/eriktorbjorn">@eriktorbjorn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4443573597"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7511"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7511/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7511">#7511</a></li>

  <li>GOB: Fix memory leak in Inter_v7::o7_checkData by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ripleyXLR8/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ripleyXLR8">@ripleyXLR8</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4447181519"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7513"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7513/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7513">#7513</a></li>

  <li>SCUMM: Don''t pack fonts &lt; 8bpp by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4428364320"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7508"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7508/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7508">#7508</a></li>

  <li>TEST: Update to cxxtest-4.4 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/OMGPizzaGuy/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4434851166"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7509"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7509/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7509">#7509</a></li>

  <li>DIRECTOR: Fixes for Rodney''s Funscreen by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4448548086"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7514"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7514/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7514">#7514</a></li>

  <li>Bump idna from 3.11 to 3.15 in /doc/docportal by <a class="user-mention notranslate"
  data-hovercard-type="organization" data-hovercard-url="/orgs/dependabot/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dependabot">@dependabot</a>[bot]
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4481319996"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7520"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7520/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7520">#7520</a></li>

  <li>NANCY: Fix TBOX reader for Nancy 10+ conversation font IDs by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dukiverse/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dukiverse">@Dukiverse</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4492471200"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7524"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7524/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7524">#7524</a></li>

  <li>NANCY: Initial work on the conversation popup for Nancy 10+ by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dukiverse/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dukiverse">@Dukiverse</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4492471807"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7525"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7525/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7525">#7525</a></li>

  <li>ACCESS: Add support for Noctropolis by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mduggan/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mduggan">@mduggan</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4459136308"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7515"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7515/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7515">#7515</a></li>

  <li>PRINCE: Support hebrew translation by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BLooperZ/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BLooperZ">@BLooperZ</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4472559961"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7519"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7519/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7519">#7519</a></li>

  <li>PS3: Add support for launching engines as separate modules by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/aquadran/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aquadran">@aquadran</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4488273103"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7522"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7522/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7522">#7522</a></li>

  <li>GUI: Fix bugs introduced by FluidScroll by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4512552823"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7527"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7527/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7527">#7527</a></li>

  <li>JANITORIAL: ACCESS: resolve shadowing of function argument by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4514482573"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7528"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7528/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7528">#7528</a></li>

  <li>COLONY: Use a more universally supported OpenGL texture format by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4385474425"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7496"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7496/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7496">#7496</a></li>

  <li>ACCESS: replace int16 arrays with Common::Point by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4553597692"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7536"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7536/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7536">#7536</a></li>

  <li>GLK: SCOTT: Add ZX Spectrum TAP/TZX loading by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ShadowMaker/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ShadowMaker">@ShadowMaker</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4521872779"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7533"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7533/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7533">#7533</a></li>

  <li>JANITORIAL: ACCESS: remove struct keyword usages by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4554067672"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7537"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7537/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7537">#7537</a></li>

  <li>JANITORIAL: GLK: pass strings as references by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/meekee7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/meekee7">@meekee7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4554256787"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7538"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7538/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7538">#7538</a></li>

  <li>CHAMBER: Fix EGA rendering, performance and input handling bugs by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/11-andy-11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4518159882"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7530"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7530/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7530">#7530</a></li>

  <li>GLK: Fix saved font selection handling by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ShadowMaker/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ShadowMaker">@ShadowMaker</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4519128750"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7531"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7531/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7531">#7531</a></li>

  <li>TEST: Make cxxtest main and various printers not depend on std by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/OMGPizzaGuy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/OMGPizzaGuy">@OMGPizzaGuy</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4499774134"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7526"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7526/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7526">#7526</a></li>

  <li>GLK: SCOTT: Fix C64 detection buffer ownership by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ShadowMaker/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ShadowMaker">@ShadowMaker</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4554495370"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7539"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7539/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7539">#7539</a></li>

  <li>N64: Support returning errors when switching to unsupported resolutions by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4373209192"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7492"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7492/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7492">#7492</a></li>

  <li>DM: Fix various crashes and Implement EventManager::highlightScreenBox() by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4563696058"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7541"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7541/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7541">#7541</a></li>

  <li>DIRECTOR: Fixes for Opera Fatal by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/moralrecordings/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4565044154"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7542"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7542/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7542">#7542</a></li>

  <li>SCUMM: RA: add more RA1 hashes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mlauss2/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mlauss2">@mlauss2</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4571950499"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7545"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7545/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7545">#7545</a></li>

  <li>SCUMM: RA: Default framerate is 15fps by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mlauss2/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mlauss2">@mlauss2</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4573271394"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7546"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7546/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7546">#7546</a></li>

  <li>NANCY: Add detection for Nancy 10 variants by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4569239116"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7544"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7544/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7544">#7544</a></li>

  <li>SCUMM: RA: support female voice output by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mlauss2/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mlauss2">@mlauss2</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4573621630"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7547"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7547/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7547">#7547</a></li>

  <li>SCUMM: RA: add codec4/5 post processing by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mlauss2/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mlauss2">@mlauss2</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4578145712"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7549"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7549/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7549">#7549</a></li>

  <li>DIRECTOR: DT: Fix bugs and crashes throughout the visual debugger by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4583665028"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7553"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7553/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7553">#7553</a></li>

  <li>MM: MM1: Fix stale view close handling, crash in spells and text fix by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4581189408"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7550"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7550/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7550">#7550</a></li>

  <li>DM: Resolve various PVS-Studio Warnings by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/mohitbankar/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mohitbankar">@mohitbankar</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4591033211"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7556"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7556/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7556">#7556</a></li>

  <li>DIRECTOR: Make Elroy Hits the Pavement fully playable by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/zberry92/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zberry92">@zberry92</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4520282492"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7532"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7532/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7532">#7532</a></li>

  <li>MM: MM1: Add classic PC speaker sounds by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4599802213"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7559"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7559/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7559">#7559</a></li>

  <li>MM: MM1: Fix classic combat target crashes by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4599686066"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7558"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7558/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7558">#7558</a></li>

  <li>FREESCAPE: add ZX Spectrum tape support by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ShadowMaker/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ShadowMaker">@ShadowMaker</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4577796916"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7548"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7548/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7548">#7548</a></li>

  <li>DIRECTOR: fix empty cast slot error and immediate sprite drag in D4+ by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4606405042"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7563"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7563/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7563">#7563</a></li>

  <li>AGS: Detection, initial support for Gobliiins 5 from Gobliiins Collection (Switch)
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/einstein95/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/einstein95">@einstein95</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4595096333"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7557"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7557/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7557">#7557</a></li>

  <li>DIRECTOR: DT: improve search and add Windows panel by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4606588725"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7564"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7564/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7564">#7564</a></li>

  <li>BOLT: Split out game code into their own folders by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/beholdnec/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/beholdnec">@beholdnec</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4289787400"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7447"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7447/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7447">#7447</a></li>

  <li>DIRECTOR: Fix Elroy Hits the Pavement Map Previews by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/zberry92/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zberry92">@zberry92</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4603843734"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7560"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7560/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7560">#7560</a></li>

  <li>DIRECTOR: Fix MIAW pause isolation, FileIO append, RNG seeding, and cast member
  check by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/zberry92/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zberry92">@zberry92</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604060832"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7561"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7561/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7561">#7561</a></li>

  <li>MOHAWK: Sound fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Alstruit/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Alstruit">@Alstruit</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4627859745"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7568"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7568/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7568">#7568</a></li>

  <li>PHOENIXVR: Improve fonts, video compatibility, detection, and save rooms by
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4644390218"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7569"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7569/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7569">#7569</a></li>

  <li>PHOENIXVR: Add subtitle support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4647575138"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7570"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7570/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7570">#7570</a></li>

  <li>MOHAWK: LB - Cleanup by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Alstruit/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Alstruit">@Alstruit</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4655157552"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7571"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7571/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7571">#7571</a></li>

  <li>TWP: Remove time.h dependency by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/scemino/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/scemino">@scemino</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604863371"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7562"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7562/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7562">#7562</a></li>

  <li>CHAMBER: Bug fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/11-andy-11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/11-andy-11">@11-andy-11</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4614421748"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7566"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7566/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7566">#7566</a></li>

  <li>SCUMM: Optimised code paths by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mikrosk/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mikrosk">@mikrosk</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4095100825"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7330"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7330/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7330">#7330</a></li>

  <li>GRAPHICS: Replace use of createPixelFormat for non-ColorMask purposes by <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3157762525"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/6737"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/6737/hovercard"
  href="https://github.com/scummvm/scummvm/pull/6737">#6737</a></li>

  <li>WII: Fully implement conversion for unsupported pixel formats by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4208762486"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7401"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7401/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7401">#7401</a></li>

  <li>COMMON: Remove implicit comparison between String and U32String by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4214497060"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7407"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7407/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7407">#7407</a></li>

  <li>webOS: add 64-bit compile by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/cscd98/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cscd98">@cscd98</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4554532141"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7540"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7540/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7540">#7540</a></li>

  <li>AUDIO: Separate generating sine waves from the PC Speaker code by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4583970830"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7554"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7554/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7554">#7554</a></li>

  <li>MORPHOS: Enet support by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BeWorld2018/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BeWorld2018">@BeWorld2018</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4658605335"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7573"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7573/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7573">#7573</a></li>

  <li>BACKENDS: MORPHOS: rework backend by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/BeWorld2018/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/BeWorld2018">@BeWorld2018</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4664699306"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7575"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7575/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7575">#7575</a></li>

  <li>PHOENIXVR: Add support for Dracula 1 and 2 by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Scorpeg/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Scorpeg">@Scorpeg</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4669327927"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7578"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7578/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7578">#7578</a></li>

  <li>DIRECTOR: DT: Improve cast details, add script browser navigation and keyboard
  shortcuts by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ramyak-sharma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ramyak-sharma">@ramyak-sharma</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4669232667"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7577"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7577/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7577">#7577</a></li>

  <li>DIRECTOR: Fixes for Yellow Brick Road by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4675589417"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7579"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7579/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7579">#7579</a></li>

  <li>DIRECTOR: Savegame fixes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Lariaa/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Lariaa">@Lariaa</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4676316634"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7580"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7580/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7580">#7580</a></li>

  <li>CONFIGURE: Disable SEQ MIDI on FreeBSD and DragonFlyBSD by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/tunnelsociety/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tunnelsociety">@tunnelsociety</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4695025456"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7582"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7582/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7582">#7582</a></li>

  <li>DIRECTOR: Fixes for Yellow Brick Road by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/moralrecordings/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/moralrecordings">@moralrecordings</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4703770722"
  data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7587"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7587/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7587">#7587</a></li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/anttt194/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/anttt194">@anttt194</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4163710404" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7377"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7377/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7377">#7377</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MarTCM/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MarTCM">@MarTCM</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4200641457" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7389"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7389/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7389">#7389</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Priyanshu3820/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Priyanshu3820">@Priyanshu3820</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4164950903" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7378"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7378/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7378">#7378</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/bleggett/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/bleggett">@bleggett</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4249275514" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7425"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7425/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7425">#7425</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/prograhamer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/prograhamer">@prograhamer</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4256740288" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7427"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7427/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7427">#7427</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/beholdnec/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/beholdnec">@beholdnec</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4272903811" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7435"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7435/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7435">#7435</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/vorph999/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/vorph999">@vorph999</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4081685174" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7324"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7324/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7324">#7324</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/YengHer919/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/YengHer919">@YengHer919</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4156234263" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7371"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7371/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7371">#7371</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/M3wP/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/M3wP">@M3wP</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4297508255" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7451"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7451/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7451">#7451</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Gemba/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Gemba">@Gemba</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4298774823" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7454"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7454/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7454">#7454</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ripleyXLR8/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ripleyXLR8">@ripleyXLR8</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4447181519" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7513"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7513/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7513">#7513</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dukiverse/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dukiverse">@Dukiverse</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4492471200" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7524"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7524/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7524">#7524</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ShadowMaker/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ShadowMaker">@ShadowMaker</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4521872779" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7533"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7533/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7533">#7533</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mlauss2/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mlauss2">@mlauss2</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4571950499" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7545"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7545/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7545">#7545</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/zberry92/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zberry92">@zberry92</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4520282492" data-permission-text="Title is private" data-url="https://github.com/scummvm/scummvm/issues/7532"
  data-hovercard-type="pull_request" data-hovercard-url="/scummvm/scummvm/pull/7532/hovercard"
  href="https://github.com/scummvm/scummvm/pull/7532">#7532</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/scummvm/scummvm/compare/v2026.2.0...v2026.3.0"><tt>v2026.2.0...v2026.3.0</tt></a></p>'
updated: '2026-06-20T21:03:57Z'
version: v2026.3.0
version_title: 'ScummVM 2026.3.0: "Carousels & Killer Whales"'
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

