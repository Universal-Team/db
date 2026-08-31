---
author: estebanpdn
avatar: https://avatars.githubusercontent.com/u/72305261?v=4
categories:
- game
color: '#a58c65'
color_bg: '#806c4e'
created: '2026-07-27T22:06:01Z'
description: Nintendo 3DS dual-screen port of Zelda A Link to the Past based on zelda3
download_filter: 3dsx|cia
download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases
downloads:
  zelda3-3ds-v2.9.3dsx:
    size: 5683548
    size_str: 5 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/zelda3-3ds-v2.9.3dsx
  zelda3-3ds-v2.9.cia:
    size: 5227456
    size_str: 4 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/zelda3-3ds-v2.9.cia
github: EstebanPdN/zelda-alttp-3ds
icon: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udicon.png
image: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udbanner.png
image_length: 34742
layout: app
llm_generation: 'yes'
preinstall_message: Place a legally obtained USA, unheadered ROM in sdmc:/3ds/Zelda
  3DS/. The preferred filename is zelda3.sfc, but the setup also accepts other .sfc
  or .smc filenames.
prerelease:
  download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/tag/v3.0-E6
  downloads:
    zelda3-3ds-v3.0-E6.3dsx:
      size: 5697384
      size_str: 5 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E6/zelda3-3ds-v3.0-E6.3dsx
    zelda3-3ds-v3.0-E6.cia:
      size: 5215168
      size_str: 4 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E6/zelda3-3ds-v3.0-E6.cia
  qr:
    zelda3-3ds-v3.0-E6.cia: https://db.universal-team.net/assets/images/qr/prerelease/zelda3-3ds-v3-0-e6-cia.png
  update_notes: '<div class="markdown-alert markdown-alert-warning" dir="auto"><p
    class="markdown-alert-title" dir="auto"><svg data-component="Octicon" class="octicon
    octicon-alert mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path
    d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082
    15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25
    0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75
    0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>Warning</p><p dir="auto">This
    is an experimental release. You may encounter bugs, crashes, graphical issues,
    or other unexpected behavior.</p>

    </div>

    <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E6/QR-v3.0-E6-github.png"><img
    src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E6/QR-v3.0-E6-github.png"
    alt="QR-v3.0-E6-github.png" style="max-width: 100%;"></a></p>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Fixed the WIDE + FIXED camera map.</li>

    <li>Added the custom 3D HOME Menu logo.</li>

    <li>Improved Old 3DS bottom-screen responsiveness.</li>

    <li>Updated and reduced the 3D HOME Menu logo model.</li>

    <li>Added saved bottom-screen display and turbo settings.</li>

    <li>Improved bottom-HUD spacing.</li>

    <li>Reduced GPU and PCM-audio cache-clean overhead on Old 3DS.</li>

    <li>Removed the normal full linear-heap frame flush.</li>

    <li>Reduced render-target bandwidth and VRAM use with color-only RGB565 output.</li>

    <li>Removed unused build sections.</li>

    <li>Added the Minish Cap-style <code class="notranslate">DUMP SAVED</code> notice
    and optional top-screen FPS.</li>

    <li>Added a confirmed Developer &gt; Load State action for the newest validated<br>

    quick-dump checkpoint, protected against corrupt or wrong-ROM states.</li>

    <li>Made the Old 3DS Developer overlay event-driven and fixed the blue/glitched<br>

    bottom screen shown when Developer/FPS diagnostics were enabled.</li>

    <li>Kept the top counter as <code class="notranslate">FPS &lt;value&gt;</code>
    without CPU/GPU suffixes and fixed the<br>

    truncated <code class="notranslate">DUMP SAVED</code> text.</li>

    <li>Restored E4''s verified BGRX top-screen path and corrected the PPU output<br>

    origin that corrupted E5''s ORIGINAL and WIDE images.</li>

    <li>Restored full tile-row caches and added conservative, full-quality PPU fast<br>

    paths for the Old 3DS profile.</li>

    <li>Replaced logical-canvas screenshots with physical 400x240 and 320x240 GSP<br>

    display captures plus raw framebuffer files.</li>

    <li>Paused queued NDSP audio for the complete dump transaction and excluded the<br>

    dump I/O frame from later performance metrics.</li>

    </ul>

    <h2 dir="auto">Bug reports</h2>

    <p dir="auto">If a problem occurs, press <code class="notranslate">L + R + A</code>
    while it is visible and attach the dump from <code class="notranslate">sdmc:/3ds/Zelda
    3DS/dumps/</code>. Completed E6 dumps include physical screen captures, raw framebuffers
    and <code class="notranslate">load-state.bin</code> for Developer &gt; Load State.</p>'
  update_notes_md: "> [!WARNING]\n> This is an experimental release. You may encounter\
    \ bugs, crashes, graphical issues, or other unexpected behavior.\n\n![QR-v3.0-E6-github.png](https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E6/QR-v3.0-E6-github.png)\n\
    \n## Changelog\n\n- Fixed the WIDE + FIXED camera map.\n- Added the custom 3D\
    \ HOME Menu logo.\n- Improved Old 3DS bottom-screen responsiveness.\n- Updated\
    \ and reduced the 3D HOME Menu logo model.\n- Added saved bottom-screen display\
    \ and turbo settings.\n- Improved bottom-HUD spacing.\n- Reduced GPU and PCM-audio\
    \ cache-clean overhead on Old 3DS.\n- Removed the normal full linear-heap frame\
    \ flush.\n- Reduced render-target bandwidth and VRAM use with color-only RGB565\
    \ output.\n- Removed unused build sections.\n- Added the Minish Cap-style `DUMP\
    \ SAVED` notice and optional top-screen FPS.\n- Added a confirmed Developer >\
    \ Load State action for the newest validated\n  quick-dump checkpoint, protected\
    \ against corrupt or wrong-ROM states.\n- Made the Old 3DS Developer overlay event-driven\
    \ and fixed the blue/glitched\n  bottom screen shown when Developer/FPS diagnostics\
    \ were enabled.\n- Kept the top counter as `FPS <value>` without CPU/GPU suffixes\
    \ and fixed the\n  truncated `DUMP SAVED` text.\n- Restored E4's verified BGRX\
    \ top-screen path and corrected the PPU output\n  origin that corrupted E5's ORIGINAL\
    \ and WIDE images.\n- Restored full tile-row caches and added conservative, full-quality\
    \ PPU fast\n  paths for the Old 3DS profile.\n- Replaced logical-canvas screenshots\
    \ with physical 400x240 and 320x240 GSP\n  display captures plus raw framebuffer\
    \ files.\n- Paused queued NDSP audio for the complete dump transaction and excluded\
    \ the\n  dump I/O frame from later performance metrics.\n\n## Bug reports\n\n\
    If a problem occurs, press `L + R + A` while it is visible and attach the dump\
    \ from `sdmc:/3ds/Zelda 3DS/dumps/`. Completed E6 dumps include physical screen\
    \ captures, raw framebuffers and `load-state.bin` for Developer > Load State.\n"
  updated: '2026-08-31T10:25:02Z'
  version: v3.0-E6
  version_title: v3.0-E6
