---
author: Lordus
categories:
- emulator
color: '#875536'
description: A Sega Genesis/MegaDrive emulator for the Nintendo DS
download_page: https://gamebrew.org/wiki/JEnesisDS
downloads:
  JEnesisDS0174.zip:
    url: https://db.universal-team.net/assets/files/JEnesisDS0174.zip
icon: https://db.universal-team.net/assets/images/icons/jenesisds.png
layout: app
scripts:
  jEnesisDS.nds:
  - file: https://db.universal-team.net/assets/files/JEnesisDS0174.zip
    message: Downloading JEnesisDS0174.zip...
    output: /JEnesisDS0174.zip
    type: downloadFile
  - file: /JEnesisDS0174.zip
    input: jEnesisDS.nds
    message: Extracting jEnesisDS.nds...
    output: '%NDS%/jEnesisDS.nds'
    type: extractFile
  - file: /JEnesisDS0174.zip
    message: Deleting JEnesisDS0174.zip...
    type: deleteFile
systems:
- DS
title: jEnesisDS
updated: '2008-07-12T17:41:22Z'
version: v0.7.4
---
