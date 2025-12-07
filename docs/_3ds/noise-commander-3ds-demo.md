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
downloads:
  noisecmdr-v0_1_7-demo.cia:
    size: 3265472
    size_str: 3 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.1.7/noisecmdr-v0_1_7-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_1_7-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_1_7-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 1
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Column-header bus-color-coding in tracker-view and clipmatrix-view</li>

  <li>User may alter 16-color-palette by adding a "/nc/colors.cfg" file with one RGB
  value pair per line:<br>

  (example:) 0 50 128</li>

  <li>The colors.cfg file can be created by pressing the "Sv Clr File" button in the
  general settings</li>

  <li>Can now edit instruments in browser (delete, rename, duplicate)</li>

  <li>"Auto Sync Selection" setting in browser: Selects instrument/sample when pressing
  a pad</li>

  <li>"Auto Assign" setting in browser: Assigns the selected sample to current instrument<br>

  or the selected instrument to the current pad while browsing.</li>

  <li>Press X when in either the samples- or instrument-list to show the toggleable
  settings</li>

  <li>"Randomize values" function in tracker-menu: mutates existing values by given
  percentage</li>

  <li>Pressing X in splash-screen shows recent files</li>

  <li>"Duplicate Repeatedly" function in tracker-menu</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Wav-header loop points are now applied to instrument every time a sample-number
  is assigned</li>

  <li>Unique random names are assigned to microphone/looper recorded samlpes</li>

  <li>The browser settings "Preview", "Sync Selection" and "Auto Assign" are now persistent</li>

  <li>The last selection mode is now remembered ("cursor"/"row") in tracker/matrix
  view</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Bus/master automation has no effect while a track is soloed</li>

  <li>Crash when truncating sample in waveform view</li>

  </ul>

  <h3 dir="auto">Removed</h3>

  <ul dir="auto">

  <li>"Insert Note Stops" function from tracker-menu (seemed broken, needs investigating)</li>

  </ul>'
updated: '2025-12-07T10:12:49Z'
version: 0.1.7
version_title: New browser features
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
