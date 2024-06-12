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
    size: 522952
    size_str: 510 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.5/red-viper.3dsx
  red-viper.cia:
    size: 582080
    size_str: 568 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.5/red-viper.cia
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
update_notes: '<p dir="auto">This release features significantly improved input remapping.</p>

  <h2 dir="auto">Control changes</h2>

  <ul dir="auto">

  <li>New "Custom" control scheme (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2311648825" data-permission-text="Title is private" data-url="https://github.com/skyfloogle/red-viper/issues/67"
  data-hovercard-type="pull_request" data-hovercard-url="/skyfloogle/red-viper/pull/67/hovercard"
  href="https://github.com/skyfloogle/red-viper/pull/67">#67</a>)</li>

  <li>In the Custom control scheme, any 3DS button can be mapped to any VB button</li>

  <li>Toggle and Turbo modes are available for each button</li>

  <li>The previous control menu is still available as "Preset" for its ease of use</li>

  <li>Added remapping option to 3DS D-Pad in Preset mode (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2279829075" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/65" data-hovercard-type="pull_request"
  data-hovercard-url="/skyfloogle/red-viper/pull/65/hovercard" href="https://github.com/skyfloogle/red-viper/pull/65">#65</a>)</li>

  <li>Virtual buttons on the touchscreen can now be set to the face buttons by default</li>

  <li>"Switch" button can now be turned off</li>

  </ul>

  <h2 dir="auto">Other settings changes</h2>

  <ul dir="auto">

  <li>Configurations can now be game-specific, including controls, graphics, etc</li>

  <li>Moved rv_config.ini to a more standard location (sdmc:/config/red-viper)</li>

  <li>The red-viper directory with savestates and per-game configs can be moved by
  manually editing rv_config.ini</li>

  <li>Added VBLink for homebrew developers, accessible by pressing Y on the main menu
  (will be supported in future versions of <a href="https://www.vuengine.dev/" rel="nofollow">VUEngine
  Studio</a>)</li>

  </ul>

  <h2 dir="auto">Other changes</h2>

  <ul dir="auto">

  <li>Improved stability for capture cards</li>

  <li>Fixed occasional bug where the emulator would crash on startup</li>

  </ul>'
updated: '2024-06-11T19:48:02Z'
version: v0.9.5
version_title: v0.9.5
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