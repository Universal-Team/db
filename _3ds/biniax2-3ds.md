---
author: nop90
categories:
- game
color: '#fddfbc'
created: '2016-06-29T21:30:57Z'
description: Port of Biniax2 on 3ds
download_page: https://github.com/nop90/Biniax2-3DS/releases/tag/V0.4alpha
github: nop90/Biniax2-3DS
icon: https://raw.githubusercontent.com/nop90/Biniax2-3DS/master/resources/icon.png
image: https://raw.githubusercontent.com/nop90/Biniax2-3DS/master/resources/banner.png
layout: app
prerelease:
  download_page: https://github.com/nop90/Biniax2-3DS/releases/tag/V0.4alpha
  downloads:
    Biniax2_3DSX.v0.4.zip:
      size: 18375236
      url: https://github.com/nop90/Biniax2-3DS/releases/download/V0.4alpha/Biniax2_3DSX.v0.4.zip
    Biniax2_CIA.v0.4.zip:
      size: 18761345
      url: https://github.com/nop90/Biniax2-3DS/releases/download/V0.4alpha/Biniax2_CIA.v0.4.zip
  update_notes: '<ul>

    <li>Used a bigger font</li>

    <li>Fixed a bug typing on ther virtual keyboard in the Hall of Fame for tactica
    mode</li>

    <li>Added a very simple AI to play vs CPU in multiplayer mode</li>

    <li>Added CIA version</li>

    </ul>'
  updated: '2016-07-04T07:32:48Z'
  version: V0.4alpha
  version_title: Bigger font and CIA version
scripts:
  '[prerelease] Biniax2.3dsx':
  - file: Biniax2_3DSX.*\.zip
    includePrereleases: true
    message: Downloading Biniax2_3DSX zip...
    output: /Biniax2_3DSX.zip
    repo: nop90/Biniax2-3DS
    type: downloadRelease
  - file: /Biniax2_3DSX.zip
    input: Biniax2/Biniax2.3dsx
    message: Extracting Biniax2.3dsx...
    output: '%3DSX%/Biniax2.3dsx'
    type: extractFile
  - file: /Biniax2_3DSX.zip
    message: Deleting Biniax2_3DSX.zip...
    type: deleteFile
  '[prerelease] Biniax2.cia':
  - file: Biniax2_CIA.*\.zip
    includePrereleases: true
    message: Downloading Biniax2_CIA zip...
    output: /Biniax2_CIA.zip
    repo: nop90/Biniax2-3DS
    type: downloadRelease
  - file: /Biniax2_CIA.zip
    input: Biniax2.cia
    message: Extracting Biniax2.cia...
    output: /Biniax2.cia
    type: extractFile
  - file: /Biniax2.cia
    message: Installing Biniax2.cia...
    type: installCia
  - file: /Biniax2.cia
    message: Deleting Biniax2.cia...
    type: deleteFile
  - file: /Biniax2_CIA.zip
    message: Deleting Biniax2_CIA.zip...
    type: deleteFile
source: https://github.com/nop90/Biniax2-3DS
systems:
- 3DS
title: Biniax2-3DS
update_notes: '<ul>

  <li>Used a bigger font</li>

  <li>Fixed a bug typing on ther virtual keyboard in the Hall of Fame for tactica
  mode</li>

  <li>Added a very simple AI to play vs CPU in multiplayer mode</li>

  <li>Added CIA version</li>

  </ul>'
updated: '2016-07-04T07:32:48Z'
version: V0.4alpha
version_title: Bigger font and CIA version
wiki: https://github.com/nop90/Biniax2-3DS/wiki
---
