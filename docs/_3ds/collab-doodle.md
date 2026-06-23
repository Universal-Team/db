---
author: Thomas Armstrong
avatar: https://avatars.githubusercontent.com/u/12937683?v=4
categories:
- game
color: '#689290'
color_bg: '#5b807e'
created: '2024-12-13T18:24:03Z'
description: Collab Doodle is a simple drawing application designed for the Nintendo
  3DS platform. It allows users to create and manipulate graphical content using various
  brush sizes and colors with other people on a shared canvas!
download_page: https://github.com/ArmstrongThomas/Doodle/releases
downloads:
  CollabDoodle-update.3dsx:
    size: 280420
    size_str: 273 KiB
    url: https://github.com/ArmstrongThomas/Doodle/releases/download/v1.1.0/CollabDoodle-update.3dsx
github: ArmstrongThomas/Doodle
icon: https://raw.githubusercontent.com/ArmstrongThomas/Doodle/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/ArmstrongThomas/Doodle/refs/heads/main/icon.png
image_length: 431
layout: app
llm_generation: unknown
screenshots:
- description: Brush select
  url: https://db.universal-team.net/assets/images/screenshots/collab-doodle/brush-select.png
- description: Canvas
  url: https://db.universal-team.net/assets/images/screenshots/collab-doodle/canvas.png
