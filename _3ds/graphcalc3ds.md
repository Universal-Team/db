---
author: flarn2006
autogen_scripts: true
categories:
- utility
color: '#becdda'
created: '2015-10-04T00:18:09Z'
description: Simple graphing calculator for 3DS
download_page: https://github.com/flarn2006/GraphCalc3DS/releases/tag/v1.5.1
downloads:
  GraphCalc3DS.cia:
    size: 1024960
    url: https://github.com/flarn2006/GraphCalc3DS/releases/download/v1.5.1/GraphCalc3DS.cia
  GraphCalc3DS_3DSX.zip:
    size: 292107
    url: https://github.com/flarn2006/GraphCalc3DS/releases/download/v1.5.1/GraphCalc3DS_3DSX.zip
github: flarn2006/graphcalc3ds
icon: https://raw.githubusercontent.com/flarn2006/GraphCalc3DS/master/icon.png
image: https://raw.githubusercontent.com/flarn2006/GraphCalc3DS/master/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  GraphCalc3DS.cia: https://db.universal-team.net/assets/images/qr/graphcalc3ds.cia.png
scripts:
  GraphCalc3DS.3dsx:
  - file: GraphCalc3DS_3DSX.zip
    message: Downloading GraphCalc3DS_3DSX.zip...
    output: /GraphCalc3DS_3DSX.zip
    repo: flarn2006/graphcalc3ds
    type: downloadRelease
  - file: /GraphCalc3DS_3DSX.zip
    input: GraphCalc3DS.3dsx
    message: Extracting GraphCalc3DS.3dsx...
    output: '%3DSX%/GraphCalc3DS.3dsx'
    type: extractFile
  - file: /GraphCalc3DS_3DSX.zip
    message: Deleting GraphCalc3DS_3DSX.zip...
    type: deleteFile
source: https://github.com/flarn2006/GraphCalc3DS
systems:
- 3DS
title: GraphCalc3DS
update_notes: 'Small release to fix a bug in version 1.5. The bug was that undefined
  values weren''t graphed properly (properly in this case being not at all) when the
  equation was entered in algebraic notation. Because of this bug, for example, `sqrt(1-x^2)`
  would appear as the top half of a circle like it should, except there would be two
  vertical lines on the sides. Version 1.5.1 fixes this bug.


  QR code for CIA:


  ![https://github.com/flarn2006/GraphCalc3DS/releases/download/v1.5.1/GraphCalc3DS.cia](http://i.imgur.com/qzu5DL3.png)

  '
updated: '2016-12-03T21:05:23Z'
version: v1.5.1
version_title: Version 1.5.1
wiki: https://github.com/flarn2006/GraphCalc3DS/wiki
---
