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
    size: 39121184
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.0/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 32743941
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66529220
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39099352
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.0/3dslibris.3dsx
  3dslibris.cia:
    size: 39330752
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.1.0/3dslibris.cia
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
stars: 73
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.1.0</h2>

  <p dir="auto">This release focuses on EPUB reading quality, typography, fallback
  fonts, and onboarding. It adds configurable monospace rendering for code-heavy books,
  broadens XHTML/CSS formatting support, improves chapter/index labels and punctuation
  handling, bundles broader CJK/RTL fallback coverage, and documents the install/book-copy
  flow more clearly in both the repository and the bundled SD quickstart.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>Configurable EPUB monospace flow restored and expanded</strong>: <code
  class="notranslate">pre</code> / <code class="notranslate">code</code> now reflow
  with the active monospace font instead of measuring with the serif text face, preserving
  readable code blocks while keeping the new configurable mono font path.</li>

  <li><strong>Monospace variants now render correctly</strong>: EPUB content can distinguish
  regular, bold, italic, and bold-italic monospace text instead of collapsing everything
  to one mono style.</li>

  <li><strong>More EPUB block semantics are supported</strong>: lists, nested ordered
  lists, <code class="notranslate">blockquote</code>, <code class="notranslate">aside</code>,
  <code class="notranslate">caption</code>, <code class="notranslate">figure</code>,
  <code class="notranslate">dl</code> / <code class="notranslate">dd</code>, and basic
  table linearization now render as readable reflow blocks instead of collapsing into
  generic paragraph flow.</li>

  <li><strong>EPUB inline formatting support is broader</strong>: underline, strikethrough,
  overline, superscript, subscript, dotted/dashed/wavy underline styles, and common
  CSS-driven emphasis patterns are now recognized more consistently.</li>

  <li><strong>Hidden EPUB accessibility text is ignored</strong>: common hidden-text
  patterns such as <code class="notranslate">visually-hidden</code>, <code class="notranslate">aria-hidden</code>,
  and equivalent inline CSS are no longer shown as visible body text.</li>

  <li><strong>Styled punctuation stays attached to the surrounding text</strong>:
  closing <code class="notranslate">!</code> / <code class="notranslate">?</code>
  and opening <code class="notranslate">¡</code> / <code class="notranslate">¿</code>
  are handled more safely across inline style boundaries, avoiding the worst split
  cases in Spanish text.</li>

  <li><strong>EPUB index labels are cleaner</strong>: chapter menus now prefer simpler
  labels instead of concatenating multiple headings into one noisy entry.</li>

  <li><strong>EPUB page cache writes are safer</strong>: page cache files now save
  with the actual layout parameters used for pagination instead of stale zeroed values,
  avoiding invalid cache entries after fresh opens.</li>

  <li><strong>Bundled quickstart and SD docs are clearer about where books go</strong>:
  the release package now makes the <code class="notranslate">sdmc:/3ds/3dslibris/book/</code>
  path more explicit, since this is still the most common user setup question.</li>

  <li><strong>Book view renderer recovery is more defensive</strong>: entering or
  reopening a book now resets the text renderer state more aggressively, which should
  reduce rare cases where visible glyphs disappear until the app is restarted.</li>

  </ul>

  <h3 dir="auto">Language, fallback, and layout improvements included</h3>

  <ul dir="auto">

  <li><strong>Arabic, Hebrew, Korean, Japanese, and Chinese fallback coverage improved</strong>:
  the SD package now bundles Noto Naskh Arabic, Noto Sans Hebrew, and Droid Sans Fallback
  Full alongside Liberation, with updated Apache 2.0 / OFL notices.</li>

  <li><strong>Configured fallback fonts survive prefs loading correctly</strong>:
  loading saved preferences no longer collapses the fallback set to only one face,
  so CJK/RTL coverage remains available after restart.</li>

  <li><strong>RTL layout support is more robust</strong>: BiDi shaping, line anchoring,
  and orientation-aware layout work included since <code class="notranslate">2.0.4</code>
  make mixed-script content behave more predictably.</li>

  <li><strong>Orientation-aware inline image layout is more stable</strong>: screen
  metrics and image placement helpers were refactored so reflow/image combinations
  behave better in both orientations.</li>

  </ul>

  <h3 dir="auto">Developer and packaging work included</h3>

  <ul dir="auto">

  <li><strong>EPUB regression coverage is much wider</strong>: the test suite now
  covers punctuation flow, underline decorations, parser style behavior, and a dedicated
  EPUB rendering fixture used to validate hidden text, code blocks, lists, and tables.</li>

  <li><strong>Bundled release test content improved</strong>: the SD template and
  fixture EPUB now provide a more practical target for smoke-testing release builds
  on hardware and in Azahar.</li>

  <li><strong>Release packaging docs were refreshed</strong>: README and SD template
  docs now align better with the actual release layout and the supported install paths.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-09T20:37:08Z'
version: v2.1.0
version_title: v2.1.0
---
