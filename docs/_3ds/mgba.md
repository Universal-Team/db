---
author: mGBA
avatar: https://avatars.githubusercontent.com/u/10085927?v=4
categories:
- emulator
color: '#503a7e'
created: '2014-12-09T21:37:23Z'
description: mGBA Game Boy Advance Emulator
download_page: https://github.com/mgba-emu/mgba/releases
downloads:
  mGBA-0.9.2-3ds.7z:
    size: 1146807
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.9.2/mGBA-0.9.2-3ds.7z
eval_notes_md: true
github: mgba-emu/mgba
icon: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-48.png
image: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-256.png
image_length: 43839
layout: app
license: mpl-2.0
license_name: Mozilla Public License 2.0
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
update_notes: '<h3>Emulation fixes:</h3>

  <ul>

  <li>GB Video: Clear VRAM on reset (fixes mgba.io/i/2152)</li>

  <li>GBA SIO: Add missing NORMAL8 implementation bits (fixes mgba.io/i/2172)</li>

  <li>GBA SIO: Fix missing interrupt on an unattached NORMAL transfer</li>

  <li>GBA Memory: Fix prefetch mask when swapping modes within a region</li>

  <li>GBA Serialize: Fix loading audio enable bit late (fixes mgba.io/i/2230)</li>

  <li>GBA Video: Revert scanline latching changes (fixes mgba.io/i/2153, mgba.io/i/2149)</li>

  </ul>

  <h3>Other fixes:</h3>

  <ul>

  <li>3DS: Fix disabling "wide" mode on 2DS (fixes mgba.io/i/2167)</li>

  <li>ARM Debugger: Fix disassembly alignment (fixes mgba.io/i/2204)</li>

  <li>Core: Fix memory leak in opening games from the library</li>

  <li>Core: Fix memory searches for relative values (fixes mgba.io/i/2135)</li>

  <li>Core: Fix portable mode on macOS</li>

  <li>GB Audio: Fix audio channel 4 being slow to deserialize</li>

  <li>GB Core: Fix GBC colors setting breaking default model overrides (fixes mgba.io/i/2161)</li>

  <li>mGUI: Cache save state screenshot validity in state menu (fixes mgba.io/i/2005)</li>

  <li>Qt: Fix eventual deadlock when using sync to video</li>

  <li>Qt: Fix applying savetype-only overrides</li>

  <li>Qt: Fix crash in sprite view for partially out-of-bounds sprites (fixes mgba.io/i/2165)</li>

  <li>Qt: Fix having to press controller buttons twice for menu items (fixes mgba.io/i/2143)</li>

  <li>Qt: Redo sensor binding to be less fragile</li>

  <li>Qt: Reuse timer when rescheduling missing frames (fixes mgba.io/i/2236)</li>

  <li>Qt: Fix bounded fast forward with enhancement OpenGL renderer</li>

  <li>Util: Fix loading UPS patches that affect the last byte of the file</li>

  </ul>

  <h3>Misc:</h3>

  <ul>

  <li>Util: Improve speed of UPS patch loading</li>

  </ul>'
updated: '2021-07-11T04:19:14Z'
version: 0.9.2
website: https://mgba.io/
---
