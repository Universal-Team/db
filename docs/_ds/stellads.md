---
author: AlekMaul / wavemotion-dave
avatar: https://avatars.githubusercontent.com/u/75039837?v=4
categories:
- emulator
color: '#969188'
created: '2020-11-25T18:16:27Z'
description: Atari 2600 emulator for DS (original code by AlekMaul)
download_page: https://github.com/wavemotion-dave/StellaDS/releases
downloads:
  StellaDS.nds:
    size: 1077248
    size_str: 1 MiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/2.4/StellaDS.nds
  compatibility.txt:
    size: 25466
    size_str: 24 KiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/2.4/compatibility.txt
  readme.txt:
    size: 11824
    size_str: 11 KiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/2.4/readme.txt
github: wavemotion-dave/StellaDS
icon: https://raw.githubusercontent.com/wavemotion-dave/StellaDS/master/logo.bmp
image: https://raw.githubusercontent.com/wavemotion-dave/StellaDS/master/arm9/gfx/bgTop.png
image_length: 10279
layout: app
license: mit
license_name: MIT License
source: https://github.com/wavemotion-dave/StellaDS
systems:
- DS
title: StellaDS
update_notes: '<p>V2.4 : 31-May-2021 by Dave Bernazzani (wavemotion)</p>

  <p>A bit more juice squeezed out of the TIA. Added cart-specific options<br>

  to bypass VerticalBlank zero (not all games need that memory cleared if<br>

  we are dealing with a static screen... and this buys us CPU cycles!) and,<br>

  somewhat more dangerously, HorizontalBlank clearing can be disabled for<br>

  more speed. Only a few of the more stubborn games utilize these!<br>

  Removed PAL/NTSC option... only NTSC is supported (all games were released<br>

  in NTSC except a dozen PAL exclusives which have long since been converted<br>

  to run on NTSC - Search Atariage).<br>

  General cleanup and minor memory/code optimizations to get the most out<br>

  of the emulator.<br>

  Added 2 more lines of resolution before the top of the screen and 5 more<br>

  below... this allows the games that utilize underscan and/or significant<br>

  overscan to show properly.</p>'
updated: '2021-05-31T23:21:06Z'
version: '2.4'
version_title: Version 2.4
---
