---
author: xPsycho999
avatar: https://avatars.githubusercontent.com/u/47577362?v=4
categories:
- game
color: '#8c6c15'
color_bg: '#806213'
created: '2026-07-14T00:58:02Z'
download_page: https://github.com/xPsycho999/freeciv3ds/releases
downloads:
  3ds_port.3dsx:
    size: 10317124
    size_str: 9 MiB
    url: https://github.com/xPsycho999/freeciv3ds/releases/download/v0.2.0/3ds_port.3dsx
github: xPsycho999/freeciv3ds
icon: https://raw.githubusercontent.com/xPsycho999/freeciv3ds/main/icons/icon.png
image: https://raw.githubusercontent.com/xPsycho999/freeciv3ds/main/icons/icon-big.png
image_length: 24271
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
llm_generation: 'yes'
source: https://github.com/xPsycho999/freeciv3ds
stars: 0
systems:
- 3DS
title: freeciv3ds
update_notes: '<ul dir="auto">

  <li><strong>Real-time minimap</strong> on the top-screen HUD, replacing the earlier
  static/turn-info-only display, with a lightweight incremental refresh instead of
  a full-map rebuild each frame.</li>

  <li><strong>C2D_Text caching</strong> for on-screen text rendering, cutting redundant
  text-layout work per frame.</li>

  <li><strong>New 3DS Core Affinity</strong>: the Freeciv engine thread is pinned
  to the spare ARM11 core (with a <code class="notranslate">clock()</code> shim to
  support it), alongside the existing <code class="notranslate">osSetSpeedupEnable</code>
  clock boost, so the renderer no longer stalls waiting on engine/AI turns.</li>

  <li>SMDH metadata (<code class="notranslate">APP_TITLE</code>/<code class="notranslate">APP_DESCRIPTION</code>/<code
  class="notranslate">APP_AUTHOR</code>/<code class="notranslate">ICON</code>) wired
  up in the Makefile so the Homebrew Launcher shows proper app info instead of defaults.</li>

  <li>Build-system fix: <code class="notranslate">run_configure_3ds.sh</code>''s <code
  class="notranslate">--enable-sys-tolua-cmd</code> path is portable again instead
  of a hardcoded local path.</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/xPsycho999/freeciv3ds/compare/v0.1.0...v0.2.0"><tt>v0.1.0...v0.2.0</tt></a></p>'
updated: '2026-07-15T23:51:13Z'
version: v0.2.0
version_title: Freeciv 3DS v0.2.0
---
