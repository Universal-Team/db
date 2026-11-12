---
author: estebanpdn
avatar: https://avatars.githubusercontent.com/u/72305261?v=4
categories:
- game
created: '2026-07-27T22:06:01Z'
description: Nintendo 3DS dual-screen port of Zelda A Link to the Past based on zelda3
download_filter: 3dsx|cia
download_page: https://github.com/EstebanPdN/zelda-alttp-3ds/releases
downloads:
  zelda3-3ds-v4.1.3dsx:
    size: 8836848
    size_str: 8 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v4.1/zelda3-3ds-v4.1.3dsx
  zelda3-3ds-v4.1.cia:
    size: 7545792
    size_str: 7 MiB
    url: https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v4.1/zelda3-3ds-v4.1.cia
github: EstebanPdN/zelda-alttp-3ds
icon: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udicon.png
image: https://raw.githubusercontent.com/EstebanPdN/zelda-alttp-3ds/main/udbanner.png
layout: app
llm_generation: 'yes'
preinstall_message: Place a legally obtained USA, unheadered ROM in sdmc:/3ds/Zelda
  3DS/. The preferred filename is zelda3.sfc, but the setup also accepts other .sfc
  or .smc filenames.
qr:
  zelda3-3ds-v4.1.cia: https://db.universal-team.net/assets/images/qr/zelda3-3ds-v4-1-cia.png
source: https://github.com/EstebanPdN/zelda-alttp-3ds
stars: 791
systems:
- 3DS
title: zelda-alttp-3ds
unique_ids:
- '0x5A20D'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v4.1/QR-v4.1-github.png"><img
  width="500" height="500" alt="QR code for the v4.1 CIA" src="https://github.com/EstebanPdN/zelda-alttp-3ds/releases/download/v4.1/QR-v4.1-github.png"
  style="max-width: 100%; height: auto; max-height: 500px;"></a></p>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Added Japanese text, menus, and assets support.</li>

  <li>Added direct <code class="notranslate">.zspr</code> skins and support for up
  to 512 skins mods.</li>

  <li>Fixed translations, missing characters and clipped text in Spanish, Portuguese,
  Italian and Russian.</li>

  <li>Fixed German name entry, file screens and floor labels, and the Russian Game
  Over title.</li>

  <li>Fixed German/French save-menu freezes and item-ring hangs on empty slots.</li>

  <li>Fixed WIDE expanded inventory and HUD/save-box text after loading across languages.</li>

  <li>The QoL fairies feature now restore 10 hearts.</li>

  <li>Extended WIDE to Zora''s River and fixed the dam''s flooding window.</li>

  <li>Fixed outdoor parallax, mirror-wave camera/ending and lingering flute-boy ambience.</li>

  <li>Fixed world-map margins/corners and stale WIDE scenery after the title story.</li>

  <li>Corrected dungeon-item locations used by new randomizer seeds.</li>

  <li>And more fixes that I probably did and forgot about...</li>

  </ul>

  <h2 dir="auto">Credits</h2>

  <p dir="auto">Skins by Charmander106/SePH, iBazly, Damon, InTheBeef, Ben G and Myriachan.
  <a href="https://github.com/EstebanPdN/zelda-alttp-3ds/blob/v4.1/CREDITS.md">Full
  credits</a>.</p>

  <h2 dir="auto">Bug reports</h2>

  <p dir="auto">Press <code class="notranslate">L + R + A</code> while the issue is
  visible and attach the complete diagnostic dump folder from:</p>

  <p dir="auto"><code class="notranslate">sdmc:/3ds/Zelda 3DS/dumps/</code></p>'
updated: '2026-11-11T05:20:13Z'
version: v4.1
version_title: v4.1
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