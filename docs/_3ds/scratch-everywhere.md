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
    size: 10953068
    size_str: 10 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.1/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 9282496
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.1/scratch-3ds.cia
  scratch-ds.nds:
    size: 5669376
    size_str: 5 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.1/scratch-ds.nds
github: ScratchEverywhere/ScratchEverywhere
icon: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/icon.png
image: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/3ds/banner.png
image_length: 30159
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
llm_generation: unknown
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
  scratch-ds.nds: https://db.universal-team.net/assets/images/qr/scratch-ds-nds.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 539
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<p dir="auto">Due to Nate''s current absence, Dogo and I will be making
  releases from this point onward (until Nate returns).</p>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Fixed volume of new sounds not being set correctly</li>

  <li>Fixed missing input resets on some C blocks</li>

  <li>Fixed clones being able to call threads after being deleted</li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Fixed incorrect scaling of vector costumes on initial load</li>

  <li>Optimized collision</li>

  <li>Optimized input fetching</li>

  <li>Optimized number parsing</li>

  </ul>

  <h2 dir="auto">3DS/DS Changes</h2>

  <ul dir="auto">

  <li>Fixed <code class="notranslate">any</code> key not working correctly</li>

  <li>Improved SVG quality in dual screen mode</li>

  </ul>

  <h2 dir="auto">PC Changes</h2>

  <ul dir="auto">

  <li>

  <p dir="auto">Changed the default renderer to OpenGL Core</p>

  <p dir="auto">Due to this change, PC now supports all looks effects (including shader-based
  ones like whirl, fisheye, etc.)</p>

  </li>

  <li>

  <p dir="auto">Changed the default window size to 480x360 to match Scratch''s stage
  size</p>

  </li>

  <li>

  <p dir="auto">Added support for using the native file selector when changing the
  project directory</p>

  </li>

  </ul>

  <h2 dir="auto">webOS Changes</h2>

  <ul dir="auto">

  <li>Fixed crash at startup</li>

  </ul>

  <h2 dir="auto">Internal Changes</h2>

  <ul dir="auto">

  <li>Changed the dependency system to use <a href="https://github.com/catalog-cmake/catalog">Catalog</a>.
  This means building from source should now be easier and faster.</li>

  <li>Added support for SE! to be built as a library. This is the very beginnings
  of a potential (seperate) editor application in the future.</li>

  </ul>

  <p dir="auto">These changes brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/samuelvenable/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/samuelvenable">@samuelvenable</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/iCraft7773/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/iCraft7773">@iCraft7773</a>,
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></p>'
updated: '2026-09-07T05:22:27Z'
version: '1.1'
version_title: Release 1.1
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!