source: https://github.com/ArmstrongThomas/Doodle
stars: 6
systems:
- 3DS
title: Collab Doodle
update_notes: '<h1 dir="auto">Collab Doodle 3DS Client</h1>

  <p dir="auto">Collab Doodle is a Nintendo 3DS homebrew client for drawing together
  on shared server-backed canvases. The bottom screen is the drawing surface, and
  the top screen shows a minimap, channel/status information, controls, and the current
  app version.</p>

  <h2 dir="auto">Current Release</h2>

  <ul dir="auto">

  <li>Version: <code class="notranslate">1.1.0</code></li>

  </ul>

  <h2 dir="auto">Features</h2>

  <ul dir="auto">

  <li>Real-time collaborative drawing with the 3DS touchscreen.</li>

  <li>Top-screen minimap with viewport marker.</li>

  <li>Named channels: <code class="notranslate">main</code>, <code class="notranslate">sketch</code>,
  and <code class="notranslate">test</code>.</li>

  <li>Channel switch UI on the 3DS.</li>

  <li>Color picker, color sampling, brush size/shape controls, and hex color entry.</li>

  <li>Compressed canvas snapshots using zlib.</li>

  <li>Server update checks with manifest, size, and SHA-256 verification.</li>

  <li>App metadata/icon via SMDH, including the visible app version.</li>

  </ul>

  <h2 dir="auto">Screenshots</h2>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/bf6f6af4-396c-473d-bd6e-8dc747d2e07c"><img
  width="325" height="392" alt="image" src="https://github.com/user-attachments/assets/bf6f6af4-396c-473d-bd6e-8dc747d2e07c"
  style="max-width: 100%; height: auto; max-height: 392px;; aspect-ratio: 325 / 392;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/764a0ff5-6994-46f2-b583-b112c4a5ef61"><img
  width="320" height="386" alt="image" src="https://github.com/user-attachments/assets/764a0ff5-6994-46f2-b583-b112c4a5ef61"
  style="max-width: 100%; height: auto; max-height: 386px;; aspect-ratio: 320 / 386;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/f45f9464-cb0e-4d4b-9f0c-d0374a1a65e2"><img
  width="321" height="389" alt="image" src="https://github.com/user-attachments/assets/f45f9464-cb0e-4d4b-9f0c-d0374a1a65e2"
  style="max-width: 100%; height: auto; max-height: 389px;; aspect-ratio: 321 / 389;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <h2 dir="auto">Controls</h2>

  <ul dir="auto">

  <li>Touch bottom screen: Draw.</li>

  <li>Hold LEFT D-Pad or A + drag stylus: Pan viewport.</li>

  <li>START: Refresh canvas from server.</li>

  <li>SELECT: Exit.</li>

  <li>L: Open/close channel selector.</li>

  <li>D-Pad UP/DOWN while channel selector is open: Move channel selection.</li>

  <li>A while channel selector is open: Switch to selected channel.</li>

  <li>R: Open/close controls help on top screen.</li>

  <li>B or D-Pad DOWN: Toggle color picker.</li>

  <li>Hold D-Pad UP + tap canvas: Sample color.</li>

  <li>X: Enter hex color.</li>

  <li>Y: Check for updates.</li>

  </ul>

  <h2 dir="auto">Server Links</h2>

  <ul dir="auto">

  <li>Live canvas viewer: <a href="http://server1.rpgwo.org:3000/" rel="nofollow">http://server1.rpgwo.org:3000/</a></li>

  <li>Gallery: <a href="http://server1.rpgwo.org:3000/gallery.html" rel="nofollow">http://server1.rpgwo.org:3000/gallery.html</a></li>

  <li>Legacy gallery redirect: <a href="http://server1.rpgwo.org/" rel="nofollow">http://server1.rpgwo.org/</a></li>

  </ul>

  <h2 dir="auto">Build Requirements</h2>

  <ul dir="auto">

  <li>devkitPro with devkitARM and libctru.</li>

  <li>3DS zlib portlib installed.</li>

  <li>The project expects <code class="notranslate">DEVKITPRO</code> and <code class="notranslate">DEVKITARM</code>
  to be set.</li>

  </ul>

  <p dir="auto">Example PowerShell environment:</p>

  <div class="highlight highlight-source-powershell" dir="auto"><pre class="notranslate"><span
  class="pl-smi">$<span class="pl-c1">env:</span>DEVKITPRO</span><span class="pl-k">=</span><span
  class="pl-s"><span class="pl-pds">''</span>C:\devkitPro<span class="pl-pds">''</span></span>

  <span class="pl-smi">$<span class="pl-c1">env:</span>DEVKITARM</span><span class="pl-k">=</span><span
  class="pl-s"><span class="pl-pds">''</span>C:\devkitPro\devkitARM<span class="pl-pds">''</span></span>

  <span class="pl-smi">$<span class="pl-c1">env:</span>PATH</span><span class="pl-k">=</span><span
  class="pl-s"><span class="pl-pds">''</span>C:\devkitPro\msys2\usr\bin;C:\devkitPro\tools\bin;C:\devkitPro\devkitARM\bin;<span
  class="pl-pds">''</span></span> <span class="pl-k">+</span> <span class="pl-smi">$<span
  class="pl-c1">env:</span>PATH</span></pre></div>

  <p dir="auto">Build:</p>

  <div class="highlight highlight-source-powershell" dir="auto"><pre class="notranslate">make
  <span class="pl-k">clean</span>

  make</pre></div>

  <h2 dir="auto">Build-Time Configuration</h2>

  <p dir="auto">The Makefile exposes release/server variables:</p>

  <div class="highlight highlight-source-makefile" dir="auto"><pre class="notranslate"><span
  class="pl-smi">APP_VERSION</span> ?= 1.1.0

  <span class="pl-smi">SERVER_HOST</span> ?= server1.rpgwo.org

  <span class="pl-smi">SERVER_TCP_PORT</span> ?= 3030

  <span class="pl-smi">SERVER_HTTP_PORT</span> ?= 3000</pre></div>

  <p dir="auto">Override them when building local test versions:</p>

  <div class="highlight highlight-source-powershell" dir="auto"><pre class="notranslate">make
  SERVER_HOST<span class="pl-k">=</span><span class="pl-c1">192.168</span>.<span class="pl-c1">1.46</span>
  SERVER_TCP_PORT<span class="pl-k">=</span><span class="pl-c1">3030</span> SERVER_HTTP_PORT<span
  class="pl-k">=</span><span class="pl-c1">3000</span></pre></div>

  <p dir="auto">The same values are compiled into networking, updater requests, client
  hello/version checks, SMDH metadata, and the top-screen version label.</p>

  <h2 dir="auto">Running on Hardware</h2>

  <p dir="auto">Copy the built <code class="notranslate">.3dsx</code> to the SD card,
  or send it with <code class="notranslate">3dslink</code> while the Homebrew Launcher
  netloader is waiting:</p>

  <div class="highlight highlight-source-powershell" dir="auto"><pre class="notranslate">3dslink
  <span class="pl-k">-</span>a <span class="pl-k">&lt;</span>3ds<span class="pl-k">-</span>ip<span
  class="pl-k">&gt;</span> <span class="pl-k">-</span>r <span class="pl-c1">10</span>
  Doodle.3dsx</pre></div>

  <p dir="auto">For the current public build, use:</p>

  <pre lang="text" class="notranslate"><code class="notranslate">CollabDoodle-update.3dsx

  </code></pre>

  <h2 dir="auto">Updates</h2>

  <p dir="auto">The client checks the same Doodle server for <code class="notranslate">/api/updates/latest</code>.</p>

  <p dir="auto">When an update is available:</p>

  <ul dir="auto">

  <li>The client prompts before downloading.</li>

  <li>The download shows progress.</li>

  <li>The downloaded <code class="notranslate">.3dsx</code> is staged beside the running
  app.</li>

  <li>File size and SHA-256 are verified before replacement.</li>

  <li>After install, close the app and reopen Collab Doodle from the Homebrew Launcher.</li>

  </ul>

  <p dir="auto">Homebrew Launcher <code class="notranslate">.3dsx</code> apps do not
  currently support a reliable in-app relaunch of the freshly replaced file, so the
  final step is manual reopen.</p>

  <h2 dir="auto">Repository Notes</h2>

  <p dir="auto">This directory is only the 3DS client. The Node/web server is not
  publicly available and lives beside it in <code class="notranslate">Doodle-Server</code>
  and owns:</p>

  <ul dir="auto">

  <li>Channel persistence.</li>

  <li>Gallery snapshots.</li>

  <li>Browser live viewer.</li>

  <li>Update manifest and release artifact hosting.</li>

  </ul>

  <h2 dir="auto">License</h2>

  <p dir="auto">MIT. See the project license file for details.</p>'
updated: '2026-06-23T16:25:58Z'
version: v1.1.0
version_title: Polish and New Features v1.1.0
---
