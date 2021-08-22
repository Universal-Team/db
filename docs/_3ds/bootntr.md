---
author: Nanquitas
avatar: https://avatars.githubusercontent.com/u/13298129?v=4
categories:
- utility
color: '#7c626d'
created: '2016-04-21T14:02:23Z'
download_page: https://github.com/Nanquitas/BootNTR/releases
downloads:
  BootNTRSelector-FONZD-Banner.cia:
    size: 1508288
    size_str: 1 MiB
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-FONZD-Banner.cia
  BootNTRSelector-Mode3-FONZD-Banner.cia:
    size: 1508288
    size_str: 1 MiB
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-Mode3-FONZD-Banner.cia
  BootNTRSelector-Mode3-PabloMK7-Banner.cia:
    size: 1487808
    size_str: 1 MiB
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-Mode3-PabloMK7-Banner.cia
  BootNTRSelector-PabloMK7-Banner.3dsx:
    size: 1074176
    size_str: 1 MiB
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-PabloMK7-Banner.3dsx
  BootNTRSelector-PabloMK7-Banner.cia:
    size: 1487808
    size_str: 1 MiB
    url: https://github.com/Nanquitas/BootNTR/releases/download/v2.13.4/BootNTRSelector-PabloMK7-Banner.cia
github: Nanquitas/BootNTR
icon: https://raw.githubusercontent.com/Nanquitas/BootNTR/master/resources/icon.png
image: https://db.universal-team.net/assets/images/images/bootntr.png
image_length: 7456
layout: app
license: mit
license_name: MIT License
qr:
  BootNTRSelector-FONZD-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-fonzd-banner.cia.png
  BootNTRSelector-Mode3-FONZD-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-mode3-fonzd-banner.cia.png
  BootNTRSelector-Mode3-PabloMK7-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-mode3-pablomk7-banner.cia.png
  BootNTRSelector-PabloMK7-Banner.cia: https://db.universal-team.net/assets/images/qr/bootntrselector-pablomk7-banner.cia.png
screenshots:
- description: Auto updater
  url: https://db.universal-team.net/assets/images/screenshots/bootntr/auto-updater.png
- description: Banner fonzd
  url: https://db.universal-team.net/assets/images/screenshots/bootntr/banner-fonzd.png
- description: Banner pablomk7
  url: https://db.universal-team.net/assets/images/screenshots/bootntr/banner-pablomk7.png
- description: Failed to load
  url: https://db.universal-team.net/assets/images/screenshots/bootntr/failed-to-load.png
- description: Main menu
  url: https://db.universal-team.net/assets/images/screenshots/bootntr/main-menu.png
source: https://github.com/Nanquitas/BootNTR
systems:
- 3DS
title: BootNTR
update_notes: '<h1>This release is currently broken with official Luma3DS!</h1>

  <p>You can temporarily use the <a href="https://github.com/Nanquitas/Luma3DS/releases">Luma3DS
  3GX Loader build</a> until this issue is addressed!<br>

  <a href="https://github.com/LumaTeam/Luma3DS/blob/master/sysmodules/rosalina/include/csvc.h#L70-L79">The
  official Luma memory mapping svc</a> doesn''t function properly when mapping single
  pages from other processes, which causes BootNTR Selector to crash. In order to
  fix this issue either:</p>

  <ol>

  <li>BootNTR Selector code must be adapted to this.</li>

  <li>Luma3DS must support mapping other processes individual memory pages.</li>

  </ol>

  <p>While I''ll try to implement solution 1, I''ve decided to make this release as
  it will take some time to be implemented due to lack of time irl. (I think it''s
  better that the community has something partially functional than nothing at all.)
  Once any of the solutions are implemented, I''ll update this release with the updated
  files, sorry for the inconvenience.</p>

  <h1>Changelog</h1>

  <ul>

  <li>Added 11.14 support.</li>

  <li>Adapted code to latest ctrulib, no longer uses dma svcs to copy memory, so launching
  is way more stable.</li>

  </ul>

  <h1>Filename meaning</h1>

  <p>You will find different files below depending on your needs. Here is a little
  explanation on each term:</p>

  <h2>3dsx/cia</h2>

  <p>The <strong>3dsx</strong> file can be launched from the homebrew launcher while
  the cia files can be installed to the home menu. (There is only a single 3dsx file
  variation.)</p>

  <h2>Mode3</h2>

  <p>Files which have the the <strong>Mode3</strong> label are made specifically for
  extended memory games on Old 3DS/2DS models. (To detect if you are using an extended
  memory game, check if the console reboots after you close it from the home menu.)
  <strong>You don''t need to install the Mode3 version if you don''t want to use any
  extended memory game or you have a New 3DS/2DS.</strong></p>

  <h2>PabloMK7 / FONZD banner</h2>

  <p>The banner is the 3D model that shows in the top screen when you select the app
  in the home menu. The difference is only visual and is up to your own choice.</p>

  <h3>PabloMK7 Banner</h3>

  <p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/10946643/56131741-96b2c500-5f88-11e9-9af7-a81825505f5b.png"><img
  src="https://user-images.githubusercontent.com/10946643/56131741-96b2c500-5f88-11e9-9af7-a81825505f5b.png"
  alt="image" style="max-width:100%;"></a></p>

  <h3>FONZD Banner</h3>

  <p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/10946643/56131768-afbb7600-5f88-11e9-8585-6ceb930424cc.png"><img
  src="https://user-images.githubusercontent.com/10946643/56131768-afbb7600-5f88-11e9-8585-6ceb930424cc.png"
  alt="image" style="max-width:100%;"></a></p>'
updated: '2020-11-23T12:27:12Z'
version: v2.13.4
wiki: https://github.com/Nanquitas/BootNTR/wiki
---
