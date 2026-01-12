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
    size: 778728
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
stars: 1856
systems:
- 3DS
title: ClassiCube
unique_ids:
- '0x5115D'
update_notes: '<p dir="auto">All:</p>

  <ul dir="auto">

  <li>Added: New fancy lighting mode (Thanks Goodly)</li>

  <li>Added: Modifying selected block outline appearance (Thanks Venk)</li>

  <li>Added: replace command to singleplayer</li>

  <li>Added: option for adjusting scale of scrollbar in inventory</li>

  <li>Added: "scale with window" chat option (Thanks Goodly)</li>

  <li>Added: Anaglyph 3D option</li>

  <li>Added: Fallback terrain textures when no texture pack can be loaded</li>

  <li>Added: Option to modify the crosshair scale on gui options (Thanks Buwwet)</li>

  <li>Added: /place singleplayer command (Thanks yomcube)</li>

  <li>Added: Horizontal scroll wheel support</li>

  <li>Added: /skin singleplayer command</li>

  <li>Added: --singleplayer and --resume support to ClassiCube command line</li>

  <li>Added: CinematicGUI extension (Thanks Venk)</li>

  <li>Improved: Avoid relying on C math library (Thanks calebabutler)</li>

  <li>Improved: Better support HD terrain.png textures on low end GPUs</li>

  <li>Improved: Better handle running out of VRAM</li>

  <li>Improved: BlockEdit command allows modifying more properties</li>

  <li>Improved: Exiting reduced performance message now shown in top left for around
  a second instead of in chat</li>

  <li>Improved: Use fallback font if can''t load any system fonts</li>

  <li>Improved: Scroll wheel up/down is now bindable for key input</li>

  <li>Improved: Support multiple bindings to same button</li>

  <li>Improved: Better support multiple connected controllers for input</li>

  <li>Improved: Change saplings to not instantly grow when placed in singleplayer</li>

  <li>Improved: Scale of small and big announcements (Thanks Goodly)</li>

  <li>Improved: Load sounds from a .zip file instead</li>

  <li>Improved: Support displaying &lt; 1 FPS in HUD</li>

  <li>Improved: Show better error message when not enough memory to load a level</li>

  <li>Improved: Give a description for WoM style hacks in the hacks settings menu
  (Thanks Goodly)</li>

  <li>Improved: Make 0.0.23 texture pack more accurate</li>

  <li>Fixed: Make entities lit in fully bright blocks with Adv lighting (Thanks Goodly)</li>

  <li>Fixed: Custom blocks with no fog in .cw files mistakenly still being loaded
  with fog density</li>

  <li>Fixed: skinnedcube or custom models having white/black pixels in ''hat'' skin
  area mistakenly cleared</li>

  <li>Fixed: Keyboard camera movement having a large jump in rotation if a camera
  movement key is held down when exiting a menu that held input lock</li>

  <li>Fixed: ''overwrite existing'' not working in Save menu</li>

  <li>Fixed: Mouse getting centred when clicking on classic controls menu</li>

  </ul>

  <p dir="auto">Classic mode accuracy:</p>

  <ul dir="auto">

  <li>Improved: Default map gen size matches original Classic</li>

  <li>Fixed: Some options shouldn''t apply in Classic mode</li>

  <li>Fixed: TNT shouldn''t blow up in Classic mode</li>

  <li>Fixed: Change FPS mode in classic mode options to behave more accurately</li>

  <li>Fixed: Place dirt under generated trees (Thanks Beyond5D)</li>

  <li>Fixed: Don''t save camera''s pitch axis when making a checkpoint (Thanks Beyond5D)</li>

  </ul>

  <p dir="auto">Windows:</p>

  <ul dir="auto">

  <li>Improved: Switch to own HTTP backend rather than relying on underlying implementation
  of IE</li>

  <li>Improved: Show better message for plugin load failures</li>

  <li>Improved: Also try to dump stack contents in crash log</li>

  <li>Improved: Support more multimedia key buttons</li>

  <li>Improved: Now can run on NT 3.51 out of the box</li>

  <li>Improved: Better compatibility with older Windows SDKs</li>

  <li>Fixed: Crash after resizing window in Direct3D 11 backend</li>

  <li>Fixed: Can''t run when ImageHlp DLL is missing</li>

  <li>Fixed: File existence check not working properly on Windows 9X</li>

  <li>Added: Support for resolving domains to IPv6 addresses on Windows</li>

  </ul>

  <p dir="auto">macOS:</p>

  <ul dir="auto">

  <li>Improved: Better support compiling for macOS 10.3</li>

  <li>Improved: Support 4 extra mouse buttons</li>

  <li>Improved: Support more multimedia key buttons</li>

  <li>Improved: Always enable ModernGL builds in Updates menu</li>

  <li>Improved: Build app bundle with makefile</li>

  <li>Fixed: Camera majorly warping after returning to the game from an in-game menu</li>

  <li>Fixed: Launcher and icon colours being swapped when compiled with recent SDK
  versions</li>

  </ul>

  <p dir="auto">Linux:</p>

  <ul dir="auto">

  <li>Added: SDL3 backend</li>

  <li>Improved: Flatpak support (Thanks sungsphinx)</li>

  <li>Improved: Support 4 extra mouse buttons</li>

  <li>Improved: Support more multimedia key buttons</li>

  <li>Improved: Always enable ModernGL builds in Updates menu</li>

  <li>Improved: Try to better support non glibc systems</li>

  <li>Fixed: Crashing on system without input context support</li>

  </ul>

  <p dir="auto">Webclient:</p>

  <ul dir="auto">

  <li>Added: Support controller input</li>

  <li>Improved: Support more multimedia key buttons</li>

  </ul>

  <p dir="auto">Android:</p>

  <ul dir="auto">

  <li>Added: Support controller input</li>

  </ul>

  <p dir="auto">iOS:</p>

  <ul dir="auto">

  <li>Improved: Compatibility with iOS 5.0 and 6.0</li>

  </ul>

  <p dir="auto">Other:</p>

  <ul dir="auto">

  <li>Added: Grayscale post processor for Modern OpenGL builds (Webclient/mobile/ModernGL
  desktop)</li>

  <li>Added: Support IPV6 addresses for host component of a URL on most platforms</li>

  <li>Improved: Responsivness when generating maps on platforms without preemptive
  multithreading</li>

  <li>Added: Github actions workflows for more desktop platforms</li>

  <li>Fixed: Mouse input issues in haiku OS</li>

  <li>Fixed: Crash when exiting in haiku OS</li>

  <li>Improved: Makefile tracks dependencies and stores .o in per-platform build folders</li>

  <li>Improved: Simplify writing plugins in C++ slightly</li>

  <li>Added: Initial OS/2 support (Thanks josch1710)</li>

  <li>Added: Terminal/CLI window backend</li>

  <li>Added: Classic Mac OS port (Thanks EGAMatsu)</li>

  <li>Fixed: IRIX build crashing when displaying window</li>

  </ul>

  <p dir="auto">Consoles:</p>

  <ul dir="auto">

  <li>Added: Switch port (Thanks headshot2017)</li>

  <li>Added: Broken Sega 32x port</li>

  <li>Added: Broken Xbox 360 port</li>

  <li>Added: Incomplete PS1 port</li>

  <li>Added: Incomplete PS2 port</li>

  <li>Added: Incomplete PS3 port</li>

  <li>Added: Incomplete N64 port</li>

  <li>Added: Incomplete NDS port</li>

  <li>Added: Incomplete Saturn port</li>

  <li>Added: Broken Wii U port</li>

  <li>Added: Audio support to GC/Wii port (Thanks headshot2017)</li>

  <li>Added: Audio support to 3DS port (Thanks camthehaxman)</li>

  <li>Added: Unfinished splitscreen mode</li>

  <li>Fixed: Dreamcast build issues with latest GCC (Thanks gyrovorbis)</li>

  <li>Improved: Support dual analog controllers in Dreamcast port (thanks gyrovorbis)</li>

  <li>Improved: 3DS uses bottom screen for UI (Thanks camthehaxman)</li>

  <li>Improved: State of all console ports in general</li>

  <li>Improved: Switch to using BearSSL for SSL support</li>

  <li>Improved: Password is now remembered</li>

  <li>Improved: Use common system font implementation</li>

  <li>Improved: Partially offset FPS/position text to avoid overscan</li>

  <li>Improved: Add support for two button input binds</li>

  <li>Improved: Allow using A button as ''action'' button in menus in-game too</li>

  <li>Improved: Make Quit Game more stable</li>

  <li>Improved: Don''t auto show virtual keyboard when an input field is selected,
  only show it after A/Start is pressed</li>

  <li>Fixed: Input for save level and menu input screens</li>

  </ul>'
updated: '2024-09-21T00:43:34Z'
version: 1.3.7
version_title: Release 1.3.7
website: https://classicube.net
wiki: https://github.com/ClassiCube/ClassiCube/wiki
---
**ClassiCube** is a custom Minecraft Classic compatible client written in C from scratch.
**It is not affiliated with (or supported by) Mojang AB, Minecraft, or Microsoft in any way.**
Known issues:
- Switching to another app and back may freeze the game
- Stereoscopic 3D may not work correctly