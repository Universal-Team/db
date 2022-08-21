---
author: N•I•L
avatar: https://avatars.githubusercontent.com/u/70803115?v=4
categories:
- utility
color: '#c0a28a'
color_bg: '#806c5c'
created: '2021-01-27T13:49:42Z'
description: Flipnote Studio Player for Nintendo DS
download_page: https://github.com/NotImplementedLife/FSPDS/releases
downloads:
  FSPDS-V0-2-1.zip:
    size: 111871
    size_str: 109 KiB
    url: https://github.com/NotImplementedLife/FSPDS/releases/download/V0.2.1/FSPDS-V0-2-1.zip
github: NotImplementedLife/FSPDS
icon: https://db.universal-team.net/assets/images/icons/fspds.png
image: https://db.universal-team.net/assets/images/icons/fspds.png
image_length: 586
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/NotImplementedLife/FSPDS/releases/tag/V0.3.41164628D
  downloads:
    FSPDS-V0.3.41164628D.nds:
      size: 235520
      size_str: 230 KiB
      url: https://github.com/NotImplementedLife/FSPDS/releases/download/V0.3.41164628D/FSPDS-V0.3.41164628D.nds
  qr:
    FSPDS-V0.3.41164628D.nds: https://db.universal-team.net/assets/images/qr/prerelease/fspds-v0-3-41164628d-nds.png
  update_notes: '<p dir="auto">FSPDS now looks for flipnotes in official Flipnote
    Studio paths from the SD card:</p>

    <ul dir="auto">

    <li>/private/ds/app/4b475556 - for Flipnote Studio Europe/Australia</li>

    <li>/private/ds/app/4B475545 - for Flipnote Studio Americas</li>

    <li>/private/ds/app/4B47554A - for Flipnote Studio Japan</li>

    </ul>

    <p dir="auto">The directories are detected automatically based on whether they
    exist on the SD card. The user can choose which path to look in for flipnotes.</p>

    <p dir="auto">Pressing B on the "Files" tab displays the Path menu in case user
    wants to inspect another directory</p>

    <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/70803115/169023464-eb05000c-0c7c-4904-afed-96b54e13e17e.png"><img
    src="https://user-images.githubusercontent.com/70803115/169023464-eb05000c-0c7c-4904-afed-96b54e13e17e.png"
    alt="Screenshot" style="max-width: 100%;"></a></p>'
  update_notes_md: "FSPDS now looks for flipnotes in official Flipnote Studio paths\
    \ from the SD card:\n - /private/ds/app/4b475556 - for Flipnote Studio Europe/Australia\n\
    \ - /private/ds/app/4B475545 - for Flipnote Studio Americas\n - /private/ds/app/4B47554A\
    \ - for Flipnote Studio Japan\n\nThe directories are detected automatically based\
    \ on whether they exist on the SD card. The user can choose which path to look\
    \ in for flipnotes.\n\nPressing B on the \"Files\" tab displays the Path menu\
    \ in case user wants to inspect another directory\n\n\n![Screenshot](https://user-images.githubusercontent.com/70803115/169023464-eb05000c-0c7c-4904-afed-96b54e13e17e.png)\n\
    \n"
  updated: '2022-05-18T07:47:22Z'
  version: V0.3.41164628D
  version_title: FSPDS V0.3.41164628D
screenshots:
- description: File list
  url: https://db.universal-team.net/assets/images/screenshots/fspds/file-list.png
- description: Player 1
  url: https://db.universal-team.net/assets/images/screenshots/fspds/player-1.png
- description: Player 2
  url: https://db.universal-team.net/assets/images/screenshots/fspds/player-2.png
source: https://github.com/NotImplementedLife/FSPDS
systems:
- DS
title: FSPDS
update_notes: '<p dir="auto">Just some minor console fixes</p>

  <ul dir="auto">

  <li>Removed debugging artifacts from the player menu</li>

  <li>Updated version label on the bottom side of the border</li>

  </ul>'
updated: '2022-01-27T19:06:36Z'
version: V0.2.1
version_title: FSPDS V0.2.1
website: https://www.gamebrew.org/wiki/FSPDS
---
A DS ROM which allows playing DSi's Flipnote Studio (.ppm) files on a DS Phat/Lite. It features flipnote image and sound player with pause/resume option, and also a file metadata viewer.

Place the flipnotes you want to play in a `/flipnotes/` folder at the root of your SD card. FSPDS will not detect/play files larger than 1MB. It is also possible the app won't play correctly files with more than 512KB of BGM soundtrack (although I have never met such a file during my tests).