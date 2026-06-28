---
author: bubble2k16 / matbo87 / willjow / Xeddius-Network
avatar: https://avatars.githubusercontent.com/u/4026393?v=4
categories:
- emulator
color: '#635e5e'
color_bg: '#635e5e'
created: '2019-01-15T09:19:13Z'
description: SNES9x Port for 3DS / 2DS
download_page: https://github.com/matbo87/snes9x_3ds/releases
downloads:
  snes9x_3ds.3dsx:
    size: 2492636
    size_str: 2 MiB
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v1.61/snes9x_3ds.3dsx
  snes9x_3ds.cia:
    size: 2409408
    size_str: 2 MiB
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v1.61/snes9x_3ds.cia
github: matbo87/snes9x_3ds
icon: https://raw.githubusercontent.com/matbo87/snes9x_3ds/master/resources/icon.png
image: https://raw.githubusercontent.com/matbo87/snes9x_3ds/master/resources/icon.png
image_length: 3285
layout: app
license: other
license_name: Other
llm_generation: 'yes'
qr:
  snes9x_3ds.cia: https://db.universal-team.net/assets/images/qr/snes9x_3ds-cia.png
screenshots:
- description: Loading a game
  url: https://db.universal-team.net/assets/images/screenshots/snes9x-updated-fork/loading-a-game.png
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/snes9x-updated-fork/menu.png
- description: Playing a game
  url: https://db.universal-team.net/assets/images/screenshots/snes9x-updated-fork/playing-a-game.png
source: https://github.com/matbo87/snes9x_3ds
stars: 69
systems:
- 3DS
title: Snes9x (updated fork)
unique_ids:
- '0x3849'
update_notes: '<h3 dir="auto">Features</h3>

  <ul dir="auto">

  <li>Added 3D depth strength setting and refined splash/background depth effects
  (<a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4318088071"
  data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/65"
  data-hovercard-type="issue" data-hovercard-url="/matbo87/snes9x_3ds/issues/65/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/issues/65">#65</a>)

  <ul dir="auto">

  <li>Custom game-screen backgrounds are now ideally 448x256 instead of 400x240;<br>

  400x240 images can expose edges at higher 3D depth settings.</li>

  <li>Updated 448x256 game-screen backgrounds are available in the <a href="https://github.com/matbo87/snes9x_3ds-assets/releases/tag/v1.1.0">snes9x_3ds-assets
  v1.1.0</a> release.</li>

  </ul>

  </li>

  <li>Added save-state screenshot previews</li>

  <li>Added per-game crop/overscan control (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4266231246" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/55"
  data-hovercard-type="issue" data-hovercard-url="/matbo87/snes9x_3ds/issues/55/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/issues/55">#55</a>)</li>

  <li>Added scanlines</li>

  <li>Added Mode 7 bilinear smoothing (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4414555989" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/68"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/68/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/68">#68</a>)</li>

  <li>Added Frame Sync setting with VBlank/Sleep pacing options

  <ul dir="auto">

  <li>Sleep Sync can make games run smoother when they stutter or won''t hold full
  speed, e.g. DKC2 on Old 3DS.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Rendering &amp; Compatibility</h3>

  <ul dir="auto">

  <li>Improved HDMA/in-frame palette compatibility for games with mid-frame palette
  changes (<a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="4581682287" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/73"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/73/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/73">#73</a>)

  <ul dir="auto">

  <li>Helps games such as Top Gear and Super Turrican; see <a href="KNOWN_ISSUES.md#in-frame-palette-changes">In-frame
  palette changes</a>.</li>

  </ul>

  </li>

  <li>Added mosaic rendering support (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4515183650" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/70"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/70/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/70">#70</a>)</li>

  <li>Fixed stale core data after switching ROMs</li>

  <li>Fixed several game-specific rendering/timing issues

  <ul dir="auto">

  <li>Includes fixes for Sim City intro, Jurassic Park transparency and Super Bases
  Loaded 2 crash.</li>

  </ul>

  </li>

  <li>Optimized Mode 7 tile 0 blit (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4414545249" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/67"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/67/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/67">#67</a>)</li>

  </ul>

  <h3 dir="auto">Audio</h3>

  <ul dir="auto">

  <li>Migrated audio output from CSND to NDSP and improved audio scheduling/stability
  (<a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4298937329"
  data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/58"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/58/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/58">#58</a>, <a class="commit-link"
  data-hovercard-type="commit" data-hovercard-url="https://github.com/matbo87/snes9x_3ds/commit/7ff81cc18ee599792788765641c46d07ad427c4a/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/commit/7ff81cc18ee599792788765641c46d07ad427c4a"><tt>7ff81cc</tt></a>)</li>

  <li>Added audio buffer size setting

  <ul dir="auto">

  <li>Lower values reduce latency; higher values reduce the chance of crackling.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Documentation</h3>

  <ul dir="auto">

  <li>Added <a href="KNOWN_ISSUES.md">KNOWN_ISSUES.md</a> with compatibility notes
  for problematic games,<br>

  Satellaview (BS-X) titles and common visual/audio issues.</li>

  </ul>

  <h3 dir="auto">Credits</h3>

  <p dir="auto">Thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/f4mrfaux/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/f4mrfaux">@f4mrfaux</a>
  for contributions this release builds on:</p>

  <ul dir="auto">

  <li>NDSP audio migration built on <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4298937329" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/58"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/58/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/58">#58</a>; follow-up queue/drain,
  stability, and integration fixes were added in <a class="commit-link" data-hovercard-type="commit"
  data-hovercard-url="https://github.com/matbo87/snes9x_3ds/commit/7ff81cc18ee599792788765641c46d07ad427c4a/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/commit/7ff81cc18ee599792788765641c46d07ad427c4a"><tt>7ff81cc</tt></a></li>

  <li>Mosaic effect rendering built on <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4298937960" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/59"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/59/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/59">#59</a>, with follow-up implementation
  and cleanup in <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="4515183650" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/70"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/70/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/70">#70</a></li>

  <li>Mode 7 bilinear smoothing and Mode 7 tile 0 optimization came from <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4414545249" data-permission-text="Title
  is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/67" data-hovercard-type="pull_request"
  data-hovercard-url="/matbo87/snes9x_3ds/pull/67/hovercard" href="https://github.com/matbo87/snes9x_3ds/pull/67">#67</a>/<a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4414555989"
  data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/68"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/68/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/68">#68</a></li>

  </ul>

  <p dir="auto">For more information, see <a href="CHANGELOG.md">Changelog</a>.</p>

  <p dir="auto">Install snes9x_3ds.cia via FBI -&gt; Remote Install -&gt; Scan QR
  Code</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/d8f54962-3dff-4c05-905e-bc8edabe3e3c"><img
  width="180" height="180" alt="qr_v1 61" src="https://github.com/user-attachments/assets/d8f54962-3dff-4c05-905e-bc8edabe3e3c"
  style="max-width: 100%; height: auto; max-height: 180px;; aspect-ratio: 180 / 180;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>'
updated: '2026-06-28T18:00:50Z'
version: v1.61
version_title: v1.61
---
fork of [bubble2k's Snes9x for 3DS](https://github.com/bubble2k16/snes9x_3ds), giving you more options to enjoy your SNES game collection.