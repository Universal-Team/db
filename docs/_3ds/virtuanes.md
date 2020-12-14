---
author: bubble2k16
categories:
- emulator
color: '#3a71a4'
created: '2017-03-23T14:05:11Z'
description: VirtuaNES a high compatibility NES emulator for your old 3DS or 2DS.
download_page: https://github.com/bubble2k16/emus3ds/releases/tag/v1.02
downloads:
  virtuanes_3ds-v1.02.zip:
    size: 1371216
    url: https://github.com/bubble2k16/emus3ds/releases/download/v1.02/virtuanes_3ds-v1.02.zip
github: bubble2k16/emus3ds
icon: https://raw.githubusercontent.com/bubble2k16/emus3ds/master/src/cores/virtuanes/assets/icon.png
image: https://db.universal-team.net/assets/images/images/virtualnes.png
layout: app
scripts:
  virtuanes_3ds.3dsx:
  - file: virtuanes_3ds.*\.zip
    message: Downloading virtuanes_3ds zip...
    output: /virtuanes_3ds.zip
    repo: bubble2k16/emus3ds
    type: downloadRelease
  - file: /virtuanes_3ds.zip
    input: virtuanes_3ds.3dsx
    message: Extracting virtuanes_3ds.3dsx...
    output: '%3DSX%/virtuanes_3ds.3dsx'
    type: extractFile
  - file: /virtuanes_3ds.zip
    message: Deleting virtuanes_3ds.zip...
    type: deleteFile
  virtuanes_3ds.cia:
  - file: virtuanes_3ds.*\.zip
    message: Downloading virtuanes_3ds zip...
    output: /virtuanes_3ds.zip
    repo: bubble2k16/emus3ds
    type: downloadRelease
  - file: /virtuanes_3ds.zip
    input: virtuanes_3ds.cia
    message: Extracting virtuanes_3ds.cia...
    output: /virtuanes_3ds.cia
    type: extractFile
  - file: /virtuanes_3ds.cia
    message: Installing virtuanes_3ds.cia...
    type: installCia
  - file: /virtuanes_3ds.cia
    message: Deleting virtuanes_3ds.cia...
    type: deleteFile
  - file: /virtuanes_3ds.zip
    message: Deleting virtuanes_3ds.zip...
    type: deleteFile
source: https://github.com/bubble2k16/emus3ds
systems:
- 3DS
title: VirtuaNES
update_notes: '<ul>

  <li>Fixed bug in MMC5 mapper that was causing Castlevania 3''s graphics to corrupt.</li>

  <li>Optimized rendering to 16-bit buffer to reduce cache misses, and minor optimizations
  for MMC5 rendering.</li>

  <li>Fixed occassional crashing bug when loading a ROM.</li>

  </ul>'
updated: '2018-03-20T16:53:38Z'
version: v1.02
version_title: v1.02
wiki: https://github.com/bubble2k16/emus3ds/wiki
---
