---
author: jamesrhg
avatar: https://avatars.githubusercontent.com/u/306910809?v=4
categories:
- app
color: '#ffbdd2'
color_bg: '#805e69'
created: '2026-09-28T04:18:51Z'
description: Nintendo 3DS chatting app with Miis, images, voice and video calls.
download_page: https://github.com/jamesrhg/chatnow/releases
downloads:
  ChatNow-v1.0.2.cia:
    size: 11776960
    size_str: 11 MiB
    url: https://github.com/jamesrhg/chatnow/releases/download/v1.0.2/ChatNow-v1.0.2.cia
github: jamesrhg/chatnow
icon: https://raw.githubusercontent.com/jamesrhg/chatnow/refs/heads/main/meta/icon.png
image: https://raw.githubusercontent.com/jamesrhg/chatnow/refs/heads/main/meta/banner.png
image_length: 8757
layout: app
llm_generation: minor
qr:
  ChatNow-v1.0.2.cia: https://db.universal-team.net/assets/images/qr/chatnow-v1-0-2-cia.png
source: https://github.com/jamesrhg/chatnow
stars: 1
systems:
- 3DS
title: ChatNow
unique_ids:
- '0xBA436'
update_notes: '<p dir="auto">ChatNow v1.0.2</p>

  <ul dir="auto">

  <li>Corrected the installed CIA title version so it matches the app''s displayed
  v1.0.2 version.</li>

  <li>Made connected-user names and usernames easier to read, with two separate lines
  and a fixed device column. Checked live socket counts, reconnect replacement, the
  32-connection limit, and Web light/dark layouts.</li>

  <li>Made the Circle Pad move focus in Settings like the D-pad, including hold-to-repeat
  and keeping the selected item visible.</li>

  <li>Disabled HOME during every software keyboard call and restored the screen''s
  HOME policy afterward.</li>

  <li>Improved manual sign-in/account-creation SpotPass downloads: enabled news and
  extended-banner tasks run sequentially with foreground priority, the UI stays responsive,
  and the temporary BOSS daemon allowance is released before continuing.</li>

  <li>Added a localized "Please wait... / This might take a while..." screen with
  animated dots during those downloads.</li>

  <li>Fixed the DM notification LED timing. Pink notifications now fade smoothly for
  one second, followed by two half-second glows with short gaps. Notifications remain
  suppressed while viewing that sender''s DM.</li>

  <li>Checked Friends presence descriptions against the SDK''s buffer and visible-line
  limits; long descriptions now end with "..." without splitting characters.</li>

  </ul>

  <p dir="auto">The service continues accepting v1.0.0 and v1.0.1 clients. Install
  the attached CIA to update.</p>

  <p dir="auto">All 99 regression programs passed, covering native startup/service/client/media
  scenarios, browser/server behavior and all 18 locale catalogs. The CIA was rebuilt
  with make clean and its title version and content hash were verified. Actual Nintendo
  library-applet behavior and LED appearance still require console testing.</p>

  <p dir="auto">CIA SHA-256: <code class="notranslate">72142b236d4a3e12d16a0c21e2e15697ec596ae9c5af5897b8a961ddc1ddc841</code></p>'
updated: '2026-10-09T12:46:24Z'
version: v1.0.2
version_title: ChatNow v1.0.2
---
ChatNow is a really cool chat app for the Nintendo 3DS (and more devices, soon) with Miis as avatars, DMs, voice and video calls, and a fun Camera Mode to take pictures on 3D with your Miis.

If enabled, you can recieve Notifications from the ChatNow Team when new cool stuff happens, and a blue dot in the app icon if you have recieved a DM from a friend.