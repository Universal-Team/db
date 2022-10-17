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
download_page: https://buildbot.libretro.com/stable/1.12.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.12.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.12.0/nintendo/3ds/RetroArch_cia.7z
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

  <li>CONFIG/CLI: Allow use of --appendconfig with override cfgs instead of getting
  ignored</li>

  <li>CONFIG/LOGGING: No more console startup logging if logging to file</li>

  <li>CONFIG: Saves config on exit only once instead of (worst case scenario) 3 times</li>

  <li>DATABASE/EXPLORE/VIEW: Add View feature - Add saving of a filter set in the
  Explore menu into a so called "View" file which then gets listed alongside playlists.
  This also adds the ability to filter a category by range in the Explore menu and
  not just filter on exact matches.</li>

  <li>FILEBROWSER: Fix regression - certain extensions keep disappearing</li>

  <li>IOS: New modern iOS version (targeting iOS 13 and up), leverages Swift</li>

  <li>IOS: Fixes to iOS toolbar</li>

  <li>IOS16: Add iOS 16 lock screen widget</li>

  <li>IOS13+: Added emulator keyboard</li>

  <li>IOS13+: Add JIT support for non-jailbroken devices</li>

  <li>IOS13+: Added support for touch mouse handler</li>

  <li>IOS13+: Changed click-and-drag behavior to double tap hold and drag</li>

  <li>INPUT/HAPTIC/OVERLAYS/ANDROID: Improve haptic feedback for input overlays</li>

  <li>LINUX/MALI FBDEV: Add conditional support for OpenGL ES 3.x</li>

  <li>LOCALIZATION: Updates</li>

  <li>LOCALIZATION/ENGLISH: Add British English language option</li>

  <li>LOGGING/QT: Increase log buffer to 2048 characters - Vulkan validation layer<br>

  messages output correctly now.</li>

  <li>MENU/XMB: Remember selection per main tabs. Addresses the following : collection
  playlists can contain hundreds or thousands of items. When scrolling through one,
  pressing left or right by accident can be common. This resets the playlist to the
  top</li>

  <li>MIST/STEAM/STEAMDECK: Don''t expose Black Frame Insertion (BFI) if we are running
  on a Steam Deck</li>

  <li>NETWORKING/WINDOWS: Disable poll support for MSVC 2010 and earlier. WSAPoll
  is not supported on Windows XP and earlier.</li>

  <li>NETWORKING/WIIU: Fix socket_connect_with_timeout for WIIU</li>

  <li>NETWORKING/WIIU: Fixes RetroAchievements login</li>

  <li>NETWORKING/WIIU: Fixes other online updater functionality</li>

  <li>SAVESTATES/NOTIFICATIONS: Add delay to savestate notifications, so that GPU
  savestate screenshots stay untouched</li>

  <li>SAVESTATES/SCREENSHOTS: Avoid ''video_gpu_screenshot'' with savestates. Allow
  GPU screenshots with savestates only when there is no other way of getting a screenshot.</li>

  <li>SCREENSHOTS/VULKAN: Unload screenshot widget texture early. Fixes Vulkan crash
  when closing content while a screenshot widget is still on-screen</li>

  <li>SCREENSHOTS/VULKAN: Fix screenshot widget crash when ticker animating</li>

  <li>WAYLAND: Set correct app ID</li>

  <li>WIIU: Add some missing default directories</li>

  <li>WIIU: Get mkdir working on WiiU (directory creation)</li>

  </ul>'
updated: '2022-10-16T16:17:09Z'
version: v1.12.0
version_title: v1.12.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
