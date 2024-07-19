---
author: Adrian Siekierka
avatar: https://avatars.githubusercontent.com/u/113514?v=4
categories:
- emulator
color: '#6de0c1'
color_bg: '#3e806e'
created: '2021-05-18T19:23:58Z'
description: NDS/3DS fork/port of the uxn/Varvara virtual machine
download_page: https://github.com/asiekierka/uxnds/releases
downloads:
  uxnds051.zip:
    size: 506700
    size_str: 494 KiB
    url: https://github.com/asiekierka/uxnds/releases/download/v0.5.1/uxnds051.zip
github: asiekierka/uxnds
icon: https://raw.githubusercontent.com/asiekierka/uxnds/main/misc/uxn48.png
image: https://raw.githubusercontent.com/asiekierka/uxnds/main/misc/uxn48.png
image_length: 224
layout: app
license: mit
license_name: MIT License
source: https://github.com/asiekierka/uxnds
systems:
- 3DS
- DS
title: uxnds
update_notes: '<ul dir="auto">

  <li>[3DS] Fix crash on start.</li>

  </ul>'
updated: '2024-07-08T16:39:41Z'
version: v0.5.1
version_title: uxnds 0.5.1
website: https://100r.co/site/uxn.html
wiki: https://wiki.xxiivv.com/site/uxn.html
---
Unxds is a port of the [Unx virtual machine](https://wiki.xxiivv.com/site/uxn.html) to the 3DS. Uxn is a portable 8-bit virtual computer inspired by [forth-machines](https://en.wikipedia.org/wiki/Forth_(programming_language)), capable of running simple tools and games programmable in its own [assembly language](https://wiki.xxiivv.com/site/uxntal.html).

This emulator allows you run to your uxn projects on the 3DS, it can also be used for developers who want to learn how to program little 8-bit things.

It was designed with an implementation-first mindset with a focus on creating portable graphical applications, the distribution of Uxn projects is akin to sharing game roms for any classic console emulator.

### Usage
By default, uxnds will run /uxn/boot.rom or /uxn/launcher.rom. It also supports reading files from within /uxn.

On start, a keyboard is presented on the bottom screen, and the uxn display - on the top screen. Use the L or R buttons to swap them - in this configuration, mouse input is approximated via touchscreen.

You can use the system button in the lower-left corner to reset the uxn virtual machine.

### Installation
Two ports are provided: the 3DS port (compatible with 3DS consoles) and the NDS port (compatible with DS, DSi and 3DS consoles).

#### 3DS port
There is one binary provided: uxnds.3dsx.

#### NDS port
When using a real DS, DSi or 3DS console, it is recommended to launch this program via [nds-hb-menu](https://github.com/devkitPro/nds-hb-menu) - though, as it currently doesn't use argc/argv, it doesn't really change much.

There are three binaries provided:
- uxnds.nds - faster, but best used only with known-good software,
- uxnds_debug.nds - slower, but provides debugging information, profiling information and performs CPU stack bounds checks.
- uxnds_profile.nds - almost as fast as uxnds.nds - with debugging/profiling information, no CPU stack bounds checks.
