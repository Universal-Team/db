---
author: net
avatar: https://avatars.githubusercontent.com/u/81213545?v=4
categories:
- app
color: '#5b7793'
color_bg: '#4f6780'
created: '2026-06-03T09:15:40Z'
description: Minimalist Minecraft server for Nintendo 3DS systems, based on Bareiron.
download_page: https://github.com/DotNetttt/BareCTR/releases
downloads:
  BareCTR.3dsx:
    size: 348340
    size_str: 340 KiB
    url: https://github.com/DotNetttt/BareCTR/releases/download/v1.1/BareCTR.3dsx
github: DotNetttt/BareCTR
icon: https://raw.githubusercontent.com/DotNetttt/BareCTR/refs/heads/main/data/icon.png
image: https://raw.githubusercontent.com/DotNetttt/BareCTR/refs/heads/main/data/icon.png
image_length: 4875
layout: app
llm_generation: minor
source: https://github.com/DotNetttt/BareCTR
stars: 8
systems:
- 3DS
title: BareCTR
update_notes: '<h1 dir="auto">BareCTR - Release v1.1</h1>

  <h3 dir="auto">🧩 Performance &amp; Network</h3>

  <ul dir="auto">

  <li><strong>Progressive Streaming:</strong> Asynchronous chunk delivery to eliminate
  stuttering upon joining.</li>

  <li><strong>Network Compression:</strong> Compressed data transfers for smoother
  communication.</li>

  <li><strong>Hardware Profiles:</strong> Dynamic render distance adjustment (2 chunks
  on Old 3DS / 4 chunks on New 3DS).</li>

  <li><strong>Optimized Server Loop:</strong> Reworked loop handling to prevent unnecessary
  TPS drops.</li>

  </ul>

  <hr>

  <h3 dir="auto">🔴 Redstone &amp; Mechanics</h3>

  <ul dir="auto">

  <li><strong>Redstone Signal:</strong> Full signal propagation (0 to 15), timed repeaters,
  torches, and buttons.</li>

  <li><strong>Pistons &amp; Sticky Pistons:</strong> Working push/pull mechanics (with
  the standard 12-block safety limit).</li>

  <li><strong>Interactions:</strong> Fixed lever states, door synchronization, and
  ladder climbing mechanics.</li>

  </ul>

  <hr>

  <h3 dir="auto">🛠️ More Features</h3>

  <ul dir="auto">

  <li><strong>Game Modes:</strong> Almost full support for <strong>Creative</strong>
  mode (with inventory management) and <strong>Spectator</strong> mode.</li>

  <li><strong>Map &amp; Version Support:</strong> Supports Anvil format world maps
  (Minecraft 1.2 to 1.17.1).</li>

  <li><strong>New Integrated Commands:</strong>

  <ul dir="auto">

  <li><code class="notranslate">!tps</code> — Displays the current server TPS.</li>

  <li><code class="notranslate">!gamemode &lt;mode&gt;</code> — Changes your game
  mode.</li>

  <li><code class="notranslate">!tp &lt;player|coords&gt;</code> — Fast teleportation.</li>

  <li><code class="notranslate">!fly</code> — Toggles flight mode.</li>

  </ul>

  </li>

  </ul>'
updated: '2026-10-30T21:51:15Z'
version: v1.1
version_title: Release v1.1
---
# BareCTR

Adaptation of the minimalist Minecraft server **Bareiron** for Nintendo 3DS.

BareCTR is a version adapted and optimized for the 3DS architecture, allowing you to host a lightweight Minecraft server directly on your console. This project preserves the original goal of Bareiron: prioritizing performance and resource efficiency.

## Features
* **Native 3DS Port:** Designed to run efficiently on Nintendo 3DS.
* **Minimalist:** A clean approach to maximize server stability on the console.
* **Bareiron Base:** Adaptation of the lightweight and high-performance server engine.

## Compilation
To compile this project, you must have the **devkitPro** toolchain installed (configured for 3DS development with `libctru`).

1. Open a terminal in the project's root folder:
   ```bash
   cd BareCTR
   make
   ```
