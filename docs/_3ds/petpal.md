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
    size: 31222324
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.3-1/PetPal.3dsx
  PetPal.cia:
    size: 31396800
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.3-1/PetPal.cia
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
stars: 4
systems:
- 3DS
title: PetPal
unique_ids:
- '0xF00D5'
update_notes: '<h1 dir="auto">🐾 PetPal v0.1.3</h1>

  <p dir="auto">An accounts-and-moderation release: every pet now has a unique ID,
  rule-breakers can be banned, and you can link your 3DS to the PetPal phone app.</p>

  <h2 dir="auto">✨ What''s new</h2>

  <ul dir="auto">

  <li><strong>🆔 Pet IDs</strong> — Every pet now gets a unique server ID (like <code
  class="notranslate">PP-ABCD-2345</code>), shown on the <strong>Settings</strong>
  screen. It''s assigned automatically the first time you play online and is what
  identifies your pet for linking, reports, and support.</li>

  <li><strong>⛔ Ban enforcement</strong> — Pets that break the rules (for example,
  an offensive name) can now be banned. A banned console shows a red <strong>"401
  Forbidden"</strong> screen at launch with its Pet ID for support, and can''t play
  or pass until it''s cleared.</li>

  <li><strong>🔗 Link to your phone</strong> — New <strong>Settings → Link to phone</strong>:
  enter the Link ID from the PetPal Android app to tie your 3DS and phone to the <strong>same</strong>
  pet identity (it then shows as <em>3ds &amp; Android</em>). Completely optional
  — your 3DS still works great on its own, and linking never touches your save data.
  <em>(Android version not released yet, coming soon. Code is just there for prep)</em></li>

  <li><strong>📣 Report a pet</strong> — Ran into an inappropriate pet? You can now
  report it by its ID at <strong>teampetpal.com/report</strong>, and a moderator will
  take a look.</li>

  <li><strong>🛡️ Expanded name filter</strong> — The moderation word list has grown
  (now catches <em>Herpy</em> and related terms). The fuzzy matching from v0.1.2 still
  applies, so leetspeak and repeated-letter tricks don''t get through.</li>

  <li>The Settings screen now shows your <strong>Pet ID</strong> alongside the version
  (<strong>v0.1.3</strong>).</li>

  </ul>

  <h2 dir="auto">⬆️ Upgrading from 0.1.2</h2>

  <p dir="auto">This release keeps the <strong>same title ID</strong> as v0.1.2, so
  it installs as a normal update over your existing PetPal — nothing to delete. Your
  <strong>save data is safe</strong>; older saves upgrade to the new format automatically
  the first time you launch. (Still on 0.1.0 / 0.1.1? Follow the v0.1.2 upgrade steps
  first.)</p>

  <h2 dir="auto">📦 Downloads</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>File</th>

  <th>Use</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">PetPal.cia</code></td>

  <td>Install to the HOME Menu (recommended)</td>

  </tr>

  <tr>

  <td><code class="notranslate">PetPal.3dsx</code></td>

  <td>Run from the Homebrew Launcher</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>'
updated: '2026-07-11T18:56:20Z'
version: v0.1.3-1
version_title: PetPal v0.1.3-1 Fix Pet name check
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