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
    size: 39121736
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.1/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 32745232
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.1/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66526475
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.1/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39099496
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.1/3dslibris.3dsx
  3dslibris.cia:
    size: 39330752
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.1/3dslibris.cia
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
update_notes: '<h2 dir="auto">3dslibris 2.1.1</h2>

  <p dir="auto">Patch release restoring page-turn performance to pre-2.1.0 levels.</p>

  <h3 dir="auto">Fix</h3>

  <ul dir="auto">

  <li><strong>Page-turn speed restored</strong>: page rendering was ~10× slower than
  2.0.4 due to a glyph cache regression introduced alongside the CJK/RTL fallback
  font support in 2.1.0. The glyph cache was effectively bypassed on every character
  because the ghost-glyph detection path called <code class="notranslate">FT_Load_Char</code>
  unconditionally, even when the glyph was already cached. This is fixed by checking
  the cache first and restricting the ghost-glyph check to the Arabic Presentation
  Forms block (U+FE70–U+FEFF) where it is actually needed.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-10T07:38:52Z'
version: v2.1.1
version_title: v2.1.1
---
