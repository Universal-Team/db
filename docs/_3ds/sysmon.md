---
author: Just-a-Spider
avatar: https://avatars.githubusercontent.com/u/120763283?v=4
categories:
- utility
color: '#1c4c53'
color_bg: '#1c4c53'
created: '2025-02-10T01:38:42Z'
description: Turn your Nintendo 3DS into a secondary PC hardware monitor, macro pad,
  and virtual gamepad controller.
download_page: https://github.com/Just-a-Spider/SysMon/releases
downloads:
  SHA256SUMS.txt:
    size: 559
    size_str: 559 Bytes
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3/SHA256SUMS.txt
  sysmon-3ds.3dsx:
    size: 4516468
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3/sysmon-3ds.3dsx
  sysmon-3ds.cia:
    size: 4527040
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3/sysmon-3ds.cia
  sysmon-server-0.3.3-1_amd64.deb:
    size: 3868656
    size_str: 3 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.3/sysmon-server-0.3.3-1_amd64.deb
github: Just-a-Spider/SysMon
icon: https://raw.githubusercontent.com/Just-a-Spider/SysMon/refs/heads/main/sysmon-3ds/icon.png
image: https://raw.githubusercontent.com/Just-a-Spider/SysMon/refs/heads/main/sysmon-3ds/banner.png
image_length: 25608
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
qr:
  sysmon-3ds.cia: https://db.universal-team.net/assets/images/qr/sysmon-3ds-cia.png
screenshots:
- description: Sysmon
  url: https://db.universal-team.net/assets/images/screenshots/sysmon/sysmon.png
source: https://github.com/Just-a-Spider/SysMon
stars: 2
systems:
- 3DS
title: SysMon
unique_ids:
- '0x1337'
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>Dev by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Just-a-Spider/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Just-a-Spider">@Just-a-Spider</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="5313619698"
  data-permission-text="Title is private" data-url="https://github.com/Just-a-Spider/SysMon/issues/1"
  data-hovercard-type="pull_request" data-hovercard-url="/Just-a-Spider/SysMon/pull/1/hovercard"
  href="https://github.com/Just-a-Spider/SysMon/pull/1">#1</a></li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Just-a-Spider/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Just-a-Spider">@Just-a-Spider</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5313619698" data-permission-text="Title is private" data-url="https://github.com/Just-a-Spider/SysMon/issues/1"
  data-hovercard-type="pull_request" data-hovercard-url="/Just-a-Spider/SysMon/pull/1/hovercard"
  href="https://github.com/Just-a-Spider/SysMon/pull/1">#1</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.2...v0.3.3"><tt>v0.3.2...v0.3.3</tt></a></p>'
updated: '2026-09-01T15:42:19Z'
version: v0.3.3
version_title: v0.3.3
---
**Note: This application requires sysmon-server running on a Linux PC.**

SysMon connects a Nintendo 3DS to a Linux PC over local Wi-Fi to display system telemetry and provide remote input controls.

### Features
* **Telemetry:** Displays PC CPU usage, CPU/GPU temperatures, clock frequencies, fan speeds, free RAM, uptime, and weather.
* **Gamepad Controller (CTRL):** Low-latency UDP controller mapped to the Linux uinput virtual gamepad driver.
* **Macro Deck (MACRO):** Triggers custom commands, shell scripts, and keyboard shortcuts via touch buttons or 3DS buttons (A/B/X/Y).
* **Audio Level Mixer (LEVEL):** Adjusts volume and mute states for active audio applications via PulseAudio or PipeWire.
* **Media Controls (MEDIA):** Controls playback (play, pause, skip) and displays track metadata via MPRIS.
* **Process Manager (KILL):** Displays high-CPU processes and allows terminating unresponsive applications.
* **Focus Timer (POMO):** Built-in Pomodoro timer.
* **Settings (SET):** Supports multiple server profiles, theme switching, and audio feedback.

### Setup
1. Download and run `sysmon-server` on your Linux PC (`cargo build --release` or install the RPM package).
2. Open the SET tab in SysMon on your 3DS and enter your PC IP address and port (default: 7341).
3. For gamepad functionality, ensure your Linux user account has write access to `/dev/uinput`.

Source code and server downloads are available at the [GitHub Repository](https://github.com/Just-a-Spider/SysMon).