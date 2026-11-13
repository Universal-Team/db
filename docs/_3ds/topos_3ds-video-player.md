---
author: mockmodular
avatar: https://avatars.githubusercontent.com/u/85780766?v=4
categories:
- app
- media
color: '#425254'
color_bg: '#425254'
created: '2026-04-08T13:03:39Z'
description: ' topos — True SBS 3D (and normal 2D) Video Player for 3DS | RGB888,
  MVD Hardware Decode, Smooth & Clean '
download_filter: (3dsx|cia)
download_page: https://github.com/mockmodular/topos_3ds-video-player/releases
downloads:
  topos.cia:
    size: 9978816
    size_str: 9 MiB
    url: https://github.com/mockmodular/topos_3ds-video-player/releases/download/1.12.3.4/topos.cia
github: mockmodular/topos_3ds-video-player
icon: https://raw.githubusercontent.com/mockmodular/topos_3ds-video-player/main/resource/icon.png
image: https://raw.githubusercontent.com/mockmodular/topos_3ds-video-player/main/resource/icon.png
image_length: 5767
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  topos.cia: https://db.universal-team.net/assets/images/qr/topos-cia.png
source: https://github.com/mockmodular/topos_3ds-video-player
stars: 19
systems:
- 3DS
title: topos_3ds-video-player
update_notes: '<h1 dir="auto">1.12.3.4</h1>

  <h2 dir="auto">Direct decoded-frame input for Y2R x2</h2>

  <ul dir="auto">

  <li>Software-decoded YUV420P frames can now feed Y2R x2 directly in both 2D and
  side-by-side 3D playback, eliminating the intermediate YUV buffer allocation and
  frame copy.</li>

  <li>Transfer the AVFrame reference to the conversion thread and retain it until
  hardware conversion completes or cancellation is acknowledged. Use the actual plane
  addresses and row strides.</li>

  <li>Keep compatibility with input layouts that require copying. Preserve the existing
  RGB output fallback for 2D playback with 1024-wide textures while still avoiding
  the YUV input copy.</li>

  <li>Represent each contiguous decoded-image allocation with one correctly sized
  AVBufferRef and a single release callback.</li>

  </ul>

  <h2 dir="auto">Audio track selection</h2>

  <ul dir="auto">

  <li>Add <code class="notranslate">track</code> immediately below <code class="notranslate">volume</code>
  in the root settings menu, with choices <code class="notranslate">3</code>, <code
  class="notranslate">2</code>, <code class="notranslate">1</code>, and <code class="notranslate">0</code>.
  The default is <code class="notranslate">0</code>.</li>

  <li>Save the preferred track in persistent settings. Existing settings files default
  to track <code class="notranslate">0</code>.</li>

  <li>Apply the current in-memory preference when opening a video. If the requested
  track does not exist, use track <code class="notranslate">0</code> without overwriting
  the preference.</li>

  <li>Changing the setting does not switch the current playback session. Reopening
  the same video starts it from the beginning with the new selection; seeking retains
  the session''s active track.</li>

  <li>Use the active track''s audio parameters for speaker setup, buffer timing, and
  codec display.</li>

  </ul>

  <h2 dir="auto">Validation</h2>

  <ul dir="auto">

  <li>Built and linked the Nintendo 3DS application and generated the CIA package.</li>

  <li>Passed host checks for frame-reference lifetime, DMA addressing, conversion
  error handling, audio-track routing, settings round-trips, and compatibility with
  older settings files.</li>

  <li>Passed the existing CIA package structure checks.</li>

  </ul>

  <h2 dir="auto">Download</h2>

  <ul dir="auto">

  <li><code class="notranslate">topos.cia</code></li>

  </ul>'
updated: '2026-11-02T19:43:17Z'
version: 1.12.3.4
version_title: 1.12.3.4
---
