---
author: phijor
autogen_scripts: true
categories:
- utility
color: '#a8a8a8'
created: '2016-05-09T16:49:33Z'
description: Use your 3DS as a gamepad on linux
download_page: https://github.com/phijor/ctroller/releases/tag/0.4.0
downloads:
  ctroller-0.4.0.tar.gz:
    size: 489430
    url: https://github.com/phijor/ctroller/releases/download/0.4.0/ctroller-0.4.0.tar.gz
  ctroller.cia:
    size: 620992
    url: https://github.com/phijor/ctroller/releases/download/0.4.0/ctroller.cia
github: phijor/ctroller
icon: https://raw.githubusercontent.com/phijor/ctroller/master/3DS/resources/icon.png
image: https://raw.githubusercontent.com/phijor/ctroller/master/3DS/resources/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  ctroller.cia: https://db.universal-team.net/assets/images/qr/ctroller.cia.png
scripts:
  ctroller.3dsx:
  - message: UU is unable to extract this at the moment...
    type: promptMessage
  - type: exit
  - file: ctroller.*.tar.gz
    message: Downloading ctroller.tar.gz...
    output: /ctroller.tar.gz
    repo: phijor/ctroller
    type: downloadRelease
  - file: /ctroller.tar.gz
    input: ctroller.tar
    message: Extracting ctroller.tar...
    output: /ctroller.tar
    type: extractFile
  - file: /ctroller.tar
    input: ctroller.3dsx
    message: Extracting ctroller.3dsx...
    output: '%3DSX%/ctroller.3dsx'
    type: extractFile
  - file: /ctroller.tar.gz
    message: Deleting ctroller.tar.gz...
    type: deleteFile
  - file: /ctroller.tar
    message: Deleting ctroller.tar...
    type: deleteFile
source: https://github.com/phijor/ctroller
systems:
- 3DS
title: ctroller
updated: '2016-06-15T19:03:12Z'
version: 0.4.0
version_title: '0.4.0: Virtual device rework and gyroscope support'
wiki: https://github.com/phijor/ctroller/wiki
---
