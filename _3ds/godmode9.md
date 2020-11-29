---
author: d0k3
categories:
- utility
- firm
color: '#130000'
created: '2016-01-22T18:00:30Z'
description: 'GodMode9 Explorer - A full access file browser for the Nintendo 3DS
  console :godmode:'
download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.1
downloads:
  GodMode9-v1.9.1-20200110121417.zip:
    size: 1840083
    url: https://github.com/d0k3/GodMode9/releases/download/v1.9.1/GodMode9-v1.9.1-20200110121417.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.2pre1
  downloads:
    GodMode9-v1.9.2pre1-20200820205253.zip:
      size: 2243273
      url: https://github.com/d0k3/GodMode9/releases/download/v1.9.2pre1/GodMode9-v1.9.2pre1-20200820205253.zip
  updated: '2020-08-22T10:18:04Z'
  version: v1.9.2pre1
  version_title: GodMode9 v1.9.2pre1 Fourth Anniversary Edition
scripts:
  GodMode9.firm:
  - file: GodMode9.*.zip
    message: Downloading GodMode9 zip...
    output: /GodMode9.zip
    repo: d0k3/GodMode9
    type: downloadRelease
  - file: /GodMode9.zip
    input: GodMode9.firm
    message: Extracting the GodMode9.firm...
    output: /luma/payloads/GodMode9.firm
    type: extractFile
  - file: /GodMode9.zip
    input: gm9/
    message: Extracting the /gm9/ directory...
    output: /gm9/
    type: extractFile
  - file: /luma/payloads/GodMode9.firm.sha
    message: Deleting a stowaway file...
    type: deleteFile
  - file: /GodMode9.zip
    message: Deleting the downloaded ZIP file...
    type: deleteFile
  '[prerelease] GodMode9.firm':
  - file: GodMode9.*.zip
    includePrereleases: true
    message: Downloading GodMode9 zip...
    output: /GodMode9.zip
    repo: d0k3/GodMode9
    type: downloadRelease
  - file: /GodMode9.zip
    input: GodMode9.firm
    message: Extracting the GodMode9.firm...
    output: /luma/payloads/GodMode9.firm
    type: extractFile
  - file: /GodMode9.zip
    input: gm9/
    message: Extracting the /gm9/ directory...
    output: /gm9/
    type: extractFile
  - file: /luma/payloads/GodMode9.firm.sha
    message: Deleting a stowaway file...
    type: deleteFile
  - file: /GodMode9.zip
    message: Deleting the downloaded ZIP file...
    type: deleteFile
source: https://github.com/d0k3/GodMode9
systems:
- 3DS
title: GodMode9
update_notes: "Time for a new GodMode9 release. The last major release, v1.9.0, was\
  \ a pretty solid release to begin with, but as always there is room for improvement.\
  \ This one focuses on bugfixes, fixing stuff that v1.9.0 did not do right. This\
  \ is new:\r\n* [new] On verification, offer fixing for badly decrypted NCCH/NCSD\r\
  \n* [improved] Much faster scrolling speeds in wordwrapped text view\r\n* [improved]\
  \ Largely improved method of GBA VC save injection (thanks @TurdPooCharger)\r\n\
  * [fixed] Fixed the .BPS code in scripting (thanks @Wolfvak)\r\n* [fixed] Fixed\
  \ a crash in the DISA/DIFF handling code (thanks @aspargas2)\r\n* [fixed] Actually\
  \ allow decrypting N3DS NATIVE_FIRM on O3DS\r\n* [fixed] Last search drive is back\
  \ again\r\n* [fixed] Cart drive checking (don't show empty when it isn't\r\n* [fixed]\
  \ Notification light handling\r\n\r\n**Did you know?**\r\nThis marks the 40th release\
  \ of GodMode9, with a whopping 1260 commits leading up to here. GodMode9 is now\
  \ in it's fourth year of development and still going strong, thanks to all of my\
  \ fellow developers, bug reporters and feature requesters.\r\n\r\n**Tsktsktsk**\r\
  \nWe've been seeing a lot of bug reports these days with people telling us they\
  \ can't convert their NCSD (\".3DS\") files to CIA in GodMode9. It can be assumed\
  \ that _all of them_ got their _badly decrypted_ .3DS files from some shady source.\
  \ Shady source: please at least provide proper decrypted files. @citra-emu: maybe\
  \ stop supporting these files or at least give a warning to users? We, for our part,\
  \ now properly detect these files and offer fixing. To use the new fixer, just verify\
  \ your files.\r\n\r\n**Credits**\r\nAs always this wouldn't have been possible without\
  \ some help. Thanks go to @Wolfvak, @aspargas2 and @TurdPooCharger for actively\
  \ contributing to development. I also thank everyone submitting bug reports and\
  \ feature requests. A special mention goes to @HIDE810 who finally pointed out that\
  \ text viewer scrolling is awfully slow in some cases and needs some work. Thanks,\
  \ all of you!"
updated: '2020-01-10T18:33:56Z'
version: v1.9.1
version_title: GodMode9 v1.9.1
wiki: https://github.com/d0k3/GodMode9/wiki
---
