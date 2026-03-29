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
    size: 9188444
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.38/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7885760
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.38/scratch-3ds.cia
  scratch-ds.nds:
    size: 4319232
    size_str: 4 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.38/scratch-ds.nds
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
stars: 466
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Accurate Sprite collision! (Via pull request <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4098573061" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/586"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/586/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/586">#586</a>)

  <ul dir="auto">

  <li>When using the <code class="notranslate">Touching ___</code> block, collision
  now uses accurate bit-masks instead of rotated rectangles!</li>

  <li>On 3DS and Wii, these bit-masks are 2 times lower in resolution. On NDS, PSP
  and GameCube, they are 3 times lower. This is to save performance.</li>

  <li>Do note that this update does NOT add support for color touching blocks.</li>

  </ul>

  </li>

  <li>Add support for <code class="notranslate">When Stage Clicked</code> block</li>

  <li>Make base conversions work with doubles</li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Finished migrating all platforms to CMake!

  <ul dir="auto">

  <li>This makes it easier for us to add new platforms and features later down the
  road</li>

  </ul>

  </li>

  <li>Only load SVG fonts when needed instead of at the start of the app</li>

  <li>General code refactoring under the hood</li>

  </ul>

  <h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>The <code class="notranslate">Bottom Screen</code> project option no longer
  shows up on platforms that don''t have it</li>

  <li>Pressing <code class="notranslate">L</code> and <code class="notranslate">R</code>
  takes you up and down pages</li>

  <li>Project now stays selected when going from Project Settings menu</li>

  <li>Mouse no longer keeps priority when using a controller/keyboard to navigate
  the menu</li>

  </ul>

  <h2 dir="auto">Windows Changes</h2>

  <ul dir="auto">

  <li>Add support for <code class="notranslate">Text To Speech</code> Extension</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li><code class="notranslate">Say</code> and <code class="notranslate">Think</code>
  blocks now work correctly in dual screen mode</li>

  </ul>

  <h2 dir="auto">Authors</h2>

  <p dir="auto">This beta was brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></p>'
updated: '2026-03-24T13:15:05Z'
version: '0.38'
version_title: Beta Build 38
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!