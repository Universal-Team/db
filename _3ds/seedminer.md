---
author: zoogie
categories:
- utility
color: '#121212'
created: '2018-01-21T07:02:04Z'
description: 34.2c3 POC
download_page: https://github.com/zoogie/seedminer/releases/tag/v2.1
downloads:
  RELEASE_v2.1.zip:
    size: 11053478
    url: https://github.com/zoogie/seedminer/releases/download/v2.1/RELEASE_v2.1.zip
github: zoogie/seedminer
icon: https://raw.githubusercontent.com/zoogie/seedminer/master/seedstarter/resources/icon.png
image: https://raw.githubusercontent.com/zoogie/seedminer/master/seedstarter/resources/banner.png
layout: app
license: mit
license_name: MIT License
scripts:
  seedstarter.3dsx:
  - file: RELEASE.*\.zip
    message: Downloading seedminer.zip...
    output: /seedminer.zip
    repo: zoogie/seedminer
    type: downloadRelease
  - file: /seedminer.zip
    input: RELEASE.*/seedstarter.3dsx
    message: Extracting seedstarter.3dsx...
    output: '%3DSX%/seedstarter.3dsx'
    type: extractFile
  - file: /seedminer.zip
    message: Deleting seedminer.zip...
    type: deleteFile
  seedstarter.cia:
  - file: RELEASE.*\.zip
    message: Downloading seedminer.zip...
    output: /seedminer.zip
    repo: zoogie/seedminer
    type: downloadRelease
  - file: /seedminer.zip
    input: RELEASE.*/seedstarter.cia
    message: Extracting seedstarter.cia...
    output: /seedstarter.cia
    type: extractFile
  - file: /seedstarter.cia
    message: Installing seedstarter.cia...
    type: installCia
  - file: /seedstarter.cia
    message: Deleting seedstarter.cia...
    type: deleteFile
  - file: /seedminer.zip
    message: Deleting seedminer.zip...
    type: deleteFile
source: https://github.com/zoogie/seedminer
systems:
- 3DS
title: seedminer
updated: '2018-02-22T09:37:13Z'
version: v2.1
version_title: Gimmie bin edition
wiki: https://github.com/zoogie/seedminer/wiki
---
