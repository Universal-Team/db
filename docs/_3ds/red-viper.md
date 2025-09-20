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
    size: 623972
    size_str: 609 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v1.1.0/red-viper.3dsx
  red-viper.cia:
    size: 664512
    size_str: 648 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v1.1.0/red-viper.cia
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
stars: 923
systems:
- 3DS
title: red-viper
unique_ids:
- '0xFE7CB'
update_notes: '<p dir="auto">This release improves the software renderer and enables
  it for Test Chamber on New 3DS. This fixes the issue where black walls may appear
  transparent.<br>

  The old 3DS is not fast enough to run a software renderer, so it is not enabled
  there. There is an alternative solution that could work on the o3DS, but it is not
  yet clear whether this solution is viable. See <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3323924534" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/88" data-hovercard-type="issue"
  data-hovercard-url="/skyfloogle/red-viper/issues/88/hovercard" href="https://github.com/skyfloogle/red-viper/issues/88">#88</a>
  for more information.</p>

  <ul dir="auto">

  <li>Improve software renderer and enabled it for Test Chamber on New 3DS, fixing
  see-through black walls</li>

  <li>Fixed XB instruction not saving when register is in-memory, resulting in crashes
  in the comet shooting minigame in Galactic Pinball''s Colony stage (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3303941971" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/87" data-hovercard-type="issue"
  data-hovercard-url="/skyfloogle/red-viper/issues/87/hovercard" href="https://github.com/skyfloogle/red-viper/issues/87">#87</a>)</li>

  <li>Numerous improvements to interpreter

  <ul dir="auto">

  <li>These changes do not affect any existing games, but do make it easier to test
  the emulator in alternate environments</li>

  </ul>

  </li>

  </ul>'
updated: '2025-08-15T00:05:03Z'
version: v1.1.0
version_title: v1.1.0
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