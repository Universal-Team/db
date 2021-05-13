---
author: Steveice10
avatar: https://avatars.githubusercontent.com/u/1269164?v=4
categories:
- utility
color: '#c0d0ff'
created: '2015-01-20T04:23:49Z'
description: Open source title manager for the 3DS.
download_page: https://github.com/Steveice10/FBI/releases
downloads:
  FBI.3dsx:
    size: 1133148
    size_str: 1 MiB
    url: https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.3dsx
  FBI.cia:
    size: 1151936
    size_str: 1 MiB
    url: https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.cia
  FBI.zip:
    size: 4128978
    size_str: 3 MiB
    url: https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.zip
github: Steveice10/FBI
icon: https://raw.githubusercontent.com/Steveice10/FBI/master/meta/icon_3ds.png
image: https://raw.githubusercontent.com/Steveice10/FBI/master/romfs/logo.png
image_length: 573
layout: app
license: mit
license_name: MIT License
qr:
  FBI.cia: https://db.universal-team.net/assets/images/qr/fbi.cia.png
screenshots:
- description: Main menu
  url: https://db.universal-team.net/assets/images/screenshots/fbi/main-menu.png
- description: Qr scanner
  url: https://db.universal-team.net/assets/images/screenshots/fbi/qr-scanner.png
- description: Sd list
  url: https://db.universal-team.net/assets/images/screenshots/fbi/sd-list.png
source: https://github.com/Steveice10/FBI
systems:
- 3DS
title: FBI
update_notes: '<ul>

  <li>Remove TitleDB support.</li>

  <li>Add TLSv1.2 support.

  <ul>

  <li>In testing, speeds were ~70-80kbps, which should be good enough for homebrew
  downloads.

  <ul>

  <li>I hope to investigate the matter further and improve speeds in the future, but
  wanted to finally get something out for the time being.</li>

  </ul>

  </li>

  <li>Downloads from sources that support earlier TLS versions (i.e. not GitHub) will
  continue to use the 3DS''s built-in HTTP stack, and thus should progress at the
  same speeds as before.</li>

  </ul>

  </li>

  <li>Revert the built-in updater back to using GitHub.</li>

  </ul>'
updated: '2019-01-02T01:41:35Z'
version: 2.6.0
version_title: 2.6.0
---
