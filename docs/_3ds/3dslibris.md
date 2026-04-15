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
    size: 39167944
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.1/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39396288
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.1/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32767568
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.1/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66548015
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.1/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39140176
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.1/3dslibris.3dsx
  3dslibris.cia:
    size: 39371712
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.2.1/3dslibris.cia
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
stars: 82
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.2.1</h2>

  <p dir="auto">This release builds on <code class="notranslate">v2.2.0</code> with
  a faster library browsing option and a cleaner debug-install workflow.</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/a13cde9f-8f62-4dde-a208-04bf062fb04a"><img
  width="600" alt="imagen" src="https://github.com/user-attachments/assets/a13cde9f-8f62-4dde-a208-04bf062fb04a"
  style="max-width: 100%;"></a>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>Optional library list view</strong>: settings now let you switch the
  browser between the existing cover gallery and a DSLibris-style list view that loads
  only titles, starts faster, and is easier to navigate on large libraries.</li>

  <li><strong>List view is fully integrated</strong>: the new mode is saved in the
  XML preferences, works even with no book currently open, supports vertical navigation,
  and keeps the existing browser flow intact.</li>

  <li><strong>Long titles are handled better in the list</strong>: list rows now use
  the dedicated presentation path introduced for this feature, with clearer rendering
  and spacing for long display names.</li>

  <li><strong>Debug and release CIA builds can coexist</strong>: <code class="notranslate">3dslibris-debug.cia</code>
  now uses its own Title ID/Product Code so it installs separately instead of overwriting
  the release build.</li>

  </ul>

  <h3 dir="auto">Included fixes and behavior changes</h3>

  <ul dir="auto">

  <li><strong>Browser presentation is split cleanly by mode</strong>: grid and list
  rendering now live in separate presentation files while <code class="notranslate">app_browser.cpp</code>
  remains the coordinator for shared navigation and actions.</li>

  <li><strong>Preformatted host wrapping stays correct</strong>: the host-side regression
  fix for hard wrapping in preformatted text is included in this release train.</li>

  <li><strong>Release automation still publishes the full artifact set</strong>: the
  release workflow continues to generate and attach both CIA variants, both 3DSX variants,
  the SD package, and the source tarball.</li>

  </ul>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-15T12:52:13Z'
version: v2.2.1
version_title: v2.2.1
---
