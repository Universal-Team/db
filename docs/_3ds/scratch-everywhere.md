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
    size: 8742724
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.2/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 6874048
    size_str: 6 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.2/scratch-3ds.cia
  scratch-ds.nds:
    size: 6008320
    size_str: 5 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.2/scratch-ds.nds
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
stars: 538
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<p dir="auto">The runtime is now up to 60% faster and should have ~7%
  better parity with Scratch! Let''s see what changed...</p>

  <h1 dir="auto">THE GREAT ABSTRACTENING (the third)</h1>

  <p dir="auto">(No, our code did not in fact turn into a black polygonal monster
  with five hundred glowing eyes)</p>

  <p dir="auto"><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>
  did a bunch of refactoring under the hood, which most notably includes:</p>

  <ul dir="auto">

  <li>Abstract project parsing

  <ul dir="auto">

  <li><strong>This means SE! can now read .sb and .sb2 files!</strong> Pretty cool,
  right?</li>

  </ul>

  </li>

  <li>Zip handling has also been abstracted, meaning other libraries such as <code
  class="notranslate">minizip-ng</code> can now be supported, making porting for e.g.
  the OG Xbox possible.</li>

  </ul>

  <p dir="auto">All of this and more™ via PR <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5364205424" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/765"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/765/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/765">#765</a>!</p>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Some collision changes for better parity</li>

  <li>Improved pen (GLCore)</li>

  <li>The runtime now accounts for wait blocks with negative values</li>

  </ul>

  <p dir="auto">If you find any bugs while running your projects that don''t happen
  in Scratch, as always, please let us know!</p>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Added type prediction for better performance</li>

  <li>Added support for <strong>color touching</strong> detection!</li>

  <li>The <code class="notranslate">When [] &gt; ()</code> hat block has been implemented</li>

  <li>Fixed blurry pen stamping on GLCore-based builds (Linux, macOS and Windows)</li>

  <li>Added the "all at once" block</li>

  <li>Fixed a crash related to sound</li>

  <li>Fixed variable monitors not populating fields correctly in some cases</li>

  <li>Lots of optimizations, notably string and collision-related</li>

  </ul>

  <h2 dir="auto">Platform Changes</h2>

  <h3 dir="auto">PC</h3>

  <p dir="auto">Lots of new stuff on PC this time around...</p>

  <ul dir="auto">

  <li>XDG Desktop Portal support!</li>

  <li>[Windows] Fixed a directory picker bug that caused it to return multiple trailing
  slashes in a row at the end of a path.</li>

  <li>[Windows] The OpenGL and GLCore renderers can now use windowing directly from
  the Win32 API</li>

  <li>[Windows] Added a bunch of native backends, including GDI rendering and WinMM
  audio!</li>

  <li>[Windows] Added an easy installer if you prefer having SE! on your computer
  that way!</li>

  <li>[Linux] Audio now uses libpulse instead of SDL2. This also comes with the benefit
  of reducing the executable''s file size on that platform!</li>

  <li>Other (mostly PC dialog-related) refactoring and fixing under the hood done
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/samuelvenable/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/samuelvenable">@samuelvenable</a>
  in the following PRs: <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5609017223" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/781"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/781/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/781">#781</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5609988091"
  data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/783"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/783/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/783">#783</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5655769903"
  data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/786"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/786/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/786">#786</a></li>

  </ul>

  <h3 dir="auto">Libretro</h3>

  <ul dir="auto">

  <li>Reset is now supported! (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5467150017" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/772"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/772/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/772">#772</a>)</li>

  </ul>

  <h2 dir="auto">Translations</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/jamalkamaladdin/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/jamalkamaladdin">@jamalkamaladdin</a>
  added the Azerbaijani language!</li>

  <li>Fixed some typos occurring in both Spanish variants (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/luarpri/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/luarpri">@luarpri</a>!)</li>

  <li>Linux .desktop file is now translated.</li>

  </ul>

  <div class="markdown-alert markdown-alert-warning" dir="auto"><p class="markdown-alert-title"
  dir="auto"><svg data-component="Octicon" class="octicon octicon-alert mr-2" viewBox="0
  0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M6.457
  1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75
  1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25
  0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1
  1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>Warning</p><p dir="auto">Due to the changes
  made during refactoring and other complications, the following releases will be
  delayed until 1.2.1 OR 1.3:</p>

  <ul dir="auto">

  <li>PS4</li>

  <li>webOS</li>

  </ul>

  </div>

  <p dir="auto">This release was brought to you by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/luarpri/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/luarpri">@luarpri</a>
  (new contributor!), <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/samuelvenable/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/samuelvenable">@samuelvenable</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>,
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a>!
  (no nate this time 😔)</p>'
updated: '2026-10-07T03:03:25Z'
version: '1.2'
version_title: Release 1.2
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!