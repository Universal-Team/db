---
author: Apache Thunder
avatar: https://avatars.githubusercontent.com/u/11767416?v=4
categories:
- utility
color: '#8b8d89'
color_bg: '#7e807c'
created: '2017-02-12T20:50:13Z'
description: 'NTR Launcher - Bring back classic DS boot animation + boot older flashcarts! '
download_page: https://github.com/ApacheThunder/NTR_Launcher/releases
downloads:
  NTR_Launcher.zip:
    size: 4441407
    size_str: 4 MiB
    url: https://github.com/ApacheThunder/NTR_Launcher/releases/download/3.1/NTR_Launcher.zip
github: ApacheThunder/NTR_Launcher
icon: https://db.universal-team.net/assets/images/icons/ntr-launcher.png
image: https://db.universal-team.net/assets/images/images/ntr-launcher.png
image_length: 314
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/ApacheThunder/NTR_Launcher
stars: 58
systems:
- DS
title: NTR Launcher
update_notes: '<ul dir="auto">

  <li>Original R4 rom now available in default pack of NDS files available to Stage2
  filebrowser.</li>

  <li>R4i SDHC varient''s bootloader rom now available to stage2 filebrowser.</li>

  <li>Order of header/chip ID commands changed in main read_card code to match order
  used in bootloader. Reads header before chip ID like bootloader does. This triggers
  some carts to use DS/DS Lite rom insteat of white listed spoof game instead. The
  main consequence is that this makes DSTwo a bit more functional. Cart loader now
  actually boots the DSTwo correctly provided you wait till NTR Launcher is booted
  before inserting it. (or eject/reinsert while in stage 2 menu).</li>

  </ul>'
updated: '2024-08-16T02:59:48Z'
version: '3.1'
version_title: 3.1 Release Build
---
A DS Slot-1 Launcher. Original code from NitroHax but with cheat engine/menu stripped out. Useful for launching older DS flashcarts.
Credits go to Chishm for NitroHax which this source is based from and WinterMute for dslink source/reset code.