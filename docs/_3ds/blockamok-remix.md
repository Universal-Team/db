---
author: Mode8fx
avatar: https://avatars.githubusercontent.com/u/57763469?v=4
categories:
- game
color: '#49ef8e'
color_bg: '#27804c'
created: '2024-03-25T23:03:58Z'
description: Dodge the incoming blocks!
download_page: https://github.com/Mode8fx/blockamok/releases
downloads:
  BlockamokRemix-v1.1-3ds.cia:
    size: 2578880
    size_str: 2 MiB
    url: https://github.com/Mode8fx/blockamok/releases/download/v1.1/BlockamokRemix-v1.1-3ds.cia
  BlockamokRemix-v1.1-3dsx.zip:
    size: 1870556
    size_str: 1 MiB
    url: https://github.com/Mode8fx/blockamok/releases/download/v1.1/BlockamokRemix-v1.1-3dsx.zip
  BlockamokRemix-v1.1-gamecube.zip:
    size: 2695827
    size_str: 2 MiB
    url: https://github.com/Mode8fx/blockamok/releases/download/v1.1/BlockamokRemix-v1.1-gamecube.zip
  BlockamokRemix-v1.1-psp.zip:
    size: 1934147
    size_str: 1 MiB
    url: https://github.com/Mode8fx/blockamok/releases/download/v1.1/BlockamokRemix-v1.1-psp.zip
github: Mode8fx/blockamok
icon: https://github.com/Mode8fx/blockamok/raw/main/release-resources/logo_icon_48.png
image: https://github.com/Mode8fx/blockamok/raw/main/release-resources/banner_3ds.png
image_length: 72113
layout: app
license: mit
license_name: MIT License
qr:
  BlockamokRemix-v1.1-3ds.cia: https://db.universal-team.net/assets/images/qr/blockamokremix-v1-1-3ds-cia.png
source: https://github.com/Mode8fx/blockamok
stars: 10
systems:
- 3DS
title: Blockamok Remix
unique_ids:
- '0x3F18B'
update_notes: '<p dir="auto">v1.1</p>

  <p dir="auto">Major performance improvements and others, make sure you update!</p>

  <h3 dir="auto">New Ports:</h3>

  <ul dir="auto">

  <li><strong>Added Android port</strong>! A controller/keyboard is required.</li>

  <li><strong>Added 3DS port</strong>! This runs well on a New 3DS, but O3DS only
  hits ~20 FPS on the lowest settings.</li>

  <li><strong>Added PSP port</strong>! This was previously available as an experimental
  release, but it''s now playable on a real system.</li>

  </ul>

  <h3 dir="auto">Technical Improvements:</h3>

  <ul dir="auto">

  <li><strong>Significantly optimized</strong> rendering and block logic. This means
  <strong>higher framerates</strong> on all systems (sometimes much higher)!

  <ul dir="auto">

  <li>The goal was usually to reach 60 FPS on the most intense settings while maintaining
  good block spawn boundaries, though some consoles only reach this target on less
  intense difficulties.</li>

  <li>If you''re curious, <a href="https://github.com/Mode8fx/blockamok/blob/main/Console%20Performance%20Metrics%20v1.0%20to%20v1.1.png">here''s
  a breakdown</a> of how much performance has been improved on each system.</li>

  </ul>

  </li>

  <li><strong>Increased cube spawn boundaries</strong> on almost all consoles to take
  advantage of improved performance. The only exception is Wii U, where boundaries
  are reduced.</li>

  <li>Other minor optimizations and polish.</li>

  <li>[Linux] <strong>Changed save data location</strong> to point to current executable
  directory instead.</li>

  <li>[Linux] Enabled fullscreen by default.</li>

  <li>[Wii U] Reduced framerate to 540p for better performance (it basically looks
  the same as in 1080p anyway).</li>

  </ul>

  <h3 dir="auto">Changes:</h3>

  <ul dir="auto">

  <li><strong>Enhanced controller support</strong>! Input is now read from all connected
  controllers, and you can freely connect/disconnect controllers as desired.</li>

  <li><strong>Added Block Transparency setting</strong>. Disabling this can <em>slightly</em>
  improve performance if needed.</li>

  <li><strong>Added Frame Rate setting</strong>, intended for weak hardware.</li>

  <li>Made True Analog (formerly called Type B) the default control scheme.</li>

  <li>Made Pitch Black the default overlay color.</li>

  <li>Renamed and reorganized some menu options.</li>

  <li>Added version number to credits.</li>

  <li>[Vita] <strong>Restored Giant block setting</strong>.</li>

  </ul>

  <h3 dir="auto">Bug Fixes:</h3>

  <ul dir="auto">

  <li>[Gamecube] <strong>Fixed save data</strong> reading/writing (mostly; see known
  bug below).</li>

  <li>[Vita] <strong>Fixed crash</strong> on high intensities.</li>

  <li>[Windows+Linux] <strong>Fixed save data</strong> not being read when you run
  the game from a directory other than the one containing the executable.</li>

  </ul>

  <h4 dir="auto">Known Bugs:</h4>

  <ul dir="auto">

  <li>[Android] Performance is weaker than it could be (caps out at around 45 FPS
  on my Retroid Pocket 2+) but improves significantly when the system navigation bar
  is visible.</li>

  <li>[Gamecube] Saving/loading only works on an SD Gecko or SD2SP2; optical drive
  emulators such as FlippyDrive are not supported.</li>

  <li>[PSP] Edge lines are not drawn on blocks. I highly suspect that this is a limitation
  of the PSP''s SDL2 library.</li>

  </ul>

  <p dir="auto">Enjoy!</p>'
updated: '2025-07-20T01:59:21Z'
version: v1.1
version_title: v1.1
---
Fly through a 3D world of never-ending blocks and survive for as long as you can! Includes customization options for gameplay and visuals, along with five music tracks.

New 3DS is recommended; performance is poor on O3DS.