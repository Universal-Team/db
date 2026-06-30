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
  thextech-3ds-assets-aod-v1.3.7.3.zip:
    size: 60025376
    size_str: 57 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.3-1/thextech-3ds-assets-aod-v1.3.7.3.zip
  thextech-3ds-assets-smbx13-v1.3.7.3.zip:
    size: 48012828
    size_str: 45 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.3-1/thextech-3ds-assets-smbx13-v1.3.7.3.zip
  thextech-3ds-v1.3.7.3.zip:
    size: 4225243
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.3-1/thextech-3ds-v1.3.7.3.zip
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
stars: 400
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">This is a hotfix release for the 1.3.7.3 since there
  are serious bugs were been found and were been fixed.</p>

  <p dir="auto">You can read details for the original release here: <a href="https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7.3">https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7.3</a></p>

  <h2 dir="auto">Hotfix changelog 1.3.7.3-hotfix1:</h2>

  <ul dir="auto">

  <li>Adjusted the IME start logic to enable it when direct text input is enabled
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fixed build on FreeBSD (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>
  and also contributed by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Renkoto/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Renkoto">@Renkoto</a>)</li>

  <li>Fixed behaviour of the MD5 algorithm on Big Endian hardware (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li><em>Fixed a critical bug of checkpoints being reset when re-entering normal
  level from the hub</em> (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed TheXTech bug where medals were incorrectly saved after death in hub worlds
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <hr>

  <p dir="auto">All the downloads at the official site has been replaced with hotfix
  builds.</p>'
updated: '2026-06-22T20:49:35Z'
version: v1.3.7.3-1
version_title: 'TheXTech v1.3.7.3-1: A hotfix for 1.3.7.3 release'
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
<li>Download <code>thextech-3ds-v1.3.7.3.zip</code></li>
<li>Extract <code>/thextech-3ds/thextech.3dsx</code> from the zip to <code>/3ds/thextech.3dsx</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[git] thextech.3dsx</summary>
<ol>
<li>Download <code>thextech-3ds-main.zip</code></li>
<li>Extract <code>/thextech-3ds/thextech.3dsx</code> from the zip to <code>/3ds/thextech.3dsx</code> on your SD card</li>
</ol>
</details>

