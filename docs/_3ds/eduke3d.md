---
author: masterfeizz
categories:
- utility
color: '#6fb1f4'
created: '2015-11-08T13:42:52Z'
description: Unofficial port of EDuke32 for the Nintendo 3DS
download_page: https://github.com/masterfeizz/EDuke3D/releases/tag/v1.0-beta
github: masterfeizz/EDuke3D
icon: https://raw.githubusercontent.com/masterfeizz/EDuke3D/master/icon.png
image: https://db.universal-team.net/assets/images/images/eduke3d.png
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
prerelease:
  download_page: https://github.com/masterfeizz/EDuke3D/releases/tag/v1.0-beta
  downloads:
    EDuke3D-v1.0-beta.zip:
      size: 5673892
      url: https://github.com/masterfeizz/EDuke3D/releases/download/v1.0-beta/EDuke3D-v1.0-beta.zip
    EDuke3D.cia:
      size: 1067456
      url: https://github.com/masterfeizz/EDuke3D/releases/download/v1.0-beta/EDuke3D.cia
  qr:
    EDuke3D.cia: https://db.universal-team.net/assets/images/qr/prerelease/eduke3d.cia.png
  update_notes: '<p>Bugfixes (mostly memory management) and first CIA release.<br>

    View README on the project page for instructions.<br>

    CIA bugs:<br>

    Game must be closed from quit option on the menu, and not from the 3ds home menu<br>

    Home button only works when in a level</p>'
  updated: '2016-05-08T04:36:44Z'
  version: v1.0-beta
  version_title: Beta release (fixed)
scripts:
  '[prerelease] EDuke3D.cia':
  - file: EDuke3D.*\.zip
    includePrereleases: true
    message: Downloading EDuke3D.zip...
    output: /EDuke3D.zip
    repo: masterfeizz/EDuke3D
    type: downloadRelease
  - file: /EDuke3D.zip
    input: ''
    message: Extracting EDuke3D...
    output: /
    type: extractFile
  - file: EDuke3D.cia
    includePrereleases: true
    message: Downloading EDuke3D.cia...
    output: /EDuke3D.cia
    repo: masterfeizz/EDuke3D
    type: downloadRelease
  - file: /EDuke3D.cia
    message: Installing EDuke3D.cia...
    type: installCia
  - file: /EDuke3D.cia
    message: Deleting EDuke3D.cia...
    type: deleteFile
  - file: /EDuke3D.zip
    message: Deleting EDuke3D.zip...
    type: deleteFile
  '[prerelease] eduke3d.3dsx':
  - file: EDuke3D.*\.zip
    includePrereleases: true
    message: Downloading EDuke3D.zip...
    output: /EDuke3D.zip
    repo: masterfeizz/EDuke3D
    type: downloadRelease
  - file: /EDuke3D.zip
    input: ''
    message: Extracting EDuke3D...
    output: /
    type: extractFile
  - new: '%3DSX%/eduke3d.3dsx'
    old: /3ds/eduke3d/eduke3d.3dsx
    type: move
  - file: /EDuke3D.zip
    message: Deleting EDuke3D.zip...
    type: deleteFile
source: https://github.com/masterfeizz/EDuke3D
systems:
- 3DS
title: EDuke3D
update_notes: '<p>Bugfixes (mostly memory management) and first CIA release.<br>

  View README on the project page for instructions.<br>

  CIA bugs:<br>

  Game must be closed from quit option on the menu, and not from the 3ds home menu<br>

  Home button only works when in a level</p>'
updated: '2016-05-08T04:36:44Z'
version: v1.0-beta
version_title: Beta release (fixed)
wiki: https://github.com/masterfeizz/EDuke3D/wiki
---
