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
    size: 5744164
    size_str: 5 MiB
    url: https://github.com/windows-server-2003/ThirdTube/releases/download/v0.4.0/ThirdTube.3dsx
  ThirdTube.cia:
    size: 4084672
    size_str: 3 MiB
    url: https://github.com/windows-server-2003/ThirdTube/releases/download/v0.4.0/ThirdTube.cia
github: windows-server-2003/ThirdTube
icon: https://raw.githubusercontent.com/windows-server-2003/ThirdTube/main/resource/icon.png
icon_index: 185
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
update_notes: '<p dir="auto">Hello, I''m releasing a new version with the community
  posts support, basic audio editing options, and the ability to browse videos while
  playing another video.<br>

  Unfortunately, I have to tell you that I will be on a hiatus and temporarily leave
  from the development of ThirdTube for four months from now for personal reasons.<br>

  I''m glad if you remember this app when I come back.</p>

  <p dir="auto">Here is the changelog :</p>

  <ul dir="auto">

  <li>Separated the video player and the video page<br>

  This means you can now browse other videos while continuously playing one video.<br>

  It also means that a video doesn''t automatically play upon loading if another video
  is playing, so you have to press the "Play" button in the "General" tab</li>

  <li>Added support for community posts in the channel page<br>

  Animated images are currently not supported</li>

  <li>Added preamp, speed and pitch manipulators in the "Playback" tab</li>

  <li>Added playlist tab in the channel page</li>

  <li>The 3DS now doesn''t go into sleep mode so that the app can continue the playback<br>

  While the lid is closed, you can still listen to the audio through the headphone
  plug but not from the speaker because there seems to be no way to prevent it from
  being disabled</li>

  <li>Introduced thumb up/down icon to indicate like/dislike in the video page</li>

  <li>Added like counters on comments and replies</li>

  <li>Improved network performance when libcurl is chosen as the network framework
  and a redirect occurs on a video/audio stream</li>

  <li>Improved the behavior when one of the subscribed channels changes its icon</li>

  <li>Improved the performance and memory usage of the subscribed channels scene</li>

  <li>Improved the behavior of option selector when you grab it and scroll</li>

  <li>Made it to retry when a minor network error occurs</li>

  <li>Fixed random crashes when trying to play a video<br>

  Tips : it had the possibility of crashing after loading 17th video counting from
  the startup of the app</li>

  <li>Fixed crashes when exiting the app while loading something (video page, comments
  continuation, etc.)</li>

  <li>Fixed the throttling by YouTube which came back due to a change in one of their
  javascripts</li>

  <li>Fixed long loading and possible crashes when trying to seek near the end of
  the video</li>

  <li>Fixed terrible audio for some video (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1030176577" data-permission-text="Title is private" data-url="https://github.com/windows-server-2003/ThirdTube/issues/53"
  data-hovercard-type="issue" data-hovercard-url="/windows-server-2003/ThirdTube/issues/53/hovercard"
  href="https://github.com/windows-server-2003/ThirdTube/issues/53">#53</a>)</li>

  <li>Fixed memory leaks when video loading fails</li>

  <li>Implemented a workaround for <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1028279176" data-permission-text="Title is private" data-url="https://github.com/windows-server-2003/ThirdTube/issues/47"
  data-hovercard-type="issue" data-hovercard-url="/windows-server-2003/ThirdTube/issues/47/hovercard"
  href="https://github.com/windows-server-2003/ThirdTube/issues/47">#47</a> (240p
  or below fails to load for some videos)</li>

  </ul>'
updated: '2021-11-28T15:33:37Z'
version: v0.4.0
version_title: Release v0.4.0
website: https://gbatemp.net/threads/release-thirdtube-a-homebrew-youtube-client-for-the-new-3ds.591696/
---
