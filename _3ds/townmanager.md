---
author: dragos240
categories:
- utility
- save-tool
color: '#ae822b'
created: '2016-10-20T18:11:56Z'
description: A specialized save manager for AC:NL
download_page: https://github.com/dragos240/TownManager/releases/tag/v1.2.1
downloads:
  TownManager-v1.2.1.zip:
    size: 1445661
    url: https://github.com/dragos240/TownManager/releases/download/v1.2.1/TownManager-v1.2.1.zip
github: dragos240/TownManager
icon: https://raw.githubusercontent.com/dragos240/TownManager/master/icon.png
image: https://raw.githubusercontent.com/dragos240/TownManager/master/res/banner%20icon.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  TownManager.3dsx:
  - file: TownManager.*\.zip
    message: Downloading TownManager.zip...
    output: /TownManager.zip
    repo: dragos240/TownManager
    type: downloadRelease
  - file: /TownManager.zip
    input: TownManager/TownManager.3dsx
    message: Extracting TownManager.3dsx...
    output: '%3DSX%/TownManager.3dsx'
    type: extractFile
  - file: /TownManager.zip
    message: Deleting TownManager.zip...
    type: deleteFile
  TownManager.cia:
  - file: TownManager.*\.zip
    message: Downloading TownManager.zip...
    output: /TownManager.zip
    repo: dragos240/TownManager
    type: downloadRelease
  - file: /TownManager.zip
    input: TownManager/TownManager.cia
    message: Extracting TownManager.cia...
    output: /TownManager.cia
    type: extractFile
  - file: /TownManager.cia
    message: Installing TownManager.cia...
    type: installCia
  - file: /TownManager.cia
    message: Deleting TownManager.cia...
    type: deleteFile
  - file: /TownManager.zip
    message: Deleting TownManager.zip...
    type: deleteFile
source: https://github.com/dragos240/TownManager
systems:
- 3DS
title: TownManager
update_notes: <p>Converts tm.conf files to the new config format.</p>
updated: '2017-01-21T13:45:49Z'
version: v1.2.1
version_title: v1.2.1 - Bugfix release
wiki: https://github.com/dragos240/TownManager/wiki
---
