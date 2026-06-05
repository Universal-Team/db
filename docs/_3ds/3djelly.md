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
    size: 506408
    size_str: 494 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.4.1/3dJelly.3dsx
  3dJelly.cia:
    size: 352704
    size_str: 344 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.4.1/3dJelly.cia
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
update_notes: '<h2 dir="auto">Added</h2>

  <ul dir="auto">

  <li>Added Afrikaans, French, German, Italian, Dutch, Portuguese, Russian, Korean,
  Simplified Chinese, and Traditional Chinese language support.</li>

  <li>Added native Korean/Hangul text rendering.</li>

  <li>Added Simplified and Traditional Chinese system-font support for normal UI text.</li>

  <li>Added compact playback-screen glyph support for Korean, Japanese, Simplified
  Chinese, and Traditional Chinese.</li>

  <li>Added configurable bottom-screen dimming during video playback, with timer options
  and a Never setting.</li>

  </ul>

  <h2 dir="auto">Changed</h2>

  <ul dir="auto">

  <li>Reworked translations into separate JSON files with a generated C translation
  table.</li>

  <li>Improved the language selector with a larger modal, scroll window, current-language
  marker, and clearer controls.</li>

  <li>Improved Japanese playback UI text so bottom-screen controls and status labels
  use native Japanese.</li>

  </ul>

  <h2 dir="auto">Fixed</h2>

  <ul dir="auto">

  <li>Fixed ampersands rendering as question marks in playback text.</li>

  <li>Fixed Japanese language label rendering after adding Chinese font support.</li>

  <li>Fixed Korean, Japanese, Simplified Chinese, and Traditional Chinese playback
  status labels showing missing or fallback characters.</li>

  </ul>

  <h2 dir="auto">Notes</h2>

  <ul dir="auto">

  <li>3dJelly now supports 13 languages.</li>

  <li>Some translations are new and may need community feedback, especially text that
  is too long for the 3DS screen.</li>

  <li>Playback is still experimental, especially at higher quality settings on Old
  3DS. 3dJelly has not been tested on a new 3ds.</li>

  </ul>'
updated: '2026-06-05T20:25:56Z'
version: v0.4.1
version_title: 3dJelly 0.4.1
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