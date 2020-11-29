---
author: GiantBlargg
autogen_scripts: true
categories:
- utility
color: '#ffc9ac'
created: '2015-11-29T08:18:36Z'
description: Temporarily suppresses the 3ds update nag.
download_page: https://github.com/GiantBlargg/UpdateSuppressor/releases/tag/v0.2.0
downloads:
  UpdateSuppressor-3dsx.zip:
    size: 91407
    url: https://github.com/GiantBlargg/UpdateSuppressor/releases/download/v0.2.0/UpdateSuppressor-3dsx.zip
  UpdateSuppressor.cia:
    size: 557504
    url: https://github.com/GiantBlargg/UpdateSuppressor/releases/download/v0.2.0/UpdateSuppressor.cia
github: GiantBlargg/UpdateSuppressor
icon: https://raw.githubusercontent.com/GiantBlargg/UpdateSuppressor/master/icon.png
image: https://raw.githubusercontent.com/GiantBlargg/UpdateSuppressor/master/banner.png
layout: app
qr:
  UpdateSuppressor.cia: https://db.universal-team.net/assets/images/qr/updatesuppressor.cia.png
scripts:
  UpdateSuppressor.3dsx:
  - file: UpdateSuppressor-3dsx.zip
    message: Downloading UpdateSuppressor-3dsx.zip...
    output: /UpdateSuppressor-3dsx.zip
    repo: GiantBlargg/UpdateSuppressor
    type: downloadRelease
  - file: /UpdateSuppressor-3dsx.zip
    input: UpdateSuppressor/UpdateSuppressor.3dsx
    message: Extracting UpdateSuppressor.3dsx...
    output: '%3DSX%/UpdateSuppressor.3dsx'
    type: extractFile
  - file: /UpdateSuppressor-3dsx.zip
    message: Deleting UpdateSuppressor-3dsx.zip...
    type: deleteFile
source: https://github.com/GiantBlargg/UpdateSuppressor
systems:
- 3DS
title: UpdateSuppressor
update_notes: 'The CIA version will always run in delete-all mode.


  If the 3dsx version is installed with its xml file it will run in single delete
  mode. If the xml file is not present the 3dsx version will run in delete-all mode.

  '
updated: '2016-01-21T08:10:53Z'
version: v0.2.0
version_title: Delete all mode + CIA version
wiki: https://github.com/GiantBlargg/UpdateSuppressor/wiki
---
