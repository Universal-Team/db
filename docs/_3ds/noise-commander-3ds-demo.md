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
  noisecmdr-v0_0_10-demo.cia:
    size: 2360256
    size_str: 2 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.0.10/noisecmdr-v0_0_10-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_0_10-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_0_10-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 0
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h2 dir="auto">0.0.10</h2>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Per-bus probability setting ("BChance" in Bus-FX view)</li>

  <li>Per-lane probability setting ("LnChance" in tracker bottome companion view)</li>

  <li>Per-note probability setting in tracker companion screen (Percentage column)

  <ul dir="auto">

  <li>If the first hex digit is zero then the second number represents a percentage
  (1=10%, 5=50% etc.)</li>

  <li>0F ("First") is a one-off trigger, only fired when the phrase plays for the
  first time</li>

  <li>If the first hex digit is non-zero then the trigger occurs every nth out of
  x times (x being the second digit)

  <ul dir="auto">

  <li>e.g. "14" plays every first out of four times and so forth (the maximum is 8/8)</li>

  </ul>

  </li>

  </ul>

  </li>

  <li>Splash screen</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Removed automatic insertion of note length in tracker editor</li>

  <li>Files are now sorted alphabetically in browsers</li>

  <li>The phrase length now updates to the total length of the four euclideans whenever
  a value is changed</li>

  <li>Added dynamic length toggle ("Len") button to second page in euclidean view
  (off by default)

  <ul dir="auto">

  <li>When enabled, the clip length is set to the total euclidean length whenever
  a value is changed</li>

  </ul>

  </li>

  <li>The "All", "Bus" and "Selected" lane mode buttons now behave as mutually exclusive
  radio buttons</li>

  <li>The Y-button now resets the selected parameter in instrument view</li>

  <li>A unique instrument is assigned to each lane''s first clip when creating a new
  project</li>

  <li>Default template is created by code when no template.nsm file is found</li>

  <li>Follow- and narrow modes are now initially active by default in tracker view</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Deleting notes by holding L+Pad was broken</li>

  <li>Reverb-tail never ends due to fixed-point math (replaced with float for fix)</li>

  <li>Instruments not duplicated by "Duplicate Uniquely" if instrument column is empty
  in matrix view</li>

  <li>Note with no volume value should play at full level but was quieter (64 instead
  of 0x64)</li>

  </ul>'
updated: '2025-01-06T19:31:23Z'
version: 0.0.10
version_title: First submission to universal-db
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
