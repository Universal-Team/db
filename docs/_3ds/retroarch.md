---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.7/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    url: https://buildbot.libretro.com/stable/1.9.7/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    url: https://buildbot.libretro.com/stable/1.9.7/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
image: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/libretro_banner.png
image_length: 3154
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/libretro/RetroArch
systems:
- 3DS
title: RetroArch
update_notes: '<ul>

  <li>3DS: Add unique ID''s</li>

  <li>CRT/SWITCHRES: Fixed some Monitor index bugs ad updated to the latest SR2</li>

  <li>CRT/SWITCHRES: Fixed monitor index corruption on Windows and added correct fractal
  scaling. Only used when required</li>

  <li>CRT/SWITCHRES: Updated log defines to match SR upstream.</li>

  <li>CRT/SWITCHRES: Added new SR_CONFIG_PATHS for non Windows and Linux systems.<br>

  Not that SR works on them but to fix RA compile issues</li>

  <li>CRT/SWITCHRES: Updated SR2 code base to latest. Added supprt for windows monitor
  indexing. Fixed monitor index bug where index 1 was not being used correctly and
  "auto" was not being sent.</li>

  <li>CRT/SWITCHRES: Updated swithres for x86 windows fix</li>

  <li>CRT/SWITCHRES: fixed SR2 auto issue</li>

  <li>CRT/SWITCHRES: Fixed auto monitor bug</li>

  <li>CRT/SWITCHRES: Fixed monitor index corruption on Windows</li>

  <li>CRT/SWITCHRES: Fixed buffer size bug</li>

  <li>CRT/SWITCHRES: Added correct fractal scalling. only used when required.</li>

  <li>CORE INFO: Automatically disable core info cache when core info directory is
  read-only</li>

  <li>EMSCRIPTEN: add MAME2003 / MAME2003-plus to web.libretro</li>

  <li>INPUT/UDEV: udev fixes add pointer pressed to pointer device to allow udev users
  to access this device</li>

  <li>LIBNX/SWITCH: Enable 7zip support</li>

  <li>LINUX/XDG: Prevent xdg-screensaver''s "Protocol error" messages</li>

  <li>LOCALIZATION: Fetch translations from Crowdin</li>

  <li>LOCALIZATION: Add missing languages for the first startup</li>

  <li>MENU/XMB/WIDGETS: Add workaround for FPU bug that breaks scale factor comparisons
  on certain platforms (fixes XMB thumbnails on 32bit Linux/Windows)</li>

  <li>MENU/RGUI: Enable fullscreen thumbnail toggle using RetroPad ''start'' button</li>

  <li>MENU/RGUI: Fix sublabel length when menu clock is disabled</li>

  <li>NETWORK/HTTP: Fix HTTP progress indication for large files on 32-bit systems</li>

  <li>NETWORK/NATT: implement natt fix from void()</li>

  <li>OPENDINGUX: Fix display when cores ''drop'' frames</li>

  <li>OPENDINGUX BETA: Use ALSA audio driver by default</li>

  <li>OPENDINGUX BETA: Fix IPU scaling when running 256x224 (SNES/Genesis) content</li>

  <li>PATHS: Fix garbled path string</li>

  <li>PS2: Implement proper ps2_font driver instead of using the font driver from
  gskit</li>

  <li>PS2: Use BDM for increasing up USB stability</li>

  <li>PS3: First basic RSX driver for PSL1GHT</li>

  <li>RS90: Initial port</li>

  <li>RS90: Fix offset of OSD text</li>

  <li>RS90: Disable menu clock by default</li>

  <li>RS90: Hide ''Bilinear Filtering'' video option</li>

  <li>RS90: Move appdata (retroarch) base directory to external microsd card</li>

  <li>RS90: Add optional approximate ''semi-linear'' scaling filter</li>

  <li>SHADERS: Max Shader Parameters increased to 1024</li>

  <li>VIDEO: Add ''Integer Scale Overlay'' - Force integer scaling to round up to
  the next larger integer instead of rounding down</li>

  <li>VIDEO: New ''Full'' aspect ratio added. This aspect ratio is useful when used
  with a shader which has a border in it. The aspect ratio is set to the full window
  area, so that the viewport spans the whole viewport. When using a border type shader
  like the Mega Bezel this allows the graphics to span the whole window regardless
  of the user''s monitor aspect ratio</li>

  <li>VITA: Wrong flags for not piglet version</li>

  <li>UNIX: Correct backlight max_brightness path</li>

  <li>UWP/XBOX: Default to Direct3D11 driver on UWP builds</li>

  <li>UWP/XBOX: Do not use windowed mode on UWP/Xbox by default, set default resolution
  to 1920x1080 by default. Should fix display issues with Dolphin/PCSX2 on Xbox</li>

  <li>WIIU: Fix inputs breaking when connecting/disconnecting remotes</li>

  <li>WIIU: Input - ignore some bogus KPAD results</li>

  <li>WIIU: Font rendering fixes - render font lines with correct spacing, and only
  sample alpha channel when rendering fonts</li>

  <li>WIIU/NETWORK: Network speed optimisations - WINSCALE, TCP sACK, large buffers</li>

  <li>WIIU/LIBFAT: Increase cache size on WiiU</li>

  <li>WIIU/FILE IO: Filesystem optimisations - add fast path for already aligned buffers</li>

  <li>WIIU/FILE IO: Use 128K vbufs for WiiU - we have loads of RAM and large vbufs
  are very beneficial</li>

  <li>WIIU/MENU/OZONE: Fix Ozone rendering error (scissor fix)</li>

  <li>WIIU/MENU/OZONE: Use Ozone icons instead of XMB Monochrome</li>

  </ul>'
updated: '2021-07-25T06:00:06Z'
version: v1.9.7
website: http://www.libretro.com
---
