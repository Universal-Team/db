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
  mGBA-0.9.1-3ds.7z:
    size: 1147259
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.9.1/mGBA-0.9.1-3ds.7z
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

  <li>ARM: Fix LDM^ with empty rlist (fixes mgba.io/i/2127)</li>

  <li>Core: Fix first event scheduling after loading savestate</li>

  <li>GB Serialize: Fix switching speed modes when loading a state (fixes mgba.io/i/2097)</li>

  <li>GB: Fix skipping BIOS</li>

  <li>GBA Memory: Fix loading Thumb savestates when in ARM mode</li>

  <li>GBA Video: Fix window start on modes 3-5 with mosaic (fixes mgba.io/i/1690)</li>

  <li>GBA Video: Fix mode 3-5 overflow with mosaic (fixes mgba.io/i/1691)</li>

  </ul>

  <h3>Other fixes:</h3>

  <ul>

  <li>GBA: Fix non-USA 1.0 FireRed misdetecting as a ROM hack (fixes mgba.io/i/2100)</li>

  <li>GBA: Fix crash when ROM loading fails</li>

  <li>GBA e-Reader: Fix bitmap short strip scanning</li>

  <li>GBA Video: Fix mode 5 frame 1 caching (fixes mgba.io/i/2075)</li>

  <li>GBA Video: Don''t attempt to copy invalid registers when switching renderer</li>

  <li>Qt: Fix crash when switching from high-resolution OpenGL renderer to software</li>

  <li>Qt: Fix OpenGL renderer lagging behind when fast-forwarding (fixes mgba.io/i/2094)</li>

  <li>Qt: Fix smudged window icon on Windows</li>

  <li>Qt: Fix saving settings enabling camera when camera name changes (fixes mgba.io/i/2125)</li>

  <li>Qt: Fix frames getting backlogged (fixes mgba.io/i/2122)</li>

  <li>Qt: Restore maximized state when starting (fixes mgba.io/i/487)</li>

  </ul>

  <h3>Misc:</h3>

  <ul>

  <li>Core: Truncate preloading ROMs that slightly exceed max size (fixes mgba.io/i/2093)</li>

  <li>GBA: Default-enable VBA bug compat for Ruby and Emerald ROM hacks</li>

  <li>GBA Memory: Log GPIO writes on non-GPIO carts as Pak Hardware instead of Memory</li>

  <li>Qt: Add ROM filename and size to bug reporter</li>

  <li>Qt: Improve handling of disabling VBA bug compat mode (fixes mgba.io/i/2129)</li>

  </ul>'
updated: '2021-04-19T05:34:38Z'
version: 0.9.1
website: https://mgba.io/
---
