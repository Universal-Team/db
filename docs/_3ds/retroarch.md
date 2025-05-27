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
download_page: https://buildbot.libretro.com/stable/1.21.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.21.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.21.0/nintendo/3ds/RetroArch_cia.7z
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
stars: 11390
systems:
- 3DS
title: RetroArch
unique_ids:
- '0xBAC00'
update_notes: '<ul dir="auto">

  <li>3DS: Fix unique IDs for newer cores</li>

  <li>3DS: Enable TLS (SSL)</li>

  <li>3DS: Fix UI freeze when threaded rendering is enabled</li>

  <li>3DS: Fix crash on load content</li>

  <li>3DS: Other minor fixes</li>

  <li>APPLE: Enable Vulkan emulated mailbox</li>

  <li>APPLE: Include b2 core in App Store builds</li>

  <li>APPLE: CoreMIDI driver for IOS/MacOS</li>

  <li>APPLE: CoreLocation driver for IOS/MacOS</li>

  <li>AUTOCONF: Enable alternative display name in autoconfig files</li>

  <li>AUTOCONF: Make autoconfig failure messages optional</li>

  <li>AUDIO: Option to mute on rewind</li>

  <li>AUDIO/PIPEWIRE: Fix app launch when pipewire service is stopped</li>

  <li>AUDIO/PIPEWIRE: Fix speedup with threaded video mode</li>

  <li>AUDIO/PIPEWIRE: Fix latency setting and microphone handling</li>

  <li>AUDIO/PIPEWIRE: Pass the new rate to the audio driver</li>

  <li>CAMERA: Add PipeWire camera driver</li>

  <li>CAMERA: Add ffmpeg camera driver</li>

  <li>CHEAT: Rewrite part of cheat_manager_load_cb_second_pass()</li>

  <li>CHEEVOS: Include achievement state in netplay states</li>

  <li>CHEEVOS: Fix crash when entering achievements in quick menu while client is
  not present</li>

  <li>CHEEVOS: Restore cheevos_badges_enable for HAVE_GFX_WIDGETS builds</li>

  <li>CLI: Allow --entryslot to fall back to normal states</li>

  <li>CLOUDSYNC: Fix Windows path issues</li>

  <li>CLOUDSYNC: Workaround for duplicated requests bug</li>

  <li>CLOUDSYNC: Workaround for 301 redirects</li>

  <li>CLOUDSYNC: Handle ignored directories properly</li>

  <li>EMSCRIPTEN: Added new AudioWorklet driver, a fast callback-based audio driver</li>

  <li>EMSCRIPTEN: Scale window to correct size</li>

  <li>EMSCRIPTEN: Additional platform functions</li>

  <li>EMSCRIPTEN: Add new default video context driver: emscriptenwebgl_ctx</li>

  <li>EMSCRIPTEN: Add new audio driver: AudioWorklet</li>

  <li>EMSCRIPTEN: Add new modernized web player which will eventually replace the
  existing one</li>

  <li>EMSCRIPTEN/RWEBINPUT: Add touch input support</li>

  <li>GAMECUBE: Fixes</li>

  <li>GENERAL: Fix save state auto increment</li>

  <li>GENERAL: Fix softpatching with periods/dots in the file name</li>

  <li>GENERAL: Fix compilation with --enable-videocore</li>

  <li>GENERAL: Allow asset directory redefinition and other directory overrides via
  environment variables</li>

  <li>GENERAL: Allow override of player 1/2 input with machine learning models (needs
  recompilation and external library)</li>

  <li>GENERAL: Fix performance counter option not remembered between sessions</li>

  <li>GENERAL: Create security statement</li>

  <li>GENERAL: Fix crash when core is not selected</li>

  <li>GENERAL: Use core fps instead of screen refresh for calculating dropped frames</li>

  <li>INPUT: Fix a crash when initializing illuminance sensor on Linux</li>

  <li>INPUT: Analog-to-digital refactor, fixing behavior when analogs are assigned
  to keys</li>

  <li>INPUT: Turbo fire overhaul. See <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2882712839" data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/17633"
  data-hovercard-type="pull_request" data-hovercard-url="/libretro/RetroArch/pull/17633/hovercard"
  href="https://github.com/libretro/RetroArch/pull/17633">#17633</a></li>

  <li>INPUT/ANDROID: Fix game focus and pause handling</li>

  <li>INPUT/COCOA: Include gravity in acceleration sensor values</li>

  <li>INPUT/COCOA: Fix relative mouse input</li>

  <li>INPUT/COCOA: Allow mouse input while mouse overlay is active</li>

  <li>INPUT/WINRAW: Invert mouse index order</li>

  <li>IOS: Ensure webserver notice can be dismissed</li>

  <li>IOS: Fix rescanning manual playlists after app update</li>

  <li>IOS: Fix clean playlist function</li>

  <li>IOS: Fix crash when scanning</li>

  <li>IOS: Fix jump back to selected item when closing content</li>

  <li>IOS: Fix shared GL context setup</li>

  <li>IOS: Update Launch Screen</li>

  <li>IOS: Screen orientation lock through display server</li>

  <li>IOS: Fix rescanning manual playlists after app update</li>

  <li>LAKKA: Remove bluetooth device after disconnection</li>

  <li>LINUX/X11: Extend X11 input driver with XInput2 extensions for multi-mouse</li>

  <li>MACOS: Fix some sandbox handling in App Store builds</li>

  <li>MACOS: Reset keyboard state when focus is lost</li>

  <li>MENU: Add SSL support to the information list</li>

  <li>MENU: Add warning to BFI and related menu items</li>

  <li>MENU: Fix latency statistics when using runahead</li>

  <li>MENU: Fix opening file inside archive with core selection</li>

  <li>MENU: Main menu unified between different menu drivers</li>

  <li>MENU: Visibility toggle for playlist tabs</li>

  <li>MENU: Color the notification icon by message category</li>

  <li>MENU: Gray Dark+Light theme adjustments</li>

  <li>MENU/GLUI: Menu back button switches tabs like in other menu drivers</li>

  <li>MENU/GLUI: Tab selection option is honored</li>

  <li>MENU/GLUI: Fix CD icon appearing when no icon is specified</li>

  <li>MENU/GLUI: Allow fullscreen thumbnail browsing</li>

  <li>MENU/GLUI: Save state thumbnails</li>

  <li>MENU/PLAYLISTS: Random selection/shuffle function</li>

  <li>MENU/QT: Fix desktop menu crash with Cheevos disabled</li>

  <li>MENU/RGUI: Cleanups of certain menu items</li>

  <li>MENU/RGUI: Thumbnail fixes</li>

  <li>MENU/OZONE: Fix messagebox background</li>

  <li>MENU/XMB: Fix Light theme, font shadow</li>

  <li>MENU/XMB: Appearance menu cleanup</li>

  <li>MENU/XMB: Icon thumbnail can be any of the existing types</li>

  <li>MISC: Guard nanosleep prototype behind _POSIX_TIMERS</li>

  <li>MISC: Use fabsf and intended threshold for refresh rate check</li>

  <li>MISC: Use platform-specific checks for invalid descriptors</li>

  <li>MIDI: Add dropdown items for midi device selection</li>

  <li>NETWORK: Refactor of net_http, improvements for task blocking and performance</li>

  <li>NETWORK: Follow http redirects in net_http</li>

  <li>NETWORK: Expire failed DNS lookups much faster</li>

  <li>NETWORK: Fix netplay when using netpacket interface with recent cheevos</li>

  <li>NETWORK/HTTP: Fix crash in net_http_resolve() in single-thread mode</li>

  <li>OVERLAY: Fix overlay lightgun, mouse &amp; pointer</li>

  <li>OVERLAY: Preferred overlay loading is now default only on mobile platforms</li>

  <li>OVERLAY: Improve analog recentering when touching the area just outside the
  recentering zone</li>

  <li>QT: Enable non-png thumbnails also for Qt interface</li>

  <li>REPLAY: Fix issue when replaying old format input recordings in newer RetroArch</li>

  <li>TTS: Fix initial text-to-speech on Windows</li>

  <li>TVOS: Fix 720p display</li>

  <li>TVOS: Fix refresh rate fetching on tvOS 13/14</li>

  <li>TVOS: Update Top Shelf art</li>

  <li>SAVESTATES: Reset state index when loading new content</li>

  <li>UWP: Fix slang shader compilation</li>

  <li>VIDEO: Enable BFI setting for mobile platforms (mind the warnings)</li>

  <li>VIDEO/OpenGLES: Fix FP/sRGB FBO support</li>

  <li>VIDEO/SHADERS: Allow exact refresh rate sync with shader subframes</li>

  <li>VIDEO/SHADERS: FIX shader wildcards</li>

  <li>VIDEO/VULKAN: Enable adaptive vsync</li>

  <li>VIDEO/V4L2: Added resolution picker/forcing.</li>

  <li>VIDEO/V4L2: Rewrote logic for finding ALSA audio devices in enumerate_audio_devices
  function</li>

  <li>VIDEO/V4L2: Added a skip for some of the interface queries that fail and aren''t
  required for magewell usb.</li>

  <li>VITA: Fixes</li>

  <li>WINDOWS: Win32 socket improvements</li>

  <li>WII: Fixes</li>

  <li>WIIU: Fixes</li>

  <li>WEBPLAYER: Update core list for 1.20.0</li>

  </ul>'
updated: '2025-05-01T13:25:07Z'
version: v1.21.0
version_title: v1.21.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
