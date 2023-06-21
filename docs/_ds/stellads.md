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
  README.md:
    size: 35303
    size_str: 34 KiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/6.6b/README.md
  StellaDS.nds:
    size: 1652736
    size_str: 1 MiB
    url: https://github.com/wavemotion-dave/StellaDS/releases/download/6.6b/StellaDS.nds
github: wavemotion-dave/StellaDS
icon: https://db.universal-team.net/assets/images/icons/stellads.png
image: https://raw.githubusercontent.com/wavemotion-dave/StellaDS/master/arm9/gfx/bgTop.png
image_length: 10279
layout: app
license: mit
license_name: MIT License
qr:
  StellaDS.nds: https://db.universal-team.net/assets/images/qr/stellads-nds.png
source: https://github.com/wavemotion-dave/StellaDS
systems:
- DS
title: StellaDS
update_notes: '<p dir="auto">V6.6b : 21-Jun-2023 by Dave Bernazzani (wavemotion)</p>

  <ul dir="auto">

  <li>DSi now defaults to the ''Accurate'' BUS MODE for maximum compatibility.</li>

  <li>Improved data bus handling for undriven pins in Tia::Peek() for improved compatibility.</li>

  <li>A few more tweaks to a few more games to make them as accurate as possible.</li>

  </ul>

  <p dir="auto">V6.6 : 20-Jun-2023 by Dave Bernazzani (wavemotion)</p>

  <ul dir="auto">

  <li>Fix for Meltdown prototype so it doesn''t crash.</li>

  <li>Fix for Pleiades to fix graphical glitches.</li>

  <li>Fix for Atom Smasher prototype so it doesn''t crash on start (wrong bank scheme
  detected).</li>

  <li>Fix for E7 banking so it handles 8K, 12K and 16K roms.</li>

  <li>Fix for Flash Gordon to eliminate graphical glitches.</li>

  <li>Fix for Elf Adventure prototype so it runs.</li>

  <li>Fix for Star Gunner so it doesn''t glitch.</li>

  <li>Fix for Warlords graphical glitches.</li>

  <li>Fix for Worm War I graphical glitches.</li>

  <li>Fix for A-Star not starting.</li>

  <li>Fix for Hugo Hunt graphical glitches.</li>

  <li>Improved random() generator for more robust RAM clear / handling on startup
  and added config to either randomize RAM or clear it at start.</li>

  <li>Added new option to use the ''Compatible'' BUS driver which will handles things
  like invalid reads and drives unused TIA bits (a few games rely on this - but it
  does slow down emulation slightly).</li>

  </ul>'
updated: '2023-06-21T10:44:07Z'
version: 6.6b
version_title: Version 6.6b
---
