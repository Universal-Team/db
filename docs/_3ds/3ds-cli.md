---
author: cmdada
avatar: https://avatars.githubusercontent.com/u/79297197?v=4
categories:
- emulator
color: '#1c371b'
color_bg: '#1c371b'
created: '2026-05-10T04:52:37Z'
description: Nintendo 3DS homebrew application that embeds a full RISC-V emulator
  to boot a Linux environment inside the 3DS Horizon OS.
download_page: https://github.com/cmdada/3DS-CLI/releases
downloads:
  3ds_cli.zip:
    size: 1634405
    size_str: 1 MiB
    url: https://github.com/cmdada/3DS-CLI/releases/download/1.4/3ds_cli.zip
github: cmdada/3DS-CLI
icon: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image_length: 2587
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: undisclosed
source: https://github.com/cmdada/3DS-CLI
stars: 9
systems:
- 3DS
title: 3DS-CLI
update_notes: '<p dir="auto">MASSIVELY improved performance</p>

  <ul dir="auto">

  <li>source/main.c:276: added emulator tuning constants and a 2 KB UART output buffer.</li>

  <li>source/main.c:299: UART output now batches with fwrite instead of calling printf
  for every byte.</li>

  <li>source/main.c:473: emulator execution is now time-budgeted per frame. It no
  longer runs only 10000 instructions then waits for VBlank, which was the big bottleneck.</li>

  <li>Makefile:52: bumped C optimization from -O2 to -O3 and added -fomit-frame-pointer.</li>

  <li>running at higher speed!</li>

  </ul>'
updated: '2026-06-03T19:42:30Z'
version: '1.4'
version_title: V1.4
---

A Nintendo 3DS homebrew application that embeds a full RISC-V CPU emulator (`mini-rv32ima` by cnlohr) to boot a real Linux environment inside the 3DS Horizon OS.

Features a custom bottom-screen touch keyboard and standard VT100 console output on the top screen.
Usage
- Bottom Screen: Custom touch keyboard, you can probably tell I'm not UX :3
- START Button: Hard exit the emulator and return to the Homebrew Launcher.

Credits
- Built using [devkitARM / libctru](https://github.com/devkitPro/libctru).
- Powered by the incredible [mini-rv32ima](https://github.com/cnlohr/mini-rv32ima) RISC-V emulator by cnlohr.
