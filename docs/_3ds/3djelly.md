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
    size: 263656
    size_str: 257 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.2.0/3dJelly.3dsx
  3dJelly.cia:
    size: 211392
    size_str: 206 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.2.0/3dJelly.cia
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
update_notes: '<h2 dir="auto">3dJelly v0.2.0</h2>

  <p dir="auto">This release focuses on making playback controls and Jellyfin transcoding
  more reliable on Nintendo 3DS hardware and emulators.</p>

  <h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>Working in-playback quality switching with <code class="notranslate">L/R</code>.</li>

  <li>Fresh Jellyfin playback sessions when changing quality, so the server actually
  rebuilds the transcode.</li>

  <li>Current-position resume when changing quality.</li>

  <li>Higher-resolution quality popup showing requested and actual decoded stream
  size.</li>

  <li>Improved bottom-screen playback controls and UI.</li>

  <li>Better volume and mute controls during playback.</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li><code class="notranslate">B</code> during video returns directly to the previous
  screen instead of the playback setup screen.</li>

  <li>Library/item filtering now avoids showing media not actually in your server.</li>

  <li>Bottom-screen playback UI no longer flashes as aggressively during updates.</li>

  <li>Improved text rendering for punctuation and accented characters.</li>

  <li>Fixed HOME-button close behavior that left app stuck closing in a loop.</li>

  </ul>

  <h3 dir="auto">Notes</h3>

  <ul dir="auto">

  <li><code class="notranslate">144p</code> and <code class="notranslate">240p</code>
  are still the best targets for Old 3DS.</li>

  <li><code class="notranslate">360p</code> and <code class="notranslate">480p</code>
  may be slow depending on hardware, emulator, server speed, and the media being transcoded.</li>

  <li>For Homebrew Launcher use, download both <code class="notranslate">3dJelly.3dsx</code>
  and <code class="notranslate">3dJelly.smdh</code>.</li>

  <li>Source archives are attached automatically by GitHub.</li>

  </ul>

  <p dir="auto">Full changes: <a class="commit-link" href="https://github.com/8-bitStudio/3d-jelly/compare/v0.1.2...v0.2.0"><tt>v0.1.2...v0.2.0</tt></a><br>

  Key playback switching commit: <a class="commit-link" data-hovercard-type="commit"
  data-hovercard-url="https://github.com/8-bitStudio/3d-jelly/commit/9a2d363/hovercard"
  href="https://github.com/8-bitStudio/3d-jelly/commit/9a2d363"><tt>9a2d363</tt></a></p>'
updated: '2026-06-04T16:08:44Z'
version: v0.2.0
version_title: 3dJelly v0.2.0
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