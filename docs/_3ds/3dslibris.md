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
    size: 14388388
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.4/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13136832
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.4/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.4/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66954044
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.4/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14512340
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.4/3dslibris.3dsx
  3dslibris.cia:
    size: 13272000
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.4/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: other
license_name: Other
llm_usage: undisclosed
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
update_notes: '<h2 dir="auto">3dslibris 2.7.4</h2>

  <p dir="auto">Hotfix update focused on saving the book progress.</p>

  <h3 dir="auto">New Features</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4541290172"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/133"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/133/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/133">#133</a>: improved <strong>Book
  Information</strong> description rendering by sanitizing common inline HTML/CSS
  markup (for example <code class="notranslate">&lt;br&gt;</code>, <code class="notranslate">&lt;p&gt;</code>,
  <code class="notranslate">&lt;li&gt;</code>, <code class="notranslate">&amp;amp;</code>,
  <code class="notranslate">&amp;lt;</code>) and adapting inline style parsing (including
  <code class="notranslate">font-weight</code>, <code class="notranslate">font-style</code>,
  <code class="notranslate">text-decoration</code>, <code class="notranslate">white-space</code>,
  <code class="notranslate">text-transform</code>) so tags no longer appear as raw
  code and long descriptions can be read across additional info pages.</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4528040226"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/130"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/130/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/130">#130</a>: fixed a cover-layout
  regression where page-like EPUB covers could be pre-advanced and pushed to the next
  reading page/screen instead of staying in the current opening spread.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4541962981"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/134"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/134/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/134">#134</a>: fixed a reading-progress
  regression where the saved page could reopen at page 1 after restart or book switching
  by persisting before switch-close and preserving restored pending position until
  parse completes.</li>

  <li>Improved EPUB reopen stability for very large page-cache files (RAM crashes
  related)</li>

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
updated: '2026-05-29T15:29:10Z'
version: v2.7.4
version_title: v2.7.4
---
