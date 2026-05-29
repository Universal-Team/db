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
    size: 14370608
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.3/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13128640
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.3/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.3/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66950520
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.3/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14492672
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.3/3dslibris.3dsx
  3dslibris.cia:
    size: 13259712
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.3/3dslibris.cia
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
stars: 121
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.7.3</h2>

  <p dir="auto">Quality-of-life update for in-reader visibility and settings flow.</p>

  <h3 dir="auto">New Features</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4528225752"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/131"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/131/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/131">#131</a>: added <strong>Time
  Remaining (ETA)</strong> in the reader HUD as an optional setting.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4478103249"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/115"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/115/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/115">#115</a>: added <strong>Book
  Information</strong> in book settings with quick stats (title, author, format, current
  page, total pages, chapters, last read...).</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4377631381"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/94"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/94/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/94">#94</a>: added <strong>custom
  adjacent cover overrides</strong>. If present next to the book, 3dslibris now prioritizes
  <code class="notranslate">Book.jpg</code> or <code class="notranslate">Book.png</code>
  (including <code class="notranslate">.txt</code>, <code class="notranslate">.md</code>,
  <code class="notranslate">.rtf</code>, and <code class="notranslate">.odt</code>).</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Keeping the Y:lnk hint visible to standardize the reader HUD.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347167582"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/77"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/77/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/77">#77</a>: improved CSS paragraph
  spacing consistency near page bottoms (percent-based margins like <code class="notranslate">1.5%</code>
  no longer collapse as if they were <code class="notranslate">1%</code>, and CSS-driven
  breaks avoid compressed separation at screen edges).</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347167582"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/77"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/77/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/77">#77</a>: added block-level
  <code class="notranslate">padding-top</code> support for <code class="notranslate">%</code>/<code
  class="notranslate">px</code>/<code class="notranslate">em</code> in inline styles,
  and upgraded <code class="notranslate">page-break-before: always</code> handling
  to a hard page break so entry separators start on a new logical page.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4509263790"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/128"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/128/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/128">#128</a>: fixed wide leading
  EPUB images that could be forced into an isolated full-width block on their own
  reading screen.</li>

  </ul>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">Thanks to everyone who keeps testing early builds and reporting UI
  details quickly.</p>

  <ul dir="auto">

  <li><strong>Fueling the Code:</strong> A special thank you to my <strong>Ko-fi supporters</strong>.
  Your donations help keep the project going and keep me caffeinated!</li>

  </ul>

  <p dir="auto"><em>Want to support the project? Consider leaving a ⭐ on GitHub or
  <a href="https://ko-fi.com/rigle" rel="nofollow">buying me a coffee</a>!</em></p>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code> (runtime files only; pair
  it with the <code class="notranslate">.3dsx</code> asset for Homebrew Launcher installs)</li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-05-28T10:09:45Z'
version: v2.7.3
version_title: v2.7.3
---
