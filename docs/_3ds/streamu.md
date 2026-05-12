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
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.4.0/StreaMu-Server.zip
  streamu.3dsx:
    size: 1734760
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.4.0/streamu.3dsx
  streamu.cia:
    size: 1354688
    size_str: 1 MiB
    url: https://github.com/imissuuuu/StreaMu/releases/download/v1.4.0/streamu.cia
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
update_notes: '<h2 dir="auto">What''s New</h2>

  <h3 dir="auto">Standalone Server EXE</h3>

  <ul dir="auto">

  <li><strong><code class="notranslate">StreaMu-Server.zip</code></strong> — extract
  and run. No Python required.</li>

  <li>Automatically downloads FFmpeg and yt-dlp on first launch.</li>

  </ul>

  <h3 dir="auto">Improved Documentation</h3>

  <ul dir="auto">

  <li>Added Quick Start guide for easy setup</li>

  <li>Added Troubleshooting section (connection timeout, firewall, FFmpeg)</li>

  <li>Documented playlist workflow, custom wallpaper, and all settings</li>

  <li>Bilingual (English / Japanese)</li>

  </ul>

  <h2 dir="auto">Download</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>File</th>

  <th>Description</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">streamu.cia</code></td>

  <td>Install via FBI (HOME Menu)</td>

  </tr>

  <tr>

  <td><code class="notranslate">streamu.3dsx</code></td>

  <td>Homebrew Launcher</td>

  </tr>

  <tr>

  <td><code class="notranslate">StreaMu-Server.zip</code></td>

  <td>Proxy server (Windows, no dependencies)</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <h2 dir="auto">Setup</h2>

  <ol dir="auto">

  <li>Install <code class="notranslate">streamu.cia</code> on your 3DS</li>

  <li>Extract <code class="notranslate">StreaMu-Server.zip</code> and run the EXE
  inside</li>

  <li>Enter the IP shown on the server dashboard</li>

  <li>Press Y to search and play music</li>

  </ol>

  <p dir="auto">For Mac/Linux or manual setup, see the <a href="../../blob/main/README.md">README</a>.</p>'
updated: '2026-05-12T05:18:29Z'
version: v1.4.0
version_title: v1.4.0
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