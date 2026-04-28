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
    size: 39074264
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39306176
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020623
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67981241
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39171284
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.0/3dslibris.3dsx
  3dslibris.cia:
    size: 39404480
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.6.0/3dslibris.cia
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
stars: 101
systems:
- 3DS
title: 3dslibris
update_notes: "<h2 dir=\"auto\">3dslibris 2.6.0</h2>\n<p dir=\"auto\">Navigation improvements\
  \ and a fast metadata cache.</p>\n<markdown-accessiblity-table><table role=\"table\"\
  >\n  <tbody><tr>\n<td width=\"33%\"><a target=\"_blank\" rel=\"noopener noreferrer\"\
  \ href=\"https://github.com/user-attachments/assets/7255a111-9be2-4978-a116-48a2e0b2beef\"\
  ><img width=\"664\" height=\"553\" alt=\"imagen\" src=\"https://github.com/user-attachments/assets/7255a111-9be2-4978-a116-48a2e0b2beef\"\
  \ style=\"max-width: 100%; height: auto; max-height: 553px;; aspect-ratio: 664 /\
  \ 553; background-color: var(--bgColor-muted); border-radius: 6px; display: block\"\
  \ class=\"js-gh-image-fallback\"></a> </td>\n<td width=\"33%\"><a target=\"_blank\"\
  \ rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/9c430418-e116-4dfd-94c8-3088cc2ed80c\"\
  ><img width=\"664\" height=\"553\" alt=\"imagen\" src=\"https://github.com/user-attachments/assets/9c430418-e116-4dfd-94c8-3088cc2ed80c\"\
  \ style=\"max-width: 100%; height: auto; max-height: 553px;; aspect-ratio: 664 /\
  \ 553; background-color: var(--bgColor-muted); border-radius: 6px; display: block\"\
  \ class=\"js-gh-image-fallback\"></a></td>\n<td width=\"33%\">\n<a target=\"_blank\"\
  \ rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/b8c4a8f5-ae48-4e6d-b7a5-b5f33f6b3c61\"\
  ><img width=\"664\" height=\"553\" alt=\"imagen\" src=\"https://github.com/user-attachments/assets/b8c4a8f5-ae48-4e6d-b7a5-b5f33f6b3c61\"\
  \ style=\"max-width: 100%; height: auto; max-height: 553px;; aspect-ratio: 664 /\
  \ 553; background-color: var(--bgColor-muted); border-radius: 6px; display: block\"\
  \ class=\"js-gh-image-fallback\"></a>\n</td>\n  </tr>\n</tbody></table></markdown-accessiblity-table>\n\
  <h3 dir=\"auto\">New</h3>\n<ul dir=\"auto\">\n<li><strong>ZL/ZR page flip (New 3DS\
  \ only)</strong>: ZL advances to the next page (same as R), ZR goes back (same as\
  \ L). Orientation-aware: the mapping flips automatically when the display is rotated.\
  \ See <a href=\"https://github.com/RigleGit/3dslibris/issues/63\" data-hovercard-type=\"\
  issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/63/hovercard\">#63</a>.</li>\n\
  <li><strong>D-pad wraps to next/previous page at list boundaries</strong>: in list\
  \ view, pressing Down on the last item jumps to the next page; pressing Up on the\
  \ first item jumps to the previous page. In gallery view the same applies column-wise\
  \ — pressing Right from the right column advances a page, Left from the left column\
  \ goes back. See <a href=\"https://github.com/RigleGit/3dslibris/issues/64\" data-hovercard-type=\"\
  issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/64/hovercard\">#64</a>.</li>\n\
  <li><strong>Separated Circle Pad and D-pad controls</strong>: reader, browser, and\
  \ paged menus now use explicit mappings instead of the mixed libctru directional\
  \ aliases, so Circle Pad and physical D-pad can behave differently where needed.\
  \ For example, the reader now uses the Circle Pad for smooth panning in fixed-layout\
  \ formats, while the D-pad retains the original page-turning behaviour. It also\
  \ supports the New 3DS stick. See <a href=\"https://github.com/RigleGit/3dslibris/issues/57\"\
  \ data-hovercard-type=\"issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/57/hovercard\"\
  >#57</a>.</li>\n<li><strong>Inline internal link navigation</strong>: hold <code\
  \ class=\"notranslate\">Y</code> on a page with inline links to enter link focus\
  \ mode, move with the D-pad, and press <code class=\"notranslate\">A</code> to follow\
  \ the selected link. See <a href=\"https://github.com/RigleGit/3dslibris/issues/27\"\
  \ data-hovercard-type=\"issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/27/hovercard\"\
  >#27</a>.</li>\n<li><strong>Alternative SD data path support</strong>: runtime data\
  \ can now also be loaded from <code class=\"notranslate\">sdmc:/config/3dslibris</code>\
  \ in addition to the legacy <code class=\"notranslate\">sdmc:/3ds/3dslibris</code>\
  \ layout. See <a href=\"https://github.com/RigleGit/3dslibris/issues/6\" data-hovercard-type=\"\
  issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/6/hovercard\">#6</a>.</li>\n\
  <li><strong>Visual feedback</strong>: added \"saving cache...\" status screens during\
  \ the page cache write phase for EPUB and MOBI, paired with \"loading...\" and the\
  \ progress indicator during the open phase.</li>\n<li><strong>Reset to defaults</strong>:\
  \ the <code class=\"notranslate\">GENERAL</code> settings screen now has a <strong>reset\
  \ settings</strong> option (on page 2, navigate with L/R or the <strong>next</strong>\
  \ footer button) that restores font size, paragraph spacing, orientation, color\
  \ mode, clock format, and library view to their factory defaults.</li>\n<li><strong>Clear\
  \ all caches</strong>: the <code class=\"notranslate\">GENERAL</code> settings screen\
  \ now has a <strong>clear cache</strong> option (page 2) that deletes all epub,\
  \ mobi, cover, and metadata disk caches so everything is rebuilt fresh on the next\
  \ open.</li>\n</ul>\n<h3 dir=\"auto\">Performance</h3>\n<ul dir=\"auto\">\n<li><strong>Metadata\
  \ disk cache (~60–80× faster per book)</strong>: title, author, and cover path are\
  \ now written to a small binary cache file (<code class=\"notranslate\">cache/meta/*.bmc</code>)\
  \ the first time a book is indexed. On subsequent launches the cache is read in\
  \ ~1–2 ms per book instead of the previous 115–163 ms required to parse the source\
  \ file. The cache key is derived from the file path, size, and mtime, so stale entries\
  \ are ignored automatically when the source file changes.</li>\n<li><strong>Library\
  \ opens fully populated (~300 ms for a 147-book library on warm cache)</strong>:\
  \ metadata for all books is now pre-loaded from the disk cache during the \"Preparing\
  \ library...\" phase, before the browser opens. This also means the initial title\
  \ sort uses real book titles instead of empty strings. On a cold cache, the failed\
  \ lookups return in under 1 ms each and the behaviour is unchanged.</li>\n<li><strong>Faster\
  \ first EPUB opens</strong>: first-time EPUB pagination no longer writes the page\
  \ cache during the spine parse, and common LTR text now uses a lighter shaping path\
  \ while keeping the full BIDI/Arabic path for RTL content.</li>\n<li><strong>MOBI\
  \ page cache saves immediately at first open with visual feedback</strong>: MOBI\
  \ page cache saving no longer blocks at 100% during parsing. The write happens right\
  \ after parsing completes.</li>\n<li><strong>Page cache saves are really faster\
  \ for large books</strong>: the SD card write buffer for EPUB and MOBI page caches\
  \ was increased from 32 KB to 256 KB, reducing the number of physical write operations\
  \ per save. For a 9,919-page EPUB the cold-cache save time dropped <strong>from\
  \ ~7 minutes to under 10 seconds (~45× faster)</strong>.</li>\n<li><strong>EPUB\
  \ cache-hit opens are significantly faster</strong>: the read buffer for EPUB page\
  \ cache loads was mismatched at 32 KB while writes used 256 KB, causing up to 8×\
  \ more SD card round trips on every cache-hit open. Both paths now use the same\
  \ 256 KB buffer.</li>\n<li><strong>EPUB TOC resolution is faster on large books</strong>:\
  \ the internal href and basename lookup tables used during TOC resolution now use\
  \ <strong>hash maps instead of sorted trees</strong>, reducing per-entry lookup\
  \ cost <strong>from O(log N) to O(1)</strong>.</li>\n<li><strong>Bookmark insert\
  \ no longer sorts the full list</strong>: toggling a bookmark on a page now inserts\
  \ at the correct sorted position directly (binary search + single insert) instead\
  \ of appending then sorting the entire bookmark list.</li>\n<li><strong>MOBI text\
  \ cleanup uses less peak memory</strong>: the mojibake repair pass now moves the\
  \ text into its safety backup rather than copying it, eliminating one full allocation\
  \ of the text buffer (~2–3 MB for a large MOBI) at the peak of the cleanup phase.</li>\n\
  </ul>\n<h3 dir=\"auto\">Fixes</h3>\n<ul dir=\"auto\">\n<li><strong>Homebrew shutdown\
  \ is now deterministic again</strong>: <code class=\"notranslate\">.3dsx</code>\
  \ exits now finish app cleanup before terminating through the homebrew-safe path,\
  \ avoiding the invalid APT shutdown sequence that could still trigger a crash or\
  \ undefined exit behaviour after the fixes for HOME-time loading. See <a href=\"\
  https://github.com/RigleGit/3dslibris/issues/58\" data-hovercard-type=\"issue\"\
  \ data-hovercard-url=\"/RigleGit/3dslibris/issues/58/hovercard\">#58</a>.</li>\n\
  <li><strong>Async opening progress stays main-thread safe</strong>: the async open\
  \ state is now installed before the worker is submitted, preventing worker-side\
  \ progress callbacks from falling back to direct splash rendering.</li>\n<li><strong>Reader\
  \ images no longer slip under the bottom HUD</strong>: full-page covers and other\
  \ large inline images now stop at the start of the status bar area, which also avoids\
  \ some lower-edge content being clipped. See <a href=\"https://github.com/RigleGit/3dslibris/issues/59\"\
  \ data-hovercard-type=\"issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/59/hovercard\"\
  >#59</a>.</li>\n<li><strong>Text alignment is now consistent across EPUB documents</strong>:\
  \ fixed three independent bugs that caused unreliable text centering and right-alignment\
  \ — alignment declared via a CSS class was silently ignored; the first line of a\
  \ paragraph continuing onto a new page lost its alignment and reverted to left;\
  \ and line-width calculations for center/right positioning were thrown off by inline\
  \ style tokens (bold/italic toggles, headings, <code class=\"notranslate\">&lt;small&gt;</code>),\
  \ causing text to appear at the wrong horizontal offset. See <a href=\"https://github.com/RigleGit/3dslibris/issues/66\"\
  \ data-hovercard-type=\"issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/66/hovercard\"\
  >#66</a>.</li>\n<li><strong>EPUB headings now honor CSS font sizes and wrap correctly</strong>:\
  \ <code class=\"notranslate\">h1</code>-<code class=\"notranslate\">h6</code> now\
  \ respect heading-specific <code class=\"notranslate\">font-size</code> styling\
  \ from inline CSS and stylesheet classes, including relative units, and large headings\
  \ paginate without corrupting line breaks or leaking their size/bold styling into\
  \ the following paragraph. The same EPUB CSS class map path now also applies <code\
  \ class=\"notranslate\">vertical-align: super/sub</code> rules declared in stylesheet\
  \ classes, so superscript and subscript styling no longer depends on inline markup\
  \ alone. See <a href=\"https://github.com/RigleGit/3dslibris/issues/46\" data-hovercard-type=\"\
  issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/46/hovercard\">#46</a>.</li>\n\
  <li><strong>EPUB lists now respect CSS marker suppression on <code class=\"notranslate\"\
  >&lt;li&gt;</code> items</strong>: list bullets/ordinals are now correctly hidden\
  \ when <code class=\"notranslate\">list-style-type: none</code> is declared through\
  \ stylesheet classes on the list item itself, instead of only through inherited\
  \ parent-list context. See <a href=\"https://github.com/RigleGit/3dslibris/issues/48\"\
  \ data-hovercard-type=\"issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/48/hovercard\"\
  >#48</a>.</li>\n</ul>\n<h3 dir=\"auto\">Packaging</h3>\n<ul dir=\"auto\">\n<li><strong>SD\
  \ data compatibility</strong>: installs that keep data under <code class=\"notranslate\"\
  >sdmc:/config/3dslibris</code> are now supported alongside the existing <code class=\"\
  notranslate\">sdmc:/3ds/3dslibris</code> layout. See <a href=\"https://github.com/RigleGit/3dslibris/issues/6\"\
  \ data-hovercard-type=\"issue\" data-hovercard-url=\"/RigleGit/3dslibris/issues/6/hovercard\"\
  >#6</a>.</li>\n</ul>\n<hr>\n<h2 dir=\"auto\">❤️ Community Shoutouts</h2>\n<p dir=\"\
  auto\">3dslibris wouldn't be the same without your support! This version is dedicated\
  \ to:</p>\n<ul dir=\"auto\">\n<li><strong>Fueling the Code:</strong> A special thank\
  \ you to my <strong>Ko-fi supporters</strong>. Your donations help keep the project\
  \ going and keep me caffeinated!</li>\n<li><strong>Enhancement Ideas:</strong> Thanks\
  \ to <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Kr0Key/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Kr0Key\">@Kr0Key</a>, <a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/Narwher/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Narwher\">@Narwher</a>,  <a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/EmbersFlying/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/EmbersFlying\">@EmbersFlying</a> and <a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/The0zymandias/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/The0zymandias\">@The0zymandias</a> for their suggestions\
  \ and feedback that helped shape this release.</li>\n</ul>\n<p dir=\"auto\"><em>Want\
  \ to support the project? Consider leaving a ⭐ on GitHub or <a href=\"https://ko-fi.com/rigle\"\
  \ rel=\"nofollow\">buying me a coffee</a>!</em></p>\n<h3 dir=\"auto\">Included assets</h3>\n\
  <ul dir=\"auto\">\n<li><code class=\"notranslate\">3dslibris.cia</code></li>\n<li><code\
  \ class=\"notranslate\">3dslibris-debug.cia</code></li>\n<li><code class=\"notranslate\"\
  >3dslibris.3dsx</code></li>\n<li><code class=\"notranslate\">3dslibris-debug.3dsx</code></li>\n\
  <li><code class=\"notranslate\">3dslibris-sdmc.zip</code> (runtime files only; pair\
  \ it with the <code class=\"notranslate\">.3dsx</code> asset for Homebrew Launcher\
  \ installs)</li>\n<li><code class=\"notranslate\">3dslibris-source.tar.gz</code></li>\n\
  </ul>"
updated: '2026-04-28T08:36:06Z'
version: v2.6.0
version_title: v2.6.0
---
