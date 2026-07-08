---
author: Oldhimaster1
avatar: https://avatars.githubusercontent.com/u/179153474?v=4
categories:
- app
- media
color: '#294c7a'
color_bg: '#294c7a'
created: '2026-06-27T23:27:59Z'
description: A custom MIVF video player for Nintendo 3DS with lots of features.
download_filter: ^mivf_player_3ds\.(cia|3dsx)$
download_page: https://github.com/Oldhimaster1/MIVF/releases
downloads:
  mivf_player_3ds.3dsx:
    size: 340132
    size_str: 332 KiB
    url: https://github.com/Oldhimaster1/MIVF/releases/download/v2026.07.05/mivf_player_3ds.3dsx
  mivf_player_3ds.cia:
    size: 407488
    size_str: 397 KiB
    url: https://github.com/Oldhimaster1/MIVF/releases/download/v2026.07.05/mivf_player_3ds.cia
github: Oldhimaster1/MIVF
icon: https://raw.githubusercontent.com/Oldhimaster1/MIVF/refs/heads/main/meta/icon48.png
image: https://raw.githubusercontent.com/Oldhimaster1/MIVF/refs/heads/main/meta/banner.png
image_length: 4907
layout: app
license: mit
license_name: MIT License
llm_generation: minor
preinstall_message: Place encoded .mivf videos in sdmc:/mivf/ or sdmc:/3ds/mivf_player_3ds/.
  PC video encoding requires the separate encode_mivf tool from the GitHub release.
qr:
  mivf_player_3ds.cia: https://db.universal-team.net/assets/images/qr/mivf_player_3ds-cia.png
source: https://github.com/Oldhimaster1/MIVF
stars: 2
systems:
- 3DS
title: MIVF Player
unique_ids:
- '0xF8002'
update_notes: '<h1 dir="auto">MIVF Player v2026.07.05</h1>

  <h2 dir="auto">Highlights</h2>

  <ul dir="auto">

  <li>Updated README and full documentation set.</li>

  <li>Added sidecar and embedded seek-index support.</li>

  <li>Added encoder packet-size report.</li>

  <li>Added --profile 3ds-fast for smaller, Old 3DS-friendly encodes.</li>

  <li>Improved large-file startup behavior.</li>

  <li>Improved browser preview responsiveness on Old 3DS.</li>

  <li>Improved settings responsiveness by saving on close instead of every value change.</li>

  <li>UI polish for browser, settings, alerts, timeline, and playback footer.</li>

  </ul>

  <h2 dir="auto">Assets</h2>

  <ul dir="auto">

  <li>mivf_player_3ds.3dsx - Homebrew Launcher build.</li>

  <li>mivf_player_3ds.cia - installable HOME Menu build.</li>

  <li>encode_mivf.exe - Windows encoder frontend.</li>

  <li>miv2y_moflex_tier.exe - native encoder helper, also uploaded separately for
  debugging/dev use.</li>

  <li>SHA256SUMS.txt - checksums for release assets.</li>

  </ul>

  <h2 dir="auto">Recommended encoding</h2>

  <p dir="auto">For best Old 3DS playback:</p>

  <p dir="auto">encode_mivf.exe input.mp4 output.mivf --m2y2 --profile 3ds-fast --report-packet-sizes</p>

  <p dir="auto">For smaller files:</p>

  <p dir="auto">encode_mivf.exe input.mp4 output.mivf --m2y2 --profile 3ds-fast --qp
  45 --lambda 45 --keep 4 --c-qp-offset 10 --report-packet-sizes</p>'
updated: '2026-07-06T02:49:03Z'
version: v2026.07.05
version_title: MIVF Player v2026.07.05
---

MIVF Player is a homebrew video player for Nintendo 3DS built around the custom MIVF container format.

It supports custom MIVF video streams plus IA4M audio. The player is designed for real Nintendo 3DS hardware and includes a file browser, playback controls, subtitles, chapters, resume bookmarks, favorites, playlists, aspect-ratio modes, and settings saved on the SD card.

Videos can be converted on PC with the included `encode_mivf` encoder. Encoded `.mivf` files can be placed in `sdmc:/mivf/`, `sdmc:/3ds/mivf_player_3ds/`, or the SD root.

(M2Y2 range coding can reduce file size while preserving the already-encoded video packets losslessly... or in simpler terms.... video is highh quality with very small file size)
