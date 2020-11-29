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
update_notes: "NOTE: This release archive contains a pyinstaller compiled python script\
  \ named seedminer_launcher.exe. Windows will likely trigger a false virus warning\
  \ (Trojan:Win32/Occamy.B) and delete the file. This is a known issue with some antivirus\
  \ programs not trusting pyinstaller binaries. The exe is not actually dangerous,\
  \ but if you still don't trust it, go ahead and run one of the seedminer_launcher.py\
  \ scripts instead -- they are functionally identical to the exe version.\r\nCHANGELOG:\r\
  \n- update to latest msed_data with update-db command\r\n- mii qr brute force is\
  \ now combined with msed bf provided input.bin and movable_part1.sed (w/ID0) are\
  \ in seedminer/\r\n- more error checks for noob protection\r\n- a bunch more msed_data!\r\
  \n- python3 support added (thx @ihaveamac ) use seedminer_launcher3.py\r\n- triumphant\
  \ return of the pyinstaller exe blob - by popular demand - false virus warning be\
  \ damned!\r\n- seedstarter.cia is now in archive\r\n- DSIHaxInjector is now officially\
  \ recommended in the readme instead of TADpole (DSIHaxInjector is basically tadpole\
  \ in the cloud with a nice web ui)\r\n\r\nStealth 2/23/18: readme update\r\nStealth\
  \ 3/1/18: msed update, total 503->707\r\nStealth 3/19/18: msed update, total 707->1201\r\
  \nStealth 3/29/18: msed update, total 1201->1501\r\nStealth 4/5/18: msed update,\
  \ total 1501->1801\r\nStealth 4/7/18: msed update, total 1801->2004\r\nStealth 4/7/18:\
  \ seedstarter update to 1.1 (minor)\r\nStealth 4/11/18: msed update, total 2004->2603\r\
  \nStealth 4/17/18: msed update, total 2603->3502\r\nStealth 6/27/18: msed update,\
  \ total 3503 -> 20000, small readme tweak\r\nStealth 8/27/18 msed update, total\
  \ 20000 -> 32000, seedstarter 1.2 (foolproof id0 retrieval)\r\nStealth 11/19/18\
  \ msed update, total 32000 -> 40000 (final v1 msed update)\r\nStealth 1/20/19 readme\
  \ update"
updated: '2018-02-22T09:37:13Z'
version: v2.1
version_title: Gimmie bin edition
wiki: https://github.com/zoogie/seedminer/wiki
---
