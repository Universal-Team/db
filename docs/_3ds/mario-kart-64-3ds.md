---
author: estebanpdn
avatar: https://avatars.githubusercontent.com/u/72305261?v=4
categories:
- game
created: '2026-08-04T19:39:14Z'
description: Native Nintendo 3DS port work based on the Mario Kart 64 decompilation.
download_filter: ^mk64-3ds-v.*\.(cia|3dsx)$
download_page: https://github.com/EstebanPdN/mario-kart-64-3ds/releases
downloads:
  mk64-3ds-v1.5.3dsx:
    size: 14266292
    size_str: 13 MiB
    url: https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.5/mk64-3ds-v1.5.3dsx
  mk64-3ds-v1.5.cia:
    size: 11420608
    size_str: 10 MiB
    url: https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.5/mk64-3ds-v1.5.cia
github: EstebanPdN/mario-kart-64-3ds
icon: https://raw.githubusercontent.com/EstebanPdN/mario-kart-64-3ds/main/icon.jpeg
image: https://raw.githubusercontent.com/EstebanPdN/mario-kart-64-3ds/main/banner.png
layout: app
llm_generation: 'yes'
preinstall_message: 'This game is mainly intended for New Nintendo 3DS systems.  After
  installation, place your Mario Kart 64 ROM in: sd:/3ds/MK64/  For a faster setup,
  generate `mk64.o2r` using SpaghettiKart on a computer and place it in the same folder.'
qr:
  mk64-3ds-v1.5.cia: https://db.universal-team.net/assets/images/qr/mk64-3ds-v1-5-cia.png
source: https://github.com/EstebanPdN/mario-kart-64-3ds
stars: 214
systems:
- 3DS
title: mario-kart-64-3ds
unique_ids:
- '0x5A270'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.5/QR-v1.5-github.png"><img
  width="500" height="500" alt="QR code for the v1.5 CIA" src="https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.5/QR-v1.5-github.png"
  style="max-width: 100%; height: auto; max-height: 500px;"></a></p>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Fixed startup, shutdown, and gameplay crashes.</li>

  <li>Fixed the graphics command-buffer crash on race results.</li>

  <li>Improved Old and New 3DS performance and memory use.</li>

  <li>Fixed frame interpolation and frame pacing.</li>

  <li>Preloaded game resources into RAM to remove in-race resource reads from SD.</li>

  <li>Improved rendering, textures, colors, and audio processing.</li>

  <li>Faster on-device game-data extraction.</li>

  <li>Always show ROM extraction progress independently of game loading screens.</li>

  <li>Added adjustable render scale, render distance, and display filters.</li>

  <li>Added five HUD layouts and improved race HUD presentation.</li>

  <li>Redesigned Data and Course Data across both screens.</li>

  <li>Centered Grand Prix and Time Trial results with text shadows.</li>

  <li>Fixed record display and ghost save/load persistence.</li>

  <li>Added Race Ghost and Erase Ghost actions in Course Data.</li>

  <li>Expanded diagnostic dumps with numbering, RAM capture, and Clean dumps.</li>

  <li>Updated the HOME Menu banner and sound.</li>

  </ul>

  <h2 dir="auto">Bug reports</h2>

  <p dir="auto">Press <code class="notranslate">SELECT</code> while the issue is visible
  and attach the complete diagnostic dump folder from:</p>

  <p dir="auto"><code class="notranslate">sd:/3ds/MK64/dump/</code></p>'
updated: '2026-09-07T23:52:19Z'
version: v1.5
version_title: v1.5
---
Native Nintendo 3DS port of Mario Kart 64, based on SpaghettiKart