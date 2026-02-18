---
author: wavemotion-dave
avatar: https://avatars.githubusercontent.com/u/75039837?v=4
categories:
- emulator
color: '#b4b4d3'
color_bg: '#6d6d80'
created: '2021-09-02T21:28:15Z'
description: Nintellivision - an Intellivision Emulator for the DS/DSi. High compatibility,
  custom overlay support, high score saving, tons of input mapping - all the quality
  of life improvements you need!
download_page: https://github.com/wavemotion-dave/NINTV-DS/releases
downloads:
  NINTV-DS.nds:
    size: 790016
    size_str: 771 KiB
    url: https://github.com/wavemotion-dave/NINTV-DS/releases/download/6.3/NINTV-DS.nds
  README.md:
    size: 36905
    size_str: 36 KiB
    url: https://github.com/wavemotion-dave/NINTV-DS/releases/download/6.3/README.md
github: wavemotion-dave/NINTV-DS
icon: https://db.universal-team.net/assets/images/icons/nintellivision.png
image: https://raw.githubusercontent.com/wavemotion-dave/NINTV-DS/main/arm9/gfx/bgTop.png
image_length: 40671
layout: app
qr:
  NINTV-DS.nds: https://db.universal-team.net/assets/images/qr/nintv-ds-nds.png
script_message: 'You need "grom.bin", "exec.bin",

  and optionally "ivoice.bin" in the folder with your ROM files.'
source: https://github.com/wavemotion-dave/NINTV-DS
stars: 51
systems:
- DS
title: Nintellivision
update_notes: '<p dir="auto">V6.3 : 01-Jan-2026 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Fix for horizontal scroll bug that caused a bit of blurring when moving left/right
  in some games. Fixes Ninja Odyssey health bar.</li>

  <li>Improved backtab latched handling - the DSi and above now utilizes backtab latching
  by default for improved emulation accuracy.</li>

  <li>Fixed mapping DS keys to DISC UP/DOWN such that you can move left/right and
  press the DS button to JUMP (previously it would ignore the left/right if you pressed
  a DS button that mapped to DISC UP/DOWN).</li>

  <li>Refactored memory to free up another 160K of memory for future use.</li>

  <li>Improved PSG handling to move the structs into ARM fast memory for a slight
  boost in performance.</li>

  <li>Lots of minor database cleanup under the hood so more games and homebrews work
  properly without additional configuration needed.</li>

  </ul>'
updated: '2026-01-01T12:21:57Z'
version: '6.3'
version_title: Version 6.3
---
