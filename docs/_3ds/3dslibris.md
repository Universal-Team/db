---
author: Rigle
avatar: https://avatars.githubusercontent.com/u/8595185?v=4
categories:
- app
- media
color: '#bfa387'
color_bg: '#806d5a'
created: '2026-03-12T11:06:40Z'
description: An ebook and manga reader for Nintendo 3DS
download_page: https://github.com/RigleGit/3dslibris/releases
downloads:
  3dslibris-debug.3dsx:
    size: 14735148
    size_str: 14 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.2.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13452224
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.2.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5021452
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.2.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67638122
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.2.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14944996
    size_str: 14 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.2.0/3dslibris.3dsx
  3dslibris.cia:
    size: 13648832
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v3.2.0/3dslibris.cia
github: RigleGit/3dslibris
icon: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/icon-32x32.png
image: https://raw.githubusercontent.com/RigleGit/3dslibris/refs/heads/main/assets/release/banner.png
image_length: 48063
layout: app
license: other
license_name: Other
llm_generation: 'yes'
qr:
  3dslibris-debug.cia: https://db.universal-team.net/assets/images/qr/3dslibris-debug-cia.png
  3dslibris.cia: https://db.universal-team.net/assets/images/qr/3dslibris-cia.png
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/menu.png
- description: Reading
  url: https://db.universal-team.net/assets/images/screenshots/3dslibris/reading.png
source: https://github.com/RigleGit/3dslibris
stars: 185
systems:
- 3DS
title: 3dslibris
unique_ids:
- '0x3D51B'
update_notes: '<h2 dir="auto">3dslibris 3.2.0</h2>

  <p dir="auto">This update adds selectable control schemes (the asked one-handed),
  and fixes opening books from library search and some more issues.</p>

  <p dir="auto">I''m releasing this together with 3.1.2, so read the 3.1.2 release
  notes for the full list of changes since 3.1.1.</p>

  <h3 dir="auto">New</h3>

  <ul dir="auto">

  <li><a href="https://github.com/RigleGit/3dslibris/issues/183" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/183/hovercard">#183</a>: control
  schemes. The settings <code class="notranslate">controls (vertical)</code> and <code
  class="notranslate">controls (horizontal)</code> each choose between <code class="notranslate">Default</code>
  and <code class="notranslate">One-handed</code>, so portrait and landscape can use
  different schemes.

  <ul dir="auto">

  <li>In <code class="notranslate">One-handed</code>, a tap on D-Pad Left (vertical)
  or D-Pad Up (horizontal) toggles the bookmark, and holding it enters link and image
  selection. While selecting, the D-Pad moves the selection and D-Pad Right (vertical)
  or D-Pad Down (horizontal) opens the selected link or image. L and R leave the selection,
  and bookmark jumps move to the Circle Pad.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Fixes and improvements</h3>

  <ul dir="auto">

  <li>Library search: tapping or pressing A on an EPUB, MOBI or FB2 result now opens
  the book (There was a bug that made it not work for some books).</li>

  <li>Settings: <code class="notranslate">reset settings</code> now also resets the
  colour theme everywhere.</li>

  <li>Library: tapping a book or folder now opens it right away instead of needing
  a second tap.

  <ul dir="auto">

  <li>Touch and hold a cell to select it and see its full title on the top screen
  without opening it; dragging off the cell cancels.</li>

  </ul>

  </li>

  <li>Layout improvements:

  <ul dir="auto">

  <li>Long titles and paths no longer run past their boxes.</li>

  <li>Settings rows keep both lines inside the border.</li>

  <li>Search results, the chapter index, book information and font file names wrap
  their full text and grow or paginate to fit.</li>

  <li>The library list shows up to three lines per title, and the selected list row
  scrolls its title when it still does not fit.</li>

  </ul>

  </li>

  <li><strong>Faster first opening of MOBI, FB2 and EPUB books</strong>: the progress
  screen is repainted far less often, and MOBI and FB2 caches are written in larger
  blocks. Measured my consoles:

  <ul dir="auto">

  <li><strong>Old 3DS</strong>: a 2.9 MB MOBI drops from 46.5 s to 20.8 s (<strong>−55%</strong>),
  a 2 MB FB2 from 35.5 s to 15.9 s (<strong>−55%</strong>), a long EPUB from about
  13 s to 9.8 s (<strong>−25%</strong>), and small MOBI and FB2 books open about 40%
  faster (3.6 → 2.0 s and 2.6 → 1.6 s).</li>

  <li><strong>New 3DS</strong>: the 2.9 MB MOBI drops from 16.5 s to 12.5 s (<strong>−24%</strong>),
  a 10 MB MOBI from 45.8 s to 27.9 s (<strong>−39%</strong>), and small books open
  about 25% faster.</li>

  <li>Opening a book again from its cache still takes well under a second.</li>

  </ul>

  </li>

  <li><strong>Very large MOBI books now open on the Old 3DS</strong>: previously,
  large MOBI files (around 10 MB) caused the homebrew to crash on launch. Now, when
  a MOBI file exceeds the Old 3DS memory, it is processed in chunks using a temporary
  file on the SD card.

  <ul dir="auto">

  <li>This initial load is slow, but it works.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Downloads</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code> or <code class="notranslate">3dslibris.3dsx</code>
  for normal use.</li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code>: runtime files for Homebrew
  Launcher installs; use with the <code class="notranslate">.3dsx</code> download.</li>

  <li>Debug builds (<code class="notranslate">3dslibris-debug.cia</code> / <code class="notranslate">3dslibris-debug.3dsx</code>)
  and <code class="notranslate">3dslibris-source.tar.gz</code> are also included.</li>

  </ul>

  <p dir="auto">Thanks to everyone trying the builds and reporting issues. You can
  support the project with a ⭐ on GitHub or <a href="https://ko-fi.com/rigle" rel="nofollow">a
  coffee</a>.</p>'
updated: '2026-11-12T16:20:37Z'
version: v3.2.0
version_title: v3.2.0
---
### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>3dslibris.3dsx</summary>
<ol>
<li>Download <code>3dslibris.3dsx</code> to <code>/3ds/3dslibris.3dsx</code> on your SD card</li>
<li>Download <code>3dslibris-sdmc.zip</code></li>
<li>Extract <code>/3ds</code> from the zip to <code>/3ds</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>3dslibris.cia</summary>
<ol>
<li>Download <code>3dslibris.cia</code> to <code>/cias/3dslibris.cia</code> on your SD card</li>
<li>Download <code>3dslibris-sdmc.zip</code></li>
<li>Extract <code>/3ds</code> from the zip to <code>/3ds</code> on your SD card</li>
<li>Insert your SD card back into your 3DS and turn it on</li>
<li>Install and delete <code>/cias/3dslibris.cia</code> using FBI or GodMode9</li>
</ol>
</details>

