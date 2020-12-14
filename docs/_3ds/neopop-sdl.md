---
author: nop90
autogen_scripts: true
categories:
- emulator
color: '#e5c3c3'
created: '2017-06-01T21:56:07Z'
description: Neo Geo Pocket Color Emulator for 3DS
download_page: https://github.com/nop90/Neopop-SDL/releases/tag/v0.4
github: nop90/Neopop-SDL
icon: https://raw.githubusercontent.com/nop90/Neopop-SDL/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/Neopop-SDL/master/resources/banner.png
layout: app
prerelease:
  download_page: https://github.com/nop90/Neopop-SDL/releases/tag/v0.4
  downloads:
    neopop_3DSX_v0.4.zip:
      size: 415884
      url: https://github.com/nop90/Neopop-SDL/releases/download/v0.4/neopop_3DSX_v0.4.zip
    neopop_v0.4.cia:
      size: 1180608
      url: https://github.com/nop90/Neopop-SDL/releases/download/v0.4/neopop_v0.4.cia
  qr:
    neopop_v0.4.cia: https://db.universal-team.net/assets/images/qr/prerelease/neopop_v0.4.cia.png
  updated: '2017-06-14T18:53:35Z'
  version: v0.4
  version_title: Menu completed
scripts:
  neopop.3dsx:
  - file: neopop_3DSX.*\.zip
    message: Downloading neopop zip...
    output: /neopop.zip
    repo: nop90/Neopop-SDL
    type: downloadRelease
  - file: /neopop.zip
    input: neopop/neopop.3dsx
    message: Extracting neopop.3dsx...
    output: '%3DSX%/neopop.3dsx'
    type: extractFile
  - file: /neopop.zip
    message: Deleting neopop.zip...
    type: deleteFile
source: https://github.com/nop90/Neopop-SDL
systems:
- 3DS
title: Neopop-SDL
updated: '2017-06-14T18:53:35Z'
version: v0.4
version_title: Menu completed
wiki: https://github.com/nop90/Neopop-SDL/wiki
---
