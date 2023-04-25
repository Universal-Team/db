---
author: mGBA
avatar: https://avatars.githubusercontent.com/u/10085927?v=4
categories:
- emulator
color: '#503a7e'
color_bg: '#503a7e'
created: '2014-12-09T21:37:23Z'
description: mGBA Game Boy Advance Emulator
download_page: https://github.com/mgba-emu/mgba/releases
downloads:
  mGBA-0.10.2-3ds.7z:
    size: 1196353
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.10.2/mGBA-0.10.2-3ds.7z
eval_notes_md: true
github: mgba-emu/mgba
icon: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-48.png
image: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-256.png
image_length: 43839
layout: app
license: mpl-2.0
license_name: Mozilla Public License 2.0
nightly:
  download_page: https://mgba.io/downloads.html#development-downloads
  downloads:
    mGBA-build-latest-3ds.7z:
      url: https://s3.amazonaws.com/mgba/mGBA-build-latest-3ds.7z
screenshots:
- description: File list
  url: https://db.universal-team.net/assets/images/screenshots/mgba/file-list.png
- description: In game menu
  url: https://db.universal-team.net/assets/images/screenshots/mgba/in-game-menu.png
- description: Scale 1x
  url: https://db.universal-team.net/assets/images/screenshots/mgba/scale-1x.png
- description: Scale aspect ratio
  url: https://db.universal-team.net/assets/images/screenshots/mgba/scale-aspect-ratio.png
- description: Scale stretch
  url: https://db.universal-team.net/assets/images/screenshots/mgba/scale-stretch.png
source: https://github.com/mgba-emu/mgba
systems:
- 3DS
title: mGBA
unique_ids:
- '0x1A1E'
update_notes: '<h3 dir="auto">Emulation fixes:</h3>

  <ul dir="auto">

  <li>GBA Audio: Fix improperly deserializing GB audio registers (fixes mgba.io/i/2793)</li>

  <li>GBA Audio: Clear GB audio state when disabled</li>

  <li>GBA Memory: Make VRAM access stalls only apply to BG RAM</li>

  <li>GBA Overrides: Fix saving in PMD:RRT (JP) (fixes mgba.io/i/2862)</li>

  <li>GBA SIO: Fix SIOCNT SI pin value after attaching player 2 (fixes mgba.io/i/2805)</li>

  <li>GBA SIO: Fix unconnected normal mode SIOCNT SI bit (fixes mgba.io/i/2810)</li>

  <li>GBA SIO: Normal mode transfers with no clock should not finish (fixes mgba.io/i/2811)</li>

  <li>GBA Timers: Cascading timers don''t tick when disabled (fixes mgba.io/i/2812)</li>

  <li>GBA Video: Fix interpolation issues with OpenGL renderer</li>

  </ul>

  <h3 dir="auto">Other fixes:</h3>

  <ul dir="auto">

  <li>Core: Allow sending thread requests to a crashed core (fixes mgba.io/i/2784)</li>

  <li>FFmpeg: Force lower sample rate for codecs not supporting high rates (fixes
  mgba.io/i/2869)</li>

  <li>Qt: Fix crash when attempting to use OpenGL 2.1 to 3.1 (fixes mgba.io/i/2794)</li>

  <li>Qt: Disable sync while running scripts from main thread (fixes mgba.io/i/2738)</li>

  <li>Qt: Properly cap number of attached players by platform (fixes mgba.io/i/2807)</li>

  <li>Qt: Disable attempted linking betwen incompatible platforms (fixes mgba.io/i/2702)</li>

  <li>Qt: Fix modifier key names in shortcut editor (fixes mgba.io/i/2817)</li>

  <li>Qt: Fix a handful of edge cases with graphics viewers (fixes mgba.io/i/2827)</li>

  <li>Qt: Fix full-buffer rewind</li>

  <li>Qt: Fix crash if loading a shader fails</li>

  <li>Qt: Fix black screen when starting with a game (fixes mgba.io/i/2781)</li>

  <li>Qt: Fix OSD on modern macOS (fixes mgba.io/i/2736)</li>

  <li>Qt: Fix checked state of mute menu option at load (fixes mgba.io/i/2701)</li>

  <li>Qt: Remove OpenGL proxy thread and override SwapInterval directly instead</li>

  <li>Scripting: Fix receiving packets for client sockets</li>

  <li>Scripting: Fix empty receive calls returning unknown error on Windows</li>

  <li>Scripting: Return proper callback ID from socket.add</li>

  <li>Vita: Work around broken mktime implementation in Vita SDK (fixes mgba.io/i/2876)</li>

  </ul>

  <h3 dir="auto">Misc:</h3>

  <ul dir="auto">

  <li>Qt: Include wayland QPA in AppImage (fixes mgba.io/i/2796)</li>

  <li>Qt: Stop eating boolean action key events (fixes mgba.io/i/2636)</li>

  <li>Qt: Automatically change video file extension as appropriate</li>

  <li>Qt: Swap P1 and other player''s save if P1 loaded it first (closes mgba.io/i/2750)</li>

  </ul>'
updated: '2023-04-24T04:39:19Z'
version: 0.10.2
website: https://mgba.io/
wiki: https://github.com/mgba-emu/mgba/wiki
---
