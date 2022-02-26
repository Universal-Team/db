---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
color_bg: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.10.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: 73976240
    size_str: 70 MiB
    url: https://buildbot.libretro.com/stable/1.10.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: 74965352
    size_str: 71 MiB
    url: https://buildbot.libretro.com/stable/1.10.0/nintendo/3ds/RetroArch_cia.7z
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
update_notes: '<ul dir="auto">

  <li>3DS: Add Jaxe, A5200 and WASM4 cores</li>

  <li>3DS: Fix rotation</li>

  <li>ARCHIVE: Allow loading files from archive subdirectory</li>

  <li>AUDIO: Remove frame limit from audio batch callback. Before, if a core used
  the audio batch callback, there would be a hidden cap of 1024 on the number of audio
  frames that could be sent. If a core exceeded this value, any excess samples were
  silently discarded. While this is sufficient for ''normal'' samplerates/framerates,
  it means that e.g. a core using the batch callback to send 44100 Hz audio at 30
  fps with would have entirely broken sound. This has been fixed by removing the audio
  batch frame limit.</li>

  <li>AUDIO/RESAMPLER/NEON: Implement sinc kaiser NEON function</li>

  <li>CHEEVOS: Reset hardcore default to enabled; show message when trying to load
  state in hardcore</li>

  <li>CHEEVOS: Fix memory map conversion</li>

  <li>CHEEVOS: Check netplay status when unlocking achievements</li>

  <li>CHEEVOS: Support for hashing buffered NDS ROMs</li>

  <li>CHEEVOS: Fix hung task whe badge doesn''t exist</li>

  <li>CLI: Load save states from command-line or playlist</li>

  <li>CORE INFO CACHE/SETTINGS: Restore missing ''Cache Core Info Files'' menu entry</li>

  <li>DATABASE: Serial scanning for Gamecube/MegaCD/SegaCD/Saturn/PSX/PSP/Dreamcast/Wii</li>

  <li>D3D10/D3D11: Add Vsync swap interval</li>

  <li>EMSCRIPTEN: Add Jaxe, WASM4 cores</li>

  <li>FILE IO: Fix incorrect file names for remap files when the content path doesn''t
  have a preceding slash</li>

  <li>INPUT/OVERLAY: Added support for showing the overlay behind the menu instead
  of in front. This is currently only supported on the GL, Vulkan, D3D 9/10/11/12
  and 3DS drivers.</li>

  <li>INPUT/UDEV: Convert abs mouse from screen to viewport coordinates; fix relative
  mouse coords</li>

  <li>INPUT/WAYLAND: Ignore mouse clicks on window decoration</li>

  <li>INPUT/WAYLAND: Add scroll wheel support</li>

  <li>LINUX: Added support for Linux GameMode (<a href="https://github.com/FeralInteractive/gamemode">https://github.com/FeralInteractive/gamemode</a>),
  which can be toggled on/off in the Power Management or Latency settings menus.</li>

  <li>LOCALIZATION: Fetch translations from Crowdin</li>

  <li>LOCALIZATION: Add Indonesian, Swedish and Ukrainian language options</li>

  <li>LOCALIZATION/MENU/RGUI: Enable Indonesian and Swedish localisations for RGUI</li>

  <li>LOGGING: Logging cleanups</li>

  <li>LOGGING: Stop logging FPS statistics twice on quit</li>

  <li>LOGGING: Log font rendering backend only once</li>

  <li>HOTKEYS: Added a hotkey toggle for the on-screen technical statistics.</li>

  <li>HOTKEYS: Add delay + acceleration to volume hotkeys</li>

  <li>MENU: Add option for showing notifications only in menu</li>

  <li>MENU/RGUI: Add Finnish to supported languages</li>

  <li>MENU/XMB: Optional vertical list item fade</li>

  <li>MENU/XMB/OZONE: Category + History/Favorites icons</li>

  <li>NETWORK: Fix dummy notification - no longer shows a netplay initialization failed
  notification when netplay is not enabled</li>

  <li>NETWORK: LAN addresses only for UPnP - Some router devices might accept non-LAN
  addresses without raising an error.</li>

  <li>NETWORK: Filter out non-connectable rooms. Add an option for filtering out non-connectable
  netplay rooms.</li>

  <li>NETWORK: Netplay spectator notification fix. Fix double notification when the
  host switches to spectator.</li>

  <li>NETWORK: Prevents long-term pausing from clients dishonoring allow pausing</li>

  <li>NETWORK/LOBBY: Lobby Viewer: Filter out rooms that are not running RetroArch</li>

  <li>NETWORK/LOBBY: Lobby Viewer: Display a non-connectable tag to non-connectable
  rooms</li>

  <li>NETWORK/LOBBY: Host: Display warning if we are announcing to the internet but
  our room isn''t connectable from there</li>

  <li>NETWORK/RELAY: Custom relay server support - Add support for custom user-ran
  relay servers</li>

  <li>NETWORK/RELAY: Replace Canadian relay server with Singapore relay server. Current
  relays: New York/USA, Madrid/Spain, Sao Paulo/Brazil, Singapore</li>

  <li>NETWORK/UPNP: Various refactors/improvements, no more dependent on miniupnpc</li>

  <li>NETWORK/UPNP: Various UPnP binding fixes for specific routers</li>

  <li>NETWORK/UPNP: Accept IGD v2 service types</li>

  <li>NETWORK/UPNP: Delay lobby server announcing - delay the announcing in order
  to give UPnP''s port forwarding more time. Fix the remaining truncation warnings.</li>

  <li>NETWORK/UPNP: Smart interface selection - Find the most suitable address for
  UPnP by scoring interfaces on how close their address is to the device''s address</li>

  <li>OPENGL1: Fix buffer overflow - RetroArch would sometimes crashes at startup
  when loading asset textures with GL1 driver</li>

  <li>PS3: PSL1GHT port added to Gitlab CI</li>

  <li>VULKAN: Double combined image sampler descriptor pool size - fix segfaults with
  AMD GPUs using RADV</li>

  <li>VULKAN: Emulate mailbox only with Vsync enabled - otherwise have it disabled
  - useful for VRR/G-Sync/FreeSync</li>

  <li>VULKAN/SWAPCHAIN: Vulkan max swapchain images option adjustments: removed value
  1, since it won''t be used - Video reinit on change, so that there is no need to
  restart or toggle fullscreen</li>

  <li>VULKAN/HDR: HDR support - tested on Windows</li>

  <li>WAYLAND: Add libdecor for client side decoration</li>

  <li>WAYLAND: Use any display for initial metrics</li>

  <li>WAYLAND: Fix the window closing, if RetroArch is build without libdecor</li>

  <li>WAYLAND: Use checked sizes in EGL resize</li>

  <li>WAYLAND: Fix window title update</li>

  <li>WEBOS: Fix webOS build and run</li>

  <li>WIIU: Fix rotation</li>

  <li>UWP/XBOX: Fix content over 4GB (approx) failing to load, improve/speed up copy/load
  times</li>

  <li>UWP/XBOX: Fix scanning for playlists</li>

  <li>UWP/XBOX: Move content copied to LocalState to a dedicated dir and clear on
  startup</li>

  <li>UWP/XBOX: Make content copy to a specific cache directory in the LocalState
  folder when it''s copied</li>

  <li>UWP/XBOX: Auto delete VFS cache dir on startup</li>

  <li>UWP/XBOX: Make resolution switching automatic and fix angle output issues</li>

  <li>UWP/XBOX: Force ANGLE to render at 1080p regardless of screensize as the output
  is 1080p regardless of screensize. This fixes an issue where at 4k any angle output
  would be zoomed into a corner.</li>

  <li>UWP/XBOX: Set resolution based on display resolution (auto 4k)</li>

  <li>UWP/XBOX: Set driver to D3D11 if booting with opengl</li>

  <li>UWP/XBOX: Reset width and height of output on boot to match display</li>

  <li>UWP/XBOX: Mitigate need for VFS cores on NTFS drives</li>

  <li>UWP/XBOX: Make check for standard I/O by access rather than the just assuming
  based on path string</li>

  <li>UWP/XBOX: Add code to auto permissions so files can be accessed by non VFS cores
  (no exFAT or FAT32 support yet)</li>

  </ul>'
updated: '2022-01-20T17:38:41Z'
version: v1.10.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
