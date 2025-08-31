---
author: AlekMaul / wavemotion-dave
avatar: https://avatars.githubusercontent.com/u/75039837?v=4
categories:
- emulator
color: '#4a4a42'
color_bg: '#4a4a42'
created: '2021-11-09T21:09:48Z'
description: ColecoDS - An Emulator for the DS/DSi. Original port by Alekmaul. Phoenix-Edition
  by Wavemotion with support for Colecovision, ADAM, MSX1, Sord-M5, Memotech MTX,
  Spectravision SVI, Hanimex Pencil II, Tatung Einstein, SG-1000/SC-3000 and the Creativision.
download_page: https://github.com/wavemotion-dave/ColecoDS/releases
downloads:
  ColecoDS.nds:
    size: 1462784
    size_str: 1 MiB
    url: https://github.com/wavemotion-dave/ColecoDS/releases/download/10.7/ColecoDS.nds
  README.md:
    size: 55805
    size_str: 54 KiB
    url: https://github.com/wavemotion-dave/ColecoDS/releases/download/10.7/README.md
  cbios.txt:
    size: 2265
    size_str: 2 KiB
    url: https://github.com/wavemotion-dave/ColecoDS/releases/download/10.7/cbios.txt
github: wavemotion-dave/ColecoDS
icon: https://db.universal-team.net/assets/images/icons/colecods.png
image: https://raw.githubusercontent.com/wavemotion-dave/ColecoDS/main/arm9/gfx_data/pdev_tbg0.png
image_length: 15870
layout: app
qr:
  ColecoDS.nds: https://db.universal-team.net/assets/images/qr/colecods-nds.png
