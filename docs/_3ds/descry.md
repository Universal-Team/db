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
    size: 450832
    size_str: 440 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.4/descry.3dsx
  descry.cia:
    size: 504768
    size_str: 492 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.4/descry.cia
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
stars: 11
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<h1 dir="auto">descry v1.0.4 — modes, scopes &amp; housekeeping</h1>

  <h2 dir="auto">record modes done right (issue <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4863598431" data-permission-text="Title
  is private" data-url="https://github.com/patausx/descry/issues/5" data-hovercard-type="issue"
  data-hovercard-url="/patausx/descry/issues/5/hovercard" href="https://github.com/patausx/descry/issues/5">#5</a>)</h2>

  <p dir="auto">the touch keyboard used to <strong>always</strong> write notes in
  the phrase view — "REC off still records", as <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Rhlp-Engineering/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Rhlp-Engineering">@Rhlp-Engineering</a>
  rightly complained. the REC button now cycles three explicit modes:</p>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>mode</th>

  <th>what happens</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><strong>JAM</strong> <em>(default)</em></td>

  <td>keys and pads only preview. nothing is ever written — noodle over a playing
  song without leaving fingerprints</td>

  </tr>

  <tr>

  <td><strong>WRT</strong></td>

  <td>tracker write mode: notes land at the cursor, cursor advances</td>

  </tr>

  <tr>

  <td><strong>LIVE</strong></td>

  <td>with the transport running, notes are recorded onto the step playing <em>right
  now</em></td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto">and the other half of the report — <em>"i couldn''t find the note
  clear button"</em> — there''s a <strong>CLR</strong> button next to REC now: in
  WRT it clears the step under the cursor and advances (tap-tap-tap wipes a run),
  in LIVE it clears the currently playing step. everything is undoable (ZL+B), and
  touch-entered notes finally participate in undo too.</p>

  <h2 dir="auto">scope styles</h2>

  <p dir="auto">tap the DESCRY wordmark — under the theme list there''s a new <strong>SCOPE</strong>
  row:</p>

  <ul dir="auto">

  <li><strong>WAVE</strong> — the classic filled envelope (default)</li>

  <li><strong>BARS</strong> — mirrored peak bars, chunky VU look</li>

  <li><strong>X-Y</strong> — a proper <strong>goniometer</strong>: mid/side-rotated
  lissajous with auto-gain, connected phosphor-decay trail and CRT-style beam blanking
  on transients. mono sits as a vertical needle; reverb, detune and panning bloom
  the figure sideways. gorgeous in fullscreen (L+SELECT)</li>

  </ul>

  <p dir="auto">the picker stays open while you choose so the strip reacts live. your
  pick is remembered.</p>

  <h2 dir="auto">song export, wired up</h2>

  <p dir="auto"><code class="notranslate">render.wav — song export</code> was promised
  by the manual... but no button ever triggered it. now: <strong>SELECT in the project
  view</strong> renders the song to <code class="notranslate">sdmc:/3ds/descry/render.wav</code>
  (up to 60 s, 32 kHz stereo), with a status toast either way.</p>

  <h2 dir="auto">settings that stick</h2>

  <p dir="auto">new <code class="notranslate">settings.cfg</code> replaces <code class="notranslate">theme.cfg</code>
  (your saved theme migrates automatically). descry now wakes up exactly how you left
  it: theme, octave, KEYS/PADS/KAOS mode, kaoss X/Y assignments, stick sync, scope
  style.</p>

  <h2 dir="auto">fixes</h2>

  <ul dir="auto">

  <li><strong>bottom screen flickered / vanished in fullscreen X-Y scope</strong>
  — the goniometer trail was draining the shared citro2d quad pool on hot transients,
  silently starving everything drawn after it. hard quad budget + beam blanking +
  a bigger pool</li>

  <li>in-app manual updated: record modes, groove pattern column (mixer GRV), scope
  styles</li>

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

  <td><code class="notranslate">descry.3dsx</code></td>

  <td>homebrew launcher</td>

  </tr>

  <tr>

  <td><code class="notranslate">descry.cia</code></td>

  <td>install to home menu (FBI)</td>

  </tr>

  <tr>

  <td><code class="notranslate">descry.3ds</code></td>

  <td>flashcart / citra-azahar</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <blockquote>

  <p dir="auto"><strong>emulator users:</strong> descry needs a real DSP firmware
  dump — see <a href="https://github.com/patausx/descry/issues/2" data-hovercard-type="issue"
  data-hovercard-url="/patausx/descry/issues/2/hovercard">issue #2</a> for the dspfirm.cdc
  setup.</p>

  </blockquote>'
updated: '2026-07-15T09:23:06Z'
version: v1.0.4
version_title: descry v1.0.4
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