---
author: Trinitro21
autogen_scripts: true
categories:
- utility
color: '#82846c'
created: '2016-03-19T01:42:21Z'
description: SmileBASIC File Manager
download_page: https://github.com/Trinitro21/lpp-3ds/releases/tag/sbfm1.7
downloads:
  sbfm.cia:
    size: 1627072
    url: https://github.com/Trinitro21/lpp-3ds/releases/download/sbfm1.7/sbfm.cia
  sbfm.zip:
    size: 1112262
    url: https://github.com/Trinitro21/lpp-3ds/releases/download/sbfm1.7/sbfm.zip
github: Trinitro21/lpp-3ds
icon: https://raw.githubusercontent.com/Trinitro21/lpp-3ds/sbfm/icon.png
image: https://db.universal-team.net/assets/images/images/lpp-3ds.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  sbfm.cia: https://db.universal-team.net/assets/images/qr/sbfm.cia.png
scripts:
  sbfm.3dsx:
  - file: sbfm.zip
    message: Downloading sbfm.zip...
    output: /sbfm.zip
    repo: Trinitro21/lpp-3ds
    type: downloadRelease
  - file: /sbfm.zip
    input: sbfm.3dsx
    message: Extracting sbfm.3dsx...
    output: '%3DSX%/sbfm.3dsx'
    type: extractFile
  - file: /sbfm.zip
    message: Deleting sbfm.zip...
    type: deleteFile
source: https://github.com/Trinitro21/lpp-3ds
systems:
- 3DS
title: lpp-3ds
update_notes: '<ul>

  <li>Added footer signing using the SHA1-HMAC algorithm</li>

  <li>Fixed the crash that occurs when the "copy DAT contents" function is invoked
  on a file that doesn''t evenly divide into the size of the data type</li>

  </ul>'
updated: '2019-05-08T20:03:37Z'
version: sbfm1.7
version_title: SmileBASIC File Manager v1.7
wiki: https://github.com/Trinitro21/lpp-3ds/wiki
---
