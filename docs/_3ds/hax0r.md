---
author: TurtleP
categories:
- game
color: '#343434'
created: '2015-08-28T23:47:21Z'
description: 'A Ludum Dare #33 Game'
download_page: https://github.com/TurtleP/Hax0r/releases/tag/v1.2
downloads:
  Hax0r.zip:
    size: 8511357
    url: https://github.com/TurtleP/Hax0r/releases/download/v1.2/Hax0r.zip
github: TurtleP/Hax0r
icon: https://raw.githubusercontent.com/TurtleP/Hax0r/master/graphics/icon.png
image: https://db.universal-team.net/assets/images/images/hax0r.png
layout: app
scripts:
  Hax0r.3dsx:
  - file: Hax0r.zip
    message: Downloading Hax0r.zip...
    output: /Hax0r.zip
    repo: TurtleP/Hax0r
    type: downloadRelease
  - file: /Hax0r.zip
    input: ''
    message: Extracting Hax0r...
    output: /3ds/Hax0r/
    type: extractFile
  - message: Moving Hax0r...
    new: '%3DSX%/Hax0r.3dsx'
    old: /3ds/Hax0r/Hax0r.3dsx
    type: move
  - file: /Hax0r.zip
    message: Deleting Hax0r.zip...
    type: deleteFile
  Hax0r.cia:
  - file: Hax0r.zip
    message: Downloading Hax0r.zip...
    output: /Hax0r.zip
    repo: TurtleP/Hax0r
    type: downloadRelease
  - file: /Hax0r.zip
    input: ''
    message: Extracting Hax0r...
    output: /3ds/Hax0r/
    type: extractFile
  - file: /3ds/Hax0r/Hax0r.cia
    message: Installing Hax0r.cia...
    type: installCia
  - file: /3ds/Hax0r/Hax0r.cia
    message: Deleting Hax0r.cia...
    type: deleteFile
  - file: /Hax0r.zip
    message: Deleting Hax0r.zip...
    type: deleteFile
source: https://github.com/TurtleP/Hax0r
systems:
- 3DS
title: Hax0r
update_notes: '<p>Welp I messed up after Love Potion updated.</p>

  <p>Here''s a fix for it.</p>

  <p>Included are a 3dsx version <em>and</em> cia version!</p>

  <p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/275903375fb85cff9bd69756538b893f16d1cef872d02eaaa686769917b64c23/687474703a2f2f74696e7975726c2e636f6d2f4861783072434941"><img
  src="https://camo.githubusercontent.com/275903375fb85cff9bd69756538b893f16d1cef872d02eaaa686769917b64c23/687474703a2f2f74696e7975726c2e636f6d2f4861783072434941"
  alt="" data-canonical-src="http://tinyurl.com/Hax0rCIA" style="max-width:100%;"></a></p>'
updated: '2016-07-07T19:36:27Z'
version: v1.2
version_title: Bugfixes 'n Stuff
wiki: https://github.com/TurtleP/Hax0r/wiki
---
