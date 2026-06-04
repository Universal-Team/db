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
    size: 267060
    size_str: 260 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.2.1/3dJelly.3dsx
  3dJelly.cia:
    size: 213952
    size_str: 208 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.2.1/3dJelly.cia
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
update_notes: '<h2 dir="auto">3dJelly v0.2.1</h2>

  <p dir="auto">Incremental stability release focused on Old 3DS playback, audio behavior,
  and large Jellyfin library browsing.</p>

  <h3 dir="auto">Changes</h3>

  <ul dir="auto">

  <li>Added Old 3DS specific quality options, including <code class="notranslate">240HQ</code>.</li>

  <li>Improved <code class="notranslate">144p</code> and <code class="notranslate">240p</code>
  bitrate targets for better image quality.</li>

  <li>Improved audio stability during MJPEG playback.</li>

  <li>Added boosted-volume limiting and NDSP soft clipping to reduce harsh clipping
  on loud audio.</li>

  <li>Saved D-pad volume between videos and app restarts.</li>

  <li>Optimized MJPEG/AVI playback parsing, audio queue handling, JPEG color conversion,
  and fullscreen <code class="notranslate">400x240</code> frame drawing.</li>

  <li>Fixed large libraries, seasons, and folders being cut off by adding paged Jellyfin
  item loading.</li>

  <li>Increased browse capacity for large folders.</li>

  <li>Improved playback bottom-screen title wrapping for long titles.</li>

  </ul>

  <h3 dir="auto">Assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dJelly.cia</code> for installable 3DS title builds.</li>

  <li><code class="notranslate">3dJelly.3dsx</code> for Homebrew Launcher builds.</li>

  <li><code class="notranslate">3dJelly.smdh</code> metadata/icon file.</li>

  <li>Source archives are generated automatically by GitHub.</li>

  </ul>'
updated: '2026-06-04T18:30:12Z'
version: v0.2.1
version_title: 3dJelly v0.2.1
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