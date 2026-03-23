---
author: Rigle
avatar: https://avatars.githubusercontent.com/u/8595185?v=4
categories:
- app
color: '#bfa387'
color_bg: '#806d5a'
created: '2026-03-12T11:06:40Z'
description: An ebook reader for Nintendo 3DS
download_page: https://github.com/RigleGit/3dslibris/releases
downloads:
  3dslibris-debug.3dsx:
    size: 1391164
    size_str: 1 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v1.0.3/3dslibris-debug.3dsx
  3dslibris-sdmc.zip:
    size: 3151101
    size_str: 3 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v1.0.3/3dslibris-sdmc.zip
  3dslibris.3dsx:
    size: 1385100
    size_str: 1 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v1.0.3/3dslibris.3dsx
  3dslibris.cia:
    size: 1060288
    size_str: 1 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v1.0.3/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
qr:
  3dslibris.cia: https://db.universal-team.net/assets/images/qr/3dslibris-cia.png
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/menu.png
- description: Reading
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/reading.png
source: https://github.com/RigleGit/3dslibris
stars: 35
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 1.0.3</h2>

  <p dir="auto">This release fixes the direction of horizontal controls in the settings
  UI and defers book relayout until the book is reopened. It also restores working
  <code class="notranslate">.cia</code> packaging for hardware and Azahar.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li>Pressing right on settings rows such as font size and paragraph spacing now
  increases the value.</li>

  <li>Pressing left now decreases the value, matching the on-screen arrows and touch
  layout.</li>

  <li>Horizontal navigation inside the settings list is aligned with the same left/right
  direction.</li>

  <li>The main browser splash now shows the app version centered at the bottom of
  the left screen.</li>

  <li>Changing font size, paragraph spacing, orientation, or reading fonts no longer
  tries to repaginate the book inside the settings menu.</li>

  <li>When layout-related settings change, the app shows a warning and applies the
  new layout after reopening the current book.</li>

  <li>MOBI parsing is more resilient against empty or corrupt files and now shows
  a readable error instead of a raw numeric failure.</li>

  <li>MOBI books now have an optional per-book <code class="notranslate">line wrap
  fix</code> for badly converted files that hard-wrap normal prose into many short
  blocks.</li>

  <li>The <code class="notranslate">.cia</code> packaging flow was rebuilt around
  the same <code class="notranslate">makerom</code>/<code class="notranslate">bannertool</code>
  process used by Universal-Updater.</li>

  <li>Previous <code class="notranslate">1.0.3</code> test <code class="notranslate">.cia</code>
  builds could install but fail to boot because the packaged exheader ended up with
  an invalid main-thread priority.</li>

  <li>The generated <code class="notranslate">.cia</code> now boots correctly on original
  hardware and in Azahar.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>When a book is reopened after a layout change, or after toggling the per-book
  MOBI <code class="notranslate">line wrap fix</code>, reading position and existing
  bookmarks are remapped approximately and may land a few pages away from their original
  location.</li>

  <li>Some malformed MOBI files still contain source encoding or OCR artifacts that
  cannot be repaired fully by the reader.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  </ul>'
updated: '2026-03-14T13:57:05Z'
version: v1.0.3
version_title: v1.0.3
---
