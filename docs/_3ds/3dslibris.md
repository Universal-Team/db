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
    size: 33895632
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.1/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 27497291
    size_str: 26 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.1/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 101821368
    size_str: 97 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.1/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 33882920
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.1/3dslibris.3dsx
  3dslibris.cia:
    size: 27628480
    size_str: 26 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.1/3dslibris.cia
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
stars: 42
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.0.1</h2>

  <p dir="auto">This release republishes the real post-<code class="notranslate">2.0.0</code>
  branch state as a clean public tag. The functional reader improvements from the
  <code class="notranslate">2.0.0</code> line remain intact, but <code class="notranslate">2.0.1</code>
  is the first tag that matches the full codebase as it exists after the later cleanup,
  path centralization, test refactors, and repository reorganization work.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>Full branch catch-up release</strong> — <code class="notranslate">v2.0.1</code>
  includes the missing commits that were finished after the original <code class="notranslate">v2.0.0</code>
  tag, so the public release now matches the maintained <code class="notranslate">main</code>
  line.</li>

  <li><strong>Centralized runtime paths</strong> — SD, cache, and related filesystem
  paths now live in a shared path layer instead of being duplicated across subsystems.</li>

  <li><strong>Cleaner repo structure</strong> — shared helpers were reorganized, legacy
  duplicate files were removed after the move, and bundled <code class="notranslate">expat</code>
  sources now live under <code class="notranslate">third_party/</code>.</li>

  <li><strong>MOBI cache code split out cleanly</strong> — page-cache serialization
  and invalidation logic now live in a dedicated MOBI cache module instead of being
  embedded in the larger common book I/O unit.</li>

  <li><strong>Improved native test ergonomics</strong> — the text-layout and Unicode
  tests now reuse a shared native build helper instead of each script compiling the
  same dependency objects manually.</li>

  <li><strong>Expanded technical documentation</strong> — the repository now includes
  architecture notes plus local NDS/3DS hardware reference material derived from GBATek
  for future maintenance work.</li>

  </ul>

  <h3 dir="auto">Included reader functionality</h3>

  <p dir="auto"><code class="notranslate">v2.0.1</code> still includes all user-facing
  work shipped in the <code class="notranslate">v2.0.0</code> line:</p>

  <ul dir="auto">

  <li>MuPDF-backed <code class="notranslate">PDF</code>, <code class="notranslate">CBZ</code>,
  and <code class="notranslate">XPS</code> support</li>

  <li>progressive fixed-layout rendering with preview-first display</li>

  <li>asynchronous/deferred <code class="notranslate">MOBI</code> open on New 3DS</li>

  <li>generated library cover thumbnails for <code class="notranslate">EPUB</code>,
  <code class="notranslate">FB2</code>, <code class="notranslate">MOBI</code>, <code
  class="notranslate">PDF</code>, and <code class="notranslate">CBZ</code></li>

  <li>bundled runtime assets for <code class="notranslate">.cia</code> installs</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  </ul>'
updated: '2026-04-01T14:08:56Z'
version: v2.0.1
version_title: v2.0.1
---
