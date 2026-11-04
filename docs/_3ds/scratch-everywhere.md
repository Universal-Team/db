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
    size: 9862056
    size_str: 9 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.3/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7926720
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.3/scratch-3ds.cia
  scratch-ds.nds:
    size: 10997248
    size_str: 10 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.3/scratch-ds.nds
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
stars: 544
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Xbox</h2>

  <ul dir="auto">

  <li>SE! has been ported to the original Xbox!</li>

  <li>Featuring a custom renderer, complete with HD A/V, Pen and Sprite effect support!

  <ul dir="auto">

  <li>SDL3 renderer is also available as a fallback (though will be removed in a future
  release)</li>

  </ul>

  </li>

  <li>Port by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MikeDev101/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MikeDev101">@MikeDev101</a></li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Added a new <strong>Bytecode runtime</strong>

  <ul dir="auto">

  <li>Bytecode is a much smaller and faster way of executing Scratch projects!</li>

  <li>Projects ran with bytecode runs <strong>~2.25x faster</strong> than 1.2.1, and
  consumes less RAM!</li>

  <li>Bytecode is on by default for all projects, and can be changed in Project settings.</li>

  </ul>

  </li>

  <li>Added support for <code class="notranslate">Loudness</code> blocks

  <ul dir="auto">

  <li>This is the last block we didn''t support, so with that we now support EVERY
  Scratch block!</li>

  </ul>

  </li>

  <li>Added the ability to switch renderer, input and audio backends

  <ul dir="auto">

  <li>Useful for testing, and for computers that may not support a certain backend</li>

  <li>These can be changed in Main Menu settings</li>

  </ul>

  </li>

  <li>Monitors now have an improved look on PC</li>

  <li>Made audio more performant and use less resources</li>

  </ul>

  <h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>New spOooOoky theme! (please ignore the fact that it''s now November)

  <ul dir="auto">

  <li>New menu music by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Dogo6647/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>
  as always</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Wii U Changes</h2>

  <ul dir="auto">

  <li>Added a new GX2 Renderer

  <ul dir="auto">

  <li>This adds support for both Sprite effects and dual screen support!</li>

  <li>Dual screen mode requires your project to be the same resolution as 3DS''s dual
  screen mode (400x480).</li>

  </ul>

  </li>

  <li>Added a Wii U specific audio backend</li>

  </ul>

  <h2 dir="auto">NDS Changes</h2>

  <ul dir="auto">

  <li>Audio has been re-enabled!

  <ul dir="auto">

  <li>Currently NDS only supports playing <code class="notranslate">.wav</code> files.</li>

  </ul>

  </li>

  <li>The NDS exclusive chiptune menu music is back</li>

  </ul>

  <h2 dir="auto">Windows Changes</h2>

  <ul dir="auto">

  <li>Added new Direct3D 9 Renderer

  <ul dir="auto">

  <li>This renderer will be the new default for Windows going forward.</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Nintendo Switch &amp; PS4 Changes</h2>

  <ul dir="auto">

  <li>Added support for OpenGL Core

  <ul dir="auto">

  <li>This now means that Sprite effects are now supported on these platforms.</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fix bottom screen cursor mapping</li>

  <li>Fix Pen rendering on dual screen mode</li>

  </ul>

  <h2 dir="auto">PSP Changes</h2>

  <ul dir="auto">

  <li>Update renderer to SDL3

  <ul dir="auto">

  <li>Fixes text and Pen rendering, and should overall be more performant</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">PS Vita Changes</h2>

  <ul dir="auto">

  <li>Fix app crashing on startup</li>

  </ul>

  <h2 dir="auto">Wii Changes</h2>

  <ul dir="auto">

  <li>Fix app crashing on startup</li>

  </ul>

  <p dir="auto">This release was brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Br0tcraft/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Br0tcraft">@Br0tcraft</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/luarpri/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/luarpri">@luarpri</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MikeDev101/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MikeDev101">@MikeDev101</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Mistium/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Mistium">@Mistium</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ZacharyLeahan/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZacharyLeahan">@ZacharyLeahan</a>,
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/PwLDev/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PwLDev">@PwLDev</a></p>'
updated: '2026-11-01T09:02:42Z'
version: '1.3'
version_title: Release 1.3
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!