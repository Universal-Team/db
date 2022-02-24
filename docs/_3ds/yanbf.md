---
author: lifehackerhansol
avatar: https://avatars.githubusercontent.com/u/37358975?v=4
categories:
- utility
color: '#90594d'
color_bg: '#804f44'
created: '2021-06-16T08:14:55Z'
description: Yet another nds-bootstrap forwarder. Runs from 3DS-mode!
download_page: https://github.com/lifehackerhansol/YANBF/releases
downloads:
  YANBF-Linux.zip:
    size: 79758325
    size_str: 76 MiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.3.0/YANBF-Linux.zip
  YANBF-Windows.zip:
    size: 54980660
    size_str: 52 MiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.3.0/YANBF-Windows.zip
  YANBF-macOS.zip:
    size: 81644972
    size_str: 77 MiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.3.0/YANBF-macOS.zip
  bootstrap.cia:
    size: 206080
    size_str: 201 KiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.3.0/bootstrap.cia
github: lifehackerhansol/YANBF
icon_index: 198
image: https://avatars.githubusercontent.com/u/37358975?v=4
image_length: 32023
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
qr:
  bootstrap.cia: https://db.universal-team.net/assets/images/qr/bootstrap-cia.png
source: https://github.com/lifehackerhansol/YANBF
systems:
- 3DS
title: YANBF
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>UniqueID randomizing is here.

  <ul dir="auto">

  <li>Not present in the GUI yet. You will need to do it via CLI.</li>

  <li>Pass -r as an argument to randomize.</li>

  </ul>

  </li>

  <li>Launch splash has been changed from Homebrew to Nintendo 3DS.</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>UniqueID collision checking is now implemented.

  <ul dir="auto">

  <li>This will require your <code>Nintendo 3DS</code> folder to be "clean". This
  means one ID0 folder and one ID1 folder only. If you have multiple, please clean
  them up.</li>

  <li>This works by checking all TIDLOW values that are present on the SD card. If
  the UniqueID calculated by YANBF already exists on the SD card, it will simply increment
  the UniqueID by 1 until it no longer collides.

  <ul dir="auto">

  <li>This may still collide with any titles that have not yet been installed. So
  this has a chance of potentially being replaced in the future by a retail game or
  some others homebrew app. There isn''t a public database of this stuff or anything
  so unfortunately I cannot guarantee this for you.</li>

  </ul>

  </li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed an issue where the 3DS-side app may display "Failed to launch CIA" error
  for a brief moment before actually launching.</li>

  </ul>'
updated: '2022-02-20T19:12:21Z'
version: v1.3.0
version_title: 'v1.3.0: randomizing is here'
---
YANBF is a 3DS-mode nds-bootstrap forwarder, allowing for more than 40 forwarder titles as compared to the older forwarder template.