---
author: Ryuzaki-MrL
autogen_scripts: true
categories:
- utility
color: '#7abd9c'
created: '2016-04-18T06:36:04Z'
description: Homebrew Notification Manager for the Nintendo 3DS
download_page: https://github.com/Ryuzaki-MrL/NotifyMii/releases/tag/1.2
downloads:
  NotifyMii.cia:
    size: 491968
    url: https://github.com/Ryuzaki-MrL/NotifyMii/releases/download/1.2/NotifyMii.cia
  NotifyMii.zip:
    size: 1802585
    url: https://github.com/Ryuzaki-MrL/NotifyMii/releases/download/1.2/NotifyMii.zip
github: Ryuzaki-MrL/NotifyMii
icon: https://raw.githubusercontent.com/Ryuzaki-MrL/NotifyMii/master/meta/icon.png
image: https://raw.githubusercontent.com/Ryuzaki-MrL/NotifyMii/master/meta/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  NotifyMii.cia: https://db.universal-team.net/assets/images/qr/notifymii.cia.png
scripts:
  NotifyMii.3dsx:
  - file: NotifyMii.zip
    message: Downloading NotifyMii.zip...
    output: /NotifyMii.zip
    repo: Ryuzaki-MrL/NotifyMii
    type: downloadRelease
  - file: /NotifyMii.zip
    input: 3ds/NotifyMii/NotifyMii.3dsx
    message: Extracting NotifyMii.3dsx...
    output: '%3DSX%/NotifyMii.3dsx'
    type: extractFile
  - file: /NotifyMii.zip
    message: Deleting NotifyMii.zip...
    type: deleteFile
source: https://github.com/Ryuzaki-MrL/NotifyMii
systems:
- 3DS
title: NotifyMii
update_notes: "If everything's working then this will be my last release for now.\r\
  \n\r\nWhat's new:\r\n- Major UI changes.\r\n- Uses the 3DS's software keyboard.\r\
  \n- Support for viewing a notification's image.\r\n- Preview support for TXT and\
  \ JPG files.\r\n- Installed title list will now display all title's names alongside\
  \ their title ID.\r\n\r\nWhat's fixed:\r\n- Deleting a notification will no longer\
  \ mess with other notifications.\r\n- Max image filesize is now 50kb instead of\
  \ 128kb.\r\n\r\nWhat's next:\r\nThere are some leftovers of unimplemented stuff\
  \ in this release: Nintendo 3DS Camera support, notification editing, multi-selection,\
  \ and other stuff.\r\nThese were canceled and will be implemented into a future\
  \ release, which will have a GUI.\r\nHowever, it'll take some time as I don't plan\
  \ on working on this anytime soon.\r\n"
updated: '2016-05-24T15:23:21Z'
version: '1.2'
version_title: NotifyMii v1.2
wiki: https://github.com/Ryuzaki-MrL/NotifyMii/wiki
---
