---
author: DS-Homebrew
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v17.1.1
downloads:
  TWiLightMenu-3DS.7z:
    size: 30024531
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.1.1/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 30031081
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.1.1/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 43124707
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.1.1/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 43528527
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.1.1/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
image: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/logo.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    TWiLightMenu-3DS.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-3DS.7z
    TWiLightMenu-DSi.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-DSi.7z
    TWiLightMenu-Flashcard.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Flashcard.7z
    TWiLightMenu-Lite.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Lite.7z
    TWiLightMenu.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu.7z
scripts:
  TWiLight Menu++:
  - file: TWiLightMenu-3DS.7z
    message: Downloading TWiLight Menu++...
    output: /TWiLightMenu-3DS.7z
    repo: DS-Homebrew/TWiLightMenu
    type: downloadRelease
  - file: /TWiLightMenu-3DS.7z
    input: ''
    message: Extracting TWiLight Menu++...
    output: /
    type: extractFile
  - file: /TWiLight Menu.cia
    message: Installing TWiLight Menu++...
    type: installCia
  - file: /TWiLight Menu - Game booter.cia
    message: Installing TWiLight Menu - Game booter...
    type: installCia
  - file: /TWiLight Menu - Game booter.cia
    type: deleteFile
  - file: /TWiLight Menu.cia
    type: deleteFile
  - file: /TWiLightMenu-3DS.7z
    type: deleteFile
  '[nightly lite] TWiLight Menu++':
  - file: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Lite.7z
    message: Downloading TWiLight Menu++...
    output: /TWiLightMenu.7z
    type: downloadFile
  - file: /TWiLightMenu.7z
    input: TWiLightMenu/_nds/
    message: Extracting TWiLight Menu++...
    output: /_nds/
    type: extractFile
  - file: /TWiLightMenu.7z
    input: TWiLightMenu/3DS - CFW users/
    message: Extracting TWiLight Menu++...
    output: /
    type: extractFile
  - file: /TWiLightMenu.7z
    input: TWiLightMenu/DSi&3DS - SD card users/
    message: Extracting TWiLight Menu++...
    output: /
    type: extractFile
  - file: /TWiLight Menu.cia
    message: Installing TWiLight Menu++...
    type: installCia
  - file: /TWiLight Menu - Game booter.cia
    message: Installing TWiLight Menu - Game booter...
    type: installCia
  - file: /TWiLight Menu - Game booter.cia
    type: deleteFile
  - file: /TWiLight Menu.cia
    type: deleteFile
  - file: /TWiLightMenu.7z
    type: deleteFile
  '[nightly] TWiLight Menu++':
  - file: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-3DS.7z
    message: Downloading TWiLight Menu++...
    output: /TWiLightMenu-3DS.7z
    type: downloadFile
  - file: /TWiLightMenu-3DS.7z
    input: TWiLightMenu/
    message: Extracting TWiLight Menu++...
    output: /
    type: extractFile
  - file: /TWiLight Menu.cia
    message: Installing TWiLight Menu++...
    type: installCia
  - file: /TWiLight Menu - Game booter.cia
    message: Installing TWiLight Menu - Game booter...
    type: installCia
  - file: /TWiLight Menu - Game booter.cia
    type: deleteFile
  - file: /TWiLight Menu.cia
    type: deleteFile
  - file: /TWiLightMenu-3DS.7z
    type: deleteFile
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: '<p>Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul>

  <li><a href="https://github.com/DS-Homebrew/TWiLightMenu/wiki/updating-%28flashcard%29">Flashcard</a></li>

  <li><a href="https://github.com/DS-Homebrew/TWiLightMenu/wiki/updating-%28dsi%29">DSi</a></li>

  <li><a href="https://github.com/DS-Homebrew/TWiLightMenu/wiki/updating-%283ds%29">3DS</a>

  <ul>

  <li><a href="https://github.com/DS-Homebrew/TWiLightMenu/wiki/updating-%283ds,-universal-updater%29">Universal-Updater</a></li>

  <li><a href="https://github.com/DS-Homebrew/TWiLightMenu/wiki/updating-%283ds,-manual%29">Manual</a></li>

  </ul>

  </li>

  </ul>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>(<strong>Not tested!</strong>) With M3 and SuperCard Slot-2 cards being supported,
  G6 and EZ-Flash are now supported as well!<br>

  Most Slot-2 cards with it''s own RAM (except the DS Memory Expansion Pak) can now
  be used for native GBA ROM loading!

  <ul>

  <li>For EZ-Flash, if the launched GBA ROM is larger than 16MB, the NOR Flash chip
  will be used instead of the PSRAM.</li>

  </ul>

  </li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations!</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>Attempted to fix GBA ROM not being loaded into the Slot-2 card''s RAM.</li>

  <li>Fixed ROM being loaded instead of the .sav file, into the card''s SRAM.</li>

  <li>File copy buffer is now 32KB (previously 256KB) as originally intended, and
  frees up a bit of memory.</li>

  </ul>'
updated: '2020-11-28T16:13:13Z'
version: v17.1.1
version_title: v17.1.1
wiki: https://github.com/DS-Homebrew/TWiLightMenu/wiki
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://github.com/DS-Homebrew/TWiLightMenu/wiki) for help installing.