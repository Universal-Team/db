---
author: Ryuzaki-MrL
categories:
- utility
color: '#b4ac70'
created: '2016-07-13T17:16:45Z'
description: RomFS file explorer and dumper for Nintendo 3DS titles
download_page: https://github.com/Ryuzaki-MrL/RomFS-Explorer/releases/tag/v1.0.1
downloads:
  RomFSExplorer.zip:
    size: 1093834
    url: https://github.com/Ryuzaki-MrL/RomFS-Explorer/releases/download/v1.0.1/RomFSExplorer.zip
github: Ryuzaki-MrL/RomFS-Explorer
icon: https://raw.githubusercontent.com/Ryuzaki-MrL/RomFS-Explorer/master/meta/icon.png
image: https://raw.githubusercontent.com/Ryuzaki-MrL/RomFS-Explorer/master/meta/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  RomFSExplorer.3dsx:
  - file: RomFSExplorer.zip
    message: Downloading RomFSExplorer.zip...
    output: /RomFSExplorer.zip
    repo: Ryuzaki-MrL/RomFS-Explorer
    type: downloadRelease
  - file: /RomFSExplorer.zip
    input: 3ds/RomFSExplorer/RomFSExplorer.3dsx
    message: Extracting RomFSExplorer.3dsx...
    output: '%3DSX%/RomFSExplorer.3dsx'
    type: extractFile
  - file: /RomFSExplorer.zip
    message: Deleting RomFSExplorer.zip...
    type: deleteFile
  RomFSExplorer.cia:
  - file: RomFSExplorer.zip
    message: Downloading RomFSExplorer.zip...
    output: /RomFSExplorer.zip
    repo: Ryuzaki-MrL/RomFS-Explorer
    type: downloadRelease
  - file: /RomFSExplorer.zip
    input: RomFSExplorer.cia
    message: Extracting RomFSExplorer.cia...
    output: /RomFSExplorer.cia
    type: extractFile
  - file: /RomFSExplorer.cia
    message: Installing RomFSExplorer.cia...
    type: installCia
  - file: /RomFSExplorer.cia
    message: Deleting RomFSExplorer.cia...
    type: deleteFile
  - file: /RomFSExplorer.zip
    message: Deleting RomFSExplorer.zip...
    type: deleteFile
source: https://github.com/Ryuzaki-MrL/RomFS-Explorer
systems:
- 3DS
title: RomFS-Explorer
updated: '2016-09-23T00:16:29Z'
version: v1.0.1
version_title: Hotfix release
wiki: https://github.com/Ryuzaki-MrL/RomFS-Explorer/wiki
---
