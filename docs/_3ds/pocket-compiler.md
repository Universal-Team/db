---
author: Planet Doge
avatar: https://avatars.githubusercontent.com/u/142177581?v=4
categories:
- utility
- app
color: '#c8c8c8'
color_bg: '#808080'
created: '2026-05-20T00:17:27Z'
description: An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS
  consoles.
download_page: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases
downloads:
  PocketCompiler.v0-34.3dsx:
    size: 662700
    size_str: 647 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.34/PocketCompiler.v0-34.3dsx
github: PlanetDogeCodes/Pocket-Compiler
icon: https://db.universal-team.net/assets/images/icons/pocket-compiler.png
image: https://db.universal-team.net/assets/images/images/pocket-compiler.png
image_length: 14156
layout: app
license: apache-2.0
license_name: Apache License 2.0
llm_usage: undisclosed
source: https://github.com/PlanetDogeCodes/Pocket-Compiler
stars: 3
systems:
- 3DS
title: Pocket-Compiler
update_notes: '<p dir="auto">The compiled, install-and-play .3dsx file of the first
  fully featured HTML compiler made for 3DS/n3DS consoles.</p>

  <p dir="auto">CIA files will be added for release 1.0</p>

  <p dir="auto">What Was Changed This Update:</p>

  <ul dir="auto">

  <li>Slight UI changes</li>

  <li>Bordered rendering for text &amp; iframe</li>

  <li>Memory usage fixes</li>

  <li>More accurate CSS parsing</li>

  </ul>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>File</th>

  <th>Fixes/Changes</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">web_layout.c</code></td>

  <td>Body <code class="notranslate">avail_w</code> bug fixed: was <code class="notranslate">2×margin_left</code>,
  now <code class="notranslate">margin_left + margin_right</code>.</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_layout.c</code></td>

  <td>Text node <code class="notranslate">lay_w</code> uses full available container
  width for alignment.</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_render.c</code></td>

  <td>Scale formula <code class="notranslate">size/11.0f</code> → <code class="notranslate">size/30.0f</code>
  (correct for system font at scale 1.0 ≈ 30px).</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_render.c</code></td>

  <td>TEXT nodes use parent container width for proper text alignment.</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_render.c</code></td>

  <td>Bottom border drawn on document viewport to frame the output area.</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_engine.c</code></td>

  <td><code class="notranslate">css_apply_ua_defaults()</code> called after <code
  class="notranslate">css_reset()</code>, before parse — so user styles always win.</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_engine.c</code></td>

  <td>RUNNING bar cleaned up; conflicting title bar overlay removed.</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto">Note: Crashing is a recurring issue. If your 3DS crashes while using
  PocketCompiler, please open an issue and describe what you were doing at the time
  of the crash.</p>'
updated: '2026-06-15T20:46:39Z'
version: v0.34
version_title: Compiled 3DSX (Release v0.34)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!