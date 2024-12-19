---
author: mGBA
avatar: https://private-avatars.githubusercontent.com/u/10085927?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MzQ2NDMzMjAsIm5iZiI6MTczNDY0MjEyMCwicGF0aCI6Ii91LzEwMDg1OTI3In0.DFqKv0RuBFeCLjR8OM9LSzymezTLKYLNXYvyj_km834&v=4
categories:
- emulator
color: '#503a7e'
color_bg: '#503a7e'
created: '2014-12-09T21:37:23Z'
description: mGBA Game Boy Advance Emulator
download_page: https://github.com/mgba-emu/mgba/releases
downloads:
  mGBA-0.10.4-3ds.7z:
    size: 1211751
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.10.4/mGBA-0.10.4-3ds.7z
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
stars: 5791
systems:
- 3DS
title: mGBA
unique_ids:
- '0x1A1E'
update_notes: '<h3 dir="auto">Emulation fixes:</h3>

  <ul dir="auto">

  <li>GB Audio: Fix audio envelope timing resetting too often (fixes mgba.io/i/3164)</li>

  <li>GB I/O: Fix STAT writing IRQ trigger conditions (fixes mgba.io/i/2501)</li>

  <li>GBA GPIO: Fix gyro read-out start (fixes mgba.io/i/3141)</li>

  <li>GBA I/O: Fix HALTCNT access behavior (fixes mgba.io/i/2309)</li>

  <li>GBA I/O: Fix audio register 8-bit write behavior (fixes mgba.io/i/3086)</li>

  <li>GBA Serialize: Properly restore GPIO register state (fixes mgba.io/i/3294)</li>

  <li>GBA SIO: Fix MULTI mode SIOCNT bit 7 writes on secondary GBAs (fixes mgba.io/i/3110)</li>

  </ul>

  <h3 dir="auto">Other fixes:</h3>

  <ul dir="auto">

  <li>Core: Fix patch autoloading leaking the file handle</li>

  <li>GB: Fix uninitialized save data when loading undersized temporary saves</li>

  <li>GB, GBA Core: Fix memory leak if reloading debug symbols</li>

  <li>GB Serialize: Prevent loading invalid states where LY &gt;= 144 in modes other
  than 1</li>

  <li>GBA Audio: Fix crash if audio FIFOs and timers get out of sync</li>

  <li>GBA Audio: Fix crash in audio subsampling if timing lockstep breaks</li>

  <li>GBA Core: Fix loading symbols from ELF files if the file doesn''t end with .elf</li>

  <li>GBA Memory: Let raw access read high MMIO addresses</li>

  <li>Qt: Fix crash when applying changes to GB I/O registers in I/O view</li>

  <li>Qt: Fix LCDC background priority/enable bit being mis-mapped in I/O view</li>

  <li>Qt: Fix saving named states breaking when screenshot states disabled (fixes
  mgba.io/i/3320)</li>

  <li>Qt: Fix potential crash on Wayland with OpenGL (fixes mgba.io/i/3276)</li>

  <li>Qt: Fix installer updates if a version number is in the filename (fixes mgba.io/i/3109)</li>

  <li>Updater: Fix updating appimage across filesystems</li>

  </ul>

  <h3 dir="auto">Misc:</h3>

  <ul dir="auto">

  <li>Qt: Make window corners square on Windows 11 (fixes mgba.io/i/3285)</li>

  <li>Switch: Add bilinear filtering option (closes mgba.io/i/3111)</li>

  <li>Vita: Add imc0 and xmc0 mount point support</li>

  </ul>'
updated: '2024-12-08T05:18:53Z'
version: 0.10.4
website: https://mgba.io/
wiki: https://github.com/mgba-emu/mgba/wiki
---
