---
author: windows-server-2003
avatar: https://avatars.githubusercontent.com/u/31173797?v=4
categories:
- utility
color: '#871112'
created: '2021-07-19T17:53:12Z'
description: A work-in-progress homebrew YouTube client for new 3DS
download_page: https://github.com/windows-server-2003/ThirdTube/releases
downloads:
  ThirdTube.3dsx:
    size: 4152172
    size_str: 3 MiB
    url: https://github.com/windows-server-2003/ThirdTube/releases/download/v0.1.1/ThirdTube.3dsx
  ThirdTube.cia:
    size: 3113920
    size_str: 2 MiB
    url: https://github.com/windows-server-2003/ThirdTube/releases/download/v0.1.1/ThirdTube.cia
github: windows-server-2003/ThirdTube
icon: https://raw.githubusercontent.com/windows-server-2003/ThirdTube/main/resource/icon.png
image: https://raw.githubusercontent.com/windows-server-2003/ThirdTube/main/resource/banner.png
image_length: 9933
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  ThirdTube.cia: https://db.universal-team.net/assets/images/qr/thirdtube.cia.png
screenshots:
- description: Comments
  url: https://db.universal-team.net/assets/images/screenshots/thirdtube/comments.png
- description: General
  url: https://db.universal-team.net/assets/images/screenshots/thirdtube/general.png
- description: Search
  url: https://db.universal-team.net/assets/images/screenshots/thirdtube/search.png
source: https://github.com/windows-server-2003/ThirdTube
systems:
- 3DS
title: ThirdTube
update_notes: '<p>A relatively critical crash bug was found in the previous release,
  so I''m releasing this with the fix for it.</p>

  <ul>

  <li>Fixed crashing when playing 1h + video</li>

  <li>Speeded up YouTube parser for quicker loading</li>

  <li>Reduced the binary size by removing unnecessary codecs and demuxers from ffmpeg
  library</li>

  <li>Implemented experimental network framework using sslc service + manual HTTP/1.1
  parser which can be enabled in Settings<br>

  This reuses TLS connection sessions if possible, improving performance for thumbnails
  and livestreams.<br>

  However, it''s less stable than current one using httpc service for now, so it''s
  optional (and disabled by default).<br>

  Bug reports for this feature are greatly appreciated. It would be helpful to include
  whether the bug still occurs if you turn off this feature in the bug report.</li>

  </ul>'
updated: '2021-08-12T16:07:55Z'
version: v0.1.1
version_title: Release v0.1.1
website: https://gbatemp.net/threads/release-thirdtube-a-homebrew-youtube-client-for-the-new-3ds.591696/
---
