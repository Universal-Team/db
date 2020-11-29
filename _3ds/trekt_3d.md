---
author: Manurocker95
autogen_scripts: true
categories:
- game
color: '#5f9478'
created: '2017-08-26T12:59:26Z'
description: T-Rekt for 3DS in C++
download_page: https://github.com/Manurocker95/TRekt_3D/releases/tag/1.0
downloads:
  TRekt_3D.cia:
    size: 6026176
    url: https://github.com/Manurocker95/TRekt_3D/releases/download/1.0/TRekt_3D.cia
  TRekt_3D.rar:
    size: 7699415
    url: https://github.com/Manurocker95/TRekt_3D/releases/download/1.0/TRekt_3D.rar
github: Manurocker95/TRekt_3D
icon: https://raw.githubusercontent.com/Manurocker95/TRekt_3D/master/TRekt_3D/resources/icon.png
image: https://raw.githubusercontent.com/Manurocker95/TRekt_3D/master/TRekt_3D/resources/banner.png
layout: app
qr:
  TRekt_3D.cia: https://db.universal-team.net/assets/images/qr/trekt_3d.cia.png
scripts:
  TRekt.3dsx:
  - message: UU is unable to extract this at the moment...
    type: promptMessage
  - type: exit
  - file: TRekt_3D.rar
    message: Downloading TRekt_3D.rar...
    output: /TRekt_3D.rar
    repo: Manurocker95/TRekt_3D
    type: downloadRelease
  - file: /TRekt_3D.rar
    input: TRekt_3D.3dsx
    message: Extracting TRekt_3D.3dsx...
    output: '%3DSX%/TRekt_3D.3dsx'
    type: extractFile
  - file: /TRekt_3D.rar
    message: Deleting TRekt_3D.rar...
    type: deleteFile
source: https://github.com/Manurocker95/TRekt_3D
systems:
- 3DS
title: TRekt_3D
update_notes: Just one meteorite falls. Debug Mode activated by default
updated: '2017-08-26T15:39:19Z'
version: '1.0'
version_title: '1.0'
wiki: https://github.com/Manurocker95/TRekt_3D/wiki
---
