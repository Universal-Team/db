---
author: RedShyGuy
categories:
- utility
created: '2019-08-22T07:15:13Z'
description: Animal Crossing NL Vapecord Public Plugin WIP
download_page: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/tag/v1.8.0
downloads:
  Vapecord.Public.zip: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/download/v1.8.0/Vapecord.Public.zip
github: RedShyGuy/Vapecord-ACNL-Plugin
image: https://avatars1.githubusercontent.com/u/43783060?v=4
layout: app
scripts:
  ACNL Welcome Luxury:
  - file: Vapecord.Luxury.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/00040000004C5700/
    message: Extracting... please wait.
    output: /luma/plugins/00040000004C5700/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL EUR:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086400/
    message: Extracting... please wait.
    output: /luma/plugins/0004000000086400/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL JPN:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086200/
    message: Extracting... please wait.
    output: /luma/plugins/0004000000086200/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL KOR:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086500/
    message: Extracting... please wait.
    output: /luma/plugins/0004000000086500/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL USA:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086300/
    message: Extracting... please wait.
    output: /luma/plugins/0004000000086300/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL WA EUR:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198f00/
    message: Extracting... please wait.
    output: /luma/plugins/0004000000198f00/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL WA JPN:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198d00/
    message: Extracting... please wait.
    output: /luma/plugins/0004000000198d00/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Full ACNL WA USA:
  - file: Vapecord.Public.zip
    message: Download the latest Plugin... please wait.
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198e00/
    message: Extracting 1/3... please wait.
    output: /luma/plugins/0004000000198e00/
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting unneded file.
    type: deleteFile
  Plugin Boot.firm:
  - file: boot.firm
    message: Download the plugin boot.firm... please wait.
    output: /boot.firm
    repo: mariohackandglitch/Luma3DS
    type: downloadRelease
source: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin
systems:
- 3DS
title: Vapecord-ACNL-Plugin
updated: '2020-09-26T13:11:32Z'
version: v1.8.0
version_title: ACNL Vapecord Public Plugin [v.1.8.0] [EDITED]
wiki: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/wiki
---
