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
    size: 8898056
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.26/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 7836608
    size_str: 7 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/0.26/scratch-3ds.cia
github: ScratchEverywhere/ScratchEverywhere
icon: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/ScratchEverywhere/ScratchEverywhere/refs/heads/main/gfx/logo.png
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 387
systems:
- 3DS
title: Scratch Everywhere!
update_notes: '<h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Migrated from SDL2 to SDL3 for audio

  <ul dir="auto">

  <li>Overall audio performance will be better with this change!</li>

  <li>Every sound is now a streamed sound, meaning you no longer have to put certain
  sounds in the stage!</li>

  </ul>

  </li>

  <li>Refactored images to use 2x less RAM!</li>

  <li>Unused images will now stay in memory for longer before being freed

  <ul dir="auto">

  <li>Changed from 4 seconds to 21 seconds</li>

  </ul>

  </li>

  <li>Audio now works when using <code class="notranslate">.cia</code></li>

  </ul>

  <h2 dir="auto">GameCube Changes</h2>

  <p dir="auto"><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Extrems/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Extrems">@Extrems</a>
  has done a ton of work to the GameCube port recently!</p>

  <ul dir="auto">

  <li>Migrated to libogc2</li>

  <li>Fixed not being able to find projects in Main Menu

  <ul dir="auto">

  <li>This means the GameCube build can finally come back to releases!</li>

  </ul>

  </li>

  <li>Fixed GameCube controller inputs getting stuck</li>

  <li>Fixed system time getting reset to January 1st, 2000</li>

  <li>Fixed progressive scan mode being forcibly enabled when using component video</li>

  <li>General GameCube code cleanup</li>

  <li>All via pull request <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3528029154" data-permission-text="Title is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/411"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/411/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/411">#411</a>!</li>

  </ul>

  <h2 dir="auto">Switch Changes</h2>

  <ul dir="auto">

  <li>Fixed audio not working</li>

  <li>Fixed Dockerfile builds crashing

  <ul dir="auto">

  <li>This should also fix the crashing that was present in Beta 25.</li>

  </ul>

  </li>

  <li>Fixed resolution not getting changed correctly</li>

  <li>Swapped ABXY buttons from Xbox layout to Nintendo layout</li>

  <li>Added correct error text for no projects in Main Menu</li>

  <li>Fixed icon not showing up</li>

  </ul>

  <h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Lists now have a maximum length of <code class="notranslate">200,000</code>
  items</li>

  <li>the <code class="notranslate">equals</code> block is now case-insensitive, matching
  Scratch behavior</li>

  <li><code class="notranslate">Stop "other scripts in this sprite"</code> block now
  stops playing sounds in the sprite</li>

  <li>Sounds are now in memory longer before getting freed

  <ul dir="auto">

  <li>Changed from 8 seconds to 21 seconds</li>

  </ul>

  </li>

  <li>Sound loading is no longer threaded

  <ul dir="auto">

  <li>This means that every time a new sound is loading, the game will freeze for
  a bit, until the sound is loaded.</li>

  <li>There are pros and cons to this, but ultimately this change makes audio more
  stable.</li>

  </ul>

  </li>

  <li><strong>[SDL2]</strong> Sounds in the stage can now be stopped by <code class="notranslate">Stop
  all sounds</code> block</li>

  <li>The <code class="notranslate">Stop all sounds</code> block now stops every playing
  sound, not just sounds in the sprite</li>

  <li>Fixed collision on off-center costumes</li>

  <li>Fixed sprites with off-center costumes being rendered in the wrong position</li>

  <li>Images now stay loaded in memory when stamping with Pen</li>

  <li>Custom controls will now only try to load with projects from the Main Menu</li>

  <li>Main Menu buttons can now be clicked with touchscreen devices</li>

  <li>Renamed <code class="notranslate">Running flag block</code> text in loading
  screen to <code class="notranslate">Finishing up!</code></li>

  </ul>'
updated: '2025-10-19T12:25:05Z'
version: '0.26'
version_title: Beta Build 26
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!