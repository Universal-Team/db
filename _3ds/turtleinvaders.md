---
author: TurtleP
categories:
- game
color: '#4d4317'
created: '2015-08-29T03:59:28Z'
description: A fixed-axis shooter with netplay
download_page: https://github.com/TurtleP/TurtleInvaders/releases/tag/v1.0.2
downloads:
  TurtleInvaders.zip:
    size: 5546969
    url: https://github.com/TurtleP/TurtleInvaders/releases/download/v1.0.2/TurtleInvaders.zip
github: TurtleP/TurtleInvaders
icon: https://db.universal-team.net/assets/images/icons/turtleinvaders.png
image: https://db.universal-team.net/assets/images/images/turtleinvaders.png
layout: app
license: other
license_name: Other
scripts:
  TurtleInvaders.3dsx:
  - file: TurtleInvaders.zip
    message: Downloading TurtleInvaders.zip...
    output: /TurtleInvaders.zip
    repo: TurtleP/TurtleInvaders
    type: downloadRelease
  - file: /TurtleInvaders.zip
    input: TurtleInvaders.3dsx
    message: Extracting TurtleInvaders.3dsx...
    output: '%3DSX%/TurtleInvaders/TurtleInvaders.3dsx'
    type: extractFile
  - file: /TurtleInvaders.zip
    input: game
    message: Extracting game...
    output: '%3DSX%/TurtleInvaders/game'
    type: extractFile
  - file: /TurtleInvaders.zip
    message: Deleting TurtleInvaders.zip...
    type: deleteFile
  TurtleInvaders.cia:
  - file: TurtleInvaders.zip
    message: Downloading TurtleInvaders.zip...
    output: /TurtleInvaders.zip
    repo: TurtleP/TurtleInvaders
    type: downloadRelease
  - file: /TurtleInvaders.zip
    input: TurtleInvaders.cia
    message: Extracting TurtleInvaders.cia...
    output: /TurtleInvaders.cia
    type: extractFile
  - file: /TurtleInvaders.cia
    message: Installing TurtleInvaders.cia...
    type: installCia
  - file: /TurtleInvaders.cia
    message: Deleting TurtleInvaders.cia...
    type: deleteFile
  - file: /TurtleInvaders.zip
    message: Deleting TurtleInvaders.zip...
    type: deleteFile
source: https://github.com/TurtleP/TurtleInvaders
systems:
- 3DS
title: TurtleInvaders
updated: '2016-06-30T04:51:24Z'
version: v1.0.2
version_title: 3DS Stable Release 1.0.2
wiki: https://github.com/TurtleP/TurtleInvaders/wiki
---
