---
author: Elliot Kempson
avatar: https://avatars.githubusercontent.com/u/55849851?v=4
categories:
- app
color: '#92cfbd'
color_bg: '#5a8074'
created: '2026-04-05T01:13:14Z'
description: A 3DS Client for any Kavita Library Manager Instance!
download_filter: ''
download_page: https://github.com/ellio86/kavita-3ds/releases
downloads:
  kavita-3ds.3dsx:
    size: 680172
    size_str: 664 KiB
    url: https://github.com/ellio86/kavita-3ds/releases/download/0.4.1/kavita-3ds.3dsx
  kavita-3ds.cia:
    size: 517056
    size_str: 504 KiB
    url: https://github.com/ellio86/kavita-3ds/releases/download/0.4.1/kavita-3ds.cia
github: ellio86/kavita-3ds
icon: https://raw.githubusercontent.com/ellio86/kavita-3ds/main/icon.png
image: https://raw.githubusercontent.com/ellio86/kavita-3ds/main/banner.png
image_length: 8092
layout: app
qr:
  kavita-3ds.cia: https://db.universal-team.net/assets/images/qr/kavita-3ds-cia.png
source: https://github.com/ellio86/kavita-3ds
stars: 2
systems:
- 3DS
title: kavita-3ds
unique_ids:
- '0xF8C31'
update_notes: '<h2 dir="auto">Kavita 3DS v0.4.1</h2>

  <p dir="auto">Now on Universal Updater!</p>

  <p dir="auto">Install via Universal Updater. Alternatively, install CIA Via FBI
  or run .3dsx through the Homebrew Launcher.</p>

  <p dir="auto">Point at your Kavita instance and provide your credentials and you
  should be able to access your library. EPUBs, CBR/CBZ and PDFs are supported currently.</p>

  <h2 dir="auto">v0.4.1 Change Log</h2>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Fixed threading issue that would cause the app to be unusable on some devices.</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/ellio86/kavita-3ds/compare/0.3.1...0.4"><tt>0.3.1...0.4</tt></a></p>'
updated: '2026-04-13T14:40:25Z'
version: 0.4.1
---
# Kavita 3DS

A Nintendo 3DS homebrew client for [Kavita](https://www.kavitareader.com/) — browse your comic, manga, and book library from your 3DS.

## Features

- Browse libraries, series, volumes, and chapters
- Cover art thumbnails with lazy loading
- Full-screen comic/manga page reader
- Reading progress sync back to Kavita
- Credentials saved to SD card

## Build Setup

### 1. Install devkitPro

Download and install [devkitPro](https://devkitpro.org/wiki/Getting_Started).

On Windows: use the devkitPro MSYS2 installer, then open a devkitPro MSYS2 shell.

### 2. Install 3DS packages

```sh
dkp-pacman -S 3ds-dev 3ds-citro2d 3ds-citro3d
```

### 3. Download vendored libraries

```sh
bash bootstrap.sh
```

This downloads `cJSON` and `stb_image` into the `libs/` directory.

### 4. Python (for icon / CIA assets)

The first `make` runs `tools/prepare_cia_assets.py`, which resizes `icon.png` to 48×48 (for the `.smdh`), builds the CIA banner from `icon-large.png`, and writes a short silent audio clip for the banner. Install Python 3 and Pillow:

```sh
pip install Pillow
```

### 5. Build

```sh
make
```

Output: `kavita-3ds.3dsx` and `kavita-3ds.smdh`

### 6. CIA package (optional)

Installing a `.cia` on the HOME Menu requires **bannertool** and **makerom**, which are not included in devkitPro’s `3dstools` package. Download release binaries and put them on your `PATH` (for example copy `bannertool.exe` and `makerom.exe` into `%DEVKITPRO%\tools\bin`), or pass explicit paths when invoking Make.

- **makerom:** [Project_CTR releases](https://github.com/3DSGuy/Project_CTR/releases) — use the Windows x86_64 zip (contains `makerom.exe`).
- **bannertool:** [Epicpkmn11/bannertool releases](https://github.com/Epicpkmn11/bannertool/releases) — extract `bannertool.zip` and use `windows-x86_64/bannertool.exe`.

From a devkitPro MSYS2 shell (same environment as `make`):

```sh
make cia
```

If the tools are not on `PATH`, use MSYS-style paths, for example:

```sh
make cia BANNERTOOL=/c/path/to/bannertool.exe MAKEROM=/c/path/to/makerom.exe
```

Output: `kavita-3ds.cia` in the project root. Ensure `make` has already been run at least once so `kavita-3ds.elf` and the CIA banner/icon assets under `build/` exist.

## Running

Copy `kavita-3ds.3dsx` to `/3ds/kavita-3ds/kavita-3ds.3dsx` on your SD card, then launch via the Homebrew Launcher.

## Controls
Displayed on touchscreen. 

In reader, press the A button to show the following controls: 
- X: Adjust Zoom Level
- Circle Pad (Whilst Zoomed): Pan Viewport
- Start: Go To page
- B: Back to Chapter List
- Left / Right D-Pad: Previous / Next Page


## Config

Server URL and credentials are saved to `/3ds/kavita-3ds/config.ini` on the SD card. Delete this file to reset.

## Project Structure

```
kavita-3ds/
├── Makefile
├── bootstrap.sh          # Downloads vendored libs
├── icon.png              # app icon
├── romfs/                # Read-only filesystem embedded in .3dsx
├── libs/                 # Vendored: cJSON.h/c, stb_image.h (after bootstrap)
├── include/              # Header files
└── source/               # C source files
    ├── main.c            # Entry point, service init, main loop
    ├── app.c             # State machine
    ├── config.c          # SD card config INI
    ├── http_client.c     # libctru httpc wrapper
    ├── kavita_api.c      # Kavita REST API calls
    ├── image_loader.c    # JPEG/PNG decode → GPU texture
    ├── ui.c              # UI primitives
    ├── screen_setup.c    # Login screen
    ├── screen_libraries.c
    ├── screen_series.c   # Cover grid with lazy loading
    ├── screen_detail.c   # Volume/chapter list
    └── screen_reader.c   # Full-screen page reader
```