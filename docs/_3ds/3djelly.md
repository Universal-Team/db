---
author: 8 Bit Studio
avatar: https://avatars.githubusercontent.com/u/256004323?v=4
categories:
- app
color: '#2e3746'
color_bg: '#2e3746'
created: '2026-03-03T02:38:59Z'
description: A Jellyfin client for Nintendo 3DS.
download_filter: \.3dsx$|\.cia$
download_page: https://github.com/8-bitStudio/3d-jelly/releases
downloads:
  3dJelly.3dsx:
    size: 400044
    size_str: 390 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.4.0/3dJelly.3dsx
  3dJelly.cia:
    size: 300992
    size_str: 293 KiB
    url: https://github.com/8-bitStudio/3d-jelly/releases/download/v0.4.0/3dJelly.cia
github: 8-bitStudio/3d-jelly
icon: https://raw.githubusercontent.com/8-bitStudio/3d-jelly/main/gfx/icon.png
image: https://raw.githubusercontent.com/8-bitStudio/3d-jelly/main/gfx/icon.png
image_length: 4191
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
llm_usage: undisclosed
qr:
  3dJelly.cia: https://db.universal-team.net/assets/images/qr/3djelly-cia.png
source: https://github.com/8-bitStudio/3d-jelly
stars: 1
systems:
- 3DS
title: 3dJelly
unique_ids:
- '0xD7E11'
update_notes: '<h2 dir="auto">Added</h2>

  <ul dir="auto">

  <li>Added a Settings screen opened with Y from browsing screens.</li>

  <li>Added settings for default quality, playback mode, stream buffer preference,
  server URL, and username.</li>

  <li>Added actions to clear saved login data, reset server/user data, and reset playback
  defaults.</li>

  <li>Added configurable audio sample rates for 240p and 240HQ playback.</li>

  <li>Added automatic next-episode playback when an episode ends.</li>

  <li>Added a top-screen next-episode countdown with A to play next immediately and
  B to cancel.</li>

  <li>Added English, Spanish, and Japanese language support.</li>

  <li>Added a stacked language selector with native labels: English, Español, and
  日本語.</li>

  </ul>

  <h2 dir="auto">Changed</h2>

  <ul dir="auto">

  <li>Moved Setup access on the Libraries screen to B.</li>

  <li>Changed the Language setting from inline cycling to a selector menu.</li>

  <li>Removed the experimental 240M1 quality mode from user-selectable settings.</li>

  <li>Kept 144p audio at 22050 Hz while allowing higher audio rates for 240p and 240HQ.</li>

  </ul>

  <h2 dir="auto">Fixed</h2>

  <ul dir="auto">

  <li>Fixed episodes replaying the last few seconds after reaching the end.</li>

  <li>Fixed near-end MJPEG/H.264 stream closes being treated as reconnects.</li>

  <li>Fix login redirects for public Jellyfin servers <a href="https://github.com/8-bitStudio/3d-jelly/issues/7"
  data-hovercard-type="issue" data-hovercard-url="/8-bitStudio/3d-jelly/issues/7/hovercard">Issue
  #7</a>, by <a href="https://github.com/ClammyMantis488">@ClammyMantis488</a></li>

  <li>Fixed the language selector drawing behind Settings text.</li>

  <li>Fixed Japanese playback status badges not recognizing Japanese loading, error,
  and stopped states.</li>

  </ul>

  <h2 dir="auto">Notes</h2>

  <ul dir="auto">

  <li>Japanese support is new and should be considered early. Please report any text
  that does not fit or any translation issues.</li>

  <li>Playback is still experimental, especially at higher quality settings on Old
  3DS.</li>

  </ul>'
updated: '2026-06-05T15:02:04Z'
version: v0.4.0
version_title: 3dJelly v0.4.0
---
3dJelly is a Jellyfin client for Nintendo 3DS. It can connect to a Jellyfin server, browse libraries, and play video through server-side transcoding.

Features:
- Native 3DS interface inspired by Jellyfin.
- CIA and 3DSX builds.
- Server-side transcoding with 144p, 240p, 360p, and 480p targets.
- In-playback quality switching.
- Audio playback, mute, and volume controls.

Notes:
- 144p and 240p are recommended for Old 3DS.
- 360p and 480p may be slow depending on hardware, emulator, server speed, and media.