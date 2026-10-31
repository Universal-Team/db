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
    size: 14485464
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.0.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13292480
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.0.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5021175
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.0.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67312089
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.0.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14600912
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.0.0/3dslibris.3dsx
  3dslibris.cia:
    size: 13423552
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.0.0/3dslibris.cia
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
stars: 179
systems:
- 3DS
title: 3dslibris
unique_ids:
- '0x3D51B'
update_notes: '<h2 dir="auto">3dslibris 3.0.0</h2>

  <p dir="auto">It has been a while, but now you can search your books and zoom in
  on images!</p>

  <p dir="auto">This release also includes many fixes and improvements, including
  better support for CJK text, landscape orientation and handedness controls, and
  more.</p>

  <h3 dir="auto">New</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5646639228"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/163"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/163/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/163">#163</a>: find words and
  phrases with the 3DS keyboard, highlight matches and move between results. Available
  in EPUB, MOBI, TXT, Markdown, FB2, RTF and ODT through the BOOK menu.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4219533406"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/28"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/28/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/28">#28</a>: zoom and pan illustrations
  in EPUB, MOBI and FB2. Hold Y to select an image, then press A to open it. Includes
  touch controls and returns to your reading position.</li>

  <li><a href="https://github.com/RigleGit/3dslibris/issues/101" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/101/hovercard">#101</a>: optional
  800×240 top-screen mode for PDF, CBZ and XPS through <code class="notranslate">wide
  top screen</code> in the BOOK menu. Available on Old/New 3DS (including XL) and
  New 2DS XL; the original 2DS stays at 400×240.</li>

  <li>Optional <code class="notranslate">disable ebook images</code> setting under
  <code class="notranslate">style customization</code> (I also read YT comment hehe).</li>

  </ul>

  <h3 dir="auto">Fixes and improvements</h3>

  <ul dir="auto">

  <li>Faster library browsing and EPUB page turns, smoother PDF panning and quicker
  app shutdown.</li>

  <li>Open PDFs fitted to the whole page and improve PDF/CBZ image scaling.</li>

  <li>EPUB books show the first page before the page cache finishes saving.</li>

  <li>Fix overlapping full-page images and preserve authored image sizes across reading
  screens.</li>

  <li>Correct orientation and handedness controls, landscape buttons, loading screens
  and partial redraws (I didn''t try these for a while and some things were broken).</li>

  <li>Show two lines for library titles and load folder covers only when visible and
  idle.</li>

  <li>Fix a CJK pagination stack overflow (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5793889435" data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/165"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/165/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/165">#165</a>), parsing errors,
  image-loading limits and invalid page-cache handling.</li>

  </ul>

  <h3 dir="auto">Updating</h3>

  <p dir="auto">EPUB and MOBI page caches are rebuilt on first open after updating.
  Reading progress, bookmarks and preferences are kept. If you close the app while
  an EPUB cache is still being prepared, it may need rebuilding on the next open.
  Returning to the library finishes the pending save.</p>

  <p dir="auto">Search does not support PDF/CBZ/XPS, OCR or RTL text. See the <a href="https://github.com/RigleGit/3dslibris/blob/main/docs/BOOK_SEARCH.md">search
  guide</a> and <a href="https://github.com/RigleGit/3dslibris/blob/main/docs/IMAGE_VIEWER.md">image
  controls</a> for details.</p>

  <h3 dir="auto">Downloads</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code> or <code class="notranslate">3dslibris.3dsx</code>
  for normal use.</li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code>: runtime files for Homebrew
  Launcher installs; use with the <code class="notranslate">.3dsx</code> download.</li>

  <li>Debug builds (<code class="notranslate">3dslibris-debug.cia</code> / <code class="notranslate">3dslibris-debug.3dsx</code>)
  and <code class="notranslate">3dslibris-source.tar.gz</code> are also included.</li>

  </ul>

  <p dir="auto">Thanks to everyone reporting issues and supporting the project. Special
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Rhlp-Engineering/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Rhlp-Engineering">@Rhlp-Engineering</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Leblatar/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Leblatar">@Leblatar</a>
  for supporting this version! You can help with a ⭐ on GitHub or <a href="https://ko-fi.com/rigle"
  rel="nofollow">a coffee</a>.</p>'
updated: '2026-10-27T14:37:09Z'
version: v3.0.0
version_title: v3.0.0
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

