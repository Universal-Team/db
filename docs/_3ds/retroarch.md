---
author: Libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
color_bg: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.13.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.13.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.13.0/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
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
unique_ids:
- '0xBAC00'
update_notes: '<ul dir="auto">

  <li>3DS: Remove debug button combo to shutdown RA</li>

  <li>3DS: Remove MaterialUI as per MrHuu recommendation</li>

  <li>ANDROID: Enable ''Vibrate On Key Press'' by default</li>

  <li>ANDROID: Turn ''Threaded Video'' off by default</li>

  <li>CHEEVOS: Upgrade to rcheevos 10.5</li>

  <li>COMPILATION: Fixed compiling with --disable-menu</li>

  <li>CONFIG: Don''t show override notification with appendconfig alone</li>

  <li>DATABASE/PLAYLISTS: Playlist + database changes - Cleanup ''entry_slot'', fallback
  label + logging</li>

  <li>FRONTEND: Fix default remaps folder for various cores: remap should …<br>

  …be nested in config folder</li>

  <li>HOTKEYS: Fix shader toggle and add hotkey + sublabel</li>

  <li>HOTKEYS: Cleanups and corrections - Keep hotkey pause and menu pause separate
  in order to not trigger unwanted pause when toggling menu regardless if menu will
  pause or not</li>

  <li>HOTKEYS: Cleanups and corrections - Allow unpausing with Start (makes resuming
  more convenient after controller disconnect if menu does not pause)</li>

  <li>IOS13+: Pointer movement accuracy. iPad Trackpad Pointer Movement Accuracy through
  absolute location (for iOS 13.4 and above)</li>

  <li>IOS13+: Adds iPad Trackpad Support to iOS13 Project (for iOS 13.4 and above)</li>

  <li>INPUT: Addition to analog stick menu navigation</li>

  <li>INPUT: Fixed the way devices were previously indexed. Input devices were only
  being indexed in order and would stop at the first time an input has no device connected
  to it. The problem is when a device gets disconnected, that input will have no devices
  connected to it, but the next input may still have a device connected. So, that
  makes changing the port of the currently connected devices impossible.</li>

  <li>INPUT/AUTOCONFIG: Add option for pause on controller disconnect</li>

  <li>INPUT/AUTOCONFIG: Driver independent disconnection notification. Should show
  disconnect notification now properly on Windows with XInput and/or DirectInput pads</li>

  <li>INPUT/HID: Added usb hid controllers for the famous ZeroDelay encoder and also
  for "Kade: Kick Ass Dynamic Encoder" to be able to use some custom arcade sticks.</li>

  <li>INPUT/OVERLAY: Add eightway area types. The playlist supports UTF8, but edit
  control replaces the extended character with #. The following code enables extended
  character input in Netplay Chatting, Search, and Rename titles.</li>

  <li>INPUT/OVERLAY: Fix overlay next_index for unnamed targets</li>

  <li>LOCALIZATION: Updates</li>

  <li>LOCALIZATION: Add Hungarian language option</li>

  <li>MENU: Thumbnail fullscreen toggle behavior correction</li>

  <li>MENU: Consistent left-right scrolling for Quick Menu items</li>

  <li>MENU: Remove useless sublabel from System Information</li>

  <li>MENU: Improve widget appearance with missing assets</li>

  <li>MENU/INPUT: Add option for swapping menu scrolling buttons</li>

  <li>MENU/QT/WIMP: Remove SSL/TLS check at startup</li>

  <li>MENU/OZONE: Show metadata helper in footer only with second thumbnail</li>

  <li>MENU/OZONE: Footer improvements - Add "Cycle thumbnails" helper when suitable</li>

  <li>MENU/OZONE: Footer improvements - Show "Search" helper only when search function
  is enabled</li>

  <li>MENU/OZONE: Footer improvements - Fix "Thumbnails available" helper for save
  states</li>

  <li>MENU/OZONE: Footer improvements - Tighten padding between icon and title, and
  widen between helpers</li>

  <li>MENU/OZONE: Remember selection per main tabs</li>

  <li>MENU/OZONE: Remove incomplete assets warning</li>

  <li>MENU/OZONE: Add option to adjust cursor memory when changing menu tabs</li>

  <li>MENU/OZONE: Further extend texture support for Core Option categories</li>

  <li>MENU/XMB: Remove incomplete assets warning</li>

  <li>MENU/XMB: Add truncate playlist name option</li>

  <li>MENU/XMB: Improve background image selector</li>

  <li>MENU/XMB: Add option to adjust cursor memory when changing menu tabs</li>

  <li>MENU/XMB: Further extend texture support for Core Option categories</li>

  <li>MENU/MATERIALUI: Remove incomplete assets warning</li>

  <li>OSX: Fixed Z/X keys not working on the macOS port</li>

  <li>OSX: Fixed RETROK_LMETA not working on macOS port. The RETROK_LMETA key was
  not defined in the rarch_key_map_apple_hid</li>

  <li>OSX: Fix broken fullscreen mode in macOS Ventura</li>

  <li>OVERLAYS: Ignore hitboxes with zero area. I.e. Set ''reach_x'' or ''reach_y''
  to zero to ensure no hitbox math is done. This simplifies designating animation-only
  descriptors (e.g. for eightway areas) or obsolete descriptors.</li>

  <li>OVERLAYS: Add ''reach'' and ''exclusive'' for hitboxes. Allows stretching hitboxes
  and handling their overlap.</li>

  <li>PS2: Fix Error saving remaps and runtime logs</li>

  <li>PS3: Fix Core Remap Overwrite Fail</li>

  <li>QB: Don''t fail if OSDependent/OGLCompiler libraries are not present</li>

  <li>SCANNER/PS1: Improved scanning of PS1 discs</li>

  <li>SCANNER/PS2: Added serial scanning of PS2 discs - should now scan DVDs and other
  discs which were previously missed</li>

  <li>THUMBNAIL: If you rename title, you cannot use the thumbnail image. because
  the thumbnail filename and the title must be the same.<br>

  If there is no thumbnail with title, find the thumbnail image with rom-name. This
  has nothing to do with IME.</li>

  <li>THREADED VIDEO/GLCORE: Fix regression ''Shader presets dont load, when video
  driver is set to glcore''</li>

  <li>VULKAN: Fix HDR inverse tonemapping</li>

  </ul>'
updated: '2022-11-19T02:11:12Z'
version: v1.13.0
version_title: v1.13.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
