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
  PocketCompiler.v0-42.3dsx:
    size: 702888
    size_str: 686 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.42/PocketCompiler.v0-42.3dsx
github: PlanetDogeCodes/Pocket-Compiler
icon: https://db.universal-team.net/assets/images/icons/pocket-compiler.png
image: https://db.universal-team.net/assets/images/images/pocket-compiler.png
image_length: 14156
layout: app
license: apache-2.0
license_name: Apache License 2.0
llm_generation: 'yes'
source: https://github.com/PlanetDogeCodes/Pocket-Compiler
stars: 5
systems:
- 3DS
title: Pocket-Compiler
update_notes: '<p dir="auto">This update changes the way that styling is handled and
  fixes some control issues on 3DS consoles</p>

  <h2 dir="auto">All Major Changes</h2>

  <h3 dir="auto">CSS Transitions</h3>

  <p dir="auto"><code class="notranslate">transition: 0.3s ease-in-out</code> now
  actually animates. When a style property changes on an element with a transition
  duration, the old and new values are interpolated over the duration using smoothstep
  easing. Supports 25 numeric properties (opacity, width, height, margins, padding,
  position, font-size, border, transforms) plus color properties (color, background)
  which interpolate per-channel. The transition engine runs in the frame loop and
  marks transitioning nodes dirty so layout re-runs each frame to reflect the changing
  values.</p>

  <h3 dir="auto">Box-Shadow</h3>

  <p dir="auto"><code class="notranslate">box-shadow: 2px 2px 4px rgba(0,0,0,0.5)</code>
  is parsed into offset/blur/color and drawn as a semi-transparent rect behind the
  element before the background fill. No real gaussian blur (3DS hardware can''t do
  that efficiently), but the spread approximation looks reasonable for most UI shadows.</p>

  <h3 dir="auto">Linear-Gradient Backgrounds</h3>

  <p dir="auto"><code class="notranslate">background: linear-gradient(to right, red,
  blue)</code> is parsed into start/end colors and a direction, then rendered as 16
  interpolated color bands. Supports <code class="notranslate">to right/bottom/left/top</code>
  directions and <code class="notranslate">Ndeg</code> angles. Falls back to solid
  <code class="notranslate">background</code> color when no gradient is active. Transparent
  colors work correctly (uses explicit "set" flags instead of checking for zero).</p>

  <h3 dir="auto">CSS Grid Layout</h3>

  <p dir="auto"><code class="notranslate">display: grid</code> with <code class="notranslate">grid-template-columns</code>
  now lays out children in a grid. Supports fixed pixel widths, <code class="notranslate">fr</code>/<code
  class="notranslate">auto</code> (equal distribution), and <code class="notranslate">repeat(N,
  ...)</code> syntax up to 8 columns. Rows auto-size to the tallest cell, gap is applied
  between cells, and children are vertically centered within their row.</p>

  <h3 dir="auto">CSS <code class="notranslate">calc()</code></h3>

  <p dir="auto"><code class="notranslate">calc(100% - 20px)</code> is now evaluated
  at layout time. Supports <code class="notranslate">+</code>, <code class="notranslate">-</code>,
  <code class="notranslate">*</code>, <code class="notranslate">/</code> with correct
  operator precedence, and all length units (px, em, rem, vw, vh, %) work inside calc
  terms. Self-contained in the length parser — no new systems.</p>

  <h3 dir="auto">Form Submission</h3>

  <p dir="auto">Clicking a <code class="notranslate">&lt;button type="submit"&gt;</code>
  or <code class="notranslate">&lt;input type="submit"&gt;</code> inside a <code class="notranslate">&lt;form&gt;</code>
  now fires the form''s <code class="notranslate">onsubmit</code> handler and dispatches
  a <code class="notranslate">submit</code> event. This replaces the old START-key
  approach which conflicted with START=exit-run-mode.</p>

  <h3 dir="auto">Keybind Conflict Fixes</h3>

  <p dir="auto">Resolved button assignment conflicts between the app shell and web
  content event system. In run mode, only DPad (arrow keys) and Y (Space) generate
  keyboard events for web content. A/B/X/L/R/START are exclusively mouse clicks, cursor
  lock, and exit-run-mode — no more phantom keydown events alongside mouse clicks.</p>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>IndexedDB path overflow: <code class="notranslate">store</code>/<code class="notranslate">key</code>
  strings from JS are now length-validated to prevent path truncation</li>

  <li>IndexedDB <code class="notranslate">get()</code> return logic: was returning
  true for empty files</li>

  <li>IndexedDB <code class="notranslate">clear()</code> prefix buffer: enlarged from
  80 to 128 bytes to handle longer store names</li>

  <li>Transition color precision: RGBA8 colors now stored as uint32 (not float) to
  avoid precision loss past 2^24</li>

  <li>Gradient transparent-color: <code class="notranslate">0x00000000</code> (transparent)
  no longer treated as "unset"</li>

  </ul>'
updated: '2026-07-07T18:34:55Z'
version: v0.42
version_title: Compiled 3DSX (Version 0.42)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!