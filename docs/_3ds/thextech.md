---
author: TheXTech Developers
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/160427994?v=4
categories:
- game
color: '#5f6dc0'
color_bg: '#3f4880'
created: '2020-02-12T20:02:49Z'
description: The full port of the SMBX engine from VB6 into C++ and SDL2, FreeImage
  and MixerX
download_filter: 3ds
download_page: https://github.com/TheXTech/TheXTech/releases
downloads: {}
github: TheXTech/TheXTech
icon: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/icon/thextech_48.png
image: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/wiiu/wuhb-splash.png
image_length: 121515
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  downloads:
    thextech-3ds-main.zip:
      url: https://builds.wohlsoft.ru/3ds/thextech-3ds-main.zip
screenshots:
- description: Editor
  url: https://db.universal-team.net/assets/images/screenshots/thextech/editor.png
- description: Loading
  url: https://db.universal-team.net/assets/images/screenshots/thextech/loading.png
- description: Smbx menu
  url: https://db.universal-team.net/assets/images/screenshots/thextech/smbx-menu.png
- description: Smbx title
  url: https://db.universal-team.net/assets/images/screenshots/thextech/smbx-title.png
source: https://github.com/TheXTech/TheXTech
stars: 340
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">This is a small hotfix release for the Windows to address
  serious graphical issues happens on Intel Iris Xe (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2666816824" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/859" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/859/hovercard" href="https://github.com/TheXTech/TheXTech/issues/859">#859</a>,
  this problem doesn''t gets reproduced on Linux, it happens on Windows exclusively)
  and black screen problem when running this under VirtualBox VM with OpenGL enabled.</p>

  <p dir="auto">This post contains Windows only builds, for other platforms, you can
  download packages <a href="https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7.1">at
  the main post here</a>.</p>

  <h2 dir="auto">Changelog:</h2>

  <ul dir="auto">

  <li>Added workaround for the texture corruption problem on Windows 10+ with the
  Intel Iris Xe GPU: the depth buffer will be completely disabled here to avoid glitches
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Implemented the proper initialisation of the OpenGL on VirtualBox''s SVGA3D
  driver (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>'
updated: '2025-07-20T22:51:02Z'
version: v1.3.7.1-1
version_title: 'TheXTech v1.3.7.1-hotfix: A Hotfix for Intel Iris Xe on Windows and
  VirtualBox'
website: https://wohlsoft.ru/projects/TheXTech/
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features. The original SMBX assets are not included, but a compatible preservation asset packs are available from wohlsoft.ru.