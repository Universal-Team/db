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
    size: 10081024
    size_str: 9 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.29/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 9020352
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.29/scratch-3ds.cia
  scratch-ds.nds:
    size: 4523008
    size_str: 4 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.29/scratch-ds.nds
github: ScratchEverywhere/ScratchEverywhere
icon: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/logo.png
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
  scratch-ds.nds: https://db.universal-team.net/assets/images/qr/scratch-ds-nds.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 414
systems:
- 3DS
title: Scratch Everywhere!
update_notes: '<h2 dir="auto">New Features</h2>

  <ul dir="auto">

  <li>PSP Port!</li>

  </ul>

  <h2 dir="auto">Switch Changes</h2>

  <ul dir="auto">

  <li>Upgraded to the latest <code class="notranslate">libnx</code> version, meaning
  SE! is now supported on Firmware <code class="notranslate">21.0.0</code>.</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fixed app not closing when closed from the Main Menu</li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>The Main Menu is feeling a bit jolly...</li>

  <li>Changed <code class="notranslate">Arialn</code> font to <code class="notranslate">Liberation
  Sans Narrow</code> font</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Added instant block execution

  <ul dir="auto">

  <li>In Scratch, if nothing on screen happens, all blocks run as if <code class="notranslate">Run
  Without Screen Refresh</code> was on. SE! now handles this behavior.</li>

  </ul>

  </li>

  <li>Sprites now correctly run their blocks in layer order</li>

  <li>The <code class="notranslate">direction</code> blocks are now correctly clamped
  and rounded</li>

  <li>The <code class="notranslate">Change Variable by x</code> block now works correctly
  when putting in letters as input</li>

  <li>Fixed some blocks not running without screen refresh when they should</li>

  <li>The <code class="notranslate">Pick random</code> block now correctly works with
  non-decimal numbers</li>

  <li><code class="notranslate">NaN</code> is now correctly handled as a number when
  put in block inputs</li>

  <li>Booleans now work as they would in Scratch</li>

  <li>Uppercase letters in hex colors now work correctly</li>

  <li>SE! now handles Scratch''s rare <code class="notranslate">null</code> input
  bug correctly</li>

  <li>Fixed <code class="notranslate">Broadcast and wait</code> block''s weird behavior
  from a clone who''s ready to be deleted</li>

  </ul>'
updated: '2025-11-17T12:36:06Z'
version: '0.29'
version_title: Beta Build 29
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!