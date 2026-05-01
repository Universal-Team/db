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
  StreaMu-server.zip:
    size: 8312
    size_str: 8 KiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.3.0/StreaMu-server.zip
  streamu.3dsx:
    size: 1734760
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.3.0/streamu.3dsx
  streamu.cia:
    size: 1354688
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.3.0/streamu.cia
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
stars: 5
systems:
- 3DS
title: StreaMu
unique_ids:
- '0xFF3D1'
update_notes: '<h2 dir="auto">v1.3.0</h2>

  <h3 dir="auto">Features</h3>

  <ul dir="auto">

  <li>Split L/R button action into <strong>Skip Back</strong> and <strong>Skip Fwd</strong>
  — each independently assignable in Settings</li>

  <li>Search keyboard hint text updated to "Search music..."</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Fix seek bar not pausing when using L/R Play/Pause action</li>

  <li>Fix <code class="notranslate">mp3d</code> uninitialized in MP3Player constructor</li>

  </ul>

  <h3 dir="auto">Performance</h3>

  <ul dir="auto">

  <li>Faster startup: removed 1.1s of artificial sleep delays</li>

  <li>Startup loading screen now appears before wallpaper decode (no more black screen
  on launch)</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Track rename feature in Track Options popup (playlist context only)</li>

  <li>Separated search results from playlist tracks — no more overwriting each other</li>

  <li>SearchScreen redesigned to match PlayingScreen layout (PlayBar + seek + hamburger)</li>

  <li>Network: reduced streaming latency, pipe-based stream generator, Keep-Alive
  support</li>

  <li>Fixed DASH fMP4 seek via manual segment fetch + init segment pre-send</li>

  </ul>

  <hr>

  <h2 dir="auto">v1.2.0</h2>

  <h3 dir="auto">Features</h3>

  <ul dir="auto">

  <li>Thumbnail display on PlayingScreen top screen (async download, center crop)</li>

  <li>Thumbnail routed through proxy server (no direct ytimg.com access)</li>

  <li>Delayed thumbnail fetch by 3s to prioritize audio buffering</li>

  <li>Hide view count when playing from playlist</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Fix crash on START exit when thumbnail is loaded</li>

  </ul>'
updated: '2026-04-06T17:01:19Z'
version: v1.3.0
version_title: v1.3.0
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