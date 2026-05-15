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
    size: 9587168
    size_str: 9 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.0-rc1/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 8434624
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.0-rc1/scratch-3ds.cia
  scratch-ds.nds:
    size: 5109760
    size_str: 4 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.0-rc1/scratch-ds.nds
github: ScratchEverywhere/ScratchEverywhere
icon: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/icon.png
image: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/3ds/banner.png
image_length: 30159
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
  scratch-ds.nds: https://db.universal-team.net/assets/images/qr/scratch-ds-nds.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 512
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<p dir="auto"><strong>A Release Candidate? In this economy? More likely
  than you think!</strong></p>

  <h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>The Menu has been given new music and colors for SE!''s one year anniversary
  (May 2)!

  <ul dir="auto">

  <li>Menu music is, as always, made by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Dogo6647/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a></li>

  </ul>

  </li>

  <li>Translation Support!

  <ul dir="auto">

  <li>In the Settings menu, there will be a new option to change the main menu language!</li>

  <li>We currently support <code class="notranslate">English (US)</code>, <code class="notranslate">Español
  (Latam)</code>, <code class="notranslate">Español (España)</code>, <code class="notranslate">한국어</code>,
  <code class="notranslate">日本語</code>, <code class="notranslate">Português (Portugal)</code>,
  <code class="notranslate">Português (Brasil)</code>, <code class="notranslate">Русский
  (Россия)</code> and <code class="notranslate">Deutsch (Deutschland)</code>.</li>

  <li>It''s thanks to the many translators (listed below) that this is possible!</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Libretro port! (Via PR <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4370088031" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/635"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/635/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/635">#635</a>)</li>

  <li><strong>[SDL2 / SDL3 Platforms]</strong> Completely re-written Accurate Pen
  to be much faster in performance!

  <ul dir="auto">

  <li>Because of this, Accurate Pen is now the default on these platforms.</li>

  </ul>

  </li>

  <li>Added DECtalk support for the Text To Speech Extension (Via PR <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4381840598" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/648"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/648/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/648">#648</a>)

  <ul dir="auto">

  <li>DECtalk is a completely offline Text-To-Speech library!</li>

  <li>You can change whether to use DECtalk or Scratch''s tts system in Main Menu
  settings</li>

  <li>Do note that only certain platforms will have this option in the release build,
  but any platform can have this option enabled when compiling from source.</li>

  </ul>

  </li>

  <li>Fixed Transparent SVG images looking gray</li>

  <li>Audio should sound a bit better</li>

  <li><code class="notranslate">Set size</code> and <code class="notranslate">Change
  Size</code> blocks now work correctly if the costume image hasn''t been loaded yet</li>

  <li>Added constant folding while parsing projects</li>

  <li>Add better support for Solaris/illumos and Haiku (Via PR <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4411993806" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/663"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/663/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/663">#663</a>)</li>

  <li>Fixed a ton of memory leaks</li>

  <li>Remove Monitor caching due to a bug</li>

  </ul>

  <h2 dir="auto">Parity Changes</h2>

  <ul dir="auto">

  <li>Fixed Crashes when using recursive broadcasts and Custom blocks</li>

  <li>Fixed parity issues when doing math with hexadecimal numbers</li>

  <li>Fixed parity issues when doing math with <code class="notranslate">-0</code></li>

  <li>Revert ability to get special characters with <code class="notranslate">letter
  x of x</code> block, due to many bugs caused when introducing it</li>

  <li>Fixed Glide blocks being weird when using clones</li>

  <li>Fixed some issues when getting variables</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fixed crash when sometimes using <code class="notranslate">Erase All</code>
  Pen block</li>

  </ul>

  <h2 dir="auto">Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Starlii10/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Starlii10">@Starlii10</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/samuelvenable/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/samuelvenable">@samuelvenable</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Xeltalliv/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Xeltalliv">@Xeltalliv</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/poipole807/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/poipole807">@poipole807</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a></li>

  </ul>

  <h2 dir="auto">Translators</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/PwLDev/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PwLDev">@PwLDev</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/francthe3dsnerd/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/francthe3dsnerd">@francthe3dsnerd</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/vernacular7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/vernacular7">@vernacular7</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Luapree/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Luapree">@Luapree</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NishiOwO/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NishiOwO">@NishiOwO</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/skibidisonicthehedgehog-glitch/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/skibidisonicthehedgehog-glitch">@skibidisonicthehedgehog-glitch</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MicroChelik123/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MicroChelik123">@MicroChelik123</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SplaatSites/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SplaatSites">@SplaatSites</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Br0tcraft/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Br0tcraft">@Br0tcraft</a></li>

  </ul>'
updated: '2026-05-10T22:33:24Z'
version: 1.0-rc1
version_title: 1.0 Release Candidate 1
website: https://scratcheverywhere.github.io
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!