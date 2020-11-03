---
author: dragos240
categories:
- utility
- save-tool
color: '#007600'
created: '2016-08-31T14:42:55Z'
description: 'A portable save editor for Animal Crossing: New Leaf on the Nintendo
  3DS'
download_page: https://github.com/dragos240/Pocket-NLSE/releases/tag/v1.0.0
downloads:
  Pocket-NLSE-v1.0.0.zip:
    size: 2068489
    url: https://github.com/dragos240/Pocket-NLSE/releases/download/v1.0.0/Pocket-NLSE-v1.0.0.zip
github: dragos240/Pocket-NLSE
icon: https://raw.githubusercontent.com/dragos240/Pocket-NLSE/master/icon.png
image: https://raw.githubusercontent.com/dragos240/Pocket-NLSE/master/res/banner%20icon.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  Pocket-NLSE.3dsx:
  - file: Pocket-NLSE.*\.zip
    message: Downloading Pocket-NLSE zip...
    output: /Pocket-NLSE.zip
    repo: dragos240/Pocket-NLSE
    type: downloadRelease
  - file: /Pocket-NLSE.zip
    input: Pocket-NLSE/Pocket-NLSE.3dsx
    message: Extracting Pocket-NLSE.3dsx...
    output: '%3DSX%/Pocket-NLSE.3dsx'
    type: extractFile
  - file: /Pocket-NLSE.zip
    message: Deleting Pocket-NLSE.zip...
    type: deleteFile
  Pocket-NLSE.cia:
  - file: Pocket-NLSE.*\.zip
    message: Downloading Pocket-NLSE zip...
    output: /Pocket-NLSE.zip
    repo: dragos240/Pocket-NLSE
    type: downloadRelease
  - file: /Pocket-NLSE.zip
    input: Pocket-NLSE/Pocket-NLSE.cia
    message: Extracting Pocket-NLSE.cia...
    output: /Pocket-NLSE.cia
    type: extractFile
  - file: /Pocket-NLSE.cia
    message: Installing Pocket-NLSE.cia...
    type: installCia
  - file: /Pocket-NLSE.cia
    message: Deleting Pocket-NLSE.cia...
    type: deleteFile
  - file: /Pocket-NLSE.zip
    message: Deleting Pocket-NLSE.zip...
    type: deleteFile
source: https://github.com/dragos240/Pocket-NLSE
systems:
- 3DS
title: Pocket-NLSE
updated: '2017-01-11T13:18:21Z'
version: v1.0.0
version_title: v1.0.0
wiki: https://github.com/dragos240/Pocket-NLSE/wiki
---
