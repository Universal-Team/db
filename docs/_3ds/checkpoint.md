---
author: Bernardo Giordano
avatar: https://avatars.githubusercontent.com/u/17624378?v=4
categories:
- utility
color: '#40576f'
color_bg: '#40576f'
created: '2017-09-06T17:20:55Z'
description: Fast and simple homebrew save manager for 3DS and Switch.
download_page: https://github.com/BernardoGiordano/Checkpoint/releases
downloads:
  Checkpoint.3dsx:
    size: 1444356
    size_str: 1 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.9.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 1024960
    size_str: 1000 KiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.9.0/Checkpoint.cia
github: BernardoGiordano/Checkpoint
icon: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/icon.png
image: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/banner.png
image_length: 5618
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  Checkpoint.cia: https://db.universal-team.net/assets/images/qr/checkpoint-cia.png
source: https://github.com/BernardoGiordano/Checkpoint
stars: 2679
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<p dir="auto">This release mostly  contains changes and patches related
  to the infamous 3.8.x startup crash issue affecting the 3DS version of the software.
  General improvements have been added to the Switch version as well.</p>

  <h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li><strong>Fixed: the startup crash issue affecting all version since 3.8.0 has
  been identified and patched.</strong>

  <ul dir="auto">

  <li>Huge shoutout to achinech on Discord who volunteered to debug the issue on their
  console.</li>

  <li>If you still encounter startup crash issues, please notify the team immediately
  on <a href="https://discord.gg/bGKEyfY" rel="nofollow">Discord</a> and on GitHub
  issues.</li>

  </ul>

  </li>

  <li><strong>Fixed: cartridge scanning has been refactored to be way more efficient.</strong>

  <ul dir="auto">

  <li>Previously, the software used to poll the cartridge synchronously for every
  frame of the UI thread. Cartridge scanning is now happening on a separate thread
  which only runs twice per second.</li>

  </ul>

  </li>

  <li>Added: a more advanced threading framework ported from PKSM.</li>

  <li>Added: networking support and an integrated HTTP server. This is currently used
  to provide real-time online access to the application logs, but this code will be
  useful for future features like self-updating.</li>

  <li>Added: more robust logging ported from PKSM. Logs are stored in the <code class="notranslate">/3ds/Checkpoint/logs</code>
  folder and are split by date.

  <ul dir="auto">

  <li>Logs are also accessible at runtime through the integrated HTTP server at the
  following addresses:

  <ul dir="auto">

  <li><code class="notranslate">http://3ds-ip-address:8000/logs/memory</code> for
  the logs of Checkpoint''s current run</li>

  <li><code class="notranslate">http://3ds-ip-address:8000/logs/file</code> for all
  the logs for the current date</li>

  </ul>

  </li>

  </ul>

  </li>

  <li>Added: compiler optimizations are back. This includes link-time optimization
  and an upgrade from <code class="notranslate">O2</code> to <code class="notranslate">O3</code>
  compared to v.3.7.4.</li>

  <li>Fixed: better configuration file handling ported from PKSM.</li>

  <li>Fixed: better thread synchronization between UI thread and title loading thread.</li>

  <li>Fixed: wrap the entire program into try-catch blocks to prevent crashes caused
  by other unhandled exceptions in the future.</li>

  <li>Fixed: few graphics improvements.</li>

  <li>Fixed: readme has been updated with latest screenshots.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <p dir="auto">The source code has started to become a little bit messy, but this
  patch needed to be released as soon as possible. Future improvements to the software
  will surely focus on code and program cleanup and performance improvements.</p>

  <p dir="auto">Thank you for your patience and support.</p>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <p dir="auto"></p>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4fd6621149dd39281a0da7c2c9d80ad1408edca0c82a0153a1d7df9ea37c7e11/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a>](<a href="https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.9.0/Checkpoint.cia">https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.9.0/Checkpoint.cia</a>)</p>'
updated: '2025-04-13T16:10:29Z'
version: v3.9.0
version_title: Checkpoint 3.9.0
---
