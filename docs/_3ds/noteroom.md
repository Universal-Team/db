---
author: SprtnDio
avatar: https://avatars.githubusercontent.com/u/183821772?v=4
categories:
- utility
color: '#444637'
color_bg: '#444637'
created: '2026-03-13T00:19:39Z'
description: Drawing and text Chat Rooms.
download_page: https://github.com/SprtnDio/NoteRoom/releases
downloads:
  NoteRoom.3dsx:
    size: 262296
    size_str: 256 KiB
    url: https://github.com/SprtnDio/NoteRoom/releases/download/v1.0.4/NoteRoom.3dsx
  NoteRoom.cia:
    size: 933824
    size_str: 911 KiB
    url: https://github.com/SprtnDio/NoteRoom/releases/download/v1.0.4/NoteRoom.cia
github: SprtnDio/NoteRoom
icon: https://raw.githubusercontent.com/SprtnDio/NoteRoom/main/icon.png
image: https://raw.githubusercontent.com/SprtnDio/NoteRoom/main/images/NoteRoom_05.04.26_04.21.54.546.png
image_length: 12806
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  NoteRoom.cia: https://db.universal-team.net/assets/images/qr/noteroom-cia.png
source: https://github.com/SprtnDio/NoteRoom
stars: 2
systems:
- 3DS
title: NoteRoom
update_notes: '<h2 dir="auto">Patch Notes – v1.0.4</h2>

  <h3 dir="auto">🛠️ Fixes</h3>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Save / Load Functionality Restored</strong><br>

  Drawings saved to SD card now load correctly when selected. A previous issue prevented
  loaded drawings from appearing on the canvas.</p>

  </li>

  <li>

  <p dir="auto"><strong>Drawing Preview Clipping</strong><br>

  Chat drawing previews are now properly clipped to their message bubble boundaries
  – lines no longer spill outside the bubble.</p>

  </li>

  </ul>

  <h3 dir="auto">✨ New Features</h3>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Improved Ban Evasion Protection</strong><br>

  Banned users are now reliably blocked from joining any room. Deleting local ban
  files has no effect – the restriction is enforced server‑side and remains active
  for the full 48‑hour duration.</p>

  </li>

  <li>

  <p dir="auto"><strong>Admin Recognition</strong><br>

  Messages from server administrators are now marked with a gold <strong>[ADMIN]</strong>
  tag. Admins are identified via a built‑in ID list.</p>

  </li>

  <li>

  <p dir="auto"><strong>Spam Protection for Menu Actions</strong><br>

  Rapidly pressing the A button in menus no longer triggers multiple actions. A 0.5‑second
  cooldown prevents accidental double‑joins or room selections.</p>

  </li>

  </ul>

  <h3 dir="auto">⚡ Improvements</h3>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Network Responsiveness</strong><br>

  The MQTT receive loop now processes all incoming packets every frame, eliminating
  lag and stutter when many messages arrive at once.</p>

  </li>

  <li>

  <p dir="auto"><strong>Drawing Precision</strong><br>

  Touch input is now strictly clamped to the valid drawing area, preventing lines
  from being placed outside the canvas bounds.</p>

  </li>

  <li>

  <p dir="auto"><strong>Heartbeat Reliability</strong><br>

  Heartbeat messages are sent with QoS 1 to improve presence accuracy on unreliable
  connections.</p>

  </li>

  <li>

  <p dir="auto"><strong>UI Polish</strong></p>

  <ul dir="auto">

  <li>Current pen/eraser size is displayed in the top toolbar.</li>

  <li>WiFi and battery indicators are more accurately rendered.</li>

  </ul>

  </li>

  </ul>'
updated: '2026-04-13T20:55:07Z'
version: v1.0.4
version_title: NoteRoom v1.0.4
---
NoteRoom is a real-time online drawing and text Chatroom messenger for the Nintendo 2/3DS, inspired by a well known chatroom. Connect globally across themed, dynamic lobbies, share hand-drawn doodles, and view live user counts.