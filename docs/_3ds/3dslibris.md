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
    size: 39127244
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.3/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39363520
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.3/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.3/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66923506
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.3/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39241132
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.3/3dslibris.3dsx
  3dslibris.cia:
    size: 39478208
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.3/3dslibris.cia
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
stars: 107
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.6.3</h2>

  <p dir="auto">Improved PDF/CBZ speed and EPUB rendering fidelity: global CSS element
  rules now apply correctly, list marker suppression is more reliable, centered paragraphs
  behave more consistently, line wrapping is improved, inline figures/captions behave
  better across both reading screens, and random empty space from page-break and margin
  flush edge cases is fixed.</p>

  <p dir="auto">See the full changelog below for details.</p>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366944710"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/83"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>: apply global CSS
  element rules (<code class="notranslate">p {}</code>, <code class="notranslate">body
  {}</code>, <code class="notranslate">li {}</code>, <code class="notranslate">h1
  {}</code>, <code class="notranslate">blockquote {}</code>, etc.) to block layout,
  margins, font-size, and text-align</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347081948"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/76"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>: suppress list markers
  when <code class="notranslate">list-style-type: none</code> is declared on <code
  class="notranslate">&lt;ol&gt;</code> or <code class="notranslate">&lt;ul&gt;</code>
  via a bare element selector</li>

  <li>make PDF and CBZ fixed-layout viewport panning smooth by blitting cached zoom/preview
  bitmaps while expensive render/decode work is deferred</li>

  <li>improve EPUB NCX/NAV/TOC handling and parser coverage</li>

  <li>improve EPUB line wrapping</li>

  <li>improve preformatted text wrapping so whitespace is preferred before splitting
  long tokens</li>

  <li>improve EPUB <code class="notranslate">&lt;dd&gt;</code> indentation by using
  block margins instead of injecting literal leading spaces</li>

  <li>improve inline image layout for <code class="notranslate">&lt;figure&gt;</code>
  / <code class="notranslate">div.figure</code> content with captions</li>

  <li>allow page-mode images and covers to fill the available page box when appropriate</li>

  <li>add a START-button quit shortcut from the library/browser for Homebrew Launcher
  users</li>

  <li>improve parser dispatch boundaries and integration coverage for real EPUB opens
  and metadata indexing</li>

  <li>reduce App singleton usage across library, UI, menu, and settings layers</li>

  </ul>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347167582"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/77"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/77/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/77">#77</a>: fix random empty
  space when rendering caused by pending block-spacing not flushing correctly at page
  boundaries</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366944710"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/83"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>: fix text-align not
  rendering when declared on a bare element selector (<code class="notranslate">p
  { text-align: center }</code>)</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347081948"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/76"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>: fix list markers
  not suppressing when the CSS rule targets the parent <code class="notranslate">&lt;ol&gt;</code>/<code
  class="notranslate">&lt;ul&gt;</code> element rather than the <code class="notranslate">&lt;li&gt;</code>
  directly</li>

  <li>fix page break edge cases in EPUB reflow</li>

  <li>fix EPUB screen transitions so parser state and rendered page buffers stay synchronized
  between left/right reading screens</li>

  <li>fix block-boundary edge cases where pretty-printed whitespace between XHTML
  block elements could consume pending breaks</li>

  <li>fix heading spacing when a heading follows existing content</li>

  <li>fix page-mode inline images on the second reading screen incorrectly advancing
  to a blank next screen</li>

  <li>fix large EPUB inline JPGs failing to draw on constrained 3DS memory by using
  bounded subsampled decode</li>

  <li>fix figure-with-caption images on the second reading screen being pushed too
  aggressively to the next spread</li>

  <li>fix bottom reading-screen margin handling by using the compact margin resolver
  consistently</li>

  <li>fix a MOBI page-cache compatibility regression by bumping the cache version
  after line-break behavior changed</li>

  <li>fix old-3DS gallery covers being skipped when the previous memory guard was
  too conservative for real hardware</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4346280911"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/68"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>: mitigate Old 3DS
  <code class="notranslate">.3dsx</code> HOME/APT crashes by handling pending suspend
  before more graphics/input work</li>

  <li>fix flowed text emission so local left margins cannot move text left of the
  base reading margin</li>

  </ul>

  <h3 dir="auto">Infrastructure</h3>

  <ul dir="auto">

  <li>extract parser and renderer dispatch layers for EPUB, MOBI, FB2, TXT, RTF, ODT,
  PDF, CBZ</li>

  <li>move <code class="notranslate">Book::Index</code> to <code class="notranslate">book_parser::Index</code></li>

  <li>remove <code class="notranslate">Book::Open</code>, move open/parse/index dispatch
  into <code class="notranslate">book_parser</code>, and unify the fixed-layout book
  path</li>

  <li>move public rendering and fixed-layout dispatch into <code class="notranslate">book_renderer</code></li>

  <li>remove <code class="notranslate">Text::app</code></li>

  <li>extract gradient drawing from <code class="notranslate">App</code></li>

  <li>decouple <code class="notranslate">Text</code>, touch utilities, browser views,
  library helpers, and menu layer from <code class="notranslate">App</code></li>

  <li>move the NDS/3DS hardware reference docs out of this repository into <a href="https://github.com/RigleGit/gba-ds-3ds-specs">gba-ds-3ds-specs</a></li>

  <li>expand host integration, CSS, NCX/NAV, FB2 metadata, TXT/FB2/RTF, and page-cache
  test coverage</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4346280911"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/68"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>: add targeted debug
  lifecycle logs for APT suspend/resume/exit and shutdown diagnostics</li>

  <li>keep host parser integration tests linked with the shared binary/ZIP helpers
  used by cache and EPUB image paths</li>

  </ul>

  <h3 dir="auto">Testing</h3>

  <ul dir="auto">

  <li>host test suite now covers 110 scripts</li>

  <li>add real EPUB integration coverage for <code class="notranslate">epub_parser::Open</code>,
  <code class="notranslate">epub_parser::Index</code>, <code class="notranslate">book_parser::Open
  -&gt; EPUB</code>, and <code class="notranslate">book_parser::Index -&gt; EPUB</code></li>

  <li>add regression coverage for preformatted wrapping, inline figure placement,
  bounded inline-image JPEG decode sizing, and old-3DS cover warmup thresholds</li>

  <li>add <code class="notranslate">coverage-host</code> reporting for host-testable
  code paths</li>

  </ul>

  <hr>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">3dslibris wouldn''t be the same without your support! This version
  is dedicated to:</p>

  <ul dir="auto">

  <li><strong>Issue reports and testing:</strong> Thanks to everyone who reported
  and followed up on <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="4346280911" data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/68"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4347081948" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/76" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard" href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347167582"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/77"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/77/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/77">#77</a> and <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4366944710" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/83" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard" href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>.</li>

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
updated: '2026-05-09T11:26:47Z'
version: v2.6.3
version_title: v2.6.3
---
