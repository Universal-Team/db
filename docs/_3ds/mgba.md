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
  mGBA-0.10.1-3ds.7z:
    size: 1197171
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.10.1/mGBA-0.10.1-3ds.7z
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

  <li>GB Audio: Fix channels 1/2 not playing when resetting volume (fixes mgba.io/i/2614)</li>

  <li>GB Audio: Fix channel 3 volume being changed between samples (fixes mgba.io/i/1896)</li>

  <li>GB Audio: Fix up boot sequence</li>

  <li>GB Audio: Fix updating channels other than 2 when writing NR5x</li>

  <li>GB Memory: Actually, HDMAs should start when LCD is off (fixes mgba.io/i/2662)</li>

  <li>GB Serialize: Don''t write BGP/OBP when loading SCGB state (fixes mgba.io/i/2694)</li>

  <li>GB SIO: Further fix bidirectional transfer starting</li>

  <li>GBA: Fix resetting key IRQ state (fixes mgba.io/i/2716)</li>

  <li>GBA BIOS: Include timing in degenerate ArcTan2 cases (fixes mgba.io/i/2763)</li>

  <li>GBA Video: Ignore disabled backgrounds as OBJ blend target (fixes mgba.io/i/2489)</li>

  </ul>

  <h3 dir="auto">Other fixes:</h3>

  <ul dir="auto">

  <li>GBA: Fix forceskip BIOS logic for multiboot ROMs (fixes mgba.io/i/2753)</li>

  <li>GBA Cheats: Fix issues detecting unencrypted cheats (fixes mgba.io/i/2724)</li>

  <li>Qt: Manually split filename to avoid overzealous splitting (fixes mgba.io/i/2681)</li>

  <li>Qt: Fix scanning specific e-Reader dotcodes (fixes mgba.io/i/2693)</li>

  <li>Qt: Don''t re-enable sync if GBA link modes aren''t the same (fixes mgba.io/i/2044)</li>

  <li>Qt: Improve handling of multiplayer syncing (fixes mgba.io/i/2720)</li>

  <li>Qt: Fix initializing update revision info</li>

  <li>Qt: Redo stable branch detection heuristic (fixes mgba.io/i/2679)</li>

  <li>Res: Fix species name location in Ruby/Sapphire revs 1/2 (fixes mgba.io/i/2685)</li>

  <li>VFS: Fix minizip write returning 0 on success instead of size</li>

  </ul>

  <h3 dir="auto">Misc:</h3>

  <ul dir="auto">

  <li>macOS: Add category to plist (closes mgba.io/i/2691)</li>

  <li>macOS: Fix modern build with libepoxy (fixes mgba.io/i/2700)</li>

  <li>Qt: Keep track of current palette preset name (fixes mgba.io/i/2680)</li>

  <li>Qt: Move OpenGL proxy onto its own thread (fixes mgba.io/i/2493)</li>

  </ul>'
updated: '2023-01-11T04:13:19Z'
version: 0.10.1
website: https://mgba.io/
wiki: https://github.com/mgba-emu/mgba/wiki
---
