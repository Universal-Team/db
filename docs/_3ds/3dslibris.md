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
    size: 39035020
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.1/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39265216
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.1/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32796556
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.1/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67914826
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.1/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39122708
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.1/3dslibris.3dsx
  3dslibris.cia:
    size: 39355328
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.1/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: other
license_name: Other
qr:
  3dslibris-debug.cia: https://db.universal-team.net/assets/images/qr/3dslibris-debug-cia.png
  3dslibris.cia: https://db.universal-team.net/assets/images/qr/3dslibris-cia.png
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/menu.png
- description: Reading
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/reading.png
source: https://github.com/RigleGit/3dslibris
stars: 91
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.4.1</h2>

  <p dir="auto">Crash-at-boot fix.</p>

  <h3 dir="auto">Fix</h3>

  <ul dir="auto">

  <li><strong>Crash on launch</strong>: <code class="notranslate">FontMenu</code>
  is constructed during <code class="notranslate">App::App()</code> before fonts are
  loaded (<code class="notranslate">FontManager</code> is still null). Calling <code
  class="notranslate">GetHeight()</code> and <code class="notranslate">GetAdvance()</code>
  through the null pointer cascaded into a heap Data Abort immediately at startup.
  Both methods now return safe defaults (<code class="notranslate">PIXELSIZE</code>
  / <code class="notranslate">0</code>) until the font manager is initialised.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-22T08:38:02Z'
version: v2.4.1
version_title: v2.4.1
---
