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
    size: 605336
    size_str: 591 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v1.0.0/red-viper.3dsx
  red-viper.cia:
    size: 652224
    size_str: 636 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v1.0.0/red-viper.cia
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
stars: 854
systems:
- 3DS
title: red-viper
unique_ids:
- '0xFE7CB'
update_notes: '<p dir="auto">30 years ago today, the Virtual Boy released in Japan.
  What better time to release a big Red Viper update?</p>

  <ul dir="auto">

  <li>New "Multicolor" mode, allowing for more versatile color remapping</li>

  <li>Circle Pad Pro support</li>

  <li>Software renderer to reduce visual glitches, enabled in Golf</li>

  <li>Double buffering to hide garbage frames and improve frametime accuracy, enabled
  in Red Alarm and Bound High</li>

  <li>Numerous performance improvements</li>

  <li>In particular, interrupt checking was moved from a polling-based system to predicting
  exactly when the next interrupt will trigger, improving performance particularly
  in the Space Invaders intro</li>

  <li>A ROM can be bundled with a Red Viper CIA, to create what is commonly called
  a "forwarder"</li>

  <li>An error code is now shown when loading a ROM fails</li>

  <li>Fix "Discard" not correctly restoring settings for New 3DS Speedup</li>

  <li>Fix occasional graphical glitches on touch screen when toggling Home Menu</li>

  </ul>

  <p dir="auto">When I originally released Red Viper, I chose to release it as v0.9.0,
  to indicate that while there were still some compatibility issues, it was most of
  the way there. I decided that I would bump the version to v1.0.0 once all officially
  released games fully ran at playable speeds, with no major glitches or slowdown.
  The optimizations introduced in this update bring the Space Invaders intro up to
  full speed and fixes rendering bugs and audio stutters in Golf. These were the last
  big things (and I didn''t like how close it was getting to being v0.9.10), so I''m
  happy calling this v1.0.0.<br>

  This new version number does not mean that I am done updating this emulator - some
  homebrew is not yet fully compatible, and there are additional features I would
  still like to implement. Stay tuned 😉</p>'
updated: '2025-07-21T16:59:29Z'
version: v1.0.0
version_title: v1.0.0
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