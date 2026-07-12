---
author: Oldhimaster1
avatar: https://avatars.githubusercontent.com/u/179153474?v=4
categories:
- app
- media
color: '#294c7a'
color_bg: '#294c7a'
created: '2026-06-27T23:27:59Z'
description: A custom MIVF video player for Nintendo 3DS with lots of features.
download_filter: ^mivf_player_3ds\.(cia|3dsx)$
download_page: https://github.com/Oldhimaster1/MIVF/releases
downloads:
  mivf_player_3ds.3dsx:
    size: 346704
    size_str: 338 KiB
    url: https://github.com/Oldhimaster1/MIVF/releases/download/v2026.07.09/mivf_player_3ds.3dsx
  mivf_player_3ds.cia:
    size: 412096
    size_str: 402 KiB
    url: https://github.com/Oldhimaster1/MIVF/releases/download/v2026.07.09/mivf_player_3ds.cia
github: Oldhimaster1/MIVF
icon: https://raw.githubusercontent.com/Oldhimaster1/MIVF/refs/heads/main/meta/icon48.png
image: https://raw.githubusercontent.com/Oldhimaster1/MIVF/refs/heads/main/meta/banner.png
image_length: 4907
layout: app
license: mit
license_name: MIT License
llm_generation: minor
preinstall_message: Place encoded .mivf videos in sdmc:/mivf/ or sdmc:/3ds/mivf_player_3ds/.
  PC video encoding requires the separate encode_mivf tool from the GitHub release.
qr:
  mivf_player_3ds.cia: https://db.universal-team.net/assets/images/qr/mivf_player_3ds-cia.png
source: https://github.com/Oldhimaster1/MIVF
stars: 2
systems:
- 3DS
title: MIVF Player
unique_ids:
- '0xF8002'
update_notes: '<h2 dir="auto">Highlights</h2>

  <ul dir="auto">

  <li>Added an in-app controls/keybinds help screen.</li>

  <li>Added experimental <code class="notranslate">--motion-search hybrid</code> encoder
  mode.</li>

  <li>Hardened M2Y1/M2Y2 payload-size validation against malformed or corrupted files.</li>

  <li>Added HOME/exit and startup lifecycle diagnostics.</li>

  <li>Updated README with real screenshots, benchmark charts, and MoFlex-vs-MIVF comparison
  notes.</li>

  <li>Documented encoder options, warm-start chunks, packet diagnostics, and release
  packaging requirements.</li>

  </ul>

  <h2 dir="auto">Player changes</h2>

  <ul dir="auto">

  <li>Added the controls help screen, available from the browser with X or from Settings
  -&gt; CONTROLS during playback.</li>

  <li>Hardened M2Y1/M2Y2 decode validation so malformed plane payload sizes are rejected
  safely.</li>

  <li>Added lifecycle/startup diagnostics for investigating HOME/exit behavior and
  startup/browser scan timing.</li>

  </ul>

  <h2 dir="auto">Encoder changes</h2>

  <ul dir="auto">

  <li>Added experimental <code class="notranslate">--motion-search hybrid</code>.</li>

  <li>Existing <code class="notranslate">full</code>, <code class="notranslate">diamond</code>,
  and <code class="notranslate">fast</code> motion-search modes remain available.</li>

  <li>Added/updated documentation for <code class="notranslate">--warm-start-chunks</code>,
  <code class="notranslate">--max-video-packet-kb</code>, <code class="notranslate">--report-packet-sizes</code>,
  and packaged encoder builds.</li>

  <li>Windows and Linux encoder packages include bundled helper binaries.</li>

  </ul>

  <h2 dir="auto">Packaged encoder usage</h2>

  <p dir="auto">Windows:</p>

  <pre lang="text" class="notranslate"><code class="notranslate">encode_mivf.exe input.mp4
  output.mivf --m2y2

  encode_mivf.exe input.mp4 output.mivf --m2y2 --motion-search hybrid

  encode_mivf.exe input.mp4 output.mivf --m2y2 --motion-search hybrid --warm-start-chunks

  encode_mivf.exe input.mp4 output.mivf --m2y2 --profile 3ds-fast

  </code></pre>

  <p dir="auto">Linux:</p>

  <pre lang="text" class="notranslate"><code class="notranslate">./encode_mivf.sh
  input.mp4 output.mivf --m2y2

  ./encode_mivf.sh input.mp4 output.mivf --m2y2 --motion-search hybrid --warm-start-chunks

  </code></pre>

  <h2 dir="auto">Notes</h2>

  <ul dir="auto">

  <li><code class="notranslate">--motion-search hybrid</code> is experimental. Use
  <code class="notranslate">--report-packet-sizes</code> and compare output before
  relying on it for a final encode.</li>

  <li><code class="notranslate">--warm-start-chunks</code> is experimental and serializes
  chunk encoding, but helps avoid repeated forced chunk-boundary keyframes.</li>

  <li>The Windows encoder package should be distributed as the whole <code class="notranslate">encode_mivf/</code>
  folder, not just <code class="notranslate">encode_mivf.exe</code>.</li>

  <li>The Linux encoder package should be launched through <code class="notranslate">encode_mivf.sh</code>.</li>

  <li>A macOS encoder package may be added later.</li>

  </ul>

  <h2 dir="auto">Assets</h2>

  <p dir="auto">This release includes:</p>

  <ul dir="auto">

  <li><code class="notranslate">mivf_player_3ds.3dsx</code></li>

  <li><code class="notranslate">mivf_player_3ds.smdh</code></li>

  <li><code class="notranslate">mivf_player_3ds.cia</code></li>

  <li><code class="notranslate">encode_mivf_windows_x86_64.zip</code></li>

  <li><code class="notranslate">encode_mivf_linux_x86_64.tar.gz</code></li>

  </ul>'
updated: '2026-07-09T17:13:05Z'
version: v2026.07.09
version_title: MIVF Player v2026.07.09
---

MIVF Player is a homebrew video player for Nintendo 3DS built around the custom MIVF container format.

It supports custom MIVF video streams plus IA4M audio. The player is designed for real Nintendo 3DS hardware and includes a file browser, playback controls, subtitles, chapters, resume bookmarks, favorites, playlists, aspect-ratio modes, and settings saved on the SD card.

Videos can be converted on PC with the included `encode_mivf` encoder. Encoded `.mivf` files can be placed in `sdmc:/mivf/`, `sdmc:/3ds/mivf_player_3ds/`, or the SD root.

(M2Y2 range coding can reduce file size while preserving the already-encoded video packets losslessly... or in simpler terms.... video is highh quality with very small file size)
