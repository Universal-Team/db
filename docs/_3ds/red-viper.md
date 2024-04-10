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
    size: 442880
    size_str: 432 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.3/red-viper.3dsx
  red-viper.cia:
    size: 529856
    size_str: 517 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.3/red-viper.cia
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
systems:
- 3DS
title: red-viper
unique_ids:
- '0xFE7CB'
update_notes: '<p dir="auto">This release features much smoother gameplay, partially
  thanks to running the 3DS displays at 50Hz! Also includes a number of compatibility
  improvements, especially with homebrew.</p>

  <ul dir="auto">

  <li>Run 3DS displays at 50Hz (thanks to everyone in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2178306727" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/46" data-hovercard-type="issue"
  data-hovercard-url="/skyfloogle/red-viper/issues/46/hovercard" href="https://github.com/skyfloogle/red-viper/issues/46">#46</a>
  who knows much more about this than I do!)</li>

  <li>Improve frame pacing by rendering on VBlank</li>

  <li>The image is now displayed in full 24-bit colour</li>

  <li>Various renderer optimizations, significantly improving performance in Elevated
  Speed</li>

  <li>Improved audio clarity</li>

  <li>Fixed issues with various sound effects in Wario Land</li>

  <li>Fixed compatibility hack for Virtual Lab''s English patch</li>

  <li>Improved performance in Nester''s Funky Bowling</li>

  <li>Compatibility fixes for lots of homebrew</li>

  <li>Add a confirmation prompt to Reset and Quit menu options</li>

  <li>Game progress is now saved when entering sleep mode</li>

  </ul>'
updated: '2024-04-10T18:18:19Z'
version: v0.9.3
version_title: v0.9.3
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