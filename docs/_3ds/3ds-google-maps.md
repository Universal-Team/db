---
author: Oldhimaster1
avatar: https://avatars.githubusercontent.com/u/179153474?v=4
categories:
- utility
color: '#5a635b'
color_bg: '#5a635b'
created: '2026-04-03T20:43:47Z'
description: Interactive OpenStreetMap and satellite map viewer with GPS tracking,
  offline tile caching, place search, and route planning.
download_filter: \.3dsx$
download_page: https://github.com/Oldhimaster1/3ds-Google-Maps/releases
downloads:
  3ds_google_maps.3dsx:
    size: 1228008
    size_str: 1 MiB
    url: https://github.com/Oldhimaster1/3ds-Google-Maps/releases/download/v2.0/3ds_google_maps.3dsx
github: Oldhimaster1/3ds-Google-Maps
icon: https://raw.githubusercontent.com/Oldhimaster1/3ds-Google-Maps/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/Oldhimaster1/3ds-Google-Maps/refs/heads/main/banner.png
image_length: 42667
layout: app
license: mit
license_name: MIT License
llm_generation: unknown
source: https://github.com/Oldhimaster1/3ds-Google-Maps
stars: 4
systems:
- 3DS
title: 3ds Google Maps
update_notes: '<h2 dir="auto">What''s New in v2.0</h2>

  <h3 dir="auto">Offline Tile Caching</h3>

  <ul dir="auto">

  <li><strong>Tilepack format</strong> — download thousands of tiles on your PC and
  pack them into a single <code class="notranslate">.tilepack</code> file for your
  SD card</li>

  <li><strong>PC download tool</strong> (<code class="notranslate">tools/download_region.py</code>)
  — bulk tile downloader with 8 parallel workers and SHA-256 deduplication</li>

  <li><strong>In-app Download Region</strong> — download tiles for your current map
  view directly on the 3DS (Settings &gt; Data tab)</li>

  <li><strong>Auto-loading</strong> — the app checks for <code class="notranslate">sat.tilepack</code>
  and <code class="notranslate">street.tilepack</code> on startup</li>

  </ul>

  <h3 dir="auto">New Tile Source</h3>

  <ul dir="auto">

  <li><strong>Esri World Street Map</strong> — switchable alongside OSM and Esri satellite
  in the Tiles settings tab</li>

  </ul>

  <h3 dir="auto">Other</h3>

  <ul dir="auto">

  <li>Comprehensive README rewrite with offline caching docs</li>

  <li>Updated .gitignore</li>

  </ul>

  <h3 dir="auto">Installation</h3>

  <ol dir="auto">

  <li>Copy <code class="notranslate">3ds_google_maps.3dsx</code> to <code class="notranslate">sdmc:/3ds/3ds_google_maps/</code>
  on your SD card</li>

  <li>(Optional) Generate tilepacks with <code class="notranslate">python tools/download_region.py</code>
  and copy them to <code class="notranslate">sdmc:/3ds_google_maps/tiles/</code></li>

  <li>Launch via Homebrew Launcher</li>

  </ol>'
updated: '2026-04-15T20:53:30Z'
version: v2.0
version_title: v2.0 — Offline Tile Caching
---
Interactive map viewer for Nintendo 3DS. Browse OpenStreetMap street tiles and Esri satellite imagery, track your GPS location through your phone, search for places, plan routes, and save favorites.

**Features:**
- Pan and zoom maps on both screens (touch, D-pad, Circle Pad, L/R)
- Three tile sources: OpenStreetMap, Esri Satellite, Esri Street Map
- Offline tile caching — download regions on your PC and transfer as a single .tilepack file
- GPS tracking via phone browser (3DS runs an HTTPS server, phone sends coordinates)
- Place search, route planning, reverse geocoding, favorites
- Night mode, tile prefetching, SD card tile cache

**Offline caching (new in v2.0):**
Use the included Python tool to bulk-download tiles for any region. Transfers as one file instead of thousands of PNGs. Works completely without WiFi.

**GPS phone bridge:**
The 3DS starts a TLS server and shows a QR code. Scan it with your phone, allow location access, and your position streams to the 3DS in real time. On iPhone, use Chrome instead of Safari.

Requires WiFi for live tile downloads and GPS. Offline tilepacks work without any network.