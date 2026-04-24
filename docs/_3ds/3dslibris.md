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
    size: 39041924
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.5.0/3dslibris-debug.3dsx
  3dslibris-debug.cia:
    size: 39277504
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.5.0/3dslibris-debug.cia
  3dslibris-sdmc.zip:
    size: 5020623
    size_str: 4 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.5.0/3dslibris-sdmc.zip
  3dslibris-source.tar.gz:
    size: 67942432
    size_str: 64 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.5.0/3dslibris-source.tar.gz
  3dslibris.3dsx:
    size: 39122520
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.5.0/3dslibris.3dsx
  3dslibris.cia:
    size: 39355328
    size_str: 37 MiB
    url: https://github.com/RigleGit/3dslibris/releases/download/v2.5.0/3dslibris.cia
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
stars: 96
systems:
- 3DS
title: 3dslibris
update_notes: '<h2 dir="auto">3dslibris 2.5.0</h2>

  <p dir="auto">Performance, stability, and new formatting support.</p>

  <h3 dir="auto">New</h3>

  <ul dir="auto">

  <li><strong>Text alignment support</strong>: <code class="notranslate">text-align:
  center</code> and <code class="notranslate">text-align: right</code> are now honoured
  in EPUB reflow. Each paragraph emits an alignment token that <code class="notranslate">Page::Draw</code>
  uses to compute per-line offset, so wrapped lines stay correctly aligned across
  the whole paragraph. See <a href="https://github.com/RigleGit/3dslibris/issues/47"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/47/hovercard">#47</a>.</li>

  <li><strong>README revamped</strong>: the README has been reorganized to better
  highlight the features of the project.</li>

  </ul>

  <h3 dir="auto">Performance</h3>

  <ul dir="auto">

  <li><strong>EPUB CSS scanning (~1 sec less loading time)</strong>: only the <code
  class="notranslate">&lt;head&gt;</code> section of each XHTML spine document is
  scanned for stylesheet links, reducing zip I/O on large books.</li>

  <li><strong>Reused zip handle (~20% less loading time)</strong>: a single <code
  class="notranslate">unzFile</code> handle is recycled across all spine CSS scans
  instead of opening/closing per document.</li>

  <li><strong>Plain text pagination</strong>: eliminated per-line heap allocation;
  uses data/size pointer streaming.</li>

  <li><strong>Text shaping pipeline</strong>: reuses static scratch buffers (<code
  class="notranslate">text_run</code>, <code class="notranslate">normalized</code>,
  <code class="notranslate">breaks</code>) instead of re-allocating on every shaped
  run.</li>

  <li><strong>Release build overhead removed</strong>: guarded <code class="notranslate">osGetTime</code>
  calls and unnecessary allocations with <code class="notranslate">DSLIBRIS_DEBUG</code>
  only.</li>

  <li><strong>Text renderer diagnostics budget raised</strong>: increased the debug
  blit page diagnostics budget from 12 to 48 entries, making short debug captures
  less likely to miss relevant draw calls.</li>

  <li><strong>Faster first-time EPUB covers (x3 speed increase)</strong>: large JPEG
  covers now try a MuPDF subsampled thumbnail decode before falling back to full-image
  <code class="notranslate">stb_image</code> decoding, reducing old3DS work for oversized
  cover art.</li>

  <li><strong>Quieter blit diagnostics</strong>: debug logs now skip steady idle blit
  frames where no dirty region or framebuffer copy occurred.</li>

  <li><strong>Safer PDF cover preparation</strong>: PDF cover warmup now runs with
  shared complexity guards on both old3DS and new3DS, skipping pathological pages
  earlier instead of risking OOM during first-time cover extraction.</li>

  </ul>

  <h3 dir="auto">Fixes</h3>

  <ul dir="auto">

  <li><strong>Browser return and suspend handling stabilized</strong>: returning from
  the reader to the library now explicitly resumes browser jobs, handles applet suspend/resume
  through the app controllers, and avoids tearing down in-flight async opens during
  HOME suspension. See <a href="https://github.com/RigleGit/3dslibris/issues/62" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/62/hovercard">#62</a>.</li>

  <li><strong>Open cancel polling is worker-safe</strong>: cancellation polling no
  longer touches HID/APT state from worker threads; background open paths now use
  an atomic cancellation flag while the main thread remains responsible for system
  event polling.</li>

  <li><strong>Gallery covers clipped correctly</strong>: cover thumbnails in gallery
  view are clipped to the rounded frame, preventing image pixels from bleeding outside
  the card border. See <a href="https://github.com/RigleGit/3dslibris/issues/59" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/59/hovercard">#59</a>.</li>

  <li><strong>PDF shouldn''t crash on HOME button</strong>: <code class="notranslate">ParseMuPdfFile</code>
  is now split into three independently cancellable steps (<code class="notranslate">fz_open_document</code>,
  <code class="notranslate">fz_count_pages</code>, <code class="notranslate">fz_load_outline</code>),
  each separated by an APT yield point via <code class="notranslate">open_cancel_poll::Poll</code>.
  Pressing HOME during PDF loading is now handled cleanly instead of causing a console
  restart. See <a href="https://github.com/RigleGit/3dslibris/issues/58" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/58/hovercard">#58</a>.</li>

  <li><strong>Worker join timeouts bounded</strong>: <code class="notranslate">LightEvent_Wait</code>
  in <code class="notranslate">CancelMuPdfIncrementalRenderState</code> replaced with
  a 100 ms polling loop; <code class="notranslate">ShutdownMuPdfWorker</code> and
  <code class="notranslate">ShutdownCbzWorker</code> now use a 500 ms join timeout
  instead of <code class="notranslate">U64_MAX</code>, preventing either path from
  blocking HOME acknowledgment indefinitely. See <a href="https://github.com/RigleGit/3dslibris/issues/58"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/58/hovercard">#58</a>.</li>

  <li><strong>Bookmarks button icon updated</strong>: refreshed the bookmarks button
  artwork. See <a href="https://github.com/RigleGit/3dslibris/issues/60" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/60/hovercard">#60</a>.</li>

  <li><strong>Large EPUB page limit raised</strong>: <code class="notranslate">kMaxPagesInMemory</code>
  raised from 5 000 → 25 000 and cache guard to 50 000, fixing books that stopped
  loading halfway through. See <a href="https://github.com/RigleGit/3dslibris/issues/54"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/54/hovercard">#54</a>
  and <a href="https://github.com/RigleGit/3dslibris/issues/37" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/37/hovercard">#37</a>.</li>

  <li><strong>HR overflow tracking</strong>: parser and renderer now agree on <code
  class="notranslate">pen.y</code> after <code class="notranslate">&lt;hr&gt;</code>
  rules, preventing <code class="notranslate">&lt;hr/&gt; &lt;p&gt;Text&lt;/p&gt;</code>
  from overlapping text. See <a href="https://github.com/RigleGit/3dslibris/issues/37"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/37/hovercard">#37</a>.</li>

  <li><strong>PagedListMenu overflow</strong>: pagination indices changed from <code
  class="notranslate">u8</code> to <code class="notranslate">u16</code> so menus with
  more than 255 entries no longer wrap and corrupt the page list.</li>

  <li><strong>MOBI synchronous-only open</strong>: removed the deferred-finalize path
  that could leave the reader in an inconsistent state on large MOBI files.</li>

  <li><strong>Startup font path cleanup</strong>: removed hardcoded RomFS font paths;
  all runtime asset discovery now goes through <code class="notranslate">paths::kRomfsFontDir</code>.</li>

  <li><strong>Reflow open gate simplified</strong>: removed stale <code class="notranslate">ForceSynchronousBookOpen</code>
  flag and <code class="notranslate">deferred_pumped</code> references; <code class="notranslate">ShouldUseAsyncReflowOpen</code>
  is now a single-parameter function.</li>

  <li><strong>Permanent cover failures stop retrying</strong>: browser warmup now
  stops requeueing covers after non-recoverable failures, avoiding repeated work on
  unsupported files.</li>

  <li><strong>Gallery redraws after visible cover jobs</strong>: finishing a cover
  job for a visible gallery item now forces a browser redraw, preventing stale tiles
  after first-time cover extraction.</li>

  <li><strong>Raw SVG gallery covers are skipped cleanly</strong>: EPUBs whose detected
  cover is a raw SVG now fall back to the no-cover placeholder instead of going through
  an unsupported decode path.</li>

  <li><strong>No-cover gallery placeholder cleaned up</strong>: generated placeholders
  now keep the frame visible, use tighter centered metadata text, and inherit the
  active theme fill color. See <a href="https://github.com/RigleGit/3dslibris/issues/59"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/59/hovercard">#59</a>.</li>

  </ul>

  <h3 dir="auto">Packaging</h3>

  <ul dir="auto">

  <li><strong>SDMC zip trimmed</strong>: <code class="notranslate">3dslibris-sdmc.zip</code>
  now contains only SD card runtime files. The <code class="notranslate">.3dsx</code>
  builds remain separate release assets instead of being duplicated inside the zip.</li>

  </ul>

  <hr>

  <h2 dir="auto">❤️ Community Shoutouts</h2>

  <p dir="auto">3dslibris wouldn''t be the same without your support! This version
  is dedicated to:</p>

  <ul dir="auto">

  <li><strong>Text alignment</strong>: Thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/EmbersFlying/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/EmbersFlying">@EmbersFlying</a>
  for opening <a href="https://github.com/RigleGit/3dslibris/issues/47" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/47/hovercard">#47</a> and pushing
  for <code class="notranslate">text-align: center</code> and <code class="notranslate">text-align:
  right</code> support in EPUB reflow.</li>

  <li><strong>Large book reports</strong>: Thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Davetheword/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Davetheword">@Davetheword</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/EmbersFlying/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/EmbersFlying">@EmbersFlying</a>
  for reporting <a href="https://github.com/RigleGit/3dslibris/issues/54" data-hovercard-type="issue"
  data-hovercard-url="/RigleGit/3dslibris/issues/54/hovercard">#54</a> and <a href="https://github.com/RigleGit/3dslibris/issues/37"
  data-hovercard-type="issue" data-hovercard-url="/RigleGit/3dslibris/issues/37/hovercard">#37</a>:
  those issues led to raising the page limit to 25.000 and fixing the <code class="notranslate">&lt;hr&gt;</code>
  overflow overlap bug.</li>

  <li><strong>Bug triaging</strong>: Thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/runarcn/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/runarcn">@runarcn</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/EmbersFlying/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/EmbersFlying">@EmbersFlying</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lunapanshiel/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lunapanshiel">@lunapanshiel</a>
  and @TrevorArenival07 for testing and reporting multiple issues that were fixed
  (or at least tried) in this release.</li>

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
updated: '2026-04-24T14:47:35Z'
version: v2.5.0
version_title: v2.5.0
---
