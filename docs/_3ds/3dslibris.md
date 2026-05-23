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
    size: 14347112
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13112256
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66862233
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14471708
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.0/3dslibris.3dsx
  3dslibris.cia:
    size: 13243328
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.7.0/3dslibris.cia
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
stars: 120
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.7.0</h2>

  <p dir="auto">Library folder navigation, continuous D-Pad page turning, unified
  publisher font scaling, much more reliable HOME button on Old 3DS / 2DS, and rendering
  fixes.</p>

  <p dir="auto">Notable changes</p>

  <ul dir="auto">

  <li>Books can now be organized into one level of subfolders. The root library shows
  folders first, then root-level books. Opening a folder shows its contents, with
  <code class="notranslate">B</code> or the touch <strong>back</strong> button returning
  to the root.</li>

  <li>Holding D-Pad Up/Down in reflowable books (EPUB, MOBI, FB2, TXT, RTF, ODT) now
  repeats page turns automatically after a short delay.</li>

  <li>The "Respect Publisher Font Sizes" toggle has been removed. Publisher CSS font
  sizes are now always honored, but scaled relative to the user''s font-size preference.</li>

  <li><strong>New improvements to prevent HOME crashes:</strong> several causes have
  been fixed at once and the app now frees up to ~20 MB before suspending. <strong>Check
  if you have installed a custom theme that is conflicting with the homebrew and it''s
  crashing on "menu"</strong>.</li>

  </ul>

  <h3 dir="auto">Stability</h3>

  <ul dir="auto">

  <li>SD-card writes inside the APT hook callback (running on the system thread) sometimes
  blocked the HOME menu from getting its acknowledgment in time.</li>

  <li><strong>free up to ~20 MB of RAM before HOME takes over</strong>: PDF/CBZ bitmap
  caches, preloaded adjacent pages, MuPDF display lists, the inline image cache, and
  the FreeType glyph bitmap cache are now released the moment the app suspends</li>

  <li>PDF/CBZ workers shut down cleanly on suspend and re-init on resume</li>

  <li>book opening, first library scan, cover extraction, metadata indexing, TOC resolution,
  and page-cache writes now temporarily block HOME only while the unsafe critical
  section is running</li>

  <li>applet exit handling no longer changes reader mode directly inside the APT hook;
  the main loop observes the exit request and shuts down from the normal app thread</li>

  <li>CIA: drop SystemMode to 80 MB (safer on Old 3DS), enable ExeFS compression,
  bump <code class="notranslate">bannertool</code> to 1.2.2 (matches stable homebrew
  like <a href="github.com/astronautlevel2/Anemone3DS">Anemone3DS</a>, <a href="https://github.com/BernardoGiordano/Checkpoint">Checkpoint</a>...)</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4269663849"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/41"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/41/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/41">#41</a>: <strong>first-level
  folder navigation in the library</strong>: the root library shows folders first,
  then root-level books; opening a folder shows the books directly inside it; <code
  class="notranslate">B</code> or touch <strong>back</strong> returns to the root
  library; optional sibling folder covers supported via <code class="notranslate">FolderName.jpg</code></li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4219392679"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/24"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/24/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/24">#24</a>: <strong>continuous
  D-Pad page turning for reflowable books</strong>: holding D-Pad Up/Down repeats
  previous/next page turns reflowable layout; new general setting to disable Circle
  Pad page turns for users affected by analog drift</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4460902041"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/106"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/106/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/106">#106</a>: <strong>unify
  publisher font-size rendering</strong>: publisher CSS <code class="notranslate">font-size</code>
  is always applied; absolute <code class="notranslate">px</code> values scale relative
  to the publisher''s declared <code class="notranslate">body { font-size }</code>
  baseline; reader''s font-size preference acts as a global scale factor</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4461204241"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/108"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/108/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/108">#108</a>: <strong>CSS <code
  class="notranslate">em</code>/<code class="notranslate">rem</code> lengths now resolve
  against the actual font size</strong>: <code class="notranslate">text-indent</code>,
  <code class="notranslate">margin-left</code>, <code class="notranslate">margin-right</code>,
  and related properties previously converted <code class="notranslate">em</code>
  to pixels using a hardcoded 12px baseline</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4438907512"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/102"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/102/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/102">#102</a> add conservative
  Markdown reading for <code class="notranslate">.md</code> and <code class="notranslate">.markdown</code>
  files: headings, emphasis, lists, blockquotes, code spans, and link text are converted
  into the existing reflowable text renderer</li>

  <li>battery percentage now uses the real <code class="notranslate">mcu::HWC</code>
  reading, following the approach used by <a href="https://github.com/joel16/3DSident">3DSident</a>;
  PTMU''s coarse 0-5 level is only kept as a fallback</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366944710"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/83"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>: fix center- and
  right-aligned paragraphs containing narrow inline elements</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366971031"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/84"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/84/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/84">#84</a>: <strong>CSS <code
  class="notranslate">margin-top</code> and <code class="notranslate">margin-bottom</code>
  on block elements</strong>: section spacing in poetry-style EPUBs now respects the
  declared CSS margin size</li>

  </ul>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413479835"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/98"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/98/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/98">#98</a>: fix "Clear Cache"
  not triggering a book re-parse on the next open</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4380629950"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/96"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/96/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/96">#96</a>: fix CSS keyword
  font sizes in inline <code class="notranslate">style=</code> attributes being silently
  ignored</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413498510"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/99"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/99/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/99">#99</a>: fix incomplete TOC
  index in very large anthology EPUBs (regression from v2.6.4)</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413861981"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/100"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/100/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/100">#100</a>: fix link navigation
  performance on TOC pages with many inline links</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4464420913"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/112"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/112/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/112">#112</a>: fix filenames with
  decomposed/combining UTF-8 accents not matching their saved settings and metadata
  entries</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4479120923"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/116"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/116/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/116">#116</a>: fix CIA banner audio</li>

  <li>fix CSS <code class="notranslate">margin-top: 0</code> / <code class="notranslate">margin-bottom:
  0</code> (and negative values) on block elements incorrectly applying the default
  inter-paragraph spacing instead of suppressing it</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4347167582"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/77"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/77/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/77">#77</a>: fix random blank
  space before the first heading on a page</li>

  <li>fix single-line paragraphs whose text is wrapped in an inline element (e.g.
  <code class="notranslate">&lt;p class="centered"&gt;&lt;span&gt;…&lt;/span&gt;&lt;/p&gt;</code>)
  being bumped to the next screen by the paragraph-start orphan guard</li>

  <li>fix overflow detection in page and screen advance firing one line too late</li>

  <li>fix MOBI pre-wrap pagination adding blank lines when text exactly reached the
  right edge</li>

  <li>fix a reflowed EPUB rendering case where a forced screen-break token on the
  already-active right screen was ignored</li>

  <li>tighten reflowed page drawing to the configured content bounds so glyph overhang
  no longer leaks into the right margin</li>

  </ul>

  <h3 dir="auto">Infrastructure</h3>

  <ul dir="auto">

  <li>split the 1,286-line <code class="notranslate">app.cpp</code> into focused translation
  units (<code class="notranslate">app_accessors.cpp</code>, <code class="notranslate">app_lifecycle.cpp</code>,
  <code class="notranslate">app_menu_frames.cpp</code>, <code class="notranslate">app_views.cpp</code>);
  <code class="notranslate">app.cpp</code> is now 446 lines and holds only initialization,
  screens/orientation, status, and gradient backgrounds</li>

  <li>add <code class="notranslate">-fdata-sections</code> and drop C++ unwind tables
  (exceptions are off) to let the linker garbage-collect more dead data (small but
  free .3dsx size reduction)</li>

  <li>add boot/APT trace files (<code class="notranslate">sdmc:/3dslibris_boot_trace.txt</code>
  and <code class="notranslate">sdmc:/3dslibris_apt_trace.txt</code>) to diagnose
  CIA launch and HOME suspend crashes on real hardware</li>

  <li>add <code class="notranslate">debug-safe-cia</code>, a diagnostic CIA build
  path with simplified title metadata and no custom banner/audio, for isolating HOME
  Menu metadata/cache issues</li>

  <li>debug logs for failed PDF/TXT/RTF opens now include <code class="notranslate">errno</code>/<code
  class="notranslate">strerror(errno)</code> when the filesystem layer exposes a useful
  error</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4497396984"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/121"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/121/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/121">#121</a>: optimize PNG UI/readme
  assets to shave a little size from the repository and packaged resources</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4498433059"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/124"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/124/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/124">#124</a>: refine the PTMU
  fallback battery label so an empty/critical coarse level displays as ~1% instead
  of ~0%</li>

  <li>keep very noisy diagnostics behind explicit Makefile flags instead of enabling
  them in every debug build</li>

  <li>remove stale TODO comments whose underlying refactors have already landed</li>

  </ul>

  <hr>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">3dslibris wouldn''t be the same without your support! This version
  is dedicated to:</p>

  <ul dir="auto">

  <li><strong>Library organization and D-Pad repeat:</strong> Thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/svenotta/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/svenotta">@svenotta</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/EmbersFlying/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/EmbersFlying">@EmbersFlying</a>
  for the suggestions.</li>

  <li><strong>HOME crash investigation:</strong> Thanks to everyone who investigated
  and shared hardware details, crash dumps, and trace logs for <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4346280911" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/68" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard" href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>.
  Let''s see if we can fix it for good in newest releases.</li>

  <li><strong>Community PRs:</strong> Thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/adri22235/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/adri22235">@adri22235</a>
  for <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4464420913"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/112"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/112/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/112">#112</a>, <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/AverageJohtonian/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/AverageJohtonian">@AverageJohtonian</a>
  for <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4479120923"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/116"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/116/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/116">#116</a>, and <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Rhlp-Engineering/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Rhlp-Engineering">@Rhlp-Engineering</a>
  for <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4497396984"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/121"
  data-hovercard-type="pull_request" data-hovercard-url="/RigleGit/3dslibris/pull/121/hovercard"
  href="https://github.com/RigleGit/3dslibris/pull/121">#121</a> and <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4498433059" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/124" data-hovercard-type="pull_request"
  data-hovercard-url="/RigleGit/3dslibris/pull/124/hovercard" href="https://github.com/RigleGit/3dslibris/pull/124">#124</a>.</li>

  <li><strong>Font rendering and CSS fixes:</strong> Thanks to everyone who reported
  and tested <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="4347167582" data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/77"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/77/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/77">#77</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4366944710" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/83" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/83/hovercard" href="https://github.com/RigleGit/3dslibris/issues/83">#83</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4366971031"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/84"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/84/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/84">#84</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4413498510" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/99" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/99/hovercard" href="https://github.com/RigleGit/3dslibris/issues/99">#99</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4413861981"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/100"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/100/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/100">#100</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4438907512" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/102" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/102/hovercard" href="https://github.com/RigleGit/3dslibris/issues/102">#102</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4460902041"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/106"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/106/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/106">#106</a>, <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4461204241" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/108" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/108/hovercard" href="https://github.com/RigleGit/3dslibris/issues/108">#108</a>,
  and the poetry stanza spacing fix.</li>

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
updated: '2026-05-23T15:44:15Z'
version: v2.7.0
version_title: v2.7.0
---
