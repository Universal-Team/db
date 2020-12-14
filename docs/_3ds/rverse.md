---
author: rverseTeam
categories:
- utility
color: '#142699'
created: '2020-04-18T01:16:12Z'
description: Miiverse clone framework, for 3DS and Wii U
download_page: https://github.com/rverseTeam/rverse-Releases/releases/tag/v3.0.0
downloads:
  rverse-3ds.7z:
    size: 3292
    url: https://github.com/rverseTeam/rverse-Releases/releases/download/v3.0.0/rverse-3ds.7z
  rverse-3ds.zip:
    size: 6551
    url: https://github.com/rverseTeam/rverse-Releases/releases/download/v3.0.0/rverse-3ds.zip
github: rverseTeam/rverse-Releases
image: https://avatars2.githubusercontent.com/u/38678735?v=4
layout: app
scripts:
  rverse:
  - file: rverse-3ds.zip
    message: Downloading rverse...
    output: /rverse.zip
    repo: rverseTeam/rverse-Releases
    type: downloadRelease
  - file: /rverse.zip
    input: ''
    message: Extracting rverse...
    output: /
    type: extractFile
  - file: sdmc:/rverse.zip
    message: Deleting rverse.zip...
    type: deleteFile
source: https://github.com/rverseTeam/rverse2
systems:
- 3DS
title: rverse
update_notes: '<h1>rverse Public Release #1</h1>

  <p>This is the release you need to use, not the earlier one.</p>'
updated: '2020-04-18T20:45:33Z'
version: v3.0.0
version_title: Release 20200417
website: https://github.com/rverseTeam/rverse-Releases
---
