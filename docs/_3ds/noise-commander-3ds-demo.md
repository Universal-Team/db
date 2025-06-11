---
author: gearmo3ds
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/156527942?v=4
categories:
- app
color: '#856d28'
color_bg: '#806826'
created: '2025-01-06T19:04:39Z'
description: Beat-making audio sequencer and DJ-tool for the Nintendo 3DS
download_page: https://github.com/gearmo3ds/noisecommander3dsdemo/releases
downloads: {}
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 1
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h2 dir="auto">0.0.15</h2>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Pads show current instrument number in lower right corner</li>

  <li>New generic "set length" dialog for changing current phrase- and clip-lengths</li>

  <li>New tracker-view hotkey Y+X - shows "set phrase-length" dialog</li>

  <li>New clipmatrix-view hotkey Y+X - shows "set clip-length" dialog</li>

  <li>New tracker hotkey: Y + C-Pad for paging up/down by 16 steps or jump to top/bottom</li>

  <li>Large status-icon displays deck''s playing, looping or stopped state</li>

  <li>B + D-Right as an alternative way to start an entire row in clipmatrix-view
  to double tapping A</li>

  <li>"Set Lengths" menu item in clipmatrix view assigns length to all twelve row-cells
  at once</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Assigning a pitch value to an instrument sets num-beats to zero, otherwise the
  pitch may change unexpectedly later</li>

  <li>Muting lane via B + Pad now works in tracker- and clipmatrix widgets too</li>

  <li>Swing amount is now per deck instead of global (current was disturbingly changing
  when loading new song)</li>

  <li>Volumes are adjusted when loading files from versions before 0.0.14 but the
  levels still sound quite different</li>

  <li>Piano octave-setting no longer affects drum pads</li>

  <li>Default volume is now 70 instead of 50</li>

  <li>Instrument number is shown in hex in instrument-view to be consistent with tracker
  columns</li>

  <li>Tracker-operations now work in clipmatrix too: shift cell selection w. A+up/down,
  select above/below w. X+up/down</li>

  <li>Select button now toggles "row-loop" mode in tracker view too</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Pressing START sometimes plays random clip row - it should play selected clip
  row</li>

  <li>Cross-fading exports sample (forgot to un-comment)</li>

  <li>No instrument number inserted with linear slice notes menu-function</li>

  <li>Some instrument parameters are not reset when creating new project (loopEnabled)</li>

  <li>"Reload" and "Reload Seq" in project view causes app to freeze</li>

  <li>Pressing A to disable follow mode while deck is not playing leads to confusing
  behavior (cursor stays locked)</li>

  </ul>

  <h3 dir="auto">Removed</h3>

  <ul dir="auto">

  <li>Removed shortcuts which re-order lanes as they don''t work as intended (A+D-Left/D-Right)</li>

  <li>Hid shortcuts from tracker/clipmatrix menus as they aren''t functional</li>

  <li>Removed "Rotate" menu item from clipmatrix menu</li>

  </ul>'
updated: '2025-06-04T14:18:50Z'
version: 0.0.15
version_title: Bugfixes
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
