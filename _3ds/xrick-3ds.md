---
author: nop90
categories:
- game
color: '#764d2f'
created: '2017-03-01T23:04:10Z'
description: Port to 3ds of the open source remake of Rick Dangerous
download_page: https://github.com/nop90/Xrick-3ds/releases/tag/v1.0
downloads:
  Xrick_v1.0.zip:
    size: 3966121
    url: https://github.com/nop90/Xrick-3ds/releases/download/v1.0/Xrick_v1.0.zip
github: nop90/Xrick-3ds
icon: https://raw.githubusercontent.com/nop90/Xrick-3ds/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/Xrick-3ds/master/resources/banner.png
layout: app
scripts:
  Xrick.3dsx:
  - file: Xrick.*\.zip
    message: Downloading Xrick zip...
    output: /Xrick.zip
    repo: nop90/Xrick-3ds
    type: downloadRelease
  - file: /Xrick.zip
    input: Xrick/Xrick.3dsx
    message: Extracting Xrick.3dsx...
    output: '%3DSX%/Xrick.3dsx'
    type: extractFile
  - file: /Xrick.zip
    message: Deleting Xrick.zip...
    type: deleteFile
  Xrick.cia:
  - file: Xrick.*\.zip
    message: Downloading Xrick zip...
    output: /Xrick.zip
    repo: nop90/Xrick-3ds
    type: downloadRelease
  - file: /Xrick.zip
    input: Xrick.cia
    message: Extracting Xrick.cia...
    output: /Xrick.cia
    type: extractFile
  - file: /Xrick.cia
    message: Installing Xrick.cia...
    type: installCia
  - file: /Xrick.cia
    message: Deleting Xrick.cia...
    type: deleteFile
  - file: /Xrick.zip
    message: Deleting Xrick.zip...
    type: deleteFile
source: https://github.com/nop90/Xrick-3ds
systems:
- 3DS
title: Xrick-3ds
updated: '2017-03-10T20:41:13Z'
version: v1.0
version_title: Stable release
wiki: https://github.com/nop90/Xrick-3ds/wiki
---
