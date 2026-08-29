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
  SHA256SUMS.txt:
    size: 559
    size_str: 559 Bytes
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2/SHA256SUMS.txt
  sysmon-3ds.3dsx:
    size: 4512568
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2/sysmon-3ds.3dsx
  sysmon-3ds.cia:
    size: 4522944
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2/sysmon-3ds.cia
  sysmon-server-0.3.2-1_amd64.deb:
    size: 3858488
    size_str: 3 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.2/sysmon-server-0.3.2-1_amd64.deb
github: Just-a-Spider/SysMon
icon: https://raw.githubusercontent.com/Just-a-Spider/SysMon/refs/heads/main/sysmon-3ds/icon.png
image: https://raw.githubusercontent.com/Just-a-Spider/SysMon/refs/heads/main/sysmon-3ds/banner.png
image_length: 25608
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
prerelease:
  download_page: https://github.com/Just-a-Spider/SysMon/releases/tag/v0.3.3-dev.1
  downloads:
    SHA256SUMS.txt:
      size: 559
      size_str: 559 Bytes
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3-dev.1/SHA256SUMS.txt
    sysmon-3ds.3dsx:
      size: 4516468
      size_str: 4 MiB
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3-dev.1/sysmon-3ds.3dsx
    sysmon-3ds.cia:
      size: 4527040
      size_str: 4 MiB
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3-dev.1/sysmon-3ds.cia
    sysmon-server_0.3.3-1_amd64.deb:
      size: 3855592
      size_str: 3 MiB
      url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3-dev.1/sysmon-server_0.3.3-1_amd64.deb
  qr:
    sysmon-3ds.cia: https://db.universal-team.net/assets/images/qr/prerelease/sysmon-3ds-cia.png
  update_notes: '<p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link"
    href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.2-dev.2...v0.3.3-dev.1"><tt>v0.3.2-dev.2...v0.3.3-dev.1</tt></a></p>

    <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.2-dev.2...v0.3.3-dev.1"><tt>v0.3.2-dev.2...v0.3.3-dev.1</tt></a></p>'
  update_notes_md: '**Full Changelog**: https://github.com/Just-a-Spider/SysMon/compare/v0.3.2-dev.2...v0.3.3-dev.1


    **Full Changelog**: https://github.com/Just-a-Spider/SysMon/compare/v0.3.2-dev.2...v0.3.3-dev.1'
  updated: '2026-08-28T18:58:04Z'
  version: v0.3.3-dev.1
  version_title: v0.3.3-dev.1
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
update_notes: '<p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link"
  href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.1...v0.3.2"><tt>v0.3.1...v0.3.2</tt></a></p>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.1...v0.3.2"><tt>v0.3.1...v0.3.2</tt></a></p>'
updated: '2026-08-24T18:43:32Z'
version: v0.3.2
version_title: v0.3.2
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