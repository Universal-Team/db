---
author: UnknownShadow200
avatar: https://avatars.githubusercontent.com/u/51250960?v=4
categories:
- game
color: '#c5c5c5'
color_bg: '#808080'
created: '2014-12-17T03:42:16Z'
description: Custom Minecraft Classic / ClassiCube client written in C  from scratch
  (formerly ClassicalSharp in C#)
download_page: https://www.classicube.net/download/3ds
downloads:
  ClassiCube-3ds.3dsx:
    size: 778956
    size_str: 760 KiB
    url: https://cdn.classicube.net/client/latest/ClassiCube-3ds.3dsx
  ClassiCube-3ds.cia:
    size: 630208
    size_str: 615 KiB
    url: https://cdn.classicube.net/client/latest/ClassiCube-3ds.cia
github: ClassiCube/ClassiCube
icon: https://raw.githubusercontent.com/ClassiCube/ClassiCube/master/misc/3ds/icon.png
image: https://raw.githubusercontent.com/ClassiCube/ClassiCube/master/misc/3ds/banner.png
image_length: 10600
layout: app
license: other
license_name: Other
qr:
  ClassiCube-3ds.cia: https://db.universal-team.net/assets/images/qr/classicube-3ds-cia.png
source: https://github.com/ClassiCube/ClassiCube
stars: 1905
systems:
- 3DS
title: ClassiCube
unique_ids:
- '0x5115D'
update_notes: '<p dir="auto">All:</p>

  <ul dir="auto">

  <li>Added: NotifyAction CPE (Thanks Venk)</li>

  <li>Added: ToggleBlockList CPE (Thanks Venk)</li>

  <li>Added: Fixed point software renderer graphics backend (Thanks oorange32)</li>

  <li>Added: Flat minimal software renderer graphics backend</li>

  <li>Added: Hidden option for auto pause on focus lost</li>

  <li>Improved: Use BearSSL for SSL support on all backends</li>

  <li>Improved: Fallback native SSL certificate checking on Windows/macOS/Unix/ios/Android</li>

  <li>Improved: Added PushStrength to EntityProperty (Thanks Venk)</li>

  <li>Improved: Prefer visible block in auto rotate group when opening inventory (Thanks
  Goodlyay)</li>

  <li>Improved: Cancel queued skin download if no more entities are using the skin</li>

  <li>Improved: Mark all chunks as needing to be redrawn rather than immediately deleting
  when world state changes (e.g. sunlight changes, block properties updated)</li>

  <li>Improved: Performance of SoftGPU backend slightly improved</li>

  <li>Improved: Glass should have metal step sound like classic</li>

  <li>Improved: Make primary UI button smaller on small displays</li>

  <li>Improved: Log IP when opening a connection to a webserver</li>

  <li>Improved: Allow overriding LINKER executable in makefile (Thanks Izder456)</li>

  <li>Improved: Don''t allow chat scrolling in pure classic mode</li>

  <li>Improved: Crash logging shows module relative addresses instead</li>

  <li>Improved: Allow using left/right for menu navigation in launcher</li>

  <li>Improved: Updates are now fetched over SSL</li>

  <li>Improved: Change crash message if possibly due to a third party plugin</li>

  <li>Improved: Defer audio/texpacks directory creation until actually needed</li>

  <li>Improved: Support very old systems without BGRA support in OpenGL 1 build</li>

  <li>Improved: Use flat button background colour based on current theme if gui texture
  missing</li>

  <li>Improved: Don''t render clouds/sky in software renderer backends</li>

  <li>Improved: Show better error messages for when required symbols aren''t found</li>

  <li>Improved: UI texture upload performance slightly on most systems</li>

  <li>Improved: Minorly increase performance on some GPUs in Modern OpenGL backend</li>

  <li>Fixed: OpenGL 1 build on big endian systems</li>

  <li>Fixed: .wavs accidentally being generated/read with wrong endian on big endian
  systems</li>

  <li>Fixed: Can''t download from URLs that have raw IPv6 address as the hostname</li>

  <li>Fixed: Occasional crashes when handling redirected web requests</li>

  <li>Fixed: Can''t overwrite existing map when saving without using mouse</li>

  <li>Fixed: Loading default texture pack twice if it isn''t default.zip</li>

  <li>Fixed: Non-ASCII characters not parsed properly in server names</li>

  <li>Fixed: 8 bit grayscale without alpha PNGs not being decoded correctly</li>

  <li>Fixed: Colour code bleeding in URLs, partially</li>

  <li>Fixed: Ampersands being UTF8 converted in HTTP URLs</li>

  <li>Fixed: Save level button should not be enabled in pure classic mode (thanks
  Beyond5D)</li>

  <li>Fixed: Non power of two skins not rendering properly with humanoid models</li>

  <li>Fixed: Make sapling physics more accurate (thanks Beyond5D)</li>

  <li>Fixed: Better handle out of memory when downloading HTTP data</li>

  <li>Fixed: Random corruption on low stack memory systems (e.g. NDS, Saturn, etc)</li>

  <li>Fixed: Mipmaps level not being properly calculated for modern OpenGL build</li>

  <li>Fixed: Classic options menu not using proper layout</li>

  <li>Fixed: When opening inventory with no block selected, arrow input scrolls hotbar
  instead</li>

  <li>Fixed: Server list not immediately redrawing after new flag downloaded (Thanks
  CornerPin)</li>

  <li>Fixed: CinematicGui CPE state not properly reset (Thanks eoniiii)</li>

  <li>Fixed: Accidentally copying too much data for textures on 16bpp systems</li>

  <li>Fixed: Try to fix rarely rendering as a translucent window on some systems</li>

  <li>Fixed: GFX resource leak if server sends LevelFinalise without level chunks
  first</li>

  <li>Fixed: HTTP URL redirects not remapping hosts (excluding webclient)</li>

  <li>Fixed: Triangles not always being properly clipped in software renderer</li>

  <li>Fixed: Crash if a plugin calls Chat_Add multiple times with very long input</li>

  <li>Fixed: Properly prevent loading multiplayer maps over 2 GB in size</li>

  <li>Fixed: OpenGL 1.0 fallback on 64 bit systems</li>

  </ul>

  <p dir="auto">Unix:</p>

  <ul dir="auto">

  <li>Added: hp-ux support (Thanks tenox7)</li>

  <li>Added: Option for disabling xinput2 support at runtime</li>

  <li>Improved: Launcher on X11 now uses pure 2D visual instead of GLX visual</li>

  <li>Improved: When using EGL, try to ensure chosen config has same visual ID as
  X11 window</li>

  </ul>

  <p dir="auto">Linux:</p>

  <ul dir="auto">

  <li>Added: Support for compiling on Elbrus (Thanks a1batross)</li>

  <li>Improved: Flatpak comes with ClassiCube texture pack and audio (Thanks sungsphinx)</li>

  <li>Improved: Upgrade flatpak runtime (Thanks sungsphinx)</li>

  <li>Fixed: Always link lm in makefile to avoid ''undefined sqrtf` on some CPU architectures</li>

  </ul>

  <p dir="auto">Windows:</p>

  <ul dir="auto">

  <li>Improved: More specific crash messages for null pointer reads/writes</li>

  <li>Improved: Support versions of Direct3D 9 earlier than Direct3D 9.0c</li>

  <li>Improved: Compatibility with NT 3.5</li>

  <li>Improved: Better win32s compatibility</li>

  <li>Improved: Avoid linking to opengl32.dll directly in OpenGL build</li>

  <li>Fixed: Use proper backtrace on ARM/ARM64 platforms</li>

  <li>Fixed: OpenGL build not working with builtin 1.1 software renderer</li>

  <li>Fixed: Cinematic GUI with Direct3D 9</li>

  <li>Fixed: TinyC compilation</li>

  </ul>

  <p dir="auto">macOS:</p>

  <ul dir="auto">

  <li>Improved: 32 bit website download is a universal Intel/PowerPC build</li>

  <li>Improved: 64 bit website download is a universal Intel/ARM build</li>

  <li>Improved: Enable Game Mode support in info.plist</li>

  </ul>

  <p dir="auto">iOS:</p>

  <ul dir="auto">

  <li>Improved: Enable file sharing in Files app (Thanks Pear)</li>

  <li>Improved: Better support 32 bit only devices</li>

  <li>Improved: Enable Game Mode support in info.plist</li>

  <li>Improved: Use pre iOS 8 available way of detecting device rotation</li>

  <li>Fixed: Missing app icons</li>

  </ul>

  <p dir="auto">Android:</p>

  <ul dir="auto">

  <li>Improved: WIP on pre 2.3 support</li>

  <li>Fixed: Wrong username/password not being handled properly</li>

  <li>Fixed: Crashing on certain CPUs, such as Tegra 2</li>

  <li>Fixed: Crashing on some old ARM CPUs</li>

  </ul>

  <p dir="auto">OpenBSD:</p>

  <ul dir="auto">

  <li>Fixed: libexecinfo not being used</li>

  </ul>

  <p dir="auto">NetBSD:</p>

  <ul dir="auto">

  <li>Fixed: Not building on sparc64 (Thanks alarixnia)</li>

  </ul>

  <p dir="auto">IRIX:</p>

  <ul dir="auto">

  <li>Fixed: Not compiling</li>

  </ul>

  <p dir="auto">Solaris:</p>

  <ul dir="auto">

  <li>Fixed: Not compiling</li>

  </ul>

  <p dir="auto">Symbian:</p>

  <ul dir="auto">

  <li>Added: Mostly complete port (Big thanks to shinovon)</li>

  </ul>

  <p dir="auto">SDL:</p>

  <ul dir="auto">

  <li>Fixed: Only 1 filter type showing on save dialog in SDL3 (Thanks sungsphinx)</li>

  <li>Fixed: Can''t exit fullscreen in SDL2</li>

  <li>Fixed: OpenGL attributes not being properly set (thanks DrinkyBird)</li>

  </ul>

  <hr>

  <p dir="auto">Consoles:</p>

  <ul dir="auto">

  <li>Improved: On most systems, L defaults to Place block and R to Delete block</li>

  <li>Improved: On console builds just always ignore expired SSL certificates</li>

  <li>Improved: Display full path when file opening/creation fails</li>

  <li>Improved: Add option for changing content offset x/y</li>

  <li>Improved: More descriptive error when no FAT filesystem found on some systems</li>

  <li>Improved: More descriptive error for non writable filesystem</li>

  <li>Fixed: Pointer/Touch inputs not being properly intercepted by onscreen keyboard</li>

  <li>Fixed: Touching on-screen keyboard button repeatedly typing same character</li>

  <li>Fixed: Special text (e.g Bottom right) not rendering properly on some systems</li>

  <li>Fixed: Pressing enter on virtual keyboard resulting in lockup</li>

  <li>Fixed: Cinematic bars not rendering properly</li>

  </ul>

  <p dir="auto">PS4:</p>

  <ul dir="auto">

  <li>Added: Completely unfinished and non-working port</li>

  </ul>

  <p dir="auto">PS2:</p>

  <ul dir="auto">

  <li>Improved: Performance increased</li>

  <li>Improved: Reduce VRAM usage with paletted textures and 16 bit depth buffer</li>

  <li>Fixed: Textures overlapping frame buffer</li>

  <li>Fixed: Onscreen keyboard not appearing</li>

  </ul>

  <p dir="auto">PS3:</p>

  <ul dir="auto">

  <li>Improved: Minorly improve performance (e.g. swizzled textures)</li>

  <li>Improved: Increase controller sensitivity</li>

  <li>Improved: Auto detect whether to use circle or cross as primary button</li>

  </ul>

  <p dir="auto">PS1:</p>

  <ul dir="auto">

  <li>Improved: Triangle+DPad controls camera</li>

  <li>Improved: Reduce world block clipping (Thanks wav3)</li>

  <li>Improved: Performance increased (Thanks wav3)</li>

  <li>Improved: Reduce VRAM usage with paletted textures</li>

  <li>Improved: Water/Ice is now rendered translucent</li>

  <li>Fixed: Some objects (e.g. Water/Bedrock outside map) not rendering</li>

  <li>Fixed: Not handling running out of RAM for vertices</li>

  <li>Fixed: On screen keyboard now displays</li>

  </ul>

  <p dir="auto">PS Vita:</p>

  <ul dir="auto">

  <li>Improved: Minorly improve performance (e.g. swizzled textures)</li>

  <li>Improved: Auto detect whether to use circle or cross as primary button</li>

  <li>Improved: Change DPAD to instead be for flying up/down and cycling hotbar slot</li>

  <li>Improved: Remove back screen touch behaviour</li>

  </ul>

  <p dir="auto">PSP:</p>

  <ul dir="auto">

  <li>Improved: On-screen dialog displays wifi connection progress/status</li>

  <li>Improved: Minorly improve performance (e.g. swizzled textures)</li>

  <li>Improved: Try to allocate textures in VRAM when possible</li>

  <li>Improved: Reduce VRAM usage with paletted textures and 16 bit depth buffer</li>

  <li>Improved: Start working on clipping support, not finished though</li>

  <li>Fixed: Block outline and sky not drawing at all</li>

  <li>Fixed: Usually failing to connect to wifi on startup</li>

  <li>Fixed: Launcher not rendering after returning from in-game</li>

  </ul>

  <p dir="auto">Wii U:</p>

  <ul dir="auto">

  <li>Improved: Change ZL/L/ZR/R default vpad bindings</li>

  <li>Improved: Increase vpad sensitivity</li>

  <li>Fixed: Mostly renders on real hardware</li>

  <li>Fixed: Loading audio sound looping forever</li>

  <li>Fixed: Clouds not moving</li>

  <li>Fixed: Tried to fix Exit not working properly</li>

  </ul>

  <p dir="auto">Wii/GameCube:</p>

  <ul dir="auto">

  <li>Improved: For gamecube controller, map B+Dpad L/R to hotbar L/R</li>

  <li>Improved: For gamecube controller, map dpad to just be fly up/down and hotbar
  left/right</li>

  <li>Improved: Power/Reset buttons properly supported (thanks Extrems)</li>

  <li>Fixed: Lockup after quitting in-game (thanks Extrems)</li>

  <li>Fixed: GameCube controller hotplugging (thanks Extrems)</li>

  <li>Fixed: Switching from splitscreen to singleplayer mode leaving viewport messed
  up</li>

  <li>Fixed: Screenshots rarely having corrupted data (thanks Extrems)</li>

  </ul>

  <p dir="auto">GameCube:</p>

  <ul dir="auto">

  <li>Improved: Use libogc2 instead, e.g. allowing SD card support (big thanks to
  Extrems)</li>

  <li>Improved: Sign in, resources, and some texture pack downloads work</li>

  <li>Improved: Allow using additional ARAM in systems with it as temp filesystem
  (Thanks Extrems)</li>

  <li>Improved: Show network details on startup</li>

  </ul>

  <p dir="auto">N64:</p>

  <ul dir="auto">

  <li>Added: Filesystem support for flashcarts (Thanks Phil564)</li>

  <li>Improved: Moderately optimise performance</li>

  <li>Improved: Texture precision slightly</li>

  </ul>

  <p dir="auto">3DS:</p>

  <ul dir="auto">

  <li>Improved: Don''t use low memory mode (enables block IDs over 255)</li>

  <li>Improved: Try to allocate textures in VRAM when possible</li>

  <li>Improved: Request OS to make more RAM available to ClassiCube (Thanks man-of-eel)</li>

  <li>Improved: Minorly increase performance</li>

  <li>Fixed: Can''t click on on-screen keyboard in the launcher</li>

  <li>Fixed: On-screen keyboard not showing when 3D anaglyph is enabled</li>

  <li>Fixed: UI being affected by fog</li>

  </ul>

  <p dir="auto">NDS:</p>

  <ul dir="auto">

  <li>Added: Separate non networking build</li>

  <li>Added: Fog (thanks rmn20, currently disabled as it interferes with UI)</li>

  <li>Improved: Unified build that supports both NDS and DSi wifi hardware (thanks
  BlocksDS)</li>

  <li>Improved: Use paletted textures</li>

  <li>Improved: Slightly increase performance (thanks rmn20)</li>

  <li>Improved: Appearance of water outside the map</li>

  <li>Improved: Texture precision slightly</li>

  <li>Improved: Water is now partially translucent</li>

  <li>Improved: Unhandled exception shows crash screen</li>

  <li>Improved: Colour wifi success/failure messages</li>

  <li>Fixed: Crashing when downloading resources fails</li>

  <li>Fixed: Keyboard not working the first time</li>

  <li>Fixed: Clouds not moving</li>

  <li>Fixed: Properly set/restore VRAM banks (thanks AntonioND)</li>

  </ul>

  <p dir="auto">Dreamcast:</p>

  <ul dir="auto">

  <li>Improved: Performance increased</li>

  <li>Improved: B+L/R now switch hotbar slot</li>

  <li>Improved: Exiting from launcher now ''Returns to menu''</li>

  <li>Improved: Reduce VRAM usage with paletted textures</li>

  <li>Improved: Don''t force 50hz in Europe region</li>

  <li>Improved: RAM reduce minorly reduced</li>

  <li>Improved: Unhandled exception shows crash screen</li>

  <li>Fixed: Crashing when playing music</li>

  </ul>

  <p dir="auto">Saturn:</p>

  <ul dir="auto">

  <li>Improved: Improve performance</li>

  <li>Improved: Graphics are mostly rendered in proper order</li>

  <li>Fixed: Frustum culling not working</li>

  <li>Fixed: Water/Bedrock outside map not rendering</li>

  <li>Fixed: Leaking VRAM overtime</li>

  <li>Fixed: Can''t see menus</li>

  </ul>

  <p dir="auto">UWP:</p>

  <ul dir="auto">

  <li>Added: Majorly unfinished port</li>

  </ul>

  <p dir="auto">XBOX 360:</p>

  <ul dir="auto">

  <li>Fixed: Launcher at least works, in-game doesn''t work though</li>

  </ul>

  <p dir="auto">XBOX:</p>

  <ul dir="auto">

  <li>Improved: On-screen dialog displays network connection progress/status</li>

  <li>Improved: Slightly increase default content x/y offset</li>

  <li>Improved: Clouds now move</li>

  <li>Fixed: Texture warping</li>

  <li>Fixed: Can''t go back to launcher menu</li>

  <li>Fixed: Sprites always being drawn solidly</li>

  <li>Fixed: Switching from splitscreen to singleplayer mode leaving viewport messed
  up</li>

  <li>Fixed: Log output on Xemu</li>

  </ul>

  <p dir="auto">32x/GBA:</p>

  <ul dir="auto">

  <li>Improved: Majorly optimise performance, still runs as a slideshow</li>

  <li>Improved: Completely skip launcher and go directly in-game</li>

  <li>Improved: Technically usable controls</li>

  <li>Improved: Render world without edge/horizon</li>

  <li>Fixed: Timing measurement now partially works</li>

  </ul>

  <hr>

  <p dir="auto">Atari ST:</p>

  <ul dir="auto">

  <li>Added: Barely working port</li>

  </ul>

  <p dir="auto">Amiga:</p>

  <ul dir="auto">

  <li>Added: Non-working unfinished port</li>

  </ul>

  <p dir="auto">DOS:</p>

  <ul dir="auto">

  <li>Added: Unfinished and slow port</li>

  </ul>

  <p dir="auto">Mac OS Classic:</p>

  <ul dir="auto">

  <li>Added: 68040 optimised build</li>

  <li>Improved: Use flat minimal software renderer for 68k build</li>

  <li>Fixed: 68k build now ''runs'' on 4 MB system</li>

  </ul>

  <p dir="auto">WinCE:</p>

  <ul dir="auto">

  <li>Added: Mostly working port (Thanks oorange32 and picat)</li>

  </ul>

  <p dir="auto">OS/2:</p>

  <ul dir="auto">

  <li>Fixed: Not compiling and crashing at runtime (Thanks josch1710)</li>

  </ul>'
updated: '2026-02-17T12:28:45Z'
version: 1.3.8
version_title: Release 1.3.8
website: https://classicube.net
wiki: https://github.com/ClassiCube/ClassiCube/wiki
---
**ClassiCube** is a custom Minecraft Classic compatible client written in C from scratch.
**It is not affiliated with (or supported by) Mojang AB, Minecraft, or Microsoft in any way.**
Known issues:
- Switching to another app and back may freeze the game
- Stereoscopic 3D may not work correctly