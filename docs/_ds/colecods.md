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
    size: 1405440
    size_str: 1 MiB
    url: https://github.com/wavemotion-dave/ColecoDS/releases/download/9.7/ColecoDS.nds
  README.md:
    size: 51361
    size_str: 50 KiB
    url: https://github.com/wavemotion-dave/ColecoDS/releases/download/9.7/README.md
  cbios.txt:
    size: 2265
    size_str: 2 KiB
    url: https://github.com/wavemotion-dave/ColecoDS/releases/download/9.7/cbios.txt
github: wavemotion-dave/ColecoDS
icon: https://db.universal-team.net/assets/images/icons/colecods.png
image: https://raw.githubusercontent.com/wavemotion-dave/ColecoDS/main/arm9/gfx_data/pdev_tbg0.png
image_length: 15870
layout: app
qr:
  ColecoDS.nds: https://db.universal-team.net/assets/images/qr/colecods-nds.png
source: https://github.com/wavemotion-dave/ColecoDS
systems:
- DS
title: ColecoDS
update_notes: '<p dir="auto">V9.7: 16-Apr-2024 by wavemotion-dave</p>

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

  <li>Minor cleanup and optimizations to the Adam core.</li>

  </ul>'
updated: '2024-04-16T10:28:58Z'
version: '9.7'
version_title: Version 9.7
---
