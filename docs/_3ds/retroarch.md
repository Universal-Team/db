---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.12/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: 72975143
    size_str: 69 MiB
    url: https://buildbot.libretro.com/stable/1.9.12/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: 73492340
    size_str: 70 MiB
    url: https://buildbot.libretro.com/stable/1.9.12/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
icon_index: 162
image: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/libretro_banner.png
image_length: 3154
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://buildbot.libretro.com/nightly/nintendo/3ds/
  downloads:
    RetroArch_3dsx.7z:
      url: https://buildbot.libretro.com/nightly/nintendo/3ds/RetroArch_3dsx.7z
    RetroArch_cia.7x:
      url: https://buildbot.libretro.com/nightly/nintendo/3ds/RetroArch_cia.7z
source: https://github.com/libretro/RetroArch
systems:
- 3DS
title: RetroArch
update_notes: '<ul>

  <li>3DS: Ensure parallax barrier is disabled when ''3DS Display Mode'' is ''2D''</li>

  <li>COMMAND: Command interface should work again</li>

  <li>INPUT/HID: Rewrote the HID deregistration algorithm; it should no longer cause
  issues when dealing with multiple pads of the same HID/VID combo</li>

  <li>INPUT/HID: Fix initialization bug that caused wiimotes to fail to register without
  an accessory attached</li>

  <li>INPUT/HID: Fix Wiimote regression</li>

  <li>INPUT/HID/MAC: Get Sony Sixaxis (DualShock 3) working on MacOS</li>

  <li>INPUT/UDEV: Add extra abs check for dolphinbar</li>

  <li>INPUT/UDEV: Add relative left mouse button when pointer device is not abs</li>

  <li>INPUT/WAYLAND: Fix keyboard input on Wayland - fixes ''Certain cores ignore
  user input''</li>

  <li>NETPLAY: Improvements from Cthulhu</li>

  <li>OPENDINGUX: Fix HAS_ANALOG/HAS_MENU_TOGGLE defines in sdl_dingux joypad driver</li>

  <li>LIBRETRO: Enable SRAM for contentless cores</li>

  <li>LIBRETRO: Add environment callback to get the rate retro_run is called - GET_THROTTLE_STATE
  and RETRO_THROTTLE_UNBLOCKED environment callback</li>

  <li>LINUX: Update metadata manifest</li>

  <li>MENU/OZONE: New themes - Solarized Light, Solarized Dark</li>

  <li>WINDOWS/WIN9X: Fix non-ASCII text display in window title</li>

  </ul>'
updated: '2021-10-24T01:57:44Z'
version: v1.9.12
version_title: v1.9.12
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
