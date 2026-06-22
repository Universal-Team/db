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
    size: 559880
    size_str: 546 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.4.2/3dJelly.3dsx
  3dJelly.cia:
    size: 381888
    size_str: 372 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.4.2/3dJelly.cia
github: 8-bitStudio/3d-jelly
icon: https://raw.githubusercontent.com/8-bitStudio/3d-jelly/main/gfx/icon.png
image: https://raw.githubusercontent.com/8-bitStudio/3d-jelly/main/gfx/icon.png
image_length: 4191
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
llm_generation: unknown
qr:
  3dJelly.cia: https://db.universal-team.net/assets/images/qr/3djelly-cia.png
source: https://github.com/8-bitStudio/3d-jelly
stars: 7
systems:
- 3DS
title: 3dJelly
unique_ids:
- '0xD7E11'
update_notes: '<h2 dir="auto">Added</h2>

  <ul dir="auto">

  <li>Added a search feature</li>

  <li>Added Polish language support.</li>

  <li>Added Indonesian language support.</li>

  <li>Added Turkish language support.</li>

  <li>Added Swedish language support.</li>

  <li>Added localized search, settings, browsing, playback status, error, and bottom-screen
  playback text for new languages.</li>

  </ul>

  <h2 dir="auto">Changed</h2>

  <ul dir="auto">

  <li>Improved playback overlay handling for Latin diacritics so translated titles
  and status text avoid question marks where possible.</li>

  <li>Updated app-reported version to 0.4.2.</li>

  </ul>

  <h2 dir="auto">Fixed</h2>

  <ul dir="auto">

  <li>Fixed browse artwork fitting so show and poster previews better cover their
  frame without small top or bottom bars.</li>

  <li>Fixed playback status badges for Polish, Indonesian, Turkish, and Swedish loading,
  error, and stopped messages.</li>

  </ul>

  <h2 dir="auto">Notes</h2>

  <p dir="auto">The focus is now on plugins</p>

  <p dir="auto">3dJelly now supports a total of <strong>17 languages</strong></p>'
updated: '2026-06-06T02:07:44Z'
version: v0.4.2
version_title: 3dJelly v0.4.2
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