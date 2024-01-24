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
    size: 547840
    size_str: 535 KiB
    url: https://github.com/wavemotion-dave/NINTV-DS/releases/download/4.8/NINTV-DS.nds
  README.md:
    size: 23150
    size_str: 22 KiB
    url: https://github.com/wavemotion-dave/NINTV-DS/releases/download/4.8/README.md
github: wavemotion-dave/NINTV-DS
icon: https://db.universal-team.net/assets/images/icons/nintellivision.png
image: https://raw.githubusercontent.com/wavemotion-dave/NINTV-DS/main/arm9/gfx/bgTop.png
image_length: 35437
layout: app
qr:
  NINTV-DS.nds: https://db.universal-team.net/assets/images/qr/nintv-ds-nds.png
script_message: 'You need "grom.bin", "exec.bin",

  and optionally "ivoice.bin" in the folder with your ROM files.'
source: https://github.com/wavemotion-dave/NINTV-DS
systems:
- DS
title: Nintellivision
update_notes: '<p dir="auto">V4.8 : 24-Jan-2024 by wavemotion-dave</p>

  <ul dir="auto">

  <li>.int files are now auto-detected as either .bin(+cfg) or .rom files. This allows
  you to rename .rom files or .bin files to .int and let Twilight Menu++ auto-launch
  Nintellivision.</li>

  <li>Slight improvement to the Intellivoice driver to give a minor boost in performance
  (mostly for DS-Lite/Phat).</li>

  <li>Added new keyclick enable option in Configuration (page 2) that produces the
  typical Intellivision keyclick when you press the 12-button keypad (on the DS lower
  screen).</li>

  <li>Added a new level of sound quality ''Ultimate''. The default for the DSi and
  above is still ''High'' as ''Ultimate'' consumes significant CPU time but you can
  enable it on a per-game basis for some of the more simple games (e.g. Astrosmash,
  Beauty and the Beast, AD&amp;D Tarmin, etc)</li>

  <li>DS-Lite now enables Intellivoice on World Series Major League Baseball - sound
  quality is a bit rough on the older handheld but very playalbe.</li>

  <li>Fixed save/restore state including when backtab latched is TRUE (Stampede, Masters
  of the Universe)</li>

  <li>Fix for intellivoice games so there are no more glitches on the updated version
  of Same Game and Robots.</li>

  <li>Fix for ecs games so they don''t inadvertantly write over the last graphics
  card in memory (causing minor graphics corruption on some games)</li>

  <li>Correction of one intellivoice coefficient value (thanks to documentation in
  JZINTV) so voice games sound their best.</li>

  <li>Other minor tweaks and cleanup as time permitted.</li>

  </ul>'
updated: '2024-01-24T13:17:11Z'
version: '4.8'
version_title: Version 4.8
---
