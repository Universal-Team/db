---
author: Steveice10
autogen_scripts: true
categories:
- game
color: '#231e13'
created: '2014-12-04T06:15:13Z'
description: World of Sand for the 3DS.
download_page: https://github.com/Steveice10/WorldOf3DSand/releases/tag/1.3.4
downloads:
  Worldof3DSand.cia:
    size: 737216
    url: https://github.com/Steveice10/WorldOf3DSand/releases/download/1.3.4/Worldof3DSand.cia
  Worldof3DSand.zip:
    size: 2139145
    url: https://github.com/Steveice10/WorldOf3DSand/releases/download/1.3.4/Worldof3DSand.zip
github: Steveice10/WorldOf3DSand
icon: https://raw.githubusercontent.com/Steveice10/WorldOf3DSand/master/meta/icon_3ds.png
image: https://raw.githubusercontent.com/Steveice10/WorldOf3DSand/master/meta/banner_3ds.png
layout: app
license: mit
license_name: MIT License
qr:
  Worldof3DSand.cia: https://db.universal-team.net/assets/images/qr/worldof3dsand.cia.png
scripts:
  Worldof3DSand.3dsx:
  - file: Worldof3DSand.zip
    message: Downloading Worldof3DSand.zip...
    output: /Worldof3DSand.zip
    repo: Steveice10/WorldOf3DSand
    type: downloadRelease
  - file: /Worldof3DSand.zip
    input: 3ds-arm/3ds/Worldof3DSand/Worldof3DSand.3dsx
    message: Extracting Worldof3DSand.3dsx...
    output: '%3DSX%/Worldof3DSand.3dsx'
    type: extractFile
  - file: /Worldof3DSand.zip
    message: Deleting Worldof3DSand.zip...
    type: deleteFile
source: https://github.com/Steveice10/WorldOf3DSand
systems:
- 3DS
title: WorldOf3DSand
update_notes: '- Bring tooling up to date.

  - Change unique ID to 0xF8002.

  - Migrate to citro3d.

  '
updated: '2016-07-12T03:28:55Z'
version: 1.3.4
version_title: 1.3.4
---
