---
author: NateXS
avatar: https://avatars.githubusercontent.com/u/230057427?v=4
categories:
- emulator
- utility
color: '#c291a9'
color_bg: '#805f6f'
created: '2025-05-01T16:11:42Z'
description: Play Scratch games on your 3DS!
download_filter: (\.3dsx|\.cia|\.nds)
download_page: https://github.com/ScratchEverywhere/ScratchEverywhere/releases
downloads:
  scratch-3ds.3dsx:
    size: 24890404
    size_str: 23 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.37/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 23778240
    size_str: 22 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.37/scratch-3ds.cia
  scratch-ds.nds:
    size: 4425728
    size_str: 4 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.37/scratch-ds.nds
github: ScratchEverywhere/ScratchEverywhere
icon: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/icon.png
image: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/3ds/banner.png
image_length: 22206
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
  scratch-ds.nds: https://db.universal-team.net/assets/images/qr/scratch-ds-nds.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 464
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Runtime Changes</h2>

  <h3 dir="auto">The SVG Update!!</h3>

  <ul dir="auto">

  <li>Switched SVG backends from <a href="https://github.com/memononen/nanosvg">NanoSVG</a>
  to <a href="https://github.com/sammycage/lunasvg">LunaSVG</a> (Via <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3993777890" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/568"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/568/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/568">#568</a>)

  <ul dir="auto">

  <li>LunaSVG supports many more SVG features, so things such as bitmap images inside
  of vector images are now supported!</li>

  </ul>

  </li>

  <li>LunaSVG also allows us to support text inside of vector images!

  <ul dir="auto">

  <li>Many of Scratch''s default fonts (<code class="notranslate">Pixel</code>,<code
  class="notranslate">Sans Serif</code>, <code class="notranslate">Serif</code>, <code
  class="notranslate">Handwriting</code>, <code class="notranslate">Marker</code>,
  <code class="notranslate">Curly</code>) are supported</li>

  <li>Other fonts will fallback to a default font</li>

  <li>The app size has increased a bit due to having to embed all the fonts</li>

  </ul>

  </li>

  <li>Added the ability for SVG images to scale up and down in resolution (Via <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4006016689"
  data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/571"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/571/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/571">#571</a>)

  <ul dir="auto">

  <li>This means SVG images should no longer be pixelated when at an increased size!</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Performance Updates</h3>

  <ul dir="auto">

  <li>Added <code class="notranslate">Pen Mode</code> Project Setting

  <ul dir="auto">

  <li>When <code class="notranslate">Pen Mode</code> is set to fast, Performance with
  pen is way faster, with the tradeoff of rendering pen strokes as rectangles instead
  of circles</li>

  <li>Fast pen is good for when your project has hundreds of pen blocks being called
  every frame, otherwise Accurate pen is still a good choice</li>

  </ul>

  </li>

  <li>Added <code class="notranslate">Show FPS</code> Project setting

  <ul dir="auto">

  <li>When turned on, it adds debug Monitors showing you FPS and Frame Time information</li>

  </ul>

  </li>

  <li>Added <code class="notranslate">Keep Project In RAM</code> Project Setting

  <ul dir="auto">

  <li>When turned off, the entire .sb3 project file will no longer be kept in RAM,
  which is great for large projects on low RAM devices</li>

  <li>Assets (Images and Sounds) will take longer to load when this option is turned
  off</li>

  <li>This option is on by default for all devices except for NDS, PSP, and GameCube</li>

  </ul>

  </li>

  <li>Increased Performance by Caching a bunch of data (Variable/List data, block
  handlers, etc) (Via <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3981868530" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/565"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/565/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/565">#565</a>)

  <ul dir="auto">

  <li>In some cases this improves performance quite significantly!</li>

  <li>This is not available for Low RAM devices (PSP, NDS, 3DS, GameCube, Wii)</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li>Fixed crash when loading RomFS projects</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Added support for <code class="notranslate">data_variable</code> and <code class="notranslate">data_listcontents</code>
  hidden blocks (Via <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="3998956710" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/569"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/569/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/569">#569</a>)</li>

  <li>Fixed parsing error when parsing block field values that are arrays</li>

  </ul>

  <h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>Projects are now sorted Alphabetically</li>

  <li>The Unpacked Project button is now a vector instead of a bitmap image</li>

  </ul>

  <h2 dir="auto">PSP &amp; PS Vita Changes</h2>

  <ul dir="auto">

  <li>PSP and Vita are now built in Release mode

  <ul dir="auto">

  <li>This means that performance on these devices should now be much better!</li>

  </ul>

  </li>

  <li>[Vita] denoise livearea background</li>

  </ul>

  <h2 dir="auto">PS4 Changes</h2>

  <ul dir="auto">

  <li>Enable VSync</li>

  </ul>

  <p dir="auto">This Beta was brought to you by; <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DevelopCMD/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DevelopCMD">@DevelopCMD</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/PwLDev/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PwLDev">@PwLDev</a>,
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></p>'
updated: '2026-03-08T14:34:03Z'
version: '0.37'
version_title: Beta Build 37
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!