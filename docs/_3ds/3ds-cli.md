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
    size: 1631432
    size_str: 1 MiB
    url: https://github.com/cmdada/3DS-CLI/releases/download/1.3/3ds_cli.zip
github: cmdada/3DS-CLI
icon: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image_length: 2587
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/cmdada/3DS-CLI
stars: 5
systems:
- 3DS
title: 3DS-CLI
update_notes: <p dir="auto">Better keyboard feedback and Universal-DB install package.</p>
updated: '2026-05-28T21:03:45Z'
version: '1.3'
version_title: V1.3
---

A Nintendo 3DS homebrew application that embeds a full RISC-V CPU emulator (`mini-rv32ima` by cnlohr) to boot a real Linux environment inside the 3DS Horizon OS.

Features a custom bottom-screen touch keyboard and standard VT100 console output on the top screen.
Usage
- Bottom Screen: Custom touch keyboard, you can probably tell I'm not UX :3
- START Button: Hard exit the emulator and return to the Homebrew Launcher.

Credits
- Built using [devkitARM / libctru](https://github.com/devkitPro/libctru).
- Powered by the incredible [mini-rv32ima](https://github.com/cnlohr/mini-rv32ima) RISC-V emulator by cnlohr.
