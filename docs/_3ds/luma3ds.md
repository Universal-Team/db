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
description: Noob-proof (N)3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases
downloads:
  Luma3DSv10.2.zip:
    size: 359574
    size_str: 351 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v10.2/Luma3DSv10.2.zip
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

  <li>Massively improved the screenshot feature:

  <ul dir="auto">

  <li><strong>Now takes around 100ms instead of 10s</strong> (speed may vary, and
  the first screenshot in a series is slower)</li>

  <li>800px top-screen mode is now supported</li>

  <li>Rosalina menu options have been reordered to take this into account</li>

  </ul>

  </li>

  <li>Added brightness (luminance) selection submenu</li>

  <li>Screen filters submenu improvements:

  <ul dir="auto">

  <li>Changed the filter values, and there are now more of them</li>

  <li>The selected filter is now properly restored when the lid is reopened</li>

  </ul>

  </li>

  <li>Removed the lag and crash associated to InputRedirection (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Nanquitas/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Nanquitas">@Nanquitas</a>)

  <ul dir="auto">

  <li>On N3DS, this may cause a key press to be repeated in Home Menu for no reason.
  Just pressing ZL/ZR on the console is enough to fix this</li>

  </ul>

  </li>

  <li>Improved Rosalina menu handling:

  <ul dir="auto">

  <li>C-Pad (left pad) can now be used to navigate the menu</li>

  <li>You can now easily scroll through the menus by maintaining directional keys</li>

  <li>InputRedirection can now be used to access and navigate the menu</li>

  <li>New key options for the menu combo: C-Pad Left/Right/Up/Down &amp; "Touch Screen
  Pressed" (sorry, no ZL/ZR)</li>

  </ul>

  </li>

  <li>Removed the need for the console to reboot again when switching to homebrew
  from a higher-memory game (e.g. Pokémon Sun on O3DS -&gt; configured homebrew title)</li>

  <li>Homebrew can now write to the shared config page</li>

  <li>Fixed the fact that the console would hang if sleep mode was entered when the
  Rosalina menu was open</li>

  <li>Enabling either the debugger or InputRedirection will now prevent the console
  from going to sleep until both are disabled (to prevent the console from hanging)</li>

  <li>Rosalina is now supported on N3DS <code class="notranslate">SAFE_FIRM</code>,
  including the homebrew launching functionality that comes with it:

  <ul dir="auto">

  <li>This is controlled by a new option in the main Luma menu. That option also enables
  running 11.3-and-below system versions on N2DS and also allows the system to run
  even with defective head-tracking hardware</li>

  <li>The newest release of the Homebrew Menu needs to be used (it comes bundled with
  Luma3DS in this release archive). You also need to rebuild all your homebrew with
  the latest libctru release. Some homebrew may not work, nevertheless</li>

  <li>Some Rosalina features may not work properly there (e.g. the brightness and
  New 3DS submenus)</li>

  </ul>

  </li>

  <li>Separated the exception dump parser script to a new repository: <a href="https://github.com/LumaTeam/luma3ds_exception_dump_parser">https://github.com/LumaTeam/luma3ds_exception_dump_parser</a></li>

  </ul>

  <p dir="auto">In addition, with thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/fincs/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/fincs">@fincs</a>,
  this release of Luma3DS comes bundled with version 2.2.0 of the <a href="https://github.com/fincs/new-hbmenu">Homebrew
  Menu</a>. (EDIT: replaced by hotfixed version)</p>'
updated: '2020-07-16T17:33:28Z'
version: v10.2
version_title: v10.2
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
