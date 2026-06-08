---
author: cmdada
avatar: https://avatars.githubusercontent.com/u/79297197?v=4
categories:
- emulator
color: '#433943'
color_bg: '#433943'
created: '2026-05-10T04:52:37Z'
description: Nintendo 3DS homebrew application that embeds a full RISC-V emulator
  to boot a Linux environment inside the 3DS Horizon OS.
download_page: https://github.com/cmdada/3DS-CLI/releases
downloads:
  3ds_cli.zip:
    size: 1636732
    size_str: 1 MiB
    url: https://github.com/cmdada/3DS-CLI/releases/download/1.7/3ds_cli.zip
github: cmdada/3DS-CLI
icon: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image_length: 3509
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: undisclosed
source: https://github.com/cmdada/3DS-CLI
stars: 14
systems:
- 3DS
title: 3DS-CLI
update_notes: '<p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link"
  href="https://github.com/cmdada/3DS-CLI/compare/1.6...1.7"><tt>1.6...1.7</tt></a></p>'
updated: '2026-06-07T20:57:26Z'
version: '1.7'
version_title: V1.7
---

A Nintendo 3DS homebrew application that embeds a full RISC-V CPU emulator (`mini-rv32ima` by cnlohr) to boot a real Linux environment inside the 3DS Horizon OS.

Features a custom ANSI/xterm terminal emulator on the top screen with full 16/256/24-bit colour support, zoom, and viewport panning, plus a custom bottom-screen touch keyboard. Comes with a prebuilt image including BusyBox tools, a JavaScript runtime, and some other goodies.

## Controls
- **L / Y**: Zoom out
- **R / X**: Zoom in
- **ZL**: Toggle auto-follow cursor
- **ZR**: Toggle font (8x8 ↔ 5x7 compact)
- **Circle Pad**: Pan viewport
- **D-Pad**: Send arrow keys to Linux
- **START**: Quit and return to Homebrew Launcher

## Keyboard
- **SHF**: Shift (uppercase)
- **?#1 / #+=**: Symbol layers
- **ABC**: Return to alphabetic layer
- **CTL**: Ctrl modifier
- **TAB / ESC / ENT / DEL**: As labelled

## Credits
- Built using libctru and minirv32-ima