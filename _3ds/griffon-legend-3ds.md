---
author: nop90
categories:
- game
color: '#d0e2cf'
created: '2016-12-05T09:08:27Z'
description: Port to 3DS of a nice Action RPG in SNES style originally written by
  Syn9 in FreeBASIC
download_page: https://github.com/nop90/Griffon-Legend-3DS/releases/tag/v1.0
downloads:
  GriffonLegend.v1.0.zip:
    size: 5008278
    url: https://github.com/nop90/Griffon-Legend-3DS/releases/download/v1.0/GriffonLegend.v1.0.zip
github: nop90/Griffon-Legend-3DS
icon: https://raw.githubusercontent.com/nop90/Griffon-Legend-3DS/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/Griffon-Legend-3DS/master/resources/banner.png
layout: app
license: other
license_name: Other
scripts:
  GriffonLegend.3dsx:
  - file: GriffonLegend.*\.zip
    message: Downloading GriffonLegend.zip...
    output: /GriffonLegend.zip
    repo: nop90/Griffon-Legend-3DS
    type: downloadRelease
  - file: /GriffonLegend.zip
    input: GriffonLegend.3dsx
    message: Extracting GriffonLegend.3dsx...
    output: '%3DSX%/GriffonLegend.3dsx'
    type: extractFile
  - file: /GriffonLegend.zip
    message: Deleting GriffonLegend.zip...
    type: deleteFile
  GriffonLegend.cia:
  - file: GriffonLegend.*\.zip
    message: Downloading GriffonLegend.zip...
    output: /GriffonLegend.zip
    repo: nop90/Griffon-Legend-3DS
    type: downloadRelease
  - file: /GriffonLegend.zip
    input: GriffonLegend.cia
    message: Extracting GriffonLegend.cia...
    output: /GriffonLegend.cia
    type: extractFile
  - file: /GriffonLegend.cia
    message: Installing GriffonLegend.cia...
    type: installCia
  - file: /GriffonLegend.cia
    message: Deleting GriffonLegend.cia...
    type: deleteFile
  - file: /GriffonLegend.zip
    message: Deleting GriffonLegend.zip...
    type: deleteFile
source: https://github.com/nop90/Griffon-Legend-3DS
systems:
- 3DS
title: Griffon-Legend-3DS
updated: '2017-02-12T16:35:33Z'
version: v1.0
version_title: Final release
wiki: https://github.com/nop90/Griffon-Legend-3DS/wiki
---
