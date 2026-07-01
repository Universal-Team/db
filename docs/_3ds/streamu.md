---
author: imissuuuu
avatar: https://avatars.githubusercontent.com/u/270337682?v=4
categories:
- app
color: '#fdebeb'
color_bg: '#807676'
created: '2026-03-23T11:45:54Z'
description: ' A homebrew music player for Nintendo 3DS that streams YouTube audio
  via a companion PC proxy   server.'
download_page: https://github.com/imissuuuu/StreaMu/releases
downloads:
  StreaMu-Server.zip:
    size: 23798235
    size_str: 22 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.5.1/StreaMu-Server.zip
  streamu.3dsx:
    size: 1875276
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.5.1/streamu.3dsx
  streamu.cia:
    size: 1462720
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.5.1/streamu.cia
github: imissuuuu/StreaMu
icon: https://raw.githubusercontent.com/imissuuuu/StreaMu/main/assets/icon_48.png
image: https://raw.githubusercontent.com/imissuuuu/StreaMu/main/assets/banner_256.png
image_length: 3392
layout: app
license: mit
license_name: MIT License
llm_generation: unknown
qr:
  streamu.cia: https://db.universal-team.net/assets/images/qr/streamu-cia.png
source: https://github.com/imissuuuu/StreaMu
stars: 9
systems:
- 3DS
title: StreaMu
unique_ids:
- '0xFF3D1'
update_notes: '<h1 dir="auto">StreaMu v1.5.1 Release Notes</h1>

  <h2 dir="auto">Highlights</h2>

  <ul dir="auto">

  <li>Improved steady-state Opus playback behavior to reduce low-FPS feeling and refill
  instability during playback.</li>

  <li>Reduced noisy hot-path observation overhead while keeping the playback pipeline
  changes that were validated on hardware.</li>

  <li>Tightened several playback and UI edge cases, including buffering state transitions,
  startup connection checks, and QA Remove handling.</li>

  </ul>

  <h2 dir="auto">Upgrade Notes</h2>

  <ul dir="auto">

  <li>Update both the 3DS app and the proxy server together.</li>

  <li>Replace your existing <code class="notranslate">StreaMu-Server.zip</code> with
  the version from this release.</li>

  <li>Existing Opus Direct usage stays the same; this is a maintenance and smoothness
  update rather than a feature reset.</li>

  </ul>

  <h2 dir="auto">Release Assets</h2>

  <ul dir="auto">

  <li><code class="notranslate">streamu.cia</code></li>

  <li><code class="notranslate">streamu.3dsx</code></li>

  <li><code class="notranslate">StreaMu-Server.zip</code>

  <ul dir="auto">

  <li>Includes <code class="notranslate">StreaMu-Server.exe</code>, <code class="notranslate">LICENSE</code>,
  and <code class="notranslate">THIRD_PARTY_LICENSES.md</code>.</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Validation</h2>

  <ul dir="auto">

  <li>The Opus playback tuning changes were reviewed in TAKT review runs before release
  preparation.</li>

  <li>Device testing reported no regression and no meaningful playback artifacts after
  the steady-state refill tuning adjustments.</li>

  <li>GitHub release automation rebuilds the 3DS and server artifacts from the merged
  <code class="notranslate">main</code> commit before publishing this release.</li>

  </ul>'
updated: '2026-06-01T15:08:42Z'
version: v1.5.1
version_title: StreaMu v1.5.1
---
StreaMu is a homebrew music player for Nintendo 3DS that lets you search and stream YouTube
  audio directly on your device.

  A lightweight companion proxy server runs on your PC and handles YouTube data fetching and
  audio transcoding via yt-dlp and FFmpeg.

  ### Features
  - YouTube music search and streaming
  - Playlist management with favorites
  - Thumbnail display on the top screen
  - Customizable themes and accent colors
  - Dual-screen UI with touch support

  ### Requirements
  - Nintendo 3DS with custom firmware (Luma3DS)
  - A PC running the companion proxy server (Python 3.10+, FFmpeg)

  ### Setup
  1. Start the proxy server on your PC (`server/start_server.bat` on Windows)
  2. Launch StreaMu on your 3DS and enter your PC's IP address
  3. Search for music with the Y button and enjoy