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
    size: 478264
    size_str: 467 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.5/descry.3dsx
  descry.cia:
    size: 524736
    size_str: 512 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.5/descry.cia
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
stars: 14
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<p dir="auto">three weeks of work, and most of it is the unglamorous
  kind: races, silent<br>

  corruption and knobs that did nothing. a sampler workflow overhaul on top.</p>

  <h2 dir="auto">sampling &amp; wavetables</h2>

  <ul dir="auto">

  <li><strong>complete sampler capture / slicing workflow</strong> — recording, trimming,<br>

  transient and equal chopping, per-slice reverse, slice-to-phrase and<br>

  slice-to-kit, beat-sync repitch, and a wav browser that handles 8/16/24/32-bit<br>

  and float files. all of it realtime-safe: SD and decode work happens off the<br>

  audio lock, then swaps under it</li>

  <li><strong>capture any sampler window as a permanent oscillator</strong> — the
  visible window<br>

  becomes a single-cycle USER wavetable plus a matching wavsynth instrument, DC<br>

  removed and normalised, persisted across reboots. record a vowel through the<br>

  mic, play it as an oscillator</li>

  <li>host-side tools for building sample/wav libraries and pushing them to the<br>

  console over FTP</li>

  </ul>

  <h2 dir="auto">fixes</h2>

  <ul dir="auto">

  <li><strong>two use-after-free races between the UI and the audio worker</strong>
  — preview<br>

  voices were published to the mixer <em>before</em> <code class="notranslate">note_on()</code>,
  so if a buffer fill<br>

  landed in that window the worker deleted the voice as inactive and the UI then<br>

  called <code class="notranslate">note_on()</code> on freed memory. separately, every
  destructive sample edit<br>

  (normalize, reverse, fade, crop, wav load, resample, drum regen, mic record)<br>

  mutated a vector a live sampler voice was reading — a realloc there is heap<br>

  corruption. new <code class="notranslate">start_voice()</code> and <code class="notranslate">cut_slot_voices()</code>
  close both. <em>found in<br>

  an external audit of v1.0.4</em></li>

  <li><strong>a full SD card could destroy the project you were saving</strong> —
  saves went<br>

  straight over the target file, so a failed write left a torn file while the UI<br>

  reported success. saves are now atomic (temp file, verified, renamed) and<br>

  loads are transactional, so a short read can no longer leave the live project<br>

  half-old and half-new. loading also validates and clamps anything the player<br>

  indexes into or divides by, instead of trusting the file</li>

  <li><strong>sampler LENGTH disagreed with the engine</strong> — the UI drew the
  window as<br>

  <code class="notranslate">[start, start+length)</code>, the engine read LENGTH as
  an absolute end frame.<br>

  invisible at the default 100%, but any moved START played something other than<br>

  what was on screen: START 50 + LENGTH 50 played an empty window instead of the<br>

  visible second half</li>

  <li><strong>mic recordings were 39 cents flat</strong> — the 3DS mic delivers 32728
  Hz, the<br>

  engine plays 32000, and nothing resampled. every recording ever made was 2.3%<br>

  slow. now resampled on stop</li>

  <li><strong>long wavetable filenames never loaded</strong> — the scan buffer counted
  <code class="notranslate">.wav</code><br>

  against a 20-byte limit, leaving 15 characters of real name, so<br>

  <code class="notranslate">AKWF_hvoice_0001.wav</code> and friends were skipped.
  that is the dominant naming<br>

  convention for single-cycle packs, so the usual symptom was an empty list with<br>

  no explanation</li>

  <li><strong>wavetable slot order was not alphabetical</strong>, despite the header
  saying so —<br>

  it sorted a 32-entry window and took the first 16, so with more than 16 files<br>

  the surviving set depended on raw FAT order. since projects store the slot as<br>

  an index, a saved project could come back playing a different waveform</li>

  <li><strong>CHA FF skipped its guaranteed trigger once every 256 rolls</strong>
  (off-by-one on a<br>

  0..255 range)</li>

  <li><strong>a deep down-transpose under DLY jumped ten octaves up</strong> — the
  note wrapped<br>

  through unsigned before being clamped, so −1 became 255 became 127</li>

  <li><strong>full-scale peaks read as silence on the meters</strong> — negating <code
  class="notranslate">INT16_MIN</code><br>

  wrapped back to itself</li>

  <li><strong>cross-core flags were <code class="notranslate">volatile</code>, not
  atomic</strong> — no happens-before between<br>

  the UI on core 0 and the audio worker on core 1. also, a failed audio init<br>

  leaked everything it had already acquired</li>

  <li><strong>the in-app help page documenting the SD layout and export was invisible</strong>
  —<br>

  a page fits 18 lines before it hits the footer and that one had grown to 24, so<br>

  everything from "SD layout" down was drawn off-screen</li>

  </ul>

  <h2 dir="auto">song exports (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5045693870" data-permission-text="Title is private" data-url="https://github.com/patausx/descry/issues/6"
  data-hovercard-type="issue" data-hovercard-url="/patausx/descry/issues/6/hovercard"
  href="https://github.com/patausx/descry/issues/6">#6</a>)</h2>

  <p dir="auto">exports were hardcoded to a single <code class="notranslate">render.wav</code>,
  so rendering a second project<br>

  silently destroyed the first, and there was no way to name the file — reported by<br>

  <strong><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/francorv99/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/francorv99">@francorv99</a></strong>.</p>

  <p dir="auto">exports now go to <code class="notranslate">renders/</code> named
  after the current project, and an existing<br>

  take is never overwritten: repeat renders become <code class="notranslate">NAME_01.wav</code>,
  <code class="notranslate">NAME_02.wav</code>, …<br>

  so you can bounce a whole session before pulling the SD card. hold <strong>R</strong>
  in the<br>

  PROJECT view to rename, and the view shows the exact target<br>

  (<code class="notranslate">SEL -&gt; renders/NAME.wav</code>) <em>before</em> you
  press SELECT. rename mode existed<br>

  already but nothing on screen advertised it, which is half of why this was<br>

  filed — there is a <code class="notranslate">R=RENAME</code> hint now.</p>

  <h2 dir="auto">tests</h2>

  <p dir="auto"><code class="notranslate">make tests</code> builds and runs the host-side
  suite. six tests had no build rule at<br>

  all and were dead weight nobody ran. <code class="notranslate">test_slice</code>
  was worse than useless: it only<br>

  printed results and always claimed success, and it probed chop sensitivity on a<br>

  break with a silent floor where the setting cannot matter — 80, 150 and 220 all<br>

  produced byte-identical output, so that knob could have been completely broken<br>

  without anyone noticing. it asserts now, on material where sensitivity actually<br>

  does something.</p>

  <h2 dir="auto">note</h2>

  <p dir="auto">the SD layout no longer has <code class="notranslate">render.wav</code>
  — it is <code class="notranslate">renders/</code> now. no project or<br>

  sample data is affected; a leftover <code class="notranslate">render.wav</code>
  is simply unused and can be<br>

  deleted by hand.</p>'
updated: '2026-08-03T19:13:13Z'
version: v1.0.5
version_title: descry v1.0.5
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