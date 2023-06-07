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
download_page: https://buildbot.libretro.com/stable/1.15.0/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.15.0/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: null
    url: https://buildbot.libretro.com/stable/1.15.0/nintendo/3ds/RetroArch_cia.7z
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

  <li>AI SERVICE: Fix NVDA switching to Powershell on speak</li>

  <li>ANDROID: In Android builds, add input_android_physical_keyboard configuration
  option and its corresponding menu entry to force a device to act as a physical keyboard.
  When running on Android, RetroArch considers most devices that emit dpad events
  as gamepads, even if they also emit other keyboard events; this is usually the right
  thing to do, but it has the side effect of not letting some actual keyboards (e.g.:
  Logitech K480) act as such inside RetroArch. This configuration option allows users
  to manually select a specific input device to act as a physical keyboard instead
  of a gamepad, which is handy when emulating computers as opposed to consoles.</li>

  <li>APPLE: Add App Category to a few places it should have been</li>

  <li>APPLE/MFI: Prevent crash when controller player index is unset (-1)</li>

  <li>AUTOMATIC FRAME DELAY: Helped delay to decrease easier when it should and helped
  delay to stay put when it should when triggering pause &amp; menu with or without
  pause &amp; fast-forward &amp; slow-motion &amp; geometry change</li>

  <li>AUTOMATIC FRAME DELAY: Recalibrate delay on video reinit (fullscreen toggle
  and such)</li>

  <li>AUTOMATIC FRAME DELAY: Show (x effective) only in menu item and not in dropdown
  list items when auto is enabled</li>

  <li>CHEEVOS: Allow repositioning of RetroAchievement notifications</li>

  <li>CHEEVOS/MENU: Add Achievements Visibility submenu option</li>

  <li>CHEEVOS/MENU: Startup Summary split off from Verbose Mode, added option to hide
  for games with zero core cheevos</li>

  <li>CHEEVOS/MENU: ''Unlocks/Mastery'' split into two options</li>

  <li>CHEEVOS/MENU: ''Account/Login Messages'' split off from ''Verbose'', gated all
  login success/error messages</li>

  <li>CONFIG/INPUT: Unload restores current global config</li>

  <li>CONFIG/INPUT/OVERRIDES: Removing a file does not unload current override</li>

  <li>CONFIG/INPUT/OVERRIDES: Saving an empty override removes the file if it exists,
  and won''t save when it does not</li>

  <li>CONFIG/INPUT/OVERRIDES: Prevent the use of RUNLOOP_FLAG_OVERRIDES_ACTIVE with
  appendconfig</li>

  <li>CORE OPTION: Core option setting type checks. Added checks for getting and setting
  core option type, since otherwise there will be a crash on close content after browsing
  to core option categories. Also fixed the no-show switch icon for lone wolf "Lock
  Installed Core".</li>

  <li>CLI: Update selected save slot when start with cli --entryslot</li>

  <li>CLI: Decouple config CLI append and config overrides</li>

  <li>CLI/MENU/XMB: Stop showing bogus previous icon on CLI launch</li>

  <li>D3D9: Fixed display driver scissoring implementation  - can now accept 0 width/height</li>

  <li>D3D10: Fixed display driver scissoring implementation - can now accept 0 width/height</li>

  <li>D3D11: Fixed display driver scissoring implementation - can now accept 0 width/height</li>

  <li>D3D11: Fixed build when HAVE_DXGI_HDR is not defined</li>

  <li>D3D11: Moved waitable swapchain waiting to happen always even when resizing
  swapchain</li>

  <li>D3D12: Fixed display driver scissoring implementation - can now accept 0 width/height</li>

  <li>D3D12: Fixed window scaling issue, which was caused by swapchain resize function
  not using the same flags (waitable swapchain) as swapchain creation</li>

  <li>D3D12: Fixed swapchain scissoring issue (visual + crash) after manually resizing
  window to smaller size</li>

  <li>D3D12: Fixed eventual crashing issue on video reinit when swapchain is being
  freed</li>

  <li>D3D12: Moved waitable swapchain waiting to happen always even when resizing
  swapchain</li>

  <li>EMSCRIPTEN: Add HAVE_PATCH support for Emscripten</li>

  <li>EMSCRIPTEN: Add BSV/Replay support for Emscripten</li>

  <li>EMSCRIPTEN: Add command and stdin_cmd features to emscripten RA. update libretro.js
  to show how commands could be sent over emscripten stdin.</li>

  <li>FRAME DELAY/MENU: Show Frame Delay without VSync</li>

  <li>GENERAL: Start unpause restriction. Limit the feature using retropad start button
  to unpause RA to the setting it was made for; "pause on controller disconnect".</li>

  <li>GENERAL: Savestate thumbnail aspect ratio fallback. Thanks to at least one certain
  core that announces aspect ratio as 0, we have to add the same fallback in savestate
  thumbnails that is happening elsewhere in normal video driver use anyway.</li>

  <li>GENERAL: Add support for system subdirs per core/database. Added the trivial
  and graceful automatic ability to send a different system directory to cores if
  it exists, for keeping the system dir more sane. First by using the core/library
  name just like in configs and saves, and then by playlist name, like in thumbnails,
  and of course default to the current global system dir.</li>

  <li>GENERAL: Ignore system subdir replacement if subdir has subdirs.</li>

  <li>GENERAL: Restore cached video driver always on quit</li>

  <li>IOS: Include ''Update Core Info Files''</li>

  <li>IOS: Fix <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="1513227857" data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/14778"
  data-hovercard-type="issue" data-hovercard-url="/libretro/RetroArch/issues/14778/hovercard"
  href="https://github.com/libretro/RetroArch/issues/14778">#14778</a> - In addition
  to sending logs to asl_client, add them to the logfile.</li>

  <li>IOS/VULKAN/MOLTENVK: Vulkan video driver on iOS</li>

  <li>LATENCY/PREEMPTIVE FRAMES: Add Preemptive Frames to Latency Settings. RunAhead
  alternative that reruns core logic to "rewrite history" before the current frame.
  Frames are only rerun when the controller state changes, so it''s faster overall.</li>

  <li>LATENCY/PREEMPTIVE FRAMES: Call retro_run before retro_serialize (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1552356794" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14893" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14893/hovercard" href="https://github.com/libretro/RetroArch/pull/14893">#14893</a>).
  Fixes preemptive frames not starting up with a few cores</li>

  <li>LIBRETRO-COMMON/VFS/FILESTREAM: Fixes filestream_vscanf regression</li>

  <li>LOCALIZATION: Updates</li>

  <li>LOCALIZATION: Enable localization of video rotation, orientation, and aspect
  ratio option values.</li>

  <li>LOCALIZATION: Mixer stream localization also added</li>

  <li>LOCALIZATION/MENU/HELP: Context dependent help text for audio and video drivers.
  Language corrections</li>

  <li>LOCALIZATION/MENU/LANGUAGE: Language submenu now shows the progress of translated
  strings for each language.</li>

  <li>LOCALIZATION: Help texts now localizable through Crowdin.</li>

  <li>LIBRETRO: Enable RETRO_ENVIRONMENT_SET_SUPPORT_NO_GAME for libretro-video-processor</li>

  <li>LIBRETRO/HW: Add GET_HW_CONTEXT_NEGOTIATION_INTERFACE_SUPPORT. Works around
  issues in v1 interface where it was not possible to<br>

  query what frontend would do when faces with newer interface versions. This env-call
  gives stronger guarantees how things have to work.</li>

  <li>INPUT: Allowing keyboard hotkeys to work without hotkey modifier if modifier
  is only mapped to RetroPad</li>

  <li>INPUT: Allowing keyboard hotkey keys for typing if hotkey modifier is set to
  keyboard but not pressed</li>

  <li>INPUT: Allowing keyboard RetroPad keys for typing if emulated device type is
  "None"</li>

  <li>INPUT/AUTOCONFIG: Check for ''enable_hotkey'' also from autoconf binds</li>

  <li>INPUT/BLUETOOTH: Fix a crash in for BT HID devices. (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1561147322" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14922" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14922/hovercard" href="https://github.com/libretro/RetroArch/pull/14922">#14922</a>)
  pad_connection_destroy() frees slots, no need to free it again.</li>

  <li>INPUT/BSV/REPLAY: Don''t start video recording when BSV recording starts</li>

  <li>INPUT/BSV/REPLAY: Don''t double-record inputs in BSV recording</li>

  <li>INPUT/BSV/REPLAY: Don''t autoload states if a BSV file is being played back
  or recorded</li>

  <li>INPUT/BSV/REPLAY: Moved BSV initialization before autoload code</li>

  <li>INPUT/BSV/REPLAY: Don''t trigger autoload code if there is bsv movie state</li>

  <li>INPUT/BSV/REPLAY: Allow for both -e and -R to start a BSV file recording at
  a state</li>

  <li>INPUT/BSV/REPLAY: Add keyboard recording support to BSV</li>

  <li>INPUT/BSV/REPLAY: Fix BSV playback from a starting state for DOSbox</li>

  <li>INPUT/BSV/REPLAY: Associate states with replays. Now states can be saved and
  loaded during replay recording and playback in a way that keeps the integrity of
  the recording. Recordings also have a (moderately) unique identifier associated
  with them.</li>

  <li>INPUT/BSV/REPLAY: Add checkpointing feature for replay recordings. If cores
  are not deterministic, or if they only have bounded determinism, we can obtain less
  drift if replay files also contain periodic checkpoint states.  These are configured
  by the new retroarch setting replay_checkpoint_interval (measured in seconds).  States
  are inserted into the replay file in between frames. This also fixes the settings
  display for the replay autoincrement max keep setting.</li>

  <li>INPUT/FRAMEADVANCE: Use non-rendering pause mode when frameadvance is triggered</li>

  <li>INPUT/HOTKEYS/OVERLAYS: Do not block input overlay hotkeys</li>

  <li>INPUT/HOTKEYS: Hotkey blocking correction. Turned out the previous hotkey blocking
  changes worked properly only with winraw driver and not the rest (at least with
  Windows), because input_keyboard_event() could be called at the wrong moment, and
  thus storing keyboard menu press there broke the separation of controller Guide
  menu button and keyboard menu key. Also allowed the blocking to work in both directions
  so that controller hotkeys won''t get blocked if only keyboard has "enable_hotkey"
  bind.</li>

  <li>INPUT/LINUX/UDEV: Fix udev guns input when id_mouse is not id_joystick</li>

  <li>MENU: Rename ''Standalone Cores'' to ''Contentless Cores''</li>

  <li>MENU: Music files should also obey builtin_mediaplayer_enable (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1580229958" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14967" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14967/hovercard" href="https://github.com/libretro/RetroArch/pull/14967">#14967</a>)
  Disabling the built in media player should be possible for music files<br>

  as well. Without this, sound files can not be opened from file browser with cores
  that support them.</li>

  <li>MENU: Relocated items to a more logical order</li>

  <li>MENU: Corrected some title capitalizations (when/before/after are not low case,
  but for/the/a are)</li>

  <li>MENU/AUDIO: Add dropdown menu for audio device</li>

  <li>MENU/HELP: Help for turbo modes (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1560932243" data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/14919"
  data-hovercard-type="pull_request" data-hovercard-url="/libretro/RetroArch/pull/14919/hovercard"
  href="https://github.com/libretro/RetroArch/pull/14919">#14919</a>). Help text added
  for each of the selectable turbo modes.</li>

  <li>MENU/INPUT: Add unified back action to all menu drivers. Usability boost for
  all menu drivers resulting in similar behavior as with Ozone currently, which is
  pressing back/cancel enough the selection jumps first to Main Menu and when pressed
  again jumps to the first item, so that when a core is running, Quick Menu is very
  quickly accessible from anywhere. And when core is not running, the first item would
  be Load Core.</li>

  <li>MENU/INPUT: Override bind save + menu manager overhaul</li>

  <li>MENU/INPUT: Allowed and fixed input bind saving to overrides</li>

  <li>MENU/INPUT: Overhauled override menu</li>

  <li>MENU/INPUT: Pressing Start on the top active file entry reloads current overrides
  as startup would</li>

  <li>MENU/SUBLABELS: All under "Configuration File" + moved "Reset to Defaults" to
  bottom</li>

  <li>MENU/SUBLABELS: Quick Menu &gt; Controls &gt; Port x Controls</li>

  <li>MENU/SUBLABELS: Port x Controls &gt; Device Type</li>

  <li>MENU/RGUI: Fix disabled menu item color. The effect was not working properly,
  since transparency meant using the core output color as background.</li>

  <li>MENU/XMB: Horizontal icon animation fix</li>

  <li>MENU/XMB: Fixed playlist manager icons to take Explore Views into account properly</li>

  <li>MENU/XMB: Changed XMB Explore View title to match Ozone</li>

  <li>MENU/XMB: Added "Switch Icons" option</li>

  <li>MENU/XMB: Fix MENU_ACTION_CANCEL when search is active. Nasty issue discovered
  in XMB which broke search term cancelation.</li>

  <li>MENU/XMB: Layout corrections:</li>

  <li>MENU/XMB: More room for longer item labels and values</li>

  <li>MENU/XMB: "Core Downloader" has extra space for item and "installed" indicator</li>

  <li>MENU/XMB: Fixed "Menu Scale Factor" to not require restarting to get the actual
  end result</li>

  <li>MENU/XMB: Adjusted scale factor to behave better with both layouts</li>

  <li>MENU/XMB: Fixed savestate thumbnails and adjusted vertical fade factor in "Handheld"
  layout</li>

  <li>MENU/XMB: Changed thumbnail shadow to outline and tightened fullscreen thumbnail
  margins</li>

  <li>MENU/XMB: Adjusted global shadow opacity</li>

  <li>MENU/XMB: Remove "Framebuffer opacity" from XMB as it does not use it. Also,
  rename the corresponding menu title, since "framebuffer" is not that intuitive.</li>

  <li>MENU/OZONE: Fixed playlist manager icons to take Explore Views into account
  properly</li>

  <li>MENU/OZONE: Refresh thumbnail on close content hotkey</li>

  <li>MENU/OZONE: Ozone footer enhancements (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1561403885" data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/14926"
  data-hovercard-type="pull_request" data-hovercard-url="/libretro/RetroArch/pull/14926/hovercard"
  href="https://github.com/libretro/RetroArch/pull/14926">#14926</a>). Add Help button
  (Select) and Reset to Default (Start) to footer where applicable.</li>

  <li>MENU/OZONE: Ozone footer enhancements (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1566709194" data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/14934"
  data-hovercard-type="pull_request" data-hovercard-url="/libretro/RetroArch/pull/14934/hovercard"
  href="https://github.com/libretro/RetroArch/pull/14934">#14934</a>). Display Help
  footer only if there is actual info to be displayed, either actual help, or sublabel
  if it is not visible otherwise.</li>

  <li>MENU/OZONE: Ozone footer enhancement: Scan button (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1571011961" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14949" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14949/hovercard" href="https://github.com/libretro/RetroArch/pull/14949">#14949</a>).
  Display Scan button in footer when it is applicable.</li>

  <li>MENU/OZONE: Add Clear button to Ozone footer (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1570886718" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14947" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14947/hovercard" href="https://github.com/libretro/RetroArch/pull/14947">#14947</a>).
  Add indication of Clear button when it is applicable (currently: keybinds).</li>

  <li>MENU/MATERIALUI: Added missing Favorites+History icons in playlist manager</li>

  <li>MENU/MATERIALUI: Added "Switch Icons" option</li>

  <li>MENU/CHEATS: Added missing icons in cheats (Delete + Copy After/Before)</li>

  <li>MENU/CHEATS: Fixed label capitalization in cheats (Add New After/Before This)</li>

  <li>MENU/SOUNDS: Add scrolling sounds for RGUI, XMB, MaterialUI and Ozone.</li>

  <li>MENU/SOUNDS: Better scrolling sound implementation, add new ''notice back''
  sound</li>

  <li>MENU/SOUNDS: Scroll sound fixes. Correctly get list size in xmb.c for playing
  scrolling sound when switching categories, play the scrolling sound when pressing
  cancel in ozone, play the sound when scrolling with ZL and ZR, play the correct
  sound when scrolling with L</li>

  <li>MENU/WIDGETS: Show square sized widget on volume mute. Volume widget is currently
  fixed size always, and thus showing a lot of empty space when muting, therefore
  shorten the box to icon size only when muting.</li>

  <li>MIYOO: L3/R3 support for Dingux Gamepad controller device.</li>

  <li>NETWORKING: Call ssl_socket_close for SSL sockets</li>

  <li>NETWORKING/CHEEVOS: net_http - Temporary fix for cheevos crash. Don''t use new
  timeout/poll code for cheevos HTTP requests.</li>

  <li>NETWORKING/MENU: Network information cleanup:</li>

  <li>NETWORKING/MENU: Remove extra space from : delimiter</li>

  <li>NETWORKING/MENU: Trim useless/duplicate garbage from the end of ipv6 address.
  Windows shows %[adapter number], Linux shows %[adapter name], which already shows
  before the address</li>

  <li>NETWORKING/STDIN: Add LOAD_STATE_SLOT N command to stdin/network protocol</li>

  <li>OSD/STATISTICS: Add Run-Ahead data to on-screen statistics</li>

  <li>OSD/STATISTICS: Notification font + statistics adjustments</li>

  <li>OSD/STATISTICS: Finetuned statistics layout to be more compact and aligned</li>

  <li>OSD/STATISTICS: Group Run-Ahead and Frame Delay as "Latency"</li>

  <li>OSD/STATISTICS: Try to scale font as small as possible/readable if stats won''t
  fit</li>

  <li>OSD/STATISTICS/FONT: Allow reseting notification font with RetroPad Y to "null",
  which uses the fallback pixel font</li>

  <li>OSD/STATISTICS/FONT: Show "Default" instead of empty with default font</li>

  <li>OSD/STATISTICS/FONT: Start browsing font from assets instead of root</li>

  <li>OSX/MACOS: Steam platform support</li>

  <li>OSX/MACOS: Set LSApplicationCategoryType to games</li>

  <li>OSX/MACOS: Include OpenGL video driver on Metal macOS builds (10.13 and higher)</li>

  <li>OSX/MACOS: Fix a few mac windowed mode settings -</li>

  <li>OSX/MACOS: Use "Remember window position and size" setting (fixes <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1520562158" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14806" data-hovercard-type="issue"
  data-hovercard-url="/libretro/RetroArch/issues/14806/hovercard" href="https://github.com/libretro/RetroArch/issues/14806">#14806</a>)</li>

  <li>OSX/MACOS: Implement window opacity</li>

  <li>OSX/MACOS: Enable "Show window decorations" toggle</li>

  <li>OSX/MACOS: Hide "Disable composition" option (osx does not support disabling
  composition)</li>

  <li>OSX/MACOS: Make sure to use the file system path name, not the URL name</li>

  <li>OSX/MACOS/IOHIDMANAGER: Various memory access fixes to prevent crashes (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1393648706" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14459" data-hovercard-type="issue"
  data-hovercard-url="/libretro/RetroArch/issues/14459/hovercard" href="https://github.com/libretro/RetroArch/issues/14459">#14459</a>)
  (<a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1592664051"
  data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/15000"
  data-hovercard-type="pull_request" data-hovercard-url="/libretro/RetroArch/pull/15000/hovercard"
  href="https://github.com/libretro/RetroArch/pull/15000">#15000</a>). Prevent double
  free and null dereference when the controller is quickly reconnected. Handle error
  when controller device query returns null instead of crashing.</li>

  <li>OSX/MACOS/METAL BUILD: Fix input events (keyboard/mouse) sometimes going lost
  when switching between fullscreen and windowed mode. Fixes lots of longstanding
  issues</li>

  <li>OSX/MACOS/OPENGL: Fix for fullscreen OpenGL driver in Metal macOS build</li>

  <li>OSX/MACOS/VULKAN/MOLTENVK: Default to Vulkan driver when available (for 10.13
  Metal Universal build)</li>

  <li>OSX/MACOS/VULKAN/MOLTENVK: Updated Vulkan on Metal for OSX via MoltenVK</li>

  <li>OSX/MACOS/VULKAN/MOLTENVK/HDR: Fix non-HDR colors</li>

  <li>OSX/MACOS/SLANG: The change to apply shaders would be executed and then a command
  to apply shaders would immeidately be enqueued, to run asynchronously<br>

  after the current event handler, which then did exactly the same. Fixes issue <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1515529110"
  data-permission-text="Title is private" data-url="https://github.com/libretro/RetroArch/issues/14789"
  data-hovercard-type="issue" data-hovercard-url="/libretro/RetroArch/issues/14789/hovercard"
  href="https://github.com/libretro/RetroArch/issues/14789">#14789</a> - Turning on
  shaders on Metal build 1.14.0 stable for Mac OS will slow emulation drastically
  thing, creating a busy loop.</li>

  <li>PS2: Avoid loading extra drivers when not needed. Fixed a bug where it wasn''t
  using the variable extra_drivers, for loading the specific IRX needed drivers. This
  is increasing compatibility with some specific PS2 models that sometimes fail when
  loading cores.</li>

  <li>PS3/PSL1GHT: Add improvements to the RSX driver (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1579097024" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14965" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14965/hovercard" href="https://github.com/libretro/RetroArch/pull/14965">#14965</a>)</li>

  <li>PS3/PSL1GHT: Add modern_alpha_blend and modern_opaque rsx shaders</li>

  <li>PS3/PSL1GHT: Add perf improvements to the rsx driver</li>

  <li>PS3/PSL1GHT: Add RSX video driver</li>

  <li>PS3/PSL1GHT/MENU/XMB: Do XMB menu scaling for psl1ght</li>

  <li>PS3/PSL1GHT: Update Makefile to use latest shaders and more UI menu options</li>

  <li>PS3/PSL1GHT: Default folders normalization</li>

  <li>PS3/PSL1GHT: Fix video rotation</li>

  <li>PS3/PSL1GHT: Fix HTTP download</li>

  <li>QB/CONFIGURE: Add new flags - HAVE_UPDATE_CORE_INFO, ASSETS_DIR, FILTERS_DIR</li>

  <li>RECORDING: Add recordings to video history playlist</li>

  <li>REWIND: Don''t take rewind steps while menu pause active</li>

  <li>RUNLOOP: Currently when core is paused, video output will be stopped completely
  too, making it impossible to animate widgets while paused, therefore:</li>

  <li>RUNLOOP: Added a new runloop state for pause which renders last cached frame</li>

  <li>RUNLOOP: Allowed rewinding while paused so that it acts like backwards frameadvance.
  Also moved rewind step taking before menu iteration so that steps won''t be lost
  while in menu when menu_pause is disabled</li>

  <li>RUNLOOP: State load and reset while paused will forget pause for x frames in
  order to show proper output</li>

  <li>RUNLOOP: Allowed reading pause hotkey while menu is active</li>

  <li>RUNLOOP: Allowed reading screenshot hotkey while menu is active</li>

  <li>RUNLOOP: Joined 2 fullscreen hotkey checks to one (Any ideas why they were separated
  for paused and non-paused states, since one works fine for both..?)</li>

  <li>RUNLOOP: Implement GET_HW_CONTEXT_NEGOTIATION_INTERFACE_SUPPORT. Fairly trivial.
  Just report the latest version.</li>

  <li>SAVESTATES: State slot hotkey adjustments -</li>

  <li>SAVESTATES: Allow selecting -1 Auto slot with hotkeys</li>

  <li>SAVESTATES: Allow wrap-around from -1 to 999 and backwards</li>

  <li>SAVESTATES: Show failure message when trying to load a state that does not exist
  instead of plain "Loading state"</li>

  <li>SAVESTATES: Shorten the duration of slot change notification</li>

  <li>SAVESTATES: Change the widget type to the same type as shader toggle for better
  back and forth action. Closes [Widgets] Save state slot switcher</li>

  <li>SHADERS: Append Preset feature</li>

  <li>SHADERS: Prepend Preset feature</li>

  <li>SHADERS: Shader Preset - Wildcard Replacement in Paths on Load. When a simple
  preset loads, text wildcards which are found in paths inside the presets will be
  replaced with values coming from the current RetroArch context. The replacement
  will be executed on both texture paths and reference paths.</li>

  <li>SHADERS/SLANG/SPIRVCROSS: Update to latest SPIRV-Cross, fixing Metal shader
  compilation issues along the way</li>

  <li>STATICALLY LINKED/SALAMANDER: Fix salamander config save on fork for static
  platforms</li>

  <li>TVOS/VULKAN/MOLTENVK: Vulkan on tvOS</li>

  <li>VIDEO: Allow manual video swap interval forcing. The addition of auto swap interval
  effectively prevented manual forcing, which is beneficial when the rate is not reported
  properly. Therefore use the interval in the calculation only when using automatic
  interval.</li>

  <li>VULKAN: Fix crash when using multiple physical devices and HW core (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1552174877" data-permission-text="Title
  is private" data-url="https://github.com/libretro/RetroArch/issues/14889" data-hovercard-type="pull_request"
  data-hovercard-url="/libretro/RetroArch/pull/14889/hovercard" href="https://github.com/libretro/RetroArch/pull/14889">#14889</a>)</li>

  <li>VULKAN: Detect if wrong PhysicalDevice is returned.</li>

  <li>VULKAN: Actually query physical device before creating core device.</li>

  <li>VULKAN: Define and implement v2 of context negotiation interface</li>

  <li>VULKAN: Add v2 of context negotiation interface.</li>

  <li>VULKAN: Add vkEnumerateInstanceVersion symbol.</li>

  <li>VULKAN: Implement v2 context negotiation</li>

  <li>VULKAN: Use compute shaders to upload RGB565</li>

  <li>VULKAN: Fix regression with RGB565 and OriginalHistory.</li>

  <li>VULKAN/WAYLAND: Don''t clamp the number of requested images. Due to an unfortunate
  "feature", MESA always reports 4 as the Vulkan surface''s minImageCount in Wayland.<br>

  However, values of 2 and 3 work perfectly well, even if they are out of spec, providing
  way better latencies when using the Vulkan backend on Wayland.<br>

  So this removes the artificial clamping that was being done to desired_swapchain_images,
  because it''s not really necessary and was causing very noticeable input lag on
  Wayland+Vulkan.</li>

  <li>VULKAN/MENU/RGUI: Fix RGUI on Vulkan on platforms that don''t have _pack16 VkFormats</li>

  <li>VULKAN/MACOS/OSX: avoid using _PACK16 pixel formats on platforms without them</li>

  <li>WAYLAND: On scaled desktops the wayland backend deciding to resize based on
  values multiplied by the scale factor twice. Resulting in continuous attempts to
  rebuild the swapchain when in fullscreen.</li>

  <li>WAYLAND: Wait for splash screen configuration. Before, configuration (resize)
  events for the initial wayland window could happen before or after set_video_mode
  which could result in a small or corrupted window. Now we make sure that the initial
  window has processed it''s resize events before window size is set by set_video_mode.</li>

  <li>WAYLAND: Changes the initial window to show a RetroArch logo copied from the
  icon of the X11 backend.</li>

  <li>WAYLAND: Build pointer-constraints and relative-pointer protocols.</li>

  <li>WAYLAND/GL: GL is sometimes not rescaling property (Super + Left).</li>

  <li>WIN32: Ignore window limiting with fixed position. The other resizing part already
  took this into account, but WM_GETMINMAXINFO did not.</li>

  <li>WIN32/INPUT: Add support for mouse button swap</li>

  <li>WIN32: Fix keyboard event characters. Added sending key chars to all input drivers
  (currently they only send scan codes), and also missing mods for raw.</li>

  <li>WIN32: Fix restart if path has spaces. CreateProcess does not like to have anything
  executable path related in the second parameter lpCommandLine if the path has spaces.
  Thus strip everything from args except the actual parameters.</li>

  </ul>'
updated: '2023-03-16T06:15:37Z'
version: v1.15.0
version_title: v1.15.0
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
