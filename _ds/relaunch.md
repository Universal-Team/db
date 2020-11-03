---
author: Universal-Team
categories:
- utility
color: '#282928'
created: '2019-04-27T19:07:23Z'
description: "Open-Source lookalike of nocash\u2019s Unlaunch.dsi"
download_page: https://github.com/Universal-Team/Relaunch/releases/tag/v4.0.1
downloads:
  Relaunch.7z:
    size: 148518
    url: https://github.com/Universal-Team/Relaunch/releases/download/v4.0.1/Relaunch.7z
github: Universal-Team/Relaunch
icon: https://raw.githubusercontent.com/Universal-Team/Relaunch/master/main/icon.bmp
image: https://raw.githubusercontent.com/Universal-Team/Relaunch/master/logo.png
layout: app
license: mit
license_name: MIT License
nightly:
  download_page: https://github.com/Universal-Team/extras/tree/master/builds/Relaunch
  downloads:
    Relaunch.7z:
      url: https://github.com/Universal-Team/extras/raw/master/builds/Relaunch/Relaunch.7z
scripts:
  Relaunch.cia:
  - file: Relaunch.7z
    message: Downloading Relaunch.7z...
    output: /Relaunch.7z
    repo: Universal-Team/Relaunch
    type: downloadRelease
  - file: /Relaunch.7z
    input: Relaunch/Relaunch.cia
    message: Extracting Relaunch.cia...
    output: /Relaunch.cia
    type: extractFile
  - file: /Relaunch.7z
    input: Relaunch/_nds/Relaunch/menu.bin
    message: Extracting menu.bin...
    output: /_nds/Relaunch/menu.bin
    type: extractFile
  - file: /Relaunch.cia
    message: Installing Relaunch.cia...
    type: installCia
  - file: /Relaunch.cia
    message: Deleting Relaunch.cia...
    type: deleteFile
  - file: /Relaunch.7z
    message: Deleting Relaunch.7z...
    type: deleteFile
  Relaunch.nds:
  - file: Relaunch.7z
    message: Downloading Relaunch.7z...
    output: /Relaunch.7z
    repo: Universal-Team/Relaunch
    type: downloadRelease
  - file: /Relaunch.7z
    input: Relaunch/Relaunch.nds
    message: Extracting Relaunch.nds...
    output: '%NDS%/Relaunch.nds'
    type: extractFile
  - file: /Relaunch.7z
    input: Relaunch/_nds/Relaunch/menu.bin
    message: Extracting menu.bin...
    output: /_nds/Relaunch/menu.bin
    type: extractFile
  - file: /Relaunch.7z
    message: Deleting Relaunch.7z...
    type: deleteFile
  '[nightly] Relaunch.cia':
  - file: https://github.com/Universal-Team/extras/raw/master/builds/Relaunch/Relaunch.7z
    message: Downloading Relaunch.7z...
    output: /Relaunch.7z
    type: downloadFile
  - file: /Relaunch.7z
    input: Relaunch/Relaunch.cia
    message: Extracting Relaunch.cia...
    output: /Relaunch.cia
    type: extractFile
  - file: /Relaunch.7z
    input: Relaunch/_nds/Relaunch/menu.bin
    message: Extracting menu.bin...
    output: /_nds/Relaunch/menu.bin
    type: extractFile
  - file: /Relaunch.cia
    message: Installing Relaunch.cia...
    type: installCia
  - file: /Relaunch.cia
    message: Deleting Relaunch.cia...
    type: deleteFile
  - file: /Relaunch.7z
    message: Deleting Relaunch.7z...
    type: deleteFile
  '[nightly] Relaunch.nds':
  - file: https://github.com/Universal-Team/extras/raw/master/builds/Relaunch/Relaunch.7z
    message: Downloading Relaunch.7z...
    output: /Relaunch.7z
    type: downloadFile
  - file: /Relaunch.7z
    input: Relaunch/Relaunch.nds
    message: Extracting Relaunch.nds...
    output: '%NDS%/Relaunch.nds'
    type: extractFile
  - file: /Relaunch.7z
    input: Relaunch/_nds/Relaunch/menu.bin
    message: Extracting menu.bin...
    output: /_nds/Relaunch/menu.bin
    type: extractFile
  - file: /Relaunch.7z
    message: Deleting Relaunch.7z...
    type: deleteFile
source: https://github.com/Universal-Team/Relaunch
systems:
- DS
title: Relaunch
updated: '2020-07-20T15:23:43Z'
version: v4.0.1
version_title: 'v4.0.1: replace Bruh edition'
website: https://universal-team.net/projects/relaunch
wiki: https://github.com/Universal-Team/Relaunch/wiki
---
