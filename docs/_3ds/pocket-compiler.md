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
  PocketCompiler.v0-47.3dsx:
    size: 712916
    size_str: 696 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.47/PocketCompiler.v0-47.3dsx
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
update_notes: '<p dir="auto">This release focuses on furthering the extent of CSS
  and JS text/style rendering compatibility and stability.<br>

  Version 0.46 was skipped due to issues with a beta build.</p>

  <h2 dir="auto">All The New Stuff</h2>

  <h3 dir="auto">Multi-line text rendering</h3>

  <p dir="auto"><code class="notranslate">wrender_text</code> previously drew the
  entire text string as a single <code class="notranslate">C2D_DrawText</code> call,
  so paragraphs that the layout engine had correctly wrapped to multiple lines rendered
  as one long line overflowing off-screen. The function now detects when text exceeds
  the available width, splits at word boundaries using the same <code class="notranslate">char_width</code>
  metric as the layout engine, and draws each line separately with correct alignment,
  bold, italic, and decoration.</p>

  <h3 dir="auto"><code class="notranslate">position: fixed</code> / <code class="notranslate">sticky</code></h3>

  <p dir="auto"><code class="notranslate">position: fixed</code> elements no longer
  scroll with the page — the renderer skips applying the scroll offset for <code class="notranslate">position==3</code>
  nodes, keeping them pinned to the viewport. <code class="notranslate">position:
  sticky</code> is now parsed (value 4) and treated like <code class="notranslate">relative</code>
  for layout. True scroll-tracking stickiness is deferred.</p>

  <h3 dir="auto">Dirty-only CSS cascade</h3>

  <p dir="auto"><code class="notranslate">css_cascade</code> previously ran <code
  class="notranslate">css_compute_node</code> on every element every frame when any
  node was dirty. On a 100-element page with 50 CSS rules, that''s ~5000 <code class="notranslate">selector_matches</code>
  calls per frame. Now only processes nodes where <code class="notranslate">dirty==1</code>.
  On page load all nodes are dirty (unchanged behavior); during per-frame hover/focus
  updates, typically 1-2 nodes are dirty, reducing cascade cost by ~99%.</p>

  <h3 dir="auto"><code class="notranslate">window.getComputedStyle()</code></h3>

  <p dir="auto">Returns a read-only object with 20+ computed style properties as CSS-formatted
  strings: <code class="notranslate">width</code>, <code class="notranslate">height</code>,
  <code class="notranslate">display</code> (as string), <code class="notranslate">color</code>/<code
  class="notranslate">backgroundColor</code> (as <code class="notranslate">rgba(...)</code>),
  <code class="notranslate">fontSize</code>, <code class="notranslate">position</code>,
  <code class="notranslate">opacity</code> (as 0-1 float), <code class="notranslate">visibility</code>,
  margins, padding, border, <code class="notranslate">left</code>/<code class="notranslate">top</code>,
  and <code class="notranslate">offsetLeft/Top/Width/Height</code>. Fixed: <code class="notranslate">display</code>
  was being set twice (boolean then string); <code class="notranslate">opacity</code>
  was returning 0-255 instead of 0.0-1.0.</p>

  <h3 dir="auto"><code class="notranslate">Element.matches()</code> rewritten</h3>

  <p dir="auto">Previously only handled <code class="notranslate">#id</code>, <code
  class="notranslate">.class</code>, and bare tag names. Now delegates to <code class="notranslate">css_selector_matches</code>
  — the full selector matching engine — so it handles descendant selectors, attribute
  selectors, pseudo-classes (<code class="notranslate">:hover</code>, <code class="notranslate">:checked</code>),
  <code class="notranslate">:not()</code>, adjacent siblings (<code class="notranslate">+</code>),
  and pseudo-elements.</p>

  <h3 dir="auto"><code class="notranslate">Element.closest()</code></h3>

  <p dir="auto">New method. Walks up the ancestor chain (including self) until one
  matches the given selector, returning the element or <code class="notranslate">null</code>.
  Cycle-guarded with <code class="notranslate">g_dom_node_n</code> bound. Uses the
  full <code class="notranslate">css_selector_matches</code> engine for each ancestor
  check.</p>

  <h3 dir="auto"><code class="notranslate">Array.from()</code> polyfill + <code class="notranslate">NodeList</code>
  alias</h3>

  <p dir="auto">Polyfills <code class="notranslate">Array.from</code> for array-like
  objects and iterables with optional <code class="notranslate">mapFn</code>/<code
  class="notranslate">thisArg</code>. Aliases <code class="notranslate">NodeList</code>
  to <code class="notranslate">Array</code> so <code class="notranslate">instanceof
  NodeList</code> checks pass and <code class="notranslate">NodeList.prototype.forEach</code>
  exists (Duktape arrays already have <code class="notranslate">forEach</code>). <code
  class="notranslate">JSON.parse</code>/<code class="notranslate">JSON.stringify</code>
  verified working via Duktape''s built-in <code class="notranslate">DUK_USE_JSON_BUILTIN</code>.</p>

  <h3 dir="auto">Files changed</h3>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>File</th>

  <th>Changes</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">web_render.c</code></td>

  <td>Multi-line text wrapping in <code class="notranslate">wrender_text</code>; <code
  class="notranslate">position:fixed</code> scroll-offset skip</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_layout.c</code></td>

  <td><code class="notranslate">position:fixed</code> uses viewport (0,0); <code class="notranslate">position:sticky</code>
  (value 4) treated like relative</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_css.c</code></td>

  <td>Dirty-only cascade in <code class="notranslate">css_cascade</code>; <code class="notranslate">css_selector_matches</code>
  public wrapper; <code class="notranslate">position:sticky</code> parser</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_css.h</code></td>

  <td><code class="notranslate">css_selector_matches</code> declaration; <code class="notranslate">CSS_SEL_LEN</code>
  64→128</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_dom.h</code></td>

  <td><code class="notranslate">position</code> comment updated for sticky (value
  4)</td>

  </tr>

  <tr>

  <td><code class="notranslate">web_js.c</code></td>

  <td><code class="notranslate">getComputedStyle</code>, <code class="notranslate">closest</code>,
  rewritten <code class="notranslate">matches</code>, <code class="notranslate">Array.from</code>
  polyfill, <code class="notranslate">NodeList</code> alias, opacity format fix</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>'
updated: '2026-07-12T21:51:18Z'
version: v0.47
version_title: Compiled 3DSX (Version 0.47)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!