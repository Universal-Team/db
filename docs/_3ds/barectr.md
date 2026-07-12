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
  barectr.3dsx:
    size: 211572
    size_str: 206 KiB
    url: https://github.com/DotNetttt/BareCTR/releases/download/Release/barectr.3dsx
github: DotNetttt/BareCTR
icon: https://raw.githubusercontent.com/DotNetttt/BareCTR/refs/heads/main/data/icon.png
image: https://raw.githubusercontent.com/DotNetttt/BareCTR/refs/heads/main/data/icon.png
image_length: 4875
layout: app
llm_generation: minor
source: https://github.com/DotNetttt/BareCTR
stars: 3
systems:
- 3DS
title: BareCTR
updated: '2026-06-03T09:25:45Z'
version: Release
version_title: Release v1.0
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
