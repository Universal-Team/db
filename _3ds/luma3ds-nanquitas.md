---
author: Nanquitas
categories:
- utility
- firm
- luma3ds
color: '#e39dd1'
created: '2018-06-22T08:47:04Z'
description: Noob-proof (N)3DS "Custom Firmware"
download_page: https://github.com/Nanquitas/Luma3DS/releases/tag/v10.2.1
downloads:
  boot.firm:
    size: 240640
    url: https://github.com/Nanquitas/Luma3DS/releases/download/v10.2.1/boot.firm
github: Nanquitas/Luma3DS
image: https://avatars3.githubusercontent.com/u/13298129?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  boot.firm:
  - file: boot.firm
    message: Downloading boot.firm...
    output: /boot.firm
    repo: Nanquitas/Luma3DS
    type: downloadRelease
source: https://github.com/Nanquitas/Luma3DS
systems:
- 3DS
title: Luma3DS (Nanquitas)
update_notes: "# About 3GX plugins\r\n## What are **.3gx** files?\r\n**.3GX** (**3**ds\
  \ **G**ame e**X**tension)  is a plugin file format (evolved from NTR's **.plg**\
  \ format) which allows extra C/C++/asm code to be loaded into an application at\
  \ runtime and then executed. \r\n## What can plugins do?\r\nAs the file format name\
  \ suggests, plugins can be used to extend game functionality, from game mods, to\
  \ trainers or cheat loaders. One example of a plugin is the [CTRPluginFramework\
  \ Blank Plugin](https://gbatemp.net/threads/ctrpluginframework-blank-plugin-now-with-action-replay.487729/).\r\
  \n## How can I install plugins?\r\nPlugins can be placed at 2 locations:\r\n - ``sd:/luma/plugins/<TITLEID>/<filename>.3gx``\
  \ to set a plugin for a specified title (higher priority)\r\n - ``sd:/luma/plugins/default.3gx``\
  \ to set a plugin which would be loaded for all games (lower priority)\r\n\r\nDefault\
  \ plugin is only loaded if no specific plugin is found.\r\n## How can I make my\
  \ own plugins?\r\nAn api is available to allow you to create your own plugins using\
  \ a menu easily.\r\nAn example is available [here](https://github.com/Nanquitas/Luma3DS-Plugin-sample)."
updated: '2020-11-17T11:21:13Z'
version: v10.2.1
version_title: v10.2.1 3GX Loader Edition
wiki: https://github.com/Nanquitas/Luma3DS/wiki
---
