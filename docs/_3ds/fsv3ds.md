---
author: Bruce303lee
avatar: https://avatars.githubusercontent.com/u/5742315?v=4
categories:
- utility
color: '#8b7c58'
color_bg: '#807251'
created: '2026-08-16T00:32:04Z'
description: A homebrew 3DS port of fsv, the 3D File System Visualizer
download_page: https://github.com/Bruce303lee/fsv3ds/releases
downloads:
  fsv3ds-launcher.cia:
    size: 83392
    size_str: 81 KiB
    url: https://github.com/Bruce303lee/fsv3ds/releases/download/v1.0.0/fsv3ds-launcher.cia
  fsv3ds.3dsx:
    size: 691948
    size_str: 675 KiB
    url: https://github.com/Bruce303lee/fsv3ds/releases/download/v1.0.0/fsv3ds.3dsx
github: Bruce303lee/fsv3ds
icon: https://raw.githubusercontent.com/Bruce303lee/fsv3ds/main/forwarder/assets/icon.png
image: https://raw.githubusercontent.com/Bruce303lee/fsv3ds/main/forwarder/assets/banner.png
image_length: 1121
layout: app
license: lgpl-2.1
license_name: GNU Lesser General Public License v2.1
llm_generation: 'yes'
qr:
  fsv3ds-launcher.cia: https://db.universal-team.net/assets/images/qr/fsv3ds-launcher-cia.png
source: https://github.com/Bruce303lee/fsv3ds
stars: 0
systems:
- 3DS
title: fsv3ds
update_notes: '<p dir="auto">fsv3ds is a homebrew 3DS port of <a href="https://github.com/mcuelenaere/fsv"><strong>fsv</strong></a>,
  the "3D File System Visualizer" — the file-browser-as-a-cyberspace-city thing from
  <em>Jurassic Park</em> (SGI''s <code class="notranslate">fsn</code>). Point it at
  a folder on your SD card and it lays out directories and files as a 3D treemap you
  fly around with the circle pad, in stereoscopic 3D, on real 3DS hardware.</p>

  <h2 dir="auto">Features</h2>

  <ul dir="auto">

  <li><strong>MapV treemap rendering</strong> and <strong>TreeV cylindrical rendering</strong>,
  switchable live with X</li>

  <li><strong>Navigation</strong> — drill in/up, D-pad selection cycling, cinematic
  camera moves</li>

  <li><strong>Real per-extension file coloring</strong> — ROMs, homebrew (<code class="notranslate">.3dsx</code>/<code
  class="notranslate">.cia</code> get their own colors), archives, images, audio/video,
  text/config, directories</li>

  <li><strong>Stereoscopic 3D</strong> using the console''s own 3D slider</li>

  <li><strong>Live labels</strong>, switchable between selected-only / all / off</li>

  <li><strong>Touch-driven bottom screen</strong> — status bar, Folder/Settings/Info/Log
  panel, footer breadcrumb</li>

  <li><strong>Text and hex file viewers</strong>, and a <strong>BMP/PNG/JPEG image
  viewer</strong></li>

  <li><strong>Launch other <code class="notranslate">.3dsx</code> homebrew</strong>
  directly from the file browser</li>

  <li>A dev-only, credential-gated remote control service (see <code class="notranslate">RPC.md</code>)
  for scripted testing — not needed for normal use</li>

  </ul>

  <h2 dir="auto">Downloads</h2>

  <ul dir="auto">

  <li><code class="notranslate">fsv3ds.3dsx</code> — run via the Homebrew Launcher
  (copy to <code class="notranslate">/3ds/</code> on your SD card)</li>

  <li><code class="notranslate">fsv3ds-launcher.cia</code> — optional forwarder CIA
  that gives fsv3ds its own Home Menu icon and chainloads the <code class="notranslate">.3dsx</code>
  above (requires the <code class="notranslate">.3dsx</code> to be present at <code
  class="notranslate">sdmc:/3ds/fsv3ds/fsv3ds.3dsx</code>)</li>

  <li><code class="notranslate">fsv3ds.smdh</code> — icon/metadata sidecar, not required
  to run</li>

  </ul>

  <h2 dir="auto">License</h2>

  <p dir="auto">fsv3ds is a derivative work of fsv, licensed under the GNU Lesser
  General Public License v2.1 — see <a href="COPYING"><code class="notranslate">COPYING</code></a>.</p>'
updated: '2026-08-16T00:39:02Z'
version: v1.0.0
version_title: fsv3ds v1.0.0
---
A homebrew 3DS port of fsv, the '3D File System Visualizer' -- the file-browser-as-a-cyberspace-city thing from Jurassic Park (SGI's fsn). Point it at a folder on your SD card and it lays out directories and files as a 3D treemap you fly around with the circle pad, in stereoscopic 3D, on real 3DS hardware.

Features MapV (treemap) and TreeV (cylindrical) rendering modes, real per-extension file coloring, a touch-driven bottom screen with folder browsing and settings, text/hex/image (BMP/PNG/JPEG) file viewers, and the ability to launch other .3dsx homebrew directly from the file browser.