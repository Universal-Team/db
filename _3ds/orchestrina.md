---
author: EBLeifEricson
categories:
- utility
color: '#b7b7cf'
created: '2016-07-09T04:21:45Z'
description: A homebrew Legend of Zelda instrument player
download_page: https://github.com/EBLeifEricson/orchestrina/releases/tag/v0.5.0-beta
downloads:
  Orchestrina.zip:
    size: 20274620
    url: https://github.com/EBLeifEricson/orchestrina/releases/download/v0.5.0-beta/Orchestrina.zip
github: EBLeifEricson/orchestrina
icon: https://raw.githubusercontent.com/EBLeifEricson/orchestrina/master/meta/icon.png
image: https://raw.githubusercontent.com/EBLeifEricson/orchestrina/master/meta/banner2.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  Orchestrina.3dsx:
  - file: Orchestrina.zip
    message: Downloading Orchestrina.zip...
    output: /Orchestrina.zip
    repo: EBLeifEricson/orchestrina
    type: downloadRelease
  - file: /Orchestrina.zip
    input: 3ds-arm/3ds/Orchestrina/Orchestrina.3dsx
    message: Extracting Orchestrina.3dsx...
    output: '%3DSX%/Orchestrina.3dsx'
    type: extractFile
  - file: /Orchestrina.zip
    message: Deleting Orchestrina.zip...
    type: deleteFile
  Orchestrina.cia:
  - file: Orchestrina.zip
    message: Downloading Orchestrina.zip...
    output: /Orchestrina.zip
    repo: EBLeifEricson/orchestrina
    type: downloadRelease
  - file: /Orchestrina.zip
    input: 3ds-arm/Orchestrina.cia
    message: Extracting Orchestrina.cia...
    output: /Orchestrina.cia
    type: extractFile
  - file: /Orchestrina.cia
    message: Installing Orchestrina.cia...
    type: installCia
  - file: /Orchestrina.cia
    message: Deleting Orchestrina.cia...
    type: deleteFile
  - file: /Orchestrina.zip
    message: Deleting Orchestrina.zip...
    type: deleteFile
source: https://github.com/EBLeifEricson/orchestrina
systems:
- 3DS
title: orchestrina
updated: '2017-03-30T01:49:01Z'
version: v0.5.0-beta
version_title: Orchestrina - Beta Release 5
wiki: https://github.com/EBLeifEricson/orchestrina/wiki
---
