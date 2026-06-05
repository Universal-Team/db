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
    url: https://github.com/cmdada/3DS-CLI/releases/download/build-7c80c45a6fe28324d2949e2871ce3bf4bbe65e38/3ds_cli.zip
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
updated: '2026-06-05T00:06:11Z'
version: build-7c80c45a6fe28324d2949e2871ce3bf4bbe65e38
version_title: Build 7c80c45
---

A Nintendo 3DS homebrew application that embeds a full RISC-V CPU emulator (`mini-rv32ima` by cnlohr) to boot a real Linux environment inside the 3DS Horizon OS.

Features a custom bottom-screen touch keyboard and standard VT100 console output on the top screen.
Usage
- Bottom Screen: Custom touch keyboard, you can probably tell I'm not UX :3
- START Button: Hard exit the emulator and return to the Homebrew Launcher.

Credits
- Built using [devkitARM / libctru](https://github.com/devkitPro/libctru).
- Powered by the incredible [mini-rv32ima](https://github.com/cnlohr/mini-rv32ima) RISC-V emulator by cnlohr.
