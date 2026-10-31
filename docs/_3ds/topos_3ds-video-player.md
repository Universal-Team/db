---
author: mockmodular
avatar: https://avatars.githubusercontent.com/u/85780766?v=4
categories:
- app
- media
color: '#425254'
color_bg: '#425254'
created: '2026-04-08T13:03:39Z'
description: ' topos — True SBS 3D (and normal 2D) Video Player for 3DS | RGB888,
  MVD Hardware Decode, Smooth & Clean '
download_filter: (3dsx|cia)
download_page: https://github.com/mockmodular/topos_3ds-video-player/releases
downloads:
  topos_0.12.3.2.cia:
    size: 9974720
    size_str: 9 MiB
    url: https://github.com/mockmodular/topos_3ds-video-player/releases/download/0.12.3.2/topos_0.12.3.2.cia
github: mockmodular/topos_3ds-video-player
icon: https://raw.githubusercontent.com/mockmodular/topos_3ds-video-player/main/resource/icon.png
image: https://raw.githubusercontent.com/mockmodular/topos_3ds-video-player/main/resource/icon.png
image_length: 5767
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  topos_0.12.3.2.cia: https://db.universal-team.net/assets/images/qr/topos_0-12-3-2-cia.png
source: https://github.com/mockmodular/topos_3ds-video-player
stars: 18
systems:
- 3DS
title: topos_3ds-video-player
update_notes: '<ol dir="auto">

  <li>

  <p dir="auto">Volume Control: Changed the volume slider to directly control the
  output volume of the NDSP playback channel, allowing queued audio buffers that have
  not yet been played to use the updated volume immediately, without waiting for buffers
  using the previous volume to finish playing. Removed the previous per-sample volume
  scaling and its associated overload state. Preserved the 0–100 volume range and
  settings persistence (save/load).</p>

  </li>

  <li>

  <p dir="auto">MPEG-2 3D Texture Refresh: Skipped the two per-eye partial texture
  cache flushes only in the MPEG-2 + SBS 3D + Y2R×2 path, while retaining the final
  full-heap cache flush before GPU execution to reduce redundant cache flush overhead.</p>

  </li>

  <li>

  <p dir="auto">Seek Gate Scope: Only require waiting until the first frame enters
  the display pipeline before allowing seeking when H.264 hardware decoding is actually
  enabled. For other video formats, audio-only files, and H.264 streams that fall
  back to software decoding after hardware decoder initialization fails, seeking is
  allowed immediately after initialization completes. Removed the two existing audio-specific
  seek unlock checks.</p>

  </li>

  </ol>'
updated: '2026-10-31T19:44:25Z'
version: 0.12.3.2
version_title: topos 0.12.3.2
---
