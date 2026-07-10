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
  PocketCompiler.v0-44.3dsx:
    size: 707416
    size_str: 690 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.44/PocketCompiler.v0-44.3dsx
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
update_notes: '<p dir="auto">This version is mostly just a CSS engine overhaul. Most
  styles weren''t loading correctly (thanks to <a href="https://github.com/ValEthanYT-Dev">ValEthanYT-Dev</a>
  for pointing that out), an issue that had slipped my grasp for a while but should
  be mostly fixed for now. Beware that the CSS engine is far from complete, and is
  still not fully-featured by any means, but small additions here and there are all
  I can do for now.</p>

  <h2 dir="auto">All The New Stuff</h2>

  <h3 dir="auto">CSS Custom Properties (Variables) — <code class="notranslate">var()</code>
  + <code class="notranslate">:root</code></h3>

  <p dir="auto">The biggest addition. <code class="notranslate">:root { --bg: #000;
  }</code> stores custom properties in a global variable table. <code class="notranslate">var(--bg)</code>
  is resolved at parse time before any property handler runs — works in colors, lengths,
  and any value. Supports <code class="notranslate">var(--name, fallback)</code> syntax
  and recursive resolution (variables referencing other variables). Up to 64 variables
  stored. Reset on page recompile.</p>

  <h3 dir="auto"><code class="notranslate">@media</code> Queries — Graceful Skip</h3>

  <p dir="auto"><code class="notranslate">@media(max-width: 680px) { ... }</code>
  is now parsed and skipped gracefully (with proper brace-nesting tracking). Previously,
  <code class="notranslate">@media</code> would confuse the stylesheet parser and
  corrupt all subsequent rules. Also skips <code class="notranslate">@keyframes</code>,
  <code class="notranslate">@import</code>, <code class="notranslate">@font-face</code>,
  and <code class="notranslate">@charset</code>.</p>

  <h3 dir="auto"><code class="notranslate">:root</code> Selector</h3>

  <p dir="auto"><code class="notranslate">:root { ... }</code> declarations are applied
  as a universal <code class="notranslate">*</code> rule with the lowest specificity,
  so <code class="notranslate">:root</code> properties cascade to all elements via
  inheritance. Custom properties (<code class="notranslate">--name: value</code>)
  are stored in the variable table.</p>

  <h3 dir="auto"><code class="notranslate">:not()</code> Selector</h3>

  <p dir="auto"><code class="notranslate">:not(.hidden)</code> now works. The inner
  selector is recursively matched and negated. Forward-declared to handle the mutual
  recursion between <code class="notranslate">pseudo_matches</code> → <code class="notranslate">pseudo_not_matches</code>
  → <code class="notranslate">selector_matches</code>.</p>

  <h3 dir="auto">Comma-Separated Selectors</h3>

  <p dir="auto"><code class="notranslate">h1, h2, h3 { ... }</code> now creates a
  separate rule for each sub-selector instead of creating one rule with a comma in
  the selector (which never matched anything).</p>

  <h3 dir="auto"><code class="notranslate">!important</code> Support</h3>

  <p dir="auto"><code class="notranslate">color: red !important</code> is now accepted
  — the <code class="notranslate">!important</code> suffix is stripped before parsing.
  All declarations are treated as having the same specificity (later wins), so <code
  class="notranslate">!important</code> doesn''t change cascade behavior but no longer
  causes parse failures.</p>

  <h3 dir="auto">New CSS Properties (15 additions)</h3>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>Property</th>

  <th>Description</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">box-sizing</code></td>

  <td><code class="notranslate">border-box</code> / <code class="notranslate">content-box</code>
  (parsed, stored)</td>

  </tr>

  <tr>

  <td><code class="notranslate">flex</code> shorthand</td>

  <td><code class="notranslate">flex: 1</code> → grow=1; <code class="notranslate">flex:
  1 0 auto</code> → grow/shrink/basis</td>

  </tr>

  <tr>

  <td><code class="notranslate">flex-shrink</code></td>

  <td>Default 1</td>

  </tr>

  <tr>

  <td><code class="notranslate">flex-basis</code></td>

  <td><code class="notranslate">auto</code> or length</td>

  </tr>

  <tr>

  <td><code class="notranslate">pointer-events</code></td>

  <td><code class="notranslate">none</code> / <code class="notranslate">auto</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">user-select</code></td>

  <td><code class="notranslate">none</code> / <code class="notranslate">auto</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">outline</code></td>

  <td>Width + color (simplified, no layout impact)</td>

  </tr>

  <tr>

  <td><code class="notranslate">outline-width</code> / <code class="notranslate">outline-color</code>
  / <code class="notranslate">outline-style</code></td>

  <td>Individual properties</td>

  </tr>

  <tr>

  <td><code class="notranslate">text-transform</code></td>

  <td><code class="notranslate">uppercase</code> / <code class="notranslate">lowercase</code>
  / <code class="notranslate">capitalize</code> / <code class="notranslate">none</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">letter-spacing</code></td>

  <td>px or <code class="notranslate">normal</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">line-height</code></td>

  <td>px, unitless multiplier, or <code class="notranslate">normal</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">list-style</code> / <code class="notranslate">list-style-type</code></td>

  <td><code class="notranslate">none</code> / <code class="notranslate">disc</code>
  / <code class="notranslate">circle</code> / <code class="notranslate">square</code>
  / <code class="notranslate">decimal</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">object-fit</code></td>

  <td><code class="notranslate">fill</code> / <code class="notranslate">contain</code>
  / <code class="notranslate">cover</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">min/max-width/height</code></td>

  <td>Now handles <code class="notranslate">none</code> and <code class="notranslate">auto</code>
  correctly</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>'
updated: '2026-07-10T18:50:33Z'
version: v0.44
version_title: Compiled 3DSX (Version 0.44)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!