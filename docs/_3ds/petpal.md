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
    size: 31211192
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.2/PetPal.3dsx
  PetPal.cia:
    size: 31392704
    size_str: 29 MiB
    url: https://github.com/PetPal-Team/PetPal/releases/download/v0.1.2/PetPal.cia
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
update_notes: '<h1 dir="auto">🐾 PetPal v0.1.2</h1>

  <p dir="auto">A safety-and-maintenance release: automatic update notifications,
  community name<br>

  moderation, and a unique title ID so PetPal installs cleanly alongside other homebrew.</p>

  <h2 dir="auto">✨ What''s new</h2>

  <ul dir="auto">

  <li><strong>🛡️ Name moderation</strong> — Offensive pet names are now automatically
  filtered, both on<br>

  the PetPal servers and on your console. Bad names from other players appear as <strong>"Pal"</strong><br>

  instead, and an already-saved friend gets cleaned up the next time you pass them.
  Your<br>

  own pet name is filtered too. The matcher is fuzzy, so tricks like <code class="notranslate">B!tch</code>,
  <code class="notranslate">n1gg@</code>,<br>

  <code class="notranslate">f.u.c.k</code> and repeated letters don''t get through.</li>

  <li><strong>🔔 Update notifications</strong> — PetPal checks for the latest version
  on launch and shows a<br>

  <strong>"Please update your app."</strong> prompt when a newer release is out (press
  START to close).<br>

  If you''re offline, nothing changes.</li>

  <li><strong>🆔 Unique title ID</strong> — PetPal''s title ID was changed off the
  shared homebrew default,<br>

  so it no longer collides with other apps (e.g. IP-Cam Viewer, SCR2JPG) and installs<br>

  cleanly for Universal-DB.</li>

  <li>The Settings screen now shows the full version (e.g. <strong>v0.1.2</strong>).</li>

  </ul>

  <h2 dir="auto">⬆️ Upgrading from 0.1.0 / 0.1.1</h2>

  <p dir="auto">Because the title ID changed, this CIA installs as a <strong>separate</strong>
  title — it won''t replace<br>

  an older PetPal automatically. <strong>Delete the old PetPal</strong> from your
  HOME Menu after<br>

  installing this one. Your <strong>save data is safe</strong>: it lives on the SD
  card at<br>

  <code class="notranslate">sdmc:/3ds/PetPal/</code>, independent of the title.</p>

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

  </table></markdown-accessiblity-table>

  <p dir="auto"><strong>Full changelog:</strong> <a class="commit-link" href="https://github.com/PetPal-Team/PetPal/compare/v0.1.1...v0.1.2"><tt>v0.1.1...v0.1.2</tt></a></p>'
updated: '2026-07-05T19:18:38Z'
version: v0.1.2
version_title: PetPal v0.1.2 Public
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