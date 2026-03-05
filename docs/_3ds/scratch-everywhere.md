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
    size: 8024640
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.35/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 6902720
    size_str: 6 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.35/scratch-3ds.cia
  scratch-ds.nds:
    size: 5468160
    size_str: 5 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.35/scratch-ds.nds
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
stars: 457
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Fix crash when loading audio in unpacked projects</li>

  <li>Fix custom blocks still running after deleting the sprite</li>

  <li>Added support for TurboWarp''s 0 FPS option</li>

  <li>Fix controls not being set sometimes</li>

  <li>Pen is now cleared when exiting a project</li>

  <li>Fix high DPI displays being scaled weirdly (via <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3882683246" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/552"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/552/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/552">#552</a>)</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Added <code class="notranslate">is online?</code> block

  <ul dir="auto">

  <li>Please note that this block isn''t correctly implemented, as it will only return
  true if your build supports cloud variables.</li>

  </ul>

  </li>

  <li>Added support for the <code class="notranslate">slider</code> Monitor type</li>

  <li>Added pages to <code class="notranslate">list</code> Monitors</li>

  <li>The <code class="notranslate">Stop All</code> block no longer takes you to the
  main menu

  <ul dir="auto">

  <li>To get to the main menu, you can pause the Project by holding <code class="notranslate">start</code>
  for 3 seconds.</li>

  </ul>

  </li>

  <li>Changed Sprite layering to be closer to Scratch</li>

  <li>Fixed some parity issues with <code class="notranslate">Backdrop</code> blocks</li>

  <li>The <code class="notranslate">mod</code> block can now return <code class="notranslate">NaN</code></li>

  <li>The <code class="notranslate">x contains x</code> block is now case-insensitive</li>

  <li><code class="notranslate">Sound</code> blocks now yield for 1 tick</li>

  <li>The <code class="notranslate">Size</code> reporter block now has its value rounded</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fix bottom screen being white in Dual-Screen mode</li>

  <li>Fix text position being a bit too far down</li>

  </ul>'
updated: '2026-02-08T14:06:56Z'
version: '0.35'
version_title: Beta Build 35
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!