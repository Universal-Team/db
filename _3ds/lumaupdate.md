---
author: KunoichiZ
autogen_scripts: true
categories:
- utility
color: '#9ae1d2'
created: '2017-04-26T01:20:59Z'
description: Updater for Luma3DS
download_page: https://github.com/KunoichiZ/lumaupdate/releases/tag/v2.5
downloads:
  lumaupdater-2.5.zip:
    size: 2009306
    url: https://github.com/KunoichiZ/lumaupdate/releases/download/v2.5/lumaupdater-2.5.zip
  lumaupdater.cia:
    size: 1468352
    url: https://github.com/KunoichiZ/lumaupdate/releases/download/v2.5/lumaupdater.cia
github: KunoichiZ/lumaupdate
icon: https://raw.githubusercontent.com/KunoichiZ/lumaupdate/master/meta/icon.png
image: https://avatars1.githubusercontent.com/u/19984244?v=4
layout: app
license: wtfpl
license_name: Do What The F*ck You Want To Public License
qr:
  lumaupdater.cia: https://db.universal-team.net/assets/images/qr/lumaupdater.cia.png
screenshots:
- description: Release notes
  url: https://db.universal-team.net/assets/images/screenshots/lumaupdate/release-notes.png
scripts:
  lumaupdater.3dsx:
  - file: lumaupdater.*\.zip
    message: Downloading lumaupdater.zip...
    output: /lumaupdater.zip
    repo: author/repo
    type: downloadRelease
  - file: /lumaupdater.zip
    input: 3ds/lumaupdater/lumaupdater.3dsx
    message: Extracting lumaupdater.3dsx...
    output: '%3DSX%/lumaupdater.3dsx'
    type: extractFile
  - file: /lumaupdater.zip
    message: Deleting lumaupdater.zip...
    type: deleteFile
source: https://github.com/KunoichiZ/lumaupdate
systems:
- 3DS
title: lumaupdate
update_notes: <p>This update fixes the error in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="572902112" data-permission-text="Title
  is private" data-url="https://github.com/KunoichiZ/lumaupdate/issues/49" data-hovercard-type="issue"
  data-hovercard-url="/KunoichiZ/lumaupdate/issues/49/hovercard" href="https://github.com/KunoichiZ/lumaupdate/issues/49">#49</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="573355357"
  data-permission-text="Title is private" data-url="https://github.com/KunoichiZ/lumaupdate/issues/50"
  data-hovercard-type="issue" data-hovercard-url="/KunoichiZ/lumaupdate/issues/50/hovercard"
  href="https://github.com/KunoichiZ/lumaupdate/issues/50">#50</a>, and <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="573445772" data-permission-text="Title
  is private" data-url="https://github.com/KunoichiZ/lumaupdate/issues/51" data-hovercard-type="issue"
  data-hovercard-url="/KunoichiZ/lumaupdate/issues/51/hovercard" href="https://github.com/KunoichiZ/lumaupdate/issues/51">#51</a>
  and closes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="572902112" data-permission-text="Title is private" data-url="https://github.com/KunoichiZ/lumaupdate/issues/49"
  data-hovercard-type="issue" data-hovercard-url="/KunoichiZ/lumaupdate/issues/49/hovercard"
  href="https://github.com/KunoichiZ/lumaupdate/issues/49">#49</a>. This update should
  now allow you to download Luma3DS and any future releases of Luma Updater.</p>
updated: '2020-02-29T22:55:37Z'
version: v2.5
version_title: Fix for v2.4
website: https://gbatemp.net/threads/release-luma-updater.471739/
---
