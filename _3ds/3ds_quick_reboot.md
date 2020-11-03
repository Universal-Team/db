---
author: Asellus
categories:
- utility
color: '#42b76e'
created: '2016-05-15T07:49:07Z'
description: 3DS Quick Reboot.
download_page: https://github.com/Asellus/3DS_Quick_Reboot/releases/tag/v1.0.1
downloads:
  3DSQuickReboot-v1.0.1.zip:
    size: 907497
    url: https://github.com/Asellus/3DS_Quick_Reboot/releases/download/v1.0.1/3DSQuickReboot-v1.0.1.zip
github: Asellus/3DS_Quick_Reboot
icon: https://raw.githubusercontent.com/Asellus/3DS_Quick_Reboot/master/resources/icon.png
image: https://raw.githubusercontent.com/Asellus/3DS_Quick_Reboot/master/resources/banner.png
layout: app
license: mit
license_name: MIT License
scripts:
  3DSQuickReboot.3dsx:
  - file: 3DSQuickReboot-.*\.zip
    message: Downloading 3DSQuickReboot zip...
    output: /3DSQuickReboot.zip
    repo: Asellus/3DS_Quick_Reboot
    type: downloadRelease
  - file: /3DSQuickReboot.zip
    input: 3ds/3DSQuickReboot/3DSQuickReboot.3dsx
    message: Extracting 3DSQuickReboot.3dsx...
    output: '%3DSX%/3DSQuickReboot.3dsx'
    type: extractFile
  - file: /3DSQuickReboot.zip
    message: Deleting 3DSQuickReboot.zip...
    type: deleteFile
  3DSQuickReboot.cia:
  - file: 3DSQuickReboot-.*\.zip
    message: Downloading 3DSQuickReboot zip...
    output: /3DSQuickReboot.zip
    repo: Asellus/3DS_Quick_Reboot
    type: downloadRelease
  - file: /3DSQuickReboot.zip
    input: 3DSQuickReboot.cia
    message: Extracting 3DSQuickReboot.cia...
    output: /3DSQuickReboot.cia
    type: extractFile
  - file: /3DSQuickReboot.cia
    message: Installing 3DSQuickReboot.cia...
    type: installCia
  - file: /3DSQuickReboot.cia
    message: Deleting 3DSQuickReboot.cia...
    type: deleteFile
  - file: /3DSQuickReboot.zip
    message: Deleting 3DSQuickReboot.zip...
    type: deleteFile
source: https://github.com/Asellus/3DS_Quick_Reboot
systems:
- 3DS
title: 3DS_Quick_Reboot
updated: '2016-05-18T11:55:39Z'
version: v1.0.1
version_title: 3DS Quick Reboot
wiki: https://github.com/Asellus/3DS_Quick_Reboot/wiki
---
