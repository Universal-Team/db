---
author: suloku
categories:
- utility
- save-tool
color: '#adb1a4'
created: '2015-10-14T14:54:41Z'
description: "Pok\xE9mon Dream Radar Savegame Editor for 3DS"
download_page: https://github.com/suloku/pdrpse/releases/tag/0.3
downloads:
  pdrpse_0.3.zip:
    size: 521315
    url: https://github.com/suloku/pdrpse/releases/download/0.3/pdrpse_0.3.zip
github: suloku/pdrpse
icon: https://raw.githubusercontent.com/suloku/pdrpse/master/icon.png
image: https://db.universal-team.net/assets/images/images/pdrpse.png
layout: app
scripts:
  pdrpse.3dsx:
  - file: pdrpse.*\.zip
    message: Downloading pdrpse zip...
    output: /pdrpse.zip
    repo: suloku/pdrpse
    type: downloadRelease
  - file: /pdrpse.zip
    input: 3ds/pdrpse/pdrpse.3dsx
    message: Extracting pdrpse.3dsx...
    output: '%3DSX%/pdrpse.3dsx'
    type: extractFile
  - file: /pdrpse.zip
    message: Deleting pdrpse.zip...
    type: deleteFile
  pdrpse.cia:
  - file: pdrpse.*\.zip
    message: Downloading pdrpse zip...
    output: /pdrpse.zip
    repo: suloku/pdrpse
    type: downloadRelease
  - file: /pdrpse.zip
    input: pdrpse.cia
    message: Extracting pdrpse.cia...
    output: /pdrpse.cia
    type: extractFile
  - file: /pdrpse.cia
    message: Installing pdrpse.cia...
    type: installCia
  - file: /pdrpse.cia
    message: Deleting pdrpse.cia...
    type: deleteFile
  - file: /pdrpse.zip
    message: Deleting pdrpse.zip...
    type: deleteFile
source: https://github.com/suloku/pdrpse
systems:
- 3DS
title: pdrpse
updated: '2015-10-18T21:15:51Z'
version: '0.3'
version_title: Free Refills
wiki: https://github.com/suloku/pdrpse/wiki
---
