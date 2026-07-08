---
author: patausx
avatar: https://avatars.githubusercontent.com/u/95235529?v=4
categories:
- app
- media
color: '#2d3213'
color_bg: '#2d3213'
created: '2026-07-06T13:48:43Z'
description: music tracker + synthesizer for the New Nintendo 3DS — song/chain/phrase
  sequencer, 5 synth engines, 23 FX commands, KAOSS pad, mic sampling
download_page: https://github.com/patausx/descry/releases
downloads:
  descry-v1.0.1.zip:
    size: 246517
    size_str: 240 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.1/descry-v1.0.1.zip
  descry.3dsx:
    size: 428588
    size_str: 418 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.1/descry.3dsx
  descry.cia:
    size: 490432
    size_str: 478 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.1/descry.cia
github: patausx/descry
icon: https://raw.githubusercontent.com/patausx/descry/main/assets/icon.png
image: https://raw.githubusercontent.com/patausx/descry/main/branding/final/banner_256x128.png
image_length: 987
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  descry.cia: https://db.universal-team.net/assets/images/qr/descry-cia.png
screenshots:
- description: Fm editor
  url: https://db.universal-team.net/assets/images/screenshots/descry/fm-editor.png
- description: Kaoss pad
  url: https://db.universal-team.net/assets/images/screenshots/descry/kaoss-pad.png
- description: Mixer
  url: https://db.universal-team.net/assets/images/screenshots/descry/mixer.png
- description: Phrase editor
  url: https://db.universal-team.net/assets/images/screenshots/descry/phrase-editor.png
- description: Sampler
  url: https://db.universal-team.net/assets/images/screenshots/descry/sampler.png
- description: Song view
  url: https://db.universal-team.net/assets/images/screenshots/descry/song-view.png
source: https://github.com/patausx/descry
stars: 5
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<p dir="auto">bugfix + polish release, driven almost entirely by <a
  href="https://github.com/patausx/descry/issues/1" data-hovercard-type="issue" data-hovercard-url="/patausx/descry/issues/1/hovercard">issue
  #1</a> — thanks <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gearmo3ds/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gearmo3ds">@gearmo3ds</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DoubleSprattt/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DoubleSprattt">@DoubleSprattt</a>.</p>

  <p dir="auto"><strong>fixed</strong></p>

  <ul dir="auto">

  <li>tempo jitter: sequencer events were quantized to audio-buffer boundaries (up
  to 32ms off-grid, audible as unstable tempo in GRAVEHILL). the scheduler is now
  tick-accurate inside the buffer.</li>

  <li>kaoss pad CUT/RES (and everything else) was stomped by every note trigger —
  gestures now own their parameters while held and hand them back after the release
  ramp.</li>

  <li>mixer settings (faders, delay, reverb, duck) now apply on project load, not
  on the first visit to the mixer screen.</li>

  <li>the R-modifier help bar told the wrong story on the table screen; hint bars
  are now context-aware per screen.</li>

  <li>tapping REC in the drumkit GEN panel flips back to the pads (there was nothing
  to record in GEN).</li>

  </ul>

  <p dir="auto"><strong>improved</strong></p>

  <ul dir="auto">

  <li>kaoss DEL/REV sends: perceptual curve — audible from mid-pad instead of only
  at the top.</li>

  <li>kaoss M&gt;C: auto-engages an LPF and gives the wobble headroom (base cutoff
  to ~55% while held).</li>

  <li>instrument view header: USED IN N PHRASES counter + slot hints — instruments
  are a global bank, now the UI says so.</li>

  <li>hold <strong>L + A</strong> in the instrument view: clone the instrument to
  the first free slot.</li>

  <li>hold <strong>R + Y</strong> in the phrase view: clear the whole phrase (undo-tracked).</li>

  </ul>

  <p dir="auto"><strong>docs</strong></p>

  <ul dir="auto">

  <li>full user guide: <a href="https://github.com/patausx/descry/blob/main/docs/GUIDE.md">docs/GUIDE.md</a></li>

  </ul>

  <p dir="auto"><strong>install:</strong> CIA via FBI (recommended on CFW) · 3DSX
  in the zip (copy <code class="notranslate">3ds</code> to SD root) · <code class="notranslate">.3ds</code>
  for flashcarts. the zip carries the five demo projects and the wavetable starter
  pack. New 3DS / New 2DS only.</p>'
updated: '2026-07-07T13:05:34Z'
version: v1.0.1
version_title: descry v1.0.1
---
descry is a music tracker + synthesizer for the New Nintendo 3DS, in the tradition of LSDj, the Dirtywave M8 and Korg's discontinued DSN-12.

- song → chain → phrase sequencer, 8 tracks, hex editing, 23 FX commands with a built-in reference
- five synth engines, all fixed-point at 32 kHz: wavsynth (+ user wavetables), 4-op FM, sampler with chops/slices, drumkit, and a DSN-style 2-VCO analog voice
- per-track filter / bitcrush / downsample, global ping-pong delay + reverb, sidechain duck
- KAOSS-style XY performance pad on the touchscreen, mixer with touch faders
- record straight from the built-in mic into a sample slot
- groove/swing, scale snap, live mode, undo/redo, 6 color themes

New 3DS / New 2DS only — it needs the faster CPU and the extra core.

The release zip carries five demo projects and a starter pack of single-cycle wavetables — worth grabbing alongside the CIA.