---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
- save-tool
color: '#be8345'
created: '2018-10-02T16:59:38Z'
description: 'GodMode9i Explorer - A full access file browser for the Nintendo DS
  and DSi consoles :godmode:'
download_page: https://github.com/DS-Homebrew/GodMode9i/releases
downloads:
  GodMode9i.7z:
    size: 252456
    size_str: 246 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.0.0/GodMode9i.7z
github: DS-Homebrew/GodMode9i
icon: https://db.universal-team.net/assets/images/icons/godmode9i.png
icon_index: 11
image: https://raw.githubusercontent.com/DS-Homebrew/GodMode9i/master/resources/logo2.png
image_length: 44248
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds/blob/master/extras/GodMode9i.7z
  downloads:
    GodMode9i.7z:
      url: https://github.com/TWLBot/Builds/raw/master/extras/GodMode9i.7z
source: https://github.com/DS-Homebrew/GodMode9i
systems:
- DS
title: GodMode9i
update_notes: '<p dir="auto">All changes by <a class="user-mention" data-hovercard-type="user"
  data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  unless when noted.<br>

  There are too many changes to list, so the notable changes will be shown.</p>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li>DS(i) ROMs stored on NAND chips (ex. <em>Face Training</em>, <em>Jam with the
  Band</em>, and <em>WarioWare: DIY</em>) can now be dumped!</li>

  <li>EEPROM and FLASH save types are now supported when dumping GBA ROM and save
  files.</li>

  <li>A new font is now in use!</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Translations have been added!

  <ul dir="auto">

  <li>If installed as CIA or to directly boot via Unlaunch, you need to put either
  <code>GodMode9i.nds</code> or <code>GodMode9i.dsi</code> on the SD root, for them
  to work properly.</li>

  </ul>

  </li>

  <li>Pressing START will now bring up a START menu.</li>

  <li>Progress bar is now shown when dumping ROMs and copying/moving files.</li>

  </ul>

  <p dir="auto"><strong>Improvements</strong></p>

  <ul dir="auto">

  <li>Directory loading is now faster.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/RocketRobz/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/RocketRobz">@RocketRobz</a>)
  NAND is no longer read when detecting a DSi or 3DS console.</li>

  </ul>

  <p dir="auto"><strong>Bug fix</strong></p>

  <ul dir="auto">

  <li>Taking screenshots should now work everywhere.</li>

  </ul>'
updated: '2021-12-10T00:31:17Z'
version: v3.0.0
version_title: v3.0.0
website: https://wiki.ds-homebrew.com/godmode9i/
wiki: https://wiki.ds-homebrew.com/other/godmode9i
---
### Installation:
- TWiLight Menu++: Use either the `GodMode9i.nds` or `GodMode9i.dsi` file, they function identically with TWiLight Menu++
   - The only difference is that `GodMode9i.dsi` has a Title ID
- Flashcard: Use the `GodMode9i.nds` file
- hiyaCFW SDNAND: Install the `GodMode9i.dsi` file with [TMFH](/ds/tmfh)
- 3DS HOME Menu: Install the `GodMode9i.cia` file with [FBI](/3ds/fbi)

### Features:
- Dump GameBoy Advance cartridges on the original Nintendo DS and Nintendo DS Lite consoles.
- Dump Nintendo DS/DSi cartridges on Nintendo DSi and Nintendo 3DS consoles (if GodMode9i is ran on the console SD card).
- Copy, move, delete, rename files/folders and create folders.
- Mount the NitroFS of .nds files.
- Browse files on supported flashcards when running GM9i from the NAND or SD Card. (`AceKard 2(i)` & `R4 Ultra (r4ultra.com)`)