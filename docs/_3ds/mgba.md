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
  mGBA-0.10.0-3ds.7z:
    size: 1196321
    size_str: 1 MiB
    url: https://github.com/mgba-emu/mgba/releases/download/0.10.0/mGBA-0.10.0-3ds.7z
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
update_notes: '<h3 dir="auto">Features:</h3>

  <ul dir="auto">

  <li>Preliminary Lua scripting support</li>

  <li>Presets for Game Boy palettes</li>

  <li>Add Super Game Boy palettes for original Game Boy games</li>

  <li>Tool for converting scanned pictures of e-Reader cards to raw dotcode data</li>

  <li>Options for muting when inactive, minimized, or for different players in multiplayer</li>

  <li>Cheat code support in homebrew ports</li>

  <li>Acclerometer and gyro support for controllers on PC</li>

  <li>Support for combo "Super Game Boy Color" SGB + GBC ROM hacks</li>

  <li>Improved support for HuC-3 mapper, including RTC</li>

  <li>Support for 64 kiB SRAM saves used in some bootlegs</li>

  <li>Discord Rich Presence now supports time elapsed</li>

  <li>Additional scaling shaders</li>

  <li>Support for GameShark Advance SP (.gsv) save file importing</li>

  <li>Support for multiple saves per game using .sa2, .sa3, etc.</li>

  <li>Support for GBX format Game Boy ROMs</li>

  <li>New unlicensed GB mappers: NT (newer type), Sachen (MMC1, MMC2)</li>

  </ul>

  <h3 dir="auto">Emulation fixes:</h3>

  <ul dir="auto">

  <li>ARM7: Fix unsigned multiply timing</li>

  <li>GB: Copy logo from ROM if not running the BIOS intro (fixes mgba.io/i/2378)</li>

  <li>GB: Fix HALT breaking M-cycle alignment (fixes mgba.io/i/250)</li>

  <li>GB Audio: Fix channel 1/2 reseting edge cases (fixes mgba.io/i/1925)</li>

  <li>GB Audio: Properly apply per-model audio differences</li>

  <li>GB Audio: Revamp channel rendering</li>

  <li>GB Audio: Fix APU re-enable timing glitch</li>

  <li>GB I/O: Fix writing to WAVE RAM behavior (fixes mgba.io/i/1334)</li>

  <li>GB MBC: Fix edge case with Pocket Cam register accesses (fixes mgba.io/i/2557)</li>

  <li>GB Memory: Add cursory cartridge open bus emulation (fixes mgba.io/i/2032)</li>

  <li>GB Serialize: Fix loading MBC1 states that affect bank 0 (fixes mgba.io/i/2402)</li>

  <li>GB SIO: Fix bidirectional transfer starting (fixes mgba.io/i/2290)</li>

  <li>GB Video: Draw SGB border pieces that overlap GB graphics (fixes mgba.io/i/1339)</li>

  <li>GBA: Improve timing when not booting from BIOS</li>

  <li>GBA: Fix expected entry point for multiboot ELFs (fixes mgba.io/i/2450)</li>

  <li>GBA: Fix booting multiboot ROMs with no JOY entrypoint</li>

  <li>GBA: Fix 1 MiB ROM mirroring to only mirror 4 times</li>

  <li>GBA Audio: Adjust PSG sampling rate with SOUNDBIAS</li>

  <li>GBA Audio: Sample FIFOs at SOUNDBIAS-set frequency</li>

  <li>GBA BIOS: Work around IRQ handling hiccup in Mario &amp; Luigi (fixes mgba.io/i/1059)</li>

  <li>GBA BIOS: Initial HLE timing estimation of UnLz77 functions (fixes mgba.io/i/2141)</li>

  <li>GBA DMA: Fix DMA source direction bits being cleared (fixes mgba.io/i/2410)</li>

  <li>GBA I/O: Redo internal key input, enabling edge-based key IRQs</li>

  <li>GBA I/O: Disable open bus behavior on invalid register 06A</li>

  <li>GBA Memory: Fix misaligned 32-bit I/O loads (fixes mgba.io/i/2307)</li>

  <li>GBA Video: Fix OpenGL rendering on M1 Macs</li>

  <li>GBA Video: Ignore horizontally off-screen sprite timing (fixes mgba.io/i/2391)</li>

  <li>GBA Video: Fix Hblank timing (fixes mgba.io/i/2131, mgba.io/i/2310)</li>

  <li>GBA Video: Fix rare crash in modes 3-5</li>

  <li>GBA Video: Fix sprites with mid-frame palette changes in GL (fixes mgba.io/i/2476)</li>

  <li>GBA Video: Fix OBJ tile wrapping with 2D char mapping (fixes mgba.io/i/2443)</li>

  <li>GBA Video: Fix horizontal lines in GL when charbase is changed (fixes mgba.io/i/1631)</li>

  <li>GBA Video: Fix sprite layer priority updating in GL</li>

  </ul>

  <h3 dir="auto">Other fixes:</h3>

  <ul dir="auto">

  <li>ARM: Disassemble Thumb mov pseudo-instruction properly</li>

  <li>ARM: Disassemble ARM asr/lsr <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="84864002" data-permission-text="Title is private" data-url="https://github.com/mgba-emu/mgba/issues/32"
  data-hovercard-type="issue" data-hovercard-url="/mgba-emu/mgba/issues/32/hovercard"
  href="https://github.com/mgba-emu/mgba/issues/32">#32</a> properly</li>

  <li>ARM: Disassemble ARM movs properly</li>

  <li>Core: Don''t attempt to restore rewind diffs past start of rewind</li>

  <li>Core: Fix the runloop resuming after a game has crashed (fixes mgba.io/i/2451)</li>

  <li>Core: Fix crash if library can''t be opened</li>

  <li>Debugger: Fix crash with extremely long CLI strings</li>

  <li>Debugger: Fix multiple conditional watchpoints at the same address</li>

  <li>FFmpeg: Fix crash when encoding audio with some containers</li>

  <li>FFmpeg: Fix GIF recording (fixes mgba.io/i/2393)</li>

  <li>GB: Fix temporary saves</li>

  <li>GB: Fix replacing the ROM crashing when accessing ROM base</li>

  <li>GB: Don''t try to map a 0-byte SRAM (fixes mgba.io/i/2668)</li>

  <li>GB, GBA: Save writeback-pending masked saves on unload (fixes mgba.io/i/2396)</li>

  <li>mGUI: Fix FPS counter after closing menu</li>

  <li>Qt: Fix some hangs when using the debugger console</li>

  <li>Qt: Fix crash when clicking past last tile in viewer</li>

  <li>Qt: Fix preloading for ROM replacing</li>

  <li>Qt: Fix screen not displaying on Wayland (fixes mgba.io/i/2190)</li>

  <li>Qt: Fix crash when selecting 256-color sprite in sprite view</li>

  <li>Qt: Fix coloration of swatches on styles with distinct frame backgrounds</li>

  <li>VFS: Failed file mapping should return NULL on POSIX</li>

  </ul>

  <h3 dir="auto">Misc:</h3>

  <ul dir="auto">

  <li>Core: Suspend runloop when a core crashes</li>

  <li>Core: Add wallclock offset RTC type</li>

  <li>Debugger: Save and restore CLI history</li>

  <li>Debugger: GDB now works while the game is paused</li>

  <li>Debugger: Add command to load external symbol file (fixes mgba.io/i/2480)</li>

  <li>FFmpeg: Support dynamic audio sample rate</li>

  <li>GB: Support CGB0 boot ROM loading</li>

  <li>GB Audio: Increase sample rate</li>

  <li>GB MBC: Filter out MBC errors when cartridge is yanked (fixes mgba.io/i/2488)</li>

  <li>GB MBC: Partially implement TAMA5 RTC</li>

  <li>GB Video: Add default SGB border</li>

  <li>GBA: Automatically skip BIOS if ROM has invalid logo</li>

  <li>GBA: Refine multiboot detection (fixes mgba.io/i/2192)</li>

  <li>GBA Cheats: Implement "never" type codes (closes mgba.io/i/915)</li>

  <li>GBA DMA: Enhanced logging (closes mgba.io/i/2454)</li>

  <li>GBA Memory: Implement adjustable EWRAM waitstates (closes mgba.io/i/1276)</li>

  <li>GBA Savedata: Store RTC data in savegames (closes mgba.io/i/240)</li>

  <li>GBA Video: Implement layer placement for OpenGL renderer (fixes mgba.io/i/1962)</li>

  <li>GBA Video: Fix highlighting for sprites with mid-frame palette changes</li>

  <li>mGUI: Add margin to right-aligned menu text (fixes mgba.io/i/871)</li>

  <li>mGUI: Autosave less frequently when fast-forwarding</li>

  <li>Qt: Rearrange menus some</li>

  <li>Qt: Clean up cheats dialog</li>

  <li>Qt: Only set default controller bindings if loading fails (fixes mgba.io/i/799)</li>

  <li>Qt: Save converter now supports importing GameShark Advance saves</li>

  <li>Qt: Save positions of multiplayer windows (closes mgba.io/i/2128)</li>

  <li>Qt: Add optional frame counter to OSD (closes mgba.io/i/1728)</li>

  <li>Qt: Add optional emulation-related information on reset (closes mgba.io/i/1780)</li>

  <li>Qt: Add QOpenGLWidget cross-thread codepath for macOS (fixes mgba.io/i/1754)</li>

  <li>Qt: Enable -b for Boot BIOS menu option (fixes mgba.io/i/2074)</li>

  <li>Qt: Add tile range selection to tile viewer (closes mgba.io/i/2455)</li>

  <li>Qt: Show warning if XQ audio is toggled while loaded (fixes mgba.io/i/2295)</li>

  <li>Qt: Add e-Card passing to the command line (closes mgba.io/i/2474)</li>

  <li>Qt: Boot both a multiboot image and ROM with CLI args (closes mgba.io/i/1941)</li>

  <li>Qt: Improve cheat parsing (fixes mgba.io/i/2297)</li>

  <li>Qt: Change lossless setting to use WavPack audio</li>

  <li>Qt: Use FFmpeg to convert additional camera formats, if available</li>

  <li>Qt: Resume crashed game when loading a save state</li>

  <li>Qt: Include cheats in bug report</li>

  <li>SDL: Support exposing an axis directly as the gyro value (closes mgba.io/i/2531)</li>

  <li>Windows: Attach to console if present</li>

  <li>VFS: Early return NULL if attempting to map 0 bytes from a file</li>

  <li>Vita: Add bilinear filtering option (closes mgba.io/i/344)</li>

  </ul>'
updated: '2022-10-12T03:59:49Z'
version: 0.10.0
website: https://mgba.io/
---
