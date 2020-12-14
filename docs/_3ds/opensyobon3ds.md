---
author: nop90
categories:
- game
color: '#9ca8a5'
created: '2016-04-23T18:50:28Z'
description: 'Open Syobon Action (a.k.a Cat Mario) for 3DS '
download_page: https://github.com/nop90/OpenSyobon3DS/releases/tag/v1.2
downloads:
  OpenSyobon3DS_v1.2.zip:
    size: 14967899
    url: https://github.com/nop90/OpenSyobon3DS/releases/download/v1.2/OpenSyobon3DS_v1.2.zip
github: nop90/OpenSyobon3DS
icon: https://raw.githubusercontent.com/nop90/OpenSyobon3DS/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/OpenSyobon3DS/master/resources/banner.png
layout: app
scripts:
  OpenSyobon3DS.3dsx:
  - file: OpenSyobon3DS.*\.zip
    message: Downloading OpenSyobon3DS zip...
    output: /OpenSyobon3DS.zip
    repo: author/repo
    type: downloadRelease
  - file: /OpenSyobon3DS.zip
    input: 3ds/OpenSyobon3DS/OpenSyobon3DS.3dsx
    message: Extracting OpenSyobon3DS.3dsx...
    output: '%3DSX%/OpenSyobon3DS.3dsx'
    type: extractFile
  - file: /OpenSyobon3DS.zip
    message: Deleting OpenSyobon3DS.zip...
    type: deleteFile
  OpenSyobon3DS.cia:
  - file: OpenSyobon3DS.*\.zip
    message: Downloading OpenSyobon3DS zip...
    output: /OpenSyobon3DS.zip
    repo: author/repo
    type: downloadRelease
  - file: /OpenSyobon3DS.zip
    input: OpenSyobon3DS.cia
    message: Extracting OpenSyobon3DS.cia...
    output: /OpenSyobon3DS.cia
    type: extractFile
  - file: /OpenSyobon3DS.cia
    message: Installing OpenSyobon3DS.cia...
    type: installCia
  - file: /OpenSyobon3DS.cia
    message: Deleting OpenSyobon3DS.cia...
    type: deleteFile
  - file: /OpenSyobon3DS.zip
    message: Deleting OpenSyobon3DS.zip...
    type: deleteFile
source: https://github.com/nop90/OpenSyobon3DS
systems:
- 3DS
title: OpenSyobon3DS
update_notes: '<ul>

  <li>Fixed blurred text caused by SFTDLib (used workaround found on Xerpi github)</li>

  <li>Added sprites for ceiling spikes, previously drawn as white lines</li>

  <li>Changed two level icons with better images</li>

  <li>Added touch controls for level selection in menu and to retry level/quit level
  in game</li>

  </ul>'
updated: '2016-07-27T08:58:59Z'
version: v1.2
version_title: Open Syobon 3DS v1.2
wiki: https://github.com/nop90/OpenSyobon3DS/wiki
---
