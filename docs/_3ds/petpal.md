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
    size: 31234376
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.4/PetPal.3dsx
  PetPal.cia:
    size: 31404992
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.4/PetPal.cia
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
update_notes: '<h1 dir="auto">PetPal v0.1.4</h1>

  <p dir="auto"><strong>The care, play &amp; profiles release.</strong> Your pet now
  has real needs and moods, a daily care streak, a quick arcade minigame, badges by
  its name — and a linked 3DS + phone finally share the <em>same pet</em>, not just
  the same identity.</p>

  <h2 dir="auto">✨ New</h2>

  <ul dir="auto">

  <li><strong>Needs, moods &amp; Rest</strong> — happiness, energy, and a new <strong>hunger</strong>
  need now drain in real time (even while the app is closed). Your pet shows a live
  <strong>mood</strong> — Happy, Content, Hungry, Tired, or Sad — on the Pet screen.
  Feeding fills the belly, and a new <strong>Rest</strong> action restores energy.</li>

  <li><strong>Daily care streak</strong> — tend your pet at least once a day to build
  a streak. Every 7 days pays out a <strong>coin bonus</strong>. Your current streak
  shows right on the Pet screen.</li>

  <li><strong>Star Tap minigame</strong> — press <strong>Y</strong> on the Pet screen
  to play a quick reaction game. Tap the target before the timer runs out for <strong>coins
  and a happiness boost</strong>.</li>

  <li><strong>Cross-device pet continuity</strong> — a linked 3DS and PetPal Android
  app now keep the <strong>same pet in sync</strong> (name, species, stage, level,
  and stats), reconciled automatically each time you open the app. (v0.1.3 linked
  only the identity; v0.1.4 syncs the actual pet.)</li>

  <li><strong>Profile badges</strong> — server-assigned tags shown next to your pet''s
  name: <strong>Owner, Developer, Network Mod, Helper, Support Team, Testing Bot</strong>,
  plus an automatic <strong>1-Year-Club</strong> badge once your account turns a year
  old. Badges appear on both the 3DS and Android.</li>

  </ul>

  <h2 dir="auto">🔧 Changed</h2>

  <ul dir="auto">

  <li><strong>Pet screen top display</strong> now shows your pet''s mood, a hunger
  bar, your care streak, and any profile badges alongside the existing stats.</li>

  <li><strong>Phone linking</strong> is more robust — the console keeps its own credential
  after linking, which is what enables two-way pet syncing.</li>

  <li>Settings now reports <strong>version 0.1.4</strong>.</li>

  </ul>

  <h2 dir="auto">⬆️ Upgrade</h2>

  <p dir="auto">Same title ID as v0.1.3 — installs as a standard update. Your existing
  save is safe and <strong>upgrades automatically</strong> (save format v3 → v4) on
  first launch. No reset needed.</p>

  <hr>

  <p dir="auto"><em>Requires a modded 3DS. Online features (passes, linking, badges)
  need an internet connection. Not affiliated with Nintendo.</em></p>'
updated: '2026-07-17T22:45:33Z'
version: v0.1.4
version_title: PetPal v0.1.4 Public
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