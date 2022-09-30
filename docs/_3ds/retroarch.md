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
download_page: https://buildbot.libretro.com/stable/1.11.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.11.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.11.0/nintendo/3ds/RetroArch_cia.7z
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

  <li>3DS: Add unique ID''s</li>

  <li>3DS: Add bottom menu options</li>

  <li>3DS: Set bottom_asset directory default</li>

  <li>3DS: Only enable internal counter with CONSOLE_LOG defined</li>

  <li>3DS: Set default bottom font values</li>

  <li>3DS: Fix CIA installation issues</li>

  <li>3DS: Support latest libctru</li>

  <li>ANDROID: Add HAVE_ACCESSIBILITY</li>

  <li>ANDROID: Gingerbread support</li>

  <li>ANDROID: Touchpads support</li>

  <li>ANDROID: Builtin Xperia Play autoconfig profile</li>

  <li>ANDROID: Disable Feral GameMode for Android - only available on Linux</li>

  <li>ANDROID: Add a configurable workaround for Android reconnecting devices</li>

  <li>ANDROID/FDROID: Add F-Droid metadata to repo in Fastlane format</li>

  <li>AUDIO/AUDIO MIXER: Add missing locks for thread safety</li>

  <li>AUDIO/AUDIO MIXER: Fix audio mixer memory leak + remove redundant ''single threaded''
  rthreads implementation</li>

  <li>AUTOSAVE: Change/improve exit behavior of autosave thread - if condition variable
  is signaled, the loop is ran another last time so we can do a final check/save before
  stopping the thread.</li>

  <li>CDROM: Fix memory leak caught with asan - buf passed to filestream_read_file</li>

  <li>CORE INFO/NETPLAY: Ensure current core info is initialized at runloop_event_init_core
  when netplay is enabled</li>

  <li>CHEEVOS: Upgrade to rcheevos 10.4</li>

  <li>CHEEVOS: Allow creating auto savestate in hardcore</li>

  <li>CHEEVOS: prevent invalid memory reference if game has achievements but core
  doesn''t expose memory</li>

  <li>CHEEVOS: Release achievement badge textures when video driver is deinitialized</li>

  <li>CHEEVOS: Re-enforce hardcore limitations once achievements are loade</li>

  <li>CHEEVOS/MENU/MATERIALUI: Show achievement badge icons in MaterialUI driver</li>

  <li>D3D9: D3D9 has been split up into two drivers - D3D9 HLSL (max compatibility,
  no shader support yet) and D3D9 Cg (dependent on deprecated Nvidia Cg runtime library)</li>

  <li>D3D9/HLSL/XMB: XMB fix</li>

  <li>D3D9/CG: D3D9 Cg driver fixed</li>

  <li>D3D11: Fix overlay not showing up</li>

  <li>D3D11/12: Reduce lag with WaitForVBlank - this rather simple addition seems
  to make D3D11/12 very very close to Vulkan/GLCore regarding input lag.</li>

  <li>D3D11/12: Add waitable swapchains and max frame latency option</li>

  <li>D3D11/12: Make waitable swapchains optional</li>

  <li>DATABASE: Reformat ''rdb_entry_int'' - Nitpick adjustments for database entries:
  Capitalize "Release Date", and remove space before : from Release Date rows which
  use integer</li>

  <li>DATABASE/EXPLORE: Allow On-Demand Thumbnails in Explore menu</li>

  <li>DATABASE/EXPLORE/MENU/OZONE/XMB/RGUI: Explore menu thumbnails</li>

  <li>DISC CONTROL: Better Disc Control append focus</li>

  <li>DOS/DJGPP: Add a workaround for libc bug</li>

  <li>AUTOMATIC FRAME DELAY: Added slowmotion resiliency</li>

  <li>AUTOMATIC FRAME DELAY: Added string representation for seeing the current effective
  delay without opening statistics</li>

  <li>AUTOMATIC FRAME DELAY: Added "ms" to logging and "(ms)" to label just like in
  Audio Latency</li>

  <li>GENERAL: Don''t bake in OpenAL and libcaca by default unless explicitly enabled
  with configure switch.</li>

  <li>GENERAL: Reduce amount of strlen calls</li>

  <li>GENERAL: Reduce or simply sin/cosf calls</li>

  <li>GFX: Fix readability and precision issues in aspectratio_lut</li>

  <li>GFX: Add option to manually enable/disable automatic refresh rate switching</li>

  <li>GFX: Enable automatic configuration of ''VSync Swap Interval''</li>

  <li>GFX/FONT/FREETYPE: Use FT_New_Memory_Face - first read it from file to memory
  beforehand -<br>

  this solves an asset extraction issue when selecting ''Update Assets'' - apparently
  FT_New_Face keeps an open file handle to the font file which<br>

  prevents it from being overwritten/deleted while the program is still running.</li>

  <li>GFX/THUMBNAILS: Thumbnail aspect ratio fix</li>

  <li>GFX/THREADED VIDEO: Optimizations, fixes and cleanups</li>

  <li>GFX/VIDEO FILTERS: Add Upscale_240x160-320x240 video filter with ''mixed'' method</li>

  <li>GLSLANG: Fix compilation with ./configure --disable-builtinglslang - was missing
  linking against -lMachineIndependent and -lGenericCodeGen static libs</li>

  <li>INPUT: Fix off by one error for input_block_timeout setting. Also default to
  0 for this setting (pretty massive performance gain)</li>

  <li>INPUT: Analog button mapping fixes</li>

  <li>INPUT/HID/OSX: Fix DualShock3 support</li>

  <li>INPUT/HID/LINUX: (qb) Disable HAVE_HID by default for now for Linux as long
  as there are no working backends for both</li>

  <li>INPUT/HID/WINDOWS: (qb) Disable HAVE_HID by default for now for Windows as long
  as there are no working backends for both</li>

  <li>INPUT/HID/WIIU: Fix DualShock3 support</li>

  <li>INPUT/OVERLAY: Block pointer input when overlay is pressed</li>

  <li>INPUT/REMAPPING: input_remapping_save_file - existing remapping file was needlessly
  reloaded</li>

  <li>INPUT/REMAPPING: Add option to disable automatic saving of input remap files</li>

  <li>INPUT/LINUX/UDEV: Fix lightgun scaling on Y axis</li>

  <li>INPUT/LINUX/X11/LED: Add LED keyboard driver</li>

  <li>INPUT/WINDOWS/LED: LED keyboard driver cleanup</li>

  <li>INPUT/WINDOWS/WINRAW: Clear key states when unfocused</li>

  <li>INPUT/WINDOWS/WINRAW: Fix pointer device position</li>

  <li>IOS: iOS app icon fixes &amp; revisions</li>

  <li>LIBRETRO/SAVESTATES: Implement an api call for context awareness</li>

  <li>LOCALIZATION: Updates</li>

  <li>LOCALIZATION: Add Catalan language option</li>

  <li>LOCALIZATION: Fix some bad localization</li>

  <li>LINUX: Make memfd_create call more backwards compatible by calling it through
  syscall - on older systems, you''ll have to include linux/memfd.h for the MFD_ defines,
  and call memfd_create() via the the syscall(2) wrapper (and include unistd.h and
  sys/syscall.h for it work). We exclude linux/memfd.h header include because we already
  provide the MFD_ defines in case they are missing</li>

  <li>LINUX/MALI FBDEV: Fix assertion failed on video threaded switch</li>

  <li>MENU: Menu paging navigation adjustments</li>

  <li>MENU: New Menu Items for disabling Info &amp; Search buttons in the menu</li>

  <li>MENU: Allow the user to use volume up/down/mute hotkeys from within the menu</li>

  <li>MENU: Add missing sublabels for non-running Quick Menu</li>

  <li>MENU: Reorganize Quick Menu Information</li>

  <li>MENU: Savestate thumbnails - Savestate slot reset action</li>

  <li>MENU: Allow changing savestate slots with left/right on save/load</li>

  <li>MENU: Add ''Ago'' to playlist last played styles</li>

  <li>MENU: Add proper icons for shader items</li>

  <li>MENU/MATERIALUI: Add icon for ''Download Thumbnails''</li>

  <li>MENU/XMB: Add options for hiding header and horizontal title margin</li>

  <li>MENU/XMB: Dynamic wallpaper fixes</li>

  <li>MENU/XMB: Add Daite XMB Icon Theme</li>

  <li>MENU/XMB/OZONE: Savestate thumbnail aspect ratio</li>

  <li>MENU/XMB/OZONE: Core option category icon refinements</li>

  <li>MENU/XMB/OZONE: Fullscreen thumbnail browsing</li>

  <li>MENU/XMB/OZONE: Add playlist icons under ''Load Content''</li>

  <li>MENU/XMB/OZONE: Thumbnail improvements</li>

  <li>MENU/XMB/OZONE: Savestate thumbnail fullscreen + dropdown</li>

  <li>MENU/XMB/OZONE: Prevent unnecessary thumbnail requests when scrolling through
  playlists</li>

  <li>MENU/OZONE: Fix playlist thumbnail mouse hover after returning from Quick Menu</li>

  <li>MENU/OZONE: Thumbnail visibility corrections</li>

  <li>MENU/OZONE: Playlist metadata reformat</li>

  <li>MENU/OZONE: Savestate thumbnail fixes</li>

  <li>MENU/OZONE: Add savestate thumbnails</li>

  <li>MENU/OZONE: Header icon spacing adjustment</li>

  <li>MENU/RGUI: Savestate thumbnails</li>

  <li>MENU/SETTINGS: Turn Advanced Settings on by default, this entire filtering of
  settings will need a complete rethink anyways</li>

  <li>MENU/WIDGETS: Widget color + position adjustments</li>

  <li>MIYOO: Exclude unused HAVE_HID for Miyoo</li>

  <li>MIYOO: Enable screenshots</li>

  <li>MIYOO: Enable rewind</li>

  <li>NETWORK: Allow MITM server selection on OK callback</li>

  <li>NETWORK: Replace socket_select calls</li>

  <li>NETWORK: Implement binary network streams</li>

  <li>NETWORK: Poll support</li>

  <li>NETWORK: Check connect errno for successful connection</li>

  <li>NETWORK: Get rid of the timeout_enable parameter for socket_connect</li>

  <li>NETWORK: Fix getnameinfo_retro''s port value for HAVE_SOCKET_LEGACY platforms</li>

  <li>NETWORK: Define inet_ntop and inet_pton for older Windows versions</li>

  <li>NETWORK: Define isinprogress function</li>

  <li>NETWORK/NATT: Move natt files to "network"</li>

  <li>NETWORK/NETWORK STREAMS: Add function netstream_eof</li>

  <li>NETWORK/NETPLAY: Fix game CRC parsing</li>

  <li>NETWORK/NETPLAY: Disable and hide stateless mode</li>

  <li>NETWORK/NETPLAY: Change default for input sharing to "no sharing"</li>

  <li>NETWORK/NETPLAY: Enforce a timeout during connection</li>

  <li>NETWORK/NETPLAY: Disallow clients from loading states and resetting</li>

  <li>NETWORK/NETPLAY: Special saves directory for client</li>

  <li>NETWORK/NETPLAY: Ensure current content is reloaded before joining a host</li>

  <li>NETWORK/NETPLAY: Fix client info devices index</li>

  <li>NETWORK/NETPLAY: Fix input for some cores when hosting</li>

  <li>NETWORK/NETPLAY: Memory leak fixes</li>

  <li>NETWORK/NETPLAY: Force a core update when starting netplay</li>

  <li>NETWORK/NETPLAY: Fix NAT traversal announce for HAVE_SOCKET_LEGACY platforms</li>

  <li>NETWORK/NETPLAY: Refactor fork arguments</li>

  <li>NETWORK/NETPLAY: Fix content reload deadlocks on static core platforms</li>

  <li>NETWORK/NETPLAY: Disallow netplay start when content is not loaded for static
  core platforms</li>

  <li>NETWORK/NETPLAY: Show client slowdown information</li>

  <li>NETWORK/NETPLAY: Improve check frames menu entry</li>

  <li>NETWORK/NETPLAY: Do not try to receive new data if the data is in the buffer</li>

  <li>NETWORK/NETPLAY: Copy data on receive, even if the buffer is full</li>

  <li>NETWORK/NETPLAY: Fix lobby sublabel CRC display on some platforms</li>

  <li>NETWORK/NETPLAY: Support for customizing chat colors</li>

  <li>NETWORK/NETPLAY: Small launch compatibility patch adjustments</li>

  <li>NETWORK/NETPLAY: Support for banning clients</li>

  <li>NETWORK/NETPLAY: Minor tweaks to the find content task</li>

  <li>NETWORK/NETPLAY: Support for gathering client info and kicking</li>

  <li>NETWORK/NETPLAY: Fix possible deadlock</li>

  <li>NETWORK/NETPLAY: Initialize client''s allow_pausing to true</li>

  <li>NETWORK/NETPLAY: Disable netplay for unsupported cores - with stateless mode
  being disabled for now, there is no reason not to include this. Refuse to initialize
  netplay when the current core is not supported (no proper savestates support)</li>

  <li>NETWORK/NETPLAY/DISCOVERY: Ensure fixed width ints on packet struct</li>

  <li>NETWORK/NETPLAY/DISCOVERY: Support for IPv4 tunneling (6to4)</li>

  <li>NETWORK/NETPLAY/DISCOVERY/TASKS: Netplay/LAN Discovery Task refactor -  aims
  to prevent blocking the main thread while awaiting for the LAN discovery timeout;
  This is accomplished by moving the whole discovery functionality into its task and
  using a non-blocking timer to finish the task. Also fixes discovery sockets not
  being made non-blocking, which could cause the main thread to hang for very long
  periods of time every pre-frame.</li>

  <li>NETWORK/NETPLAY/TASKS: Find content task refactor - fixes many issues along
  the way, including a couple of nasty memory leaks that would leak thousands of bytes
  each time the task ran. It also expands the original concept by matching currently
  run content by filename (CRC matching is always performed first though).</li>

  <li>NETWORK/NETPLAY/TASKS: Find content task refactor - Ensure CRC32 is 8 characters
  long</li>

  <li>NETWORK/NETPLAY/LOBBY: Add setting for filtering out rooms with non-installed
  cores</li>

  <li>NETWORK/NETPLAY/LOBBY: Hide older (incompatible) rooms</li>

  <li>NETWORK/NETPLAY/LOBBY: Add a toggleable filter for passworded rooms. In addition,
  move lobby filters into its own submenu for better organization.</li>

  <li>NETWORK/NETPLAY/MENU: Chat supported info for the host kick submenu</li>

  <li>NETWORK/NETPLAY/MENU: Localize relay servers</li>

  <li>NETWORK/NETPLAY/MENU: Host Ban Submenu</li>

  <li>NETWORK/NETPLAY/MENU: Add client devices info to the kick sub-menu</li>

  <li>NETWORK/NETPLAY/MENU: Path: Netplay -&gt; Host -&gt; Kick Client - Allows the
  host to kick clients. Allows the host to view client information: connected clients
  (names), status (playing/spectating) and ping.</li>

  <li>NETWORK/NETPLAY/VITA: Add net_ifinfo support</li>

  <li>NETWORK/NETPLAY/VITA: Enable partial LAN discovery</li>

  <li>NETWORK/NETPLAY/VITA: Change default UDP port to 19492</li>

  <li>NETWORK/NETPLAY/VITA: Do not multiply negative timeout values</li>

  <li>NETWORK/NETPLAY/VITA: Fix epoll''s timeout parameter</li>

  <li>NETWORK/NETPLAY/VITA: Launch compatibility patch</li>

  <li>NETWORK/NETPLAY/3DS: Launch compatibility patch</li>

  <li>NETWORK/NETPLAY/3DS: Adapt POLL for 3DS platform</li>

  <li>NETWORK/NETPLAY/PS3: Launch compatibility patch</li>

  <li>NETWORK/NETPLAY/WII: Enable net_ifinfo for some features. In practice, this
  only allows the netplay''s UPnP task to succeed on the Wii.</li>

  <li>NETWORK/NETPLAY/WIIU: Launch compatibility patch</li>

  <li>NETWORK/NETPLAY/SWITCH: Launch compatibility patch</li>

  <li>NETWORK/UPNP: Attempt support for remaining platforms</li>

  <li>NETWORK/UPNP: Support for IPv4 tunneling</li>

  <li>ODROID GO2: Increase DEFAULT_MAX_PADS to 8 for ODROIDGO2, since that impacts
  the RG351[X] consoles. The RG351[X] have a USB host controller and can have an arbitrary
  number of USB gamepads.</li>

  <li>ONLINE UPDATER: Online Updater menu reorganizing</li>

  <li>OSX: Fixed items of system top menu bar on macOS</li>

  <li>OSX: Revision to macOS app icon set</li>

  <li>PLAYLISTS: Ensure history list will contain CRC32</li>

  <li>PLAYLISTS: Fix CRC32 comparison - as state-&gt;content_crc has "|crc" suffix.</li>

  <li>PS4/ORBIS: Orbis/PS4 Support using OrbisDev toolchain</li>

  <li>PS4/ORBIS: Update xxHash dependecy</li>

  <li>PS4/ORBIS: Shader cache</li>

  <li>RETROFW: Exclude unused HAVE_HID for RetroFW</li>

  <li>RETROFW: Support battery indicator on RetroFW</li>

  <li>RETROFW: Enable menu toggle button on retrofw devices</li>

  <li>SHADERS: Shader Preset Loading of Multiple additional #references lines for
  settings</li>

  <li>SHADERS: Shader Load Extra Parameter Reference Files - this adds the ability
  to put additional #reference lines inside shader presets which will load additional
  settings. The first reference in the preset still needs to point at a chain of presets
  which ends with a shader chain, and subsequent #reference lines will load presets
  which only have parameter values adjustment. This allows presets to be made with
  a modular selection of settings. For example with the Mega Bezel one additional
  reference could point at a preset which contained settings for Night mode vs Day
  mode, and another reference could point to a preset which contained settings for
  how much the screen should be zoomed in.</li>

  <li>SHADERS/MENU: Increase shader scale max value</li>

  <li>SCANNER/DC: Fix Redump bin/cue scan for some DC games</li>

  <li>SCANNER/GC/WII: Add RVZ/WIA scan support for GC/Wii</li>

  <li>SCANNER/PS1: Improved success rate of Serial scanning on PS1 by adding support
  for the xx.xxx format</li>

  <li>SCANNER/PS1: Changed return value of detect_ps1_game function to actuially return
  a failure when the Serial couldn''t be extracted. Scanner will then fallback on   crc
  check, and usually ends up finding the games in the database.</li>

  <li>SWITCH: Enable RWAV (WAV audio file) support</li>

  <li>STRING: Do not assume char is unsigned</li>

  <li>TASKS: More thread-awareness in task callbacks</li>

  <li>TASKS: Fix race condition at task_queue_wait</li>

  <li>TVOS: Revised tvOS icons w/ updated alien.</li>

  <li>VFS: Fix various VFS / file stream issues</li>

  <li>VULKAN: Fix more validation errors</li>

  <li>VULKAN: Attempt to fix validation errors with HDR swapchain. Always use final
  render pass type equal to swapchain format. Use more direct logic to expose if filter
  chain emits HDR10 color space or not</li>

  <li>VULKAN/ANDROID: Honor SUBOPTIMAL on non-Android since you''d want to recreate
  swapchains then. On Android it can be promoted to SUCCESS.<br>

  SUBOPTIMAL_KHR can happen there when rotation (pre-rotate) is wrong.</li>

  <li>VULKAN/DEBUG: Automatically mark buffer/images/memory with names</li>

  <li>VULKAN/DEBUG: Move over to VK_EXT_debug_utils. Debug marker is deprecated years
  ago.</li>

  <li>VULKAN/HDR: Fix leak of HDR UBO buffer</li>

  <li>VULKAN/BFI: Fix BFI (Black Frame Insertion) regression</li>

  <li>WINDOWS: Fix exclusive fullscreen video refresh rate when vsync swap interval
  is not equal to one - refresh rate in exclusive fullscreen mode was being incorrectly
  multiplied by vsync swap interval, breaking swap interval functionality at the gfx
  driver level</li>

  <li>WIN32: Do optimization for Windows where we only update the title with SetWindowText
  when the previous title differs from the current title</li>

  <li>WIN32: Skip console attach when logging to file</li>

  <li>WIN32: Remove black margins with borderless non-fullscreen window</li>

  <li>WIN32/TASKBAR: Release ITaskbarList3 on failed HrInit - pointer wasn''t NULL''d,
  thus set_window_progress would cause weird behavior</li>

  <li>WII/GX: Fix potential datarace</li>

  <li>WIIU: Implement sysconf and __clear_cache</li>

  <li>WIIU: Add OS memory mapping imports</li>

  <li>UWP: Added launch protocol arg ''forceExit'' so a frontend can tell an already-running
  RetroArch UWP instance to quit.</li>

  <li>UWP: Enable core downloader/updater</li>

  <li>UWP: Remove copy permissions as its inefficient as we can just directly assign
  the new ACL and that works</li>

  <li>Xbox/UWP: Remove expandedResources</li>

  <li>Xbox/UWP: UWP OnSuspending crash fix</li>

  <li>Xbox/UWP: Enable savestate file compression by default for UWP/Xbox - got told
  there are no more issues with it</li>

  <li>Xbox/UWP: Add support for 4k to angle on xbox for MSVC2017 build</li>

  </ul>'
updated: '2022-09-30T13:08:57Z'
version: v1.11.0
version_title: v1.11.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
