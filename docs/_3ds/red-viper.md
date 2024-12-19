---
author: Floogle
avatar: https://private-avatars.githubusercontent.com/u/18466542?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MzQ2NDcxNjAsIm5iZiI6MTczNDY0NTk2MCwicGF0aCI6Ii91LzE4NDY2NTQyIn0.oGY2RVBYhJt68IxRPdEymL6Cw7Kl4KDYPwdcutZh9Ws&v=4
categories:
- emulator
color: '#d3d2d2'
color_bg: '#807f7f'
created: '2023-06-18T19:13:04Z'
description: A Virtual Boy emulator for the 3DS
download_page: https://github.com/skyfloogle/red-viper/releases
downloads:
  red-viper.3dsx:
    size: 544064
    size_str: 531 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.7/red-viper.3dsx
  red-viper.cia:
    size: 599488
    size_str: 585 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.7/red-viper.cia
github: skyfloogle/red-viper
icon: https://raw.githubusercontent.com/skyfloogle/red-viper/master/icon.png
image: https://raw.githubusercontent.com/skyfloogle/red-viper/master/resources/banner.png
image_length: 2798
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
stars: 809
systems:
- 3DS
title: red-viper
unique_ids:
- '0xFE7CB'
update_notes: '<p dir="auto">This patch introduces anaglyph mode, render time emulation,
  and numerous bugfixes.<br>

  Render time emulation means that some in-game sequences run at the same speed they
  did on a real Virtual Boy, which no previous emulator has emulated accurately. This
  includes the Jack Bros. level transitions being as choppy as they originally were,
  so a toggle has been added to revert to the old behaviour. For more information,
  check out <a href="https://skyfloogle.github.io/vip-timing" rel="nofollow">my write-up</a>.</p>

  <ul dir="auto">

  <li>Added anaglyph mode, with configurable colours for each eye

  <ul dir="auto">

  <li>2DS users can configure a depth offset in anaglyph mode, as they have no depth
  slider</li>

  </ul>

  </li>

  <li>Add render time emulation, including a toggle to turn it off</li>

  <li>Fix audio bug in Colony intro in Galactic Pinball</li>

  <li>Fix various issues in the Game Boy emulator</li>

  <li>Fix Red Alarm wireframe graphics drawing on top of UI</li>

  <li>Add a hack for Jack Bros. to make the intro chime play at roughly the correct
  speed</li>

  <li>Apply game fixes based on game ID rather than checksum, for better compatibility
  with ROM hacks</li>

  <li>Increased frameskip aggressiveness to improve performance in Elevated Speed</li>

  <li>Update software framebuffer more conservatively to improve performance in Waterworld
  and 3-D Tetris</li>

  <li>Adjusted gamma correction for improved visibility</li>

  <li>Fix D-Pad ABXY mirroring having an incorrect right input</li>

  </ul>'
updated: '2024-12-17T21:08:00Z'
version: v0.9.7
version_title: v0.9.7
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