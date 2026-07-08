---
author: AlekMaul / wavemotion-dave
avatar: https://avatars.githubusercontent.com/u/75039837?v=4
categories:
- emulator
color: '#969188'
color_bg: '#807b74'
created: '2020-11-25T18:16:27Z'
description: Atari 2600 emulator for DS (original code by AlekMaul). This is the PHOENIX
  EDITION which brings greater speed, compatibility and accuracy to the emulation
  on the DSi. New features such as instruction manuals and high score support included!
download_page: https://github.com/wavemotion-dave/StellaDS/releases
downloads:
  Copyright.txt:
    size: 3708
    size_str: 3 KiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/8.4a/Copyright.txt
  LICENSE:
    size: 17997
    size_str: 17 KiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/8.4a/LICENSE
  README.md:
    size: 48883
    size_str: 47 KiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/8.4a/README.md
  StellaDS.nds:
    size: 1699328
    size_str: 1 MiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/8.4a/StellaDS.nds
github: wavemotion-dave/StellaDS
icon: https://db.universal-team.net/assets/images/icons/stellads.png
image: https://raw.githubusercontent.com/wavemotion-dave/StellaDS/master/arm9/gfx/bgTop.png
image_length: 10279
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
llm_generation: unknown
qr:
  StellaDS.nds: https://db.universal-team.net/assets/images/qr/stellads-nds.png
source: https://github.com/wavemotion-dave/StellaDS
stars: 52
systems:
- DS
title: StellaDS
update_notes: '<p dir="auto">8.4a : 28-June-2026 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Fix for cart detection so SB carts don''t detect as CDFJ. Fixes Rescue from
  Poseidon''s Gate.</li>

  </ul>

  <p dir="auto">8.4 : 27-June-2026 by wavemotion-dave</p>

  <ul dir="auto">

  <li>Fix for TIA rendering that fixes Aardvark and probably others.</li>

  <li>Fix for banking on Squish-Em-Deluxe (F8) so dummy read on RTI properly hits
  the hotspot.</li>

  <li>Hotfix for PAL rendering which was causing the LCD to misbehave. True-sync is
  NTSC only for now.</li>

  <li>Full cleanup of ARM Thumbulator. I''ve decided to peel back on some of the ''unsafe''
  code that I''ve been using to gain speed. In the end, the speed optimizations and
  the improved accuracy have balanced themselves out - so 8.4 is still a bit faster
  than 8.3 in terms of raw speed but has a improved ARM Thumb emulation for a nice
  gain of accuracy.</li>

  <li>Lots of cleanup and both ARM and 6502 optimizations as time permitted. Better
  accuracy and improved speed all-around.</li>

  </ul>'
updated: '2026-06-28T12:00:23Z'
version: 8.4a
version_title: Version 8.4a
---
