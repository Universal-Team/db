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
    size: 39167028
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39396288
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32768813
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66547021
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39139056
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.0/3dslibris.3dsx
  3dslibris.cia:
    size: 39371712
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.0/3dslibris.cia
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
stars: 81
systems:
- 3DS
title: 3dslibris
update_notes: "<h2 dir=\"auto\">3dslibris 2.2.0</h2>\n<p dir=\"auto\">This release\
  \ rolls up the full user-facing work completed since <code class=\"notranslate\"\
  >v2.1.4</code>. It focuses on safer HOME/app lifecycle behavior, more reliable cover\
  \ handling on old3DS, several EPUB rendering fixes, better title presentation in\
  \ the library browser, and a more usable fixed-layout reading experience for PDF/CBZ/XPS.</p>\n\
  <h3 dir=\"auto\">Navigation Demo</h3>\n<details open=\"\" class=\"details-reset\
  \ border rounded-2\">\n  <summary class=\"tmp-px-3 py-2\">\n    <svg aria-hidden=\"\
  true\" height=\"16\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" data-view-component=\"\
  true\" class=\"octicon octicon-device-camera-video\">\n    <path d=\"M16 3.75v8.5a.75.75\
  \ 0 0 1-1.136.643L11 10.575v.675A1.75 1.75 0 0 1 9.25 13h-7.5A1.75 1.75 0 0 1 0\
  \ 11.25v-6.5C0 3.784.784 3 1.75 3h7.5c.966 0 1.75.784 1.75 1.75v.675l3.864-2.318A.75.75\
  \ 0 0 1 16 3.75Zm-6.5 1a.25.25 0 0 0-.25-.25h-7.5a.25.25 0 0 0-.25.25v6.5c0 .138.112.25.25.25h7.5a.25.25\
  \ 0 0 0 .25-.25v-6.5ZM11 8.825l3.5 2.1v-5.85l-3.5 2.1Z\"></path>\n</svg>\n    <span\
  \ class=\"m-1\">Grabacion.de.pantalla.2026-04-15.a.las.8.31.45.mov</span>\n    <span\
  \ class=\"dropdown-caret\"></span>\n  </summary>\n\n  <video src=\"https://github.com/user-attachments/assets/c18b085e-29c0-4520-abb9-13416200b40d\"\
  \ data-canonical-src=\"https://github.com/user-attachments/assets/c18b085e-29c0-4520-abb9-13416200b40d\"\
  \ controls=\"controls\" muted=\"muted\" class=\"d-block rounded-bottom-2 border-top\
  \ width-fit\" style=\"max-height:640px; min-height: 200px\">\n\n  </video>\n</details>\n\
  \n<h3 dir=\"auto\">Highlights</h3>\n<ul dir=\"auto\">\n<li><strong>HOME handling\
  \ is now safer across <code class=\"notranslate\">.3dsx</code> and <code class=\"\
  notranslate\">.cia</code></strong>: the app now tracks APT suspend/restore/wakeup/exit\
  \ events explicitly, pauses work during HOME transitions, and avoids the homebrew-exit\
  \ crash path seen in HBL-driven <code class=\"notranslate\">.3dsx</code> launches.</li>\n\
  <li><strong>old3DS cover loading is more stable under memory pressure</strong>:\
  \ cover extraction now uses device-aware memory guards, bounded warmup queueing,\
  \ and retry backoff instead of hammering the same failing books in a tight loop.</li>\n\
  <li><strong>EPUB block spacing support is broader</strong>: paragraph and horizontal-rule\
  \ margin handling now respects more CSS class-based margin definitions, improving\
  \ scene breaks and block layout in real books.</li>\n<li><strong>EPUB TOC / contents\
  \ pages render more sanely</strong>: TOC-like documents are now detected from document\
  \ metadata as well as filename/path, which prevents dense contents entries from\
  \ collapsing into one run-on paragraph.</li>\n<li><strong>Long book titles are easier\
  \ to browse in the library</strong>: selected and grid titles now support marquee\
  \ scrolling, and display names prefer embedded metadata titles over raw filenames\
  \ when available.</li>\n<li><strong>Preformatted text is safer</strong>: clipping\
  \ for <code class=\"notranslate\">pre</code> / code-heavy blocks was corrected so\
  \ wrapping/truncation no longer corrupts surrounding text flow.</li>\n<li><strong>Fixed-layout\
  \ reading is more practical on 3DS screens</strong>: PDF/CBZ/XPS now expose an extra\
  \ zoom tier for small-screen readability, and fixed-layout page turns now also work\
  \ on <code class=\"notranslate\">L</code> / <code class=\"notranslate\">R</code>\
  \ for the supported reader paths in this release.</li>\n</ul>\n<h3 dir=\"auto\"\
  >Included fixes and behavior changes</h3>\n<ul dir=\"auto\">\n<li><strong>HBL <code\
  \ class=\"notranslate\">.3dsx</code> HOME crash avoided</strong>: after app cleanup\
  \ completes, homebrew launches now exit through <code class=\"notranslate\">svcExitProcess()</code>\
  \ instead of falling into a broken <code class=\"notranslate\">aptExit()</code>\
  \ path after HBL has already reclaimed the APT session.</li>\n<li><strong>Suspend/resume\
  \ lifecycle is explicit</strong>: applet hooks now pause background work on suspend,\
  \ mark screens dirty on restore/wakeup, and persist prefs on exit.</li>\n<li><strong>Reader/browser\
  \ state is hardened across HOME</strong>: resume paths now reset transient touch/input\
  \ state and avoid continuing presentation in an inconsistent applet state.</li>\n\
  <li><strong>Cover retry storms are blocked on old3DS</strong>: failed low-memory\
  \ cover jobs are deferred with backoff, and speculative warmup is kept much more\
  \ conservative on memory-constrained hardware.</li>\n<li><strong>EPUB <code class=\"\
  notranslate\">&lt;hr&gt;</code> rendering is more accurate</strong>: structural\
  \ separators such as <code class=\"notranslate\">hr.transition</code> no longer\
  \ force a visible line when the source CSS says <code class=\"notranslate\">border:\
  \ none</code>, while actual rule blocks retain block-margin handling.</li>\n<li><strong>Browser\
  \ display names are cleaner</strong>: metadata titles are preferred when present,\
  \ cached display names are invalidated correctly when titles change, and edge cases\
  \ are covered by added tests.</li>\n<li><strong>MuPDF page backtracking is now reliable</strong>:\
  \ changing pages resets the fixed-layout viewport coherently before deferred redraw,\
  \ which avoids stale pan state when moving backward through PDFs/XPS documents.</li>\n\
  <li><strong>CBZ failure diagnosis is better</strong>: debug logging now records\
  \ whether loading failed during ZIP access or during image decode, making file-specific\
  \ reports easier to triage.</li>\n</ul>\n<h3 dir=\"auto\">Included assets</h3>\n\
  <ul dir=\"auto\">\n<li><code class=\"notranslate\">3dslibris.cia</code></li>\n<li><code\
  \ class=\"notranslate\">3dslibris-debug.cia</code></li>\n<li><code class=\"notranslate\"\
  >3dslibris.3dsx</code></li>\n<li><code class=\"notranslate\">3dslibris-debug.3dsx</code></li>\n\
  <li><code class=\"notranslate\">3dslibris-sdmc.zip</code></li>\n<li><code class=\"\
  notranslate\">3dslibris-source.tar.gz</code></li>\n</ul>"
updated: '2026-04-15T06:53:19Z'
version: v2.2.0
version_title: v2.2.0
---
