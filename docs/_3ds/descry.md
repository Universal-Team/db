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
  SHA256SUMS:
    size: 325
    size_str: 325 Bytes
    url: https://github.com/patausx/descry/releases/download/v1.0.6/SHA256SUMS
  descry-v1.0.6-IRONLUNG.zip:
    size: 113925
    size_str: 111 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.6/descry-v1.0.6-IRONLUNG.zip
  descry.3dsx:
    size: 529624
    size_str: 517 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.6/descry.3dsx
  descry.cia:
    size: 562112
    size_str: 548 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.6/descry.cia
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
stars: 21
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<h1 dir="auto">descry v1.0.6 — one clock, honest renders, sharper tools</h1>

  <p dir="auto">this release attacks the parts of a tracker that absolutely cannot
  lie: time, playback position, undo and export. it also ships the first proper flagship
  demo — a copyright-clean jungle track built to show what the sampler and sequencer
  actually do.</p>

  <h2 dir="auto">one Song clock</h2>

  <p dir="auto">Song rows used to advance independently on every track. put a one-phrase
  drum chain next to a four-phrase bass chain and the drums reached the next arrangement
  row three phrases early; an <code class="notranslate">EMPTY</code> cell raced ahead
  even faster. the arrangement could look aligned and still dissolve during playback.</p>

  <p dir="auto">v1.0.6 gives every Song row one shared boundary, derived from the
  longest chain in that row. shorter chains loop inside it, <code class="notranslate">EMPTY</code>
  cells wait silently, and all eight tracks enter the next row together. the same
  boundary now drives end-of-song detection and offline export, so an unused track
  can no longer truncate a render.</p>

  <h2 dir="auto">exports you can trust</h2>

  <p dir="auto">WAV export now uses the same mixer state as live playback:</p>

  <ul dir="auto">

  <li>channel faders, master volume and persisted mutes</li>

  <li>delay time / feedback / wet, reverb wet / size / damping</li>

  <li>sends and sidechain ducking</li>

  <li>long rests and sparse sections without false early-stop</li>

  <li>the complete Song pass plus roughly three seconds of FX tail</li>

  </ul>

  <p dir="auto">renders stream straight to the SD card instead of accumulating the
  whole WAV in RAM, with a ten-minute safety cap. at the shared wrap boundary the
  sequencer releases the current voices without triggering row 0 again, so the tail
  belongs to the song you rendered — not the next loop.</p>

  <h2 dir="auto">IRONLUNG</h2>

  <p dir="auto">IRONLUNG is a 174 BPM jungle demo built entirely from descry''s own
  engines and procedural drum generator:</p>

  <ul dir="auto">

  <li>copyright-clean two-bar break, sliced into 32 chromatic sixteenth-note chops</li>

  <li>step-programmed rearrangements, retrigger rolls and reverse fills</li>

  <li>reese bass, sine sub, pads, stabs and sidechain ducking</li>

  </ul>

  <p dir="auto">install all three demo files together in <code class="notranslate">/3ds/descry/</code>:</p>

  <pre lang="text" class="notranslate"><code class="notranslate">project_00.tr3d

  sample_63.s16

  sample_63.name

  </code></pre>

  <p dir="auto"><code class="notranslate">.tr3d</code> files do not embed sample audio.
  slot 63 is reserved for IRONLUNG; the optional BMT add-on now occupies slots 32–62
  only.</p>

  <h2 dir="auto">Phrase Tools, inspector and editing</h2>

  <p dir="auto">Phrase view now keeps a permanent inspector beside the grid. it resolves
  the<br>

  sticky/inherited instrument, shows its source and live envelope, exposes ALWAYS<br>

  defaults and the mod table that can otherwise make a patch sound mysteriously<br>

  processed, and decodes all three FX slots. press <strong>SELECT</strong> on the
  instrument<br>

  column to jump straight into that instrument''s editor.</p>

  <p dir="auto">Phrase Tools adds deterministic generators alongside rotate, reverse,
  transpose,<br>

  octave and velocity transforms:</p>

  <ul dir="auto">

  <li>Euclidean rhythms and density gating</li>

  <li>humanize and ratchets</li>

  <li>random notes and scale-aware mutation</li>

  <li>trigger-chance spread and <code class="notranslate">EVN</code> cycle conditions</li>

  </ul>

  <p dir="auto">random operations use an explicit seed, stay inside the selected rows,
  respect the active key/scale and leave unrelated FX alone. every operation is one
  undo step.</p>

  <p dir="auto">analog controls are editing tools now: the circle pad accelerates
  Song navigation<br>

  and scrubs/zooms the sampler window; the C-stick is a relative fine/coarse value<br>

  encoder. this replaces the old left-stick-as-KAOSS and right-stick sends/crush<br>

  mappings, and the KAOSS <code class="notranslate">STK</code> toggle is gone. START
  in Song view plays from the<br>

  cursor row; hold <strong>L+START</strong> to start from the top.</p>

  <h2 dir="auto">undo, playheads and visible state</h2>

  <ul dir="auto">

  <li>preset loads, instrument type changes and instrument clones are undoable as
  whole snapshots</li>

  <li>replacing or loading a project clears old history, preventing undo from splicing
  data from the previous project</li>

  <li>phrase and chain playheads report the position that actually sounded, including
  phrase boundaries and tracks other than track 0</li>

  <li>Song and Chain edits finally mark the project dirty</li>

  <li>mute/solo state, Song end, active playhead owner and the unsaved marker are
  visible in the views where they matter</li>

  <li>track mutes persist across save/load; PLAY and leaving solo no longer wipe them</li>

  </ul>

  <h2 dir="auto">UI fixes and maintenance</h2>

  <ul dir="auto">

  <li>theme switching now reaches touch keys, pads, filter tints and confirmation
  states instead of leaving cretaceous-coloured strays</li>

  <li>overlays animate closed while remaining input-opaque, so the dismiss button
  cannot hit the screen underneath</li>

  <li>leaving KAOSS mode during a held gesture performs the normal release ramp instead
  of freezing performance parameters</li>

  <li>grid lines no longer shout louder than dim data in every theme</li>

  <li><code class="notranslate">DTIM</code> is shown in milliseconds</li>

  <li>removed the nonexistent <code class="notranslate">GRAN</code> instrument label
  and cleaned the full-build warnings</li>

  <li>split the UI monolith into per-screen translation units</li>

  <li>CI now runs all 15 host regressions, builds IRONLUNG and performs a clean devkitARM
  build on every push and pull request</li>

  </ul>

  <h2 dir="auto">files</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>file</th>

  <th>use</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">descry.cia</code></td>

  <td>install to the Home Menu with FBI</td>

  </tr>

  <tr>

  <td><code class="notranslate">descry.3dsx</code></td>

  <td>Homebrew Launcher — copy to <code class="notranslate">/3ds/descry/descry.3dsx</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">descry.3ds</code></td>

  <td>flashcart / Citra / Azahar</td>

  </tr>

  <tr>

  <td><code class="notranslate">descry-v1.0.6-IRONLUNG.zip</code></td>

  <td>complete demo bundle for project slot 00 and sample slot 63</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto">New 3DS / New 2DS only.</p>

  <h2 dir="auto">checksums</h2>

  <pre lang="text" class="notranslate"><code class="notranslate">fe5eac672dac3b5c66ccc62de2617d8a251d047473d088ba9175f013f974a3db  descry.3dsx

  ab20c8e0d0d0c0e5a9f20907d8d4cd5b710609db4bdba341cb67557d3ba65086  descry.cia

  2063e92e63e91250f1123556a32bcd1cd082ffc402d055a6db822c834187fec1  descry.3ds

  23f73f5278336ef87aaa2a7dc85672c6a541f6f275912e5ff1360ef9345de5d1  descry-v1.0.6-IRONLUNG.zip

  </code></pre>'
updated: '2026-08-15T08:30:07Z'
version: v1.0.6
version_title: descry v1.0.6
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