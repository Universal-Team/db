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
    size: 51881840
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.39/tougelike.3dsx
  tougelike.cia:
    size: 52184000
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.39/tougelike.cia
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
stars: 11
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

  <h3 dir="auto">3DS 00.01.39</h3>

  <ul dir="auto">

  <li>OPTIONS, VISUAL, PARTICLES now sets how much the module effects draw. DYNAMIC
  draws every spark, flame and puff of smoke, STATIC about half of them, DISABLED
  the fewest. Before, DYNAMIC and STATIC looked the same on the 3DS.</li>

  <li>PARTICLES starts on STATIC, which runs a little faster in runs full of effects.
  A setting saved by an earlier version moves to STATIC once, and DISABLED stays.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.38</h3>

  <ul dir="auto">

  <li>An Old 3DS or 2DS that cannot hold 30 frames a second no longer drops to a steady
  20. It shows every frame as soon as it is ready. A real Old 3DS ran the last version
  at 20 early in a run, and the emulator at that console''s speed runs this one at
  24.</li>

  <li>The installed version never used the second processor core on an Old 3DS or
  2DS, because the system refused the share of it the game asked for. It gets that
  share now.</li>

  <li>Late in a run the game stuttered twice a second while it rebuilt the module
  list on the bottom screen. It now rebuilds the list only when it changes.</li>

  <li>Below 30 frames a second the gauges on the top screen are redrawn every other
  frame, which leaves more time for the race.</li>

  <li>The speed lines in tougelike.log now say which part of the game the time went
  to.</li>

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

  <td><code class="notranslate">dac52da79ecb2c7ecc1ff8af2ed71d23cde397f38fb4d8df651de558cd911a93</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3dsx</code></td>

  <td>Homebrew Launcher</td>

  <td>49.5 MB</td>

  <td><code class="notranslate">695142c6100a2c36eb666845961c4498d0e5381a7024ad98c9defdc3c8c1b706</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3ds</code></td>

  <td>Emulators such as Azahar</td>

  <td>49.8 MB</td>

  <td><code class="notranslate">f846771d614a9a921dd05a3addfe33e6f5e19cf1cc5cccee5ff85e4d0029e320</code></td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <h2 dir="auto">Install</h2>

  <ul dir="auto">

  <li><strong>HOME Menu (CIA):</strong> copy <code class="notranslate">tougelike.cia</code>
  to the SD card, open FBI, choose SD, pick the file and install it. Tougelike then
  has its own icon and banner on the HOME Menu.</li>

  <li><strong>Universal-Updater:</strong> find Tougelike in Universal-Updater and
  install the CIA or the 3DSX from there. It is <a href="https://db.universal-team.net/3ds/tougelike"
  rel="nofollow">listed on Universal-DB</a>.</li>

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

  <li>A New 3DS aims for 60 fps and holds 30 where it cannot keep up. An Old 3DS or
  2DS aims for 30 and runs below it in busy stretches, more so late in a long run.
  The speed-ups since 3DS 00.01.37 are still experimental.</li>

  </ul>

  <h2 dir="auto">Version</h2>

  <p dir="auto">3DS 00.01.39, built on Tougelike 00.22.39 (upstream commit <code class="notranslate">22b94e1</code>).
  Full history: <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.39/CHANGELOG.md">CHANGELOG.md</a>.</p>

  <p dir="auto">Tougelike by Noel Justin Lent (njlent). Copying or sharing this build
  needs the author''s permission, so link to this page instead. The licence is in
  <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.39/LICENSE">LICENSE</a>
  and in the game under LICENCE.</p>'
updated: '2026-11-11T22:25:43Z'
version: v0.1.39
version_title: Tougelike for Nintendo 3DS 00.01.39
---
Tougelike is a night racing roguelike set on Japanese mountain roads. Navigate through challenging terrain, avoid obstacles, and survive the night in this fast-paced adventure.

More info on [github](https://github.com/njlent/tougelike-3ds-pub).