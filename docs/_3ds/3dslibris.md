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
    size: 39116592
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.2/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39351232
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.2/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.2/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 68036303
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.2/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39233428
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.2/3dslibris.3dsx
  3dslibris.cia:
    size: 39470016
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.2/3dslibris.cia
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
update_notes: '<h2 dir="auto">3dslibris 2.6.2</h2>

  <p dir="auto">Improved EPUB rendering and performance, a new battery indicator in
  the reader HUD, an optional publisher font-size toggle, and a critical APT suspend
  thread-safety fix (hopefully) preventing HOME Menu crashes after reading.</p>

  <p dir="auto">See the full changelog below for details.</p>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>add battery level indicator in the reader HUD</li>

  <li>add publisher font-size toggle in settings</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366978372"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/85"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/85/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/85">#85</a>: support basic <code
  class="notranslate">&lt;hr/&gt;</code> styling for EPUB reflow</li>

  <li>reduce heap allocations during pagination</li>

  <li>reuse BiDi analysis buffers across pagination</li>

  <li>avoid one full temporary buffer copy on EPUB first-time cover extraction</li>

  <li>start visible cover warmup sooner on New 3DS in conservative browser mode</li>

  <li>stop carrying full OPF baggage on metadata-only EPUB indexing</li>

  <li>avoid extra work on simple LTR text during EPUB text shaping</li>

  <li>reuse Latin-1 glyph advances during pagination for EPUB text measurement</li>

  <li>avoid the heavyweight Unicode decoder during layout for simple Latin UTF-8 text</li>

  <li>batch EPUB content text before shaping</li>

  <li>consolidate CSS class lookups into a single pass per element</li>

  <li>simplify button label draw code</li>

  <li>simplify <code class="notranslate">ContainsRTL</code> in BiDi utils</li>

  </ul>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4367065521"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/87"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/87/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/87">#87</a>: render large EPUB
  images by moving pixel budget guard from metadata probe to draw time</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366971031"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/84"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/84/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/84">#84</a>: support CSS <code
  class="notranslate">margin-top</code> and <code class="notranslate">margin-bottom</code>
  in EPUB reflow</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4346280911"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/68"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>: defer APT suspend
  hook state mutations to main thread to fix cross-thread write hazards, crashes and
  freezes on HOME menu</li>

  <li>follow manifest document order for EPUB spine ordering when the NAV <code class="notranslate">toc</code>
  link is absent</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366899315"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/82"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/82/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/82">#82</a>: accumulate nested
  list indentation correctly per depth level</li>

  <li>apply CSS <code class="notranslate">display:block</code> promotion to block-level
  layout properties</li>

  <li>restore EPUB open path after parser-reuse regression</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366944710"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/83"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>: ensure text-align
  from CSS class definitions applies to block elements properly</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347081948"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/76"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>: respect <code class="notranslate">list-style-type:
  none</code> on <code class="notranslate">&lt;ol&gt;</code> and <code class="notranslate">&lt;ul&gt;</code></li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4242354467"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/35"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/35/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/35">#35</a>: keep adjacent length
  values on CSS <code class="notranslate">margin</code> shorthand with <code class="notranslate">auto</code>
  values</li>

  <li>use the document base instead of the inherited context size for heading font-size
  restore</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366877093"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/81"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/81/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/81">#81</a>: clamp tiny CSS font
  sizes to a readable range</li>

  <li>skip no-op inline font-size changes</li>

  <li>keep thumbnail fast-path under the RGB safety guard for large EPUB PNG/JPEG
  covers</li>

  </ul>

  <h3 dir="auto">Infrastructure</h3>

  <ul dir="auto">

  <li>silence noisy debug builds after the EPUB/cover profiling pass</li>

  <li>remove obsolete EPUB parser helpers left behind by CSS lookup consolidation</li>

  </ul>

  <hr>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">3dslibris wouldn''t be the same without your support! This version
  is dedicated to:</p>

  <ul dir="auto">

  <li><strong>Issue reports and testing:</strong> Thanks to everyone who reported
  and followed up on <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="4242354467" data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/35"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/35/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/35">#35</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4346280911" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/68" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard" href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347081948"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/76"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4366877093" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/81" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/81/hovercard" href="https://github.com/RigleGit/3dslibris/issues/81">#81</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366899315"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/82"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/82/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/82">#82</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4366944710" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/83" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard" href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366971031"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/84"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/84/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/84">#84</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4366978372" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/85" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/85/hovercard" href="https://github.com/RigleGit/3dslibris/issues/85">#85</a>
  and <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4367065521"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/87"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/87/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/87">#87</a>.</li>

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
updated: '2026-05-04T16:38:47Z'
version: v2.6.2
version_title: v2.6.2
---
