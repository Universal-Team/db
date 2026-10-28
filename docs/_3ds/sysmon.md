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
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.4/SHA256SUMS.txt
  sysmon-3ds.3dsx:
    size: 4516860
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.4/sysmon-3ds.3dsx
  sysmon-3ds.cia:
    size: 4527040
    size_str: 4 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.4/sysmon-3ds.cia
  sysmon-server-0.3.4-1_amd64.deb:
    size: 3878348
    size_str: 3 MiB
    url: https://github.com/Just-a-Spider/SysMon/releases/download/v0.3.4/sysmon-server-0.3.4-1_amd64.deb
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
stars: 4
systems:
- 3DS
title: SysMon
unique_ids:
- '0x1337'
update_notes: '<h2 dir="auto">Release v0.3.4</h2>

  <h3 dir="auto">3DS Client Improvements</h3>

  <ul dir="auto">

  <li><strong>Settings Apply/Save Freeze Fix</strong>: Eliminated cross-thread socket
  destruction. Background worker threads now use cooperative cancellation (<code class="notranslate">g_telemetry_reconnect_req
  = 1</code>), closing and resetting their own sockets without blocking the main UI
  loop or contending for <code class="notranslate">libctru</code> <code class="notranslate">soc:u</code>
  mutexes.</li>

  <li><strong>Connection Timeout</strong>: Replaced system-default 75s blocking connect
  with non-blocking <code class="notranslate">connect()</code> + 4.0s <code class="notranslate">select()</code>
  timeout and <code class="notranslate">getpeername()</code> validation.</li>

  <li><strong>HUD Error State</strong>: Connection failures retain <code class="notranslate">TCP:
  ERROR</code> on the HUD for 3.0s before retrying, waking immediately if settings
  are changed or <code class="notranslate">SELECT</code> is pressed.</li>

  <li><strong>Manual Retry Hotkey</strong>: Press <code class="notranslate">SELECT</code>
  while in error state to trigger an immediate reconnect attempt.</li>

  <li><strong>Camera Stream Worker</strong>: Aligned <code class="notranslate">net_cam.c</code>
  with cooperative disconnection and non-blocking timeout handling.</li>

  </ul>

  <h3 dir="auto">Windows Host Support</h3>

  <ul dir="auto">

  <li><strong>TCP Connection Loop</strong>: Resolved immediate socket drop and reconnect
  loops on Windows hosts by validating TCP handshake before non-blocking polling.</li>

  <li><strong>Master Volume Control</strong>: Implemented native Windows WASAPI master
  volume control via <code class="notranslate">IAudioEndpointVolume</code>.</li>

  <li><strong>Monitor Brightness Control</strong>: Added hardware monitor brightness
  control using DXVA2 (<code class="notranslate">SetMonitorBrightness</code>) with
  PowerShell WMI (<code class="notranslate">WmiSetBrightness</code>) fallback for
  laptops.</li>

  </ul>

  <h3 dir="auto">Documentation &amp; UI</h3>

  <ul dir="auto">

  <li>Added screenshots covering dual HUD, macro controls, and virtual controller
  modes.</li>

  <li>Added comprehensive 20-segment HUD breakdown table to README.</li>

  <li>Documented GPU metrics (tracking core temperature &amp; fan speed).</li>

  </ul>

  <h3 dir="auto">Pull Requests</h3>

  <ul dir="auto">

  <li>Release v0.3.4: Windows Connection &amp; Slider Support, 3DS Settings Freeze
  Fix, HUD Docs by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Just-a-Spider/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Just-a-Spider">@Just-a-Spider</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="6084212995"
  data-permission-text="Title is private" data-url="https://github.com/Just-a-Spider/SysMon/issues/4"
  data-hovercard-type="pull_request" data-hovercard-url="/Just-a-Spider/SysMon/pull/4/hovercard"
  href="https://github.com/Just-a-Spider/SysMon/pull/4">#4</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/Just-a-Spider/SysMon/compare/v0.3.3...v0.3.4"><tt>v0.3.3...v0.3.4</tt></a></p>'
updated: '2026-10-28T17:54:02Z'
version: v0.3.4
version_title: v0.3.4
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