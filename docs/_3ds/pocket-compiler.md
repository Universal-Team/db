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
  PocketCompiler.v0-48.3dsx:
    size: 713188
    size_str: 696 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.48/PocketCompiler.v0-48.3dsx
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
update_notes: '<p dir="auto">The 3DS crash issue in the previous version was caused
  by the <strong>Duktape fatal error handler</strong> entering an infinite spin loop
  (<code class="notranslate">for(;;) svcSleepThread(...)</code>) after JS context
  creation completed. When any post-creation Duktape operation triggered a fatal error
  (OOM, etc.), the handler froze the entire 3DS, requiring a reboot.</p>

  <h3 dir="auto">Fixes Applied</h3>

  <p dir="auto"><strong>1. Fatal handler no longer spins infinitely (web_js.c)</strong></p>

  <p dir="auto">Changed the post-creation fatal handler from <code class="notranslate">for(;;)
  svcSleepThread(1000000000LL)</code> to simply <code class="notranslate">return</code>.
  While returning from a Duktape fatal handler is technically undefined, in practice
  Duktape propagates the error as a JS exception or returns a safe value. The app
  continues running instead of freezing the 3DS.</p>

  <p dir="auto"><strong>2. All unprotected <code class="notranslate">duk_eval_string</code>
  calls replaced with protected versions:</strong></p>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>File</th>

  <th>Call</th>

  <th>Fix</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">web_js.c:1346</code></td>

  <td><code class="notranslate">duk_eval_string_noresult</code> (polyfills)</td>

  <td>→ <code class="notranslate">duk_peval_string_noresult</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">web_iframe.c:184</code></td>

  <td><code class="notranslate">duk_eval_string_noresult</code> (postMessage stub)</td>

  <td>→ <code class="notranslate">duk_peval_string_noresult</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">web_canvas.c:369</code></td>

  <td><code class="notranslate">duk_eval_string</code> (canvas property setup)</td>

  <td>→ <code class="notranslate">duk_peval_string</code> + fallback to plain object
  on failure</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto"><strong>3. <code class="notranslate">&lt;style&gt;</code> block buffer
  increased (web_html_parser.c)</strong></p>

  <p dir="auto"><code class="notranslate">stbuf</code> increased from 8192 to 16384
  bytes. A 31KB HTML file can easily have &gt;8KB of CSS. Truncation at 8KB produced
  malformed CSS that could confuse the parser.</p>

  <p dir="auto"><strong>4. <code class="notranslate">&lt;script&gt;</code> block buffer
  increased (web_html_parser.c)</strong></p>

  <p dir="auto"><code class="notranslate">scbuf</code> increased from 16384 to 32768
  bytes. Large inline scripts were being truncated at 16KB, causing syntax errors
  (caught by <code class="notranslate">duk_peval_string</code> but wasteful).</p>

  <p dir="auto"><strong>5. DOM pool sizes increased (web_dom.h)</strong></p>

  <ul dir="auto">

  <li><code class="notranslate">WE_MAX_NODES</code>: 1024 → 2048 (a complex 31KB page
  can have &gt;1024 elements + text nodes)</li>

  <li><code class="notranslate">WE_MAX_ATTRS</code>: 512 → 1024 (matching the larger
  node pool)</li>

  </ul>

  <p dir="auto"><strong>6. C2D_TextBuf NULL checks (web_render.c)</strong></p>

  <p dir="auto">Added OOM guards after <code class="notranslate">C2D_TextBufNew(4096)</code>
  in both the wrapping and non-wrapping text render paths. If allocation fails, the
  function skips drawing that text instead of crashing.</p>'
updated: '2026-07-14T01:23:25Z'
version: v0.48
version_title: Compiled 3DSX (Version 0.48)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!