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
    size: 2654720
    size_str: 2 MiB
    url: https://github.com/KirovAir/TwilightBoxart/releases/download/2.3.1/TwilightBoxart-DS-DSi.nds
github: KirovAir/TwilightBoxart
icon: https://raw.githubusercontent.com/KirovAir/TwilightBoxart/master/docs/unistore-icon.png
image: https://raw.githubusercontent.com/KirovAir/TwilightBoxart/master/docs/unistore-banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: minor
qr:
  TwilightBoxart-DS-DSi.nds: https://db.universal-team.net/assets/images/qr/twilightboxart-ds-dsi-nds.png
source: https://github.com/KirovAir/TwilightBoxart
stars: 200
systems:
- DS
title: TwilightBoxart
update_notes: '<h3 dir="auto">What''s new</h3>

  <ul dir="auto">

  <li><strong>Web: bring your own covers.</strong> Drop any image on a game that came
  back blank (a scan, a photo of<br>

  the box, a screenshot) and it goes onto your card like any downloaded cover.</li>

  <li><strong>Much cleaner scans.</strong> hiyaCFW and Unlaunch cards no longer drag
  their whole NAND mirror through<br>

  a scan, documentation is no longer scanned as a game, and files too small to be
  a ROM are skipped.</li>

  <li><strong>Old SNES scene dumps match now.</strong> A loose <code class="notranslate">.smc</code>
  with the 512-byte copier header gets its cover.</li>

  <li><strong>DS/DSi:</strong> new BlocksDS SDK. (And also cleaner scans)</li>

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
updated: '2026-08-10T18:47:48Z'
version: 2.3.1
version_title: TwilightBoxart 2.3.1
---
TwilightBoxart fills your launcher's box art folder from the console itself. TwilightMenu++ and DSPico are currently supported.
Connect to WiFi and it scans your card and downloads the right cover at the size your launcher
needs. Anything already on the card is left alone.

It works on a DSi over WPA2, and on an original DS or DS Lite with a flashcart over open or WEP WiFi.

## Box art for 27 systems
Supports DS, DSi and GBA, plus everything else a Nintendo DS can play that is supported: Gameboy, SNES, NES, Mega Drive, PC Engine, WonderSwan, Neo Geo Pocket, the Atari consoles and more.