---
author: LumaTeam
categories:
- utility
- firm
- luma3ds
color: '#82e5d9'
created: '2016-02-08T02:26:12Z'
description: Noob-proof (N)3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases/tag/v10.2.1
downloads:
  Luma3DSv10.2.1.zip:
    size: 364996
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v10.2.1/Luma3DSv10.2.1.zip
github: LumaTeam/Luma3DS
image: https://avatars3.githubusercontent.com/u/65085206?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  '[hourly] boot.firm':
  - file: boot.firm
    message: Downloading boot.firm...
    output: /boot.firm
    repo: hax0kartik/luma-hourlies
    type: downloadRelease
  boot.firm:
  - file: Luma3DS.*.zip
    message: Downloading Luma3DS zip...
    output: /Luma3DS.zip
    repo: LumaTeam/Luma3DS
    type: downloadRelease
  - file: /Luma3DS.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: /Luma3DS.zip
    message: Deleting Luma3DS.zip...
    type: deleteFile
source: https://github.com/LumaTeam/Luma3DS
systems:
- 3DS
title: Luma3DS
update_notes: "* **Fix system version 11.14 not booting**\r\n* Allow out-of-region\
  \ Download Play functionality (thanks @Pixel-Pop)\r\n* Fix a rare issue where the\
  \ Rosalina Menu wouldn't be displayed during application launch (thanks @Nanquitas)\r\
  \n* General system stability improvements to enhance the user's experience"
updated: '2020-11-17T02:06:56Z'
version: v10.2.1
version_title: v10.2.1
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
