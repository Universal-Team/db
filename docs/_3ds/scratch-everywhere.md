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
    size: 8865508
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.40/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7660480
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.40/scratch-3ds.cia
  scratch-ds.nds:
    size: 4385792
    size_str: 4 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.40/scratch-ds.nds
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
stars: 491
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Added support for Native Extensions (Via PR <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4189677636" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/598"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/598/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/598">#598</a>)

  <ul dir="auto">

  <li>Native Extensions allow you to run custom extensions via dynamic C++ libraries</li>

  <li>Currently only supports Linux and macOS, with Windows support coming later</li>

  <li>We''re still a ways away from implementing a Lua-based custom extension system
  that will support more platforms</li>

  <li>Native Extensions can be found at this repo: <a href="https://github.com/ScratchEverywhere/native-extensions">https://github.com/ScratchEverywhere/native-extensions</a></li>

  </ul>

  </li>

  <li>Added an interactive CLI inspector for real time debugging (Via PR <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4289065329" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/624"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/624/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/624">#624</a>)</li>

  <li>Fix audio speeding up in some situations</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Made fencing even more accurate</li>

  <li>Stage Sprite can no longer use the <code class="notranslate">hide</code> block</li>

  <li>Fixed <code class="notranslate">When key Pressed</code> block being able to
  get recalled before it''s finished</li>

  <li>Fixed <code class="notranslate">Makeymakey</code> blocks being called without
  pressing any buttons</li>

  <li>Fixed <code class="notranslate">Letter # of x</code> block not being able to
  return special characters</li>

  </ul>

  <h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>New <code class="notranslate">op op op :itchytongue:</code> splash text</li>

  </ul>

  <h2 dir="auto">Authors</h2>

  <p dir="auto">This beta was brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Starlii10/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Starlii10">@Starlii10</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Br0tcraft/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Br0tcraft">@Br0tcraft</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/rttyg46305Unj/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/rttyg46305Unj">@rttyg46305Unj</a>,
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></p>'
updated: '2026-04-26T21:01:25Z'
version: '0.40'
version_title: Beta Build 40
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!