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
  zelda3-3ds-v3.1.3dsx:
    size: 6754764
    size_str: 6 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1/zelda3-3ds-v3.1.3dsx
  zelda3-3ds-v3.1.cia:
    size: 5944256
    size_str: 5 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1/zelda3-3ds-v3.1.cia
github: EstebanPdN/zelda-alttp-3ds
icon: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udicon.png
image: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udbanner.png
image_length: 34742
layout: app
llm_generation: 'yes'
preinstall_message: Place a legally obtained USA, unheadered ROM in sdmc:/3ds/Zelda
  3DS/. The preferred filename is zelda3.sfc, but the setup also accepts other .sfc
  or .smc filenames.
qr:
  zelda3-3ds-v3.1.cia: https://db.universal-team.net/assets/images/qr/zelda3-3ds-v3-1-cia.png
source: https://github.com/EstebanPdN/zelda-alttp-3ds
stars: 668
systems:
- 3DS
title: zelda-alttp-3ds
unique_ids:
- '0x5A20D'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1/QR-v3.1-github.png"><img
  width="500" height="500" alt="QR code for the v3.1 CIA" src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.1/QR-v3.1-github.png"
  style="max-width: 100%; height: auto; max-height: 500px;"></a></p>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Added in-game GitHub updates with Stable/Pre-release channels.</li>

  <li>Fixed bottom-screen startup, touch accuracy and navigation delay on the Old
  3DS.</li>

  <li>Simplified Settings and combined Restart with ROM selection.</li>

  <li>Fixed stale world colors after mirror and portal transitions.</li>

  <li>Added touch history to dumps.</li>

  </ul>

  <h2 dir="auto">Bug reports</h2>

  <p dir="auto">Press <code class="notranslate">L + R + A</code> while the issue is
  visible and attach the complete diagnostic dump folder from:</p>

  <p dir="auto"><code class="notranslate">sdmc:/3ds/Zelda 3DS/dumps/</code></p>'
updated: '2026-09-11T02:56:04Z'
version: v3.1
version_title: v3.1
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