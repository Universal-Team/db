---
author: masterfeizz
categories:
- game
color: '#44291b'
created: '2015-10-20T01:25:02Z'
description: Port of quake for the Nintendo 3DS
download_page: https://github.com/masterfeizz/ctrQuake/releases/tag/v0.8
downloads:
  ctrQuake.cia:
    size: 984000
    url: https://github.com/masterfeizz/ctrQuake/releases/download/v0.8/ctrQuake.cia
  ctrQuake.zip:
    size: 8921677
    url: https://github.com/masterfeizz/ctrQuake/releases/download/v0.8/ctrQuake.zip
github: masterfeizz/ctrQuake
icon: https://raw.githubusercontent.com/masterfeizz/ctrQuake/master/icon.png
image: https://db.universal-team.net/assets/images/images/ctrquake.png
layout: app
qr:
  ctrQuake.cia: https://db.universal-team.net/assets/images/qr/ctrquake.cia.png
scripts:
  ctrQuake.3dsx:
  - file: ctrQuake.zip
    message: Downloading ctrQuake.zip...
    output: /ctrQuake.zip
    repo: masterfeizz/ctrQuake
    type: downloadRelease
  - file: /ctrQuake.zip
    input: ''
    message: Extracting ctrQuake...
    output: /
    type: extractFile
  - new: '%3DSX%/ctrQuake.3dsx'
    old: /3ds/ctrQuake/ctrQuake.3dsx
    type: move
  - file: /ctrQuake.zip
    message: Deleting ctrQuake.zip...
    type: deleteFile
  ctrQuake.cia:
  - file: ctrQuake.zip
    message: Downloading ctrQuake.zip...
    output: /ctrQuake.zip
    repo: masterfeizz/ctrQuake
    type: downloadRelease
  - file: /ctrQuake.zip
    input: ''
    message: Extracting ctrQuake...
    output: /
    type: extractFile
  - file: ctrQuake.cia
    message: Downloading ctrQuake.cia...
    output: /ctrQuake.cia
    repo: masterfeizz/ctrQuake
    type: downloadRelease
  - file: /ctrQuake.cia
    message: Installing ctrQuake.cia...
    type: installCia
  - file: /ctrQuake.cia
    message: Deleting ctrQuake.cia...
    type: deleteFile
  - file: /ctrQuake.zip
    message: Deleting ctrQuake.zip...
    type: deleteFile
source: https://github.com/masterfeizz/ctrQuake
systems:
- 3DS
title: ctrQuake
update_notes: 'You can now host and also join online servers. Dithering has also been
  implemented and can be toggled from the options menu.


  A list of servers that "SHOULD" work can be found here http://servers.quakeone.com/home/0

  Keep in mind that most servers require the full game


  Happy Fragging

  '
updated: '2016-09-13T02:38:10Z'
version: v0.8
version_title: 8th Release - Online MP
wiki: https://github.com/masterfeizz/ctrQuake/wiki
---
