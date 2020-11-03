---
author: Steveice10
autogen_scripts: true
categories:
- emulator
color: '#9e8e57'
created: '2015-02-06T01:26:33Z'
description: '[Super] Gameboy [Color] emulator for the Nintendo [3]DS'
download_page: https://github.com/Steveice10/GameYob/releases/tag/1.0.8
downloads:
  GameYob.cia:
    size: 792000
    url: https://github.com/Steveice10/GameYob/releases/download/1.0.8/GameYob.cia
  GameYob.zip:
    size: 4168036
    url: https://github.com/Steveice10/GameYob/releases/download/1.0.8/GameYob.zip
github: Steveice10/GameYob
icon: https://raw.githubusercontent.com/Steveice10/GameYob/master/meta/icon_3ds.png
image: https://avatars2.githubusercontent.com/u/1269164?v=4
layout: app
license: mit
license_name: MIT License
qr:
  GameYob.cia: https://db.universal-team.net/assets/images/qr/gameyob.cia.png
scripts:
  GameYob.3dsx:
  - file: GameYob.zip
    message: Downloading GameYob.zip...
    output: /GameYob.zip
    repo: Steveice10/GameYob
    type: downloadRelease
  - file: /GameYob.zip
    input: 3ds-arm/3ds/GameYob/GameYob.3dsx
    message: Extracting GameYob.3dsx...
    output: '%3DSX%/GameYob.3dsx'
    type: extractFile
  - file: /GameYob.zip
    message: Deleting GameYob.zip...
    type: deleteFile
source: https://github.com/Steveice10/GameYob
systems:
- 3DS
title: GameYob (3DS)
updated: '2015-12-23T02:19:04Z'
version: 1.0.8
version_title: 1.0.8
---
