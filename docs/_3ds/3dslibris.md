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
    size: 14401128
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.1/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13145024
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.1/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.1/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 66978777
    size_str: 63 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.1/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14528176
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.1/3dslibris.3dsx
  3dslibris.cia:
    size: 13280192
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.8.1/3dslibris.cia
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
stars: 135
systems:
- 3DS
title: 3dslibris
unique_ids:
- '0x3D51B'
update_notes: '<h2 dir="auto">3dslibris 2.8.1</h2>

  <p dir="auto">Better personalized covers, more accurate EPUB publisher styling,
  safer fixed-layout rendering, and reliable reading progress across library folders.</p>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4654518746"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/144"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/144/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/144">#144</a>: improved personalized
  cover scaling and rendering quality so external cover images more closely match
  covers extracted from EPUB and CBZ files.</li>

  <li>Reduced internal coupling around input, menus, settings, fonts, and library
  jobs to make navigation and future maintenance safer.</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4689259664"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/145"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/145/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/145">#145</a>: fixed reading
  progress and bookmarks being lost after leaving a library subfolder and entering
  it again, including after restarting the app.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604526454"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/142"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/142/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/142">#142</a>: fixed EPUB publisher
  <code class="notranslate">text-indent</code> rules being ignored while preserving
  explicit no-indent classes such as <code class="notranslate">.left</code>.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604526454"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/142"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/142/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/142">#142</a>: fixed publisher
  block margins appearing too wide on the 3DS screen and vertical spacing below block
  or page-break images being discarded.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4599203754"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/139"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/139/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/139">#139</a>: fixed pagination
  near the bottom safety area skipping text between pages.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4599203754"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/139"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/139/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/139">#139</a>: fixed large font
  sizes placing the final visible line too close to the bottom clip area, which could
  make text appear missing between pages.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4346280911"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/68"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>: stopped repeated
  high-resolution MuPDF render attempts after an allocation failure, reducing the
  risk of black screens, instability, or crashes when returning to the HOME Menu under
  memory pressure.</li>

  </ul>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">Thanks to everyone who tested personalized covers and subfolder progress,
  and to everyone who shared EPUB samples, screenshots, and HOME Menu crash logs!</p>

  <ul dir="auto">

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
updated: '2026-06-23T15:43:37Z'
version: v2.8.1
version_title: v2.8.1
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

