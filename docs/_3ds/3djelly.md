---
author: 8 Bit Studio
avatar: https://avatars.githubusercontent.com/u/256004323?v=4
categories:
- app
color: '#2e3746'
color_bg: '#2e3746'
created: '2026-03-03T02:38:59Z'
description: A Jellyfin client for Nintendo 3DS.
download_filter: \.3dsx$|\.cia$
download_page: https://github.com/8-bitStudio/3d-jelly/releases
downloads:
  3dJelly.3dsx:
    size: 392160
    size_str: 382 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.3.0/3dJelly.3dsx
  3dJelly.cia:
    size: 297920
    size_str: 290 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.3.0/3dJelly.cia
github: 8-bitStudio/3d-jelly
icon: https://raw.githubusercontent.com/8-bitStudio/3d-jelly/main/gfx/icon.png
image: https://raw.githubusercontent.com/8-bitStudio/3d-jelly/main/gfx/icon.png
image_length: 4191
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
llm_usage: undisclosed
qr:
  3dJelly.cia: https://db.universal-team.net/assets/images/qr/3djelly-cia.png
source: https://github.com/8-bitStudio/3d-jelly
stars: 1
systems:
- 3DS
title: 3dJelly
unique_ids:
- '0xD7E11'
update_notes: '<h2 dir="auto">3dJelly v0.3.0</h2>

  <p dir="auto">This release focuses on Old 3DS playback stability, buffering, and
  new playback controls.</p>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Added encrypted saved password and token storage.</li>

  <li>Added L/R video scrubbing with accelerated hold-to-skip behavior.</li>

  <li>Added top-screen seek progress overlay.</li>

  <li>Added experimental <code class="notranslate">240M1</code> MPEG-1/MP2 playback
  mode for Old 3DS testing. This mode may be kept, changed, or removed depending on
  further testing.</li>

  <li>Added deeper stream buffering with startup prebuffering.</li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li>Changed playback quality switching to D-pad left/right so L/R can be used for
  scrubbing.</li>

  <li>Improved bottom-screen playback controls for seek, quality, and volume.</li>

  <li>Improved Old 3DS MJPEG playback performance and catch-up behavior.</li>

  <li>Lowered normal Old 3DS <code class="notranslate">240p</code> MJPEG bitrate from
  <code class="notranslate">820 kbps</code> to <code class="notranslate">720 kbps</code>
  for stability.</li>

  <li>Added threaded stream reading so network reads are less likely to block playback.</li>

  <li>Optimized MJPEG frame presentation by flushing only the top video framebuffer.</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>Added stream-open retries and reconnect-from-current-position behavior after
  MJPEG stream interruptions.</li>

  <li>Improved handling of saved credential decrypt failures.</li>

  </ul>

  <h3 dir="auto">Notes</h3>

  <ul dir="auto">

  <li><code class="notranslate">240M1</code> is experimental. It may work better than
  MJPEG on some Old 3DS setups, but it is still being tested.</li>

  <li>Playback is still experimental on Old 3DS hardware.</li>

  </ul>'
updated: '2026-06-04T23:43:25Z'
version: v0.3.0
version_title: v0.3.0
---
3dJelly is a Jellyfin client for Nintendo 3DS. It can connect to a Jellyfin server, browse libraries, and play video through server-side transcoding.

Features:
- Native 3DS interface inspired by Jellyfin.
- CIA and 3DSX builds.
- Server-side transcoding with 144p, 240p, 360p, and 480p targets.
- In-playback quality switching.
- Audio playback, mute, and volume controls.

Notes:
- 144p and 240p are recommended for Old 3DS.
- 360p and 480p may be slow depending on hardware, emulator, server speed, and media.