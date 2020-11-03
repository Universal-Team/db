---
author: bubble2k16
categories:
- emulator
color: '#1449b4'
created: '2018-01-06T16:44:35Z'
description: This is a port of notaz's PicoDrive emulator to the old 3DS and old 2DS.
download_page: https://github.com/bubble2k16/picodrive_3ds/releases/tag/v0.94
downloads:
  picodrive_3ds-v0.94.zip:
    size: 1372485
    url: https://github.com/bubble2k16/picodrive_3ds/releases/download/v0.94/picodrive_3ds-v0.94.zip
github: bubble2k16/picodrive_3ds
icon: https://raw.githubusercontent.com/bubble2k16/emus3ds/master/src/cores/picodrive/assets/icon.png
image: https://db.universal-team.net/assets/images/images/picodrive.png
layout: app
scripts:
  picodrive_3ds.3dsx:
  - file: picodrive_3ds.*\.zip
    message: Downloading picodrive_3ds zip...
    output: /picodrive_3ds.zip
    repo: bubble2k16/picodrive_3ds
    type: downloadRelease
  - file: /picodrive_3ds.zip
    input: picodrive_3ds.3dsx
    message: Extracting picodrive_3ds.3dsx...
    output: '%3DSX%/picodrive_3ds.cia'
    type: extractFile
  - file: /picodrive_3ds.zip
    message: Deleting picodrive_3ds.zip...
    type: deleteFile
  picodrive_3ds.cia:
  - file: picodrive_3ds.*\.zip
    message: Downloading picodrive_3ds zip...
    output: /picodrive_3ds.zip
    repo: bubble2k16/picodrive_3ds
    type: downloadRelease
  - file: /picodrive_3ds.zip
    input: picodrive_3ds.cia
    message: Extracting picodrive_3ds.cia...
    output: /picodrive_3ds.cia
    type: extractFile
  - file: /picodrive_3ds.cia
    message: Installing picodrive_3ds.cia...
    type: installCia
  - file: /picodrive_3ds.cia
    message: Deleting picodrive_3ds.cia...
    type: deleteFile
  - file: /picodrive_3ds.zip
    message: Deleting picodrive_3ds.zip...
    type: deleteFile
source: https://github.com/bubble2k16/picodrive_3ds
systems:
- 3DS
title: PicoDrive
updated: '2018-03-24T02:19:48Z'
version: v0.94
version_title: v0.94
wiki: https://github.com/bubble2k16/picodrive_3ds/wiki
---
