---
author: SprtnDio
avatar: https://avatars.githubusercontent.com/u/183821772?v=4
categories:
- utility
color: '#444637'
color_bg: '#444637'
created: '2026-03-13T00:19:39Z'
description: Drawing and text Chat Rooms.
download_page: https://github.com/SprtnDio/NoteRoom/releases
downloads:
  NoteRoom.3dsx:
    size: 840436
    size_str: 820 KiB
    url: https://github.com/SprtnDio/NoteRoom/releases/download/v2.5.0/NoteRoom.3dsx
  NoteRoom.cia:
    size: 1318336
    size_str: 1 MiB
    url: https://github.com/SprtnDio/NoteRoom/releases/download/v2.5.0/NoteRoom.cia
github: SprtnDio/NoteRoom
icon: https://raw.githubusercontent.com/SprtnDio/NoteRoom/main/icon.png
image: https://raw.githubusercontent.com/SprtnDio/NoteRoom/refs/heads/main/banner.png
image_length: 37065
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: generation
qr:
  NoteRoom.cia: https://db.universal-team.net/assets/images/qr/noteroom-cia.png
source: https://github.com/SprtnDio/NoteRoom
stars: 3
systems:
- 3DS
title: NoteRoom
unique_ids:
- '0xF9E3'
update_notes: '<h1 dir="auto">NoteRoom v2.5 - The Music Update 🎵🎨</h1>

  <p dir="auto">Welcome to NoteRoom v2.5! This update brings a highly requested feature
  to the table, alongside smart UI improvements and crucial stability fixes to make
  your drawing and chatting experience smoother than ever.</p>

  <h2 dir="auto">🎵 New Feature: Background Music Player</h2>

  <ul dir="auto">

  <li><strong>MP3 Support:</strong> NoteRoom now supports background music! Simply
  place your favorite <code class="notranslate">.mp3</code> files into <code class="notranslate">SD:/3ds/NoteRoom/</code>
  and they will play automatically while you chat and draw.</li>

  <li><strong>Now Playing Notifications:</strong> Whenever a new track starts, a neat
  little <code class="notranslate">🎵 [Song Name]</code> banner pops up on the top
  screen.</li>

  <li><strong>Quick Skip Controls:</strong> You can now skip songs directly using
  the <strong>Circle Pad (Thumbstick)</strong>!

  <ul dir="auto">

  <li>Flick <strong>Right</strong> to skip to the next track.</li>

  <li>Flick <strong>Left</strong> to play the previous track.</li>

  <li><em>Includes a built-in deadzone to prevent accidental double-skips!</em></li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">✨ UI &amp; Quality of Life Improvements</h2>

  <ul dir="auto">

  <li><strong>Combined PEN &amp; ERS Button:</strong> To save space on the bottom
  screen, the Pen (<code class="notranslate">PEN</code>) and Eraser (<code class="notranslate">ERS</code>)
  tools have been merged into a single toggle button. Simply tap it to switch between
  drawing and erasing.</li>

  <li><strong>In-Chat Quick Help:</strong> A new <code class="notranslate">HELP</code>
  button has been added to the bottom toolbar (replacing the old eraser slot). You
  can now open the <em>Help &amp; Controls</em> screen directly while in a chat room,
  without having to leave or lose your connection!</li>

  <li><strong>Start Screen Update:</strong> The lock screen/rules screen now reminds
  users where to put their <code class="notranslate">.mp3</code> files and includes
  a custom text line to welcome users.</li>

  <li><strong>Updated Help Section:</strong> The Help &amp; Controls overlay has been
  updated to explain the new music player features and Circle Pad controls.</li>

  </ul>

  <h2 dir="auto">🚀 Performance &amp; Under the Hood</h2>

  <ul dir="auto">

  <li><strong>Zero-Freeze Sending (Async):</strong> Sending text messages and drawings
  is now lightning fast! The app immediately queues the message in the background
  and showsa smooth 4-second "Encrypting message..." -&gt; "Sent!" animation without
  freezing the UI.</li>

  <li><strong>Faster Lobby Updates:</strong> The online user and room polling rate
  in the menus has been cut in half (from 5000ms to 2500ms). You''ll now see people
  joining and leaving lobbies almost instantly!</li>

  <li><strong>CRITICAL FIX - Safe Shutdown:</strong> Fixed a nasty crash that could
  occur when exiting the app with <code class="notranslate">[START]</code>. The audio
  thread (DSP/mpg123) is now forcefully and safely terminated before the 3DS closes
  the sound channels, eliminating memory corruption crashes on exit.</li>

  <li><strong>Certificate Pinning &amp; Security:</strong> Further hardening of the
  manual TLS Certificate Pinning to ensure maximum MITM-protection.</li>

  </ul>

  <hr>

  <h3 dir="auto">📂 How to use the Music Player:</h3>

  <ol dir="auto">

  <li>Make sure your SD card has the folder <code class="notranslate">sdmc:/3ds/NoteRoom/</code>
  (The app creates this automatically).</li>

  <li>Drop up to 30 of your favorite <code class="notranslate">.mp3</code> songs into
  this folder.</li>

  <li>Launch NoteRoom and enjoy! Use the Circle Pad (Left/Right) to change tracks
  at any time.</li>

  </ol>'
updated: '2026-06-04T12:32:06Z'
version: v2.5.0
version_title: NoteRoom v2.5 - The BGM Update
---
NoteRoom is a real-time online drawing and text Chatroom messenger for the Nintendo 2/3DS, inspired by a well known chatroom. Connect globally across themed, dynamic lobbies, share hand-drawn doodles, and view live user counts.