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
download_page: https://github.com/NateXS/Scratch-Everywhere/releases
downloads:
  scratch-3ds.3dsx:
    size: 7062804
    size_str: 6 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.21/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 6120384
    size_str: 5 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.21/scratch-3ds.cia
github: NateXS/Scratch-Everywhere
icon: https://raw.githubusercontent.com/NateXS/Scratch-Everywhere/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/NateXS/Scratch-Everywhere/refs/heads/main/gfx/logo.png
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 286
systems:
- 3DS
title: Scratch Everywhere!
update_notes: '<h2>New Features</h2>

  <ul>

  <li><strong>Main menu splash text!</strong>

  <ul>

  <li>A random message will appear at the bottom of the logo!</li>

  </ul>

  </li>

  </ul>

  <h2>Runtime Changes</h2>

  <ul>

  <li>Reverted vector image collision fix

  <ul>

  <li>This caused many issues with image rendering, so vector image collision will
  be inaccurate until we find a better fix.</li>

  </ul>

  </li>

  <li>Fixed collision not working on clones</li>

  <li><code class="notranslate">Broadcast</code> and <code class="notranslate">Broadcast
  and wait</code> blocks should work more consistently</li>

  <li>Fixed sprites sometimes rendering behind the backdrop</li>

  <li>Added version number in main menu</li>

  <li>Changed font in main menu</li>

  <li>Fixed controls menu not saving or loading properly</li>

  <li>Removed <code class="notranslate">.sb3</code> extension in the project menu</li>

  </ul>

  <h2>3DS Changes</h2>

  <div class="markdown-alert markdown-alert-important"><p class="markdown-alert-title"><svg
  class="octicon octicon-report mr-2" viewBox="0 0 16 16" version="1.1" width="16"
  height="16" aria-hidden="true"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216
  0 16 .784 16 1.75v9.5A1.75 1.75 0 0 1 14.25 13H8.06l-2.573 2.573A1.458 1.458 0 0
  1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.5c0 .138.112.25.25.25h2a.75.75
  0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25
  0 0 0-.25-.25Zm7 2.25v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 9a1 1 0
  1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>Important</p><p>This beta release changes the
  location Scratch projects need to be placed at!<br>

  Changed from <code class="notranslate">sd:/3ds/</code> to <code class="notranslate">sd:/3ds/scratch-everywhere</code>!
  Make sure to move your projects!</p>

  </div>

  <ul>

  <li><strong>CIA release!</strong>

  <ul>

  <li>Highly requested feature finally brought together!</li>

  <li>Via pull request #317!</li>

  </ul>

  </li>

  <li>New <code class="notranslate">RAM_AMOUNT</code> compile variable

  <ul>

  <li>Used for old 3DS to specify the maximum amount of RAM it can use</li>

  <li>More info in the README</li>

  </ul>

  </li>

  <li>Changed executable name from <code class="notranslate">Scratch</code> to <code
  class="notranslate">scratch-3ds</code></li>

  <li>Optimized text rendering</li>

  </ul>

  <h2>PS Vita Changes</h2>

  <ul>

  <li>Significantly improved performance!

  <ul>

  <li>Via pull request #321!</li>

  </ul>

  </li>

  </ul>

  <h2>Known Issues</h2>

  <ul>

  <li>Backdrop images may not render correctly</li>

  <li><strong>[3DS]</strong> File size is much larger due to using new fonts</li>

  </ul>'
updated: '2025-09-02T00:38:23Z'
version: '0.21'
version_title: Beta Build 21
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!