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
download_page: https://buildbot.libretro.com/stable/1.22.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.22.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.22.0/nintendo/3ds/RetroArch_cia.7z
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
stars: 12142
systems:
- 3DS
title: RetroArch
unique_ids:
- '0xBAC00'
update_notes: '<ul dir="auto">

  <li>ANDROID: OnNewIntent handler to allow launchers start new content without closing
  first</li>

  <li>ANDROID: Use app-specific storage for Google Play builds of RetroArch</li>

  <li>ANDROID: Implement support for the Storage Access Framework, to allow the user
  to mount most directories1 from internal storage, the SD card, other removable storage
  devices and any document providers provided by other Android apps on the current
  device.</li>

  <li>APPLE: Include sameduck, gearcoleco, geargrafx cores in App Store builds</li>

  <li>APPLE: Include reminiscence, virtualjaguar, vitaquake2 cores in App Store builds</li>

  <li>APPLE: Include gam4980 core in App Store builds</li>

  <li>APPLE: Bundle identifier added to Information menu</li>

  <li>APPLE: Option to control the usage of Metal argument buffers</li>

  <li>APPLE: Don''t force fullscreen, allow multitasking on iPad</li>

  <li>APPLE: AppIntents for Siri, Shortcuts</li>

  <li>APPLE: Fix ffmpeg camera driver</li>

  <li>APPLE/MFI: Try harder to own the home button</li>

  <li>AUDIO: Microphone CoreAudio driver for iOS and macOS</li>

  <li>AUTOCONF: Autoconfig match extended with a physical identifier</li>

  <li>CAMERA: Use ffmpeg libavfilter virtual input device as default</li>

  <li>CHEEVOS: Show additional message for unsupported achievements</li>

  <li>CHEEVOS: Upgrade to rcheevos 12.1</li>

  <li>CHEEVOS: Change expired token message from info to error</li>

  <li>CHEEVOS: Hashing of RVZ files is now supported</li>

  <li>CLOUDSYNC: Enable icloud_drive cloud sync backend on MacOS / iOS</li>

  <li>CLOUDSYNC: Don''t always trust the server hash</li>

  <li>CLOUDSYNC: Enable WebDAV support for Android</li>

  <li>CLOUDSYNC: Speed up cloudsync on Apple</li>

  <li>DATABASE: Improve multidisk game scanning</li>

  <li>DATABASE: Filter in Database Manager now works for genre and region</li>

  <li>EMSCRIPTEN: Support core switching</li>

  <li>EMSCRIPTEN: Support suspend screensaver</li>

  <li>EMSCRIPTEN/RWEBCAM: Fix camera driver</li>

  <li>EMSCRIPTEN/RWEBINPUT: Add accelerometer/gyroscope support</li>

  <li>EMSCRIPTEN/RWEBPAD: Add rumble support</li>

  <li>EMSCRIPTEN/RWEBAUDIO: Rewrite driver, set as default audio driver</li>

  <li>INPUT: Default key and mouse binds for lightgun Start and Select buttons</li>

  <li>INPUT: Turbo mode corrections</li>

  <li>INPUT: Turbo fire settings are now saved to remaps, not to overrides</li>

  <li>INPUT: Fix menu usage when OK/Cancel has mouse binds</li>

  <li>INPUT: Ignore menu mouse startup position before moving</li>

  <li>INPUT: Fix heavy slowdown when using Bluetooth XInput controllers with rumble</li>

  <li>INPUT: Reset and close content hotkeys now require confirmation, similar to
  quit</li>

  <li>INPUT: Menu toggle and hotkey enable can now be assigned to the same key</li>

  <li>INPUT: Option to have hotkeys follow the port mapped first to the core</li>

  <li>INPUT/ANDROID: Favor mouse coordinates for lightgun</li>

  <li>INPUT/UDEV: Fix lost terminal settings after restart from menu</li>

  <li>INPUT/BSV/REPLAY: Bumped replay format version to 2. Old replays will still
  play back fine.</li>

  <li>INPUT/BSV/REPLAY: Add option to skip deserializing checkpoints from replay files
  (it introduces jank in some emulators).</li>

  <li>INPUT/BSV/REPLAY: Add checkpoint and initial savestate compression, following
  the <code class="notranslate">savestate_file_compression</code> config boolean.  Use
  zstd if available, or fall back to zlib.</li>

  <li>INPUT/BSV/REPLAY: Add incremental checkpoints based on statestreams (depending
  on <code class="notranslate">HAVE_STATESTREAM</code> compile time flag).  As an
  example, 60 <code class="notranslate">pcsx_rearmed</code> savestates would take
  267MB uncompressed; with incremental encoding this is reduced to 77MB.  Compressing
  the result can reduce the size to just 4MB.</li>

  <li>INPUT/BSV/REPLAY: Checkpoint compression and encoding can be combined. For example,
  60 <code class="notranslate">pcsx_rearmed</code> checkpoints can take up just 15MB
  if each state is incremental and compressed. This is not as optimal as using incremental
  states without save state compression followed by offline compression, but is a
  good compromise in many use cases.</li>

  <li>INPUT/BSV/REPLAY: Add hotkeys and text commands to force a checkpoint insertion
  into the currently recording replay, and to seek backwards to the previous checkpoint
  and forwards to the next checkpoint.</li>

  <li>INPUT/BSV/REPLAY: Add a text command to seek to a specific frame of the currently
  playing/recording replay; it will return via the command replier the actual seeked-to
  frame (right now it only supports seeking to checkpoints).</li>

  <li>INTL: Add Irish Gaelic to selectable languages</li>

  <li>IOS: Use native keyboard in search</li>

  <li>IOS: Fix crash on iOS9 when fetching refresh rate</li>

  <li>IOS: Stronger haptics, controllable by setting</li>

  <li>IOS: Down arrow menu is removed, all 3 options are available by other means
  now</li>

  <li>IOS/MACOS: Fix display server resolution and refresh rates</li>

  <li>IOS/TVOS: Use native keyboard</li>

  <li>LIBRETRO: Deprecate intfstream_open_writable_memory</li>

  <li>LIBRETRO: New environment function RETRO_ENVIRONMENT_GET_TARGET_SAMPLE_RATE</li>

  <li>LINUX: Add full complement of key/value pairs to desktop entry</li>

  <li>MACOS: Fix coreaudio microphone handling</li>

  <li>MACOS: Fix window size calculation</li>

  <li>MENU: Common Thumbnail Background option for all menu drivers</li>

  <li>MENU: Move core options reset from Settings/Configuration to Main Menu / Configuration
  Files</li>

  <li>MENU: Use right analog stick for thumbnail cycling in playlists</li>

  <li>MENU: Option to always suggest cores, even when a core is already loaded</li>

  <li>MENU: Option to show Favorites before History</li>

  <li>MENU: Media history playlists are now visible in playlist manager</li>

  <li>MENU: Import Content visibility defaults reverted</li>

  <li>MENU: Update CRTSwitchRes menu options for future use</li>

  <li>MENU: Debug builds are indicated in Information menu</li>

  <li>MENU: Save As / Save Main options for configuration file</li>

  <li>MENU: Unwanted input is prevented when menu is triggered by toggle combo</li>

  <li>MENU: 32-bit values in cheats and rumble are not presented as huge lists</li>

  <li>MENU: Less important widgets are now sized like task notifications</li>

  <li>MENU: Play count is added to runtime log</li>

  <li>MENU: Configurable startup page (several options beside default Main Menu)</li>

  <li>MENU: Shader menu rework, combined save/remove menus, save current, Y and Start
  hotkeys for shader parameters and background opacity toggle</li>

  <li>MENU: Single-click start option from playlists and Explore view</li>

  <li>MENU: Allow kiosk mode and hiding of Settings menu also in GLUI and RGUI</li>

  <li>MENU: Task widget improvements</li>

  <li>MENU/GLUI: Show thumbnails in Explore view</li>

  <li>MENU/XMB: Improvements for mobile/touch. More natural horizontal/vertical scrolling</li>

  <li>MENU/XMB: Select button toggles thumbnails in playlists</li>

  <li>MENU/XMB,OZONE: Fix content icons when playlist tabs are hidden</li>

  <li>MENU/OZONE: Horizontal padding factor option</li>

  <li>MENU/OZONE: Custom font selection and scaling factor</li>

  <li>MENU/RGUI: Clock format is now configurable and moved to top header</li>

  <li>NETPLAY: Push room info to lobby</li>

  <li>NETWORK: Fixes for nmcli wifi driver</li>

  <li>NETWORK: Network command interface enabled for Android, iOS, TVOS</li>

  <li>OTHER: ZStandard support and libchdr update for support of chd files converted
  with createdvd option</li>

  <li>OVERLAY: Speed limit on touch pointer tracking</li>

  <li>OVERLAY: Dedicate each touch pointer to hitboxes or pointing devices</li>

  <li>OVERLAY: Fix overlay turbo fire</li>

  <li>PLAYLIST: Built-in playlists are now stored under playlists/builtin</li>

  <li>PLAYLIST: Fix subsystem information in playlists</li>

  <li>PS3: Fix psl1ght target of dist-cores.sh</li>

  <li>REPLAY: Bugs fixed regarding rewind</li>

  <li>REPLAY: Same timeline check and future state check for replays vs. savestates</li>

  <li>SAVESTATES: Savestate thumbnails are default enabled for x86_64 builds</li>

  <li>SAVESTATES: Slot is now remembered using the runtime log file</li>

  <li>SAVESTATES: Slot hotkey widget shows save state thumbnail</li>

  <li>SCAN: Fix crash with Sega CD</li>

  <li>SCAN: Log files without database match</li>

  <li>SCAN: Optimization of database queries by content file size</li>

  <li>VIDEO: Fix auto swap interval setup</li>

  <li>VIDEO: Improvements for integer scale half scaling</li>

  <li>VIDEO: Adjustments to smart integer scaling, considering title safe area</li>

  <li>VIDEO: Frame delay improvements for the automatic setting</li>

  <li>VIDEO: Auto-enable GPU recording with HW context cores</li>

  <li>VIDEO: Fix viewport bias when using custom aspect ratio</li>

  <li>VIDEO/D3D11/D3D12: snappy extra vsync presentation mode</li>

  <li>VIDEO/GL: Fallback OpenGL symbol loader for Linux devices with EGL &lt; 1.5</li>

  <li>VIDEO/GL: Support for Cg and GLSL shaders in the GLCore video driver</li>

  <li>VIDEO/GL: Improve GLES version detection</li>

  <li>VIDEO/SHADER: Shader hold function, useful for some lightguns and shader comparison</li>

  <li>VIDEO/SWITCHRES: Horizontal and vertical geometry adjustment options added</li>

  <li>VIDEO/SWITCHRES: Game overrides</li>

  <li>VIDEO/VULKAN: Add VK_EXT_full_screen_exclusive extension support for Windows</li>

  <li>VIDEO/WAYLAND: Support for xdg-toplevel-icon-v1</li>

  <li>VIDEO/WAYLAND: Fix deadlock when using Wayland Vulkan driver</li>

  <li>VIDEO/WAYLAND: Fix fullscreen on auto monitor index (partial)</li>

  <li>VITA: Touchscreen support for PS Vita</li>

  <li>VITA: Set RGUI framebuffer to 272 lines to remove blurriness</li>

  <li>WEBOS: Various fixes and tunings</li>

  <li>WEBOS: Disable core dumps</li>

  <li>WEBOS: Debug builds enabled</li>

  <li>WEBOS: Fix GLES 3/3.1/3.2 option, enable 64-bit option</li>

  </ul>'
updated: '2025-11-12T21:49:34Z'
version: v1.22.0
version_title: v1.22.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
