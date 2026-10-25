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
    size: 783572
    size_str: 765 KiB
    url: https://cdn.classicube.net/client/latest/ClassiCube-3ds.3dsx
  ClassiCube-3ds.cia:
    size: 632768
    size_str: 617 KiB
    url: https://cdn.classicube.net/client/latest/ClassiCube-3ds.cia
github: ClassiCube/ClassiCube
icon: https://raw.githubusercontent.com/ClassiCube/ClassiCube/master/misc/3ds/icon.png
image: https://raw.githubusercontent.com/ClassiCube/ClassiCube/master/misc/3ds/banner.png
image_length: 10600
layout: app
license: other
license_name: Other
llm_generation: unknown
qr:
  ClassiCube-3ds.cia: https://db.universal-team.net/assets/images/qr/classicube-3ds-cia.png
source: https://github.com/ClassiCube/ClassiCube
stars: 2083
systems:
- 3DS
title: ClassiCube
unique_ids:
- '0x5115D'
update_notes: '<p dir="auto">All:</p>

  <ul dir="auto">

  <li>Improved: Detection of slim-armed skins (Thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Goodlyay/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Goodlyay">@Goodlyay</a>)</li>

  <li>Improved: More ports are compiled at higher optimisation levels (e.g. Xbox/PSP/Vita/macOS/Linux/Windows/Android)</li>

  <li>Improved: Try to continue running when static VB allocation fails</li>

  <li>Improved: Split dynamic into dynamic and scratch VBs, saves a little bit of
  memory on some graphics backends</li>

  <li>Improved: Minorly optimise performance in SoftGPU graphics backend</li>

  <li>Improved: Launcher direct connect autofills mc:// from address field when user
  field is empty</li>

  <li>Fixed: Memory leak in launcher when extracting terrain.png for dirt/stone background
  (Thanks <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/CiroZDP/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/CiroZDP">@CiroZDP</a>)</li>

  <li>Fixed: Fallback font not drawing with very small chat font sizes</li>

  <li>Fixed: Classic map generator inaccuracies</li>

  <li>Fixed: Singleplayer liquid physics shouldn''t flow into sprite blocks (Matches
  original classic)</li>

  <li>Fixed: Invalid server hashes in launcher (e.g. a URL) just silently erroring</li>

  <li>Fixed: Rare crash if graphics context was lost in middle of connecting to a
  server</li>

  <li>Fixed: Rare case where http SSL downloader got stuck in an infinite loop (Thanks
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SpiralP/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SpiralP">@SpiralP</a>)</li>

  <li>Fixed: Default implementation of SSL_Write (Thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/fruhland/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fruhland">@fruhland</a>)</li>

  <li>Fixed: SoftMin backend not freeing window framebuffer memory (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/CiroZDP/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/CiroZDP">@CiroZDP</a>)</li>

  <li>Added: Export Commands_Unregister for plugins (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SpiralP/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SpiralP">@SpiralP</a>)</li>

  </ul>

  <p dir="auto">Desktop/Mobile:</p>

  <ul dir="auto">

  <li>Improved: With OpenGL backend, also log VRAM amount in /client gpuinfo if nvidia
  memory stats extension is available</li>

  <li>Fixed: FDs not being closed on exec on POSIX systems</li>

  </ul>

  <p dir="auto">Linux:</p>

  <ul dir="auto">

  <li>Added: Flatpak CI (thanks <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/sungsphinx/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/sungsphinx">@sungsphinx</a>)</li>

  <li>Fixed: X11 build still passing along keypresses (e.g. ctrl+space) mapped to
  U+0000 (thanks <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SpiralP/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SpiralP">@SpiralP</a>)</li>

  <li>Fixed: X11 build not appearing in xlsclients</li>

  <li>Improved: Better compatibility on 32 bit Linux with pre glibc 2.11 versions</li>

  </ul>

  <p dir="auto">macOS:</p>

  <ul dir="auto">

  <li>Improved: Make default 64 bit macos downloadable build universal</li>

  <li>Added: unfinished WIP metal renderer</li>

  </ul>

  <p dir="auto">Windows:</p>

  <ul dir="auto">

  <li>Improved: Minorly optimised Direct3D 11 backend</li>

  <li>Improved: ARM compiled builds now have an icon</li>

  <li>Improved: Builds compiled via makefile now have an icon</li>

  <li>Improved: Add Open Watcom v2 compiler support (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/TimofeyLednev/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TimofeyLednev">@TimofeyLednev</a>)</li>

  </ul>

  <p dir="auto">iOS:</p>

  <ul dir="auto">

  <li>Fixed: Only playing first few seconds of music</li>

  <li>Added: unfinished WIP metal renderer</li>

  </ul>

  <p dir="auto">OpenBSD:</p>

  <ul dir="auto">

  <li>Fixed: LibreSSL not working for fallback SSL certificate validation</li>

  </ul>

  <p dir="auto">Symbian:</p>

  <ul dir="auto">

  <li>Improved: Use native text input dialog for on-screen input (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/shinovon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/shinovon">@shinovon</a>)</li>

  <li>Improved: Auto update keybinds on layout change (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/shinovon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/shinovon">@shinovon</a>)</li>

  <li>Improved: Set default music volume to 0 (Thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/shinovon/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/shinovon">@shinovon</a>)</li>

  <li>Fixed: Multiple key press handling (Thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/shinovon/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/shinovon">@shinovon</a>)</li>

  <li>Fixed: Main loop not halting after Process_Abort called (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/shinovon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/shinovon">@shinovon</a>)</li>

  </ul>

  <p dir="auto">WinCE:</p>

  <ul dir="auto">

  <li>Improved: ARM build defaults to armv4t to support more devices (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/TimofeyLednev/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TimofeyLednev">@TimofeyLednev</a>)</li>

  <li>Improved: Window icon is partially displayed now</li>

  <li>Fixed: Couldn''t go in-game on some devices (Thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/TimofeyLednev/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/TimofeyLednev">@TimofeyLednev</a>)</li>

  </ul>

  <p dir="auto">GNU hurd:</p>

  <ul dir="auto">

  <li>Added: Basic support (Thanks <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/NexusSfan/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NexusSfan">@NexusSfan</a>)</li>

  </ul>

  <p dir="auto">Consoles:</p>

  <ul dir="auto">

  <li>Improved: Minorly optimise framebuffer drawing on a few platforms</li>

  <li>Improved: More platforms include Commit SHA in crash logs</li>

  </ul>

  <p dir="auto">PSP:</p>

  <ul dir="auto">

  <li>Added: Implemented fog</li>

  <li>Fixed: Mostly fixed clipping issues</li>

  <li>Improved: Follow circle/cross button preference</li>

  <li>Improved: Display network profile number on startup</li>

  <li>Improved: Auto fallover to next network profile if can''t connect after 10 seconds</li>

  <li>Improved: Increased deadzone range</li>

  </ul>

  <p dir="auto">Vita:</p>

  <ul dir="auto">

  <li>Added: Implemented fog</li>

  <li>Fixed: clouds now move</li>

  <li>Fixed: 3D anaglyph not working</li>

  <li>Improved: .vpk has app icon and app version</li>

  </ul>

  <p dir="auto">PS1:</p>

  <ul dir="auto">

  <li>Added: Mouse support</li>

  <li>Improved: Slightly improve stability</li>

  </ul>

  <p dir="auto">PS2:</p>

  <ul dir="auto">

  <li>Fixed: Splitscreen mode</li>

  <li>Fixed: Palette corruption when too many palettes were used</li>

  <li>Fixed: Texture corruption on hardware (hopefully)</li>

  <li>Improved: Slightly optimise clearing</li>

  </ul>

  <p dir="auto">PS3:</p>

  <ul dir="auto">

  <li>Added: Implemented fog</li>

  <li>Improved: Slightly increase max texture size</li>

  </ul>

  <p dir="auto">PS4:</p>

  <ul dir="auto">

  <li>Technically works with software rendering</li>

  </ul>

  <p dir="auto">XBOX:</p>

  <ul dir="auto">

  <li>Added: Implemented fog</li>

  <li>Improved: Slightly increase max texture size</li>

  </ul>

  <p dir="auto">N64:</p>

  <ul dir="auto">

  <li>Improved: Try to use palettised textures when possible</li>

  </ul>

  <p dir="auto">Wii U:</p>

  <ul dir="auto">

  <li>Improved: Slightly increase max texture size</li>

  </ul>

  <p dir="auto">Saturn:</p>

  <ul dir="auto">

  <li>Added: .bin build</li>

  <li>Fixed: Reading mouse/keyboard as controller input</li>

  </ul>

  <p dir="auto">Dreamcast:</p>

  <ul dir="auto">

  <li>Fixed: Key releases not being detected sometimes</li>

  <li>Fixed: Up/down/left/right keyboard input being wrongly treated as character
  input</li>

  <li>Fixed: Debug log conflicting with network adapter if it''s using serial port</li>

  <li>Fixed: Modem networking not working</li>

  <li>Improved: Slightly optimised by avoiding unnecessary clipping in most cases</li>

  </ul>

  <p dir="auto">Atari ST:</p>

  <ul dir="auto">

  <li>Improved: Saved ~0.6 seconds per frame</li>

  </ul>

  <p dir="auto">GBA/32x:</p>

  <ul dir="auto">

  <li>Improved: Somewhat optimised rendering</li>

  </ul>

  <p dir="auto">GBA:</p>

  <ul dir="auto">

  <li>Improved: Renderer performance slightly by using faster memory region (thanks
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Kuratius/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Kuratius">@Kuratius</a>)</li>

  </ul>'
updated: '2026-10-22T01:21:36Z'
version: 1.3.9
version_title: Release 1.3.9
website: https://classicube.net
wiki: https://github.com/ClassiCube/ClassiCube/wiki
---
**ClassiCube** is a custom Minecraft Classic compatible client written in C from scratch.
**It is not affiliated with (or supported by) Mojang AB, Minecraft, or Microsoft in any way.**
Known issues:
- Switching to another app and back may freeze the game
- Stereoscopic 3D may not work correctly