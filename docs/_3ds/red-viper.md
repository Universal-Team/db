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
    size: 408212
    size_str: 398 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.2.1/red-viper.3dsx
  red-viper.cia:
    size: 508352
    size_str: 496 KiB
    url: https://github.com/skyfloogle/red-viper/releases/download/v0.9.2.1/red-viper.cia
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
update_notes: '<p dir="auto">This patch features fixes for a few critical bugs that
  snuck into v0.9.2, including the .cia not working on O3DS and the crash screen causing
  a ghost image when left alone for too long.</p>

  <h2 dir="auto">v0.9.2 changelog</h2>

  <p dir="auto">This release features a new audio engine allowing for <strong>sample
  playback</strong>, improved support for some homebrew such as <strong>Hyper Fighting</strong>
  and <strong>Elevated Speed</strong>, and a number of UI improvements, including
  <strong>button controls</strong>.</p>

  <p dir="auto">Some games may play samples at an incorrect speed. A <a href="https://github.com/skyfloogle/red-viper/wiki/Compatibility-list">compatibility
  list</a> has been created, listing these and any other lingering issues.</p>

  <p dir="auto">Big thanks to everyone who contributed!</p>

  <h3 dir="auto">Emulation improvements</h3>

  <ul dir="auto">

  <li>New audio engine allowing for sample playback</li>

  <li>16MB ROMs can now be loaded on o3DS</li>

  <li>Fixed music speed in Golf</li>

  <li>Faster affine layer drawing</li>

  <li>Various other emulation bugfixes (including <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2171767732" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/41" data-hovercard-type="pull_request"
  data-hovercard-url="/skyfloogle/red-viper/pull/41/hovercard" href="https://github.com/skyfloogle/red-viper/pull/41">#41</a>
  and <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2172542176"
  data-permission-text="Title is private" data-url="https://github.com/skyfloogle/red-viper/issues/43"
  data-hovercard-type="pull_request" data-hovercard-url="/skyfloogle/red-viper/pull/43/hovercard"
  href="https://github.com/skyfloogle/red-viper/pull/43">#43</a> by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/pizzarollsroyce/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/pizzarollsroyce">@pizzarollsroyce</a>)</li>

  </ul>

  <h3 dir="auto">UI improvements</h3>

  <ul dir="auto">

  <li>Button input in GUI (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2182379580" data-permission-text="Title is private" data-url="https://github.com/skyfloogle/red-viper/issues/47"
  data-hovercard-type="pull_request" data-hovercard-url="/skyfloogle/red-viper/pull/47/hovercard"
  href="https://github.com/skyfloogle/red-viper/pull/47">#47</a> by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/JeffRuLz/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/JeffRuLz">@JeffRuLz</a>)</li>

  <li>Zip file support</li>

  <li>Improved debug dumps for easier crash reproduction</li>

  <li>Allow mapping face buttons to the triggers on N3DS (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2170765702" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/39" data-hovercard-type="pull_request"
  data-hovercard-url="/skyfloogle/red-viper/pull/39/hovercard" href="https://github.com/skyfloogle/red-viper/pull/39">#39</a>
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/vaguerant/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/vaguerant">@vaguerant</a>)</li>

  <li>Button to turn off the touchscreen backlight (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2182543872" data-permission-text="Title
  is private" data-url="https://github.com/skyfloogle/red-viper/issues/48" data-hovercard-type="pull_request"
  data-hovercard-url="/skyfloogle/red-viper/pull/48/hovercard" href="https://github.com/skyfloogle/red-viper/pull/48">#48</a>
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/vaguerant/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/vaguerant">@vaguerant</a>)</li>

  </ul>'
updated: '2024-03-25T17:19:50Z'
version: v0.9.2.1
version_title: v0.9.2.1
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