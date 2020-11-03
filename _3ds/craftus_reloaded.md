---
author: RSDuck
autogen_scripts: true
categories:
- game
color: '#4e4f39'
created: '2017-08-11T14:40:48Z'
description: A second attempt at a homebrew Minecraft clone for 3DS
download_page: https://github.com/RSDuck/craftus_reloaded/releases/tag/0.22
downloads:
  craftus-0.22.cia:
    size: 582592
    url: https://github.com/RSDuck/craftus_reloaded/releases/download/0.22/craftus-0.22.cia
  craftus-0.22.zip:
    size: 686458
    url: https://github.com/RSDuck/craftus_reloaded/releases/download/0.22/craftus-0.22.zip
github: RSDuck/craftus_reloaded
icon: https://raw.githubusercontent.com/RSDuck/craftus_reloaded/master/icon/craftusreloaded.png
image: https://avatars3.githubusercontent.com/u/9352526?v=4
layout: app
license: other
license_name: Other
prerelease:
  download_page: https://github.com/RSDuck/craftus_reloaded/releases/tag/0.3-pre2
  downloads:
    craftusreloaded.3dsx:
      size: 471280
      url: https://github.com/RSDuck/craftus_reloaded/releases/download/0.3-pre2/craftusreloaded.3dsx
    craftusreloaded.cia:
      size: 590784
      url: https://github.com/RSDuck/craftus_reloaded/releases/download/0.3-pre2/craftusreloaded.cia
  updated: '2017-10-28T15:09:14Z'
  version: 0.3-pre2
  version_title: 0.3 Pre 2 Second Pre Release
qr:
  craftus-0.22.cia: https://db.universal-team.net/assets/images/qr/craftus-0.22.cia.png
scripts:
  craftusreloaded.3dsx:
  - file: craftus.*\.zip
    message: Downloading craftus.zip...
    output: /craftus.zip
    repo: RSDuck/craftus_reloaded
    type: downloadRelease
  - file: /craftus.zip
    input: craftusreloaded.3dsx
    message: Extracting craftusreloaded.3dsx...
    output: '%3DSX%/craftusreloaded.3dsx'
    type: extractFile
  - file: /craftus.zip
    message: Deleting craftus.zip...
    type: deleteFile
source: https://github.com/RSDuck/craftus_reloaded
systems:
- 3DS
title: craftus_reloaded
updated: '2017-08-23T14:03:18Z'
version: '0.22'
version_title: '0.22'
wiki: https://github.com/RSDuck/craftus_reloaded/wiki
---
