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
    size: 38991720
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39224256
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32759720
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67915077
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39056572
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.0/3dslibris.3dsx
  3dslibris.cia:
    size: 39285696
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.0/3dslibris.cia
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
stars: 91
systems:
- 3DS
title: 3dslibris
update_notes: "<h2 dir=\"auto\">3dslibris 2.4.0</h2>\n<p dir=\"auto\"><strong>UI and\
  \ navigation overhaul.</strong> This release delivers a six-color theme system,\
  \ improved menus throughout, dark/light splash screen variants, gradient backgrounds\
  \ in the reader, EPUB chapter detection fixes, and browser warmup re-enabled for\
  \ faster cover loading.</p>\n<p dir=\"auto\"><strong>UPDATE YOUR <code class=\"\
  notranslate\">3dslibris-sdmc.zip</code> TO HAVE THE NEWEST SPLASHES</strong>.</p>\n\
  <markdown-accessiblity-table><table role=\"table\">\n  <tbody><tr>\n    <td width=\"\
  50%\"><a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/6de341bf-7811-4e70-be73-6e0aa4ca62ac\"\
  ><img width=\"640\" height=\"531\" alt=\"3dslibris_darksepia\" src=\"https://github.com/user-attachments/assets/6de341bf-7811-4e70-be73-6e0aa4ca62ac\"\
  \ style=\"max-width: 100%; height: auto; max-height: 531px;; aspect-ratio: 640 /\
  \ 531; background-color: var(--bgColor-muted); border-radius: 6px; display: block\"\
  \ class=\"js-gh-image-fallback\"></a></td>\n    <td width=\"50%\"> <a target=\"\
  _blank\" rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/9874a40f-47d7-4c07-9f35-a90dd63edc9c\"\
  ><img width=\"640\" height=\"531\" alt=\"3dslibris_light\" src=\"https://github.com/user-attachments/assets/9874a40f-47d7-4c07-9f35-a90dd63edc9c\"\
  \ style=\"max-width: 100%; height: auto; max-height: 531px;; aspect-ratio: 640 /\
  \ 531; background-color: var(--bgColor-muted); border-radius: 6px; display: block\"\
  \ class=\"js-gh-image-fallback\"></a></td>\n  </tr>\n</tbody></table></markdown-accessiblity-table>\n\
  <h3 dir=\"auto\">Highlights</h3>\n<ul dir=\"auto\">\n<li><strong>Six-color theme\
  \ system</strong>: the app now supports six palette-based color themes (light, sepia,\
  \ dark, and three more), each controlling text, background, UI chrome, and cover\
  \ overlays consistently across all views.</li>\n<li><strong>Dark/light splash screen\
  \ variants</strong>: the startup splash now uses a dark or light version that matches\
  \ the active color mode, replacing the single legacy <code class=\"notranslate\"\
  >splash.jpg</code> with theme-aware <code class=\"notranslate\">3DSLibris_dark_small.jpg</code>\
  \ / <code class=\"notranslate\">3DSLibris_light_small.jpg</code>.</li>\n<li><strong>Cycle\
  \ themes with X in the browser</strong>: press <code class=\"notranslate\">X</code>\
  \ in the library view to cycle through color modes without opening the settings\
  \ menu.</li>\n<li><strong>Gradient backgrounds in reader mode</strong>: the top\
  \ and bottom strips of the reading view now use a smooth gradient instead of a flat\
  \ color.</li>\n<li><strong>Improved bookmark menu</strong>: entries now show a preview\
  \ of the page text alongside the bookmark position, making it easier to identify\
  \ saved positions at a glance.</li>\n<li><strong>Improved chapter menu</strong>:\
  \ chapter titles wrap to up to three lines so long titles are no longer truncated.</li>\n\
  <li><strong>Dynamic row heights in PagedListMenu</strong>: the shared paged-list\
  \ component now sizes rows dynamically per page so entries always fit the available\
  \ screen space.</li>\n<li><strong>Long font filenames wrap in FontMenu</strong>:\
  \ font file paths too long for a single line now wrap cleanly instead of being clipped.</li>\n\
  <li><strong>Browser warmup re-enabled</strong>: cover extraction now runs incrementally\
  \ on idle frames (3 ms budget), so covers populate without stalling the UI. Extraction\
  \ is deferred to idle time and never runs during menu transitions.</li>\n</ul>\n\
  <h3 dir=\"auto\">Fixes and behavior changes</h3>\n<ul dir=\"auto\">\n<li><code class=\"\
  notranslate\">TryLoadCoverCache</code> no longer runs synchronous cover extraction\
  \ when browser warmup is active — extraction is now deferred to idle <code class=\"\
  notranslate\">ProcessJobs</code> calls. This prevents the freeze-on-toggle regression\
  \ seen with warmup enabled.</li>\n<li><code class=\"notranslate\">Button::SetLabel3</code>\
  \ / <code class=\"notranslate\">GetX</code> / <code class=\"notranslate\">GetY</code>\
  \ added to support three-line button labels in menus.</li>\n<li><code class=\"notranslate\"\
  >PagedListMenu</code> row height is now computed per-page rather than fixed, accommodating\
  \ variable-length entries.</li>\n<li>EPUB NAV spine ordering fixed: chapter detection\
  \ now correctly follows the <code class=\"notranslate\">&lt;spine&gt;</code> order\
  \ from the OPF manifest rather than assuming document order. Test fixtures added\
  \ for this path.</li>\n<li>Marquee background color in the browser grid now correctly\
  \ tracks the active dark theme background instead of always using the light color.</li>\n\
  <li><code class=\"notranslate\">debug_runtime::BrowserWarmupDisabled()</code> returns\
  \ <code class=\"notranslate\">false</code> — warmup is active by default in release\
  \ builds.</li>\n</ul>\n<h3 dir=\"auto\">What comes next</h3>\n<p dir=\"auto\">Remaining\
  \ workers to re-enable one at a time as each is confirmed stable on hardware: MOBI\
  \ deferred finalize, then EPUB/FB2/MOBI reflow worker, then CBZ interactive preload,\
  \ then PDF strip worker.</p>\n<h3 dir=\"auto\">Included assets</h3>\n<ul dir=\"\
  auto\">\n<li><code class=\"notranslate\">3dslibris.cia</code></li>\n<li><code class=\"\
  notranslate\">3dslibris-debug.cia</code></li>\n<li><code class=\"notranslate\">3dslibris.3dsx</code></li>\n\
  <li><code class=\"notranslate\">3dslibris-debug.3dsx</code></li>\n<li><code class=\"\
  notranslate\">3dslibris-sdmc.zip</code></li>\n<li><code class=\"notranslate\">3dslibris-source.tar.gz</code></li>\n\
  </ul>"
updated: '2026-04-21T18:02:53Z'
version: v2.4.0
version_title: v2.4.0
---
