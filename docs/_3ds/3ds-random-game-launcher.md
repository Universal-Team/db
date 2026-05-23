---
author: selloa
avatar: https://avatars.githubusercontent.com/u/65969186?v=4
categories:
- utility
color: '#c2c2c2'
color_bg: '#808080'
created: '2025-09-07T15:52:26Z'
description: A Nintendo 3DS homebrew application that randomly selects, displays and
  then launches your installed games
download_page: https://github.com/selloa/3DS-Random-Game-Launcher/releases
downloads:
  3DS-Random-Game-Launcher-v0.2.0.3dsx:
    size: 624456
    size_str: 609 KiB
    url: https://github.com/selloa/3DS-Random-Game-Launcher/releases/download/v0.2.0/3DS-Random-Game-Launcher-v0.2.0.3dsx
  3DS-Random-Game-Launcher-v0.2.0.cia:
    size: 669120
    size_str: 653 KiB
    url: https://github.com/selloa/3DS-Random-Game-Launcher/releases/download/v0.2.0/3DS-Random-Game-Launcher-v0.2.0.cia
github: selloa/3DS-Random-Game-Launcher
icon: https://raw.githubusercontent.com/selloa/3DS-Random-Game-Launcher/main/icon.png
image: https://raw.githubusercontent.com/selloa/3DS-Random-Game-Launcher/main/meta/banner.png
image_length: 98675
layout: app
license: mit
license_name: MIT License
qr:
  3DS-Random-Game-Launcher-v0.2.0.cia: https://db.universal-team.net/assets/images/qr/3ds-random-game-launcher-v0-2-0-cia.png
source: https://github.com/selloa/3DS-Random-Game-Launcher
stars: 1
systems:
- 3DS
title: 3DS-Random-Game-Launcher
unique_ids:
- '0x0'
update_notes: '<h2 dir="auto">3DS Random Game Launcher v0.2.0</h2>

  <p dir="auto">Major update over v0.1.8 / v18 with better title names, filtering,
  and options.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>SMDH-first title names</strong> — reads display names from installed
  title icons when available</li>

  <li><strong>Expanded title database</strong> — merged eShop and community catalog
  data for better fallback names</li>

  <li><strong>Options menu (SELECT)</strong> — filter by category, toggle SD/NAND
  scanning, homebrew/unlisted mode, and long-name preference</li>

  <li><strong>Persistent settings</strong> — options saved to SD card; restore defaults
  from the options menu</li>

  <li><strong>Paginated title info screens</strong> — browse metadata across multiple
  pages (A/B to page, Y to reroll)</li>

  <li><strong>CIA + 3DSX builds</strong> — install from Universal Updater or Homebrew
  Launcher</li>

  </ul>

  <h3 dir="auto">Controls</h3>

  <ul dir="auto">

  <li><strong>A</strong> — Launch selected title</li>

  <li><strong>Y</strong> — Reroll</li>

  <li><strong>SELECT</strong> — Options / filters</li>

  <li><strong>START</strong> — Exit</li>

  </ul>

  <h3 dir="auto">Install</h3>

  <ul dir="auto">

  <li><strong>3DSX:</strong> / <strong>CIA:</strong> install with FBI or Universal
  Updater (homescreen icon)</li>

  </ul>

  <p dir="auto">Universal Updater users on Universal-DB should see this update automatically
  after the store refreshes.</p>'
updated: '2026-05-23T14:46:33Z'
version: v0.2.0
version_title: v0.2.0
---
Can't decide what to play? Let your 3DS pick for you! This utility scans your SD card, filters out system junk, and launches a random game from your library. Perfect for indecisive gamers who want to discover forgotten titles.

**Features:**
- Scans all installed games on your SD card
- Filters out system applications and junk
- Random game selection with reroll option
- Homebrew mode toggle (X button)
- Simple controls: A to launch, Y to reroll, START to exit
- Database of 4,135+ 3DS game titles with proper names

**Controls:**
- `A` - Launch the selected title
- `Y` - Reroll for something else  
- `X` - Toggle homebrew mode
- `START` - Exit

Built with libctru and includes a comprehensive title database sourced from 3dsdb community data.