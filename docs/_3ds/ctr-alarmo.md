---
author: FelixHomebrew
avatar: https://codeberg.org/avatars/5170b04eae5f1359e4ce236a7e59b002c0811db790bd51c8f44b2c5ed5c6f15d
categories:
- app
color: '#401313'
color_bg: '#401313'
created: '2026-03-26T14:19:17Z'
description: A silly alarm clock app for the Nintendo 3DS
download_page: https://codeberg.org/FelixHomebrew/CtrAlarmo/releases
downloads:
  CtrAlarmo.3dsx:
    size: 1263176
    size_str: 1 MiB
    url: https://codeberg.org/FelixHomebrew/CtrAlarmo/releases/download/1.1.0/CtrAlarmo.3dsx
  CtrAlarmo.cia:
    size: 1307584
    size_str: 1 MiB
    url: https://codeberg.org/FelixHomebrew/CtrAlarmo/releases/download/1.1.0/CtrAlarmo.cia
forgejo: FelixHomebrew/CtrAlarmo
forgejo_host: codeberg.org
icon: https://codeberg.org/FelixHomebrew/CtrAlarmo/raw/branch/main/exefs/icon_48.png
image: https://codeberg.org/FelixHomebrew/CtrAlarmo/raw/branch/main/exefs/banner.png
image_length: 6751
layout: app
license: mit
license_name: MIT License
llm_generation: unknown
qr:
  CtrAlarmo.cia: https://db.universal-team.net/assets/images/qr/ctralarmo-cia.png
screenshots:
- description: Main
  url: https://db.universal-team.net/assets/images/screenshots/ctr-alarmo/main.png
source: https://codeberg.org/FelixHomebrew/CtrAlarmo
stars: 3
systems:
- 3DS
title: CTR Alarmo
unique_ids:
- '0xC4A1A'
update_notes: '<div class="markdown-heading"><h2 class="heading-element">What''s new?</h2><a
  id="user-content-whats-new" class="anchor" aria-label="Permalink: What''s new?"
  href="#whats-new"><span aria-hidden="true" class="octicon octicon-link"></span></a></div>

  <ul>

  <li>Now disables forced JACK redirection in app, allowing beep alarm to be played
  while sleep mode</li>

  <li>Allow streetpass state in sleep mode</li>

  </ul>

  <div class="markdown-heading"><h2 class="heading-element">Changes</h2><a id="user-content-changes"
  class="anchor" aria-label="Permalink: Changes" href="#changes"><span aria-hidden="true"
  class="octicon octicon-link"></span></a></div>

  <ul>

  <li>Disabled HOME menu button, read comment at <a href="https://github.com/FelixHomebrew/CtrAlarmo/blob/1.1.0/source/main.c#L39">main.c:39</a>
  to know more</li>

  </ul>

  <div class="markdown-heading"><h2 class="heading-element">Fixes</h2><a id="user-content-fixes"
  class="anchor" aria-label="Permalink: Fixes" href="#fixes"><span aria-hidden="true"
  class="octicon octicon-link"></span></a></div>

  <ul>

  <li>Exception occured sometimes on alarm shut with Power/Wireless LEDs blink enabled</li>

  <li>Exception occured often on shut beep melody, due to a misuse of waveBuf</li>

  </ul>

  '
updated: '2026-02-17T03:08:44Z'
version: 1.1.0
version_title: v 1.1.0
---

A simple, configurable alarm clock app for the Nintendo 3DS.

## Features
* Regular audible beep
* Power/Wireless/News LEDs blink support
* 2 ring modes (Static \& Progressive)
* Rings for 10 minutes, then sleeps 5 minutes before ringing again
* Adjustable screens brightness
* Sleep mode persistence (no sound/LEDs only)

New features would may be added in the future.

## Usage
Alarm time can be set from Settings: Press `SELECT` (hotkeys are listed on bottom screen) then look for "Redefine alarm".
Adjust other settings depending on your preferences.