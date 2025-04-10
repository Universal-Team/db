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
  noisecmdr-v0_0_13-demo.cia:
    size: 2294720
    size_str: 2 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.0.13/noisecmdr-v0_0_13-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_0_13-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_0_13-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 0
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h2 dir="auto">0.0.13</h2>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Ability to start/stop playback by pressing the START button (play current row
  when in clipmatrix view)</li>

  <li>Doubled Master- and bus-effects so each deck has their own - uses more CPU</li>

  <li>Decks can be disabled in DJ-Mixer view to allow reducing CPU usage temporarily</li>

  <li>Decks are initially disabled until the user starts playack</li>

  <li>Rudimentary playlist functionality in twin-file browser

  <ul dir="auto">

  <li>Press X and choose "New Playlist" in menu</li>

  <li>With an *.nsm file highlighted, press X again and choose either "Copy" or "Add
  to Playlist"</li>

  <li>Hold A + C-Pad Up/Down to re-order items inside the playlist</li>

  <li>Press Select to cycle the panel-view-types: FILES -&gt; PLAYLIST -&gt; SAMPLES
  (not implemented yet)</li>

  <li>Press A to load a song to the current deck as usual</li>

  <li>Press B to exit back to files mode and show the "/nc/playlists" directory</li>

  <li>The current playlist selection is persists, remembered during next app launch</li>

  </ul>

  </li>

  <li>Browser: Visual scroll-bars appear in long lists to indicate paging is possible
  (press L/R to page)</li>

  <li>Browser: Pressing Y toggles deck selection</li>

  <li>Browser: new functions: Dulicate, Rename, Create directory, Jump to opposite
  dir</li>

  <li>Browser: The operations above support multi-selection but currently directories
  cannot be deleted or copied</li>

  <li>Browser: Multiple rows can be selected by holding X and moving the circle-pad
  up/down</li>

  <li>Header shows current deck''s'' loaded file name now</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Doubled Master- and bus-effects so each deck has their own - uses more CPU</li>

  <li>Toggling display in clipmatrix has been re-assigned to the L button</li>

  <li>The right-hand status column now shows the currently playing row of track 1</li>

  <li>Audio init error now shows instructions on dumping DSP firmware to fix it</li>

  <li>Browser: Switching side with circle-pad left/right now</li>

  <li>Browser: Cursor now stays in position when paging with L/R fore more comfort</li>

  <li>Browser: Pressing A when a .lst (playlist) file is selected opens it (switching
  to PLAYLIST panel type)</li>

  <li>Browser: Copying large files is now slightly faster</li>

  <li>Browser: Shows warning when attempting to load song into deck which it playing
  and audible (crossfader not off)</li>

  </ul>

  <h3 dir="auto">Removed</h3>

  <ul dir="auto">

  <li>Opening a project or creating a project no longer auto-plays the deck (must
  press Start now)</li>

  <li>Start button no longer cycles pages in instrument view, use B+Circle pad instead.</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>DJMixer view: Both "Deck Gain" sliders affect only the selected deck instead
  of respective side</li>

  </ul>'
updated: '2025-04-10T10:55:56Z'
version: 0.0.13
version_title: Effects per deck, start/stop button, playlists and browser upgrades
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
