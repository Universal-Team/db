---
author: LumaTeam
categories:
- utility
- firm
color: '#82e5d9'
created: '2016-02-08T02:26:12Z'
description: Noob-proof (N)3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases/tag/v10.2
downloads:
  Luma3DSv10.2.zip:
    size: 359574
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v10.2/Luma3DSv10.2.zip
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
  '[plugin loader] boot.firm':
  - file: boot.firm
    message: Downloading boot.firm...
    output: /boot.firm
    repo: jbmagination/Luma3DS_plg
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
updated: '2020-07-16T17:33:28Z'
version: v10.2
version_title: v10.2
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
