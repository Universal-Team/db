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
  noisecmdr-v0_1_0-demo.cia:
    size: 3228608
    size_str: 3 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.1.0/noisecmdr-v0_1_0-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_1_0-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_1_0-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 1
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>WiFi-Midi support via DSMI and custom VST3 plugin made with Juce

  <ul dir="auto">

  <li>Supports note-, control-change and program-change events (no clock nor sysex)</li>

  <li>User needs to compile and install either <a href="https://github.com/gearmo3ds/dsmi">DSMI</a>
  or the <a href="https://github.com/gearmo3ds/NoiseCommander3DSMidi">Juce VST3 plugin</a></li>

  <li>When using DSMI you''ll need to disable and enable midi in the settings to send
  a discovery signal</li>

  <li>When using the VST3, click on "Discover 3DS" and then press/tap "Discover VST3
  Server" in NC

  <ul dir="auto">

  <li>It should find the right ip-address after a couple seconds. If not, the addresses
  can be manually be set in both sides</li>

  </ul>

  </li>

  <li>Caveat: NC has a fixed audio latencty of 43ms. Midi out events are delayed by
  this amount to stay in sync</li>

  <li>Program changes are only sent when the value changed, equal values and are not
  sent repeatedly but only once</li>

  </ul>

  </li>

  <li>A midi-channel 1-16 can now be selected for each lane (0 means disabled) and
  the setting persists within the song file</li>

  <li>Midi note-on events use the instrument volume value as velocity</li>

  <li>Five Midi CC lanes for sending messages to external gear (hidden by default,
  unhide in column menu B+DLeft in tracker view)</li>

  <li>New "midi.cfg" file allows configuring up to 10 CCs for up to 10 midi out devices
  via text</li>

  <li>The first five Midi CCs can be configured in the Midi Settings UI</li>

  <li>"Fill to clip length" option in tracker menu and "Fill" in set length dialog</li>

  <li>New "Delay" column in lane allows for "micro-timing", delays note and overwrites
  swing delay for the given note</li>

  <li>New "Retrig" column: Repeats note x times or if &gt;= 0x20 then digits are amount
  and number of steps (use for triplets)</li>

  <li>New "BusNr" column to animate the bus-output assignment</li>

  <li>"Set content length" in tracker menu shows the assigned shortcut (B + D-Left)</li>

  <li>Rotary sliders for quick insertion of row-values (volume, probability, repeats
  etc.)</li>

  <li>16 Levels screen: Each pad plays current instrument at different volume</li>

  <li>Repeat screen: Plays held pad repeatedly, pressing D-Pad while held changes
  frequency</li>

  <li>Notes screen: Each pad plays a fixed note (may offer different scales in the
  future here)</li>

  <li>"Dedupe All Instruments" entry in clip-matrix menu, collapses duplicate instruments
  to one</li>

  <li>New buttons for managing column visibility: Show used, all, none, default</li>

  <li>"Delete" menu entry in instrument palette, deletes instrument and clears palette
  slot</li>

  <li>Looper: "xfade" slider cross-fades between dry and wet</li>

  <li>Looper: "Synced" button starts recording at next bar and stops after 1 or 2
  bars (according to "bars" setting)</li>

  <li>Looper: "bars" setting allows up to two bars if the tempo is greater or equal
  to 88 BPM, else only one bar (512k limit)</li>

  <li>Looper: "Automix" toggle sets dry when starting recording and wet when recording
  finishes</li>

  <li>Looper: "Overdub" toggle - does what you expect</li>

  <li>Looper: Momentary "Reverse" button</li>

  <li>Looper: Rate slider resets when releasing to allow performing a a tape stop
  effect of sorts</li>

  <li>Looper: "Capture" saves the loop sample into the song as new instrument (Disabled
  in Demo version)</li>

  <li>Renamed bottom right button label from "Select/Play" to "Silent" in pad/performance
  view for clarity</li>

  <li>Quantization slider in general settings for changing all lanes at once (temporary
  solution)</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Partly new color scheme, thanks to Keffu for submitting/suggesting</li>

  <li>New functions in help: Pressing X shows Shortcuts list for current upper view
  and pressing Y for current lower view</li>

  <li>Pressing Select in help view toggles "Auto-Show" mode which jumps to the upper
  screens shortcut list whenever help is opened</li>

  <li>Empty pads show black color in instrument palette, all but first are now initialized
  as empty</li>

  <li>Tracker lanes now show the phrase- and clip lengths at the bottom</li>

  <li>Copy/pasting single notes with the B-button in compact tracker-view now copies
  all row values</li>

  <li>Increasing phrase length also grows clip length but not the other way around
  (does not shrink)</li>

  <li>Column visibilities now persist, stored in file</li>

  <li>D-Pad functions now repeat when held in help view</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Copy/paste operations exclude columns other than note in narrow/compact tracker
  view mode</li>

  <li>Note-stops turn into notes when transposing selection by holding B+C-Pad direction</li>

  <li>Menu no longer opens after inserting a note-stop with B + Y</li>

  <li>Waveform display now supports 8Bit samples</li>

  </ul>

  <h3 dir="auto">Removed</h3>

  <ul dir="auto">

  <li>"Set Lenghts" menu entry from clip-matrix menu as it seems broken</li>

  </ul>'
updated: '2025-07-27T11:12:46Z'
version: 0.1.0
version_title: Wifi-Midi via VST, looper upgrades and more
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
