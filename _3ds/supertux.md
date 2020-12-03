---
author: nop90
categories:
- game
color: '#6d756e'
created: '2017-03-22T22:13:53Z'
description: Port to 3ds of Supertux v0.1.3 (Milestone 1)
download_page: https://github.com/nop90/Supertux-Milestone1-3ds/releases/tag/v0.1
github: nop90/Supertux-Milestone1-3ds
icon: https://raw.githubusercontent.com/nop90/Supertux-Milestone1-3ds/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/Supertux-Milestone1-3ds/master/resources/banner.png
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
prerelease:
  download_page: https://github.com/nop90/Supertux-Milestone1-3ds/releases/tag/v0.1
  downloads:
    Supertux_M1_v0.1a.zip:
      size: 16342520
      url: https://github.com/nop90/Supertux-Milestone1-3ds/releases/download/v0.1/Supertux_M1_v0.1a.zip
  updated: '2017-03-22T22:55:55Z'
  version: v0.1
  version_title: First release
scripts:
  '[prerelease] Supertux.3dsx':
  - file: Supertux.*\.zip
    includePrereleases: true
    message: Downloading Supertux zip...
    output: /Supertux.zip
    repo: nop90/Supertux-Milestone1-3ds
    type: downloadRelease
  - file: /Supertux.zip
    input: Supertux/Supertux.3dsx
    message: Extracting Supertux.3dsx...
    output: '%3DSX%/Supertux.3dsx'
    type: extractFile
  - file: /Supertux.zip
    message: Deleting Supertux.zip...
    type: deleteFile
  '[prerelease] Supertux.cia':
  - file: Supertux.*\.zip
    includePrereleases: true
    message: Downloading Supertux zip...
    output: /Supertux.zip
    repo: nop90/Supertux-Milestone1-3ds
    type: downloadRelease
  - file: /Supertux.zip
    input: Supertux.cia
    message: Extracting Supertux.cia...
    output: /Supertux.cia
    type: extractFile
  - file: /Supertux.cia
    message: Installing Supertux.cia...
    type: installCia
  - file: /Supertux.cia
    message: Deleting Supertux.cia...
    type: deleteFile
  - file: /Supertux.zip
    message: Deleting Supertux.zip...
    type: deleteFile
source: https://github.com/nop90/Supertux-Milestone1-3ds
systems:
- 3DS
title: Supertux
updated: '2017-03-22T22:55:55Z'
version: v0.1
version_title: First release
wiki: https://github.com/nop90/Supertux-Milestone1-3ds/wiki
---
