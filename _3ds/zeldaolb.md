---
author: nop90
autogen_scripts: true
categories:
- game
color: '#d1babe'
created: '2016-06-06T17:44:23Z'
description: Port of Zelda OLB on 3ds
download_page: https://github.com/nop90/ZeldaOLB/releases/tag/v1%2C1
downloads:
  ZeldaOLB_3DSX_v1.1.zip:
    size: 84591843
    url: https://github.com/nop90/ZeldaOLB/releases/download/v1%2C1/ZeldaOLB_3DSX_v1.1.zip
  ZeldaOLB_v1.1.cia:
    size: 103437248
    url: https://github.com/nop90/ZeldaOLB/releases/download/v1%2C1/ZeldaOLB_v1.1.cia
github: nop90/ZeldaOLB
icon: https://raw.githubusercontent.com/nop90/ZeldaOLB/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/ZeldaOLB/master/resources/banner.png
layout: app
qr:
  ZeldaOLB_v1.1.cia: https://db.universal-team.net/assets/images/qr/zeldaolb_v1.1.cia.png
scripts:
  ZeldaOLB.3dsx:
  - file: ZeldaOLB_3DSX.*\.zip
    message: Downloading ZeldaOLB_3DSX zip...
    output: /ZeldaOLB_3DSX.zip
    repo: nop90/ZeldaOLB
    type: downloadRelease
  - file: /ZeldaOLB_3DSX.zip
    input: ZeldaOLB/ZeldaOLB.3dsx
    message: Extracting ZeldaOLB.3dsx...
    output: '%3DSX%/ZeldaOLB.3dsx'
    type: extractFile
  - file: /ZeldaOLB_3DSX.zip
    message: Deleting ZeldaOLB_3DSX.zip...
    type: deleteFile
source: https://github.com/nop90/ZeldaOLB
systems:
- 3DS
title: ZeldaOLB
updated: '2017-06-07T19:23:53Z'
version: v1,1
version_title: Improved Italian translation and made some fixes
wiki: https://github.com/nop90/ZeldaOLB/wiki
---
