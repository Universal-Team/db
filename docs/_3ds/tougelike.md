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
    size: 51659416
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.53/tougelike.3dsx
  tougelike.cia:
    size: 51946432
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.53/tougelike.cia
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
stars: 12
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

  <h3 dir="auto">3DS 00.01.53</h3>

  <ul dir="auto">

  <li>A New 3DS is no longer held at 30 frames a second where it cannot reach 60.
  Each frame is shown as soon as it is ready, so the game runs at whatever the console
  manages above 30. OPTIONS, VISUAL, FRAME RATE 30 still gives the even 30.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.52</h3>

  <ul dir="auto">

  <li>On a New 3DS a race no longer changes its frame rate every half minute. The
  game stepped up from 30 whenever a moment of light frames suggested more was in
  reach, and stepped back a few seconds later. It now waits for a longer stretch of
  them, and each try that fails makes the next one wait twice as long.</li>

  <li><code class="notranslate">tougelike.log</code> no longer counts time in the
  HOME menu or asleep as loading.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.51</h3>

  <ul dir="auto">

  <li>A race no longer hitches about once a second on an Old 3DS or 2DS. The signs,
  lamps and posts beside the road were all placed again in a single frame each time.
  What decides where they stand is now kept until they move on, and late in a long
  run fewer than half as many frames take over a tenth of a second.</li>

  <li>A car model that loads in the middle of a race holds the game for less time.
  Its file is read in a third of the time it took.</li>

  <li>A frame takes slightly less time to draw.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.50</h3>

  <ul dir="auto">

  <li>Late in a run an Old 3DS or 2DS no longer stops for a tenth of a second every
  three seconds. The bottom screen worked the whole run out again each time, and that
  took longer with every part fitted.</li>

  <li>A car model that has to load in the middle of a race no longer freezes it. The
  load is spread over a few seconds of driving, and a third car of a kind is made
  ready the same way.</li>

  <li>Tunnels and the reservoir no longer hitch once a second while you drive past
  them.</li>

  <li>A New 3DS can now show more than 30 frames a second where it cannot hold 60.
  FRAME RATE 30 in the options keeps the even 30.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.49</h3>

  <ul dir="auto">

  <li>The freeze as a landmark comes up beside the road is gone. Placing a shrine''s
  or a lay-by''s trees and bushes held an Old 3DS or 2DS for a quarter to three quarters
  of a second each time. The console''s second core now places them while you drive,
  and they stand exactly where they did.</li>

  <li>With SECOND CORE off in the options the same moment takes about a twentieth
  of a second.</li>

  <li>A car of a kind not seen yet in the run, and the cars parked at a landmark,
  no longer hold an Old 3DS or 2DS for up to a tenth of a second the first time they
  are drawn.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.48</h3>

  <ul dir="auto">

  <li>Less stutter in a race on an Old 3DS or 2DS. A new car coming onto the road
  held the game for over a tenth of a second, and one whose model had to be loaded
  first for over a second. Cars are now made ready when their model loads, and loading
  one is much shorter. The game also starts about seven seconds sooner there.</li>

  <li>The cars are drawn with about a third fewer triangles and look the same, in
  the garage too. The valley beyond the road is drawn only where you can see it. Together
  a race has about a quarter less to draw, which takes work off the console''s graphics
  chip.</li>

  <li>Tunnels and the landmarks beside the road cost less while they are near, and
  drifting costs a little less again.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.47</h3>

  <ul dir="auto">

  <li>Drifting costs less. On an Old 3DS or 2DS the skid marks behind the car took
  more of every frame the longer a drift went on. A race with a lot of drifting runs
  about a twentieth faster.</li>

  <li>The title screen and the garage run faster on an Old 3DS or 2DS, by about a
  tenth of the work in each frame. They also no longer slow down, for minutes at times,
  while a drifting rival waits out of sight for a bend to slide through.</li>

  <li>tougelike.log on the SD card now says where the longest frames went, so the
  next log can explain the stutter that this one could only count.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.46</h3>

  <ul dir="auto">

  <li>The garage flickered. Stretches of the guard rail with its posts, the striped
  barriers, and trees and bushes beside the road dropped out of the picture and snapped
  back about once a second, and whatever stands behind them showed through. It showed
  most on an Old 3DS or 2DS. They stay in the picture now.</li>

  <li>The road and the ground at the far end of the garage''s view, in the top left
  corner of the screen, were missing. They are drawn now.</li>

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

  <td>49.5 MB</td>

  <td><code class="notranslate">011515087335b9c5f2274f06715300abc320fe6756408665c5474cbc5977a346</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3dsx</code></td>

  <td>Homebrew Launcher</td>

  <td>49.3 MB</td>

  <td><code class="notranslate">87cfebdc714a72c84d078bf18087b0e95f12f7454d20d11af6af4bd1090fd922</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3ds</code></td>

  <td>Emulators such as Azahar</td>

  <td>49.5 MB</td>

  <td><code class="notranslate">096d80de36efa60a09f7005d6fcd4953d6685542787f58668e37b9e4ce80b6e4</code></td>

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

  <li>A New 3DS aims for 60 fps and shows each frame as soon as it is ready where
  it cannot hold that. An Old 3DS or 2DS aims for 30 and runs at 14 to 30, slowest
  late in a long run. The speed-ups since 3DS 00.01.37 are still experimental.</li>

  </ul>

  <h2 dir="auto">Feedback</h2>

  <p dir="auto">Found a bug or have an idea? The game''s page, <a href="https://njlent.de/games/tougelike/"
  rel="nofollow">njlent.de/games/tougelike</a>, links the Discord, and GitHub takes
  <a href="https://github.com/njlent/tougelike-3ds-pub/issues">issues</a>. The title
  screen shows both addresses.</p>

  <h2 dir="auto">Version</h2>

  <p dir="auto">3DS 00.01.53, built on Tougelike 00.22.41 (upstream commit <code class="notranslate">16b4edf</code>).
  Full history: <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.53/CHANGELOG.md">CHANGELOG.md</a>.</p>

  <p dir="auto">Tougelike by Noel Justin Lent (njlent). Copying or sharing this build
  needs the author''s permission, so link to this page instead. The licence is in
  <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.53/LICENSE">LICENSE</a>
  and in the game under LICENCE.</p>'
updated: '2026-11-14T00:36:50Z'
version: v0.1.53
version_title: Tougelike for Nintendo 3DS 00.01.53
---
Tougelike is a night racing roguelike set on Japanese mountain roads. Navigate through challenging terrain, avoid obstacles, and survive the night in this fast-paced adventure.

More info on [github](https://github.com/njlent/tougelike-3ds-pub).