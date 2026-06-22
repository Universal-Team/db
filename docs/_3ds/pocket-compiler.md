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
  PocketCompiler.v0-36.3dsx:
    size: 672132
    size_str: 656 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.36/PocketCompiler.v0-36.3dsx
github: PlanetDogeCodes/Pocket-Compiler
icon: https://db.universal-team.net/assets/images/icons/pocket-compiler.png
image: https://db.universal-team.net/assets/images/images/pocket-compiler.png
image_length: 14156
layout: app
license: apache-2.0
license_name: Apache License 2.0
llm_generation: 'yes'
source: https://github.com/PlanetDogeCodes/Pocket-Compiler
stars: 4
systems:
- 3DS
title: Pocket-Compiler
update_notes: '<p dir="auto">The compiled, install-and-play .3dsx file of the first
  fully featured HTML compiler made for 3DS/n3DS consoles.<br>

  There was a v0.35, but it did not work as intended so that version has been skipped.</p>

  <p dir="auto">CIA files will be added for release 1.0</p>

  <p dir="auto"><strong>Crash / correctness fixes:</strong></p>

  <ul dir="auto">

  <li><code class="notranslate">editor_find</code> and <code class="notranslate">editor_find_prev</code>:
  <code class="notranslate">start_line</code> was not clamped before use — with a
  corrupted or uninitialized value it could make <code class="notranslate">editor_get_line</code>
  walk off the end of the buffer. Now clamped to <code class="notranslate">[0, total-1]</code>.</li>

  <li><code class="notranslate">editor_replace_at</code>: added <code class="notranslate">col
  &gt; llen</code> guard so an exact-end-of-line replacement can''t produce a negative
  memcpy count.</li>

  <li><code class="notranslate">we_eval_js</code>: added <code class="notranslate">!g_web_engine.loaded</code>
  check — without it, a stale non-NULL <code class="notranslate">js_ctx</code> pointer
  left from a previous <code class="notranslate">we_unload()</code> call could be
  dereferenced.</li>

  <li><code class="notranslate">draw_console</code>: <code class="notranslate">i &lt;
  WJS_LOG_MAX_LINES</code> guard added — a corrupted <code class="notranslate">g_wjs_log_n</code>
  could have caused a read past the log array bounds.</li>

  </ul>

  <p dir="auto"><strong>Compiler warning fixes:</strong></p>

  <ul dir="auto">

  <li><code class="notranslate">(down &amp; KEY_X) &amp;&amp; ...</code> — explicit
  parentheses added (GCC -Wall warning eliminated).</li>

  <li>Two <code class="notranslate">strcat()</code> calls replaced with <code class="notranslate">strncat()</code>.</li>

  <li><code class="notranslate">LAYOUT_ED_H</code> corrected to <code class="notranslate">178.0f</code>
  (was <code class="notranslate">180.0f</code>) — the 2px mismatch caused the cursor-to-line
  mapping to select the wrong line near the bottom of the editor panel.</li>

  </ul>

  <p dir="auto">Note: Crashing is a recurring issue. If your 3DS crashes while using
  PocketCompiler, please open an issue and describe what you were doing at the time
  of the crash.</p>'
updated: '2026-06-16T22:22:45Z'
version: v0.36
version_title: Compiled 3DSX (Release v0.36)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!