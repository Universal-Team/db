---
author: selloa
avatar: https://avatars.githubusercontent.com/u/65969186?v=4
categories:
- utility
color: '#c2c2c2'
color_bg: '#808080'
created: '2025-09-07T15:52:26Z'
description: Pick a random game from your SD card or NAND and launch it. SMDH title
  names, filters, and persistent options.
download_filter: \.3dsx|\.cia
download_page: https://github.com/selloa/3DS-Random-Game-Launcher/releases
downloads:
  3DS-Random-Game-Launcher-v0.2.1.3dsx:
    size: 626128
    size_str: 611 KiB
    url: https://github.com/selloa/3DS-Random-Game-Launcher/releases/download/v0.2.1/3DS-Random-Game-Launcher-v0.2.1.3dsx
  3DS-Random-Game-Launcher-v0.2.1.cia:
    size: 671680
    size_str: 655 KiB
    url: https://github.com/selloa/3DS-Random-Game-Launcher/releases/download/v0.2.1/3DS-Random-Game-Launcher-v0.2.1.cia
github: selloa/3DS-Random-Game-Launcher
icon: https://raw.githubusercontent.com/selloa/3DS-Random-Game-Launcher/main/icon.png
image: https://raw.githubusercontent.com/selloa/3DS-Random-Game-Launcher/main/meta/banner.png
image_length: 6156
layout: app
license: mit
license_name: MIT License
qr:
  3DS-Random-Game-Launcher-v0.2.1.cia: https://db.universal-team.net/assets/images/qr/3ds-random-game-launcher-v0-2-1-cia.png
source: https://github.com/selloa/3DS-Random-Game-Launcher
stars: 2
systems:
- 3DS
title: 3DS Random Game Launcher
unique_ids:
- '0x5247C'
update_notes: '<h2 dir="auto">3DS Random Game Launcher v0.2.1</h2>

  <p dir="auto">UI polish and build tooling update over v0.2.0.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>Redesigned info screens</strong> Details and Technical tabs use aligned
  label/value columns, section spacing, and wrapped long text with proper indentation</li>

  <li><strong>Technical filter summary</strong> two-column ON/OFF grid for active
  filters and sources at the bottom of the Technical page</li>

  <li><strong>Cleaner chrome</strong> inverted header/footer bar, L/R page tabs (Game
  / Details / Technical), and simplified Options header</li>

  <li><strong>Banner generator</strong> config-driven <code class="notranslate">meta/banner-src/</code>
  pipeline plus <code class="notranslate">build.ps1</code> / <code class="notranslate">build.bat
  banners</code> for store and CIA artwork</li>

  <li><strong>Docs and release workflow</strong> updated VERSIONING, tools, and meta
  README for v0.2.1 builds</li>

  </ul>

  <h3 dir="auto">Controls</h3>

  <ul dir="auto">

  <li><strong>A</strong> Launch selected title</li>

  <li><strong>Y</strong> Reroll</li>

  <li><strong>L/R</strong> Switch Game / Details / Technical pages</li>

  <li><strong>SELECT</strong> Options / filters</li>

  <li><strong>X</strong> Toggle homebrew-only mode (Game page)</li>

  <li><strong>START</strong> Exit</li>

  </ul>

  <h3 dir="auto">Install</h3>

  <ul dir="auto">

  <li><strong>3DSX:</strong> copy to <code class="notranslate">3ds/</code> on SD card,
  launch from Homebrew Launcher</li>

  <li><strong>CIA:</strong> install with FBI or Universal Updater for a Home Menu
  icon</li>

  </ul>

  <p dir="auto">Universal Updater users on Universal-DB should see this update after
  the store refreshes.</p>'
updated: '2026-05-23T21:50:38Z'
version: v0.2.1
version_title: v0.2.1
website: https://github.com/selloa/3DS-Random-Game-Launcher
---
Can't decide what to play? Let your 3DS pick for you.

Scans installed titles on SD card and/or NAND, shows a readable name, and launches a random pick from your library. Great for rediscovering games you forgot you had.

**Features (v0.2.0):**
- SMDH-first display names from installed title icons
- Offline title database (8,700+ entries) as fallback
- **SELECT** options menu: category filters, SD/NAND scan, unlisted/homebrew mode, long-name preference
- Settings saved to SD card; restore defaults from the menu
- Paginated title info screens while browsing picks
- CIA (Home Menu) and 3DSX (Homebrew Launcher) installs

**Controls:**
- `A` — Launch the selected title
- `Y` — Reroll
- `X` — Toggle unlisted/homebrew mode (quick toggle)
- `SELECT` — Options / filters
- `START` — Exit

**Source code & feedback:**
- [GitHub repository](https://github.com/selloa/3DS-Random-Game-Launcher) — source, docs, and build instructions
- [Open an issue](https://github.com/selloa/3DS-Random-Game-Launcher/issues) — bug reports and feature requests
- [Pull requests welcome](https://github.com/selloa/3DS-Random-Game-Launcher/pulls) — contributions and fixes

Install or update from Universal Updater or [GitHub Releases](https://github.com/selloa/3DS-Random-Game-Launcher/releases). MIT licensed.