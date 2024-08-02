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
    size: 3781831
    size_str: 3 MiB
    url: https://github.com/ApacheThunder/NTR_Launcher/releases/download/3.0/NTR_Launcher.zip
github: ApacheThunder/NTR_Launcher
icon: https://db.universal-team.net/assets/images/icons/ntr-launcher.png
image: https://db.universal-team.net/assets/images/images/ntr-launcher.png
image_length: 314
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/ApacheThunder/NTR_Launcher
stars: 59
systems:
- DS
title: NTR Launcher
update_notes: '<ul dir="auto">

  <li>Stage2 launcher UI added. This is a heavily modified HBMenu with ability to
  launch carts! This menu can be used to boot a bootloader NDS file for flascharts
  that the direct cart launcher fails to boot. Although you can use this menu to launch
  any NDS file you want. Just note NTR Launcher will boot the target NDS file in NTR
  mode!</li>

  <li>New audio files added for new menu.</li>

  <li>HBMenu UI loaded by default if booted with no cart inserted.</li>

  <li>INI file folder now located in NTR_Launcher folder instead. A default ini file
  from NitroFS (if mount of nitrofs succeeds) will be copied to SD if one is not present.
  A set of default stage2 launchers for common cards found to not work from the cart
  launcher also will be copied if not present on SD.</li>

  <li>Stage2 launchers are expected to be in NTR Launcher folder though you can navigate
  to any folder you want in the UI so stage2 launchers aren''t the only thing this
  can be used for. You can also use this as a means of booting homebrew off SD in
  NTR mode.</li>

  <li>New option added to INI file for autobooting to new cart menu for those who
  want it as default.</li>

  <li>Debug mode now moved to Left + Right shoulder button combo on boot instead of
  B button.</li>

  <li>B button used to toggle booting into new cart stage2 menu. If you have autoboot
  disabled in ini file holding B will make NTR Launcher auto boot the inserted cart.
  If it''s enabled it will skip auto boot and boot into stage2 menu.</li>

  </ul>

  <p dir="auto">EDIT: FIxed outdated build in titles folder in release ZIP.</p>'
updated: '2024-04-12T02:17:40Z'
version: '3.0'
version_title: 3.0 Release Build
---
A DS Slot-1 Launcher. Original code from NitroHax but with cheat engine/menu stripped out. Useful for launching older DS flashcarts.
Credits go to Chishm for NitroHax which this source is based from and WinterMute for dslink source/reset code.