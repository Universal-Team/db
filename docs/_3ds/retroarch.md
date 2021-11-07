---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.13/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    url: https://buildbot.libretro.com/stable/1.9.13/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    url: https://buildbot.libretro.com/stable/1.9.13/nintendo/3ds/RetroArch_cia.7z
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

  <li>CHEEVOS/MSVC2010: Add Cheevos support</li>

  <li>CRT/SWITCHRES: Fixes some issue where scaling is incorrect in some video modes
  for CRT output.</li>

  <li>FRAMEDELAY: Add ''Automatic Frame Delay'' option</li>

  <li>INPUT: Add ''All users control the menu'' setting - any gamepad can control
  the menu when this is enabled. Only limitation right now is that only player 1 can
  toggle the menu, but any set Menu Toggle Controller Combo will work fine for all
  users, so this should be acceptable for now</li>

  <li>INPUT/UDEV: Fix Dolphin bar and safeguard against not adding devices with no
  mouse or touch buttons detected</li>

  <li>NETPLAY/CLI: -C/--connect commandline fix</li>

  <li>NETPLAY: Other improvements</li>

  <li>NETPLAY: Remove forced disconnection on unknown netplay command -<br>

  will be backwards compatible with any version that removed this<br>

  disconnect. instead of disconnecting, we just read the data and<br>

  ignore, like most network implementations do</li>

  <li>TASKS/CHEEVOS: Replace coroutines with tasks/thread</li>

  <li>TASKS/DATABASE/EXPLORE: Initialise ''Explore'' menu on a background thread -
  no more stall when hovering over the Explore tab</li>

  </ul>'
updated: '2021-11-07T02:31:09Z'
version: v1.9.13
version_title: v1.9.13
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
