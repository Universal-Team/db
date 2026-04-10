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
    size: 39123276
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.3/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 32747527
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.3/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66525296
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.3/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39101028
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.3/3dslibris.3dsx
  3dslibris.cia:
    size: 39330752
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.3/3dslibris.cia
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
stars: 73
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.1.3</h2>

  <p dir="auto">Patch release fixing a crash on startup when an FB2 book was saved
  as the last opened book.</p>

  <h3 dir="auto">Fix</h3>

  <ul dir="auto">

  <li><strong>FB2 reopen crash on boot fixed</strong>: when <code class="notranslate">current=&lt;book&gt;.fb2</code>
  was persisted in prefs, the app crashed during boot. Root cause was a FreeType race
  condition: the reflow worker (core 1) called <code class="notranslate">ts-&gt;GetAdvance</code>
  inside XML parse callbacks while the main thread (core 0) simultaneously called
  <code class="notranslate">ts-&gt;GetStringWidth</code> / <code class="notranslate">ts-&gt;PrintString</code>
  in the opening-mode status bar. FreeType is not thread-safe. The fix defers <code
  class="notranslate">OpenBook()</code> from the boot sequence to the first tick of
  the main loop, ensuring the reopen worker is never launched before the main loop
  is running — matching the timing of a user-initiated open and eliminating the race.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-10T16:11:45Z'
version: v2.1.3
version_title: v2.1.3
---
