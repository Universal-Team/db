---
author: nop90
categories:
- game
color: '#ada6a0'
created: '2017-03-04T06:48:10Z'
download_page: https://github.com/nop90/Opentyrian-3ds/releases/tag/v1.1
downloads:
  Opentyrian_v1.1.zip:
    size: 9369840
    url: https://github.com/nop90/Opentyrian-3ds/releases/download/v1.1/Opentyrian_v1.1.zip
github: nop90/Opentyrian-3ds
icon: https://raw.githubusercontent.com/nop90/Opentyrian-3ds/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/Opentyrian-3ds/master/resources/banner.png
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
scripts:
  Opentyrian.3dsx:
  - file: Opentyrian.*\.zip
    message: Downloading Opentyrian.zip...
    output: /Opentyrian.zip
    repo: nop90/Opentyrian-3ds
    type: downloadRelease
  - file: /Opentyrian.zip
    input: Opentyrian/Opentyrian.3dsx
    message: Extracting Opentyrian.3dsx...
    output: '%3DSX%/Opentyrian.3dsx'
    type: extractFile
  - file: /Opentyrian.zip
    message: Deleting Opentyrian.zip...
    type: deleteFile
  Opentyrian.cia:
  - file: Opentyrian.*\.zip
    message: Downloading Opentyrian.zip...
    output: /Opentyrian.zip
    repo: nop90/Opentyrian-3ds
    type: downloadRelease
  - file: /Opentyrian.zip
    input: Opentyrian.cia
    message: Extracting Opentyrian.cia...
    output: /Opentyrian.cia
    type: extractFile
  - file: /Opentyrian.cia
    message: Installing Opentyrian.cia...
    type: installCia
  - file: /Opentyrian.cia
    message: Deleting Opentyrian.cia...
    type: deleteFile
  - file: /Opentyrian.zip
    message: Deleting Opentyrian.zip...
    type: deleteFile
source: https://github.com/nop90/Opentyrian-3ds
systems:
- 3DS
title: Opentyrian-3ds
updated: '2017-03-11T20:24:51Z'
version: v1.1
version_title: Bugfix
wiki: https://github.com/nop90/Opentyrian-3ds/wiki
---
