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
download_page: https://github.com/ScratchEverywhere/ScratchEverywhere/releases
downloads:
  scratch-3ds.3dsx:
    size: 8455184
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.24/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7521216
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.24/scratch-3ds.cia
github: ScratchEverywhere/ScratchEverywhere
icon: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/logo.png
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 359
systems:
- 3DS
title: Scratch Everywhere!
update_notes: '<h2 dir="auto">New Features</h2>

  <ul dir="auto">

  <li>Add support for changing your username in the main menu settings

  <ul dir="auto">

  <li>If disabled, the <code class="notranslate">username</code> block will return
  your console''s nickname</li>

  <li>If enabled, you can choose a custom username and the <code class="notranslate">username</code>
  block will return that instead</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>The <code class="notranslate">touching</code> block now works correctly with
  vector images</li>

  <li>Fixed sound effects getting cut off if a new one gets played</li>

  <li>Sound effects now get unloaded from memory after a few seconds of it not playing</li>

  <li>Sound effects with low volume now play correctly</li>

  <li>Sound blocks now work correctly if the input is another block</li>

  <li>The main menu buttons has been replaced with new SVG versions</li>

  <li>The main menu GUI now scales depending on screen resolution</li>

  <li>Added project loading screen to SDL2 platforms</li>

  <li>Reverted <code class="notranslate">project.sb3</code> auto opening at startup</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fixed a bug causing some vector images to appear bigger than it should</li>

  </ul>

  <h2 dir="auto">Wii Changes</h2>

  <ul dir="auto">

  <li>The <code class="notranslate">username</code> block now returns the Wii''s nickname</li>

  </ul>'
updated: '2025-09-22T17:04:39Z'
version: '0.24'
version_title: Beta Build 24
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!