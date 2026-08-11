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
  download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/tag/v3.0-experimental
  downloads:
    zelda3-3ds-v3.0-experimental.3dsx:
      size: 2596420
      size_str: 2 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-experimental/zelda3-3ds-v3.0-experimental.3dsx
    zelda3-3ds-v3.0-experimental.cia:
      size: 1975232
      size_str: 1 MiB
      url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-experimental/zelda3-3ds-v3.0-experimental.cia
  qr:
    zelda3-3ds-v3.0-experimental.cia: https://db.universal-team.net/assets/images/qr/prerelease/zelda3-3ds-v3-0-experimental-cia.png
  update_notes: '<h2 dir="auto">Zelda 3DS v3.0 Experimental</h2>

    <p dir="auto">This is an experimental bug-fix build for the currently reported
    3DS issues.</p>

    <h3 dir="auto">QR</h3>

    <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-experimental/QR-v3.0-experimental-github.png"><img
    src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-experimental/QR-v3.0-experimental-github.png"
    alt="QR-v3.0-experimental-github.png" style="max-width: 100%;"></a></p>

    <h3 dir="auto">Fixes</h3>

    <ul dir="auto">

    <li>Bottom Triforce/cinema/end screen can now open Settings with any tap. Use
    Back to return to the black Triforce screen.</li>

    <li>Autosave/save-state loads now recover if the top-screen map/menu module was
    saved open, so restarting should no longer trap the game on the map.</li>

    <li>Screen settings now persist <code class="notranslate">DisplayMode = Wide</code>
    correctly, while keeping <code class="notranslate">WideMode = Standard</code>
    or <code class="notranslate">Fixed</code> separate.</li>

    <li>Bottom HUD layout is more compact: rupees use three digits in the resource
    chip, hearts scale/wrap by capacity, the 1/2 magic marker is tighter, and the
    equipped item ring shrinks when space is limited.</li>

    <li>Old 3DS uses a lighter bottom-screen renderer and narrower wide rendering
    to reduce memory and presentation pressure.</li>

    </ul>

    <h3 dir="auto">Testing Request</h3>

    <p dir="auto">If you still see the issue, please send a dump from this build.
    Hold L + R + A, then send the dump folder that appears under the Zelda 3DS folder.</p>'
  update_notes_md: '## Zelda 3DS v3.0 Experimental


    This is an experimental bug-fix build for the currently reported 3DS issues.


    ### QR


    ![QR-v3.0-experimental-github.png](https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v3.0-experimental/QR-v3.0-experimental-github.png)


    ### Fixes


    - Bottom Triforce/cinema/end screen can now open Settings with any tap. Use Back
    to return to the black Triforce screen.

    - Autosave/save-state loads now recover if the top-screen map/menu module was
    saved open, so restarting should no longer trap the game on the map.

    - Screen settings now persist `DisplayMode = Wide` correctly, while keeping `WideMode
    = Standard` or `Fixed` separate.

    - Bottom HUD layout is more compact: rupees use three digits in the resource chip,
    hearts scale/wrap by capacity, the 1/2 magic marker is tighter, and the equipped
    item ring shrinks when space is limited.

    - Old 3DS uses a lighter bottom-screen renderer and narrower wide rendering to
    reduce memory and presentation pressure.


    ### Testing Request


    If you still see the issue, please send a dump from this build. Hold L + R + A,
    then send the dump folder that appears under the Zelda 3DS folder.

    '
  updated: '2026-08-10T20:24:37Z'
  version: v3.0-experimental
  version_title: v3.0
qr:
  zelda3-3ds-v2.9.cia: https://db.universal-team.net/assets/images/qr/zelda3-3ds-v2-9-cia.png
source: https://github.com/EstebanPdN/zelda-alttp-3ds
stars: 378
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