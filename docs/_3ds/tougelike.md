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
    size: 52254800
    size_str: 49 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.67/tougelike.3dsx
  tougelike.cia:
    size: 52474816
    size_str: 50 MiB
    url: https://github.com/njlent/tougelike-3ds-pub/releases/download/v0.1.67/tougelike.cia
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
stars: 21
systems:
- 3DS
title: Tougelike
unique_ids:
- '0xF7A3C'
update_notes: '<p dir="auto"><strong>Tougelike for Nintendo 3DS</strong> is the night
  racing roguelike on Japanese mountain roads, ported from the web game to the 3DS
  and 2DS. Race down touge passes in the dark, drift through the bends, weave through
  traffic, take down rivals and bosses, and build every run from module drafts. It
  runs on the Old 3DS, 2DS and New 3DS, 2DS. - <a href="https://tougelike.com" rel="nofollow">tougelike.com</a></p>

  <h2 dir="auto">What''s new</h2>

  <h3 dir="auto">Summary since 3DS 00.01.57</h3>

  <ul dir="auto">

  <li>About 8% more steps a second on a n3DS/n2DS: SMOOTH FRAMES now starts off (adds
  ~4 fps).</li>

  <li>Shorter stalls. Late in a long run the longest one went from 1.3 seconds to
  0.4 at o3DS speed, and getting a long-played save ready to write from 1.2 seconds
  to under 0.4.</li>

  <li>Fixed: running out of memory with a long-played save in OPTIONS, SAVE and in
  the garage.</li>

  <li>Fixed: a o3DS stalling every 600 frames while the game wrote its log.</li>

  <li>Drafts, route choices and part offers show your CONDITION, so you can judge
  a repair before you pick.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.67</h3>

  <ul dir="auto">

  <li>Drafts, route choices and part offers show your CONDITION at the top right,
  beside your chips, so you can see how much a repair would help before you pick.</li>

  <li>SPOOL''s multiplier is boost blue, as in the web game.</li>

  <li>The combo''s timer bar sits clear below its number instead of touching it, and
  the HAIRPIN warning under it moved down to make room.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.66</h3>

  <ul dir="auto">

  <li>Leaving the garage with a long-played save could run out of memory. When memory
  is short, the game now clears it up before it saves, which on an o3DS adds about
  half a second to the save.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.65</h3>

  <ul dir="auto">

  <li>SMOOTH FRAMES now starts off on a n3DS/n2DS, where its extra pictures cost the
  game more steps than they add pictures. A choice you make in OPTIONS, VISUAL is
  kept, and an o3DS/o2DS keeps it on unless you had turned it off.</li>

  <li>The CIA''s version, as FBI shows it, is now 2.1.0. The old numbering stopped
  at 1.63.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.63</h3>

  <ul dir="auto">

  <li>Saving stops the game for much less time with a long-played save. at o3DS speed,
  getting a save of about 250 runs ready to write went from 1.2 seconds to under 0.4,
  every time the game saves. Writing it to the SD card takes as long as before.</li>

  <li>The garage menu keeps responding while it brings in the car you stopped on.
  at o3DS speed its slowest frames went from 0.3 seconds to about 0.1, and the car
  arrives just as soon. Loading behind prompts and the results screen works the same
  way now.</li>

  <li>A new draft, route or part offer shows up before the game cleans up memory,
  not after. The cleanup comes right after it appears, while the prompt usually doesn''t
  take a pick yet.</li>

  <li>tougelike.log''s upkeep line counts the saves and how long the longest took
  to get ready and to write. A test build installed as a CIA also times another way
  of getting memory ready for the graphics chip.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.62</h3>

  <ul dir="auto">

  <li>o3DS''s log showed the game stopping for about a fifth of a second every 600
  frames, while it wrote tougelike.log to the SD card. The log now has a writer of
  its own, and the game no longer waits for it.</li>

  <li>Drafts, routes and part offers clean up memory much less often. A cleanup takes
  about 0.4 seconds at o3DS speed and holds up the cursor, and they used to do one
  every time they opened or changed.</li>

  <li>tougelike.log adds a line under each row with the free memory, the cleanups
  and the log''s own writing.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.61</h3>

  <ul dir="auto">

  <li>Scrolling the garage''s car list no longer loads every car you pass. The top
  screen brings in the car the cursor stops on, or right away when you press A or
  change tab.</li>

  <li>The garage saves once, when you leave it, instead of after every upgrade, perk
  or paint change. With a long-played save each of those saves froze the garage for
  1.7 seconds in an emulator running at o3DS speed.</li>

  <li>With a long-played save, OPTIONS, SAVE could run out of memory and stop the
  game, on opening or on EXPORT TO SD and IMPORT FROM SD. It now needs much less memory,
  and the screen says what it is doing while it works.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.60</h3>

  <ul dir="auto">

  <li>On an o3DS each step of the game should take a little less time. How much it
  saves on a real console is not measured yet.</li>

  <li>BENCHMARK''s census, and the measurements a test build takes at start, write
  more figures on copying and flushing memory to tougelike.log.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.59</h3>

  <ul dir="auto">

  <li>Headlights and lamps cost the graphics chip less. A corner outside a light''s
  beam or reach now skips that light''s sums, which in a late race is four in five
  of them, and the picture stays exactly the same.</li>

  <li>BENCHMARK adds a short census after its timed run. It draws pictures with one
  part of the work left out at a time, so they look wrong for a few seconds, and writes
  what each part costs to tougelike.log.</li>

  </ul>

  <h3 dir="auto">3DS 00.01.58</h3>

  <ul dir="auto">

  <li>The test drive list, which the web game''s secret code opens on the title screen,
  now starts with BENCHMARK. It drives the same late-game descent every time and shows
  how fast your console ran it, on screen and in tougelike.log, and your save stays
  as it was.</li>

  <li>Holding SELECT while the game starts measures the console''s graphics chip and
  second core and writes the figures to tougelike.log.</li>

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

  <td>50.0 MB</td>

  <td><code class="notranslate">2b6ad9f90a88df730cee839a1a4d38ccbfae74a7fd14f1d91e4e9acb0a9d62fb</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3dsx</code></td>

  <td>Homebrew Launcher</td>

  <td>49.8 MB</td>

  <td><code class="notranslate">5b88fe7a025f47b083011160822295fd7cceb93e427a113c1453b4be455182c3</code></td>

  </tr>

  <tr>

  <td><code class="notranslate">tougelike.3ds</code></td>

  <td>Emulators such as Azahar</td>

  <td>50.0 MB</td>

  <td><code class="notranslate">249acec26b64a0114ced0b78102902f9ea4f0df5bbf5fac8d6b70a8a91cd32aa</code></td>

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

  <li>A Nintendo o3DS/o2DS or n3DS/n2DS with custom firmware (Luma3DS) to run homebrew.</li>

  <li>For sound, a DSP firmware dump at <code class="notranslate">sdmc:/3ds/dspfirm.cdc</code>,
  made once with DSP1.</li>

  <li>About 60 MB free on the SD card.</li>

  <li>A New 3DS aims for 60 fps and an o3DS/o2DS for 30. Between two steps of the
  game the console draws the last one again from where the camera will be (OPTIONS,
  VISUAL, SMOOTH FRAMES, which starts off on a n3DS), so the screen shows more pictures
  than the game takes steps. The speed-ups are still experimental.</li>

  </ul>

  <h2 dir="auto">Feedback</h2>

  <p dir="auto">Found a bug or have an idea? The game''s page, <a href="https://njlent.de/games/tougelike/"
  rel="nofollow">njlent.de/games/tougelike</a>, links the Discord, and GitHub takes
  <a href="https://github.com/njlent/tougelike-3ds-pub/issues">issues</a>. The title
  screen shows both addresses.</p>

  <h2 dir="auto">Version</h2>

  <p dir="auto">3DS 00.01.67, built on Tougelike 00.22.41 (upstream commit <code class="notranslate">16b4edf</code>).
  Full history: <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.67/CHANGELOG.md">CHANGELOG.md</a>.</p>

  <p dir="auto">Tougelike by Noel Justin Lent (njlent). Copying or sharing this build
  needs the author''s permission, so link to this page instead. The licence is in
  <a href="https://github.com/njlent/tougelike-3ds-pub/blob/v0.1.67/LICENSE">LICENSE</a>
  and in the game under LICENCE.</p>'
updated: '2026-11-19T23:09:17Z'
version: v0.1.67
version_title: Tougelike for Nintendo 3DS 00.01.67
---
Tougelike is a night racing roguelike set on Japanese mountain roads. Navigate through challenging terrain, avoid obstacles, and survive the night in this fast-paced adventure.

More info on [github](https://github.com/njlent/tougelike-3ds-pub).