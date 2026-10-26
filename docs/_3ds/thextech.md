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
downloads:
  thextech-3ds-v1.7.4.2.zip:
    size: 4227140
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.7.4.2-hotfix/thextech-3ds-v1.7.4.2.zip
github: TheXTech/TheXTech
icon: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/icon/thextech_48.png
image: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/wiiu/wuhb-splash.png
image_length: 121515
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
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
stars: 423
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">After the previous releases v1.7.4 and v1.7.4.1, the
  critical bug was discovered on 3DS and Wii platforms that makes some effects being
  invisible. The suitable builds were been replaced at the previous v1.7.4.1''s page
  as other platforms weren''t affected by this problem.</p>

  <p dir="auto">This post contains Nintendo 3DS and Nintendo Wii only builds, for
  other platforms, you can download packages <a href="https://github.com/TheXTech/TheXTech/releases/tag/v1.7.4.1">at
  the main post here</a>. Also, all the binaries had been updated at the main post
  to prevent users downloading faulty builds without knowlege of that.</p>

  <h1 dir="auto">Hotfix changelog for 1.7.4.2</h1>

  <ul dir="auto">

  <li>3DS / Wii: fix TheXTech 1.7.4.1 bug where NPC death effects would not display
  incorrectly. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>
  for the report)</li>

  </ul>'
updated: '2026-10-25T02:34:30Z'
version: v1.7.4.2-hotfix
version_title: 'TheXTech v1.7.4.2: A hotfix for 3DS and Wii'
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features. The original SMBX assets are not included, but a compatible preservation asset packs are available from wohlsoft.ru.

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>[assets] Adventures of Demo</summary>
<ol>
<li>Download <code>thextech-adventure-of-demo-assets-full-3ds.zip</code></li>
<li>Extract <code>/thextech-adventure-of-demo-assets-full-3ds.romfs</code> from the zip to <code>/3ds/thextech/assets-aod.romfs</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>thextech.3dsx</summary>
<ol>
<li>Download <code>thextech-3ds-v1.7.4.2.zip</code></li>
<li>Extract <code>/thextech-3ds/thextech.3dsx</code> from the zip to <code>/3ds/thextech.3dsx</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[git] thextech.3dsx</summary>
<ol>
<li>Download <code>thextech-3ds-main.zip</code></li>
<li>Extract <code>/thextech-3ds/thextech.3dsx</code> from the zip to <code>/3ds/thextech.3dsx</code> on your SD card</li>
</ol>
</details>

