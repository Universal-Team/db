---
author: huiminghao / Coto
autogen_scripts: true
categories:
- emulator
color: '#b5774b'
created: '2019-02-22T22:33:39Z'
description: NesDS1.3c
download_page: https://github.com/DS-Homebrew/NesDS/tree/master/release
downloads:
  nesDS.nds:
    url: https://raw.githubusercontent.com/DS-Homebrew/NesDS/master/release/nesDS.nds
github: DS-Homebrew/NesDS
icon: https://raw.githubusercontent.com/DS-Homebrew/NesDS/master/icon.bmp
image: https://db.universal-team.net/assets/images/icons/nesds.png
layout: app
nightly:
  download_page: https://github.com/TWLBot/Builds/blob/master/extras/GodMode9i.7z
  downloads:
    nesDS.7z:
      url: https://github.com/TWLBot/Builds/raw/master/extras/nesDS.7z
scripts:
  '[nightly] nesDS.cia':
  - file: https://github.com/TWLBot/Builds/raw/master/extras/nesDS.7z
    message: Downloading nesDS.7z...
    output: /nesDS.7z
    type: downloadFile
  - file: /nesDS.7z
    input: nesDS/nesDS.cia
    message: Extracting nesDS.cia...
    output: /nesDS.cia
    type: extractFile
  - file: /nesDS.cia
    message: Installing nesDS.cia...
    type: installCia
  - file: /nesDS.cia
    message: Deleting nesDS.cia...
    type: deleteFile
  - file: /nesDS.7z
    message: Deleting nesDS.7z...
    type: deleteFile
  '[nightly] nesDS.nds':
  - file: https://github.com/TWLBot/Builds/raw/master/extras/nesDS.7z
    message: Downloading nesDS.7z...
    output: /nesDS.7z
    type: downloadFile
  - file: /nesDS.7z
    input: nesDS/nesDS.nds
    message: Extracting nesDS.nds...
    output: '%NDS%/nesDS.nds'
    type: extractFile
  - file: /nesDS.7z
    message: Deleting nesDS.7z...
    type: deleteFile
source: https://github.com/DS-Homebrew/NesDS
systems:
- DS
title: nesDS
updated: '2018-10-19T22:09:05Z'
version: v1.3c
wiki: https://github.com/DS-Homebrew/NesDS/wiki
---
