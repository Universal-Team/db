---
author: Dingplay
avatar: https://avatars.githubusercontent.com/u/92917369?v=4
categories:
- app
color: '#fbb361'
color_bg: '#805b31'
created: '2026-09-17T20:07:56Z'
description: 'Chat with your Dingplay friends from a 3DS: DMs, the world chat and
  console-only rooms online, or text / drawings / voice over Local Wireless.'
download_page: https://github.com/Sonalpt/Dingplay-chat-3DS/releases
downloads:
  dingplay-chat.3dsx:
    size: 4178120
    size_str: 3 MiB
    url: https://github.com/Sonalpt/Dingplay-chat-3DS/releases/download/v0.1.1/dingplay-chat.3dsx
  dingplay-chat.cia:
    size: 4211648
    size_str: 4 MiB
    url: https://github.com/Sonalpt/Dingplay-chat-3DS/releases/download/v0.1.1/dingplay-chat.cia
github: Sonalpt/Dingplay-chat-3DS
icon: https://raw.githubusercontent.com/Sonalpt/Dingplay-chat-3DS/main/meta/icon.png
image: https://raw.githubusercontent.com/Sonalpt/Dingplay-chat-3DS/main/meta/banner.png
image_length: 9209
layout: app
llm_generation: 'no'
qr:
  dingplay-chat.cia: https://db.universal-team.net/assets/images/qr/dingplay-chat-cia.png
source: https://github.com/Sonalpt/Dingplay-chat-3DS
stars: 0
systems:
- 3DS
title: Dingplay-chat-3DS
unique_ids:
- '0xD1A6'
update_notes: '<p dir="auto">Security and polish release. <strong>This is the build
  to use</strong> — the relay is now HTTPS-only, so 0.1.0 can no longer connect.</p>

  <p dir="auto"><strong>Secure connection</strong></p>

  <ul dir="auto">

  <li>The console talks to the relay over <strong>HTTPS with a pinned certificate</strong>
  (the app trusts only Dingplay''s own CA). Passwords and session tokens can no longer
  be read or spoofed on shared Wi-Fi.</li>

  </ul>

  <p dir="auto"><strong>Hardening</strong></p>

  <ul dir="auto">

  <li>Per-IP and per-account rate limits on the relay (login brute-force protection).</li>

  <li>Sessions are 30 days and are properly revoked on sign-out.</li>

  <li>The console no longer writes typed passwords to its debug log.</li>

  </ul>

  <p dir="auto"><strong>Fixes &amp; polish since 0.1.0</strong></p>

  <ul dir="auto">

  <li>Crisp, correctly-sized text (two font atlases; Nunito Regular/Bold).</li>

  <li>The Dingplay artwork: real icons, wordmark, world-chat background.</li>

  <li>Upright, correctly-fitted profile pictures.</li>

  <li>Host "Close room" control for online themed rooms.</li>

  </ul>

  <p dir="auto"><strong>Install</strong></p>

  <ul dir="auto">

  <li><code class="notranslate">dingplay-chat.cia</code> — install with FBI (or via
  Universal-Updater).</li>

  <li><code class="notranslate">dingplay-chat.3dsx</code> — copy to <code class="notranslate">/3ds/</code>
  for the Homebrew Launcher.</li>

  </ul>

  <p dir="auto">Voice playback needs <code class="notranslate">/3ds/dspfirm.cdc</code>
  on the SD card (dump once with DSP1).</p>'
updated: '2026-09-28T08:25:52Z'
version: v0.1.1
version_title: Dingplay Chat 0.1.1
website: https://www.dingplay.net
---
