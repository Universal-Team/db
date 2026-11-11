---
author: noeljustin
avatar: https://avatars.githubusercontent.com/u/10400593?v=4
categories:
- game
color: '#272626'
color_bg: '#272626'
created: '2026-11-10T16:26:25Z'
description: Night racing roguelike on Japanese mountain roads.
download_filter: ^tougelike\.(cia|3dsx)$
download_page: https://github.com/njlent/tougelike-3ds-pub/releases
downloads:
  tougelike.3dsx:
    size: 51872568
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.37/tougelike.3dsx
  tougelike.cia:
    size: 52171712
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.37/tougelike.cia
github: njlent/tougelike-3ds-pub
icon: https://raw.githubusercontent.com/njlent/tougelike-3ds-pub/main/assets/icon.png
image: https://raw.githubusercontent.com/njlent/tougelike-3ds-pub/main/assets/banner.png
image_length: 70297
layout: app
license: other
license_name: Other
llm_generation: 'yes'
qr:
  tougelike.cia: https://db.universal-team.net/assets/images/qr/tougelike-cia.png
screenshots:
- description: 01_title screen
  url: https://db.universal-team.net/assets/images/screenshots/tougelike/01_title-screen.png
- description: 02_mountain road
  url: https://db.universal-team.net/assets/images/screenshots/tougelike/02_mountain-road.png
- description: 03_rival takedown
  url: https://db.universal-team.net/assets/images/screenshots/tougelike/03_rival-takedown.png
- description: 04_route map
  url: https://db.universal-team.net/assets/images/screenshots/tougelike/04_route-map.png
- description: 05_module draft
  url: https://db.universal-team.net/assets/images/screenshots/tougelike/05_module-draft.png
- description: 06_garage
  url: https://db.universal-team.net/assets/images/screenshots/tougelike/06_garage.png
source: https://github.com/njlent/tougelike-3ds-pub
stars: 10
systems:
- 3DS
title: Tougelike
unique_ids:
- '0xF7A3C'
update_notes: '<p dir="auto"><strong>Tougelike for Nintendo 3DS</strong> is the night
  racing roguelike on Japanese mountain roads, ported from the web game to the 3DS
  and 2DS. Race down touge passes in the dark, drift through the bends, weave through
  traffic, take down rivals and bosses, and build every run from module drafts. It
  runs on the Old 3DS, New 3DS, 2DS and New 2DS, installs to the HOME Menu as a CIA,
  runs from the Homebrew Launcher as a 3DSX, and opens in emulators as a .3ds.</p>

  <h2 dir="auto">What''s new</h2>

  <h3 dir="auto">3DS 00.01.37</h3>

  <ul dir="auto">

  <li>The speed-ups in this version are still experimental. So far they have run in
  the emulator and passed one test on a real console. If the picture looks wrong or
  the game stutters, turn OPTIONS, VISUAL, SECOND CORE off or set FRAME RATE to 30,
  and report what you saw.</li>

  <li>A New 3DS now runs the game at 60 frames a second where it keeps up, and holds
  a steady 30 where it does not. OPTIONS, VISUAL, FRAME RATE set to 30 keeps it at
  30 all the time.</li>

  <li>An Old 3DS or 2DS holds 30 frames a second through much more of a run. In the
  emulator at their speed, a late run went from 19 to 27 frames a second.</li>

  <li>Driving looks smoother at the same frame rate. The game''s clock used to follow
  how long each frame took to work out. It now follows the pictures on the screen.</li>

  <li>The scenery is rebuilt on the console''s second processor core. OPTIONS, VISUAL,
  SECOND CORE turns that off.</li>

  <li>DEBUG now shows the frame rate, the CPU and GPU time of a frame and the free
  memory.</li>

  <li>The game writes a line about its speed to tougelike.log on the SD card every
  600 frames.</li>

  </ul>

  <h2 dir="auto">Downloads</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>File</th>

  <th>For</th>

  <th>Size</th>

  <th>SHA-256</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">tougelike.cia</code></td>

  <td>HOME Menu, installed with FBI</td>

  <td>49.8 MB</td>

  <td><code class="notranslate">c7aa94f0f6199196812c7253fd082b588885143ad625f951a27cfa55406aa062</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3dsx</code></td>

  <td>Homebrew Launcher</td>

  <td>49.5 MB</td>

  <td><code class="notranslate">b0d5f41c0f11724df80b453bc20e8597987e0d0c910da5772cdcb614b7a36ef3</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3ds</code></td>

  <td>Emulators such as Azahar</td>

  <td>49.7 MB</td>

  <td><code class="notranslate">5e365b2bf5e582a47c2e02bad8168c0ab908886c518bd1513a7d852c8ff9614f</code></td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <h2 dir="auto">Install</h2>

  <ul dir="auto">

  <li><strong>HOME Menu (CIA):</strong> copy <code class="notranslate">tougelike.cia</code>
  to the SD card, open FBI, choose SD, pick the file and install it. Tougelike then
  has its own icon and banner on the HOME Menu.</li>

  <li><strong>QR code:</strong> in FBI, choose Remote Install, then Scan QR Code,
  and scan the code on the <a href="https://github.com/njlent/tougelike-3ds-pub#install">project
  page</a>. It installs the newest CIA.</li>

  <li><strong>Homebrew Launcher (3DSX):</strong> copy <code class="notranslate">tougelike.3dsx</code>
  to the <code class="notranslate">/3ds/</code> folder on the SD card and start it
  from the Homebrew Launcher.</li>

  <li><strong>Emulator (.3ds):</strong> open <code class="notranslate">tougelike.3ds</code>
  in Azahar or any front end that lists <code class="notranslate">.3ds</code> games.
  The 3DSX opens there too, and the CIA installs with File, Install CIA. The <code
  class="notranslate">.3ds</code> is for emulators only; on a console, install the
  CIA.</li>

  </ul>

  <p dir="auto">Both keep their saves in the same files on the SD card, so you can
  switch between them.</p>

  <h2 dir="auto">Requirements</h2>

  <ul dir="auto">

  <li>A Nintendo 3DS, 2DS, New 3DS or New 2DS with custom firmware (Luma3DS) to run
  homebrew.</li>

  <li>For sound, a DSP firmware dump at <code class="notranslate">sdmc:/3ds/dspfirm.cdc</code>,
  made once with DSP1.</li>

  <li>About 60 MB free on the SD card.</li>

  <li>A New 3DS aims for 60 fps and an Old 3DS or 2DS for 30. Each drops to the next
  steady rate, 30 or 20, in the busiest late-game runs. This is new in 3DS 00.01.37
  and still experimental.</li>

  </ul>

  <h2 dir="auto">Version</h2>

  <p dir="auto">3DS 00.01.37, built on Tougelike 00.22.39 (upstream commit <code class="notranslate">22b94e1</code>).
  Full history: <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.37/CHANGELOG.md">CHANGELOG.md</a>.</p>

  <p dir="auto">Tougelike by Noel Justin Lent (njlent). Copying or sharing this build
  needs the author''s permission, so link to this page instead. The licence is in
  <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.37/LICENSE">LICENSE</a>
  and in the game under LICENCE.</p>'
updated: '2026-11-11T12:20:38Z'
version: v0.1.37
version_title: Tougelike for Nintendo 3DS 00.01.37
---
Tougelike is a night racing roguelike set on Japanese mountain roads. Navigate through challenging terrain, avoid obstacles, and survive the night in this fast-paced adventure.

More info on [github](https://github.com/njlent/tougelike-3ds-pub).