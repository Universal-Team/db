---
author: KirovAir
avatar: https://avatars.githubusercontent.com/u/1339200?v=4
categories:
- utility
- app
color: '#76558e'
color_bg: '#6a4c80'
created: '2019-09-18T13:32:06Z'
description: Automatically download box art/covers for TWiLightMenu++ and Pico Launcher,
  straight onto your SD card.
download_filter: \.nds$
download_page: https://github.com/KirovAir/TwilightBoxart/releases
downloads:
  TwilightBoxart-DS-DSi.nds:
    size: 2652160
    size_str: 2 MiB
    url: https://github.com/KirovAir/TwilightBoxart/releases/download/2.3.0/TwilightBoxart-DS-DSi.nds
github: KirovAir/TwilightBoxart
icon: https://raw.githubusercontent.com/KirovAir/TwilightBoxart/master/docs/unistore-icon.png
image: https://raw.githubusercontent.com/KirovAir/TwilightBoxart/master/docs/unistore-banner.png
image_length: 62176
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: minor
qr:
  TwilightBoxart-DS-DSi.nds: https://db.universal-team.net/assets/images/qr/twilightboxart-ds-dsi-nds.png
source: https://github.com/KirovAir/TwilightBoxart
stars: 193
systems:
- DS
title: TwilightBoxart
update_notes: '<h3 dir="auto">What''s new</h3>

  <ul dir="auto">

  <li><strong>Web/Desktop/DSi:</strong> Improved boxart scanning by a mile which should
  add ~6,600 games that used to come back blank. This will be a huge improvement for
  foreign titles.</li>

  <li><strong>DS(i)</strong> Way faster downloading. (I''d say around 4x in testing,
  even more on regular DS)</li>

  <li>If you downloaded the DS(i) version quickly after release please redownload
  it. The automated build broke the downloader.. this is now fixed.</li>

  </ul>

  <h3 dir="auto">How to run it</h3>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>Client</th>

  <th>How</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><strong>Browser</strong></td>

  <td>Open <a href="https://twilightboxart.com" rel="nofollow">https://twilightboxart.com</a>
  and press scan. Nothing to install.</td>

  </tr>

  <tr>

  <td><strong>Desktop</strong></td>

  <td>Download the build for your platform from the assets below and run it.</td>

  </tr>

  <tr>

  <td><strong>DS/DSi</strong></td>

  <td>Copy <code class="notranslate">TwilightBoxart-DS-DSi.nds</code> to your card.
  Launch it from TWiLightMenu++ on a DSi (DSi mode), or from a flashcart on a DS or
  DS Lite.</td>

  </tr>

  <tr>

  <td><strong>Self-hosted</strong></td>

  <td><code class="notranslate">docker compose up -d</code> with the compose file
  from the README.</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>'
updated: '2026-07-29T19:54:20Z'
version: 2.3.0
version_title: TwilightBoxart 2.3
---
TwilightBoxart fills your launcher's box art folder from the console itself. TwilightMenu++ and DSPico are currently supported.
Connect to WiFi and it scans your card and downloads the right cover at the size your launcher
needs. Anything already on the card is left alone.

It works on a DSi over WPA2, and on an original DS or DS Lite with a flashcart over open or WEP WiFi.

## Box art for 27 systems
Supports DS, DSi and GBA, plus everything else a Nintendo DS can play that is supported: Gameboy, SNES, NES, Mega Drive, PC Engine, WonderSwan, Neo Geo Pocket, the Atari consoles and more.