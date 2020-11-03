---
author: ingolemo
categories:
- utility
color: '#e5b8b8'
created: '2016-04-29T11:51:59Z'
description: An epub reader for the Nintendo3DS
download_page: https://github.com/ingolemo/drider/releases/tag/v0.6
downloads:
  drider.zip:
    size: 3165004
    url: https://github.com/ingolemo/drider/releases/download/v0.6/drider.zip
github: ingolemo/drider
icon: https://raw.githubusercontent.com/ingolemo/drider/master/icon.png
image: https://raw.githubusercontent.com/ingolemo/drider/master/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  drider.3dsx:
  - file: drider.zip
    message: Downloading drider.zip...
    output: /drider.zip
    repo: ingolemo/drider
    type: downloadRelease
  - file: /drider.zip
    input: 3ds/
    message: Extracting drider...
    output: /3ds/
    type: extractFile
  - message: Moving drider.3dsx...
    new: '%3DSX%/drider.3dsx'
    old: /3ds/drider/drider.3dsx
    type: move
  - file: /drider.zip
    message: Deleting drider.zip...
    type: deleteFile
  drider.cia:
  - file: drider.zip
    message: Downloading drider.zip...
    output: /drider.zip
    repo: ingolemo/drider
    type: downloadRelease
  - file: /drider.zip
    input: ''
    message: Extracting drider...
    output: /
    type: extractFile
  - file: /drider.cia
    message: Installing drider.cia...
    type: installCia
  - file: /drider.cia
    message: Deleting drider.cia...
    type: deleteFile
  - file: /drider.zip
    message: Deleting drider.zip...
    type: deleteFile
source: https://github.com/ingolemo/drider
systems:
- 3DS
title: drider
updated: '2017-11-14T16:05:57Z'
version: v0.6
version_title: Really images this time.
wiki: https://github.com/ingolemo/drider/wiki
---
