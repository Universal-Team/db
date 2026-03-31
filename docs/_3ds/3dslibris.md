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
    size: 33894092
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.0/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 27498563
    size_str: 26 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 100639651
    size_str: 95 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 33881340
    size_str: 32 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.0/3dslibris.3dsx
  3dslibris.cia:
    size: 27627456
    size_str: 26 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.0.0/3dslibris.cia
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
update_notes: '<h2 dir="auto">3dslibris 2.0.0</h2>

  <p dir="auto">This release rolls up the full reader evolution since the 1.1.0 line
  into a broader fixed-layout and reflow upgrade. The headline change is that 3dslibris
  is no longer just a reflowable-book reader: it now has a MuPDF-backed fixed-layout
  stack for PDF-class documents while also substantially improving MOBI, EPUB, FB2,
  packaging, and runtime stability.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>PDF, CBZ, and XPS reading</strong> — open PDF documents, comic books
  (CBZ), and XPS files with zoom, full-page preview on the bottom screen, and outline
  navigation when available.</li>

  <li><strong>Progressive page loading</strong> — you see a preview of the page immediately,
  then it refines to full quality in the background. No more waiting for a page to
  fully render before you can interact.</li>

  <li><strong>Faster on New 3DS</strong> — page rendering for PDF and CBZ runs on
  a separate processor core, keeping the UI responsive. Old 3DS still works with automatic
  fallback.</li>

  <li><strong>MOBI books open without freezing the UI</strong> on New 3DS thanks to
  asynchronous processing — you can start reading while the rest of the book finishes
  loading in the background.</li>

  <li><strong>Library covers now work for every format</strong> — EPUB, FB2, MOBI,
  PDF, and CBZ all show actual page thumbnails instead of placeholders.</li>

  <li><strong>All 1.1.x improvements included</strong> — inline images in MOBI and
  EPUB, faster image-heavy books, better text rendering, and more accurate MOBI table
  of contents.</li>

  <li><strong>No more manual SD card setup for <code class="notranslate">.cia</code>
  installs</strong> — fonts and UI resources are built in.</li>

  <li><strong>More stable startup</strong> — problematic MOBI files no longer cause
  crashes, and the app stays on a clear error screen instead of flickering between
  states when something goes wrong.</li>

  </ul>

  <h3 dir="auto">Extended details</h3>

  <p dir="auto"><strong>Fixed-layout stack (PDF / CBZ / XPS)</strong></p>

  <ul dir="auto">

  <li>Adds MuPDF-backed PDF reading with zoomed top-screen viewing, full-page preview
  on the bottom screen, outline navigation when available, and touch-controlled viewport
  movement.</li>

  <li>Extends that fixed-layout stack to CBZ and XPS, reusing the same rendering core
  and viewer workflow instead of maintaining separate one-off readers.</li>

  <li>Introduces a progressive fixed-layout rendering pipeline: preview first, interactive
  cache next, then full-page refinement in the background instead of a single blocking
  render.</li>

  <li>Adds progressive strip rendering for zoomed fixed-layout pages, with strips
  composited on screen as they complete.</li>

  <li>Uses a dedicated fixed-layout worker thread on the New Nintendo 3DS extra core
  when available, while keeping an automatic synchronous fallback path for Old 3DS
  hardware.</li>

  <li>Improves fixed-layout cache behavior by stabilizing preview viewport updates,
  accelerating cache reuse, and deferring expensive prefetch work until page turns
  or idle periods.</li>

  <li>Fixed-layout reader controls are now documented consistently for PDF, CBZ, and
  XPS: <code class="notranslate">A/B</code> zoom, <code class="notranslate">Left/Right</code>
  turn pages, <code class="notranslate">Up/Down</code> jump outline entries when available,
  touch moves the viewport, and <code class="notranslate">START/SELECT</code> return
  to the library or open settings.</li>

  <li>Tightens PDF-enabled release documentation and licensing notes for MuPDF-based
  builds, including corresponding-source guidance for public release packaging.</li>

  </ul>

  <p dir="auto"><strong>MOBI &amp; deferred open</strong></p>

  <ul dir="auto">

  <li>MOBI opening on New 3DS now uses asynchronous reflow, which removes the old
  long blocking open path from the UI while keeping Old 3DS on the synchronous fallback.</li>

  <li>Large MOBI books now complete deferred TOC work much faster by reusing structured
  TOC data and avoiding redundant metadata rebuilds.</li>

  <li>MOBI parsing and deferred reflow were reworked so large books spend less time
  in the slow path during open, with finer-grained timings available in debug builds.</li>

  <li>The deferred-open path is now much cleaner on real hardware: EPUB page-cache
  writes are pushed out of the async-open critical path, buffered status logging avoids
  per-line file reopen overhead, and deferred MOBI finalize work no longer floods
  debug output while background pagination runs.</li>

  </ul>

  <p dir="auto"><strong>Library covers &amp; browser</strong></p>

  <ul dir="auto">

  <li>Library cover generation is now a first-class runtime feature rather than a
  best-effort side effect: visible-page thumbs are cached and reused, the selected
  book gets warmup priority after short idle, and generated covers now work across
  EPUB, FB2, MOBI, PDF, and CBZ.</li>

  <li>PDF and CBZ library thumbs now come from the first page, which makes the fixed-layout
  formats feel integrated with the rest of the library instead of showing generic
  placeholders.</li>

  <li>Browser and fixed-layout drawing now track dirty regions more precisely and
  reuse cached physical framebuffers, which cuts redraw cost and fixes the regression
  where valid freshly generated cover thumbs could exist in RAM and cache but still
  fail to appear on screen.</li>

  </ul>

  <p dir="auto"><strong>Text &amp; layout</strong></p>

  <ul dir="auto">

  <li>EPUB and FB2 now share better text-layout instrumentation and a combined break/measure
  helper in the common layout layer, improving visibility into shaping and line-break
  cost in real books.</li>

  <li>The text engine improvements introduced around the 1.1.0 line remain part of
  this release: stronger Unicode-aware text runs, better line breaking, safer text-size
  clamping, and more resilient page-buffer handling continue to benefit EPUB, FB2,
  and other reflowable formats.</li>

  <li>MOBI support also keeps the 1.1.x improvements to inline images, safer cover
  extraction, more correct record decoding, and the legacy plain-text wrapping behavior
  that works better on real books.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  </ul>'
updated: '2026-03-31T18:04:54Z'
version: v2.0.0
version_title: v2.0.0
---
