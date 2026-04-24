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
    size: 39034920
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.2/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39265216
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.2/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 32794763
    size_str: 31 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.2/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67924801
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.2/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39122132
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.2/3dslibris.3dsx
  3dslibris.cia:
    size: 39351232
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.4.2/3dslibris.cia
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
stars: 95
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.4.2</h2>

  <p dir="auto">Stability and crash-fix release.</p>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li><strong>FontManager null dereference crash</strong>: <code class="notranslate">GetFace()</code>
  used <code class="notranslate">std::map::operator[]</code>, which silently inserted
  a <code class="notranslate">NULL</code> <code class="notranslate">FT_Face</code>
  for missing style keys. Callers then dereferenced <code class="notranslate">face-&gt;size</code>,
  causing a data abort at offset <code class="notranslate">0x58</code> from <code
  class="notranslate">NULL</code>. <code class="notranslate">GetFace()</code> now
  uses <code class="notranslate">find()</code> and returns <code class="notranslate">NULL</code>
  for missing keys; all callers (<code class="notranslate">GetHeight()</code>, <code
  class="notranslate">GetGlyphIndex()</code>, both <code class="notranslate">GetFontName()</code>
  overloads) guard against <code class="notranslate">NULL</code> before dereferencing.</li>

  <li><strong>Division by zero in browser marquee</strong>: the background color averaging
  loop in <code class="notranslate">BrowserGridView</code> divided by <code class="notranslate">vis_w
  * sh</code> without checking for zero-dimension covers, leading to a divide-by-zero
  when a book had no valid thumbnail. Guarded with <code class="notranslate">if (bg_pixels
  &gt; 0)</code>.</li>

  <li><strong>Degenerate layout when font height is zero</strong>: if <code class="notranslate">GetHeight()</code>
  returned <code class="notranslate">0</code> (for example, when no valid face was
  loaded), button and line heights collapsed to <code class="notranslate">0</code>
  and produced unreadable or non-interactive menus. Added a <code class="notranslate">line_height</code>
  floor of <code class="notranslate">10</code> pixels in <code class="notranslate">font.cpp</code>
  and <code class="notranslate">paged_list_menu.cpp</code>.</li>

  <li><strong>Out-of-bounds touch in empty list menus</strong>: <code class="notranslate">PagedListMenu::HandleTouchInput()</code>
  accessed <code class="notranslate">buttons[0]</code> without checking whether the
  vector was empty, causing an out-of-bounds read on menus with no entries. Added
  an early <code class="notranslate">return</code> when <code class="notranslate">buttons.empty()</code>.</li>

  <li><strong>Infinite loop in text wrapping</strong>: <code class="notranslate">WrapTextToLines()</code>
  could spin forever when <code class="notranslate">Utf8BytesForDisplayChars()</code>
  returned <code class="notranslate">0</code> (for example, on a zero-width or unrecognised
  code point). Forced a minimum advance of <code class="notranslate">1</code> byte
  so the loop always makes progress.</li>

  </ul>

  <hr>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">3dslibris wouldn''t be the same without your support! This version
  is dedicated to:</p>

  <ul dir="auto">

  <li><strong>Reading Milestones:</strong> Huge thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/runarcn/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/runarcn">@runarcn</a>
  at <a href="https://runarcn.no" rel="nofollow">runarcn.no</a> for the lovely write-up!
  Knowing that the app helped you finish two books in two weeks is the best motivation.</li>

  <li><strong>Issues &amp; Feedback:</strong> Thanks to everyone opening issues and
  suggesting features. In v2.4.2, reports from <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Davetheword/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Davetheword">@Davetheword</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/runarcn/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/runarcn">@runarcn</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4305833981"
  data-permission-text="Title is private" data-url="https://github.com/RigleGit/3dslibris/issues/55"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/55/hovercard"
  href="https://github.com/RigleGit/3dslibris/issues/55">#55</a> made it possible
  to track down these problems. I also want to give a special thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/EmbersFlying/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/EmbersFlying">@EmbersFlying</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lunapanshiel/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lunapanshiel">@lunapanshiel</a>,
  who have helped a lot by reporting and investigating issues since the beginning.</li>

  <li><strong>Fueling the Code:</strong> A special thank you to my <strong>Ko-fi supporters</strong>.
  Your donations help keep the project going — and keep me caffeinated.</li>

  </ul>

  <p dir="auto"><em>Want to support the project? Consider leaving a ⭐ on GitHub or
  <a href="https://ko-fi.com/rigle" rel="nofollow">buying me a coffee</a>!</em></p>

  <h3 dir="auto">Included assets</h3>

  <ul dir="auto">

  <li><code class="notranslate">3dslibris.cia</code></li>

  <li><code class="notranslate">3dslibris-debug.cia</code></li>

  <li><code class="notranslate">3dslibris.3dsx</code></li>

  <li><code class="notranslate">3dslibris-debug.3dsx</code></li>

  <li><code class="notranslate">3dslibris-sdmc.zip</code></li>

  <li><code class="notranslate">3dslibris-source.tar.gz</code></li>

  </ul>'
updated: '2026-04-22T13:30:15Z'
version: v2.4.2
version_title: v2.4.2
---
