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
  noisecmdr-v0_1_3-demo.cia:
    size: 3240896
    size_str: 3 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.1.3/noisecmdr-v0_1_3-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_1_3-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_1_3-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 1
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h1 dir="auto">0.1.3</h1>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Ability to connect and synchronize multiple 3DS consoles via local "multiplayer"
  Wifi (UDS)

  <ul dir="auto">

  <li>Starting or re-starting playback on the host will also restart playback on the
  connected clients</li>

  <li>The switches are in the General Settings (press down and tap the "General" tab)</li>

  <li>Note that normal Wifi-features (Browser-upload) is not possible while UDS is
  active</li>

  </ul>

  </li>

  <li>"Neutral Preview" setting in preferences causes browser to play samples at original
  rate (default: on)</li>

  <li>New Piano Buttons:

  <ul dir="auto">

  <li>"Gated" toggles whether lifting stops the note and sets the instrument playmode</li>

  <li>"Slide" allows pressing keys by sliding the stylus, else it needs to be lifted</li>

  <li>"Off" is a shortcut for stopping current sound and recording/inserting an note-off</li>

  </ul>

  </li>

  <li>Columns for fold distortion enable, width and gain</li>

  <li>Tempo Dialog: left/right buttons nudge playhead by one step to adjust phase
  with external audio (e.g. other 3DS)</li>

  <li>REC toggle in Bus-FX view</li>

  <li>New Tracker/Bus-FX screen combo (press right three times) for inserting slider-automation
  visually</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Retrig-column uses slice-positions now (i.e. works in combination)</li>

  <li>Repeat mode in drum-view now uses last slice-position. Nice in combination with
  linear slice trigs</li>

  <li>Enabling Right-channel-click-track disables stereo-widening effect</li>

  <li>Piano key background color now changes while pressed</li>

  <li>Fold-width (distortion) range now allows better articulation</li>

  <li>Brought pitch envelope back and added columns for animation</li>

  <li>Motion recording ability for most sliders in Bus-FX screen</li>

  <li>"Mono to stereo" settings are now preserved</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Shifting notes with A+Up intermittently not working</li>

  <li>Playback position is no longer shown in Waveform-view after pressing A</li>

  <li>Memory-alignment crash when resampling (only happened with -O3 i.e. in release)</li>

  </ul>'
updated: '2025-09-21T12:56:23Z'
version: 0.1.3
version_title: Lots of small stuff
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
