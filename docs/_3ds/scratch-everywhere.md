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
    size: 8026984
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.36/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 6902720
    size_str: 6 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.36/scratch-3ds.cia
  scratch-ds.nds:
    size: 5478400
    size_str: 5 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.36/scratch-ds.nds
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
stars: 460
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Refactored a bunch of image code under the hood

  <ul dir="auto">

  <li>This also has the side effect of fixing some Sprite position and brightness
  effect issues</li>

  </ul>

  </li>

  <li>The <code class="notranslate">touching __</code> block has been optimized</li>

  <li>Fixed default controls getting set even when custom controls are set</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Support <code class="notranslate">undefined</code> as a value</li>

  <li>Add support for <code class="notranslate">motion_xscroll</code>, <code class="notranslate">motion_yscroll</code>,
  and <code class="notranslate">sensing_userid</code> blocks</li>

  <li>Variable monitors can now only display numbers at up to 6 decimal places</li>

  <li>All via PR (<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="3972578263" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/563"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/563/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/563">#563</a>)</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fixed position/fencing issues on custom resolution projects</li>

  <li>Fixed memory leak when freeing audio</li>

  <li>Fixed Audio cracking and slowdown issues on Old 3DS (Via an <a href="https://github.com/libsdl-org/SDL/pull/15060"
  data-hovercard-type="pull_request" data-hovercard-url="/libsdl-org/SDL/pull/15060/hovercard">SDL
  PR</a>)</li>

  </ul>

  <h2 dir="auto">webOS Changes</h2>

  <ul dir="auto">

  <li>Fixed project path being incorrect</li>

  </ul>

  <h2 dir="auto">PSP Changes</h2>

  <ul dir="auto">

  <li>Disabled VSync</li>

  </ul>'
updated: '2026-02-22T15:07:48Z'
version: '0.36'
version_title: Beta Build 36
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!