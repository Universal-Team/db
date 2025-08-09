---
author: NateXS
avatar: https://avatars.githubusercontent.com/u/149607394?v=4
categories:
- emulator
- utility
color: '#b2a2a3'
color_bg: '#807475'
created: '2025-05-01T16:11:42Z'
description: Play Scratch games on your 3DS!
download_page: https://github.com/NateXS/Scratch-3DS/releases
downloads:
  Scratch.3dsx:
    size: 2963500
    size_str: 2 MiB
    url: https://github.com/NateXS/Scratch-3DS/releases/download/0.16/Scratch.3dsx
  scratch-gamecube.zip:
    size: 2394790
    size_str: 2 MiB
    url: https://github.com/NateXS/Scratch-3DS/releases/download/0.16/scratch-gamecube.zip
github: NateXS/Scratch-3DS
icon: https://raw.githubusercontent.com/NateXS/Scratch-3DS/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/NateXS/Scratch-3DS/refs/heads/main/gfx/logo.png
image_length: 15313
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
screenshots:
- description: Screenshot1
  url: https://db.universal-team.net/assets/images/screenshots/scratch-3ds/screenshot1.png
- description: Screenshot2
  url: https://db.universal-team.net/assets/images/screenshots/scratch-3ds/screenshot2.png
- description: Screenshot3
  url: https://db.universal-team.net/assets/images/screenshots/scratch-3ds/screenshot3.png
source: https://github.com/NateXS/Scratch-3DS
stars: 253
systems:
- 3DS
title: Scratch 3DS
update_notes: '<h2 dir="auto">New Features</h2>

  <p dir="auto"><strong>Wii and Gamecube port!</strong></p>

  <ul dir="auto">

  <li>The runtime has been ported to 2 new consoles!</li>

  <li>More information in the README!</li>

  </ul>

  <p dir="auto"><strong>[3DS and Wii U] Cloud Variable support!</strong></p>

  <ul dir="auto">

  <li>Cloud Variables now sync over the network with anyone also playing the same
  game!</li>

  <li>Syncs across both Wii U and 3DS</li>

  <li><strong>Note:</strong> does NOT sync with people playing on the Scratch website
  or Turbowarp.</li>

  <li>Via pull request (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3264824143" data-permission-text="Title is private" data-url="https://github.com/NateXS/Scratch-3DS/issues/145"
  data-hovercard-type="pull_request" data-hovercard-url="/NateXS/Scratch-3DS/pull/145/hovercard"
  href="https://github.com/NateXS/Scratch-3DS/pull/145">#145</a>)</li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li><code class="notranslate">Broadcast</code> blocks now have more consistent behavior</li>

  <li>Disabling <code class="notranslate">Fencing</code> in advanced settings now
  disables size limitations</li>

  <li>Variables set to <code class="notranslate">True</code> or <code class="notranslate">False</code>
  no longer gets set to <code class="notranslate">1</code> or <code class="notranslate">0</code></li>

  <li>Images in any project now only load whenever it''s needed, instead of loading
  every image in memory while loading the project</li>

  <li>[Wii U] Main Menu with no projects should now work correctly</li>

  <li>[Wii U] Unzipped projects now load images and sounds correctly</li>

  <li>[3DS] when compiling, the final executable will now be in <code class="notranslate">build/3ds/</code>
  instead of the root directory.</li>

  </ul>'
updated: '2025-08-09T22:52:13Z'
version: '0.16'
version_title: Beta Build 16
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!