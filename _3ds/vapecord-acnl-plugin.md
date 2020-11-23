---
author: RedShyGuy
categories:
- utility
color: '#947677'
created: '2019-08-22T07:15:13Z'
description: Animal Crossing NL Vapecord Public Plugin WIP
download_page: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/tag/v1.8.1
downloads:
  Vapecord.Public.zip:
    size: 4330434
    url: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/download/v1.8.1/Vapecord.Public.zip
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
updated: '2020-11-10T22:24:13Z'
version: v1.8.1
version_title: ACNL Vapecord Public Plugin [v.1.8.1][EDIT]
wiki: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/wiki
---
