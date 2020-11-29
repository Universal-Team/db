---
author: Omegadrien
categories:
- game
color: '#c8cacf'
created: '2016-10-13T20:48:22Z'
description: A 3DS memory game!
download_page: https://github.com/Omegadrien/Memory3DS/releases/tag/v1.0
downloads:
  Memory3DSv1.0.zip:
    size: 19521332
    url: https://github.com/Omegadrien/Memory3DS/releases/download/v1.0/Memory3DSv1.0.zip
github: Omegadrien/Memory3DS
icon: https://raw.githubusercontent.com/Omegadrien/Memory3DS/master/assets/icon.png
image: https://raw.githubusercontent.com/Omegadrien/Memory3DS/master/assets/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  Memory3DS.3dsx:
  - file: Memory3DS.*\.zip
    message: Downloading Memory3DS.zip...
    output: /Memory3DS.zip
    repo: Omegadrien/Memory3DS
    type: downloadRelease
  - file: /Memory3DS.zip
    input: Memory3DS/3ds/Memory3DS/Memory3DS.3dsx
    message: Extracting Memory3DS.3dsx...
    output: '%3DSX%/Memory3DS.3dsx'
    type: extractFile
  - file: /Memory3DS.zip
    message: Deleting Memory3DS.zip...
    type: deleteFile
  Memory3DS.cia:
  - file: Memory3DS.*\.zip
    message: Downloading Memory3DS.zip...
    output: /Memory3DS.zip
    repo: Omegadrien/Memory3DS
    type: downloadRelease
  - file: /Memory3DS.zip
    input: Memory3DS/Memory3DS.cia
    message: Extracting Memory3DS.cia...
    output: /Memory3DS.cia
    type: extractFile
  - file: /Memory3DS.cia
    message: Installing Memory3DS.cia...
    type: installCia
  - file: /Memory3DS.cia
    message: Deleting Memory3DS.cia...
    type: deleteFile
  - file: /Memory3DS.zip
    message: Deleting Memory3DS.zip...
    type: deleteFile
source: https://github.com/Omegadrien/Memory3DS
systems:
- 3DS
title: Memory3DS
update_notes: 'First release!

  '
updated: '2016-10-13T20:58:21Z'
version: v1.0
version_title: Memory3DS
wiki: https://github.com/Omegadrien/Memory3DS/wiki
---