source: https://github.com/wavemotion-dave/ColecoDS
stars: 49
systems:
- DS
title: ColecoDS
update_notes: '<p dir="auto">V10.7: 31-Aug-2025 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Removed proprietary cart handing by request.</li>

  </ul>

  <p dir="auto">V10.6: 30-Aug-2025 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Minor cleanup and refactor - added 6502 debugger.</li>

  <li>Tweaks to MSX beeper.</li>

  <li>Updated README.md after Z80 and 6502 compatibility tests run.</li>

  <li>Reduced the max ADAM RAM extended memory to 1MB for compatibility reasons.</li>

  </ul>

  <p dir="auto">V10.5: 14-Mar-2025 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Update to the Z80 core to improve emulation accuracy. This emulator now passes
  the ZEXALL test suite.</li>

  <li>Added proper M1 wait states for the Colecovision, ADAM and MSX emulation for
  improved CPU handling.</li>

  <li>A few optimized Z80 lookup-tables brings in some additional speed for both the
  DSi and DS-Lite/Phat.</li>

  <li>Improved file loading so that it''s more robust - ensuring a higher level of
  consistency in loading large files into memory.</li>

  <li>Other minor cleanups as time permitted.</li>

  </ul>

  <p dir="auto">V10.4: 10-Mar-2025 by wavemotion-dave</p>

  <ul dir="auto">

  <li>DSi now supports cart ROMs up to 4MB (4096K). Only a few MSX tech demos / games
  get anywhere near this.</li>

  <li>New super-simplified Colecovision CPU driver that is used for most of the well-behaved
  Colecovision games to render them full speed on the older DS-Lite/Phat.</li>

  <li>Improved emulation speed of the 6502 core to render all Creativision games at
  full speed on older DS-Lite/Phat.</li>

  <li>Corrected a few cycle timings and generally improved accuracy of the Z80 CPU
  driver.</li>

  </ul>

  <p dir="auto">V10.3: 15-Nov-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Added support for the 31-in-1 and 63-in-1 multicarts.</li>

  <li>Added support for ''Wave Direct'' sound driver to render digitized speech in
  games such as Sewer Sam, Squish-Em, Wizard of Wor, etc.</li>

  </ul>

  <p dir="auto">V10.2: 05-Nov-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Fix for SGM enable/disable that renders The Castle and Castle Excellent playable.</li>

  <li>Auto-disable SGM for Cavern Fighter to render it playable.</li>

  <li>Three year anniversary of the Phoenix Edition - Happy Birthday ColecoDS!</li>

  </ul>

  <p dir="auto">V10.1: 03-Sep-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Fix for the ADC decimal-mode instruction in the 6502 core for the CreatiVision.
  This fixes a number of problems including hex-digits showing on scores for some
  games.</li>

  <li>Tweaks and optimizations for the CreatiVision driver. Added most of the common/stable
  ''undocumented'' opcodes.</li>

  <li>Improved emulation accuracy for the ADAM with memory now initialized to alternating
  0x00 (even bytes) and 0xFF (odd bytes) per AdamEM and experiments from Shawn Merrick.</li>

  </ul>

  <p dir="auto">V10.0: 10-Aug-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Adam Sound Enhancer module support to allow AY sound games to play (mostly MSX
  ports to the ADAM)</li>

  <li>Ignore files that start with a ''.'' or ''_'' (mostly to help filter out clear
  non-game files).</li>

  <li>Minor cleanup, tweaks and a bug fixes.</li>

  </ul>

  <p dir="auto">V9.9: 02-May-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Added overlays for Blackjack and War Room. Improved War Games overlay.</li>

  <li>Added KANA lock LED indicator for Japanese MSX keyboard layouts.</li>

  <li>Correctly read-back the PPG Port B (needed to make the KANA lock work but is
  more accurate overall).</li>

  <li>Improvements to various Coleco PCB types for more accurate emulation.</li>

  </ul>

  <p dir="auto">V9.8: 23-Apr-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Cleanup of MSX BIOS handling - we now support the Panasonic CF-2700 directly.
  See MSX BIOS section for details.</li>

  <li>MSX status line now shows RAM (based on machine chosen) on the status line (was
  previously showing ROM size which no other machine in ColecoDS did).</li>

  <li>MSX Caps Lock now has LED indicator on the virtual keyboard.</li>

  <li>Added ROM/CAS/DSK size and CRC32 on the main screen after choosing a game.</li>

  <li>Numerous fixes for Save/Load states especially for the MSX and Einstein.</li>

  <li>Improved memory handling to free up some DS resources for future expansion.</li>

  </ul>

  <p dir="auto">V9.7: 16-Apr-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Fixed Colecovision RAM mirrors such that Boulderdash runs properly.</li>

  <li>The Heist now forces RAM to clear (all zeros) as it is known to be picky about
  contents of RAM on power up.</li>

  <li>Fix EEPROM sequential reads so Activision PCB games like Jewel Panic work correctly.</li>

  <li>Added the Wildcard and Print buttons on the virtual ADAM keyboard. All ADAM
  virtual keys should now be present.</li>

  <li>Added new configuration options to select the Colecovision mode to run in -
  you can force ADAM emulation, force PCB types, and set EEPROM sizes, etc.</li>

  <li>New global option to force ADAM mode, SGM can be Disabled, and BIOS auto-patch
  for ''Fast BIOS'' to force the 15 second wait down to 3 seconds.</li>

  <li>Minor cleanup and optimization to the Adam core.</li>

  </ul>

  <p dir="auto">V9.6: 08-Apr-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Removed DrZ80 core - the high quality CZ80 core is all that remains.</li>

  <li>Complete overhaul of the Adam handlers to clean and refine.</li>

  <li>Fix for games like Best of Broderbund (dsk and ddp) now load properly.</li>

  </ul>

  <p dir="auto">V9.5: 30-Mar-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>ADAMnet improvement for disk/tape handling. Improved timing, improved caching
  and more disk/tape games should load and run correctly.</li>

  <li>DSI gets a massive 2MB of Expansion RAM (32 banks of 64K). DS-Lite/Phat still
  has 128K (base 64K plus the standard 64K expansion RAM).</li>

  <li>Adam now properly handles 320K disks and three drive bays are virtually attached
  (two 320K disk drives and the internal Tape drive at 256K).</li>

  <li>Adam full keyboard now uses an LED indicator under the CAPS LOCK button to indicate
  status.</li>

  <li>Adam has improved keyboard graphic with more keys added.</li>

  <li>Adam no longer mirrors RAM as a Colecovision would.</li>

  <li>Adam optimization provided 5% improved emulation speed which should make most
  everything playable even on the older DS-Lite/Phat.</li>

  <li>Adam supports the 32K expanded ROM and running carts under Adam emulation -
  name your ROMs as .adm so it loads into the right place in memory.</li>

  <li>Tatung Einstein now has two proper standard 200K disk drives.</li>

  <li>Tatung Einstein full keyboard now uses LED indicators under the SHIFT/CTRL/GRAPH
  and ALPHA LOCK keys for a visual improvement.</li>

  <li>Tatung Einstein properly handles the backspace key when using the Alpha-Numeric
  keyboard overlay.</li>

  <li>2000 individual game configurations are supported - save/load states optimized
  and numerous tweaks under the hood.</li>

  </ul>

  <p dir="auto">V9.4: 16-Mar-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Tatung Einstein improvements - more games run more correctly.</li>

  <li>Other minor tweaks and cleanup as time permitted.</li>

  <li>Einstein RAMDISK now unified in /data/ directory (rather than have one for each
  directory of .dsk files)</li>

  <li>Tweaks to the CTC timer engine for Einstein JSW2</li>

  <li>Fixed TMS9918 VDP 5th Sprite Flag handling and slight optimization to the VDP
  driver.</li>

  <li>Updated to latest SN76496 sound driver from FluBBa.</li>

  <li>Other minor tweaks and cleanup as time permitted.</li>

  <li>Version 9.3a with hotfix for SVI game loading fixed.</li>

  </ul>'
updated: '2025-08-31T11:02:09Z'
version: '10.7'
version_title: Version 10.7
---
