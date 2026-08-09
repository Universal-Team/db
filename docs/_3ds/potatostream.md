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
    size: 7625640
    size_str: 7 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.2.0/streampotato.3dsx
  streampotato.cia:
    size: 4374464
    size_str: 4 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.2.0/streampotato.cia
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
stars: 12
systems:
- 3DS
title: PotatoStream
unique_ids:
- '0x3700'
update_notes: '<h2 dir="auto">What''s New in v1.2.0</h2>

  <p dir="auto"><strong>Pairing &amp; Connectivity</strong></p>

  <ul dir="auto">

  <li>Fixed port 47984 being blocked during Sunshine pairing</li>

  <li>Fixed certificate validity by backdating the <code class="notranslate">notBefore</code>
  field (antidating), avoiding clock mismatch issues</li>

  <li>Fixed pairing keys being lost after update/migration</li>

  <li>Added local pairing memory to avoid unnecessary re-pairing</li>

  <li>Added detailed error messages when pairing fails</li>

  <li>Added <code class="notranslate">gs_cert_was_regenerated()</code> to properly
  detect and handle certificate regeneration</li>

  <li>Added a pairing cache purge to prevent stale pairing data from causing issues</li>

  <li>Improved Sunshine pairing and HTTP connection stability even further</li>

  </ul>

  <p dir="auto"><strong>Stability</strong></p>

  <ul dir="auto">

  <li>Fixed crashes when changing stream settings (resolution, bitrate, FPS, etc.)</li>

  <li>Fixed settings crashes in the Digital D-pad editor</li>

  <li>Fixed a thread-safety issue that could cause random crashes on startup</li>

  <li>Added proper cleanup routines on app exit</li>

  </ul>

  <p dir="auto"><strong>Video</strong></p>

  <ul dir="auto">

  <li>Fixed the H.264 decoder init loop not stopping after a successful open, and
  always disable the loop filter for better performance</li>

  </ul>

  <p dir="auto"><strong>Interface</strong></p>

  <ul dir="auto">

  <li>Reworked the user interface for a smoother experience</li>

  <li>Added a Digital D-pad editor</li>

  <li>Added a number editor</li>

  <li>Added an Exit option while editing inputs</li>

  </ul>

  <p dir="auto"><strong>Security</strong></p>

  <ul dir="auto">

  <li>Secured all <code class="notranslate">C2D_TextParse</code> calls to prevent
  crashes/vulnerabilities</li>

  <li>Various other security improvements</li>

  </ul>

  <p dir="auto"><strong>New Features</strong></p>

  <ul dir="auto">

  <li>Added an update checker: the app now asks GitHub for the latest release and
  lets you know when an update is available</li>

  </ul>'
updated: '2026-08-04T05:59:20Z'
version: v1.2.0
version_title: PotatoStream v1.2.0
---
PotatoStream is a Moonlight game streaming client for all 3DS and 2DS models, with a focus on Old 3DS/2DS compatibility. Auto-detects hardware at startup and activates "Potato" mode on older models with smart frame skipping, Y2RU hardware pipeline and an optimized stream profile (400x240@24fps). (New 3DS keeps the standard MVD hardware decoder) Compatible with Sunshine and NVIDIA GameStream.