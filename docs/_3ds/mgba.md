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
  mGBA-0.10.3-3ds.7z:
    size: 1202584
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.10.3/mGBA-0.10.3-3ds.7z
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
stars: 5643
systems:
- 3DS
title: mGBA
unique_ids:
- '0x1A1E'
update_notes: '<h3 dir="auto">Emulation fixes:</h3>

  <ul dir="auto">

  <li>ARM: Remove obsolete force-alignment in <code class="notranslate">bx pc</code>
  (fixes mgba.io/i/2964)</li>

  <li>ARM: Fake bpkt instruction should take no cycles (fixes mgba.io/i/2551)</li>

  <li>GB Audio: Fix channels 1/2 staying muted if restarted after long silence</li>

  <li>GB Audio: Fix channel 1 restarting if sweep applies after stop (fixes mgba.io/i/2965)</li>

  <li>GB Audio: Fix restarting envelope when writing to register (fixes mgba.io/i/3067)</li>

  <li>GB Audio: Improve "zombie mode" emulation in CGB mode (fixes mgba.io/i/2029)</li>

  <li>GB I/O: Read back proper SVBK value after writing 0 (fixes mgba.io/i/2921)</li>

  <li>GB SIO: Disabling SIO should cancel pending transfers (fixes mgba.io/i/2537)</li>

  <li>GBA Audio: Fix sample timing drifting when changing sample interval</li>

  <li>GBA Audio: Fix initial channel 3 wave RAM (fixes mgba.io/i/2947)</li>

  <li>GBA Audio: Fix sample position issues when rate changes (fixes mgba.io/i/3006)</li>

  <li>GBA GPIO: Fix tilt scale and orientation (fixes mgba.io/i/2703)</li>

  <li>GBA BIOS: Fix clobbering registers with word-sized CpuSet</li>

  <li>GBA SIO: Fix normal mode SI/SO semantics (fixes mgba.io/i/2925)</li>

  </ul>

  <h3 dir="auto">Other fixes:</h3>

  <ul dir="auto">

  <li>GB: Fix applying a patch that changes the cartridge mapper (fixes mgba.io/i/3077)</li>

  <li>GBA Savedata: Fix crash when resizing flash save games for RTC data</li>

  <li>mGUI: Fix cases where an older save state screenshot would be shown (fixes mgba.io/i/2183)</li>

  <li>Qt: Re-enable sync for multiplayer windows that aren''t connected (fixes mgba.io/i/2974)</li>

  <li>Qt: Fix mute settings not being loaded on setting screen (fixes mgba.io/i/2990)</li>

  <li>Qt: Fix screen freezing on macOS after closing save state window (fixes mgba.io/i/2885)</li>

  <li>Vita: Fix camera setting not appearing (fixes mgba.io/i/3012)</li>

  </ul>

  <h3 dir="auto">Misc:</h3>

  <ul dir="auto">

  <li>mGUI: Persist fast forwarding after closing menu (fixes mgba.io/i/2414)</li>

  <li>Qt: Add exporting of SAV + RTC saves from Save Converter to strip RTC data</li>

  <li>VFS: Use anonymousMemoryMap for large 7z allocations (fixes mgba.io/i/3013)</li>

  </ul>'
updated: '2024-01-08T04:01:37Z'
version: 0.10.3
website: https://mgba.io/
wiki: https://github.com/mgba-emu/mgba/wiki
---
