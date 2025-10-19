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
  FSPDS-V1.0.79212842R.nds:
    size: 749568
    size_str: 732 KiB
    url: https://github.com/NotImplementedLife/FSPDS/releases/download/V1.0/FSPDS-V1.0.79212842R.nds
github: NotImplementedLife/FSPDS
icon: https://db.universal-team.net/assets/images/icons/fspds.png
image: https://db.universal-team.net/assets/images/icons/fspds.png
image_length: 586
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/NotImplementedLife/FSPDS/releases/tag/V1.0.90343508R
  downloads:
    FSPDS-V1.0.90343508R.nds:
      size: 750080
      size_str: 732 KiB
      url: https://github.com/NotImplementedLife/FSPDS/releases/download/V1.0.90343508R/FSPDS-V1.0.90343508R.nds
  qr:
    FSPDS-V1.0.90343508R.nds: https://db.universal-team.net/assets/images/qr/prerelease/fspds-v1-0-90343508r-nds.png
  update_notes: <p dir="auto">FSPDS now accepts PPM filenames that do not respect
    the original naming convention, like "my_flipnote.ppm". The filename shouldn't
    exceed more than 28 characters.</p>
  update_notes_md: FSPDS now accepts PPM filenames that do not respect the original
    naming convention, like "my_flipnote.ppm". The filename shouldn't exceed more
    than 28 characters.
  updated: '2023-12-08T13:29:30Z'
  version: V1.0.90343508R
  version_title: FSPDS V1.0.90343508R- Minipatch filenames
qr:
  FSPDS-V1.0.79212842R.nds: https://db.universal-team.net/assets/images/qr/fspds-v1-0-79212842r-nds.png
screenshots:
- description: File list
  url: https://db.universal-team.net/assets/images/screenshots/fspds/file-list.png
- description: Player 1
  url: https://db.universal-team.net/assets/images/screenshots/fspds/player-1.png
- description: Player 2
  url: https://db.universal-team.net/assets/images/screenshots/fspds/player-2.png
source: https://github.com/NotImplementedLife/FSPDS
stars: 35
systems:
- DS
title: FSPDS
update_notes: '<p dir="auto">We''ve made it to 1.0 !</p>

  <p dir="auto">What''s new:</p>

  <ul dir="auto">

  <li>recreated the application from scratch</li>

  <li>brand new beautiful UI</li>

  <li>considerably improved frame decoding performance</li>

  <li>flipnote paths are preindexed in cache file data for faster access</li>

  <li>flipnotes can be loaded from any location on the SD card</li>

  <li>more stable and useful player bar with previous/next navigation features, auto
  repeat and shuffling</li>

  <li>can display flipnote author names with Unicode support</li>

  </ul>'
updated: '2023-08-02T15:33:21Z'
version: V1.0
version_title: FSPDS V1.0
website: https://www.gamebrew.org/wiki/FSPDS
---
A DS ROM which allows playing DSi's Flipnote Studio (.ppm) files on a DS Phat/Lite. It features flipnote image and sound player with pause/resume option, and also a file metadata viewer.

Place the flipnotes you want to play in a `/flipnotes/` folder at the root of your SD card. FSPDS will not detect/play files larger than 1MB. It is also possible the app won't play correctly files with more than 512KB of BGM soundtrack (although I have never met such a file during my tests).