qr:
  zelda3-3ds-v2.9.cia: https://db.universal-team.net/assets/images/qr/zelda3-3ds-v2-9-cia.png
source: https://github.com/EstebanPdN/zelda-alttp-3ds
stars: 629
systems:
- 3DS
title: zelda-alttp-3ds
unique_ids:
- '0x5A20D'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/QR-v2.9-github.png"><img
  src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/QR-v2.9-github.png"
  alt="QR-v2.9-github.png" style="max-width: 100%;"></a></p>

  <ul dir="auto">

  <li>Fixed the map problem when using WIDE mode with FIXED camera.</li>

  <li>Changed the 3D HOME Menu banner to the custom logo model, with logo help from
  <a href="https://github.com/Phibonacci">Phibonacci</a>, based on the original 3D
  model by <a href="https://sketchfab.com/TiraArt" rel="nofollow">TiraArt</a>.</li>

  <li>Fixed Old 3DS bottom-screen responsiveness and more optimizations.</li>

  </ul>'
updated: '2026-08-04T00:21:10Z'
version: v2.9
version_title: v2.9
---
A native Nintendo 3DS dual-screen port of **The Legend of Zelda: A Link to the Past**, based on the open-source Zelda3 engine.

The top screen displays the main game, while the bottom screen provides a live map, dungeon information, equipment, items, and settings.

## Features

- Native Nintendo 3DS port
- Dual-screen interface
- Original, Stretch, and Wide display modes
- Fixed and Standard camera options for Wide Mode
- Support for New Nintendo 3DS and Old Nintendo 3DS systems
- 60 FPS gameplay on New Nintendo 3DS
- Multiple ROM profiles with separate saves and settings
- Support for certain translated ROMs
- CIA and Homebrew Launcher versions
- Diagnostic dumps for easier bug reporting

## Requirements

This download does **not** include the original game ROM or copyrighted game assets.

Users must provide their own legally obtained, unheadered **USA version 1.0 ROM** and place it inside:

`sdmc:/3ds/Zelda 3DS/`

On the first launch, the port validates the ROM and extracts the required assets locally on the console.