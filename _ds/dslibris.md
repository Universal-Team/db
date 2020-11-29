---
author: rhaleblian
categories:
- utility
color: '#202020'
created: '2017-11-11T17:53:30Z'
description: An ebook reader for the Nintendo DS, DS Lite, and DSi.
download_page: https://github.com/rhaleblian/dslibris/releases/tag/v1.5.1
downloads:
  dslibris-1.5.1.zip:
    size: 3349848
    url: https://github.com/rhaleblian/dslibris/releases/download/v1.5.1/dslibris-1.5.1.zip
github: rhaleblian/dslibris
icon: https://raw.githubusercontent.com/rhaleblian/dslibris/master/gfx/icon.bmp
image: https://avatars1.githubusercontent.com/u/94912?v=4
layout: app
scripts:
  dslibris.nds:
  - file: dslibris.*\.zip
    message: Downloading dslibris.zip...
    output: /dslibris.zip
    repo: rhaleblian/dslibris
    type: downloadRelease
  - file: /dslibris.zip
    input: ''
    message: Extracting dslibris...
    output: /
    type: extractFile
  - message: Moving dslibris.nds...
    new: '%NDS%/dslibris.nds'
    old: /dslibris.nds
    type: move
  - file: /INSTALL.txt
    message: Deleting INSTALL.txt...
    type: deleteFile
  - file: /dslibris.zip
    message: Deleting dslibris.zip...
    type: deleteFile
source: https://github.com/rhaleblian/dslibris
systems:
- DS
title: dslibris
update_notes: "Version v1.5.0 rebuilt with devkitARM r45.\r\n\r\nAs such, there are\
  \ no new features or changes in application behaviour.\r\n\r\nSee INSTALL.txt for\
  \ installation instructions.\r\n"
updated: '2018-11-23T01:58:57Z'
version: v1.5.1
version_title: v1.5.1
website: https://rhaleblian.wordpress.com/dslibris-an-ebook-reader-for-the-nintendo-ds/
wiki: https://github.com/rhaleblian/dslibris/wiki
---
