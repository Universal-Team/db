---
author: windows-server-2003
avatar: https://avatars.githubusercontent.com/u/31173797?v=4
categories:
- utility
color: '#871112'
color_bg: '#801011'
created: '2021-07-19T17:53:12Z'
description: A work-in-progress homebrew YouTube client for the 3DS
download_page: https://github.com/windows-server-2003/ThirdTube/releases
downloads:
  ThirdTube.3dsx:
    size: 5755820
    size_str: 5 MiB
    url: https://github.com/windows-server-2003/ThirdTube/releases/download/v0.5.0/ThirdTube.3dsx
  ThirdTube.cia:
    size: 4109248
    size_str: 3 MiB
    url: https://github.com/windows-server-2003/ThirdTube/releases/download/v0.5.0/ThirdTube.cia
github: windows-server-2003/ThirdTube
icon: https://raw.githubusercontent.com/windows-server-2003/ThirdTube/main/resource/icon.png
image: https://raw.githubusercontent.com/windows-server-2003/ThirdTube/main/resource/banner.png
image_length: 9933
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  ThirdTube.cia: https://db.universal-team.net/assets/images/qr/thirdtube-cia.png
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
update_notes: '<p dir="auto">I''m back with a major release v0.5.0!<br>

  I will continue to add features and fix bugs.<br>

  I would like to specially thank <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Core-2-Extreme/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Core-2-Extreme">@Core-2-Extreme</a>
  for implementing multithread decoding in his app <a href="https://github.com/Core-2-Extreme/Video_player_for_3DS/">Video
  Player for 3DS</a>, which made it possible to support o3ds.</p>

  <h2 dir="auto">New features</h2>

  <ul dir="auto">

  <li>Old 3DS support<br>

  Only 144p videos are supported, and there are some minor limitations</li>

  <li>Always play video on the top screen (when you are playing something in background)</li>

  <li>Added Home page</li>

  <li>Added self-updater integrated in the app (in Settings menu)</li>

  <li>Added equalizer</li>

  <li>SELECT + START to black out the bottom screen</li>

  <li>L/R to switch between tabs</li>

  <li>Added an option to configure the ratio of forward and backward buffer</li>

  </ul>

  <h2 dir="auto">Changes to existing features</h2>

  <ul dir="auto">

  <li>Debug log keycombo is now SELECT + X instead of SELECT only</li>

  <li>Subscription menu has been integrated into the Home page</li>

  <li>Network framework option deleted(now libcurl is always used)</li>

  <li>Removed dislike counter from the app as YouTube no longer shows it</li>

  </ul>

  <h2 dir="auto">Performance</h2>

  <ul dir="auto">

  <li>HTTP/2 multiplexing support (subscription feed loading is now super fast!)</li>

  <li>Use HTTP content encoding(brotli) (3x faster page loading in some cases)</li>

  <li>Use YouTube json endpoints(faster) instead of html page</li>

  <li>Use icons that are smaller but still clear enough for 3DS</li>

  <li>Faster YouTube parser</li>

  <li>Faster characters drawing</li>

  <li>Use rapidjson instead of json11</li>

  </ul>

  <h2 dir="auto">Bugfixes/Improvements</h2>

  <ul dir="auto">

  <li>Fixed high memory consumption after continuously playing a long video</li>

  <li>Fixed watch history and channel subscription disappear when one of the items
  contains certain characters(such as double quotes)</li>

  <li>Fixed audio only mode getting enabled when it shouldn''t</li>

  <li>Fixed the unnecessary icon reloading in the subscription menu</li>

  <li>Fixed some crashes</li>

  <li>General error handling improvements</li>

  </ul>

  <h2 dir="auto">Internals</h2>

  <ul dir="auto">

  <li>Updated stb_image to v2.27</li>

  <li>Updated libcurl to 7.82.0</li>

  </ul>'
updated: '2022-05-25T12:36:42Z'
version: v0.5.0
version_title: Release v0.5.0
website: https://gbatemp.net/threads/release-thirdtube-a-homebrew-youtube-client-for-the-new-3ds.591696/
---
