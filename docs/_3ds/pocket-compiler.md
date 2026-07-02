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
  PocketCompiler.v0-38.3dsx:
    size: 673628
    size_str: 657 KiB
    url: https://github.com/PlanetDogeCodes/Pocket-Compiler/releases/download/v0.38/PocketCompiler.v0-38.3dsx
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
update_notes: '<p dir="auto"><strong>Crash / correctness bugs:</strong><br>

  Canvas 2D silently broken — wc_install_bindings() built its property-setup script
  with snprintf into a 512-byte buffer, but the actual script is 854 bytes. It was
  truncating mid-statement, so ctx.fillStyle = ''red'' and every other canvas property
  setter did nothing, with zero error shown. Now passed as a literal directly to duk_eval_string
  — no buffer, no truncation possible.<br>

  Event listeners could misfire — DOMEvent.js_ref was a uint8_t, silently wrapping
  after the 255th addEventListener() call in a session and firing the wrong callback.
  Widened to uint16_t.<br>

  Listener ref counter never reset — it was a function-local static that persisted
  across every recompile instead of resetting with the fresh Duktape context each
  page load gets. Moved to file scope with an explicit reset tied to context creation.<br>

  Unchecked array access in we_document_open() — switched to the existing bounds-checked
  accessor so a corrupted sibling chain can''t read out-of-bounds memory.</p>

  <p dir="auto"><strong>Stack-safety hardening (3DS has only 256KB of stack):</strong><br>

  5. ~3KB of stacked buffers in the CSS parser — css_parse_inline''s 2048-byte buffer
  is called while css_parse_stylesheet''s 1024-byte buffer is still live. Both made
  static (verified safe: parsing is never re-entrant).<br>

  6. Unbounded layout recursion — nothing stopped a deeply-nested DOM tree (up to
  the 1024-node cap) from recursing that many stack frames deep. Added a depth guard
  capped well above any realistic page.</p>

  <p dir="auto">Version v0.37 was skipped due to issues with a beta build.<br>

  CIA files will be added in version 1.0</p>'
updated: '2026-07-02T17:43:11Z'
version: v0.38
version_title: Compiled 3DSX (Version v0.38)
wiki: https://github.com/PlanetDogeCodes/Pocket-Compiler/blob/main/README.md
---
An almost fully featured HTML/JS/CSS compiler application made for 3DS/n3DS consoles. Includes iframes, limited WebGL support, limited Canvas support, Audio Support, and a clean UI!