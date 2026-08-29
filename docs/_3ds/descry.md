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
  descry.3dsx:
    size: 535528
    size_str: 522 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.7/descry.3dsx
  descry.cia:
    size: 566208
    size_str: 552 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.7/descry.cia
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
stars: 24
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<h1 dir="auto">descry v1.0.7 — precise cuts, dry stems</h1>

  <p dir="auto">this one came from actually using the sampler instead of inventing
  another synth engine for the feature list. long breaks can now be cropped and sliced
  precisely, and finished arrangements can leave the 3DS as clean, synchronized tracks
  for a DAW.</p>

  <h2 dir="auto">dry stem export</h2>

  <p dir="auto">hold <strong>ZL+SELECT</strong> in the PROJECT view to export one
  synchronized set:</p>

  <pre lang="text" class="notranslate"><code class="notranslate">NAME_mix.wav

  NAME_t1.wav

  NAME_t2.wav

  ...

  NAME_t8.wav

  </code></pre>

  <p dir="auto">only tracks used by the arrangement are written. the files are captured
  in one playback pass, so note timing, chance events, noise and sidechain movement
  stay aligned.</p>

  <p dir="auto">track stems keep the instrument, note FX, filter, bitcrush/downsample,
  channel fader, pan and sidechain duck. global delay, reverb and master processing
  are deliberately left out — the point is to get clean material into a DAW and choose
  those effects there. the reference mix still includes the full descry mix and roughly
  three seconds of global FX tail.</p>

  <p dir="auto">all files begin together and have the same length. a stem set reserves
  one shared take suffix, writes through temporary files and removes partial output
  if the SD write fails. normal <strong>SELECT</strong> mix export remains available.</p>

  <h2 dir="auto">sampler precision</h2>

  <ul dir="auto">

  <li>fixed <code class="notranslate">CROP</code> on long samples: its 32-bit position
  multiply overflowed after a few seconds and could keep one unrelated hit instead
  of the selected region</li>

  <li>crop now works in frame coordinates with correct mono/stereo boundaries</li>

  <li>both <strong>WAVE</strong> and <strong>SLICE</strong> have a real editor viewport:
  Circle Pad up/down zooms up to 256×, left/right pans</li>

  <li>touch marker selection and dragging use the zoomed frame range; zooming never
  changes playback <code class="notranslate">START/LENGTH</code></li>

  <li>changing the instrument <code class="notranslate">TYPE</code> still works with
  WAVE/SLICE/LOAD open instead of firing the panel action under the same button</li>

  <li>WAV browser preview now decodes two seconds instead of five, cutting the wait
  and temporary memory for long files while full import keeps its 15-second capacity</li>

  </ul>

  <p dir="auto">crop overflow and precision zoom were reported by <strong><a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/HexManic/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/HexManic">@HexManic</a></strong>
  in <a href="https://github.com/patausx/descry/issues/7" data-hovercard-type="issue"
  data-hovercard-url="/patausx/descry/issues/7/hovercard">issue #7</a>. thanks for
  the clear report — it pointed straight at a real long-sample bug and made the sampler
  editor better in the same pass.</p>

  <h2 dir="auto">export and UI cleanup</h2>

  <ul dir="auto">

  <li>offline export now advances at tick boundaries instead of quantizing events
  to 1024-frame blocks</li>

  <li>export renders from a private project snapshot, so tempo commands cannot mutate
  the live project</li>

  <li>the in-app guide opens only from the visible <code class="notranslate">?</code>
  button — the whole hint strip is no longer an invisible hit target</li>

  <li>mixer faders have restrained theme-derived depth and highlights instead of flat
  single-colour fills</li>

  <li>help and the full guide document sampler zoom, fast preview and dry stems</li>

  </ul>

  <h2 dir="auto">verification</h2>

  <p dir="auto">the full host regression suite passes, including long mono/stereo
  crop and dry stem tap coverage. the release build was compiled with devkitARM and
  tested on a New 3DS.</p>

  <h2 dir="auto">file</h2>

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

  <td>Home Menu install with FBI</td>

  </tr>

  <tr>

  <td><code class="notranslate">descry.3dsx</code></td>

  <td>Homebrew Launcher — copy to <code class="notranslate">/3ds/descry/descry.3dsx</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">descry.3ds</code></td>

  <td>compatible flashcart / emulator</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto">New 3DS / New 2DS only.</p>'
updated: '2026-08-19T23:10:13Z'
version: v1.0.7
version_title: descry v1.0.7
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