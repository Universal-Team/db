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
    size: 33936264
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.4/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 27520560
    size_str: 26 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.4/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 64051412
    size_str: 61 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.4/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 33924852
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.4/3dslibris.3dsx
  3dslibris.cia:
    size: 34120640
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.4/3dslibris.cia
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
stars: 60
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.0.4</h2>

  <p dir="auto">This release focuses on stability and orientation correctness. It
  fixes settings persistence breakage caused by XML-invalid filenames, improves <code
  class="notranslate">.cia</code> library discovery by reading books from both SD
  and RomFS, and corrects left-handed reading and library navigation behavior.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>Bookmarks and last-read page persistence fixed</strong>: prefs XML writing
  now escapes attribute values correctly and sanitizes invalid control characters,
  so filenames like <code class="notranslate">... &amp; ...</code> no longer break
  <code class="notranslate">3dslibris.xml</code> parsing on startup.</li>

  <li><strong>CIA library source handling improved</strong>: the app now discovers
  books from both <code class="notranslate">sdmc:/3ds/3dslibris/book</code> and <code
  class="notranslate">romfs:/3ds/3dslibris/book</code>, with SD entries taking priority
  when names overlap.</li>

  <li><strong>Left-handed page screen order corrected</strong>: reflow reading now
  inverts first and second reading screens correctly in left-handed orientation.</li>

  <li><strong>Orientation-relative library D-Pad navigation</strong>: grid navigation
  now follows console orientation in both modes so directional input matches visual
  movement in right-handed and left-handed layouts.</li>

  <li><strong>Startup diagnostics improved</strong>: prefs load failures are now logged
  with an explicit warning instead of failing silently.</li>

  <li><strong>EPUB emphasis compatibility improved</strong>: the parser now recognizes
  bold/italic expressed via common <code class="notranslate">style</code> and <code
  class="notranslate">class</code> CSS patterns, not only semantic tags (<code class="notranslate">&lt;b&gt;/&lt;strong&gt;/&lt;i&gt;/&lt;em&gt;</code>).</li>

  <li><strong>Release pipeline stability improved</strong>: debug MOBI builds now
  include the correct reporter definitions so <code class="notranslate">debug-3dsx</code>
  compiles reliably in CI/release workflows.</li>

  </ul>

  <h3 dir="auto">Architecture and maintainability work included</h3>

  <ul dir="auto">

  <li><strong>App monolith reduced through controller extraction</strong>: startup
  flow, main loop dispatch, status updates, library flow, reader flow, and settings
  flow were split into dedicated controllers so <code class="notranslate">App</code>
  delegates more and owns less direct behavior.</li>

  <li><strong>Controller coupling reduced</strong>: broad <code class="notranslate">friend</code>
  access was removed in favor of explicit <code class="notranslate">App</code> APIs
  for startup, loop, reader runtime state, and presentation steps.</li>

  <li><strong>Library and reader boundaries clarified</strong>: browser warmup/job
  flow and reader open/deferred-relayout paths were moved behind controller-driven
  entry points with less direct cross-module state access.</li>

  <li><strong><code class="notranslate">book_io.cpp</code> kept as a thin dispatcher</strong>:
  parser-heavy logic was extracted into dedicated modules (plain-text, XML, and MOBI
  submodules), reducing central parser coupling and making future format changes safer.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-03T23:19:39Z'
version: v2.0.4
version_title: v2.0.4
---
