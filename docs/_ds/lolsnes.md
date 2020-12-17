---
author: Arisotura
categories:
- emulator
color: '#7c9187'
created: '2013-08-02T12:14:31Z'
description: SNES emulator for DS
download_page: http://lolsnes.kuribo64.net/download.php
downloads:
  lolsnes.7z:
    url: http://lolsnes.kuribo64.net/lolsnes.7z
github: Arisotura/lolSnes
icon: https://raw.githubusercontent.com/Arisotura/lolSnes/master/lolsnes.bmp
image: https://db.universal-team.net/assets/images/images/lolsnes.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: http://lolsnes.kuribo64.net/download.php
  downloads:
    git_b1ddc811030fe2a3ef3e97187f0eeec4a4b3e353.zip:
      url: http://lolsnes.kuribo64.net/gitbuilds/git_b1ddc811030fe2a3ef3e97187f0eeec4a4b3e353.zip
scripts:
  '[nightly] lolSnes.nds':
  - file: http://lolsnes.kuribo64.net/gitbuilds/git_b1ddc811030fe2a3ef3e97187f0eeec4a4b3e353.zip
    message: Downloading lolsnes zip...
    output: /lolsnes.zip
    type: downloadFile
  - file: /lolsnes.zip
    input: lolSnes.nds
    message: Extracting lolSnes.nds...
    output: '%NDS%/lolSnes.nds'
    type: extractFile
  - file: /lolsnes.zip
    message: Deleting lolsnes.zip...
    type: deleteFile
  lolSnes.nds:
  - file: http://lolsnes.kuribo64.net/lolsnes.7z
    message: Downloading lolsnes.7z...
    output: /lolsnes.7z
    type: downloadFile
  - file: /lolsnes.7z
    input: lolsnes/lolSnes.nds
    message: Extracting lolSnes.nds...
    output: '%NDS%/lolSnes.nds'
    type: extractFile
  - file: /lolsnes.7z
    message: Deleting lolsnes.7z...
    type: deleteFile
source: https://github.com/Arisotura/lolSnes
systems:
- DS
title: lolSnes
updated: '2013-08-31T00:23:48Z'
version: v1.0
website: http://lolsnes.kuribo64.net
wiki: https://github.com/Arisotura/lolSnes/wiki
---
