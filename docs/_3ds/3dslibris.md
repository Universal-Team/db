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
    size: 39122112
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.2/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 32745218
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.2/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66524014
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.2/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39099872
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.2/3dslibris.3dsx
  3dslibris.cia:
    size: 39330752
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.2/3dslibris.cia
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
update_notes: '<h2 dir="auto">3dslibris 2.1.2</h2>

  <p dir="auto">Patch release fixing cover-load gaps in the library browser and a
  use-after-free crash on exit.</p>

  <h3 dir="auto">Fix</h3>

  <ul dir="auto">

  <li><strong>Cover-load gaps fixed</strong>: all visible books now have their covers
  queued for extraction on each warmup tick, not just the selected one. The retry
  counter is no longer incremented on metadata-index failures (only on actual cover-extraction
  failures), so transient index misses no longer permanently blacklist a book''s cover.
  The attempt limit was raised from 2 to 3 to give marginal cases one extra pass.</li>

  <li><strong>Use-after-free crash on exit fixed</strong>: the <code class="notranslate">App</code>
  destructor now deletes <code class="notranslate">Book</code> objects before releasing
  <code class="notranslate">Prefs</code> and the touchscreen handle (<code class="notranslate">ts</code>).
  Previously, <code class="notranslate">Book</code> destructors ran after <code class="notranslate">Prefs</code>/<code
  class="notranslate">ts</code> were freed, producing a Luma3DS fault dump with FAR=0xE7E7996B.
  A <code class="notranslate">Button*</code> leak in the destructor is also plugged.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-10T14:58:55Z'
version: v2.1.2
version_title: v2.1.2
---
