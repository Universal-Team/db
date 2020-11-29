---
author: CTurt
categories:
- utility
color: '#939393'
created: '2014-12-05T16:52:25Z'
download_page: https://github.com/CTurt/3DSController/releases/tag/0.6
downloads:
  3DSController0.6.zip:
    size: 702073
    url: https://github.com/CTurt/3DSController/releases/download/0.6/3DSController0.6.zip
github: CTurt/3DSController
icon: https://raw.githubusercontent.com/CTurt/3DSController/master/3DS/cxi/icon48x48.png
image: https://raw.githubusercontent.com/CTurt/3DSController/master/3DS/cxi/banner.png
layout: app
scripts:
  3DSController.3dsx:
  - file: 3DSController.*\.zip
    message: Downloading 3DSController zip...
    output: /3DSController.zip
    repo: CTurt/3DSController
    type: downloadRelease
  - file: /3DSController.zip
    input: 3DS/3DSController.3dsx
    message: Extracting 3DSController.3dsx...
    output: '%3DSX%/3DSController.3dsx'
    type: extractFile
  - file: /3DSController.zip
    input: 3DS/3DSController.ini
    message: Extracting 3DSController.ini...
    output: /3DSController.ini
    type: extractFile
  - file: /3DSController.zip
    message: Deleting 3DSController.zip...
    type: deleteFile
  3DSController.cia:
  - file: 3DSController.*\.zip
    message: Downloading 3DSController zip...
    output: /3DSController.zip
    repo: CTurt/3DSController
    type: downloadRelease
  - file: /3DSController.zip
    input: 3DS/3DSController.cia
    message: Extracting 3DSController.cia...
    output: /3DSController.cia
    type: extractFile
  - file: /3DSController.zip
    input: 3DS/3DSController.ini
    message: Extracting 3DSController.ini...
    output: /3DSController.ini
    type: extractFile
  - file: /3DSController.cia
    message: Installing 3DSController.cia...
    type: installCia
  - file: /3DSController.cia
    message: Deleting 3DSController.cia...
    type: deleteFile
  - file: /3DSController.zip
    message: Deleting 3DSController.zip...
    type: deleteFile
source: https://github.com/CTurt/3DSController
systems:
- 3DS
title: 3DSController
update_notes: '3DS Client:

  - Backlight disabled when not in use (less battery consumption),

  - New 3DS buttons and C Stick support,


  PC Server:

  - DLL errors fixed,

  - Updated vJoy to latest version (fixes Windows 10 compatibility),

  - Screenshot code scrapped

  - 2 separate JoySticks can be configured,

  - 8 additional JoyStick buttons supported,

  '
updated: '2015-09-08T22:08:00Z'
version: '0.6'
version_title: 3DS Controller 0.6
wiki: https://github.com/CTurt/3DSController/wiki
---
