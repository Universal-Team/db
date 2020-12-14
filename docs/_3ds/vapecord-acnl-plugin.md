---
author: RedShyGuy
categories:
- utility
color: '#947677'
created: '2019-08-22T07:15:13Z'
description: Animal Crossing NL Vapecord Public Plugin WIP
download_page: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/tag/v1.8.2
downloads:
  Vapecord.Public.zip:
    size: 5120792
    url: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/download/v1.8.2/Vapecord.Public.zip
github: RedShyGuy/Vapecord-ACNL-Plugin
image: https://avatars1.githubusercontent.com/u/43783060?v=4
layout: app
scripts:
  For ACNL EUR:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086400/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086400/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL JPN:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086200/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086200/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL KOR:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086500/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086500/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL USA:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086300/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086300/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL WA EUR:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198f00/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000198f00/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL WA JPN:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198d00/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000198d00/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL WA USA:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198e00/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000198e00/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL Welcome Luxury:
  - file: Vapecord.Luxury.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/00040000004C5700/
    message: Extracting Vapecord...
    output: /luma/plugins/00040000004C5700/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
source: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin
systems:
- 3DS
title: Vapecord-ACNL-Plugin
update_notes: '<h1>New Update!!</h1>

  <p>Here a new update!! It adds a lot of stuff and changes!</p>

  <h2>The update has those features:</h2>

  <blockquote>

  <p>House Interior/Exterior Editor<br>

  Turnip Price Changer<br>

  Enable/Disable Cheats Overhaul<br>

  A lot of performance changes<br>

  Added Standard Plugin Color Editor (see FWKColors.txt)<br>

  Updated to CTRPF v0.6.0 Alpha<br>

  Plugin now uses Luma v10.2.1<br>

  and more!</p>

  </blockquote>

  <h2>There are also some bug fixes:</h2>

  <blockquote>

  <p>Catalog To Pockets and other minor related bugs should be fixed<br>

  Fixed not being able to drop at watered position (or in general at empty space with
  flag)<br>

  Map Editor Particles missing<br>

  Take TPC Pic should be crash free now<br>

  and more!</p>

  </blockquote>

  <h2>How to use:</h2>

  <p>You can find a guide about the installation <a href="https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/wiki/How-to-install">here</a>.<br>

  If you encounter any bugs feel free to report them on the official <a href="https://discord.gg/w9nvqjW"
  rel="nofollow">Vapecord Discord Server</a>.</p>'
updated: '2020-12-03T22:03:11Z'
version: v1.8.2
version_title: ACNL Vapecord Public Plugin [v.1.8.2]
wiki: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/wiki
---
