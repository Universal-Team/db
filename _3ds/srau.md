---
author: noirscape
autogen_scripts: true
categories:
- utility
- save-tool
color: '#ddbca2'
created: '2018-04-08T18:03:47Z'
description: 'Samus Returns: Amiibo Unlocker'
download_page: https://github.com/noirscape/SRAU/releases/tag/v1.1
downloads:
  SRAU.7z:
    size: 556954
    url: https://github.com/noirscape/SRAU/releases/download/v1.1/SRAU.7z
  SRAU.cia:
    size: 582592
    url: https://github.com/noirscape/SRAU/releases/download/v1.1/SRAU.cia
github: noirscape/SRAU
icon: https://raw.githubusercontent.com/noirscape/SRAU/master/meta/icon.png
image: https://raw.githubusercontent.com/noirscape/SRAU/master/meta/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  SRAU.cia: https://db.universal-team.net/assets/images/qr/srau.cia.png
scripts:
  SRAU.3dsx:
  - file: SRAU.7z
    message: Downloading SRAU.7z...
    output: /SRAU.7z
    repo: noirscape/SRAU
    type: downloadRelease
  - file: /SRAU.7z
    input: SRAU.3dsx
    message: Extracting SRAU.3dsx...
    output: '%3DSX%/SRAU.3dsx'
    type: extractFile
  - file: /SRAU.7z
    message: Deleting SRAU.7z...
    type: deleteFile
source: https://github.com/noirscape/SRAU
systems:
- 3DS
title: SRAU
update_notes: "This release mostly adds in a lot of missing error checks and adds\
  \ in gamecard support + support for mismatched regions.\r\n\r\nThis release would\
  \ not have been possible without the help of @Sonlen1414 .\r\n\r\n![QR code](https://user-images.githubusercontent.com/13433513/38756013-40d03e2e-3f68-11e8-96cb-83704530de74.gif)\r\
  \n\r\n\r\nChanges:\r\n- Closes #1 (no gamecard support). Thanks to astronautlevel\
  \ for the bug report and Sonlen for testing my fixes. If a gamecard is found, it\
  \ is chosen over any local installation.\r\n- Closes #2 (no support for mismatched\
  \ regions). Thanks to astronautlevel for this bug report. You are now prompted if\
  \ the program detects multiple regions. If there is only one region, it is autodetected\
  \ and you are not prompted.\r\n- Closes #4 (no support for missing save files).\
  \ The program only allows you to choose existing save files. If there is only one\
  \ save file, it is autodetected and you are not prompted to select a save file.\r\
  \n- Restart functionality! You can at any point now press the L button to restart\
  \ the entire process. Useful if you selected the wrong save file or region.\r\n\
  - Savedata readouts! After selecting a save file, the program now reads out the\
  \ current state of the save file and shows it on the bottom left screen.\r\n- Cleaner\
  \ interface! The main text prompts by the program are now dedicated on the top screen.\
  \ The bottom screen now contains a list of save data info on the left and a list\
  \ of your choices made in the program on the right (this include autodetection).\r\
  \n\r\nUnder the hood changes (you probably don't care about this but for my own\
  \ memory it's here):\r\n- Loads and loads. Really, I've rewritten about 90% of the\
  \ program logic except for the ctrulib function calls themselves.\r\n- No more if\
  \ blocks. The entirety of the state machine is now handled with a `switch`.\r\n\
  - Got rid of editprofile.c completely and split it up into various functions inside\
  \ save.c with lowid selection getting moved to title.c.\r\n- Dedicated failure state\
  \ that is separate from SUCCES state."
updated: '2018-04-13T20:16:16Z'
version: v1.1
version_title: Release v1.1
website: https://discord.gg/Q6jmQcV
wiki: https://github.com/noirscape/SRAU/wiki
---
