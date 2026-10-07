---
author: PainDe0Mie
avatar: https://avatars.githubusercontent.com/u/97704518?v=4
categories:
- utility
color: '#5f6983'
color_bg: '#5c6680'
created: '2026-04-18T02:45:15Z'
description: Gamestream client for old 2ds/3DS
download_page: https://github.com/PainDe0Mie/PotatoStream/releases
downloads:
  streampotato.3dsx:
    size: 7676360
    size_str: 7 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.3.0/streampotato.3dsx
  streampotato.cia:
    size: 4409280
    size_str: 4 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.3.0/streampotato.cia
github: PainDe0Mie/PotatoStream
icon: https://raw.githubusercontent.com/PainDe0Mie/PotatoStream/n3ds-main/3ds/res/ic_streampotato.png
image: https://raw.githubusercontent.com/PainDe0Mie/PotatoStream/n3ds-main/3ds/res/banner.png
image_length: 11016
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  streampotato.cia: https://db.universal-team.net/assets/images/qr/streampotato-cia.png
source: https://github.com/PainDe0Mie/PotatoStream
stars: 17
systems:
- 3DS
title: PotatoStream
unique_ids:
- '0x3700'
update_notes: '<h2 dir="auto">What''s New in v1.3.0</h2>

  <p dir="auto"><strong>Pairing &amp; Sunshine Compatibility</strong></p>

  <ul dir="auto">

  <li>Fixed recent Sunshine certificate verification rejections (Client certificate
  identity is not enabled or HTTP 401)</li>

  <li>Added automatic detection and transparent regeneration of client certificates
  if their date was generated in the future due to 3DS RTC drift</li>

  <li>Fixed host port reset bug: connecting to an IP with a custom port no longer
  corrupts your global default settings port</li>

  <li>Fixed Unpair host to unconditionally clean up local pairing records even if
  the host is offline or denies the request</li>

  <li>Changed client identity device name from roth to "PotatoStream" in pairing exchanges
  for clearer identification in Sunshine</li>

  </ul>

  <p dir="auto"><strong>Video &amp; Rendering</strong></p>

  <ul dir="auto">

  <li>Hardened Y2RU hardware color conversion to properly handle frame stride gaps
  (<code class="notranslate">luma_gap, chroma_gap</code>) and prevent buffer corruption</li>

  <li>Added automatic recovery (<code class="notranslate">DR_NEED_IDR</code>) when
  video decoding encounters corrupted frames, eliminating stream freezes</li>

  <li>Optimized GPU cache flushes (<code class="notranslate">GSPGPU_FlushDataCache
  &amp; GX_FlushCacheRegions</code>) to target exact buffer sizes, reducing micro-stutters</li>

  <li>Fix the View-Only mode</li>

  </ul>

  <p dir="auto"><strong>Interface &amp; UX</strong></p>

  <ul dir="auto">

  <li>Completely overhauled the Citro2D user interface</li>

  <li>Added on-screen toast notifications on the bottom screen for certificate updates,
  pairing advice, and system alerts</li>

  <li>Updated application description to "StreamPotato - Old &amp; New 3DS/2DS"</li>

  </ul>

  <p dir="auto"><strong>Network &amp; System</strong></p>

  <ul dir="auto">

  <li>Integrated background host discovery and persistent host book management</li>

  <li>Improved error messages for HTTPS app-list</li>

  </ul>

  <p dir="auto"><strong>New 3DS/2DS Optimizations &amp; Fixes</strong></p>

  <ul dir="auto">

  <li>Fixed a critical inverted condition in the MVD hardware decoder</li>

  <li>Enabled 2-slice multi-threaded software decoding for N3DS, leveraging the extra
  CPU core for much higher frame rates</li>

  <li>Increased application CPU time limit on N3DS</li>

  <li>Lowered audio prebuffer latency on N3DS</li>

  </ul>'
updated: '2026-10-06T22:44:00Z'
version: v1.3.0
version_title: PotatoStream v1.3.0
---
PotatoStream is a Moonlight game streaming client for all 3DS and 2DS models, with a focus on Old 3DS/2DS compatibility. Auto-detects hardware at startup and activates "Potato" mode on older models with smart frame skipping, Y2RU hardware pipeline and an optimized stream profile (400x240@24fps). (New 3DS keeps the standard MVD hardware decoder) Compatible with Sunshine and NVIDIA GameStream.