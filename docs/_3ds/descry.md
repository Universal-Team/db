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
    size: 436836
    size_str: 426 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.2/descry.3dsx
  descry.cia:
    size: 495552
    size_str: 483 KiB
    url: https://github.com/patausx/descry/releases/download/v1.0.2/descry.cia
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
stars: 6
systems:
- 3DS
title: descry
unique_ids:
- '0xDE5C1'
update_notes: '<h2 dir="auto">descry v1.0.2</h2>

  <h3 dir="auto">added</h3>

  <ul dir="auto">

  <li>live instrument voice refresh while editing synth parameters</li>

  <li>animated live envelope overlay for wavsynth, sampler, FM and DSN voices</li>

  <li>horizontal song timeline mode with rotated navigation</li>

  </ul>

  <h3 dir="auto">fixed</h3>

  <ul dir="auto">

  <li>show an explanatory error screen when NDSP init fails / <code class="notranslate">dspfirm.cdc</code>
  is missing</li>

  <li>speed up exit/autosave by skipping unchanged sample writes</li>

  <li>tighten bottom panel hit zones so upper navigation touches are not swallowed</li>

  </ul>

  <h3 dir="auto">checksums</h3>

  <pre lang="text" class="notranslate"><code class="notranslate">a6df3bef246aa92423fdd0c54a576e23480c75b7edd1b927f8c3087ee7c0c752  descry.3dsx

  f0470426cf9b9066641d09e8d0a0f1f1b48fc3fff0339bd5e1fea548379aaa8b  descry.cia

  68510353436408002ca3328281bc57e1339f3fce096592eaa7943cce777d704d  descry.3ds

  </code></pre>

  <h3 dir="auto">thanks</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DoubleSprattt/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DoubleSprattt">@DoubleSprattt</a>
  — for the careful issue <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4822698990" data-permission-text="Title is private" data-url="https://github.com/patausx/descry/issues/1"
  data-hovercard-type="issue" data-hovercard-url="/patausx/descry/issues/1/hovercard"
  href="https://github.com/patausx/descry/issues/1">#1</a> report, screenshots, and
  testing notes.</li>

  </ul>'
updated: '2026-07-08T15:04:50Z'
version: v1.0.2
version_title: descry v1.0.2
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