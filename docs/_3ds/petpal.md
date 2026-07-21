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
    size: 31234380
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/0.1.5/PetPal.3dsx
  PetPal.cia:
    size: 31404992
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/0.1.5/PetPal.cia
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
update_notes: '<h1 dir="auto">PetPal v0.1.5 — 3DS</h1>

  <p dir="auto">A small but important fix for cross-device play.</p>

  <h2 dir="auto">🐛 Fixed</h2>

  <ul dir="auto">

  <li><strong>Cross-device pet sync is now reliable.</strong> When your 3DS uploads
  its pet to a<br>

  linked phone account, it now records the <strong>server''s</strong> timestamp as
  its sync<br>

  marker instead of the console''s own clock. Previously, if your 3DS''s date/time<br>

  was wrong — common on modded consoles — the "which device has the newer pet?"<br>

  check could get stuck, so changes from your phone might never reach the 3DS<br>

  (or vice-versa). Linking and continuity now work correctly no matter what your<br>

  console clock says.</li>

  </ul>

  <h2 dir="auto">🔧 Changed</h2>

  <ul dir="auto">

  <li>Version bumped to <strong>0.1.5</strong>.</li>

  </ul>

  <h2 dir="auto">⬆️ Upgrade</h2>

  <ul dir="auto">

  <li>Same title ID and same save format (<strong>v4</strong>) — installs as a standard
  update.<br>

  Your existing pet and save are untouched; no reset needed.</li>

  </ul>

  <h2 dir="auto">ℹ️ Note</h2>

  <ul dir="auto">

  <li>The rest of this release — the level-up rebalance, real achievements,<br>

  adventure-based meeting, friend requests, and the new Shop &amp; Customize<br>

  screens — arrived in the <strong>PetPal Android</strong> companion app and the server.
  Your<br>

  3DS shares the same account and relay, so a linked pet syncs and passes right<br>

  alongside them.</li>

  </ul>'
updated: '2026-07-21T22:05:08Z'
version: 0.1.5
version_title: PetPal 0.1.5 Public
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