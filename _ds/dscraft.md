---
author: smealum
categories:
- game
color: '#4b5327'
created: '2017-03-07T07:53:43Z'
description: minecraft adaptation for nintendo DS
download_page: https://web.archive.org/web/20160818124931/http://smealum.net/dscraft/
downloads:
  DScraft_310811.7z:
    url: https://db.universal-team.net/assets/files/DScraft_310811.7z
  DScraft_fat_310811.7z:
    url: https://db.universal-team.net/assets/files/DScraft_fat_310811.7z
github: smealum/dscraft
icon: https://db.universal-team.net/assets/images/icons/dscraft.png
image: https://raw.githubusercontent.com/smealum/dscraft/master/site/dscraft-logo.png
layout: app
scripts:
  DScraft.nds:
  - file: https://db.universal-team.net/assets/files/DScraft_310811.7z
    message: Downloading DScraft_310811.7z...
    output: /DScraft_310811.7z
    type: downloadFile
  - file: /DScraft_310811.7z
    input: DScraft.nds
    message: Extracting DScraft.nds...
    output: '%NDS%/DScraft.nds'
    type: extractFile
  - file: /DScraft_310811.7z
    input: dscraft/
    message: Extracting dscraft...
    output: '%NDS%/dscraft/'
    type: extractFile
  - file: /DScraft_310811.7z
    message: Deleting DScraft_310811.7z...
    type: deleteFile
  DScraft_fat.nds:
  - file: https://db.universal-team.net/assets/files/DScraft_fat_310811.7z
    message: Downloading DScraft_fat_310811.7z...
    output: /DScraft_fat_310811.7z
    type: downloadFile
  - file: /DScraft_fat_310811.7z
    input: DScraft_fat.nds
    message: Extracting DScraft_fat.nds...
    output: '%NDS%/DScraft_fat.nds'
    type: extractFile
  - file: /DScraft_fat_310811.7z
    input: dscraft
    message: Extracting dscraft...
    output: /dscraft/
    type: extractFile
  - file: /DScraft_fat_310811.7z
    message: Deleting DScraft_fat_310811.7z...
    type: deleteFile
source: https://github.com/smealum/dscraft
systems:
- DS
title: DScraft
updated: '2011-08-31T20:29:00Z'
version: v310811
website: https://web.archive.org/web/20160818124931/http://smealum.net/dscraft/
wiki: https://github.com/smealum/dscraft/wiki
---
