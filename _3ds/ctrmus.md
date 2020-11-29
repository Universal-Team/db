---
author: deltabeard
autogen_scripts: true
categories:
- utility
color: '#f7f6f7'
created: '2016-10-23T18:40:55Z'
description: 3DS Music Player
download_page: https://github.com/deltabeard/ctrmus/releases/tag/0.4.12
downloads:
  ctrmus.cia:
    size: 1036224
    url: https://github.com/deltabeard/ctrmus/releases/download/0.4.12/ctrmus.cia
  ctrmus.zip:
    size: 3047167
    url: https://github.com/deltabeard/ctrmus/releases/download/0.4.12/ctrmus.zip
github: deltabeard/ctrmus
icon: https://raw.githubusercontent.com/deltabeard/ctrmus/master/meta/icon.png
image: https://raw.githubusercontent.com/deltabeard/ctrmus/master/meta/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  ctrmus.cia: https://db.universal-team.net/assets/images/qr/ctrmus.cia.png
scripts:
  ctrmus.3dsx:
  - file: ctrmus.zip
    message: Downloading ctrmus.zip...
    output: /ctrmus.zip
    repo: deltabeard/ctrmus
    type: downloadRelease
  - file: /ctrmus.zip
    input: 3ds-arm/3ds/ctrmus/ctrmus.3dsx
    message: Extracting ctrmus.3dsx...
    output: '%3DSX%/ctrmus.3dsx'
    type: extractFile
  - file: /ctrmus.zip
    message: Deleting ctrmus.zip...
    type: deleteFile
source: https://github.com/deltabeard/ctrmus
systems:
- 3DS
title: ctrmus
update_notes: "* Add OGG Vorbis file support.\r\n* Update Opus and mpg123 libraries\
  \ to their latest version.\r\n* Further improvements to overall system stability\
  \ and other minor adjustments have been made to enhance the user experience.\r\n\
  \r\n![QR](https://zxing.org/w/chart?cht=qr&chs=230x230&chld=L&choe=UTF-8&chl=https%3A%2F%2Fgithub.com%2Fdeltabeard%2Fctrmus%2Freleases%2Fdownload%2F0.4.12%2Fctrmus.cia)"
updated: '2017-07-08T18:35:46Z'
version: 0.4.12
version_title: '0.4.12: Vorbis Support'
---
