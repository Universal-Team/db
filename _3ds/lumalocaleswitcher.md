---
author: Possum
autogen_scripts: true
categories:
- utility
color: '#8b9990'
created: '2016-05-06T00:51:34Z'
description: Front end to Luma3DS compatible locale system.
download_page: https://github.com/Possum/LumaLocaleSwitcher/releases/tag/0.04
downloads:
  LumaLocaleSwitcher-0.04-NIGHTLY.cia:
    size: 545728
    url: https://github.com/Possum/LumaLocaleSwitcher/releases/download/0.04/LumaLocaleSwitcher-0.04-NIGHTLY.cia
  LumaLocaleSwitcher-0.04-NIGHTLY.zip:
    size: 1764562
    url: https://github.com/Possum/LumaLocaleSwitcher/releases/download/0.04/LumaLocaleSwitcher-0.04-NIGHTLY.zip
  LumaLocaleSwitcher-0.04.cia:
    size: 545728
    url: https://github.com/Possum/LumaLocaleSwitcher/releases/download/0.04/LumaLocaleSwitcher-0.04.cia
  LumaLocaleSwitcher-0.04.zip:
    size: 1764105
    url: https://github.com/Possum/LumaLocaleSwitcher/releases/download/0.04/LumaLocaleSwitcher-0.04.zip
github: Possum/LumaLocaleSwitcher
icon: https://raw.githubusercontent.com/Possum/LumaLocaleSwitcher/master/meta/icon.png
image: https://raw.githubusercontent.com/Possum/LumaLocaleSwitcher/master/meta/banner.png
layout: app
license: mit
license_name: MIT License
qr:
  LumaLocaleSwitcher-0.04-NIGHTLY.cia: https://db.universal-team.net/assets/images/qr/lumalocaleswitcher-0.04-nightly.cia.png
  LumaLocaleSwitcher-0.04.cia: https://db.universal-team.net/assets/images/qr/lumalocaleswitcher-0.04.cia.png
scripts:
  '[luma <= 6.6] LumaLocaleSwitcher.3dsx':
  - file: LumaLocaleSwitcher-0.04.zip
    message: Downloading LumaLocaleSwitcher-0.04.zip...
    output: /LumaLocaleSwitcher.zip
    repo: Possum/LumaLocaleSwitcher
    type: downloadRelease
  - file: /LumaLocaleSwitcher.zip
    input: 3ds/LumaLocaleSwitcher/LumaLocaleSwitcher-0.04-NIGHTLY.3dsx
    message: Extracting LumaLocaleSwitcher-0.04-NIGHTLY.3dsx...
    output: '%3DSX%/LumaLocaleSwitcher-0.04-NIGHTLY.3dsx'
    type: extractFile
  - file: /LumaLocaleSwitcher.zip
    message: Deleting LumaLocaleSwitcher.zip...
    type: deleteFile
  '[luma > 6.6] LumaLocaleSwitcher.3dsx':
  - file: LumaLocaleSwitcher-0.04-NIGHTLY.zip
    message: Downloading LumaLocaleSwitcher-0.04-NIGHTLY.zip...
    output: /LumaLocaleSwitcher.zip
    repo: Possum/LumaLocaleSwitcher
    type: downloadRelease
  - file: /LumaLocaleSwitcher.zip
    input: 3ds/LumaLocaleSwitcher/LumaLocaleSwitcher-0.04.3dsx
    message: Extracting LumaLocaleSwitcher-0.04.3dsx...
    output: '%3DSX%/LumaLocaleSwitcher-0.04.3dsx'
    type: extractFile
  - file: /LumaLocaleSwitcher.zip
    message: Deleting LumaLocaleSwitcher-0.04.zip...
    type: deleteFile
source: https://github.com/Possum/LumaLocaleSwitcher
systems:
- 3DS
title: LumaLocaleSwitcher
updated: '2017-04-22T18:55:03Z'
version: '0.04'
version_title: '0.04'
wiki: https://github.com/Possum/LumaLocaleSwitcher/wiki
---
