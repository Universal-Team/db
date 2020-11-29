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
update_notes: '<p>If everything''s working then this will be my last release for now.</p>

  <p>What''s new:</p>

  <ul>

  <li>Major UI changes.</li>

  <li>Uses the 3DS''s software keyboard.</li>

  <li>Support for viewing a notification''s image.</li>

  <li>Preview support for TXT and JPG files.</li>

  <li>Installed title list will now display all title''s names alongside their title
  ID.</li>

  </ul>

  <p>What''s fixed:</p>

  <ul>

  <li>Deleting a notification will no longer mess with other notifications.</li>

  <li>Max image filesize is now 50kb instead of 128kb.</li>

  </ul>

  <p>What''s next:<br>

  There are some leftovers of unimplemented stuff in this release: Nintendo 3DS Camera
  support, notification editing, multi-selection, and other stuff.<br>

  These were canceled and will be implemented into a future release, which will have
  a GUI.<br>

  However, it''ll take some time as I don''t plan on working on this anytime soon.</p>'
updated: '2016-05-24T15:23:21Z'
version: '1.2'
version_title: NotifyMii v1.2
wiki: https://github.com/Ryuzaki-MrL/NotifyMii/wiki
---
