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
download_page: https://buildbot.libretro.com/stable/1.10.2/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.10.2/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.10.2/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
icon_index: 161
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

  <li>3DS: Add a menu toggle for switching between old and new 3DS speeds, located
  in the ''Power Management'' menu. Enabled by default, hidden on old 3DS devices.</li>

  <li>CHEEVOS: Update to rcheevos 10.3.3</li>

  <li>CHEEVOS: Support for Arduboy</li>

  <li>CHEEVOS: Fix tab sequences in rich presence being turned into t character</li>

  <li>CHEEVOS: Fix overflow when parsing float value that has more than 9 digits after
  the decimal</li>

  <li>CHEEVOS: Fix memory mapping when disconnect mask breaks a region into multiple
  blocks</li>

  <li>CORES: Enable manual selection of which cores are displayed in the ''Standalone
  Cores'' menu</li>

  <li>DATABASE/EXPLORE: Added more categories to the Explore menu</li>

  <li>INPUT: Fix analog stick not working with ''Unified Menu Controls''</li>

  <li>INPUT/MAPPING: Add ''Manage Remap Files'' submenu + automatically save input
  remaps when closing content</li>

  <li>INPUT/MAPPING: Add ''Reset Input Mapping'' option to ''Manage Remap Files''
  menu</li>

  <li>INPUT/MAPPING: Fix keyboard device remap nulling</li>

  <li>IOS/IOS13+: Support a toolbar that allows toggling of onscreen keyboard and
  touch mouse</li>

  <li>LIBRETRO: RETRO_ENVIRONMENT_SHUTDOWN fix - ensure core is properly unloaded
  when RETRO_ENVIRONMENT_SHUTDOWN is called</li>

  <li>LIBRETRO: RETRO_ENVIRONMENT_SHUTDOWN fix - ensure menu stack is properly flushed
  when RETRO_ENVIRONMENT_SHUTDOWN is called</li>

  <li>LINUX/MALI FBDEV: Fix segfault switching video threaded from quickmenu</li>

  <li>LOCALIZATION: Add Czech language support</li>

  <li>MIYOO: Improve CPU architecture and model name identification for Miyoo</li>

  <li>MENU/SETTINGS: Remove ''Advanced Settings'' flag from ''Settings &gt; Core''
  menu</li>

  <li>MENU/MATERIALUI: Add ''Gray Dark + Light'' themes</li>

  <li>MENU/RGUI: Add 6x10 extended ASCII and Latin Extended A and B fonts.  These
  will enable most Latin alphabets to be displayed in RGUI.</li>

  <li>MENU/RGUI: Add ''Gray Dark + Light'' themes</li>

  <li>MENU/XMB: Add title margin adjustment</li>

  <li>MENU/XMB: Vertical fade corrections</li>

  <li>MENU/OZONE: The size of the thumbnail bar can now be changed though a new option
  (Settings-&gt;User interface-&gt;Appearance) up to double its normal size.</li>

  <li>MENU/OZONE: Add ''Gray Dark + Light'' themes</li>

  <li>MENU/OZONE: Add thumbnail scale option</li>

  <li>HOTKEYS: Added hotkey for toggling sync to exact content framerate</li>

  <li>HOTKEYS: Prevent log spam when using rewind hotkey with cores that don''t support
  rewind, if rewind functionality itself is disabled</li>

  <li>HOTKEYS: Add hotkey for toggling sync to exact content framerate</li>

  <li>STEAM: Use native OSK (Onscreen Keyboard) instead of built-in RetroArch version</li>

  <li>STEAM: New built-in core DLC downloader</li>

  <li>STEAM: Swap OK/Cancel buttons by default</li>

  <li>VIDEO/HDR: Removed redundant copy of buffer in HDR mode if the shader has already
  a HDR format i.e. R10G10B10A2 (updated Vulkan/D3D11/D3D12 drivers)</li>

  <li>VIDEO/HDR: Fixed crash when using stock shader and HDR and previous optimisation</li>

  <li>WAYLAND: Dynamically load libdecor at runtime</li>

  <li>WAYLAND: Fix splash screen when using xdg_toplevel</li>

  <li>WAYLAND: SHM anti-collision for the splash screen</li>

  <li>WAYLAND: Skip splash screen if window is not ready</li>

  <li>WII: Fix find_connection_entry(): needs unsigned int<br>

  Otherwise the USB gamepad cannot be found, if VID/PID has leading zero. This issue
  happened with Retrode gamepad adapter</li>

  <li>WII: Rework Retrode gamepad implementation to support multi_pad interface</li>

  <li>WII: Fix - Unplugging and re-plugging now works again</li>

  <li>WII: vWii- Only gamepad 1 is supported, because multi_pad is currently only
  relevant in the Wii U implementation</li>

  <li>WIIU: Implemented the multi_pad interface according to input/connect/connect_wiiugca.c</li>

  <li>WIIU: Add Optimize for Gamepad option</li>

  </ul>'
updated: '2022-03-23T05:53:24Z'
version: v1.10.2
version_title: v1.10.2
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
