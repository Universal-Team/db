---
author: Nanquitas
categories:
- utility
color: '#7c626d'
created: '2016-04-21T14:02:23Z'
download_page: https://github.com/Nanquitas/BootNTR/releases/tag/v2.13.4
downloads:
  BootNTRSelector-FONZD-Banner.cia:
    size: 1508288
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-FONZD-Banner.cia
  BootNTRSelector-Mode3-FONZD-Banner.cia:
    size: 1508288
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-Mode3-FONZD-Banner.cia
  BootNTRSelector-Mode3-PabloMK7-Banner.cia:
    size: 1487808
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-Mode3-PabloMK7-Banner.cia
  BootNTRSelector-PabloMK7-Banner.3dsx:
    size: 1074176
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-PabloMK7-Banner.3dsx
  BootNTRSelector-PabloMK7-Banner.cia:
    size: 1487808
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-PabloMK7-Banner.cia
github: Nanquitas/BootNTR
icon: https://raw.githubusercontent.com/Nanquitas/BootNTR/master/resources/icon.png
image: https://db.universal-team.net/assets/images/images/bootntr.png
layout: app
license: mit
license_name: MIT License
qr:
  BootNTRSelector-FONZD-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-fonzd-banner.cia.png
  BootNTRSelector-Mode3-FONZD-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-mode3-fonzd-banner.cia.png
  BootNTRSelector-Mode3-PabloMK7-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-mode3-pablomk7-banner.cia.png
  BootNTRSelector-PabloMK7-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-pablomk7-banner.cia.png
source: https://github.com/Nanquitas/BootNTR
systems:
- 3DS
title: BootNTR
update_notes: "# This release is currently broken with official Luma3DS!\r\n You can\
  \ temporarily use the [Luma3DS 3GX Loader build](https://github.com/Nanquitas/Luma3DS/releases)\
  \ until this issue is addressed!\r\n[The official Luma memory mapping svc](https://github.com/LumaTeam/Luma3DS/blob/master/sysmodules/rosalina/include/csvc.h#L70-L79)\
  \ doesn't function properly when mapping single pages from other processes, which\
  \ causes BootNTR Selector to crash. In order to fix this issue either:\r\n1. BootNTR\
  \ Selector code must be adapted to this.\r\n2. Luma3DS must support mapping other\
  \ processes individual memory pages.\r\n\r\nWhile I'll try to implement solution\
  \ 1, I've decided to make this release as it will take some time to be implemented\
  \ due to lack of time irl. (I think it's better that the community has something\
  \ partially functional than nothing at all.) Once any of the solutions are implemented,\
  \ I'll update this release with the updated files, sorry for the inconvenience.\r\
  \n\r\n# Changelog\r\n- Added 11.14 support.\r\n- Adapted code to latest ctrulib,\
  \ no longer uses dma svcs to copy memory, so launching is way more stable.\r\n\r\
  \n# Filename meaning\r\nYou will find different files below depending on your needs.\
  \ Here is a little explanation on each term:\r\n## 3dsx/cia\r\nThe **3dsx** file\
  \ can be launched from the homebrew launcher while the cia files can be installed\
  \ to the home menu. (There is only a single 3dsx file variation.)\r\n## Mode3\r\n\
  Files which have the the **Mode3** label are made specifically for extended memory\
  \ games on Old 3DS/2DS models. (To detect if you are using an extended memory game,\
  \ check if the console reboots after you close it from the home menu.) **You don't\
  \ need to install the Mode3 version if you don't want to use any extended memory\
  \ game or you have a New 3DS/2DS.**\r\n## PabloMK7 / FONZD banner\r\nThe banner\
  \ is the 3D model that shows in the top screen when you select the app in the home\
  \ menu. The difference is only visual and is up to your own choice.\r\n\r\n### PabloMK7\
  \ Banner\r\n![image](https://user-images.githubusercontent.com/10946643/56131741-96b2c500-5f88-11e9-9af7-a81825505f5b.png)\r\
  \n\r\n### FONZD Banner\r\n![image](https://user-images.githubusercontent.com/10946643/56131768-afbb7600-5f88-11e9-8585-6ceb930424cc.png)\r\
  \n\r\n"
updated: '2020-11-23T12:27:12Z'
version: v2.13.4
wiki: https://github.com/Nanquitas/BootNTR/wiki
---
