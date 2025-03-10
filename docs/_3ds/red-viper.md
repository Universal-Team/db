---
author: Floogle
avatar: https://avatars.githubusercontent.com/u/18466542?v=4
categories:
- emulator
color: '#d3d2d2'
color_bg: '#807f7f'
created: '2023-06-18T19:13:04Z'
description: A Virtual Boy emulator for the 3DS
download_page: https://github.com/skyfloogle/red-viper/releases
downloads:
  red-viper.3dsx:
    size: 554736
    size_str: 541 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.8/red-viper.3dsx
  red-viper.cia:
    size: 604608
    size_str: 590 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.8/red-viper.cia
github: skyfloogle/red-viper
icon: https://raw.githubusercontent.com/skyfloogle/red-viper/master/icon.png
image: https://raw.githubusercontent.com/skyfloogle/red-viper/master/resources/banner.png
image_length: 6527
layout: app
qr:
  red-viper.cia: https://db.universal-team.net/assets/images/qr/red-viper-cia.png
screenshots:
- description: Jack bros
  url: https://db.universal-team.net/assets/images/screenshots/red-viper/jack-bros.png
- description: Mario tenis
  url: https://db.universal-team.net/assets/images/screenshots/red-viper/mario-tenis.png
- description: Red alarm
  url: https://db.universal-team.net/assets/images/screenshots/red-viper/red-alarm.png
- description: Warioland
  url: https://db.universal-team.net/assets/images/screenshots/red-viper/warioland.png
source: https://github.com/skyfloogle/red-viper
stars: 819
systems:
- 3DS
title: red-viper
unique_ids:
- '0xFE7CB'
update_notes: '<p dir="auto">This patch includes a number of accuracy improvements,
  primarily related to timing (plus a few game-specific hacks where hardware research
  is insufficient). With these improvements in tow, Red Viper is currently the most
  accurate emulator for Virtual Boy games on any system, even disregarding the whole
  3D thing.</p>

  <ul dir="auto">

  <li>Improved timer emulation to fix sample playback in Galactic Pinball and Teleroboxer</li>

  <li>Added memory access time emulation, which fixes numerous games

  <ul dir="auto">

  <li>Fixes sample playback in Virtual Bowling and Niko-Chan Battle, along with improved
  timer emulation</li>

  <li>Improves emulation performance in 3D Tetris</li>

  <li>Correctly emulated game speed in Golf</li>

  <li>Fixes Blox 2 intro cutting off early</li>

  </ul>

  </li>

  <li>Fixed graphical glitches and fixed intro chime in Waterworld</li>

  <li>Improved audio emulation to fix some homebrew, including the Blox games and
  the Formula V demo</li>

  <li>Allow loading savestates from older versions</li>

  </ul>'
updated: '2025-03-09T20:11:42Z'
version: v0.9.8
version_title: v0.9.8
wiki: https://github.com/skyfloogle/red-viper/wiki
---
A Virtual Boy emulator for the 3DS. All official games are playable at full speed.
* All officially licensed games are playable at full speed, even on the original 3DS
* 3D support
* Game saves are supported
* Map either the A/B buttons or the right D-Pad to the face buttons, with the other being on the touch screen
* New 3DS C-Stick is also supported
* Configurable face button mapping
* Configurable color filter