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
    size: 448036
    size_str: 437 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.3/descry.3dsx
  descry.cia:
    size: 502720
    size_str: 490 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.3/descry.cia
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
stars: 7
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<h2 dir="auto">descry v1.0.3</h2>

  <h3 dir="auto">added</h3>

  <ul dir="auto">

  <li><strong>in-app manual</strong> — tap the <code class="notranslate">?</code>
  badge on the bottom screen: an 8-page guide right on the console (basics, global
  keys, phrase editing, instruments, the full FX command list, performance, sampling).
  the FX pages are generated from the engine''s own command table, so the help can
  never drift from what the player executes. (issue <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4841918632" data-permission-text="Title
  is private" data-url="https://github.com/patausx/descry/issues/3" data-hovercard-type="issue"
  data-hovercard-url="/patausx/descry/issues/3/hovercard" href="https://github.com/patausx/descry/issues/3">#3</a>)</li>

  <li><strong>INIT preset</strong> — preset 1 in every synth engine (wavsynth / FM
  / DSN) is now a true blank patch for building sounds from scratch: FM = DX7-style
  init voice (single sine carrier), DSN = one saw, filter open, no modulation. old
  saves are unaffected.</li>

  <li><strong>DSN drum presets</strong> — KICK / SNARE / HAT / TOM analog drum starting
  points on the DSN voice.</li>

  <li><strong>reverb size + damping</strong> — RSIZ / RDMP in the mixer master strip:
  room size up to near-self-oscillation feedback plus feedback damping, saved per
  project (older project files load unchanged).</li>

  <li><strong>key root tap</strong> — the KEY readout is split: tap the left half
  to cycle the root note, the right half to cycle the scale.</li>

  <li><strong>load confirmation</strong> — loading over unsaved changes now asks first
  (amber <code class="notranslate">LOAD?</code>, press A again to confirm).</li>

  </ul>

  <h3 dir="auto">fixed</h3>

  <ul dir="auto">

  <li><strong>sample loop modes</strong> — FWDLOOP / REVLOOP with no loop markers
  set now loop the play window (M8 behaviour) instead of silently doing nothing.</li>

  <li><strong>audio cutout recovery</strong> — a watchdog now recovers the NDSP channel
  after a silent stall: ~200 ms of unexpected silence = unpause, ~600 ms = full channel
  re-init.</li>

  <li>phrase R-hint bar no longer overflows the bottom screen.</li>

  </ul>

  <h3 dir="auto">checksums</h3>

  <pre lang="text" class="notranslate"><code class="notranslate">09f92d8e5794878f7429e3e40ab0ed6b411cbe8b6a299de7f11e680419cf1d2c  descry.3dsx

  7ab4d42f36ffd723bae4b6a13557766bff877fe1963cc72243c2b4d062d3ecbf  descry.cia

  79305cf50ee5be5c34ef4316a28200d6d9b093b1942c7c029e9ff6ff565d8291  descry.3ds

  </code></pre>

  <h3 dir="auto">thanks</h3>

  <ul dir="auto">

  <li><strong>lavenderdragon</strong> (discord) — for the detailed feedback round
  that shaped most of this release: loop behaviour, reverb depth, key handling, load
  safety, drum presets, audio cutouts.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Rhlp-Engineering/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Rhlp-Engineering">@Rhlp-Engineering</a>
  — for asking for an in-app manual (issue <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4841918632" data-permission-text="Title is private" data-url="https://github.com/patausx/descry/issues/3"
  data-hovercard-type="issue" data-hovercard-url="/patausx/descry/issues/3/hovercard"
  href="https://github.com/patausx/descry/issues/3">#3</a>). it''s the <code class="notranslate">?</code>
  badge now.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DoubleSprattt/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DoubleSprattt">@DoubleSprattt</a>
  — for continued testing and the hold-to-sustain preview idea.</li>

  </ul>

  <p dir="auto"><strong>install:</strong> CIA via FBI (recommended on CFW) · 3DSX
  from the homebrew launcher · <code class="notranslate">.3ds</code> for flashcarts.
  New 3DS / New 2DS only.</p>'
updated: '2026-07-11T10:00:11Z'
version: v1.0.3
version_title: descry v1.0.3
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