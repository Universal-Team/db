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
    size: 4556042
    size_str: 4 MiB
    url: https://github.com/ApacheThunder/NTR_Launcher/releases/download/3.2/NTR_Launcher.zip
github: ApacheThunder/NTR_Launcher
icon: https://db.universal-team.net/assets/images/icons/ntr-launcher.png
image: https://db.universal-team.net/assets/images/images/ntr-launcher.png
image_length: 314
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/ApacheThunder/NTR_Launcher
stars: 75
systems:
- DS
title: NTR Launcher
update_notes: '<ul dir="auto">

  <li>Added DSOnei kernel to included nds files for Stage2 menu.</li>

  <li>Added N-Card rom dump to included nds files for Stage2 menu.</li>

  <li>Added CycloDS, and DSTWo bootloader dumps to included nds files for Stage2 menu.</li>

  <li>DSTwo now boots correctly from cart launcher.</li>

  <li>R4 SDHC Gold and other similar DEMON time bomb DSTTi clones now boot correctly
  from cart launcher.</li>

  <li>Added back option for enabling/disabling TWL ram.</li>

  <li>Added fixes to allow DS only carts to run with TWL ram enabled.</li>

  <li>Initial modcrypt code added for TWL carts. Currently works in emulation however
  TWL carts will fail to boot on hardware (when twl mode, ram, etc is enabled).</li>

  <li>If TWL mode and ram is enabled, cart loader will now load the DSi extended binaries
  into ram. Currently however they will only boot in emulation. Have not resolved
  why it''s not working on hardware yet.</li>

  <li>Stage2 menu now allowed to load dsi extended binaries of SRLs if TWL mode and
  TWL ram is enabled. Booting rom dumps as a method of booting into TWL carts is confirmed
  working. At least for System Flaw it does. :D</li>

  <li>Despite the improvements Acekard 2i still appears to require using the stage2
  menu to boot into.</li>

  <li>Fixes that allowed Demon timebomb carts to boot from cart launcher/autoboot
  may allow other non working carts to work. Further testing needed.</li>

  </ul>'
updated: '2024-12-12T02:44:18Z'
version: '3.2'
version_title: 3.2 Release Build
---
A DS Slot-1 Launcher. Original code from NitroHax but with cheat engine/menu stripped out. Useful for launching older DS flashcarts.
Credits go to Chishm for NitroHax which this source is based from and WinterMute for dslink source/reset code.