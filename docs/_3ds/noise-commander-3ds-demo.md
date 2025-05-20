---
author: gearmo3ds
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/156527942?v=4
categories:
- app
created: '2025-01-06T19:04:39Z'
description: Beat-making audio sequencer and DJ-tool for the Nintendo 3DS
download_page: https://github.com/gearmo3ds/noisecommander3dsdemo/releases
downloads:
  noisecmdr-v0_0_14-demo.cia:
    size: 2495424
    size_str: 2 MiB
    url: https://github.com/gearmo3ds/noisecommander3dsdemo/releases/download/0.0.14/noisecmdr-v0_0_14-demo.cia
github: gearmo3ds/noisecommander3dsdemo
icon: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/icon.png
image: https://raw.githubusercontent.com/gearmo3ds/noisecommander3dsdemo/master/banner.png
image_length: 40664
layout: app
qr:
  noisecmdr-v0_0_14-demo.cia: https://db.universal-team.net/assets/images/qr/noisecmdr-v0_0_14-demo-cia.png
source: https://github.com/gearmo3ds/noisecommander3dsdemo
stars: 1
systems:
- 3DS
title: Noise Commander 3DS (Demo)
update_notes: '<h2 dir="auto">0.0.14</h2>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>New Bus- and Master lanes in tracker- and clipmatrix view for automating effects
  and volumes</li>

  <li>Fade-commands for lane/bus-volume and bus-filter for long fades can be accessed
  with B + D-UP/D-DOWN

  <ul dir="auto">

  <li>Available commands (upper case letter): fade (I)n, fade (O)ut,  set (T)arget,  slide
  (U)p,  slide (D)own,  (S)top</li>

  <li>The time-unit is amount of steps, so larger values result in longer fades and
  vice versa</li>

  <li>Only available on the lane-volume, bus-volume and bus-filter-cutoff columns
  (more to come)</li>

  </ul>

  </li>

  <li>Filter type option in Bus view: State Variable Filter LP/BP/HP and Biquad LP/BP/HP</li>

  <li>Preliminary Filter-Cutoff Sine-LFO per bus with amount and rate setting</li>

  <li>CIA files can now be installed from the file browser (press A when selected)</li>

  <li>Extremely simple waveform-view with truncating function (removes everything
  before or after the cursor)</li>

  <li>Factotum: Looper with pitch-shifting and time-stretching as a master effect.
  Work in progress.</li>

  <li>Parameter-columns can now be dynamically shown or hidden via B + D-LEFT (opens
  a menu)</li>

  <li>Pitch sliding (portamento): When a note has no instrument value, it will slide
  to the new note</li>

  <li>Pitch envelope (WIP) in third page of instrument-view</li>

  <li>The time can be set via the PSlide instrument attribute and automated via the
  new "GL" tracker-column</li>

  <li>Added cross-fade button, produces seamless loop by fading the first half into
  the second</li>

  <li>Tracker: An entire row can now be deleted by holding B and pressing A twice
  when the note e column is active</li>

  <li>Log-widget (open with Select + DDOWN)</li>

  <li>Rotary stepped-mode (toggle w. DLEFT while holding) - snaps to coarse parameter
  values</li>

  <li>Euclidean / Tracker screen-combo to allow selecting tracks quickly (press D-Right
  three times to show)</li>

  <li>B + DPAD-Left allows to choose which columns are displayed per individual lane</li>

  <li>Clip-lengths in clip-launch-matrix view are now shown as hex values</li>

  <li>Decimal value is shown in status-line when user changes hex-values</li>

  <li>"Insert Note Stops" (to first call if doesn''t hold a note'') option in tracker
  menu - to stop notes of previous pattern</li>

  <li>"Apply mutes" option in clipmatrix-menu: Assigns clip zero to all muted lanes
  and unmutes the</li>

  <li>"Double/Halve content length" options to clipmatrix- and tracker menus</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Volume levels change! A square-law curve is now applied to make fades perceived
  more evenly for humans</li>

  <li>File browser: Directories can now be recursively copied or deleted</li>

  <li>Tracker: Follow is disabled when transport is stopped to avoid confusion (user
  could not move cursor)</li>

  <li>Tracker: Follow is now initially disabled (enable by pressing A)</li>

  <li>Tracker: Can now edit multiple values in selection mode</li>

  <li>Tracker: Value-insertion waits for button B release, to avoid unwanted insertions
  (less confusing)</li>

  <li>Tracker: Releasing B on empty cell inserts previous value except if user moved
  to a different column, then it''s the ''default value</li>

  <li>Tracker: Pressing B + A now deletes the selected values as you would expect</li>

  <li>Tracker: Moving left when on the left most lane+column the cursor no longer
  wraps to the right-most column</li>

  <li>Tracker: Horizontal scrolling changed internally</li>

  <li>ClipMatrix: B + A clears selection or current cell like in tracker</li>

  <li>ClipMatrix: Replaced "Duplicate uniquely" with "Duplicate slots unique" and
  "Duplicate instr unique"</li>

  <li>Tracker/ClipMatrix: No longer pasting at cursor x-position if clipboard is from
  entire row but at 0 instead</li>

  <li>Drum pad selection reflects tracker-lane selection changes (and vice versa as
  before)</li>

  <li>Bus-number is displayed at top-right in drum pads</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Send effects on bus 4 have no effect</li>

  <li>A loop end-point at the last frame produces a click because the interpolation
  reaches out of range

  <ul dir="auto">

  <li>It means that single cycle samples can now be used, useful for chip-tunes</li>

  </ul>

  </li>

  <li>Moving a selection upwards would cause a freeze when moved beyond the first
  row</li>

  <li>Flickering playhead in tracker-view during playback</li>

  <li>Cannot insert value with B + C-Left (only C-Right worked)</li>

  <li>Visual glitch in selection drawing where the cell before the value had differnt
  color</li>

  <li>Entering and exiting the Rosalina menu freezes the console, due to framebuffer
  grab? (Still wonky but no more freezing)</li>

  <li>Interpolating in row-selection mode freezes the app, now does nothing instead
  (supports only column mode)</li>

  <li>Trig condition: x out of x triggers every time</li>

  <li>Http data leaks into file uploads via curl and corrupts them</li>

  </ul>'
updated: '2025-05-16T17:00:49Z'
version: 0.0.14
version_title: I'm the Ed Wood of audio devs
website: https://www.patreon.com/NoiseCommander3DS
---
Beat-making audio sequencer and DJ-tool

- Load your own wav-file sounds
- Combined drum-pad and tracker interface
- Clip-launching matrix
- Euclidean mode for generative sequencing
- Crossfading between two independent sequencer decks
- 12 tracks per deck and 4 global buses
