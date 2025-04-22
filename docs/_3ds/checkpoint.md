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
    size: 1444892
    size_str: 1 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.10.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 1020864
    size_str: 996 KiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.10.0/Checkpoint.cia
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
stars: 2684
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<p dir="auto">This release focuses on adding performance improvements
  to the 3DS version of the software.</p>

  <h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li><strong>Fixed: startup time has been drastically improved: ~50% speedup on uncached
  boot, ~90% speedup on cached boot.</strong>

  <ul dir="auto">

  <li>This has been achieved by profiling the application boot process, and realizing
  that title cache persistence on the SD card took majority of the loading time. Now
  this operation is lazily done in a separate thread. It''s funny to realize that
  a badly implemented optimization can become a bottleneck of its own, so take my
  mistake as a lesson.</li>

  <li>Here''s the improvements I had on my console (improvements may vary since they
  depend on how many games you have on your console):

  <ul dir="auto">

  <li>Uncached startup went down from 9.8s to 5.7s</li>

  <li>Cached startup went down from 5.7s to 0.6s</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><strong>Added: due to requests from multiple users, Checkpoint can now be updated
  from Universal Updater.</strong></li>

  <li>Fixed: cartridge loading now runs immediately rather than waiting for the title
  cache to be persisted on the SD card.</li>

  <li>Fixed: properly quit the application gracefully when an handled exception occurs.</li>

  <li>Fixed: initial code refactoring.</li>

  <li>Removed: some redundant logs in the title loader.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <p dir="auto">Thank you for your patience and support.</p>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <p dir="auto"></p>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4fd6621149dd39281a0da7c2c9d80ad1408edca0c82a0153a1d7df9ea37c7e11/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2025-04-19T08:50:26Z'
version: v3.10.0
version_title: Checkpoint 3.10.0
---
