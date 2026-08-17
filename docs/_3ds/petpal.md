---
author: PetPal Team, DisLoPik
avatar: https://avatars.githubusercontent.com/u/293414143?v=4
categories:
- game
- app
color: '#7dd9cb'
color_bg: '#498077'
created: '2026-06-20T15:29:20Z'
description: 'A virtual StreePass pet for Nintendo 3DS '
download_page: https://github.com/PetPal-Team/PetPal/releases
downloads:
  PetPal.3dsx:
    size: 31272004
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/0.1.7/PetPal.3dsx
  PetPal.cia:
    size: 31433664
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/0.1.7/PetPal.cia
github: PetPal-Team/PetPal
icon: https://raw.githubusercontent.com/PetPal-Team/PetPal/refs/heads/main/Pet%20Pal.png
image: https://raw.githubusercontent.com/PetPal-Team/PetPal/refs/heads/main/banner.png
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
qr:
  PetPal.cia: https://db.universal-team.net/assets/images/qr/petpal-cia.png
screenshots:
- description: Friends
  url: https://db.universal-team.net/assets/images/screenshots/petpal/friends.png
- description: Pet journal
  url: https://db.universal-team.net/assets/images/screenshots/petpal/pet-journal.png
- description: Stats
  url: https://db.universal-team.net/assets/images/screenshots/petpal/stats.png
source: https://github.com/PetPal-Team/PetPal
stars: 8
systems:
- 3DS
title: PetPal
unique_ids:
- '0xF00D5'
update_notes: '<h1 dir="auto">PetPal 3DS — v0.1.7</h1>

  <h2 dir="auto">✨ Highlights</h2>

  <ul dir="auto">

  <li><strong>Real StreetPass!</strong> The app now creates its own CEC message box
  on hardware —<br>

  it shows up in System Settings and cectool. Pets exchange locally over<br>

  StreetPass (and over the internet via NetPass), on top of the existing<br>

  teampetpal.com relay. <em>Install the <code class="notranslate">.cia</code> for
  this — the <code class="notranslate">.3dsx</code> under HBL<br>

  can''t be granted the system CEC permission, but still passes via the relay.</em></li>

  <li><strong>📢 News page.</strong> A new Announcements screen (press <strong>Y</strong>
  on the main menu)<br>

  shows Markdown-formatted messages from the PetPal team, fetched from<br>

  teampetpal.com.</li>

  <li><strong>🎨 UI polish.</strong> Pixel star ratings (friendship tiers + awards),
  pixel stat<br>

  bars (happiness / energy / hunger / XP), and evolution-stage emblems on the<br>

  Pet screen.</li>

  </ul>

  <h2 dir="auto">🧹 Changes &amp; fixes</h2>

  <ul dir="auto">

  <li>Removed the leftover developer CEC self-test / diagnostic text from the<br>

  Friends screen.</li>

  <li>Onboarding now reports the pet''s name to the account (fixes blank names in
  the<br>

  admin panel).</li>

  <li>Added translation-ready string catalogs (English + French) under <code class="notranslate">Strings/</code>.</li>

  </ul>

  <h2 dir="auto">🔧 Under the hood</h2>

  <ul dir="auto">

  <li><code class="notranslate">kAppVersion</code> → <strong>0.1.7</strong>; save
  format unchanged (<strong>v4</strong>, backward-compatible).</li>

  <li>New: <code class="notranslate">AnnouncementsClient</code>, a dependency-free
  Markdown renderer (<code class="notranslate">ui/Markdown</code>),<br>

  and the <code class="notranslate">AnnouncementsScreen</code>.</li>

  </ul>

  <p dir="auto"><strong>Install:</strong> grab <code class="notranslate">PetPal.cia</code>
  (recommended — enables real StreetPass) or<br>

  <code class="notranslate">PetPal.3dsx</code>.</p>'
updated: '2026-08-06T11:38:32Z'
version: 0.1.7
version_title: PetPal 0.1.7
website: https://teampetpal.com
wiki: https://teampetpal.com/wiki
---
# 🐾 PetPal — a StreetPass-style Virtual Pet for the Nintendo 3DS

PetPal is a homebrew virtual-pet game in the spirit of the StreetPass era. You
raise one pet — feed it, play with it, send it on adventures, dress it up — and
every other player you "pass" becomes a friend who brings your pet XP, gifts, and
progress toward evolution. Passing happens **over the internet** through PetPal's
own relay, so it works from anywhere without needing another console nearby.

Bright, bouncy dual-screen UI, procedurally-drawn pets, a music track and sound
effects, an auto-written journal, a coin shop, and a redeemable code system.

> **Built with** C++17 · devkitPro · libctru · citro2d/citro3d · ndsp · 3ds-curl.
> Runs on Old 3DS, New 3DS/2DS (any modded console).