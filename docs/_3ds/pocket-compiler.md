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
  PocketCompiler.v0-45.3dsx:
    size: 709160
    size_str: 692 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.45/PocketCompiler.v0-45.3dsx
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
update_notes: '<h2 dir="auto">All New Stuff</h2>

  <h3 dir="auto">1. CSS selectors were completely failing on complex selectors</h3>

  <p dir="auto">The <code class="notranslate">selector_matches</code> function only
  handled <strong>simple selectors</strong> (tag, <code class="notranslate">.class</code>,
  <code class="notranslate">#id</code>, <code class="notranslate">tag.class</code>).
  It could not match any selector containing:</p>

  <ul dir="auto">

  <li><strong>Descendant combinators</strong> (spaces): <code class="notranslate">.tog
  input</code>, <code class="notranslate">.field input[type=text]</code>, <code class="notranslate">details:not([open])
  summary</code></li>

  <li><strong>Adjacent sibling combinators</strong> (<code class="notranslate">+</code>):
  <code class="notranslate">.tog input:checked + .tog-sw</code></li>

  <li><strong>Attribute selectors</strong> (<code class="notranslate">[type=checkbox]</code>):
  <code class="notranslate">input[type=checkbox]</code></li>

  <li><strong>Pseudo-elements</strong> (<code class="notranslate">::after</code>,
  <code class="notranslate">::before</code>): <code class="notranslate">summary::after</code>,
  <code class="notranslate">.tog-sw::after</code></li>

  </ul>

  <p dir="auto">Since nearly every selector in the EaglerLite CSS uses at least one
  of these, <strong>zero CSS rules were matching</strong> — the page rendered with
  default styles only.</p>

  <h3 dir="auto">2. DPad scroll was broken</h3>

  <p dir="auto">The v0.43 DPad scroll fix (which used <code class="notranslate">we_page_scroll_by</code>
  when the web engine was loaded) was accidentally reverted during the v0.44 bugfix
  pass, going back to the old text-mode-only scroll. DPad Up/Down did nothing when
  viewing a web page.</p>

  <h2 dir="auto">What I fixed</h2>

  <h3 dir="auto">New <code class="notranslate">simple_selector_matches</code> function</h3>

  <p dir="auto">Handles a single simple selector component, now with:</p>

  <ul dir="auto">

  <li><strong>Attribute selectors</strong>: <code class="notranslate">[attr]</code>,
  <code class="notranslate">[attr=val]</code>, <code class="notranslate">[attr="val"]</code>
  — parses the bracket, splits on <code class="notranslate">=</code>, strips quotes,
  checks the node''s attribute</li>

  <li><strong>Pseudo-elements</strong>: <code class="notranslate">::after</code>,
  <code class="notranslate">::before</code>, <code class="notranslate">::marker</code>,
  <code class="notranslate">::placeholder</code>, <code class="notranslate">::selection</code>
  — always accepted (we don''t render them, but the selector matches the base element
  so its other properties still apply)</li>

  <li><strong><code class="notranslate">*</code> with attribute selectors</strong>:
  <code class="notranslate">*[attr=val]</code> works</li>

  <li>Uses <code class="notranslate">css_classlist_has</code> (local, no strtok) instead
  of <code class="notranslate">classlist_has</code> (which lives in web_js.c)</li>

  </ul>

  <h3 dir="auto">Rewritten <code class="notranslate">selector_matches</code> function</h3>

  <p dir="auto">Now handles <strong>compound selectors</strong> with combinators:</p>

  <ul dir="auto">

  <li><strong>Descendant</strong> (space): <code class="notranslate">.tog input</code>
  — walks up ancestors checking each part right-to-left</li>

  <li><strong>Adjacent sibling</strong> (<code class="notranslate">+</code>): <code
  class="notranslate">input + .tog-sw</code> — checks the immediately preceding sibling</li>

  <li>Splits the selector at spaces and <code class="notranslate">+</code> (respecting
  <code class="notranslate">[bracket]</code> depth so <code class="notranslate">[type=checkbox]</code>
  doesn''t get split)</li>

  <li>Each part is matched via <code class="notranslate">simple_selector_matches</code></li>

  <li>Guard counter on all ancestor walks prevents infinite loops</li>

  </ul>

  <h3 dir="auto">DPad scroll restored</h3>

  <p dir="auto">DPad Up/Down/Left/Right now scrolls the web page via <code class="notranslate">we_page_scroll_by(0,
  ±30)</code> when <code class="notranslate">g_web_engine.loaded</code> is true. Falls
  back to text-mode scroll when the engine isn''t loaded. Circle Pad is always cursor-only.</p>'
updated: '2026-07-11T21:46:44Z'
version: v0.45
version_title: Compiled 3DSX (Version 0.45)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!