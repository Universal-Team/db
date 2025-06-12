---
author: FlagBrew
avatar: https://avatars.githubusercontent.com/u/42673825?v=4
categories:
- utility
color: '#749285'
color_bg: '#658074'
created: '2016-05-15T08:26:47Z'
description: Gen I to GenVIII save manager.
download_page: https://github.com/FlagBrew/PKSM/releases
downloads:
  PKSM.3dsx:
    size: 7478460
    size_str: 7 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.2.2/PKSM.3dsx
  PKSM.cia:
    size: 6218688
    size_str: 5 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.2.2/PKSM.cia
github: FlagBrew/PKSM
icon: https://raw.githubusercontent.com/FlagBrew/PKSM/master/assets/icon.png
image: https://raw.githubusercontent.com/FlagBrew/PKSM/master/assets/banner.png
image_length: 8070
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  PKSM.cia: https://db.universal-team.net/assets/images/qr/pksm-cia.png
source: https://github.com/FlagBrew/PKSM
stars: 1934
systems:
- 3DS
title: PKSM
unique_ids:
- '0xEC100'
update_notes: '<h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li>Added: logging. Now PKSM is able to fully log the startup and title loading
  process (both on screen, in memory and on file) in order to improve the debugging
  of existing and future issues.

  <ul dir="auto">

  <li>Logs are accessible in files located in <code class="notranslate">/3ds/PKSM/logs</code>,
  which are split by day.</li>

  <li>Logs are also accessible at runtime through an integrated HTTP server at the
  following addresses:

  <ul dir="auto">

  <li><code class="notranslate">http://3ds-ip-address:8000/logs/memory</code> for
  the logs of PKSM''s current run</li>

  <li><code class="notranslate">http://3ds-ip-address:8000/logs/file</code> for all
  the logs for the current date</li>

  </ul>

  </li>

  <li>The console IP address is shown on the bottom screen at startup.</li>

  </ul>

  </li>

  <li>Added: more informative debug screen on startup, where one can see what PKSM
  is currently doing. This will help debugging for people having startup freeze issues.</li>

  <li>Added: shiny/egg indicator in the wondercard injection screen.</li>

  <li>Fixed: optimized sound initialization if there''s no background music to run.
  Now sound initialization is entirely skipped if unnecessary, making PKSM loading
  faster and with less resources needed.

  <ul dir="auto">

  <li>This also fixes a startup freeze issue related to sound loading.</li>

  </ul>

  </li>

  <li>Fixed: long standing memory leak in the wondercard selection screen causing
  random crashes.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <hr>

  <p dir="auto"></p>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4fd6621149dd39281a0da7c2c9d80ad1408edca0c82a0153a1d7df9ea37c7e11/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2025-03-22T13:51:28Z'
version: 10.2.2
version_title: PKSM 10.2.2
wiki: https://github.com/FlagBrew/PKSM/wiki
---
