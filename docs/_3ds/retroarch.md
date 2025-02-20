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
download_page: https://buildbot.libretro.com/stable/1.20.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.20.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.20.0/nintendo/3ds/RetroArch_cia.7z
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
stars: 10910
systems:
- 3DS
title: RetroArch
unique_ids:
- '0xBAC00'
update_notes: '<ul dir="auto">

  <li>AUDIO: Fix audio handling in case of RARCH_NETPLAY_CTL_USE_CORE_PACKET_INTERFACE</li>

  <li>AUDIO: Include missing audio filters on some platforms</li>

  <li>AUDIO/PIPEWIRE: Add PipeWire audio driver</li>

  <li>AUDIO/PIPEWIRE: Add PipeWire microphone driver</li>

  <li>APPLE: Hide threaded video setting</li>

  <li>APPLE: Use mfi joypad driver by default</li>

  <li>APPLE: Include holani, noods, mrboom, yabause, bsnes-jg core in App Store builds</li>

  <li>CHEEVOS: Add rarity and points to achievement unlock widget</li>

  <li>CHEEVOS: Add rank to leaderboard submission notification</li>

  <li>CHEEVOS: Update to rcheevos 11.5</li>

  <li>CHEEVOS: Update to rcheevos 11.6</li>

  <li>CHEEVOS: Show rcheevos game image in Discord rich presence</li>

  <li>CHEEVOS: Use translated strings for achievement messages</li>

  <li>CLOUDSYNC: Allow saves and configs to be synced optionally</li>

  <li>CLOUDSYNC: Add iCloud cloud sync driver</li>

  <li>CLOUDSYNC: Speed up by upload/download in parallel</li>

  <li>CLOUDSYNC: Allow thumbnails and system dir to be synced optionally</li>

  <li>CLOUDSYNC: Enable CloudSync on Android (non-SSL)</li>

  <li>CLOUDSYNC: Add more logs in failure situations</li>

  <li>CLOUDSYNC: Fixes for reauthentication and parallel sync</li>

  <li>CLOUDSYNC: Fixes for file resurrection</li>

  <li>CLOUDSYNC: Enable CloudSync on Windows</li>

  <li>CRT/SWITCHRES: Update switchres to 2.2.1</li>

  <li>GENERAL: Support for mbedtls v3</li>

  <li>GENERAL: Automatic Frame Delay refactor</li>

  <li>GENERAL: Remove Frame Rest, obsoleted by Frame Delay refactor</li>

  <li>GENERAL: Wrap around auto increment save state indexes when amount of states
  is limited</li>

  <li>GENERAL: Enable CHD hashing for Switch and DOS</li>

  <li>GENERAL: Enable auto save state when new content is loaded</li>

  <li>GENERAL: Improve Preemptive Frames when pointing device is used</li>

  <li>GENERAL: Fix building with menu disabled</li>

  <li>HAIKU: Restore Haiku build</li>

  <li>INPUT: Allow to select a preferred/reserved device for each player</li>

  <li>INPUT: Enable Caps, Num, Scroll Lock modifiers on multiple platforms</li>

  <li>INPUT: Autoconfig extension with alternative name/vid/pid</li>

  <li>INPUT: Fix autoconfig profile saving when device is not in the default port</li>

  <li>INPUT: Change classic turbo mode to work independently of which key was pressed
  first</li>

  <li>INPUT: Pointer and lightgun handling sanitization on Windows and Linux desktop
  platforms. These input drivers will now report edge and offscreen positions in a
  harmonized way, and will not return 0 instead.</li>

  <li>INPUT/DINPUT: Fix detection of quick shift key presses</li>

  <li>INPUT/HID: Fix crash on macOS when disconnecting the controller a second time</li>

  <li>INPUT/LINUX: Add illuminance sensor support to the linuxraw, sdl2, udev, and
  x11 input drivers</li>

  <li>INPUT/Remaps: Sort and apply remaps based on the specific connected controller</li>

  <li>INPUT/UDEV: Enable mouse buttons 4 and 5</li>

  <li>INPUT/WAYLAND: Enable horizontal scroll and mouse buttons 4 and 5</li>

  <li>INPUT/WAYLAND: Simulate lightgun input for cores</li>

  <li>INPUT/WAYLAND: Support for cursor-shape-v1 protocol</li>

  <li>INPUT/X11: Enable mouse buttons 4 and 5</li>

  <li>iOS: Enable vibration by default</li>

  <li>iOS: Better handling of physical mice/magic keyboard trackpad</li>

  <li>iOS: Mouse grab fixes</li>

  <li>iOS: Fix mouse cursor movement when button is held down</li>

  <li>iOS: Fix microphone support request and entitlement</li>

  <li>iOS: Enable compilation back to iOS 12</li>

  <li>iOS: Fix OpenGL ES context usage on iOS 9</li>

  <li>iOS/TVOS: Add Opera to App Store build</li>

  <li>iOS/TVOS: Bring NEON defines in line with ARM64</li>

  <li>iOS/TVOS: Flush save files on backgrounding</li>

  <li>LIBRETRO: Support RETRO_ENVIRONMENT_GET_FILE_BROWSER_START_DIRECTORY</li>

  <li>LIBRETRO: Support "/" as a file extension for loading a directory as content</li>

  <li>FFMPEG: Fix crash when playing back a file with 96 kHz audio</li>

  <li>MACOS: New display server, including support for ProMotion 120Hz V-Sync</li>

  <li>MACOS: Create App Store build</li>

  <li>MACOS: Generate key up events for command keys</li>

  <li>MIDI: Fix long messages (SysEx) in WinMM driver</li>

  <li>MIDI: Fix lingering notes on close in Alsa driver</li>

  <li>MENU: Support local thumbnails in other image formats than png (jpg/jpeg, bmp,
  tga)</li>

  <li>MENU: Delete also savestate thumbnails when savestates are garbage collected</li>

  <li>MENU: Option to disable analog stick menu navigation</li>

  <li>MENU: Fix pause toggle to not clear fast forward state</li>

  <li>MENU: Fix search playlist index in XMB/Ozone</li>

  <li>MENU: Fix renamed entry display</li>

  <li>MENU: Filter unknown extensions also inside zip files</li>

  <li>MENU: Add icons for present / missing firmware on core info page</li>

  <li>MENU: Ignore other hotkeys when menu toggle is pressed</li>

  <li>MENU: Fix menu jumping when using L3+R3 combo</li>

  <li>MENU: System Information now only shows features relevant for the platform</li>

  <li>MENU/GLUI: Make Show Sublabels options effective</li>

  <li>MENU/GLUI: Icon fixes</li>

  <li>MENU/XMB: Allow playlist icons to be individually customized, by looking for
  images in Named_Logos</li>

  <li>MENU/OZONE: Add Selenium theme for Ozone</li>

  <li>MENU/OZONE: Touchscreen improvements</li>

  <li>MENU/OZONE: Add a touch-sensitive Resume button in the lower right corner</li>

  <li>NETPLAY: Add East Asian relay server</li>

  <li>OVERLAY: Add option to load overlay based on system name</li>

  <li>PS2: Fix several broken cores depending on pthread</li>

  <li>QT: Enable building with Qt6</li>

  <li>QT: Fix input panel</li>

  <li>RECORDING: New WAV recording driver (audio only)</li>

  <li>REMOTE RETROPAD: Add gyro/acceleration/light sensor test screen</li>

  <li>REMOTE RETROPAD: Add pointer test screen</li>

  <li>REPLAY: Replay format extended to support external tools</li>

  <li>TVOS: Support bluetooth keyboards on tvOS</li>

  <li>TVOS: Fixes to run correctly on TVOS13</li>

  <li>TVOS: Better handling of Siri remote</li>

  <li>TVOS: WebDAV server for adding files more easily</li>

  <li>TVOS: Add Settings.app option to reset retroarch.cfg</li>

  <li>TVOS: Bring minimum tvos version down to 13.0</li>

  <li>VIDEO: Show and use exact refresh rate (3 decimals) and interlace/doublestrike
  where available</li>

  <li>VIDEO: Allow setting viewport bias to offset viewport horizontally/vertically</li>

  <li>VIDEO: Support viewport bias also with integer overscale and custom aspect ratios</li>

  <li>VIDEO: Use shader path from CLI for shader cycling</li>

  <li>VIDEO: Pixel perfect integer scaling improvements: axis options, smart mode</li>

  <li>VIDEO: Add upscale 1.66x filter</li>

  <li>VIDEO/D3D: Fix GPU screenshots</li>

  <li>VIDEO/KMS: Force fullscreen when KMS is used</li>

  <li>VIDEO/OpenGLES: Improve version directive granularity</li>

  <li>VIDEO/SHADERS: Fix memory leak when shader parameter step is 0.0</li>

  <li>VIDEO/SHADERS: Add 2 uniforms, OriginalAspect and OriginalAspectRot.</li>

  <li>VIDEO/SHADERS: Add CoreFPS and FrameTimeDelta uniforms.</li>

  <li>VIDEO/SLANG: Support optional includes</li>

  <li>VIDEO/VULKAN: Fix Vulkan window freezes when swapchain becomes suboptimal</li>

  <li>VIDEO/VULKAN: Prefer IMMEDIATE mode without vsync</li>

  <li>VIDEO/X11: Support inhibit of Xss screensaver</li>

  <li>VIDEO/WAYLAND: Support for content-type-v1 protocol</li>

  <li>VITA: Enable analog L2/R2 triggers when a DS3 controller is used with PS Vita</li>

  <li>WAYLAND: Fix segfault when relative pointer is not supported</li>

  <li>WAYLAND: Use reverse DNS name for desktop file and icon</li>

  <li>WAYLAND: Commit viewport resizes for more responsive display when resizing window</li>

  <li>WINDOWS: Fix restart if path to executable contains non-ASCII symbols</li>

  <li>WINDOWS: Hide directories starting with $ from file browser</li>

  </ul>'
updated: '2025-01-05T06:59:52Z'
version: v1.20.0
version_title: v1.20.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
