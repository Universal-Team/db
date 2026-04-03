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
    size: 33897456
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.3/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 27501274
    size_str: 26 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.3/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 101825550
    size_str: 97 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.3/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 33884704
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.3/3dslibris.3dsx
  3dslibris.cia:
    size: 34079680
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.3/3dslibris.cia
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
stars: 55
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.0.3</h2>

  <p dir="auto">This release fixes the remaining <code class="notranslate">.cia</code>
  runtime and packaging issues so the installable build now behaves correctly on real
  hardware and in Azahar. The focus is startup robustness, bundled runtime data, and
  clear fatal-screen behavior when no books are present.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>Fixed bundled RomFS for <code class="notranslate">.cia</code> builds</strong>
  — the installable build now actually includes its bundled fonts and UI resources,
  instead of staging them locally but omitting them from the final CIA package.</li>

  <li><strong>Fixed the CIA-only startup crash</strong> — a null cache entry in the
  text/font teardown path could trigger an ARM11 data abort during early startup failure;
  font initialization and cache cleanup are now hardened.</li>

  <li><strong>Better runtime asset fallback</strong> — bundled fonts and resources
  are resolved safely between SD and <code class="notranslate">RomFS</code>, so <code
  class="notranslate">.cia</code> installs no longer depend on a manual <code class="notranslate">font/</code>
  or <code class="notranslate">resources/</code> copy to boot.</li>

  <li><strong>Stable fatal boot screens</strong> — missing-book and startup error
  screens no longer flicker between old and new frames while waiting for <code class="notranslate">START</code>.</li>

  <li><strong>Clearer first-run behavior</strong> — if no books are present, the app
  now shows a stable message telling you to copy your <code class="notranslate">EPUB</code>,
  <code class="notranslate">FB2</code>, <code class="notranslate">TXT</code>, <code
  class="notranslate">RTF</code>, or <code class="notranslate">ODT</code> files into
  <code class="notranslate">sdmc:/3ds/3dslibris/book</code>.</li>

  <li><strong>CIA build validation added to CI</strong> — GitHub Actions now builds
  and verifies the <code class="notranslate">.cia</code> path as well, including checks
  that the staged <code class="notranslate">RomFS</code> contains the bundled runtime
  files.</li>

  </ul>

  <h3 dir="auto">Included reader functionality</h3>

  <p dir="auto"><code class="notranslate">v2.0.3</code> keeps the full reader feature
  set from the <code class="notranslate">2.0.x</code> line, including:</p>

  <ul dir="auto">

  <li>MuPDF-backed <code class="notranslate">PDF</code>, <code class="notranslate">CBZ</code>,
  and <code class="notranslate">XPS</code> support</li>

  <li>progressive fixed-layout rendering</li>

  <li>asynchronous/deferred <code class="notranslate">MOBI</code> open on New 3DS</li>

  <li>generated library cover thumbnails</li>

  <li>bundled runtime assets for <code class="notranslate">.cia</code> installs</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-01T19:59:36Z'
version: v2.0.3
version_title: v2.0.3
---
