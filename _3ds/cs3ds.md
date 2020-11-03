---
author: machinamentum
categories:
- game
color: '#333c49'
created: '2016-04-14T01:43:54Z'
description: CSPSP port for 3DS
download_page: https://github.com/machinamentum/CS3DS/releases/tag/0.6-alpha
github: machinamentum/CS3DS
icon: https://raw.githubusercontent.com/machinamentum/CS3DS/master/jge/Projects/cspsp/icon_3ds.png
image: https://db.universal-team.net/assets/images/images/cs3ds.png
layout: app
prerelease:
  download_page: https://github.com/machinamentum/CS3DS/releases/tag/0.6-alpha
  downloads:
    cspsp.zip:
      size: 7314200
      url: https://github.com/machinamentum/CS3DS/releases/download/0.6-alpha/cspsp.zip
  updated: '2016-04-22T01:51:31Z'
  version: 0.6-alpha
scripts:
  '[prerelease] cspsp.3dsx':
  - file: cspsp.zip
    includePrereleases: true
    message: Downloading cspsp.zip...
    output: /cspsp.zip
    repo: machinamentum/CS3DS
    type: downloadRelease
  - file: /cspsp.zip
    input: cspsp/
    message: Extracting cspsp...
    output: /cspsp/
    type: extractFile
  - message: Moving cspsp.3dsx...
    new: '%3DSX%/cspsp.3dsx'
    old: /cspsp/cspsp.3dsx
    type: move
  - file: /cspsp/cspsp.cia
    message: Deleting cspsp.cia...
    type: deleteFile
  - file: /cspsp/cspsp.smdh
    message: Deleting cspsp.smdh...
    type: deleteFile
  - file: /cspsp/README.txt
    message: Deleting README.txt...
    type: deleteFile
  - file: /cspsp.zip
    message: Deleting cspsp.zip...
    type: deleteFile
  '[prerelease] cspsp.cia':
  - file: cspsp.zip
    includePrereleases: true
    message: Downloading cspsp.zip...
    output: /cspsp.zip
    repo: machinamentum/CS3DS
    type: downloadRelease
  - file: /cspsp.zip
    input: cspsp/
    message: Extracting cspsp...
    output: /cspsp/
    type: extractFile
  - file: /cspsp/cspsp.cia
    message: Installing cspsp.cia...
    type: installCia
  - file: /cspsp/cspsp.3dsx
    message: Deleting cspsp.3dsx...
    type: deleteFile
  - file: /cspsp/cspsp.cia
    message: Deleting cspsp.cia...
    type: deleteFile
  - file: /cspsp/cspsp.smdh
    message: Deleting cspsp.smdh...
    type: deleteFile
  - file: /cspsp/README.txt
    message: Deleting README.txt...
    type: deleteFile
  - file: /cspsp.zip
    message: Deleting cspsp.zip...
    type: deleteFile
source: https://github.com/machinamentum/CS3DS
systems:
- 3DS
title: CS3DS
updated: '2016-04-22T01:51:31Z'
version: 0.6-alpha
wiki: https://github.com/machinamentum/CS3DS/wiki
---
