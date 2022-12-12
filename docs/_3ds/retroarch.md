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
download_page: https://buildbot.libretro.com/stable/1.14.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.14.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.14.0/nintendo/3ds/RetroArch_cia.7z
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

  <li>AUDIO/COREAUDIO/APPLE: Allow coreaudio3 driver to work with audio devices that
  have 2 or more output channels</li>

  <li>CHEEVOS: Fix construction of Cheevos badge path</li>

  <li>CLI: Fixed not getting any output when running --version or --features without
  --verbose</li>

  <li>CLI: Fixed crash when running empty - parameter (it proceeded to content loading)</li>

  <li>CLI: Reformatted --features to require less rows and to be more consistent</li>

  <li>CLI: Added -V shorthand for --version</li>

  <li>CLI: Tab removal + whitespace nits</li>

  <li>CONFIG/MIDI: Prevent MIDI startup error with old configurations</li>

  <li>D3D11: Fix when using shaders with TATE mode arcades etc</li>

  <li>D3D12: Fix when using shaders with TATE mode arcades etc</li>

  <li>D3D12: Added support for break on errors  (development aid - define DEVICE_DEBUG
  to use)</li>

  <li>D3D12: Added support for DRED (device remove extended data) (development aid
  - define DEVICE_DEBUG to use)</li>

  <li>D3D12: Made D3D12 viewport and scissors to behave more like Vulkan drivers (or
  be more correct)</li>

  <li>D3D12: Fixed validation error on start up due to buffers not being setup correctly
  for one frame</li>

  <li>DATABASE/EXPLORE/VIEW: Bugfix - RGUI did not clear thumbnail on non-playlist
  items such as Save and Delete<br>

  menu_explore_get_entry_playlist_index() returns -1 on invalid entries, but the variable
  where it was stored was unsigned</li>

  <li>DATABASE/EXPLORE/VIEW: Bugfix - XMB+Ozone cleared thumbnail in Quick Menu when
  navigating away from Run</li>

  <li>DRM/ODROID GO2: Implement get_video_size for DRM GL context driver</li>

  <li>FASTFORWARD: Restore framelimit on fastforward toggle. Fast-forward was broken
  after toggling vrr_runloop off, since it will force frame limit to 1.0 (even on
  every frame) and never restores it. So let''s make sure the wanted ratio is applied
  when toggling FF (Fastforward).</li>

  <li>FFMPEG CORE: Fix runtime error in FFmpeg core when build with FFmpeg n5.1.2
  and OpenGL ES</li>

  <li>GFX/VIDEO FILTERS: (picoscale_256x_320x240) Added snn function to upscale Fuse
  (ZX Spectrum) core borderless output to 320x240. ZX Spectrum resolution of 256x192
  was previously unsupported.</li>

  <li>HOTKEYS: Further reorder internal hotkey items for consistency and removed SEND_DEBUG_INFO,
  OVERLAY_NEXT and OSK from visible hotkey bind list. "Send Debug Info" stuff is removed
  as much as possible without breakage due to translation files.</li>

  <li>INPUT/AUTOCONFIG: Disable ''pause on controller disconnect'' by default - was
  enabled by default on 1.13.0</li>

  <li>INPUT/MENU: Device Index menu refactor</li>

  <li>INPUT/OVERLAY: Fix analog drift blocking touch input (could occur on overlay_next
  if physical inputs shown on overlay)</li>

  <li>INPUT/OVERLAY: Fix overlay_next buttons lighting up in unison</li>

  <li>INPUT/OVERLAY: Skip meta keys in input_overlay_add_inputs (not supported by
  input_state_internal)</li>

  <li>INPUT/WINDOWS/WINRAW: Fix mouse position when using input overlay with mouse
  cursor</li>

  <li>INPUT/WINDOWS/WINRAW: Fixed mouse position to use the same method required for
  menu items and pointer when simulating input overlays with mouse, since it won''t
  work with multi mouse method</li>

  <li>INPUT/WINDOWS/WINRAW: Fixed passing mouse position to core also when using aforementioned
  method</li>

  <li>LEAPFROG: Add Leapfrog (LFx000) Target</li>

  <li>LOCALIZATION: Updates</li>

  <li>LOCALIZATION/INPUT/IME/MENU/ONSCREEN KEYBOARD: Extended IME and Korean OSK</li>

  <li>MENU: Cleanup of help texts</li>

  <li>MENU: Allow toggling info off with the same button</li>

  <li>MENU: Allow menu wallpaper/background reset. Let''s also remove the current
  wallpaper from the screen when pressing Start.</li>

  <li>MENU: Null driver shows with different color (Added for all menus the ability
  to show "disabled" items with a muted color)</li>

  <li>MENU/DRIVERS: Menu driver first, Audio Resampler removed because it is enough
  to exist under audio settings</li>

  <li>MENU/INPUT: Moved "Confirm Quit" to Input menu</li>

  <li>MENU/INPUT/HOTKEYS: Input hotkey menu completely overhauled to keep related
  entries together, and also adjusted some labels and sublabels</li>

  <li>MENU/OVERLAY: Fix overlays behind menu without core running. "Show Overlay Behind
  Menu" is currently broken with Ozone and XMB (with any other color theme than Plain)
  when running without a core.</li>

  <li>MENU/MATERIALUI: Fix home screen on first startup - no more stray entries</li>

  <li>MENU/OZONE: Allowed drawing sidebar and thumbnail bar background color also
  when core is running</li>

  <li>MENU/OZONE: Stopped using different padding and position for savestate thumbnails
  vs imageviewer</li>

  <li>MENU/OZONE: Removed gradient background effect when core is running, because
  some themes already have gradient background, which creates ugly rough steps</li>

  <li>MENU/OZONE: Fixed "Gray Light" theme from using the same background as "Gray
  Dark", which makes selection cursor near impossible to see</li>

  <li>MENU/OZONE: Some whitespace corrections</li>

  <li>MENU/UX: Extend OFF menu value colors</li>

  <li>MENU/UX: Menu icon improvements - Menu Visibility icons (Quick Menu + Settings)</li>

  <li>MENU/UX: Menu icon improvements - Playlist Manager icons</li>

  <li>MENU/UX: Menu icon improvements - Explore icon as database icon</li>

  <li>MENU/UX: Menu icon improvements - View and filter icons as cursor icon (folder
  icon in GLUI)</li>

  <li>MENU/UX: Menu icon improvements - View save + delete icons</li>

  <li>MENU/UX: Menu icon improvements - Moved Explore + Views below Standalone Cores</li>

  <li>MENU/UX/OZONE: Removed icons from menus where others items don''t have icons,
  and added icons to menus where the rest have icons</li>

  <li>MENU/UX/OZONE: Changed the way "no icon" is handled from kludgy way of not drawing
  SUBSETTING icon</li>

  <li>MENU/UX/XMB: Changed playlist entry index positioning to bottom right when thumbnails
  are in vertical mode, because big lists will overlap with arrow and current "breadcrumb"
  icons when the position is next to current selection</li>

  <li>MENU/UX/XMB: Added a rather nasty hack to prevent showing wrong icons under
  Explore as "breadcrumb" icon</li>

  <li>MENU/UX/XMB: Optimized certain icon drawing loops (Main horizontal icons were
  looped even when not visible, and all previous "breadcrumb" icons were looped when
  only one certain was needed)</li>

  <li>MENU/UX/MATERIALUI: Fixed showing icons where there should not be any (Waitable
  Swapchains, Show Recording + Streaming)</li>

  <li>OSX/MACOS: Fixed Cocoa keyboard not allowing to map Analog stick</li>

  <li>PS2: Use the recently created ps2_drivers which makes easier the loading and
  init of all the drivers: Memory Card, USB, HDD, Audio, Controllers</li>

  <li>PS2: Adds exFat support for USB, and probably solves some unexpected issues
  when using an HDD driver for booting cores/games.</li>

  <li>SDL GFX: Fix no menu on start/blank screen issue.</li>

  <li>SRAM: Don''t init SRAM saving without content (gets rid of the redundant logging)</li>

  </ul>'
updated: '2022-12-12T22:25:22Z'
version: v1.14.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
