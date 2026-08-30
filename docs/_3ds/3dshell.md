---
author: Joel
avatar: https://avatars.githubusercontent.com/u/6271991?v=4
categories:
- utility
color: '#2c8ce1'
color_bg: '#194f80'
created: '2017-05-22T18:38:09Z'
description: 3DShell - (Pronounced 3D Shell) is a multi purpose file manager for the
  Nintendo 3DS. Heavily inspired by the CyanogenMod/LineageOS file manager.
download_page: https://github.com/joel16/3DShell/releases
downloads:
  3DShell.3dsx:
    size: 1985040
    size_str: 1 MiB
    url: https://github.com/joel16/3DShell/releases/download/v5.1.0/3DShell.3dsx
  3DShell.cia:
    size: 1651648
    size_str: 1 MiB
    url: https://github.com/joel16/3DShell/releases/download/v5.1.0/3DShell.cia
github: joel16/3DShell
icon: https://raw.githubusercontent.com/joel16/3DShell/master/res/ic_launcher_filemanager.png
image: https://raw.githubusercontent.com/joel16/3DShell/master/res/banner.png
image_length: 10753
layout: app
llm_generation: 'no'
prerelease:
  download_page: https://github.com/joel16/3DShell/releases/tag/next-v1.00
  downloads:
    3DShell.3dsx:
      size: 42890832
      size_str: 40 MiB
      url: https://github.com/joel16/3DShell/releases/download/next-v1.00/3DShell.3dsx
  update_notes: '<p dir="auto">A lot of the changes here are more under the hood changes,
    mainly being a lot of components being re-written. It''s still not as polished
    as I would''ve liked it to be and somethings may not be tested completely. The
    cia release is currently broken and will be provided at a later date if time permits.</p>

    <ul dir="auto">

    <li>Audio player has been reimplemented. (Supports FLAC, IT, MOD, MP3, OGG, OPUS,
    S3M, WAV, XM)</li>

    <li>Config no longer saves last visited directory (which led to a lot of crashes
    in previous releases)</li>

    <li>FS Dir reading has been overhauled - There will no longer be multiple layers
    of UTF8&lt;-&gt;UTF16 conversion, most FS code will handle UTF16 by default.</li>

    <li>You can now view PDFs/EBooks (This is still in BETA)</li>

    <li>Other minor changes for performance, consistency and upgrades to various libraries
    used. Also built with the latest version of devkitARM, libctru, and citro2d/3d.</li>

    </ul>'
  update_notes_md: 'A lot of the changes here are more under the hood changes, mainly
    being a lot of components being re-written. It''s still not as polished as I would''ve
    liked it to be and somethings may not be tested completely. The cia release is
    currently broken and will be provided at a later date if time permits.


    - Audio player has been reimplemented. (Supports FLAC, IT, MOD, MP3, OGG, OPUS,
    S3M, WAV, XM)

    - Config no longer saves last visited directory (which led to a lot of crashes
    in previous releases)

    - FS Dir reading has been overhauled - There will no longer be multiple layers
    of UTF8<->UTF16 conversion, most FS code will handle UTF16 by default.

    - You can now view PDFs/EBooks (This is still in BETA)

    - Other minor changes for performance, consistency and upgrades to various libraries
    used. Also built with the latest version of devkitARM, libctru, and citro2d/3d.'
  updated: '2026-07-31T13:25:42Z'
  version: next-v1.00
  version_title: 3DShell-next v1.00
qr:
  3DShell.cia: https://db.universal-team.net/assets/images/qr/3dshell-cia.png
screenshots:
- description: Settings
  url: https://db.universal-team.net/assets/images/screenshots/3dshell/settings.png
source: https://github.com/joel16/3DShell
stars: 361
systems:
- 3DS
title: 3DShell
unique_ids:
- '0x16200'
update_notes: '<ul dir="auto">

  <li>Block NAND access if developer options is disabled.</li>

  <li>Fix selector going out of bounds when right/left (page up/page down) key is
  used.</li>

  <li>CIA builds are now available. The updater will also download/install updates
  based on the version you are updating from.</li>

  <li>Fix selector going out of bounds when returning from a folder with a long list
  of files.</li>

  <li>Fix width/height display in image properties.</li>

  <li>Account for images that fit both screens in image viewer and implement zoom/navigation
  functionalities when viewing images.</li>

  <li>Archive extraction is back and currently supports .7z, .rar and .zip.</li>

  <li>Fix alphabetical sorting for filenames with different case letters.</li>

  <li>Allow user to cancel a file copy or archive extraction by the use of the "B"
  button.</li>

  <li>Improvised on bottom screen status bar icons.</li>

  <li>Updater will now display the download progress.</li>

  <li>GUI will now trim the string appropriately if length of a file name/current
  directory goes beyond the screen.</li>

  <li>Touch controls are back for both file options and settings.</li>

  <li>Fixed issues copying certain files/folders due to the file names not being cleared
  and improper casting in progress bar.</li>

  </ul>

  <p dir="auto">If you''d like to support this project, then feel free to <a href="https://www.paypal.me/Joel16IA"
  rel="nofollow">buy me a cup of ☕</a>.</p>'
updated: '2021-03-23T19:28:05Z'
version: v5.1.0
version_title: 3DShell v5.1.0
---
