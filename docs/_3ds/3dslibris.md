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
    size: 38960560
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.2/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39195584
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.2/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32712163
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.2/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66614967
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.2/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39017180
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.2/3dslibris.3dsx
  3dslibris.cia:
    size: 39248832
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.3.2/3dslibris.cia
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
update_notes: '<h2 dir="auto">3dslibris 2.3.2</h2>

  <p dir="auto"><strong>Quality-of-life patch on top of the <code class="notranslate">v2.3.1</code>
  stable conservative base.</strong> No workers have been re-enabled; all background
  processing remains on the main thread. This release restores MOBI features that
  were silently disabled in <code class="notranslate">v2.3.1</code>, fixes a cover-loading
  gap in the browser, and improves EPUB cover decoding for large and SVG covers.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>MOBI structured TOC restored</strong>: the <code class="notranslate">html_to_text</code>
  position map is now built during safe-extractor parsing. Structured TOC entries
  (e.g. "CHAPTER 1", "PART TWO") are resolved to accurate page numbers instead of
  falling back to linear estimation.</li>

  <li><strong>MOBI inline images restored</strong>: images embedded in MOBI HTML (<code
  class="notranslate">&lt;img recindex=...&gt;</code>) are now registered and rendered
  in the reading view. Previously the safe extractor wired up no callbacks and all
  inline images were silently dropped.</li>

  <li><strong>MOBI page cache re-enabled</strong>: the second open of a large MOBI
  (e.g. <em>A Promised Land</em>, 1365 pages) now loads from cache in ~3.7 s instead
  of re-parsing for ~9 s.</li>

  <li><strong>Browser grid covers load on view toggle</strong>: switching from list
  to grid view now immediately loads covers for the visible page. Previously the grid
  showed empty slots until the next navigation event.</li>

  <li><strong>EPUB large PNG covers decode via libpng</strong>: covers larger than
  4 MB decoded no longer go through <code class="notranslate">stb_image</code>''s
  full RGB decode. A direct libpng thumbnail path scales to <code class="notranslate">85×115</code>
  while keeping peak memory low.</li>

  <li><strong>EPUB SVG covers rendered via MuPDF</strong>: SVG cover images are rasterized
  at thumbnail size using the MuPDF fitz renderer instead of being skipped or incorrectly
  decoded.</li>

  </ul>

  <h3 dir="auto">Fixes and behavior changes</h3>

  <ul dir="auto">

  <li><code class="notranslate">mobi_safe_markup_extract::ExtractToText</code> now
  accepts and populates an <code class="notranslate">html_to_text_map</code> parameter,
  sampled at the same intervals as the main extractor. <code class="notranslate">mobi_toc_finalize_policy::ShouldApplyStructuredToc</code>
  gates on whether the map is usable.</li>

  <li><code class="notranslate">mobi_book_hooks::ExtractMobiMarkupToText</code> wires
  up <code class="notranslate">InlineImageCallbacks</code> (via <code class="notranslate">book-&gt;RegisterInlineImage</code>)
  and passes the map pointer through to the extractor.</li>

  <li><code class="notranslate">ToggleBrowserViewSetting</code> in <code class="notranslate">app_prefs.cpp</code>
  now calls <code class="notranslate">LoadVisibleBrowserCoverCaches()</code> after
  marking the browser dirty, so the first grid page is populated immediately.</li>

  <li><code class="notranslate">App::LoadVisibleBrowserCoverCaches()</code> moved
  to the public section of <code class="notranslate">App</code> so it can be called
  from settings code.</li>

  <li><code class="notranslate">epub_cover::Extract</code> tries a libpng thumbnail
  path for large PNG covers before falling back to <code class="notranslate">stb_image</code>.
  On failure the stb_image path is still attempted.</li>

  <li><code class="notranslate">epub_cover::Extract</code> renders SVG covers via
  a new <code class="notranslate">RenderSvgCoverThumbnail</code> function using <code
  class="notranslate">fz_open_document_with_buffer</code> / <code class="notranslate">fz_run_page</code>
  at thumbnail scale, converting the resulting pixmap to RGB565.</li>

  </ul>

  <h3 dir="auto">What comes next</h3>

  <p dir="auto">Workers will be re-enabled one at a time as each is confirmed stable
  on hardware: reflow worker (EPUB/FB2/MOBI), then CBZ interactive preload, then PDF
  strip worker, then browser warmup.</p>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-20T19:42:40Z'
version: v2.3.2
version_title: v2.3.2
---
