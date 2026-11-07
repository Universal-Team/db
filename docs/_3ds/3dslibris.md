---
author: Rigle
avatar: https://avatars.githubusercontent.com/u/8595185?v=4
categories:
- app
- media
color: '#bfa387'
color_bg: '#806d5a'
created: '2026-03-12T11:06:40Z'
description: An ebook and manga reader for Nintendo 3DS
download_page: https://github.com/RigleGit/3dslibris/releases
downloads:
  3dslibris-debug.3dsx:
    size: 14677016
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.1.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13415360
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.1.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5021452
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.1.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67575045
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.1.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14881180
    size_str: 14 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.1.0/3dslibris.3dsx
  3dslibris.cia:
    size: 13603776
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.1.0/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: other
license_name: Other
llm_generation: 'yes'
qr:
  3dslibris-debug.cia: https://db.universal-team.net/assets/images/qr/3dslibris-debug-cia.png
  3dslibris.cia: https://db.universal-team.net/assets/images/qr/3dslibris-cia.png
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/menu.png
- description: Reading
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/reading.png
source: https://github.com/RigleGit/3dslibris
stars: 184
systems:
- 3DS
title: 3dslibris
unique_ids:
- '0x3D51B'
update_notes: '<h2 dir="auto">3dslibris 3.1.0</h2>

  <p dir="auto">This update focuses on homebrew speed: the library opens faster, books
  load faster, and PDF, CBZ and illustrations now use the 3DS GPU for smooth zoom
  and pan.</p>

  <p dir="auto">It also adds library search and image rotation, and fixes the cut-off
  letters at larger font sizes.</p>

  <p dir="auto">Reminder: update <a href="https://github.com/LumaTeam/Luma3DS/releases">Luma
  to 13.5</a> for the best performance.</p>

  <h3 dir="auto">New</h3>

  <ul dir="auto">

  <li><a href="https://github.com/RigleGit/3dslibris/issues/167" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/167/hovercard">#167</a>: search your
  library. Press <code class="notranslate">Y</code> or choose <code class="notranslate">search</code>
  in general settings to find books and folders by filename, or books by title or
  author.</li>

  <li><a href="https://github.com/RigleGit/3dslibris/issues/170" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/170/hovercard">#170</a>: rotate illustrations
  in EPUB, MOBI and FB2 by 90° with <code class="notranslate">L</code> / <code class="notranslate">R</code>
  or two touch buttons. Zoom and position are kept.</li>

  <li>GPU zoom and pan for PDF, XPS, CBZ and illustrations, with automatic fallback
  to the old renderer if the GPU or memory isn''t available. Works in Wide top-screen
  mode and in all three orientations.</li>

  <li>Progressive PDF zoom and pan: the zoomed page no longer blocks while it renders.
  It appears tile by tile, the overview is drawn after the page, and it also works
  in Wide top-screen mode. Panning at high zoom is about 80% faster on Old 3DS.</li>

  <li><code class="notranslate">preload book data</code> in GENERAL settings: prepares
  covers and book info for the whole library in one go, so browsing is instant afterwards.
  It can be cancelled at any time.</li>

  <li>Opening an EPUB, MOBI or FB2 now shows clear progress, and you can cancel with
  <code class="notranslate">B</code> / <code class="notranslate">START</code>.</li>

  </ul>

  <h3 dir="auto">Fixes and improvements</h3>

  <ul dir="auto">

  <li><a href="https://github.com/RigleGit/3dslibris/issues/172" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/172/hovercard">#172</a>: fix the
  last letter of a word being cut off at larger font sizes (seen at 14), including
  spaces and non-Latin text such as Armenian, Arabic and CJK.</li>

  <li><a href="https://github.com/RigleGit/3dslibris/issues/139" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/139/hovercard">#139</a>: the same
  text-measuring fix helps pages that ended early or lost words at the bottom.</li>

  <li><a href="https://github.com/RigleGit/3dslibris/issues/90" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/90/hovercard">#90</a>: MOBI and FB2
  books open faster and keep a saved page cache, like EPUB.</li>

  <li>Faster startup: about 50% less time before the library appears.</li>

  <li>Faster EPUB opening (about 30–40% less) and page turns (about 80% less in the
  tests I ran). Searching inside a book is also much quicker.</li>

  <li>Reading backwards in a book needs fewer SD card reads.</li>

  <li>Large covers, including high-resolution EPUB covers that were rejected before,
  now load.</li>

  <li>Covers load faster, and books without a cover (FB2) are no longer scanned again
  every time.</li>

  <li>Replacing a book with a different file now shows the new text instead of pages
  from the old one. Changing bold, italic, monospace or fallback fonts also rebuilds
  the pages correctly.</li>

  <li>Your reading position is kept more reliably when changing books, going to a
  page, or changing a setting that re-paginates. A failed open no longer leaves the
  previous book selected.</li>

  <li>Lower memory use with images, PDF and CBZ.</li>

  <li>Fix Old 3DS running out of memory and exiting to the Homebrew Launcher when
  opening very long EPUBs for the first time.</li>

  <li>Fix nested tables, long FB2 titles, library folder backgrounds, duplicated bookmarks
  and custom fonts being forgotten on startup.</li>

  <li>Deleting <code class="notranslate">README.md</code> or <code class="notranslate">QuickStart.txt</code>
  from your library now keeps them gone (hi YouTube).</li>

  <li>Many small speed-ups in book parsing and drawing.</li>

  </ul>

  <h3 dir="auto">Updating</h3>

  <p dir="auto">Reading progress, bookmarks and preferences are kept.</p>

  <p dir="auto">Page caches from earlier versions are rebuilt automatically the first
  time you open each book, so the first open takes as long as before. Pages may break
  slightly differently at larger font sizes. FB2 caches include the original images
  and can use more SD space.</p>

  <p dir="auto">This version needs libctru 2.7.1 or later to build. Latest Luma 13.5
  is recommended for the best performance.</p>

  <p dir="auto">Measurements come from Azahar emulator comparisons and vary by book
  and device.</p>

  <h3 dir="auto">Downloads</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code> or <code class="notranslate">3dslibris.3dsx</code>
  for normal use.</li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code>: runtime files for Homebrew
  Launcher installs; use with the <code class="notranslate">.3dsx</code> download.</li>

  <li>Debug builds (<code class="notranslate">3dslibris-debug.cia</code> / <code class="notranslate">3dslibris-debug.3dsx</code>)
  and <code class="notranslate">3dslibris-source.tar.gz</code> are also included.</li>

  </ul>

  <p dir="auto">Thanks to everyone trying the builds and reporting issues. You can
  support the project with a ⭐ on GitHub or <a href="https://ko-fi.com/rigle" rel="nofollow">a
  coffee</a>.</p>'
updated: '2026-11-07T19:28:44Z'
version: v3.1.0
version_title: v3.1.0
---
### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>3dslibris.3dsx</summary>
<ol>
<li>Download <code>3dslibris.3dsx</code> to <code>/3ds/3dslibris.3dsx</code> on your SD card</li>
<li>Download <code>3dslibris-sdmc.zip</code></li>
<li>Extract <code>/3ds</code> from the zip to <code>/3ds</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>3dslibris.cia</summary>
<ol>
<li>Download <code>3dslibris.cia</code> to <code>/cias/3dslibris.cia</code> on your SD card</li>
<li>Download <code>3dslibris-sdmc.zip</code></li>
<li>Extract <code>/3ds</code> from the zip to <code>/3ds</code> on your SD card</li>
<li>Insert your SD card back into your 3DS and turn it on</li>
<li>Install and delete <code>/cias/3dslibris.cia</code> using FBI or GodMode9</li>
</ol>
</details>

