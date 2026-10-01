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
    size: 14414984
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.9.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 13251520
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.9.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020749
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.9.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67154964
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.9.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 14541244
    size_str: 13 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.9.0/3dslibris.3dsx
  3dslibris.cia:
    size: 13386688
    size_str: 12 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.9.0/3dslibris.cia
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
stars: 171
systems:
- 3DS
title: 3dslibris
unique_ids:
- '0x3D51B'
update_notes: '<h2 dir="auto">3dslibris 2.9.0</h2>

  <p dir="auto">I''m coming back from a long hiatus (holidays heheh) with a new release
  that fixes some long-standing issues and adds a few new features. I hope you enjoy
  it!</p>

  <p dir="auto">This version brings more reliable text pagination and alignment, finer
  publisher-margin controls, lower memory usage when reopening large MOBI books, natural
  CBZ page ordering, and corrected CIA banner audio.</p>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li><strong>Smoother library navigation:</strong> respond to input before idle cover
  and metadata work. It redraws only the parts of the library that changed.</li>

  <li><strong>Faster settings changes:</strong> apply font and spacing adjustments
  immediately, then group repeated preference saves after a short pause or when settings
  are closed.</li>

  <li><strong>Faster PDF drawing:</strong> reuse page display lists across previews
  and zoom changes, and precompute image scaling coordinates.

  <ul dir="auto">

  <li>In my New 3DS debug captures, the main drawing step at zoom 4 fell from about
  163 to 120 ms (26% less time).</li>

  </ul>

  </li>

  <li><strong>Quicker CBZ page turns:</strong> keep the archive open and reuse decoded
  images across previews and zoom levels, skipping repeat reads and scaling when possible.

  <ul dir="auto">

  <li>For a 480×701 scale, measured time fell from 93 to 14 ms on New 3DS (84% less)
  and 288 to 51 ms in Azahar (82% less).</li>

  </ul>

  </li>

  <li><strong>Clearer CBZ text at low zoom:</strong> start with a higher-resolution
  image instead of requiring a zoom in and out to sharpen it, while retaining a lower-resolution
  fallback if decoding fails.</li>

  <li><strong>Lower MOBI memory use:</strong> reopen page caches larger than 16 MiB
  incrementally instead of reading them all into memory at once.</li>

  <li><strong>More control over EPUB layout:</strong> set publisher vertical spacing
  and side margins independently, globally or per book.</li>

  <li><strong>Better debug measurements:</strong> record PDF/CBZ opening, decoding,
  drawing and presentation times, plus memory use and slow library jobs, to help locate
  remaining bottlenecks.</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Redraw PDF/CBZ viewports with smoothing when the Circle Pad or C-Stick stops,
  matching stylus release.</li>

  <li>Prepare fixed-layout workers synchronously before HOME/sleep, without blocking
  joins or freeing their resources inside the APT hook. Cleanup runs after resume.
  This addresses lifecycle hazards; the HOME Menu crash reported in <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4346280911" data-permission-text="Title
  is private" data-url="https://github.com/RigleGit/3dslibris/issues/68" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/68/hovercard" href="https://github.com/RigleGit/3dslibris/issues/68">#68</a>
  is still under investigation (I can''t reproduce it with my New 3DS nor with my
  Old 3DS XL).</li>

  <li>Wait for PDF strip rendering to finish before releasing its pixels or display
  list when cancelling or changing pages.</li>

  <li>Preserve positive publisher vertical margins between blocks, including <code
  class="notranslate">1em</code> gaps that were previously consumed by the paragraph
  line break.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4599203754"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/139"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/139/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/139">#139</a>: fixed text disappearing
  between pages when a long paragraph crossed reading screens with different heights.
  Pagination now uses each screen''s limits and starts at the same text baseline as
  the renderer.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604526454"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/142"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/142/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/142">#142</a>: load embedded
  XHTML <code class="notranslate">&lt;style&gt;</code> blocks as well as linked stylesheets,
  so their alignment and publisher margins reach the page layout. Older EPUB page
  caches are rebuilt automatically.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4604526454"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/142"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/142/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/142">#142</a>: fixed centered
  and right-aligned text reverting to left alignment after the first line. Alignment
  now applies to each line while preserving intentional blank lines, including across
  screens and pages.</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5065102644"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/151"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/151/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/151">#151</a>: corrected the
  CIA HOME Menu banner audio to stereo. Added checks for the channel count and duration
  required by the banner format (my fault not reading the docs heh).</li>

  <li><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5067441150"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/152"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/152/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/152">#152</a>: fixed CBZ chapters
  and pages being sorted alphabetically instead of numerically, so <code class="notranslate">Chapter
  5</code> comes before <code class="notranslate">Chapter 10</code> and <code class="notranslate">2.png</code>
  comes before <code class="notranslate">10.png</code>, including inside nested folders.</li>

  </ul>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">Thanks to everyone who reported the issues!</p>

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
updated: '2026-09-28T21:44:14Z'
version: v2.9.0
version_title: v2.9.0
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

