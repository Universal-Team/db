---
author: d0k3
autogen_scripts: true
categories:
- utility
color: '#b49e8d'
created: '2015-06-07T12:31:39Z'
description: Open Source SD Explorer for the 3DS.
download_page: https://github.com/d0k3/CTRXplorer/releases/tag/v0.9.8.1
downloads:
  CTRXplorer.cia:
    size: 838080
    url: https://github.com/d0k3/CTRXplorer/releases/download/v0.9.8.1/CTRXplorer.cia
  CTRXplorer.v0.9.8.1.zip:
    size: 1827733
    url: https://github.com/d0k3/CTRXplorer/releases/download/v0.9.8.1/CTRXplorer.v0.9.8.1.zip
github: d0k3/CTRXplorer
icon: https://raw.githubusercontent.com/d0k3/CTRXplorer/master/meta/icon.png
image: https://raw.githubusercontent.com/d0k3/CTRXplorer/master/meta/banner.png
layout: app
license: mit
license_name: MIT License
qr:
  CTRXplorer.cia: https://db.universal-team.net/assets/images/qr/ctrxplorer.cia.png
scripts:
  CTRXplorer.3dsx:
  - file: CTRXplorer.*\.zip
    message: Downloading CTRXplorer zip...
    output: /CTRXplorer.zip
    repo: d0k3/CTRXplorer
    type: downloadRelease
  - file: /CTRXplorer.zip
    input: 3ds/CTRXplorer/CTRXplorer.3dsx
    message: Extracting CTRXplorer.3dsx...
    output: '%3DSX%/CTRXplorer.3dsx'
    type: extractFile
  - file: /CTRXplorer.zip
    message: Deleting CTRXplorer.zip...
    type: deleteFile
source: https://github.com/d0k3/CTRXplorer
systems:
- 3DS
title: CTRXplorer
update_notes: 'What''s new:

  o Virtual keyboard available for string mode editing in hex editor


  ![qrcode](https://cloud.githubusercontent.com/assets/12467483/22735721/41c21394-edfb-11e6-80d1-a0a13c4ff9f1.png)

  '
updated: '2017-02-08T11:36:20Z'
version: v0.9.8.1
version_title: CTRXplorer v0.9.8.1
wiki: https://github.com/d0k3/CTRXplorer/wiki
---
