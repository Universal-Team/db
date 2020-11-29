---
author: nop90
categories:
- game
color: '#c39b4b'
created: '2017-01-04T10:11:24Z'
description: Port to 3DS of the roguelike game POWDER
download_page: https://github.com/nop90/POWDER-3DS/releases/tag/v1%2C1
downloads:
  Powder.v1.1.zip:
    size: 2372799
    url: https://github.com/nop90/POWDER-3DS/releases/download/v1%2C1/Powder.v1.1.zip
github: nop90/POWDER-3DS
icon: https://raw.githubusercontent.com/nop90/POWDER-3DS/master/port/3ds/icon.png
image: https://raw.githubusercontent.com/nop90/POWDER-3DS/master/port/3ds/banner.png
layout: app
license: other
license_name: Other
scripts:
  Powder.3dsx:
  - file: Powder.*\.zip
    message: Downloading Powder.zip...
    output: /Powder.zip
    repo: nop90/POWDER-3DS
    type: downloadRelease
  - file: /Powder.zip
    input: Powder/Powder.3dsx
    message: Extracting Powder.3dsx...
    output: '%3DSX%/Powder.3dsx'
    type: extractFile
  - file: /Powder.zip
    message: Deleting Powder.zip...
    type: deleteFile
  Powder.cia:
  - file: Powder.*\.zip
    message: Downloading Powder.zip...
    output: /Powder.zip
    repo: nop90/POWDER-3DS
    type: downloadRelease
  - file: /Powder.zip
    input: Powder.cia
    message: Extracting Powder.cia...
    output: /Powder.cia
    type: extractFile
  - file: /Powder.cia
    message: Installing Powder.cia...
    type: installCia
  - file: /Powder.cia
    message: Deleting Powder.cia...
    type: deleteFile
  - file: /Powder.zip
    message: Deleting Powder.zip...
    type: deleteFile
source: https://github.com/nop90/POWDER-3DS
systems:
- 3DS
title: POWDER-3DS
update_notes: '- raised walking speed

  - changed version srting from GBA to 3DS

  '
updated: '2017-02-03T23:50:45Z'
version: v1,1
version_title: Some improvements
wiki: https://github.com/nop90/POWDER-3DS/wiki
---
