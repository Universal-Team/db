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
    size: 12527172
    size_str: 11 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.32/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 11453376
    size_str: 10 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.32/scratch-3ds.cia
  scratch-ds.nds:
    size: 6924288
    size_str: 6 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.32/scratch-ds.nds
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
stars: 431
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>Added a Project pause menu

  <ul dir="auto">

  <li>Accessed by holding <code class="notranslate">Start</code> for 3 seconds while
  in a project (1 on keyboard)</li>

  <li>Currently has the ability to exit a project, re-run a project, and toggle Turbo
  Mode</li>

  <li>This feature is not accessible in RomFS projects</li>

  </ul>

  </li>

  <li>Updated logo (Via <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3765023984" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/514"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/514/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/514">#514</a>)</li>

  <li>Added the ability to change the path that projects will be found in</li>

  <li>Menu music can now be turned off in menu settings</li>

  <li>Added new menu splash text, some that could even use your username!</li>

  <li>Fixed menu splash text position being off at higher resolutions</li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>We did a whooole lot of code refactoring under the hood

  <ul dir="auto">

  <li>This may introduce new bugs we aren''t aware of yet, so be sure to open an issue
  if you find one!</li>

  </ul>

  </li>

  <li>OpenGL Port! (Via <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3764398964" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/512"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/512/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/512">#512</a>)</li>

  <li>The <code class="notranslate">Open Project</code> custom block can now open
  projects inside of the RomFS (Via <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3760928009" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/508"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/508/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/508">#508</a>)

  <ul dir="auto">

  <li><a href="https://scratchbox.dev/project/twStEkSKjQaH" rel="nofollow">Info about
  the <code class="notranslate">Open Project</code> block for those unaware</a></li>

  </ul>

  </li>

  <li>The <code class="notranslate">Text To Speech</code> block will no longer run
  if it fails to download the audio track</li>

  <li>Fixed cloud variables not working if changing more than 1 variable at a time</li>

  <li>Fixed the position of Sprites being off sometimes</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Fixed the order in which <code class="notranslate">When I start as clone</code>
  blocks run</li>

  <li>Fixed <code class="notranslate">Next Backdrop</code> block not working</li>

  <li>You can no longer click on a Sprite that has a <code class="notranslate">ghost</code>
  effect of 100</li>

  <li>The <code class="notranslate">For Each</code> block now has better parity</li>

  <li>The <code class="notranslate">When Key Pressed</code> block is no longer tied
  to the FPS</li>

  <li>Turbo Mode now works like Scratch</li>

  <li>The <code class="notranslate">Broadcast and Wait</code> block now works like
  Scratch</li>

  <li>Fixed the run order of repeating blocks</li>

  <li>Fixed repeat loops not working if ran for over 10.6 years</li>

  <li>Added more accurate <code class="notranslate">double</code> to <code class="notranslate">string</code>
  conversion (Via (<a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="3772050288" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/520"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/520/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/520">#520</a>)</li>

  <li>Variables can no longer be an <code class="notranslate">int</code></li>

  <li>Fixed some custom blocks not working</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Collision in Dual-Screen mode is now correct</li>

  <li>Mouse position in Dual-Screen mode is now correct</li>

  </ul>

  <h2 dir="auto">PC Changes</h2>

  <ul dir="auto">

  <li>The <code class="notranslate">username</code> block can now get your PC''s username</li>

  <li>Settings are now stored in your OS''s respective configuration folder.</li>

  </ul>

  <h2 dir="auto">NDS Changes</h2>

  <ul dir="auto">

  <li>Added new menu music</li>

  </ul>

  <p dir="auto">This beta was brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Br0tcraft/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Br0tcraft">@Br0tcraft</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/leap0x7b/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/leap0x7b">@leap0x7b</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/roccopm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/roccopm">@roccopm</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DevelopCMD/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DevelopCMD">@DevelopCMD</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Starlii10/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Starlii10">@Starlii10</a>,
  aaaaand <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></p>'
updated: '2026-01-05T01:19:39Z'
version: '0.32'
version_title: Beta Build 32
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!