---
author: zoeyjodon
avatar: https://avatars.githubusercontent.com/u/76182954?v=4
categories:
- utility
color: '#91959a'
color_bg: '#787b80'
created: '2023-10-17T20:37:53Z'
description: Gamestream client for the New 3DS
download_page: https://github.com/zoeyjodon/moonlight-N3DS/releases
downloads:
  moonlight.3dsx:
    size: 7521072
    size_str: 7 MiB
    url: https://github.com/zoeyjodon/moonlight-N3DS/releases/download/v3.0.0/moonlight.3dsx
  moonlight.cia:
    size: 4166592
    size_str: 3 MiB
    url: https://github.com/zoeyjodon/moonlight-N3DS/releases/download/v3.0.0/moonlight.cia
github: zoeyjodon/moonlight-N3DS
icon: https://raw.githubusercontent.com/zoeyjodon/moonlight-N3DS/n3ds-main/3ds/res/ic_moonlight.png
image: https://raw.githubusercontent.com/zoeyjodon/moonlight-N3DS/n3ds-main/3ds/res/banner.png
image_length: 7154
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  moonlight.cia: https://db.universal-team.net/assets/images/qr/moonlight-cia.png
source: https://github.com/zoeyjodon/moonlight-N3DS
stars: 256
systems:
- 3DS
title: Moonlight Streaming Client
unique_ids:
- '0x3600'
update_notes: '<h2 dir="auto">Changelog</h2>

  <h3 dir="auto">New Features</h3>

  <ul dir="auto">

  <li>Replaces touchscreen previous/next buttons, exit stream keybind, display type,
  and debug settings with an in-stream menu accessible through the HOME button.</li>

  <li>Adds display option for showing magnified images on the bottom screen to make
  small text more readable</li>

  <li>Adds the ability to specify host port when setting up a new address</li>

  <li>Adds logic to allow users to exit the app while streaming is active</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Fix host reconnection issues caused by private key deinitialization</li>

  <li>Fix hanging when trying to connect to a nonexistent/unresponsive host</li>

  <li>Fixes crashes caused by the video stream derefing NULL pointers</li>

  <li>Updates common libraries to ensure connection logic is up-to-date</li>

  </ul>

  <h3 dir="auto">Code changes</h3>

  <ul dir="auto">

  <li>Updates moonlight-common-c</li>

  <li>Pulls in upstream changes</li>

  <li>Use mvd buffer calculation and downscaling for larger image sizes (can now stream
  720p comfortably @ 30fps)</li>

  <li>Various improvements to code clarity and readability</li>

  <li>Adds messaging system to alert components to events without requiring extraneous
  knowledge of other components</li>

  <li>Removes unused driver and config definitions</li>

  <li>Add a 10s timeout to HTTP operations</li>

  <li>Move all display updating logic to the renderer/video decoder</li>

  <li>Adds mutex system for managing shared resources across threads</li>

  <li>Improve directory naming for clarity</li>

  <li>Use the GSP wait to improve control and dispatch loop responsiveness</li>

  <li>Adds a "mock video decoder" implementation</li>

  <li>Makes the config files C++</li>

  <li>Replaces "hwdecode" with a video_decoder option</li>

  </ul>

  <h2 dir="auto">CIA Download</h2>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/39947d57-e963-4cb3-8339-1c69fee27f0e"><img
  width="300" height="300" alt="frame" src="https://github.com/user-attachments/assets/39947d57-e963-4cb3-8339-1c69fee27f0e"
  style="max-width: 100%; height: auto; max-height: 300px;"></a>'
updated: '2026-03-16T17:58:53Z'
version: v3.0.0
version_title: Moonlight 3DS v3.0.0
website: https://github.com/moonlight-stream/moonlight-embedded/wiki
---
Moonlight is an open source client for Sunshine and NVIDIA GameStream for the New Nintendo 3DS, forked from Moonlight Embedded. Moonlight allows you to stream your full collection of games and applications from your PC to other devices to play them remotely.