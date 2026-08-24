---
author: Just-a-Spider
avatar: https://avatars.githubusercontent.com/u/120763283?v=4
categories:
- utility
color: '#1c4c53'
color_bg: '#1c4c53'
created: '2025-02-10T01:38:42Z'
description: Vide-coded app that allows to see RAM, GPU and CPU stats from a linux
  PC in a browser or a 3DS console.
download_page: https://github.com/Just-a-Spider/SysMon/releases
downloads:
  sysmon-3ds.3dsx:
    size: 4512088
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.1/sysmon-3ds.3dsx
  sysmon-3ds.cia:
    size: 4522944
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.1/sysmon-3ds.cia
github: Just-a-Spider/SysMon
icon: https://raw.githubusercontent.com/Just-a-Spider/SysMon/refs/heads/main/sysmon-3ds/icon.png
image: https://raw.githubusercontent.com/Just-a-Spider/SysMon/refs/heads/main/sysmon-3ds/banner.png
image_length: 25608
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
prerelease:
  download_page: https://github.com/Just-a-Spider/SysMon/releases/tag/v0.3.2-dev.2
  downloads:
    SHA256SUMS.txt:
      size: 559
      size_str: 559 Bytes
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2-dev.2/SHA256SUMS.txt
    sysmon-3ds.3dsx:
      size: 4512576
      size_str: 4 MiB
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2-dev.2/sysmon-3ds.3dsx
    sysmon-3ds.cia:
      size: 4522944
      size_str: 4 MiB
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2-dev.2/sysmon-3ds.cia
    sysmon-server_0.3.2-1_amd64.deb:
      size: 3848724
      size_str: 3 MiB
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2-dev.2/sysmon-server_0.3.2-1_amd64.deb
  qr:
    sysmon-3ds.cia: https://db.universal-team.net/assets/images/qr/prerelease/sysmon-3ds-cia.png
  update_notes: '<p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link"
    href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.2-dev.1...v0.3.2-dev.2"><tt>v0.3.2-dev.1...v0.3.2-dev.2</tt></a></p>'
  update_notes_md: '**Full Changelog**: https://github.com/Just-a-Spider/SysMon/compare/v0.3.2-dev.1...v0.3.2-dev.2'
  updated: '2026-08-24T17:54:28Z'
  version: v0.3.2-dev.2
  version_title: v0.3.2-dev.2
qr:
  sysmon-3ds.cia: https://db.universal-team.net/assets/images/qr/sysmon-3ds-cia.png
screenshots:
- description: Sysmon
  url: https://db.universal-team.net/assets/images/screenshots/sysmon/sysmon.png
source: https://github.com/Just-a-Spider/SysMon
stars: 1
systems:
- 3DS
title: SysMon
unique_ids:
- '0x1337'
update_notes: '<h2 dir="auto">SysMon v0.3.1</h2>

  <h3 dir="auto">3DS Client</h3>

  <ul dir="auto">

  <li>Fixed Monocraft font loading in <code class="notranslate">.cia</code> builds
  by embedding RomFS partition in application metadata.</li>

  <li>Added text wrapping and truncation for long track titles in the Media tab.</li>

  <li>Replaced unprintable control characters in the Settings tab with standard ASCII
  indicators.</li>

  <li>Updated 3DS HOME Menu icon and banner to flat vector designs.</li>

  <li>Added Level tab for per-application audio mixer control.</li>

  <li>Added Ctrl tab for UDP virtual gamepad input to Linux host.</li>

  <li>Added DSP hardware audio feedback for tab switching and actions.</li>

  <li>Added multi-server profile manager in Settings.</li>

  </ul>

  <h3 dir="auto">Linux Server</h3>

  <ul dir="auto">

  <li>Fixed system tray icon on Linux Wayland/COSMIC sessions by setting X11 backend
  fallback for GDK.</li>

  <li>Screen streaming (CAM) moved to optional <code class="notranslate">--features
  cam</code> build; default release is a lightweight binary without streaming dependencies.</li>

  <li>Added uinput gamepad driver integration for 3DS controller input.</li>

  <li>Added dynamic hiding of streaming controls in web config dashboard on standard
  builds.</li>

  </ul>'
updated: '2026-07-22T23:02:15Z'
version: v0.3.1
version_title: v0.3.1
---
**IMPORTANT: This app requires the companion server to be running on your PC!**

SysMon is a hardware monitor and macro executor that turns your Nintendo 3DS into a secondary dashboard for your PC.

### Features
* **Live Telemetry:** View your PC's CPU/GPU temperatures, RAM usage, and Fan speeds in real-time on the top screen.
* **Process Manager:** View the heaviest processes running on your PC and tap them to instantly kill frozen applications.
* **Productivity:** Includes a built-in Pomodoro timer to help you focus.
* **Media Controls:** Native MPRIS integration to play, pause, and skip music running on your host system.
* **Custom Macros:** Map your physical 3DS buttons (A, B, X, Y) or on-screen touch buttons to execute bash scripts, terminal commands, or keyboard shortcuts directly on your PC.

**Setup Instructions:**
To use this app, you must download and run the lightweight `sysmon-server` background service on your PC (currently supports Linux).

Visit the official [GitHub Repository](https://github.com/Just-a-Spider/SysMon) to download the server and for complete configuration instructions