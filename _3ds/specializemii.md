---
author: phijor
categories:
- utility
color: '#a59123'
created: '2016-10-09T18:02:18Z'
description: Golden Pants for everyone!
download_page: https://github.com/phijor/SpecializeMii/releases/tag/0.1.4
downloads:
  SpecializeMii.zip:
    size: 1290621
    url: https://github.com/phijor/SpecializeMii/releases/download/0.1.4/SpecializeMii.zip
github: phijor/SpecializeMii
icon: https://raw.githubusercontent.com/phijor/SpecializeMii/master/etc/icon.png
image: https://raw.githubusercontent.com/phijor/SpecializeMii/master/etc/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  SpecializeMii.3dsx:
  - file: SpecializeMii.zip
    message: Downloading SpecializeMii.zip...
    output: /SpecializeMii.zip
    repo: phijor/SpecializeMii
    type: downloadRelease
  - file: /SpecializeMii.zip
    input: 3ds-arm/3ds/SpecializeMii/SpecializeMii.3dsx
    message: Extracting SpecializeMii.3dsx...
    output: '%3DSX%/SpecializeMii.3dsx'
    type: extractFile
  - file: /SpecializeMii.zip
    message: Deleting SpecializeMii.zip...
    type: deleteFile
  SpecializeMii.cia:
  - file: SpecializeMii.zip
    message: Downloading SpecializeMii.zip...
    output: /SpecializeMii.zip
    repo: phijor/SpecializeMii
    type: downloadRelease
  - file: /SpecializeMii.zip
    input: 3ds-arm/SpecializeMii.cia
    message: Extracting SpecializeMii.cia...
    output: /SpecializeMii.cia
    type: extractFile
  - file: /SpecializeMii.cia
    message: Installing SpecializeMii.cia...
    type: installCia
  - file: /SpecializeMii.cia
    message: Deleting SpecializeMii.cia...
    type: deleteFile
  - file: /SpecializeMii.zip
    message: Deleting SpecializeMii.zip...
    type: deleteFile
source: https://github.com/phijor/SpecializeMii
systems:
- 3DS
title: SpecializeMii
update_notes: <p>This fixes issues <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="201148320" data-permission-text="Title is private" data-url="https://github.com/phijor/SpecializeMii/issues/2"
  data-hovercard-type="issue" data-hovercard-url="/phijor/SpecializeMii/issues/2/hovercard"
  href="https://github.com/phijor/SpecializeMii/issues/2">#2</a> and <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="201727055" data-permission-text="Title
  is private" data-url="https://github.com/phijor/SpecializeMii/issues/3" data-hovercard-type="issue"
  data-hovercard-url="/phijor/SpecializeMii/issues/3/hovercard" href="https://github.com/phijor/SpecializeMii/issues/3">#3</a>,
  thanks to <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/XT-8147/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/XT-8147">@XT-8147</a>
  for reporting.</p>
updated: '2017-01-22T11:19:45Z'
version: 0.1.4
version_title: Fix un-specializing personal Mii
wiki: https://github.com/phijor/SpecializeMii/wiki
---
