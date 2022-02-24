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
  mGBA-0.9.3-3ds.7z:
    size: 1147367
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.9.3/mGBA-0.9.3-3ds.7z
eval_notes_md: true
github: mgba-emu/mgba
icon: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-48.png
icon_index: 31
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
update_notes: '<h3 dir="auto">Emulation fixes:</h3>

  <ul dir="auto">

  <li>GB I/O: Fix incrementing SGB controller when P14 is low (fixes mgba.io/i/2202)</li>

  <li>GB Memory: Add cursory cartridge open bus emulation (fixes mgba.io/i/2032)</li>

  <li>GB Video: Render SGB border when unmasking with ATTR/PAL_SET (fixes mgba.io/i/2261)</li>

  <li>GBA SIO: Fix SI value for unattached MULTI mode</li>

  <li>GBA Video: Fix backdrop color if DISPCNT is first set to 0 (fixes mgba.io/i/2260)</li>

  <li>GBA Video: Don''t iterate affine backgrounds when disabled</li>

  <li>GBA Video: Delay enabling backgrounds in bitmap modes (fixes mgba.io/i/1668)</li>

  </ul>

  <h3 dir="auto">Other fixes:</h3>

  <ul dir="auto">

  <li>ARM Decoder: Fix decoding of lsl r0 (fixes mgba.io/i/2349)</li>

  <li>FFmpeg: Don''t attempt to use YUV 4:2:0 for lossless videos (fixes mgba.io/i/2084)</li>

  <li>GB Video: Fix memory leak when reseting SGB games</li>

  <li>GBA: Fix out of bounds ROM accesses on patched ROMs smaller than 32 MiB</li>

  <li>GBA: Fix maximum tile ID in caching for 256-color modes</li>

  <li>GBA Video: Fix cache updating with proxy and GL renderers</li>

  <li>Libretro: Fix crash when using Game Boy codes (fixes mgba.io/i/2281)</li>

  <li>mGUI: Fix crash if autosave file can''t be opened (fixes mgba.io/i/2268)</li>

  <li>Qt: Remove potentially deadlocking optimization</li>

  <li>Qt: Fix corrupted savestate and fatal error text</li>

  <li>Qt: Fix sprite compositing when sprite tiles go out of bounds (fixes mgba.io/i/2348)</li>

  </ul>

  <h3 dir="auto">Misc:</h3>

  <ul dir="auto">

  <li>GBA I/O: Update KEYINPUT in internal I/O memory (fixes mgba.io/i/2235)</li>

  <li>SDL: Use SDL_JoystickRumble where available</li>

  <li>Wii: Add adjustable gyroscope settings (closes mgba.io/i/2245)</li>

  </ul>'
updated: '2021-12-18T02:30:42Z'
version: 0.9.3
website: https://mgba.io/
---
