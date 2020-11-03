---
author: MrHuu
categories:
- game
color: '#683a2b'
created: '2018-12-23T19:36:03Z'
description: 'A port of the game engine behind the DOS versions of Titus the Fox and
  Moktar '
download_page: https://github.com/MrHuu/opentitus-3ds/releases/tag/27-12-2018
downloads:
  OpenTitus_MOKTAR_LOW_FREQ_27-12-2018.7z:
    size: 1044734
    url: https://github.com/MrHuu/opentitus-3ds/releases/download/27-12-2018/OpenTitus_MOKTAR_LOW_FREQ_27-12-2018.7z
  OpenTitus_TITUS_LOW_FREQ_27-12-2018.7z:
    size: 1041305
    url: https://github.com/MrHuu/opentitus-3ds/releases/download/27-12-2018/OpenTitus_TITUS_LOW_FREQ_27-12-2018.7z
github: MrHuu/opentitus-3ds
icon: https://raw.githubusercontent.com/MrHuu/opentitus-3ds/3DS/3ds/Titus_icon_48x48.png
image: https://raw.githubusercontent.com/MrHuu/opentitus-3ds/3DS/3ds/Titus_banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  '[moktar] OpenTitus.cia':
  - count: 2
    message: Are you on a New 3DS/2DS?
    type: promptMessage
  - file: https://github.com/MrHuu/opentitus-3ds/releases/download/25-12-2028/OpenTitus_MOKTAR_CIA_25-12-2018.7z
    message: Downloading OpenTitus 7z...
    output: /OpenTitus.7z
    type: downloadFile
  - count: 1
    type: skip
  - file: OpenTitus_MOKTAR.*\.7z
    message: Downloading OpenTitus 7z...
    output: /OpenTitus.7z
    repo: MrHuu/opentitus-3ds
    type: downloadRelease
  - file: /OpenTitus.7z
    input: OpenTitus/
    message: Extracting OpenTitus...
    output: /3ds/OpenTitus/
    type: extractFile
  - file: /3ds/OpenTitus/OpenTitus.cia
    message: Installing OpenTitus.cia...
    type: installCia
  - file: /3ds/OpenTitus/OpenTitus.cia
    message: Deleting OpenTitus.cia...
    type: deleteFile
  - file: /OpenTitus.7z
    message: Deleting OpenTitus.7z...
    type: deleteFile
  '[titus] OpenTitus.cia':
  - count: 2
    message: Are you on a New 3DS/2DS?
    type: promptMessage
  - file: https://github.com/MrHuu/opentitus-3ds/releases/download/25-12-2028/OpenTitus_TITUS_CIA_25-12-2018.7z
    message: Downloading OpenTitus 7z...
    output: /OpenTitus.7z
    type: downloadFile
  - count: 1
    type: skip
  - file: OpenTitus_TITUS.*\.7z
    message: Downloading OpenTitus 7z...
    output: /OpenTitus.7z
    repo: MrHuu/opentitus-3ds
    type: downloadRelease
  - file: /OpenTitus.7z
    input: OpenTitus/
    message: Extracting OpenTitus...
    output: /3ds/OpenTitus/
    type: extractFile
  - file: /3ds/OpenTitus/OpenTitus.cia
    message: Installing OpenTitus.cia...
    type: installCia
  - file: /3ds/OpenTitus/OpenTitus.cia
    message: Deleting OpenTitus.cia...
    type: deleteFile
  - file: /OpenTitus.7z
    message: Deleting OpenTitus.7z...
    type: deleteFile
source: https://github.com/MrHuu/opentitus-3ds
systems:
- 3DS
title: opentitus-3ds
updated: '2018-12-27T00:34:34Z'
version: 27-12-2018
wiki: https://github.com/MrHuu/opentitus-3ds/wiki
---
