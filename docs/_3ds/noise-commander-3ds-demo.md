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
  noisecmdr-v0_1_4-demo.cia:
    size: 3244992
    size_str: 3 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.1.4/noisecmdr-v0_1_4-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_1_4-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_1_4-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 1
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h1 dir="auto">0.1.4</h1>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Renamed "Gated" to "Hold" in piano and de-coupled the setting from drum pads.
  Hold is off per default.</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Creating empty clip assigns instrument 255 (Can now insert new row number without
  losing instrument)</li>

  <li>Pad-view does not refresh instr labels when new row plays</li>

  <li>Capturing loop to song in Factotum looper always copies only one bar when set
  to two</li>

  <li>Set fade default value to 16 in Factotum looper to avoid pops at boundary</li>

  <li>Pitch envelope amount not applied when selecting instrument</li>

  <li>Tapping "Sub-Tab" button (2nd from left at bottom in drum-pad view) does not
  toggle to previous sub-tab</li>

  <li>Stopping of transport not transmitted when connected via UDS</li>

  <li>Current slice-number not stored in song-file and lost at reload</li>

  </ul>'
updated: '2025-10-05T15:08:11Z'
version: 0.1.4
version_title: Bug fixes
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
