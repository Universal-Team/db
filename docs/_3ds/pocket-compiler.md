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
  PocketCompiler.v0-41.3dsx:
    size: 698000
    size_str: 681 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.41/PocketCompiler.v0-41.3dsx
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
update_notes: '<p dir="auto">This release fixes many bugs and continues to add full
  CSS, HTML, and JS formatting functionality. Versions 0.39 and 0.40 were skipped
  due to beta build issues.</p>

  <h2 dir="auto">New Stuff</h2>

  <h3 dir="auto">1. <code class="notranslate">&lt;input&gt;</code>/<code class="notranslate">&lt;textarea&gt;</code>
  text entry</h3>

  <ul dir="auto">

  <li>New <code class="notranslate">we_input_prompt()</code> in <code class="notranslate">web_events.c</code>
  opens the 3DS software keyboard when a click lands on an <code class="notranslate">&lt;input&gt;</code>/<code
  class="notranslate">&lt;textarea&gt;</code> (or an ancestor of one). Reads the current
  <code class="notranslate">value</code> attribute, shows it as initial text, writes
  the result back, fires <code class="notranslate">input</code> + <code class="notranslate">change</code>
  events, and marks the node dirty so the renderer shows the new text.</li>

  <li>New <code class="notranslate">we_text_input()</code> helper wraps <code class="notranslate">swkbdInit</code>/<code
  class="notranslate">swkbdInputText</code> for reuse.</li>

  </ul>

  <h3 dir="auto">2. CSS <code class="notranslate">transform: translate()</code></h3>

  <ul dir="auto">

  <li><code class="notranslate">wrender_node</code> now applies <code class="notranslate">translate_x</code>/<code
  class="notranslate">translate_y</code> to the draw position, and folds the offset
  into the children''s <code class="notranslate">ox</code>/<code class="notranslate">oy</code>
  so children move with the translated parent. ~6 lines of real logic; the parser
  already stored the values since v0.39.</li>

  </ul>

  <h3 dir="auto">3. Word-wrap in the layout engine</h3>

  <ul dir="auto">

  <li>Replaced the naive <code class="notranslate">tw/avail_w + 1</code> character-count
  wrapping with proper word-boundary wrapping. Walks the text word by word, tracks
  line width, breaks when the next word would overflow. Hard-breaks words longer than
  a full line. Respects <code class="notranslate">white-space: pre</code> and <code
  class="notranslate">nowrap</code>.</li>

  </ul>

  <h3 dir="auto">4. CSS <code class="notranslate">:hover</code> / <code class="notranslate">:focus</code>
  / <code class="notranslate">:nth-child</code> pseudo-classes</h3>

  <ul dir="auto">

  <li>New <code class="notranslate">pseudo_matches()</code> function checks <code
  class="notranslate">:hover</code>, <code class="notranslate">:focus</code>, <code
  class="notranslate">:active</code>, <code class="notranslate">:checked</code>, <code
  class="notranslate">:disabled</code>, <code class="notranslate">:first-child</code>,
  <code class="notranslate">:last-child</code>, <code class="notranslate">:nth-child(n/odd/even)</code>.</li>

  <li><code class="notranslate">selector_matches()</code> rewritten to split selectors
  at <code class="notranslate">:</code> and check the pseudo-class after the base
  selector matches. Supports chained pseudos (<code class="notranslate">a:focus:hover</code>).</li>

  <li>Dynamic re-cascade: <code class="notranslate">we_events_update</code> marks
  nodes dirty on hover/focus changes; <code class="notranslate">we_update</code> now
  re-runs <code class="notranslate">css_cascade</code> (not just <code class="notranslate">layout_document</code>)
  when nodes are dirty, so <code class="notranslate">:hover</code>/<code class="notranslate">:focus</code>
  styles apply dynamically.</li>

  </ul>

  <h3 dir="auto">5. Keyboard input to web content</h3>

  <ul dir="auto">

  <li><code class="notranslate">window.prompt(message, default)</code> now opens the
  3DS software keyboard and returns the typed string (was a no-op stub returning <code
  class="notranslate">undefined</code>).</li>

  <li>Clicking an <code class="notranslate">&lt;input&gt;</code>/<code class="notranslate">&lt;textarea&gt;</code>
  opens the keyboard (Feature 1 above).</li>

  </ul>

  <h3 dir="auto">6. localStorage persistence + IndexedDB completion</h3>

  <ul dir="auto">

  <li><strong>IndexedDB C API hardened</strong>: <code class="notranslate">ws_idb_open</code>
  now checks for existing databases with the same name (no duplicates); <code class="notranslate">ws_idb_get</code>
  validates <code class="notranslate">fread</code> return (was a potential underflow);
  <code class="notranslate">ws_idb_clear</code> is no longer a no-op — it scans the
  directory with <code class="notranslate">opendir</code>/<code class="notranslate">readdir</code>
  and removes all files matching the store prefix; all functions now have proper NULL/bounds
  checks.</li>

  <li><strong>IndexedDB JS bindings</strong>: <code class="notranslate">ws_install_idb</code>
  now installs a real <code class="notranslate">indexedDB</code> object to JS with
  <code class="notranslate">open()</code>, <code class="notranslate">put()</code>,
  <code class="notranslate">get()</code>, <code class="notranslate">delete()</code>,
  <code class="notranslate">clear()</code>, <code class="notranslate">close()</code>
  methods. <code class="notranslate">put()</code> JSON-encodes values; <code class="notranslate">get()</code>
  safely JSON-parses them back (falls back to string if not valid JSON). The "IndexedDB"
  feature pill is now actually true.</li>

  </ul>'
updated: '2026-07-07T17:04:18Z'
version: v0.41
version_title: Compiled 3DSX (Version 0.41)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!