---
author: Drenn1
categories:
- emulator
color: '#836f25'
created: '2013-02-22T17:16:52Z'
description: '[Super] Gameboy [Color] emulator for the Nintendo [3]DS'
download_page: https://github.com/Drenn1/GameYob/releases/tag/v0.5.2
downloads:
  gameyob.zip:
    size: 627066
    url: https://github.com/Drenn1/GameYob/releases/download/v0.5.2/gameyob.zip
github: Drenn1/GameYob
icon: https://raw.githubusercontent.com/Drenn1/GameYob/master/platform/ds/icon.bmp
image: https://avatars1.githubusercontent.com/u/3671681?v=4
layout: app
scripts:
  GameYob.cia:
  - file: gameyob.zip
    message: Downloading gameyob.zip...
    output: /gameyob.zip
    repo: Drenn1/GameYob
    type: downloadRelease
  - file: /gameyob.zip
    input: gameyob.cia
    message: Extracting gameyob.cia...
    output: /gameyob.cia
    type: extractFile
  - file: /gameyob.cia
    message: Installing gameyob.cia...
    type: installCia
  - file: /gameyob.cia
    message: Deleting gameyob.cia...
    type: deleteFile
  - file: /gameyob.zip
    message: Deleting gameyob.zip...
    type: deleteFile
  GameYob.nds:
  - file: gameyob.zip
    message: Downloading gameyob.zip...
    output: /gameyob.zip
    repo: Drenn1/GameYob
    type: downloadRelease
  - file: /gameyob.zip
    input: gameyob.nds
    message: Extracting gameyob.nds...
    output: '%NDS%/gameyob.nds'
    type: extractFile
  - file: /gameyob.zip
    message: Deleting gameyob.zip...
    type: deleteFile
source: https://github.com/Drenn1/GameYob
systems:
- DS
title: GameYob
updated: '2020-10-05T13:52:12Z'
version: v0.5.2
version_title: Version 0.5.2
website: https://gbatemp.net/threads/gameyob-a-gameboy-emulator-for-ds.343407/
wiki: https://github.com/Drenn1/GameYob/wiki
---
