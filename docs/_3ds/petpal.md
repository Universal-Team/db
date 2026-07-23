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
    size: 31234388
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.6/PetPal.3dsx
  PetPal.cia:
    size: 31404992
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.6/PetPal.cia
github: PetPal-Team/PetPal
icon: https://raw.githubusercontent.com/PetPal-Team/PetPal/refs/heads/main/Pet%20Pal.png
image: https://raw.githubusercontent.com/PetPal-Team/PetPal/refs/heads/main/banner.png
image_length: 25573
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
stars: 6
systems:
- 3DS
title: PetPal
unique_ids:
- '0xF00D5'
update_notes: '<h1 dir="auto">🐾 PetPal v0.1.6 — Nintendo 3DS</h1>

  <p dir="auto">A small maintenance release that keeps the pass network healthy by
  making sure<br>

  everyone trading pets is on the latest version.</p>

  <h2 dir="auto">🔄 Version-aware passing</h2>

  <ul dir="auto">

  <li>PetPal now includes its version in every pass it sends, so the relay can keep<br>

  all trading players on the current release.</li>

  <li><strong>Out-of-date copies now get <code class="notranslate">Pass FAIL</code></strong>
  when checking for new passes —<br>

  updating to 0.1.6 clears it.</li>

  <li>On boot, older copies are reminded with a <strong>“Please update your app.”</strong>
  prompt.</li>

  </ul>

  <h2 dir="auto">🛠️ Under the hood</h2>

  <ul dir="auto">

  <li>Bumped app version to <strong>0.1.6</strong> (<code class="notranslate">kAppVersion</code>).</li>

  <li>Pass packets now carry an app-version stamp in a previously-reserved field.<br>

  It’s covered by the packet checksum and ignored by other consoles, so the pass<br>

  format stays fully compatible and your <strong>save is untouched</strong> (still
  save <strong>v4</strong>).</li>

  <li>No changes to the pass wire protocol — just the version tag the server reads.</li>

  <li>Companion <strong>Android app</strong> and the <strong>server</strong> also
  moved to 0.1.6 for parity.</li>

  </ul>

  <h2 dir="auto">📥 Installing / updating</h2>

  <ul dir="auto">

  <li><strong>CIA:</strong> reinstall <code class="notranslate">PetPal.cia</code>
  over your existing copy with FBI.</li>

  <li><strong>3DSX:</strong> copy <code class="notranslate">PetPal.3dsx</code> to
  <code class="notranslate">sdmc:/3ds/</code>.</li>

  <li>Your pet and save carry over automatically — no reset needed.</li>

  </ul>

  <hr>

  <p dir="auto"><em>Requires a modded 3DS (Luma3DS / CFW). Homebrew, non-commercial
  — not affiliated with Nintendo.</em></p>'
updated: '2026-07-23T02:11:39Z'
version: v0.1.6
version_title: REQUIRED PetPal 0.1.6 Public
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