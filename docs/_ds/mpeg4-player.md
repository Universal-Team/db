---
author: Gericom
categories:
- utility
color: '#7f6a4b'
created: '2016-04-19T18:19:53Z'
description: MPEG4 player for DS and DSi
download_page: https://gbatemp.net/threads/mpeg4-player-for-ds-and-dsi.544095/page-2#post-9007621
downloads:
  MPEG4Player.nds.zip:
    url: https://gbatemp.net/attachments/mpeg4player-nds-zip.203629/
github: Gericom/YouTubeDS
image: https://avatars2.githubusercontent.com/u/5251038?v=4
layout: app
scripts:
  MPEG4Player.nds:
  - file: https://gbatemp.net/attachments/mpeg4player-nds-zip.203629/
    message: Downloading MPEG4Player.nds.zip...
    output: /MPEG4Player.nds.zip
    type: downloadFile
  - file: /MPEG4Player.nds.zip
    input: MPEG4Player.nds
    message: Extracting MPEG4Player.nds...
    output: '%NDS%/MPEG4Player.nds'
    type: extractFile
  - file: /MPEG4Player.nds.zip
    message: Deleting MPEG4Player.nds.zip...
    type: deleteFile
source: https://github.com/Gericom/YoutubeDS/tree/mpeg4player
systems:
- DS
title: MPEG4 Player
updated: '2020-04-09T16:23:00Z'
version: c633295
website: https://gbatemp.net/threads/mpeg4-player-for-ds-and-dsi.544095/
wiki: https://github.com/Gericom/YoutubeDS/wiki
---
