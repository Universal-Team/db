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
    size: 38876736
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.1/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39109568
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.1/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32664864
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.1/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66604452
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.1/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 38932180
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.1/3dslibris.3dsx
  3dslibris.cia:
    size: 39166912
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.1/3dslibris.cia
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
stars: 89
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.3.1</h2>

  <p dir="auto"><strong>Stable release — all background workers disabled.</strong>
  This release trades some speed for confirmed reliability on real hardware. All async/deferred
  rendering and parsing workers are turned off unconditionally; everything runs on
  the main thread. From here, each previously-problematic area will be re-enabled
  one at a time as it is proven safe, rather than all at once.</p>

  <p dir="auto">This patch is a stability-focused follow-up to <code class="notranslate">v2.3.0</code>,
  aimed at the real-hardware regressions reported after the menu and navigation changes
  in that release. The main goal of <code class="notranslate">v2.3.1</code> is to
  make book opening, switching, covers, and fixed-layout rendering behave reliably
  again on both <code class="notranslate">.3dsx</code> and <code class="notranslate">.cia</code>,
  especially on <code class="notranslate">new3DS</code>.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>All background workers disabled for this release</strong>: fixed-layout
  rendering (PDF, CBZ), MOBI finalization, and browser warmup all run synchronously
  on the main thread. The app will feel slightly slower to open large books or navigate
  zoom levels, but will not crash or hang from worker/heap interactions.</li>

  <li><strong>Reading direction toggle for fixed-layout documents</strong>: PDF, CBZ,
  and XPS now have a per-book <code class="notranslate">reading direction</code> toggle
  in <code class="notranslate">BOOK</code> settings. Switch between <code class="notranslate">Left
  to right</code> (default, western) and <code class="notranslate">Right to left</code>
  (manga, Arabic, Hebrew) — page turn direction and viewport navigation flip accordingly.</li>

  <li><strong>Book opening and switching are much harder to break</strong>: stale
  open sessions are gated more carefully, browser-side background work is paused at
  the right time, and the transition from one book to another no longer relies on
  timing-sensitive state.</li>

  <li><strong>Browser and cover behavior are more stable on hardware</strong>: the
  library no longer corrupts selected-title rendering while warming metadata, and
  entering a book no longer leaves behind browser artifacts in the reading view.</li>

  <li><strong>PDF and CBZ now render at zoom-correct resolution</strong>: in synchronous
  mode the interactive tile is rendered immediately after the preview, so zoomed-in
  content is sharp rather than upscaled from the preview bitmap.</li>

  <li><strong>MOBI crash on reopen is fixed</strong>: a large contiguous heap reservation
  during text merging could <code class="notranslate">std::terminate</code> on a fragmented
  3DS heap after a prior book close. The reservation is removed; the string now grows
  incrementally.</li>

  </ul>

  <h3 dir="auto">Included fixes and behavior changes</h3>

  <ul dir="auto">

  <li><strong>Conservative runtime mode</strong>: all <code class="notranslate">debug_runtime::Force*</code>
  flags return <code class="notranslate">true</code> unconditionally in both debug
  and release builds. Background workers, deferred render pumps, and browser warmup
  are all bypassed. This is the foundational change for <code class="notranslate">v2.3.1</code>
  stability.</li>

  <li><strong>PDF/CBZ interactive render in sync mode</strong>: after the preview
  bitmap is ready, the zoom-aware interactive tile is rendered immediately on the
  main thread. Zoom changes clear the tile cache so the next draw re-renders at the
  correct resolution. Strip worker no longer reloads the page on each strip — bounds
  and scale are captured once at render start.</li>

  <li><strong>MOBI <code class="notranslate">reserve()</code> removed from text merge</strong>:
  <code class="notranslate">BuildMergedText</code> no longer calls <code class="notranslate">reserve(text_len)</code>
  upfront. The prior 1.8 MB contiguous reservation could fail on a fragmented heap
  and crash via <code class="notranslate">std::terminate</code>. Incremental growth
  is safe.</li>

  <li><strong>MOBI page cache save skipped in conservative mode</strong>: writing
  a cache built under the synchronous path would produce stale or mismatched data;
  the save is now skipped when <code class="notranslate">ForceSynchronousMobiFinalize</code>
  is true.</li>

  <li><strong>EPUB inline image metadata retried on zip open failure</strong>: if
  <code class="notranslate">unzOpen</code> fails due to transient memory pressure,
  <code class="notranslate">metadata_probed</code> is left false so the next frame
  retries. Previously a failed open would permanently mark the image as unloadable.</li>

  <li><strong>Book vector capacity released on close</strong>: <code class="notranslate">pages</code>
  and <code class="notranslate">chapters</code> vectors now swap with an empty vector
  on <code class="notranslate">Book::Close()</code>, actually freeing capacity rather
  than just clearing size.</li>

  <li><strong>Opening a book is cancellable and session-safe</strong>: <code class="notranslate">opening
  book ...</code> can now be cancelled with <code class="notranslate">B</code>, <code
  class="notranslate">Start</code>, or <code class="notranslate">Select</code>, and
  switching from one book to another no longer depends on stale callbacks or unfinished
  work from the previous session.</li>

  <li><strong>Library warmup is better behaved</strong>: list-view metadata/title
  warmup no longer stalls after only a few entries, and gallery-view marquee/title
  rendering is less prone to corruption while the browser is still active.</li>

  <li><strong>EPUB parsing is more robust against real-world files</strong>: better
  named-entity coverage, improved TOC fallback behavior, and safer page-cache handling
  during interrupted opens and closes.</li>

  <li><strong>MOBI tradeoffs are explicit in this patch</strong>: inline MOBI images
  and the structured TOC/index may be unavailable when the HTML-to-text position map
  cannot be trusted. This is an intentional stability tradeoff for <code class="notranslate">v2.3.1</code>,
  not a silent regression.</li>

  <li><strong>Reader entry/exit is cleaner overall</strong>: when a book finally opens,
  the reading screens are less likely to inherit leftover browser drawing state from
  the previous mode.</li>

  </ul>

  <h3 dir="auto">What comes next</h3>

  <p dir="auto">Workers will be re-enabled one format at a time as each is verified
  stable: CBZ interactive preload, then PDF strip worker, then MOBI deferred finalize,
  then browser warmup. Each re-enablement will ship as a patch or minor release once
  confirmed on hardware.</p>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-20T18:46:05Z'
version: v2.3.1
version_title: v2.3.1
---
