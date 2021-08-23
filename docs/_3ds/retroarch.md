---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.8/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: 72520151
    size_str: 69 MiB
    url: https://buildbot.libretro.com/stable/1.9.8/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: 73190431
    size_str: 69 MiB
    url: https://buildbot.libretro.com/stable/1.9.8/nintendo/3ds/RetroArch_cia.7z
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
update_notes: '<ul>

  <li>AUDIO/WINDOWS/WASAPI: Stop deactivating audio on fast forward</li>

  <li>CHEEVOS: Hide challenge indicators when resetting</li>

  <li>CHEEVOS: Support for more than 64 memory regions</li>

  <li>CHEEVOS: Automatically retry ''http error code -1''</li>

  <li>CONTENT INFORMATION: Show content info label+path rows always</li>

  <li>CORE OPTIONS: Core option categories implemented</li>

  <li>CORE OPTIONS: Add option to disable core option categories</li>

  <li>D3D10/11/12: Fix gfx_display_draw_texture - fixes OSK (On-Screen Keyboard) issues</li>

  <li>DATABASE: Fix heap-buffer-overflow when fetching CRC values</li>

  <li>DATABASE/EXPLORE: Fix CRC32 reading in explore menu</li>

  <li>DATABASE/LIBRETRODB: Fix writing of numerical values</li>

  <li>DATABASE/LIBRETRODB: Fix libretro-db loading on big endian platforms</li>

  <li>DUMMY CORE: Skip state_manager_event_{deinit/init} when core type is dummy,
  should skip warning spam ''Implementation uses threaded audio. Cannot use rewind..''
  when using rewind</li>

  <li>INPUT/UDEV: Limit udev device scan to subsystem ''input''</li>

  <li>INPUT/SDL2/WINDOWS: Fix keyboard event keycodes</li>

  <li>INPUT/WAYLAND: Fixes a bug where the first player''s mouse, pointer, and lightgun
  are echoed to the other ports. Now, those other ports correctly report zero. In
  the future support for multiple mouselike devices will need to be added, which is
  a bigger project</li>

  <li>INPUT/WAYLAND: The driver now respects keyboard_mapping_blocked</li>

  <li>INPUT/WAYLAND: When possible, deprecated lightgun defines are replaced with
  the new ones. The coordinates are still using the old relative callbacks</li>

  <li>INPUT/WINRAW: Trigger joypad driver reinit on DEVICECHANGE - avoids fullscreen
  toggle</li>

  <li>INPUT/WINRAW: Alt sticky fix</li>

  <li>INPUT/WINRAW: Prevent Alt getting stuck when Alt-Tabbing</li>

  <li>INPUT/WINRAW: Add pointer status</li>

  <li>INPUT/WINRAW: Add missing analog keybinds</li>

  <li>LIBNX/SWITCH: Fix poll missing for controller 2-8</li>

  <li>LIBNX/SWITCH: Fix layout not applied correctly and hangs when splitting joycons</li>

  <li>LIBRETRO: Core options category API implemented</li>

  <li>LIBRETRO: Fix RETRO_ENVIRONMENT_SET_FASTFORWARDING_OVERRIDE callback when runahead
  is enabled</li>

  <li>LIBRETRO: Add environment callback for enabling core option menu visibility
  updates without toggling Quick Menu</li>

  <li>LOGGING: Starting logging and verbose mode before first config load</li>

  <li>LINUX: In some Linux Desktop Environments, like Budgie, task bar feature is
  unable to pin applications. With StartupWMClass= present in .desktop file, it is
  possible to pin the application</li>

  <li>LOCALIZATION: Fetch translations from Crowdin</li>

  <li>MENU: Relocate ''Manage Playlists'' to top</li>

  <li>MENU: Fullscreen resolution width/height settings no longer require ''advanced
  settings''</li>

  <li>MENU/REFRESH RATE: Fix double notifications with refresh rate settings</li>

  <li>MENU/OZONE: Ensure the existence of values used in selection calculation</li>

  <li>MENU/OZONE/VULKAN: Casting to unsigned caused an integer overflow and after
  float promotion would lead to ''x'' being a garbage value, leading to problems when
  this value was passed to vkCmdSetViewport. This stops Vulkan validation layers from
  complaining about it</li>

  <li>METAL: Fixed font driver memory leaks</li>

  <li>MOUSE: Change default mouse index to port index</li>

  <li>MOUSE: Friendly names for mice where available</li>

  <li>OSX: Fix some memory leaks</li>

  <li>OSX: Fix controller duplication bug</li>

  <li>PS2: Implement alpha for the video driver</li>

  <li>PS2: Aspect ratio handling</li>

  <li>RETROFW: Initial port</li>

  <li>UWP/XBOX: Enable Explore tab by default - seems to work fine</li>

  <li>UWP/XBOX: Fix startup issues with latest Xbox Dashboard updates - ANGLE cores
  still show up wrong</li>

  <li>UWP/XBOX: fix issue where files where opened as OPENALWAYS instead of OPENEXISTING
  this fixes beetle cores</li>

  <li>UWP/XBOX: fix issue where filesizes where not returned properly, this fixes
  loading arcade dat files</li>

  <li>UWP/TRANSLATION: Enabled translation services for both UWP MSVC2017 and 2019.
  No TTS speech yet.</li>

  <li>VIDEO: Fix refresh rate 59Hz rounding</li>

  <li>WINDOWS: Remember original refresh rate</li>

  <li>WINDOWS/VULKAN: Refresh rate fixes + cleanups</li>

  <li>WIIU: Fix L3/R3 buttons</li>

  <li>WIIU: Compress RPX libretro cores</li>

  <li>WIIU: Add ICInvalidateRange (necessary for JITs)</li>

  <li>WIIU: Slight filesystem optimisation</li>

  <li>WIIU: Add option for running without core info (emscripten-style)</li>

  </ul>'
updated: '2021-08-22T19:01:25Z'
version: v1.9.8
version_title: v1.9.8
website: http://www.libretro.com
---
