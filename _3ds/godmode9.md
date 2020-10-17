---
author: d0k3
categories:
- utility
- firm
created: '2016-01-22T18:00:30Z'
description: 'GodMode9 Explorer - A full access file browser for the Nintendo 3DS
  console :godmode:'
download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.1
downloads:
  GodMode9-v1.9.1-20200110121417.zip: https://github.com/d0k3/GodMode9/releases/download/v1.9.1/GodMode9-v1.9.1-20200110121417.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
layout: app
prerelease:
  download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.2pre1
  downloads:
    GodMode9-v1.9.2pre1-20200820205253.zip: https://github.com/d0k3/GodMode9/releases/download/v1.9.2pre1/GodMode9-v1.9.2pre1-20200820205253.zip
  updated: '2020-08-22T10:18:04Z'
  version: v1.9.2pre1
  version_title: GodMode9 v1.9.2pre1 Fourth Anniversary Edition
scripts:
  Release (FIRM):
  - file: GodMode9.*.zip
    message: Downloading the GodMode9 ZIP...
    output: /GodMode9.zip
    repo: d0k3/GodMode9
    type: downloadRelease
  - file: /GodMode9.zip
    input: GodMode9.firm
    message: Extracting the GodMode9 FIRM...
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
updated: '2020-01-10T18:33:56Z'
version: v1.9.1
version_title: GodMode9 v1.9.1
wiki: https://github.com/d0k3/GodMode9/wiki
---
