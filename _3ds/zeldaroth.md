---
author: nop90
categories:
- game
color: '#ceb1a5'
created: '2016-05-06T23:17:31Z'
description: Port of Zelda ROTH on 3ds
download_page: https://github.com/nop90/ZeldaROTH/releases/tag/v1.0.2
downloads:
  ZeldaROTH_3DSX_v1.0.2.zip:
    size: 44110456
    url: https://github.com/nop90/ZeldaROTH/releases/download/v1.0.2/ZeldaROTH_3DSX_v1.0.2.zip
  ZeldaROTH_CIA_v1.0.2.zip:
    size: 45068215
    url: https://github.com/nop90/ZeldaROTH/releases/download/v1.0.2/ZeldaROTH_CIA_v1.0.2.zip
github: nop90/ZeldaROTH
icon: https://raw.githubusercontent.com/nop90/ZeldaROTH/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/ZeldaROTH/master/resources/banner.png
layout: app
scripts:
  ZeldaROTH.3dsx:
  - file: ZeldaROTH_3DSX.*.zip
    message: Downloading ZeldaROTH zip...
    output: /ZeldaROTH.zip
    repo: nop90/ZeldaROTH
    type: downloadRelease
  - file: /ZeldaROTH.zip
    input: ZeldaROTH/ZeldaROTH.3dsx
    message: Extracting ZeldaROTH.3dsx...
    output: '%3DSX%/ZeldaROTH.3dsx'
    type: extractFile
  - file: /ZeldaROTH.zip
    message: Deleting ZeldaROTH.zip...
    type: deleteFile
  ZeldaROTH.cia:
  - file: ZeldaROTH_CIA.*.zip
    message: Downloading ZeldaROTH zip...
    output: /ZeldaROTH.zip
    repo: nop90/ZeldaROTH
    type: downloadRelease
  - file: /ZeldaROTH.zip
    input: ZeldaROTH.cia
    message: Extracting ZeldaROTH.cia...
    output: /ZeldaROTH.cia
    type: extractFile
  - file: /ZeldaROTH.cia
    message: Installing ZeldaROTH.cia...
    type: installCia
  - file: /ZeldaROTH.cia
    message: Deleting ZeldaROTH.cia...
    type: deleteFile
  - file: /ZeldaROTH.zip
    message: Deleting ZeldaROTH.zip...
    type: deleteFile
source: https://github.com/nop90/ZeldaROTH
systems:
- 3DS
title: ZeldaROTH
updated: '2016-06-11T21:08:59Z'
version: v1.0.2
version_title: Minor changes
wiki: https://github.com/nop90/ZeldaROTH/wiki
---
