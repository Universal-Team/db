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
    size: 39125564
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.4/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 32747284
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.4/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66522805
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.4/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39100876
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.4/3dslibris.3dsx
  3dslibris.cia:
    size: 39330752
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.4/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: other
license_name: Other
qr:
  3dslibris.cia: https://db.universal-team.net/assets/images/qr/3dslibris-cia.png
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/menu.png
- description: Reading
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/reading.png
source: https://github.com/RigleGit/3dslibris
stars: 77
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.1.4</h2>

  <p dir="auto">Small patch release for fixed-layout safety, lower stack usage during
  title-page detection, and broader debug instrumentation.</p>

  <h3 dir="auto">Fix</h3>

  <ul dir="auto">

  <li><strong>Heap-based parsing state</strong>: move <code class="notranslate">State</code>
  off the stack to avoid stack overflow on 3DS-sized stacks when opening heavier books.</li>

  <li><strong>Fixed-layout title-page guard</strong>: skip approximate title-page
  search for fixed-layout books such as <code class="notranslate">PDF</code> and <code
  class="notranslate">CBZ</code>, where text-page heuristics do not apply.</li>

  <li><strong>Extra debug coverage</strong>: expand <code class="notranslate">DSLIBRIS_DEBUG</code>
  logging across app lifecycle, main loop memory reporting, reflow worker shutdown,
  browser input, and cover-cache corruption paths to make field diagnosis easier without
  changing release-build behavior.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-11T09:31:59Z'
version: v2.1.4
version_title: v2.1.4
---
