---
author: Rigle
avatar: https://avatars.githubusercontent.com/u/8595185?v=4
categories:
- app
color: '#bfa387'
color_bg: '#806d5a'
created: '2026-03-12T11:06:40Z'
description: An ebook and manga reader for Nintendo 3DS
download_page: https://github.com/RigleGit/3dslibris/releases
downloads:
  3dslibris-debug.3dsx:
    size: 14398476
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13145024
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66974464
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14527628
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.0/3dslibris.3dsx
  3dslibris.cia:
    size: 13280192
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.0/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: other
license_name: Other
llm_usage: undisclosed
qr:
  3dslibris-debug.cia: https://db.universal-team.net/assets/images/qr/3dslibris-debug-cia.png
  3dslibris.cia: https://db.universal-team.net/assets/images/qr/3dslibris-cia.png
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/menu.png
- description: Reading
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/reading.png
source: https://github.com/RigleGit/3dslibris
stars: 128
systems:
- 3DS
title: 3dslibris
unique_ids:
- '0x3D51B'
update_notes: '<h2 dir="auto">3dslibris 2.8.0</h2>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/b20a5a5c-1a6f-4581-aae0-cdbb015a9111"><img
  width="600" alt="imagen" src="https://github.com/user-attachments/assets/b20a5a5c-1a6f-4581-aae0-cdbb015a9111"
  style="max-width: 100%;"></a>

  <p dir="auto">True landscape reading, safer GIF decoding, reorganized reading controls,
  and fixed-layout viewport corrections.</p>

  <h3 dir="auto">New Features</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4377615718"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/92"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/92/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/92">#92</a> Added true horizontal
  reading mode for reflowable books, PDF, and CBZ, with orientation-specific rendering
  across both screens.</li>

  <li>Split <strong>reading orientation</strong> (Horizontal/Vertical) from <strong>handedness</strong>
  (Left-handed/Right-handed), with both settings persisted independently.</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Moved reading orientation and handedness to the second settings page in both
  global and per-book settings. PDF/CBZ reading direction is available there as a
  separate option.</li>

  <li>Updated reflowable pagination, text wrapping, inline images, progress information,
  rules, links, and touch zones to use the real geometry of each landscape screen.</li>

  <li>Updated PDF/CBZ decoding, preview caches, workers, and rendering to follow the
  active orientation dimensions.</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604526454"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/142"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/142/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/142">#142</a>: fixed GIF pages
  and EPUB images freezing or crashing on 3DS by moving GIF decoder state off the
  thread stack and decoding the first frame safely.</li>

  </ul>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">Thanks to everyone who tested the landscape builds, shared screenshots
  and logs, and reported the GIF crash on hardware!</p>

  <ul dir="auto">

  <li><strong>Fueling the Code:</strong> A special thank you to my <strong>Ko-fi supporters</strong>.
  Your donations help keep the project going and keep me caffeinated!</li>

  </ul>

  <p dir="auto"><em>Want to support the project? Consider leaving a ⭐ on GitHub or
  <a href="https://ko-fi.com/rigle" rel="nofollow">buying me a coffee</a>!</em></p>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code> (runtime files only; pair
  it with the <code class="notranslate">.3dsx</code> asset for Homebrew Launcher installs)</li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-06-11T17:32:48Z'
version: v2.8.0
version_title: v2.8.0
---
