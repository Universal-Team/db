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
    size: 8332840
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.23/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7459776
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.23/scratch-3ds.cia
github: ScratchEverywhere/ScratchEverywhere
icon: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/logo.png
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 299
systems:
- 3DS
title: Scratch Everywhere!
update_notes: '<h2 dir="auto">New Features</h2>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Scratch Everywhere! Custom Blocks!</strong></p>

  <ul dir="auto">

  <li>This actually isn''t a new feature, but we never talked about them at all so
  I''ll talk about it here :)</li>

  <li>Similar to TurboWarp''s <code class="notranslate">is compiled?</code> and <code
  class="notranslate">is TurboWarp?</code> blocks, We''ve made a few new blocks that
  Scratch Everywhere! can understand!</li>

  <li>You can still upload your projects to the Scratch website when using these new
  blocks!</li>

  <li><code class="notranslate">is Scratch Everywhere!?</code> block returns <code
  class="notranslate">true</code> if your project is running on Scratch Everywhere,
  and returns <code class="notranslate">0</code> otherwise.</li>

  <li><code class="notranslate">is New 3DS</code> block returns <code class="notranslate">true</code>
  if your project is being played on a New 3DS, returns <code class="notranslate">false</code>
  otherwise.</li>

  <li><code class="notranslate">Scratch Everywhere! platform</code> returns the platform
  your game is being played on (<code class="notranslate">3DS</code>,<code class="notranslate">Wii</code>,etc).</li>

  <li>A project containing these blocks can be downloaded <a href="https://scratchbox.grady.link/api/project/K26OtTN2WDJ9/download"
  rel="nofollow">here</a>!</li>

  </ul>

  </li>

  <li>

  <p dir="auto"><strong>Unpack project option in project settings!</strong></p>

  <ul dir="auto">

  <li>Instead of the normal way the runtime works by putting the entire scratch project
  in memory, unpacking a project eliminates this by only loading things when it needs
  to!</li>

  <li>Unpacked projects are great for large projects, and projects with a ton of images!</li>

  <li>Depending on the speed of your SD card, unpacked projects can run way faster
  than normal projects!</li>

  <li>Unpacked projects will have a lightning symbol next to it, and will appear towards
  the bottom of the project menu.</li>

  </ul>

  </li>

  <li>

  <p dir="auto"><strong>Bottom Screen option in project settings!</strong></p>

  <ul dir="auto">

  <li>For 3DS, you can enable any project to be played on the bottom screen instead
  of the top screen!</li>

  <li>Great for projects where the touchscreen plays a key factor in gameplay!</li>

  <li>This also means Scratch Everywhere! can be used with a broken top screen! (I
  know at least 1 person will be happy about this)</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>If you have a project in your Scratch Everywhere! folder named <code class="notranslate">project.sb3</code>,
  the project will now automatically run when opening the app.</li>

  <li>Changed D-Pad controls in Main Menu

  <ul dir="auto">

  <li><strong>NOTE:</strong> If you''re using a Wii Remote, this means you now have
  to use the remote sideways to navigate the Main Menu.</li>

  </ul>

  </li>

  <li>Added more splash text to the Main Menu</li>

  <li>Fixed a ton of memory leaks under the hood</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fixed buttons in the Main Menu sometimes not loading correctly</li>

  </ul>

  <h2 dir="auto">Switch Changes</h2>

  <ul dir="auto">

  <li>Changed resolution to the handheld''s native 1280 x 720, instead of being a
  weird stretched resolution</li>

  </ul>'
updated: '2025-09-14T14:44:05Z'
version: '0.23'
version_title: Beta Build 23
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!