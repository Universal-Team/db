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
  zelda3-3ds-v2.9.3dsx:
    size: 5683548
    size_str: 5 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/zelda3-3ds-v2.9.3dsx
  zelda3-3ds-v2.9.cia:
    size: 5227456
    size_str: 4 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/zelda3-3ds-v2.9.cia
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
  download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/tag/v3.0-E3
  downloads:
    zelda3-3ds-v3.0-E3.3dsx:
      size: 5684612
      size_str: 5 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E3/zelda3-3ds-v3.0-E3.3dsx
    zelda3-3ds-v3.0-E3.cia:
      size: 5231552
      size_str: 4 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-E3/zelda3-3ds-v3.0-E3.cia
  qr:
    zelda3-3ds-v3.0-E3.cia: https://db.universal-team.net/assets/images/qr/prerelease/zelda3-3ds-v3-0-e3-cia.png
  update_notes: '

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Adds bottom screen settings by tapping the Triforce in the main menu</li>

    <li>Improves the bottom-screen HUD layout so hearts, magic, and equipped item
    spacing stay clean.</li>

    <li>Saves screen settings</li>

    </ul>

    <p dir="auto">If you run into any issues, press L + R + A, save a dump to your
    Zelda 3DS folder, and send it to me. That way, I can help you more easily.</p>'
  update_notes_md: '<img width="500" height="500" alt="qr" src="https://github.com/user-attachments/assets/16559ce0-c7e3-46b6-b6b8-d21ffead42ed"
    />


    ## Changelog


    - Adds bottom screen settings by tapping the Triforce in the main menu

    - Improves the bottom-screen HUD layout so hearts, magic, and equipped item spacing
    stay clean.

    - Saves screen settings


    If you run into any issues, press L + R + A, save a dump to your Zelda 3DS folder,
    and send it to me. That way, I can help you more easily.'
  updated: '2026-08-11T18:39:29Z'
  version: v3.0-E3
  version_title: v3.0-E3
qr:
  zelda3-3ds-v2.9.cia: https://db.universal-team.net/assets/images/qr/zelda3-3ds-v2-9-cia.png
source: https://github.com/EstebanPdN/zelda-alttp-3ds
stars: 525
systems:
- 3DS
title: zelda-alttp-3ds
unique_ids:
- '0x5A20D'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/QR-v2.9-github.png"><img
  src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v2.9/QR-v2.9-github.png"
  alt="QR-v2.9-github.png" style="max-width: 100%;"></a></p>

  <ul dir="auto">

  <li>Fixed the map problem when using WIDE mode with FIXED camera.</li>

  <li>Changed the 3D HOME Menu banner to the custom logo model, with logo help from
  <a href="https://github.com/Phibonacci">Phibonacci</a>, based on the original 3D
  model by <a href="https://sketchfab.com/TiraArt" rel="nofollow">TiraArt</a>.</li>

  <li>Fixed Old 3DS bottom-screen responsiveness and more optimizations.</li>

  </ul>'
updated: '2026-08-04T00:21:10Z'
version: v2.9
version_title: v2.9
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