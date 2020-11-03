---
author: deltabeard
autogen_scripts: true
categories:
- utility
color: '#f7f6f7'
created: '2016-10-23T18:40:55Z'
description: 3DS Music Player
download_page: https://github.com/deltabeard/ctrmus/releases/tag/0.4.12
downloads:
  ctrmus.cia:
    size: 1036224
    url: https://github.com/deltabeard/ctrmus/releases/download/0.4.12/ctrmus.cia
  ctrmus.zip:
    size: 3047167
    url: https://github.com/deltabeard/ctrmus/releases/download/0.4.12/ctrmus.zip
github: deltabeard/ctrmus
icon: https://raw.githubusercontent.com/deltabeard/ctrmus/master/meta/icon.png
image: https://raw.githubusercontent.com/deltabeard/ctrmus/master/meta/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  ctrmus.cia: https://db.universal-team.net/assets/images/qr/ctrmus.cia.png
scripts:
  ctrmus.3dsx:
  - file: ctrmus.zip
    message: Downloading ctrmus.zip...
    output: /ctrmus.zip
    repo: deltabeard/ctrmus
    type: downloadRelease
  - file: /ctrmus.zip
    input: 3ds-arm/3ds/ctrmus/ctrmus.3dsx
    message: Extracting ctrmus.3dsx...
    output: '%3DSX%/ctrmus.3dsx'
    type: extractFile
  - file: /ctrmus.zip
    message: Deleting ctrmus.zip...
    type: deleteFile
source: https://github.com/deltabeard/ctrmus
systems:
- 3DS
title: ctrmus
updated: '2017-07-08T18:35:46Z'
version: 0.4.12
version_title: '0.4.12: Vorbis Support'
---
