---
author: MechanicalDragon0687
autogen_scripts: true
categories:
- utility
color: '#735056'
created: '2019-02-02T20:50:32Z'
description: Super simple custom badge homebrew for the 3DS home menu.
download_page: https://github.com/MechanicalDragon0687/GYTB/releases/tag/1.0
downloads:
  GYTB.cia:
    size: 297408
    url: https://github.com/MechanicalDragon0687/GYTB/releases/download/1.0/GYTB.cia
  GYTB_hax.zip:
    size: 180734
    url: https://github.com/MechanicalDragon0687/GYTB/releases/download/1.0/GYTB_hax.zip
github: MechanicalDragon0687/GYTB
icon: https://raw.githubusercontent.com/MechanicalDragon0687/GYTB/master/resources/icon.png
image: https://raw.githubusercontent.com/MechanicalDragon0687/GYTB/master/resources/banner.png
layout: app
qr:
  GYTB.cia: https://db.universal-team.net/assets/images/qr/gytb.cia.png
scripts:
  GYTB.3dsx:
  - file: GYTB_hax.zip
    message: Downloading GYTB_hax.zip...
    output: /GYTB_hax.zip
    repo: MechanicalDragon0687/GYTB
    type: downloadRelease
  - file: /GYTB_hax.zip
    input: ''
    message: Extracting GYTB...
    output: /
    type: extractFile
  - new: '%3DSX%/GYTB.3dsx'
    old: /3ds/GYTB/GYTB.3dsx
    type: move
  - file: /GYTB_hax.zip
    message: Deleting GYTB_hax.zip...
    type: deleteFile
source: https://github.com/MechanicalDragon0687/GYTB
systems:
- 3DS
title: GYTB
updated: '2019-02-02T20:53:45Z'
version: '1.0'
version_title: GYTB
wiki: https://github.com/MechanicalDragon0687/GYTB/wiki
---
