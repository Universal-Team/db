---
author: Alex Taber
avatar: https://avatars.githubusercontent.com/u/7305572?v=4
categories:
- utility
color: '#5a9cc8'
color_bg: '#396380'
created: '2017-07-10T21:48:13Z'
description: A theme and boot splash manager for the Nintendo 3DS console
download_page: https://github.com/astronautlevel2/Anemone3DS/releases
downloads:
  Anemone3DS.3dsx:
    size: 648020
    size_str: 632 KiB
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.3.0/Anemone3DS.3dsx
  Anemone3DS.cia:
    size: 1041344
    size_str: 1016 KiB
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.3.0/Anemone3DS.cia
github: astronautlevel2/Anemone3DS
icon: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/icon.png
icon_index: 53
image: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/banner.png
image_length: 152331
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  Anemone3DS.cia: https://db.universal-team.net/assets/images/qr/anemone3ds-cia.png
screenshots:
- description: Get themes mode
  url: https://db.universal-team.net/assets/images/screenshots/anemone3ds/get-themes-mode.png
- description: Theme list
  url: https://db.universal-team.net/assets/images/screenshots/anemone3ds/theme-list.png
source: https://github.com/astronautlevel2/Anemone3DS
systems:
- 3DS
title: Anemone3DS
update_notes: '<p dir="auto">Hey everyone! For the first Anemone3DS update in over
  a year, we are bringing you... mostly a very minor update. In addition to a couple
  feature updates, this update also restores compatibility with ThemePlaza, which
  recently changed its network protocols to no longer support TLSv1.1. Note that from
  this update onwards, Anemone3DS will be communicating with ThemePlaza over HTTP
  rather than HTTPS, as the 3DS httpc sysmodule does not support newer TLS versions
  than 1.1. However, no identifying information is communicated with ThemePlaza, so
  there should not be any security concerns. And now, as always, it is time for the
  features and bugfixes!</p>

  <p dir="auto">Features:</p>

  <ul dir="auto">

  <li>Shuffle now works even if you''ve never used a shuffle theme before</li>

  <li>Add ability to dump all installed themes! The application already supported
  backing up the currently installed theme, but now also supports backing up all your
  themes.</li>

  <li>Connection error messages will now display considerably more information than
  before</li>

  </ul>

  <p dir="auto">Bugfixes:</p>

  <ul dir="auto">

  <li>Fixed a browser error which allowed you to scroll out of bounds</li>

  <li>Fixed a couple of error messages which weren''t displaying properly</li>

  <li>Fixed a couple minor shuffle bugs with how our shuffle implementation interacted
  with the official theme manager</li>

  <li>Fixed a bug where the application did not properly handle downloading to a filename
  which already existed on the filesystem</li>

  <li>Fixed some audio edge cases</li>

  <li>Fixed support for ThemePlaza by using HTTP rather than HTTPS</li>

  </ul>

  <p dir="auto">And now a QR Code!</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/c950f616499c88fb131d25c86d93b46edde6e8945f025533fbd616d7800d762a/68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f3335353836353339303037343536303531332f3937373935303237353332353238303238362f5152636f64652e706e673f77696474683d363731266865696768743d363731"><img
  src="https://camo.githubusercontent.com/c950f616499c88fb131d25c86d93b46edde6e8945f025533fbd616d7800d762a/68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f3335353836353339303037343536303531332f3937373935303237353332353238303238362f5152636f64652e706e673f77696474683d363731266865696768743d363731"
  alt="QR Code Download Link" data-canonical-src="https://media.discordapp.net/attachments/355865390074560513/977950275325280286/QRcode.png?width=671&amp;height=671"
  style="max-width: 100%;"></a></p>'
updated: '2022-05-22T14:59:37Z'
version: v2.3.0
version_title: Anemone3DS - Legacy Compatibility Update
wiki: https://github.com/astronautlevel2/Anemone3DS/wiki
---
