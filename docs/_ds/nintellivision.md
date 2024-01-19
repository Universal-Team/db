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
    size: 549376
    size_str: 536 KiB
    url: https://github.com/wavemotion-dave/NINTV-DS/releases/download/4.7/NINTV-DS.nds
  README.md:
    size: 20925
    size_str: 20 KiB
    url: https://github.com/wavemotion-dave/NINTV-DS/releases/download/4.7/README.md
github: wavemotion-dave/NINTV-DS
icon: https://db.universal-team.net/assets/images/icons/nintellivision.png
image: https://raw.githubusercontent.com/wavemotion-dave/NINTV-DS/main/arm9/gfx/bgTop.png
image_length: 35199
layout: app
qr:
  NINTV-DS.nds: https://db.universal-team.net/assets/images/qr/nintv-ds-nds.png
script_message: 'You need "grom.bin", "exec.bin",

  and optionally "ivoice.bin" in the folder with your ROM files.'
source: https://github.com/wavemotion-dave/NINTV-DS
systems:
- DS
title: Nintellivision
update_notes: '<p dir="auto">V4.7 : 19-Jan-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Major refactor of the audio processor for a big speedup in rendering especially
  with more than one audio processor (i.e. ECS or Intellivoice)</li>

  <li>Switched from individual pixel output to 16-bit (two pixel) output when dealing
  with scrolling games (big speedup for games like Tron Solar Sailor, Space Spartans,
  Sorrow, TNT Cowboy, etc).</li>

  <li>The DSi now defaults to NO frameskip on any game and the ''High'' (best) sound
  quality.</li>

  <li>Aggressive frameskip no longer an option - it''s not needed for any game even
  on the older DS hardware.</li>

  <li>The DS-Lite/Phat gets a 15% improvement in sound quality and many of the classic
  games now run without frameskip.</li>

  <li>Fix for B-17 Bomber so it doesn''t flash the screen when in Pilot/Gun view.</li>

  <li>With the many updates, the config format changed and will be wiped back to defaults
  - sorry!</li>

  </ul>'
updated: '2024-01-19T01:52:55Z'
version: '4.7'
version_title: Version 4.7
---
