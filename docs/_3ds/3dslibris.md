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
    size: 14328112
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.4/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 14566336
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.4/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.4/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66949361
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.4/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14452496
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.4/3dslibris.3dsx
  3dslibris.cia:
    size: 14689216
    size_str: 14 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.4/3dslibris.cia
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
stars: 119
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.6.4</h2>

  <p dir="auto">Important bug fixes and improvements for EPUB rendering, PDF/CBZ performance
  and zoom, in-book settings, and CIA size.</p>

  <p dir="auto">Notable changes</p>

  <ul dir="auto">

  <li>You can now adjust font, size, spacing, orientation, and publisher font-size
  settings in-book. Press Start to return to the library, otherwise you return to
  the book with the new settings applied.</li>

  <li>The PDF/CBZ reader is now faster and supports up to 4.0× zoom on both Old 3DS
  and New 3DS.</li>

  </ul>

  <p dir="auto">See the full changelog below for details.</p>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4377601431"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/91"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/91/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/91">#91</a>: in-book settings
  (Select) now shows font, size, spacing, orientation, and publisher font-size controls;
  exiting automatically reopens the book when any layout-affecting setting changed;
  footer adds "back" (return to book) and "library" buttons; Start key goes to library</li>

  <li>unify PDF and CBZ maximum zoom to index 6 (4.0×) on both Old 3DS and New 3DS</li>

  <li><strong>reduce CIA binary size by ~32 MB by stripping MuPDF''s embedded CJK
  fallback fonts</strong>; place a font (e.g. NotoSansCJK) in the font directory for
  CJK PDF rendering</li>

  <li>fix CIA gallery covers not loading by raising SystemMode to 96 MB and lowering
  the cover extraction memory threshold</li>

  <li>support user-supplied CJK fonts in the font directory for PDF glyph rendering</li>

  <li>render ruby annotations as <code class="notranslate">(text)</code> at 75% size;
  bold column and row headers in table output</li>

  </ul>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413479835"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/98"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/98/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/98">#98</a>: fix "Clear Cache"
  button showing stale "cleared!" text when re-entering Settings after a cache clear</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413432256"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/97"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/97/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/97">#97</a>: fix CSS keyword
  font sizes (<code class="notranslate">font-size: small</code>, <code class="notranslate">x-small</code>,
  <code class="notranslate">smaller</code>, etc.) rendering at the wrong size when
  "Respect publisher font size" is off</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413498510"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/99"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/99/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/99">#99</a>: fix incomplete TOC
  index in large books</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347081948"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/76"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>: fix only the first
  linked CSS stylesheet being loaded; books with a non-CSS file (e.g. <code class="notranslate">.xpgt</code>)
  before the <code class="notranslate">.css</code> now apply all CSS rules correctly</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4363217365"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/78"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/78/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/78">#78</a>: (hopefully™️) fix
  HOME button crashes in debug builds caused by SD card I/O in the APT hook callback
  on the system thread</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413861981"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/100"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/100/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/100">#100</a>: fix DPad controls
  in inline link focus mode: UP/DOWN now navigate across pages; LEFT/RIGHT corrected
  for portrait orientation</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4380629950"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/96"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/96/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/96">#96</a>: fix transparent
  PNG inline images (e.g. decorative banners/ornaments) rendering with a white background
  instead of compositing against the page</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4380629950"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/96"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/96/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/96">#96</a>: fix images inside
  EPUB table cells producing a stray <code class="notranslate">[image]</code> text
  artifact or white squares at the top of pages; table-cell images are now silently
  suppressed</li>

  <li>fix superscript (<code class="notranslate">&lt;sup&gt;</code>) and subscript
  (<code class="notranslate">&lt;sub&gt;</code>) text rendering: replaced box-filter
  downscaling with native FreeType rendering at 70% pixel size for sharper glyphs</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366944710"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/83"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>: fix <code class="notranslate">text-align:
  center</code> (and <code class="notranslate">right</code>) paragraphs appearing
  left-aligned when the line text is wider than the screen; each word-wrapped visual
  line is now centered independently</li>

  <li>fix centered text (<code class="notranslate">text-align: center</code>/<code
  class="notranslate">right</code>) appearing right-shifted on the second screen</li>

  <li>fix continuation wrap lines on the second screen starting with incorrect left
  margin after screen overflow</li>

  <li>fix list items containing an inner <code class="notranslate">&lt;p&gt;</code>
  element rendering the list marker on a separate line instead of inline with the
  content</li>

  <li>support CSS <code class="notranslate">text-indent</code> property for first-line
  paragraph indentation (px, em, pt, in units)</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366971031"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/84"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/84/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/84">#84</a>: honor CSS <code
  class="notranslate">margin-top</code> and <code class="notranslate">margin-bottom</code>
  on block elements (<code class="notranslate">div</code>, <code class="notranslate">aside</code>,
  <code class="notranslate">blockquote</code>, <code class="notranslate">figure</code>,
  <code class="notranslate">caption</code>, <code class="notranslate">dd</code>);
  default spacing preserved when no CSS value is specified</li>

  <li>fix CSS class <code class="notranslate">font-weight: bold</code> and <code class="notranslate">font-style:
  italic</code> being silently ignored; class-level bold/italic now applies to inline
  text</li>

  <li>fix returning from in-book settings leaving the top screen blank (book text
  now redraws immediately on return)</li>

  </ul>

  <h3 dir="auto">Infrastructure</h3>

  <ul dir="auto">

  <li>extract ten handler modules from <code class="notranslate">book_xml_parser.cpp</code>:
  heading, table capture, inline image, anchor, flow emission, screen advancement,
  element style, inline element, block element, and FB2 element handlers</li>

  <li>extract CSS element handler dispatch into dedicated per-concern compilation
  units</li>

  <li>split five large source files into focused translation units: <code class="notranslate">mupdf_view.cpp</code>,
  <code class="notranslate">book_xml_css_style_utils.cpp</code>, <code class="notranslate">text_renderer.cpp</code>,
  <code class="notranslate">book_xml_parser.cpp</code> (support helpers), <code class="notranslate">path_utils.h</code></li>

  <li>extract <code class="notranslate">cover_cache</code>, <code class="notranslate">GoToPageDialog</code>,
  fixed-layout and reflowable input handlers, and <code class="notranslate">epub_css_tokenizer</code>
  into dedicated modules</li>

  <li>expand FB2 integration test coverage</li>

  <li>add page alignment utils test coverage (<code class="notranslate">MeasureFirstVisualLineWidth</code>,
  centered/right-aligned overflow)</li>

  <li>replace hardcoded screen dimensions and consolidate repeated screen-dimension
  constants into shared headers</li>

  </ul>

  <hr>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">3dslibris wouldn''t be the same without your support! This version
  is dedicated to:</p>

  <ul dir="auto">

  <li><strong>Issue reports and testing:</strong> Thanks to everyone who reported
  and followed up on <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="4347081948" data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/76"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/76/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/76">#76</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4363217365" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/78" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/78/hovercard" href="https://github.com/RigleGit/3dslibris/issues/78">#78</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366944710"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/83"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4366971031" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/84" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/84/hovercard" href="https://github.com/RigleGit/3dslibris/issues/84">#84</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4377601431"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/91"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/91/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/91">#91</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4380629950" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/96" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/96/hovercard" href="https://github.com/RigleGit/3dslibris/issues/96">#96</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413432256"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/97"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/97/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/97">#97</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4413479835" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/98" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/98/hovercard" href="https://github.com/RigleGit/3dslibris/issues/98">#98</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413498510"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/99"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/99/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/99">#99</a>, and <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4413861981" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/100" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/100/hovercard" href="https://github.com/RigleGit/3dslibris/issues/100">#100</a>.</li>

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
updated: '2026-05-16T14:29:05Z'
version: v2.6.4
version_title: v2.6.4
---
