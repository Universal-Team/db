---
author: Jens Andersson
categories:
- utility
color: '#697e93'
description: Colors! is a simplistic painting application combining ease of use and
  powerful painting tools.
download_page: https://gamebrew.org/wiki/Colors!
downloads:
  Colors110ds.zip:
    url: https://db.universal-team.net/assets/files/Colors110ds.zip
icon: https://db.universal-team.net/assets/images/icons/colors.png
layout: app
scripts:
  Colors.nds:
  - file: https://db.universal-team.net/assets/files/Colors110ds.zip
    message: Downloading Colors110ds.zip...
    output: /Colors110ds.zip
    type: downloadFile
  - file: /Colors110ds.zip
    input: Colors.nds
    message: Extracting Colors.nds...
    output: '%NDS%/Colors.nds'
    type: extractFile
  - count: 1
    message: Extract ColorsMagazine_1.col?
    type: promptMessage
  - file: /Colors110ds.zip
    input: ColorsMagazine_1.col
    message: Extracting ColorsMagazine_1.col...
    output: '%NDS%/ColorsMagazine_1.col'
    type: extractFile
  - file: /Colors110ds.zip
    message: Deleting Colors110ds.zip...
    type: deleteFile
systems:
- DS
title: Colors!
updated: '2010-10-04T10:11:20Z'
version: v1.1
website: https://www.colorslive.com
---
