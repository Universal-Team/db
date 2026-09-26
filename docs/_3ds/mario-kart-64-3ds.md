---
author: estebanpdn
avatar: https://avatars.githubusercontent.com/u/72305261?v=4
categories:
- game
color: '#7e6a57'
color_bg: '#7e6a57'
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
image_length: 30238
layout: app
llm_generation: 'yes'
preinstall_message: 'This game is mainly intended for New Nintendo 3DS systems.  After
  installation, place your Mario Kart 64 ROM in: sd:/3ds/MK64/  For a faster setup,
  generate `mk64.o2r` using SpaghettiKart on a computer and place it in the same folder.'
prerelease:
  download_page: https://github.com/EstebanPdN/mario-kart-64-3ds/releases/tag/v1.6-E13
  downloads:
    mk64-3ds-v1.6-E13.3dsx:
      size: 15267768
      size_str: 14 MiB
      url: https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.6-E13/mk64-3ds-v1.6-E13.3dsx
    mk64-3ds-v1.6-E13.cia:
      size: 12104640
      size_str: 11 MiB
      url: https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.6-E13/mk64-3ds-v1.6-E13.cia
  qr:
    mk64-3ds-v1.6-E13.cia: https://db.universal-team.net/assets/images/qr/prerelease/mk64-3ds-v1-6-e13-cia.png
  update_notes: '<div class="markdown-alert markdown-alert-warning" dir="auto"><p
    class="markdown-alert-title" dir="auto"><svg data-component="Octicon" class="octicon
    octicon-alert mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path
    d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082
    15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25
    0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75
    0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>Warning</p><p dir="auto">This
    is an experimental release. Bugs, crashes, or graphical issues may still occur.</p>

    </div>

    <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.6-E13/QR-v1.6-E13-github.png"><img
    width="490" height="490" alt="QR code for the v1.6-E13 CIA" src="https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.6-E13/QR-v1.6-E13-github.png"
    style="max-width: 100%; height: auto; max-height: 490px;"></a></p>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Reduce repeated CPU rendering work on Old 3DS.</li>

    <li>Fix startup audio synchronization and bound display waits.</li>

    <li>Add GPU geometry, lighting and texture optimizations.</li>

    <li>Improve loading, memory handling and HOME/sleep recovery.</li>

    <li>Add an in-game updater with Stable and Experimental channels.</li>

    <li>Improve menu/HUD rendering, FPS display and volume controls.</li>

    </ul>

    <h2 dir="auto">Bug reports</h2>

    <p dir="auto">Press <code class="notranslate">SELECT</code> while the issue is
    visible and attach the complete diagnostic dump folder from:</p>

    <p dir="auto"><code class="notranslate">sd:/3ds/MK64/dump/</code></p>

    <p dir="auto">For startup failures, include <code class="notranslate">startup-e13.log</code>,
    <code class="notranslate">runtime.log</code> and <code class="notranslate">sd:/3ds/MK64/mk64-install.log</code>.
    For updater errors, include <code class="notranslate">sd:/3ds/MK64/update.log</code>.</p>'
  update_notes_md: '> [!WARNING]

    > This is an experimental release. Bugs, crashes, or graphical issues may still
    occur.


    <img width="490" height="490" alt="QR code for the v1.6-E13 CIA" src="https://github.com/EstebanPdN/mario-kart-64-3ds/releases/download/v1.6-E13/QR-v1.6-E13-github.png"
    />


    ## Changelog


    - Reduce repeated CPU rendering work on Old 3DS.

    - Fix startup audio synchronization and bound display waits.

    - Add GPU geometry, lighting and texture optimizations.

    - Improve loading, memory handling and HOME/sleep recovery.

    - Add an in-game updater with Stable and Experimental channels.

    - Improve menu/HUD rendering, FPS display and volume controls.


    ## Bug reports


    Press `SELECT` while the issue is visible and attach the complete diagnostic dump
    folder from:


    `sd:/3ds/MK64/dump/`


    For startup failures, include `startup-e13.log`, `runtime.log` and `sd:/3ds/MK64/mk64-install.log`.
    For updater errors, include `sd:/3ds/MK64/update.log`.

    '
  updated: '2026-09-20T03:53:08Z'
  version: v1.6-E13
  version_title: v1.6-E13
qr:
  mk64-3ds-v1.5.cia: https://db.universal-team.net/assets/images/qr/mk64-3ds-v1-5-cia.png
source: https://github.com/EstebanPdN/mario-kart-64-3ds
stars: 185
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