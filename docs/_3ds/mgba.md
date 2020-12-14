---
author: mgba-emu
categories:
- emulator
color: '#503a7e'
created: '2014-12-09T21:37:23Z'
description: mGBA Game Boy Advance Emulator
download_page: https://github.com/mgba-emu/mgba/releases/tag/0.8.4
downloads:
  mGBA-0.8.4-3ds.7z:
    size: 1086332
    url: https://github.com/mgba-emu/mgba/releases/download/0.8.4/mGBA-0.8.4-3ds.7z
github: mgba-emu/mgba
icon: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-48.png
image: https://raw.githubusercontent.com/mgba-emu/mgba/master/res/mgba-256.png
layout: app
license: mpl-2.0
license_name: Mozilla Public License 2.0
screenshots:
- description: File list
  url: https://db.universal-team.net/assets/images/screenshots/mgba/file-list.png
- description: In game menu
  url: https://db.universal-team.net/assets/images/screenshots/mgba/in-game-menu.png
- description: Scale 1x
  url: https://db.universal-team.net/assets/images/screenshots/mgba/scale-1x.png
- description: Scale aspect ratio
  url: https://db.universal-team.net/assets/images/screenshots/mgba/scale-aspect-ratio.png
- description: Scale stretch
  url: https://db.universal-team.net/assets/images/screenshots/mgba/scale-stretch.png
scripts:
  mgba.3dsx:
  - file: mGBA-.*-3ds.7z
    message: Downloading mGBA.7z...
    output: /mGBA.7z
    repo: mgba-emu/mgba
    type: downloadRelease
  - file: /mGBA.7z
    input: mGBA-.*-3ds/3dsx/mgba.3dsx
    message: Extracting mgba.3dsx...
    output: /mgba.3dsx
    type: extractFile
  - file: /mGBA.7z
    message: Deleting mGBA.7z...
    type: deleteFile
  mgba.cia:
  - file: mGBA-.*-3ds.7z
    message: Downloading mGBA.7z...
    output: /mGBA.7z
    repo: mgba-emu/mgba
    type: downloadRelease
  - file: /mGBA.7z
    input: mGBA-.*-3ds/cia/mgba.cia
    message: Extracting mgba.cia...
    output: /mgba.cia
    type: extractFile
  - file: /mgba.cia
    message: Installing mgba.cia...
    type: installCia
  - file: /mgba.cia
    message: Deleting mgba.cia...
    type: deleteFile
  - file: /mGBA.7z
    message: Deleting mGBA.7z...
    type: deleteFile
source: https://github.com/mgba-emu/mgba
systems:
- 3DS
title: mGBA
updated: '2020-10-30T02:03:03Z'
version: 0.8.4
website: https://mgba.io/
---
