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
    size: 271928
    size_str: 265 KiB
    url: https://github.com/Oldhimaster1/MIVF/releases/download/v1.0.0/mivf_player_3ds.3dsx
  mivf_player_3ds.cia:
    size: 362944
    size_str: 354 KiB
    url: https://github.com/Oldhimaster1/MIVF/releases/download/v1.0.0/mivf_player_3ds.cia
github: Oldhimaster1/MIVF
icon: https://raw.githubusercontent.com/Oldhimaster1/MIVF/refs/heads/main/meta/icon48.png
image: https://raw.githubusercontent.com/Oldhimaster1/MIVF/refs/heads/main/meta/banner.png
image_length: 4907
layout: app
license: mit
license_name: MIT License
llm_generation: minor
qr:
  mivf_player_3ds.cia: https://db.universal-team.net/assets/images/qr/mivf_player_3ds-cia.png
script_message: Place encoded .mivf videos in sdmc:/mivf/ or sdmc:/3ds/mivf_player_3ds/.
  PC video encoding requires the separate encode_mivf tool from the GitHub release.
source: https://github.com/Oldhimaster1/MIVF
stars: 1
systems:
- 3DS
title: MIVF Player
unique_ids:
- '0xF8001'
update_notes: <p dir="auto">First official release! Includes PC encoders and 3DS binaries.</p>
updated: '2026-06-30T14:45:02Z'
version: v1.0.0
version_title: MIVF Player & Encoder v1.0
---

MIVF Player is a homebrew video player for Nintendo 3DS built around the custom MIVF container format.

It supports custom MIVF video streams plus IA4M audio. The player is designed for real Nintendo 3DS hardware and includes a file browser, playback controls, subtitles, chapters, resume bookmarks, favorites, playlists, aspect-ratio modes, and settings saved on the SD card.

Videos can be converted on PC with the included `encode_mivf` encoder. Encoded `.mivf` files can be placed in `sdmc:/mivf/`, `sdmc:/3ds/mivf_player_3ds/`, or the SD root.

(M2Y2 range coding can reduce file size while preserving the already-encoded video packets losslessly... or in simpler terms.... video is highh quality with very small file size)
