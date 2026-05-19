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
    size: 22791422
    size_str: 21 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.4.1/StreaMu-Server.zip
  streamu.3dsx:
    size: 1736352
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.4.1/streamu.3dsx
  streamu.cia:
    size: 1356224
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.4.1/streamu.cia
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
stars: 6
systems:
- 3DS
title: StreaMu
unique_ids:
- '0xFF3D1'
update_notes: '<h2 dir="auto">Summary</h2>

  <ul dir="auto">

  <li>Added cancelable startup server connection flow.</li>

  <li>Added Mac/Linux Python server startup script.</li>

  <li>Added GitHub Actions 3DS artifact build workflow.</li>

  <li>Added GitHub Actions packaging tool installation for CIA builds.</li>

  </ul>

  <h2 dir="auto">Verification</h2>

  <ul dir="auto">

  <li>Local clean 3DS build passed.</li>

  <li>GitHub Actions required check passed on PR <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4460377293" data-permission-text="Title
  is private" data-url="https://github.com/imissuuuu/StreaMu/issues/1" data-hovercard-type="pull_request"
  data-hovercard-url="/imissuuuu/StreaMu/pull/1/hovercard" href="https://github.com/imissuuuu/StreaMu/pull/1">#1</a>.</li>

  </ul>

  <p dir="auto">Android APK prototype changes are not included in this release.</p>'
updated: '2026-05-16T15:39:44Z'
version: v1.4.1
version_title: StreaMu v1.4.1
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