---
author: estebanpdn
avatar: https://avatars.githubusercontent.com/u/72305261?v=4
categories:
- game
color: '#a58c65'
color_bg: '#806c4e'
created: '2026-07-27T22:06:01Z'
description: Nintendo 3DS dual-screen port of Zelda A Link to the Past based on zelda3
download_filter: 3dsx|cia
download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases
downloads:
  zelda3-3ds-v3.0.3dsx:
    size: 5795236
    size_str: 5 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0/zelda3-3ds-v3.0.3dsx
  zelda3-3ds-v3.0.cia:
    size: 5272512
    size_str: 5 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0/zelda3-3ds-v3.0.cia
github: EstebanPdN/zelda-alttp-3ds
icon: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udicon.png
image: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udbanner.png
image_length: 34742
layout: app
llm_generation: 'yes'
preinstall_message: Place a legally obtained USA, unheadered ROM in sdmc:/3ds/Zelda
  3DS/. The preferred filename is zelda3.sfc, but the setup also accepts other .sfc
  or .smc filenames.
prerelease:
  download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/tag/v3.1-E5
  downloads:
    zelda3-3ds-v3.1-E5.3dsx:
      size: 6754792
      size_str: 6 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1-E5/zelda3-3ds-v3.1-E5.3dsx
    zelda3-3ds-v3.1-E5.cia:
      size: 5944256
      size_str: 5 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1-E5/zelda3-3ds-v3.1-E5.cia
  qr:
    zelda3-3ds-v3.1-E5.cia: https://db.universal-team.net/assets/images/qr/prerelease/zelda3-3ds-v3-1-e5-cia.png
  update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1-E5/QR-v3.1-E5-github.png"><img
    src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1-E5/QR-v3.1-E5-github.png"
    alt="QR-v3.1-E5-github.png" style="max-width: 100%;"></a></p>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Fixed touch press and release detection with residual coordinates.</li>

    <li>Added recent touch inputs to diagnostic dumps.</li>

    <li>Fixed shifted bottom-screen touch coordinates.</li>

    <li>Improved bottom-tab touch targets and reduced navigation delay.</li>

    <li>Added GitHub updates with Stable and Pre-release channels.</li>

    <li>Added verified downloads and in-game update installation.</li>

    <li>Added paginated changelogs with matching top and bottom menu styles.</li>

    <li>Combined Restart and ROM selection and simplified Settings.</li>

    <li>Fixed Update touch controls and blank bottom-screen startup.</li>

    <li>Fixed stale overworld colors after mirror and portal transitions.</li>

    </ul>

    <h2 dir="auto">Bug reports</h2>

    <p dir="auto">Press <code class="notranslate">L + R + A</code> while the issue
    is visible and attach the resulting dump from:</p>

    <p dir="auto"><code class="notranslate">sdmc:/3ds/Zelda 3DS/dumps/</code></p>'
  update_notes_md: '![QR-v3.1-E5-github.png](https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1-E5/QR-v3.1-E5-github.png)


    ## Changelog


    - Fixed touch press and release detection with residual coordinates.

    - Added recent touch inputs to diagnostic dumps.

    - Fixed shifted bottom-screen touch coordinates.

    - Improved bottom-tab touch targets and reduced navigation delay.

    - Added GitHub updates with Stable and Pre-release channels.

    - Added verified downloads and in-game update installation.

    - Added paginated changelogs with matching top and bottom menu styles.

    - Combined Restart and ROM selection and simplified Settings.

    - Fixed Update touch controls and blank bottom-screen startup.

    - Fixed stale overworld colors after mirror and portal transitions.


    ## Bug reports


    Press `L + R + A` while the issue is visible and attach the resulting dump from:


    `sdmc:/3ds/Zelda 3DS/dumps/`

    '
  updated: '2026-09-11T01:30:20Z'
  version: v3.1-E5
  version_title: v3.1-E5
qr:
  zelda3-3ds-v3.0.cia: https://db.universal-team.net/assets/images/qr/zelda3-3ds-v3-0-cia.png
source: https://github.com/EstebanPdN/zelda-alttp-3ds
stars: 649
systems:
- 3DS
title: zelda-alttp-3ds
unique_ids:
- '0x5A20D'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0/QR-v3.0-github.png"><img
  src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0/QR-v3.0-github.png"
  alt="QR-v3.0-github.png" style="max-width: 100%;"></a></p>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Added PICA200 GPU rendering for Old 3DS with automatic software fallback.</li>

  <li>Improved Old 3DS rendering, frame pacing, audio and bottom-screen performance.</li>

  <li>Fixed WIDE/FIXED map alignment, terrain corruption and screen-edge gaps.</li>

  <li>Added native 400x240 WIDE rendering and WIDE/FIXED defaults.</li>

  <li>Fixed incorrect colors, screen flickering and Original-mode borders.</li>

  <li>Reduced slowdowns during door and room transitions.</li>

  <li>Improved bottom-map refresh and touch responsiveness; added the mirror-return
  marker.</li>

  <li>Fixed delayed heart updates and gameplay stalls after taking damage.</li>

  <li>Fixed bottom-menu borders, HUD spacing and the map''s +/− buttons.</li>

  <li>Added title-screen display/turbo settings and improved Triforce rendering.</li>

  <li>Fixed per-ROM settings persistence and configuration migration.</li>

  <li>Fixed valid ROMs being rejected and cleaned up ROM-switch handling.</li>

  <li>Fixed Old 3DS X taps while preserving hold-to-turbo controls.</li>

  <li>Improved HOME Menu responsiveness and startup/shutdown handling.</li>

  <li>Added Load State, an optional FPS counter and <code class="notranslate">DUMP
  SAVED</code> feedback.</li>

  <li>Improved numbered diagnostic dumps, screen captures and graphics/audio reports.</li>

  <li>Fixed dump freezes and audio playback during captures.</li>

  <li>Updated the custom 3D HOME Menu logo and banner orientation.</li>

  </ul>

  <p dir="auto">Thanks to <a href="https://github.com/999sian">@999sian</a> for her
  Old 3DS optimization work.</p>

  <h2 dir="auto">Bug reports</h2>

  <p dir="auto">Press <code class="notranslate">L + R + A</code> while the issue is
  visible and attach the resulting dump from:</p>

  <p dir="auto"><code class="notranslate">sdmc:/3ds/Zelda 3DS/dumps/</code></p>'
updated: '2026-09-10T22:14:06Z'
version: v3.0
version_title: v3.0
---
A native Nintendo 3DS dual-screen port of **The Legend of Zelda: A Link to the Past**, based on the open-source Zelda3 engine.

The top screen displays the main game, while the bottom screen provides a live map, dungeon information, equipment, items, and settings.

## Features

- Native Nintendo 3DS port
- Dual-screen interface
- Original, Stretch, and Wide display modes
- Fixed and Standard camera options for Wide Mode
- Support for New Nintendo 3DS and Old Nintendo 3DS systems
- 60 FPS gameplay on New Nintendo 3DS
- Multiple ROM profiles with separate saves and settings
- Support for certain translated ROMs
- CIA and Homebrew Launcher versions
- Diagnostic dumps for easier bug reporting

## Requirements

This download does **not** include the original game ROM or copyrighted game assets.

Users must provide their own legally obtained, unheadered **USA version 1.0 ROM** and place it inside:

`sdmc:/3ds/Zelda 3DS/`

On the first launch, the port validates the ROM and extracts the required assets locally on the console.