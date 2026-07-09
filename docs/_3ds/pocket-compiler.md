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
  PocketCompiler.v0-43.3dsx:
    size: 707312
    size_str: 690 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.43/PocketCompiler.v0-43.3dsx
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
update_notes: '<p dir="auto">This update does a lot of new things, but most notably
  fixes some annoying UI components that bothered me during testing (circle pad can
  scroll, but only in some menus, line compression during scrolling, etc) and also
  adds enough components so that it could (theoretically) run Cookie Clicker!</p>

  <h2 dir="auto">All the New Stuff</h2>

  <h3 dir="auto">UI: DPad = Scroll, Circle Pad = Cursor (fixed)</h3>

  <p dir="auto">The biggest UX fix: DPad and Circle Pad no longer conflict. Previously,
  DPad both scrolled the fallback text renderer AND sent arrow key events to web content
  — pressing Up would scroll the page <em>and</em> fire a <code class="notranslate">keydown("ArrowUp")</code>
  at the same time. Circle Pad could also trigger scroll in some paths.</p>

  <p dir="auto"><strong>Now:</strong></p>

  <ul dir="auto">

  <li><strong>DPad</strong> scrolls the web page (30px per press, all four directions).
  When the web engine isn''t loaded, it scrolls the fallback text output instead.</li>

  <li><strong>Circle Pad</strong> always moves the cursor — it never scrolls, in any
  mode.</li>

  <li>DPad was removed from the web content key map entirely, so no more phantom arrow
  key events.</li>

  <li>Only <strong>Y</strong> (Space) generates a keyboard event for web content.</li>

  <li>Controls help screen updated to reflect the new assignments.</li>

  </ul>

  <h3 dir="auto">Cookie Clicker Compatibility: 3 Major JS APIs Added</h3>

  <p dir="auto"><strong>1. <code class="notranslate">element.classList</code></strong>
  — Cookie Clicker (and most modern JS) uses <code class="notranslate">classList.add()</code>,
  <code class="notranslate">.remove()</code>, <code class="notranslate">.toggle()</code>,
  <code class="notranslate">.contains()</code> extensively. Previously only <code
  class="notranslate">className</code> existed. Now <code class="notranslate">classList</code>
  returns a live object with all four methods that manipulate the node''s <code class="notranslate">class</code>
  attribute and trigger <code class="notranslate">css_compute_node</code> so styles
  re-cascade.</p>

  <p dir="auto"><strong>2. Live <code class="notranslate">element.style</code> object</strong>
  — Cookie Clicker does <code class="notranslate">element.style.display = ''none''</code>,
  <code class="notranslate">element.style.left = ''100px''</code>, etc. Previously
  <code class="notranslate">style</code> was a dead object — setting properties did
  nothing. Now the style object is wrapped in a <strong>Duktape Proxy</strong> that
  intercepts every property get/set:</p>

  <ul dir="auto">

  <li><strong>Get</strong> (<code class="notranslate">element.style.display</code>):
  parses the inline <code class="notranslate">style</code> attribute and returns the
  property value.</li>

  <li><strong>Set</strong> (<code class="notranslate">element.style.display = ''none''</code>):
  updates the inline style string via a C-backed <code class="notranslate">cssText</code>
  setter, triggers <code class="notranslate">css_compute_node</code> + <code class="notranslate">dom_mark_dirty</code>
  so the layout and renderer pick up the change immediately.</li>

  </ul>

  <p dir="auto"><strong>3. <code class="notranslate">onclick</code>/<code class="notranslate">onload</code>/<code
  class="notranslate">onerror</code> property handlers</strong> — Cookie Clicker assigns
  <code class="notranslate">element.onclick = function(){...}</code> instead of using
  <code class="notranslate">addEventListener</code> or inline <code class="notranslate">onclick="..."</code>
  attributes. Previously only inline attribute handlers and <code class="notranslate">addEventListener</code>
  worked. Now <code class="notranslate">we_dispatch</code> checks for JS function
  properties on the node object (<code class="notranslate">onclick</code>, <code class="notranslate">onmousedown</code>,
  <code class="notranslate">onload</code>, <code class="notranslate">onsubmit</code>,
  etc.) and calls them with a proper event object. Supports all 13 event types.</p>'
updated: '2026-07-09T18:16:56Z'
version: v0.43
version_title: Compiled 3DSX (Version 0.43)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!