---
author: bubble2k16
categories:
- emulator
color: '#559cce'
created: '2017-06-18T16:00:26Z'
description: This is a port of Exophase's Temper (TurboGrafx/PC-Engine) emulator to
  the old 3DS and old 2DS.
download_page: https://github.com/bubble2k16/temperpce_3ds/releases/tag/v1.02
downloads:
  temperpce_3ds-v1.02.zip:
    size: 1367259
    url: https://github.com/bubble2k16/temperpce_3ds/releases/download/v1.02/temperpce_3ds-v1.02.zip
github: bubble2k16/temperpce_3ds
icon: https://raw.githubusercontent.com/bubble2k16/emus3ds/master/src/cores/temperpce/assets/icon.png
image: https://db.universal-team.net/assets/images/images/temperpce.png
layout: app
scripts:
  temperpce_3ds.3dsx:
  - file: temperpce_3ds.*\.zip
    message: Downloading temperpce_3ds zip...
    output: /temperpce_3ds.zip
    repo: bubble2k16/temperpce_3ds
    type: downloadRelease
  - file: /temperpce_3ds.zip
    input: temperpce_3ds.3dsx
    message: Extracting temperpce_3ds.3dsx...
    output: '%3DSX%/temperpce_3ds.3dsx'
    type: extractFile
  - file: /temperpce_3ds.zip
    message: Deleting temperpce_3ds.zip...
    type: deleteFile
  temperpce_3ds.cia:
  - file: temperpce_3ds.*\.zip
    message: Downloading temperpce_3ds zip...
    output: /temperpce_3ds.zip
    repo: bubble2k16/temperpce_3ds
    type: downloadRelease
  - file: /temperpce_3ds.zip
    input: temperpce_3ds.cia
    message: Extracting temperpce_3ds.cia...
    output: /temperpce_3ds.cia
    type: extractFile
  - file: /temperpce_3ds.cia
    message: Installing temperpce_3ds.cia...
    type: installCia
  - file: /temperpce_3ds.cia
    message: Deleting temperpce_3ds.cia...
    type: deleteFile
  - file: /temperpce_3ds.zip
    message: Deleting temperpce_3ds.zip...
    type: deleteFile
source: https://github.com/bubble2k16/temperpce_3ds
systems:
- 3DS
title: TemperPCE
updated: '2018-03-19T15:38:20Z'
version: v1.02
version_title: v1.02
wiki: https://github.com/bubble2k16/temperpce_3ds/wiki
---
