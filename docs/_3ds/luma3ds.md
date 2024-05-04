---
author: LumaTeam
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/65085206?v=4
categories:
- utility
- firm
- luma3ds
color: '#82e5d9'
color_bg: '#488079'
created: '2016-02-08T02:26:12Z'
description: Nintendo 3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases
downloads:
  Luma3DSv13.1.zip:
    size: 535953
    size_str: 523 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v13.1/Luma3DSv13.1.zip
github: LumaTeam/Luma3DS
image: https://avatars.githubusercontent.com/u/65085206?v=4&size=128
image_length: 7260
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LumaTeam/Luma3DS
systems:
- 3DS
title: Luma3DS
update_notes: '<ul dir="auto">

  <li>Add volume slider override

  <ul dir="auto">

  <li>Currently, this option is located under "System configuration" in the Rosalina
  menu and autosaves, while being under <code class="notranslate">[misc]</code> in
  <code class="notranslate">config.ini</code>. This is because this option is only
  supported for <code class="notranslate">NATIVE_FIRM</code>. This may change in the
  future</li>

  <li>When using the option, the console might sometimes take longer to shutdown</li>

  </ul>

  </li>

  <li>Add explicit "Boot chainloader" entry, above "Save and exit" in the boot configuration
  menu</li>

  <li>Remove unused and useless "Allow Left+Right / Up+Down combos for DSi" option</li>

  <li>Hide "Enable custom upscaling filters for DSi" option</li>

  <li>Fix an issue where baremetal screeninit would result in two white screens or
  wrong colors, usually when launching Arm9 payloads</li>

  <li>Rosalina: display SSID in "Force wifi connection" menu</li>

  <li>LayeredFS: improve game update RomFS mountpoint detection</li>

  <li>Further improvements to overall system stability and other minor adjustments
  have been made to enhance the user experience</li>

  </ul>

  <p dir="auto">In addition, with thanks to <a class="user-mention notranslate" data-hovercard-type="organization"
  data-hovercard-url="/orgs/devkitPro/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/devkitPro">@devkitPro</a>,
  this release of Luma3DS comes bundled with version 2.4.3 of the <a href="https://github.com/devkitPro/3ds-hbmenu">Homebrew
  Menu</a>, itself bundled with <code class="notranslate">config/ssl/cacert.pem</code>
  for use with libcurl.</p>'
updated: '2024-05-03T20:09:32Z'
version: v13.1
version_title: v13.1
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
