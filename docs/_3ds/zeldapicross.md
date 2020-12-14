---
author: nop90
categories:
- game
color: '#bdb183'
created: '2016-12-05T09:24:55Z'
description: Port  to 3DS of the Zelda style picross game by Vincent Joiullat
download_page: https://github.com/nop90/ZeldaPicross/releases/tag/v1%2C0RC
github: nop90/ZeldaPicross
icon: https://raw.githubusercontent.com/nop90/ZeldaPicross/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/ZeldaPicross/master/resources/banner.png
layout: app
prerelease:
  download_page: https://github.com/nop90/ZeldaPicross/releases/tag/v1%2C0RC
  downloads:
    ZeldaPicross.1.0RC.zip:
      size: 23147777
      url: https://github.com/nop90/ZeldaPicross/releases/download/v1%2C0RC/ZeldaPicross.1.0RC.zip
  updated: '2017-01-02T12:35:39Z'
  version: v1,0RC
  version_title: CIA Build
scripts:
  '[prerelease] ZeldaPicross.3dsx':
  - file: ZeldaPicross.*\.zip
    includePrereleases: true
    message: Downloading ZeldaPicross zip...
    output: /ZeldaPicross.zip
    repo: nop90/ZeldaPicross
    type: downloadRelease
  - file: /ZeldaPicross.zip
    input: ZeldaPicross/ZeldaPicross.3dsx
    message: Extracting ZeldaPicross.3dsx...
    output: '%3DSX%/ZeldaPicross.3dsx'
    type: extractFile
  - file: /ZeldaPicross.zip
    message: Deleting ZeldaPicross.zip...
    type: deleteFile
  '[prerelease] ZeldaPicross.cia':
  - file: ZeldaPicross.*\.zip
    includePrereleases: true
    message: Downloading ZeldaPicross zip...
    output: /ZeldaPicross.zip
    repo: nop90/ZeldaPicross
    type: downloadRelease
  - file: /ZeldaPicross.zip
    input: ZeldaPicross.cia
    message: Extracting ZeldaPicross.cia...
    output: /ZeldaPicross.cia
    type: extractFile
  - file: /ZeldaPicross.cia
    message: Installing ZeldaPicross.cia...
    type: installCia
  - file: /ZeldaPicross.cia
    message: Deleting ZeldaPicross.cia...
    type: deleteFile
  - file: /ZeldaPicross.zip
    message: Deleting ZeldaPicross.zip...
    type: deleteFile
source: https://github.com/nop90/ZeldaPicross
systems:
- 3DS
title: ZeldaPicross
updated: '2017-01-02T12:35:39Z'
version: v1,0RC
version_title: CIA Build
wiki: https://github.com/nop90/ZeldaPicross/wiki
---
