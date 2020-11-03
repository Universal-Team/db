---
author: Jacudibu
autogen_scripts: true
categories:
- game
color: '#d6d6d6'
created: '2016-06-03T14:02:09Z'
description: "A Snake Clone for the Nintendo 3DS. Made with L\xF6vePotion."
download_page: https://github.com/Jacudibu/Snake2DS/releases/tag/v1.0
downloads:
  Snake2DS-3DSFiles-v1.0.zip:
    size: 874256
    url: https://github.com/Jacudibu/Snake2DS/releases/download/v1.0/Snake2DS-3DSFiles-v1.0.zip
  Snake2DS-PC-v1.0.zip:
    size: 2711426
    url: https://github.com/Jacudibu/Snake2DS/releases/download/v1.0/Snake2DS-PC-v1.0.zip
  Snake2DS.cia:
    size: 1217472
    url: https://github.com/Jacudibu/Snake2DS/releases/download/v1.0/Snake2DS.cia
github: Jacudibu/Snake2DS
icon: https://raw.githubusercontent.com/Jacudibu/Snake2DS/master/icon_large.png
image: https://db.universal-team.net/assets/images/images/snake2ds.png
layout: app
license: mit
license_name: MIT License
qr:
  Snake2DS.cia: https://db.universal-team.net/assets/images/qr/snake2ds.cia.png
scripts:
  Snake2DS.3dsx:
  - file: Snake2DS-3DSFiles.*\.zip
    message: Downloading Snake2DS-3DSFiles zip...
    output: /Snake2DS.zip
    repo: Jacudibu/Snake2DS
    type: downloadRelease
  - file: /Snake2DS.zip
    input: Snake2DS
    message: Extracting Snake2DS...
    output: '%3DSX%/Snake2DS/'
    type: extractFile
  - file: /Snake2DS.zip
    message: Deleting Snake2DS.zip...
    type: deleteFile
source: https://github.com/Jacudibu/Snake2DS
systems:
- 3DS
title: Snake2DS
updated: '2016-06-16T14:28:38Z'
version: v1.0
version_title: Release v1.0
wiki: https://github.com/Jacudibu/Snake2DS/wiki
---
