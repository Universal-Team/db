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
    size: 22804302
    size_str: 21 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.5.0/StreaMu-Server.zip
  streamu.3dsx:
    size: 1963692
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.5.0/streamu.3dsx
  streamu.cia:
    size: 1541056
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.5.0/streamu.cia
github: imissuuuu/StreaMu
icon: https://raw.githubusercontent.com/imissuuuu/StreaMu/main/assets/icon_48.png
image: https://raw.githubusercontent.com/imissuuuu/StreaMu/main/assets/banner_256.png
image_length: 3392
layout: app
license: mit
license_name: MIT License
qr:
  streamu.cia: https://db.universal-team.net/assets/images/qr/streamu-cia.png
source: https://github.com/imissuuuu/StreaMu
stars: 7
systems:
- 3DS
title: StreaMu
unique_ids:
- '0xFF3D1'
update_notes: '<h1 dir="auto">StreaMu v1.5.0 Release Notes</h1>

  <h2 dir="auto">Highlights</h2>

  <ul dir="auto">

  <li>Opus Direct is now the only release playback path.</li>

  <li>MP3 Proxy and server-side FFmpeg transcoding have been removed.</li>

  <li>The proxy server no longer requires FFmpeg.</li>

  <li>Existing <code class="notranslate">audio_path</code> settings, including old
  <code class="notranslate">mp3</code> and <code class="notranslate">aac_direct</code>
  values, are treated as Opus Direct.</li>

  </ul>

  <h2 dir="auto">Upgrade Notes</h2>

  <ul dir="auto">

  <li>Update both the 3DS app and the proxy server together.</li>

  <li>Use the latest <code class="notranslate">StreaMu-Server.zip</code>; older proxy
  servers may not provide the required <code class="notranslate">/stream_opus_ogg</code>
  endpoint.</li>

  <li>If playback fails for a specific video, please include the video ID and the
  server dashboard log when reporting it.</li>

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

  <li>Clean 3DS build passed and produced <code class="notranslate">streamu.3dsx</code>
  / <code class="notranslate">streamu.cia</code>.</li>

  <li>Python syntax check passed for proxy server modules.</li>

  <li>Manual 3DS smoke test passed.</li>

  </ul>'
updated: '2026-05-22T08:53:06Z'
version: v1.5.0
version_title: StreaMu v1.5.0
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