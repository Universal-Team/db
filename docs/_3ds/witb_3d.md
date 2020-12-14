---
author: Manurocker95
autogen_scripts: true
categories:
- game
color: '#e98f7d'
created: '2017-04-16T16:13:10Z'
description: Small Game for 3DS in C++
download_page: https://github.com/Manurocker95/WITB_3D/releases/tag/1.1
downloads:
  WITB_3D.cia:
    size: 4899776
    url: https://github.com/Manurocker95/WITB_3D/releases/download/1.1/WITB_3D.cia
  WITB_3D.rar:
    size: 5982710
    url: https://github.com/Manurocker95/WITB_3D/releases/download/1.1/WITB_3D.rar
github: Manurocker95/WITB_3D
icon: https://raw.githubusercontent.com/Manurocker95/WITB_3D/master/WITB_3D/icon.png
image: https://raw.githubusercontent.com/Manurocker95/WITB_3D/master/WITB_3D/resources/banner.png
layout: app
qr:
  WITB_3D.cia: https://db.universal-team.net/assets/images/qr/witb_3d.cia.png
scripts:
  WITB_3D.3dsx:
  - message: UU is unable to extract this at the moment...
    type: promptMessage
  - type: exit
  - file: WITB_3D.rar
    message: Downloading WITB_3D.rar...
    output: /WITB_3D.rar
    repo: Manurocker95/WITB_3D
    type: downloadRelease
  - file: /WITB_3D.rar
    input: WITB_3D.3dsx
    message: Extracting WITB_3D.3dsx...
    output: '%3DSX%/WITB_3D.3dsx'
    type: extractFile
  - file: /WITB_3D.rar
    message: Deleting WITB_3D.rar...
    type: deleteFile
source: https://github.com/Manurocker95/WITB_3D
systems:
- 3DS
title: WITB_3D
update_notes: '<ul>

  <li>

  <p>New .sav mode in /3ds/data/WITB. If .sav doesn''t exists, the game checks if
  the file "witbdata.txt" exists in the root of the sd card to read the taps. (Just
  for debugging) It creates the .sav for taps.</p>

  </li>

  <li>

  <p>You can now save taps pressing START whenever you want.</p>

  </li>

  <li>

  <p>Removed 3D Stereoscopic (cz for this is not needed) and tap sound (Seems it was
  the reason for the freezing)</p>

  </li>

  </ul>'
updated: '2017-04-17T18:32:57Z'
version: '1.1'
version_title: Release 1.1 - Freeze Fix
wiki: https://github.com/Manurocker95/WITB_3D/wiki
---
