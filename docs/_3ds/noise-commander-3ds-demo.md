---
author: gearmo3ds
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/156527942?v=4
categories:
- app
color: '#856d28'
color_bg: '#806826'
created: '2025-01-06T19:04:39Z'
description: Beat-making audio sequencer and DJ-tool for the 3DS
download_page: https://github.com/gearmo3ds/noisecommander3dsdemo/releases
downloads:
  noisecmdr-v0_0_11-demo.cia:
    size: 2393024
    size_str: 2 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.0.11/noisecmdr-v0_0_11-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_0_11-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_0_11-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 0
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h2 dir="auto">0.0.11</h2>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Current octave is displayed in right-side status column</li>

  <li>B + Y inserts a hard note off value (in contrast A + B changes the note length
  to current row)</li>

  <li>"Tune to C" button in instrument view - simple zero-crossing method, sometimes
  off by one note - not perfect</li>

  <li>Pop-up dialog for downloading demo-samples appears at startup if the samples
  directory is empty</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Changed initial reverb default value from 10 to 0</li>

  <li>Matrix view displays phrase numbers in hex now and coarse edits offsets by 16</li>

  <li>Renamed "Pattern Settings" screen to "Mono to Stereo Settings" and remove redundant
  controls</li>

  <li>Hid obsolete Grid-Editor view and replaced "Assign" button with "Randomize all
  samples" button</li>

  <li>Double tapping A shortcut for row-launching in clip-matrix view</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Shifting single note row with A+DPAD UP/DOWN does not work without selection
  sometimes</li>

  <li>Row lengths don''t update when inserting or removing row in matrix view</li>

  <li>Bus-numbers display range started at zero, now starts a one</li>

  <li>Notes are still played when erasing notes with L + Pad</li>

  <li>Clearing a pattern un-assigns samples from instruments</li>

  <li>Avoid handing reserved sample, pattern or instrument with zero index to the
  user (adjusted related functions in code)</li>

  <li>Wrong tempo value shown in tempo-dialog</li>

  </ul>'
updated: '2025-02-01T11:09:49Z'
version: 0.0.11
version_title: 0.0.11
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
