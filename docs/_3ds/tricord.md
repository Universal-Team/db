---
author: 2ipper
avatar: https://avatars.githubusercontent.com/u/119087427?v=4
categories:
- app
color: '#45496a'
color_bg: '#45496a'
created: '2026-02-15T15:59:55Z'
description: Discord client for Nintendo 3DS
download_page: https://github.com/2b-zipper/TriCord/releases
downloads:
  TriCord.cia:
    size: 9106368
    size_str: 8 MiB
    url: https://github.com/2b-zipper/TriCord/releases/download/v0.6.0/TriCord.cia
github: 2b-zipper/TriCord
icon: https://raw.githubusercontent.com/2b-zipper/TriCord/refs/heads/main/resources/icon.png
image: https://raw.githubusercontent.com/2b-zipper/TriCord/refs/heads/main/resources/banner.png
image_length: 3664
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
preinstall_message: This project is developed for educational purposes only. This
  is an unofficial Discord client and is not affiliated with or endorsed by Discord
  Inc. Software is provided "as is", and you use it at your own risk. The developers
  assume no responsibility for any damages, data loss, or Discord ToS violations resulting
  from the use of this software.
qr:
  TriCord.cia: https://db.universal-team.net/assets/images/qr/tricord-cia.png
screenshots:
- description: Chat
  url: https://db.universal-team.net/assets/images/screenshots/tricord/chat.png
- description: Hamburger
  url: https://db.universal-team.net/assets/images/screenshots/tricord/hamburger.png
- description: Login
  url: https://db.universal-team.net/assets/images/screenshots/tricord/login.png
- description: Serverlist
  url: https://db.universal-team.net/assets/images/screenshots/tricord/serverlist.png
source: https://github.com/2b-zipper/TriCord
stars: 131
systems:
- 3DS
title: TriCord
unique_ids:
- '0xD5C0D'
update_notes: '<h1 dir="auto">Huge performance improvements and animated GIF support!</h1>

  <h3 dir="auto">Performance</h3>

  <ul dir="auto">

  <li>Rebuilt the entire networking layer to be lighter and more efficient</li>

  <li>Frames where nothing changed are no longer drawn, and rendering, background
  threads and texture memory have been optimized</li>

  <li>Accounts with hundreds of servers no longer run out of memory</li>

  <li>Custom emoji and avatars load faster, with on-screen emoji fetched first</li>

  <li>QR login key generation is much faster</li>

  <li>Old 3DS uses fewer network workers and caps remote images at 256px, while New
  3DS decodes images and emoji on its extra CPU core</li>

  <li>Voice calls are much lighter: a fixed-point Opus build cuts encoding time by
  about 40% on a real Old 3DS, and echo cancellation has been reworked for the 3DS
  CPU</li>

  </ul>

  <h3 dir="auto">GIFs</h3>

  <ul dir="auto">

  <li>GIFs now play in attachments, stickers and embeds such as Tenor, along with
  animated custom emoji</li>

  <li>GIF embeds are shown without the embed frame or link</li>

  <li>Playback is limited to 30 fps on New 3DS and 15 fps on Old 3DS. GIFs larger
  than 6 MB on New 3DS or 3 MB on Old 3DS are shown as still images</li>

  </ul>

  <h3 dir="auto">Bots</h3>

  <ul dir="auto">

  <li>Added support for buttons, select menus and forms (modals)</li>

  <li>Added support for Components V2 messages and ephemeral messages</li>

  <li>Fixed application command replies not being displayed, and added the "used /command"
  line</li>

  </ul>

  <h3 dir="auto">Voice</h3>

  <ul dir="auto">

  <li>Added a voice panel with per-user volume and microphone sensitivity</li>

  <li>Echo cancellation is now always on for every model, and its setting has been
  removed</li>

  <li>Encryption key changes no longer stall audio</li>

  <li>Reduced latency and echo in voice calls, with better optimization for Nintendo
  2DS, by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Nicolino075/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Nicolino075">@Nicolino075</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="6025658486"
  data-permission-text="Title is private" data-url="https://github.com/2b-zipper/TriCord/issues/63"
  data-hovercard-type="pull_request" data-hovercard-url="/2b-zipper/TriCord/pull/63/hovercard"
  href="https://github.com/2b-zipper/TriCord/pull/63">#63</a></li>

  </ul>

  <h3 dir="auto">Security</h3>

  <ul dir="auto">

  <li>WebSocket connections now verify TLS certificates</li>

  <li>QR login now verifies the public key fingerprint</li>

  <li>Fixed TLS and QR login keys being generated without a proper random source</li>

  <li>Removed the option to disable SSL certificate verification</li>

  </ul>

  <h3 dir="auto">Other changes</h3>

  <ul dir="auto">

  <li>Added a setting to turn off the notification sound</li>

  <li>Added a token login hint to the login screen</li>

  <li>Added a runtime stats overlay (hold R and press L)</li>

  <li>Reactions now appear immediately and are sent in order</li>

  <li>Fixed channels staying unread after leaving them</li>

  <li>Fixed returning to channel selection instead of the server list from menu screens</li>

  <li>Fixed the threads menu item not showing for channels with only archived threads</li>

  <li>Fixed reactions overlapping system messages</li>

  <li>Updated translations</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/2b-zipper/TriCord/compare/v0.5.1...v0.6.0"><tt>v0.5.1...v0.6.0</tt></a></p>'
updated: '2026-11-01T13:41:05Z'
version: v0.6.0
version_title: v0.6.0
---
Please see below for details: https://github.com/2b-zipper/TriCord/blob/main/README.md