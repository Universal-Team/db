---
author: hax0kartik
categories:
- utility
color: '#411d38'
created: '2020-08-20T12:36:12Z'
description: Amiibo Emulation for 3ds
download_page: https://github.com/hax0kartik/wumiibo/releases/tag/v2.0
downloads:
  0004013000004002.zip:
    size: 42617
    url: https://github.com/hax0kartik/wumiibo/releases/download/v2.0/0004013000004002.zip
github: hax0kartik/wumiibo
image: https://avatars0.githubusercontent.com/u/16360444?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  wumiibo:
  - file: 0004013000004002.zip
    message: Downloading 0004013000004002.zip...
    output: /0004013000004002.zip
    repo: hax0kartik/wumiibo
    type: downloadRelease
  - file: /0004013000004002.zip
    input: 0004013000004002/
    message: Extracting 0004013000004002...
    output: /luma/titles/0004013000004002/
    type: extractFile
  - file: /0004013000004002.zip
    message: Deleting 0004013000004002.zip...
    type: deleteFile
source: https://github.com/hax0kartik/wumiibo
systems:
- 3DS
title: wumiibo
update_notes: "This is the third public release for wumiibo.\r\nFollowing list of\
  \ changes has been made. \r\n * Proper UID assignment and UID Randomization has\
  \ been added. \r\n    *  Wumiibo no longer uses a hardcoded UID for every amiibo.\
  \ It automatically assigns a new UID to every amiibo.\r\n    *  Some games limit\
  \ users to only one scan of a specific amiibo per 24 hours. By randomizing an amiibo's\
  \ UID you can overcome this limit. \r\n      **NOTE**:- This depends on the game's\
  \ logic, and may not work with every title. \r\n\r\n* Default wumiibo menu button\
  \ can now be overridden.\r\n  *  This can be done by creating a `wumiibo.ini` file\
  \ on the root of your sd card. A sample of this file is [here](https://github.com/hax0kartik/wumiibo/blob/master/wumiibo.ini).\r\
  \n\r\n* DirectoryLister code has been improved.\r\n  *  You can now have upto `49`\
  \ folders within the `wumiibo` folder. Inside every folder you can have even more\
  \ subfolders or amiibos. So if you create your folders properly, there is virtually\
  \ no limit on how many amiibos you can have at a time.\r\n  *  As a bonus feature,\
  \ if you want to have a dedicated folder for a game, you can give a folder the game's\
  \ TitleID and put all relevant amiibos in there. For example, for Super Smash Bros\
  \ EUR, you can create a folder `sd:/wumiibo/00040000000EE000` and put the amiibos\
  \ in there. Wumiibo will automatically open this folder in-game.\r\n\r\n* Various\
  \ bugs have been fixed and minor improvements have been made. \r\n\r\nIf this the\
  \ first time you're installing wumiibo, you can follow the instruction in the readme\
  \ [here](https://github.com/hax0kartik/wumiibo/blob/master/Readme.md).\r\n\r\nAs\
  \ of writing 42 out of 47 know games that have amiibo capabalities are known to\
  \ work. You can check the compatibility list [here](https://github.com/hax0kartik/wumiibo/wiki/Compatibility-List).\r\
  \n\r\nMassive thanks to Marcus7777, druivensap, Love Leiz and Graymar on my discord\
  \ server for helping me test out the games, wouldn't been possible without you guys!\r\
  \n\r\nIf you like my work, you can support me by buying me a coffee on [ko-fi](https://ko-fi.com/hax0kartik)\
  \ or you can [paypal](https://www.paypal.com/paypalme/preetiagarwala?locale.x=en_GB)\
  \ me!\r\n\r\n"
updated: '2020-09-24T18:30:26Z'
version: v2.0
version_title: v2.0 Third Release
wiki: https://github.com/hax0kartik/wumiibo/wiki
---
