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
    size: 8851488
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.39/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7652288
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.39/scratch-3ds.cia
  scratch-ds.nds:
    size: 4360192
    size_str: 4 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.39/scratch-ds.nds
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
stars: 481
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<p dir="auto"><strong>We''re finally gearing up for release! This will
  very likely be the final Beta Build until we get to the release candidate stage,
  and soon after, 1.0!</strong></p>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li><strong>Complete Runtime Rewrite!</strong> (Via PR <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4075706267" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/583"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/583/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/583">#583</a>)

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Br0tcraft/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Br0tcraft">@Br0tcraft</a>
  has been working for months to almost completely rewrite the way Scripts in SE!
  are run, which now more closely resembles Scratch''s <code class="notranslate">Thread</code>
  architecture!</li>

  <li>The rewrite fixes many bugs (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3728293511" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/500"
  data-hovercard-type="issue" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/issues/500/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/500">#500</a>
  for example), and boosts performance a ton!</li>

  <li>Many projects that weren''t playable before, or had weird issues, are now completely
  playable!</li>

  <li>There may be some bugs introduced with this change, so please be sure to report
  any bugs you find!</li>

  <li>This change has also resulted in some of the caching features added in previous
  betas getting removed. The removed caching features will be re-added in the next
  release.</li>

  </ul>

  </li>

  <li><strong>Complete Audio Rewrite</strong> (Via PR <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4074292446" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/582"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/582/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/582">#582</a>)

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>
  has rewritten audio from the ground up to no longer rely on SDL''s mixer libraries!</li>

  <li>More audio formats are now supported, and the <code class="notranslate">Pitch</code>
  and <code class="notranslate">Pan left-right</code> audio effects now work on all
  platforms!</li>

  <li>You no longer need to put sounds in the Stage for streamed audio, as now every
  Sprite will have it!</li>

  <li>Unfortunately with this change, we were not able to get audio working for the
  NDS, so this release on NDS will have audio temporarily disabled.</li>

  </ul>

  </li>

  <li>Added support for TurboWarp''s <code class="notranslate">Custom Reporter</code>
  extension</li>

  <li>Added support for <code class="notranslate">Translate</code> Scratch extension
  (Via PR <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="4248695776" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/612"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/612/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/612">#612</a>)

  <ul dir="auto">

  <li>Adding this extension was partly the reason the Runtime was rewritten in the
  first place, since scripts in the old Runtime couldn''t yield if a reporter returned
  nothing that frame.</li>

  </ul>

  </li>

  <li>Added <code class="notranslate">Warp Timer</code> Project setting

  <ul dir="auto">

  <li>Having this enabled makes scripts check if they''ve been running for a long
  time (500 ms), and run at a low framerate instead of getting stuck until the loop
  finishes.</li>

  <li>This is similar to Scratch''s behavior. It fixes crashes/freezes but may cause
  a performance impact on some devices, so turning it off may improve performance.</li>

  </ul>

  </li>

  <li>Only downscale images on some platforms (<code class="notranslate">NDS</code>,
  <code class="notranslate">PSP</code> and <code class="notranslate">GameCube</code>)

  <ul dir="auto">

  <li>Images on all platforms used to be down-scaled by 2x to save on RAM/VRAM usage</li>

  <li>Since Scratch internally doubles the size of each image, there should''ve been
  no visual difference. However, some projects don''t have their image size doubled,
  making it look pixelated in SE!</li>

  </ul>

  </li>

  <li>Sprite fencing is now more accurate</li>

  <li>Fix memory leak when an image fails to load</li>

  <li>Fix parsing crash if certain project/Sprite properties were empty</li>

  </ul>

  <h2 dir="auto">Switch Changes</h2>

  <ul dir="auto">

  <li>Fixed touch screen not working</li>

  </ul>

  <h2 dir="auto">Credits</h2>

  <p dir="auto">This beta was brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Br0tcraft/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Br0tcraft">@Br0tcraft</a>,
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></p>'
updated: '2026-04-12T20:46:43Z'
version: '0.39'
version_title: Beta Build 39
website: https://scratcheverywhere.github.io/ScratchEverywhere/
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!