---
author: DS-Homebrew
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v17.2.0
downloads:
  TWiLightMenu-3DS.7z:
    size: 30084349
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 30093365
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 43185689
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 43597395
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.0/TWiLightMenu.7z
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
update_notes: '<p>Original release date: Dec 9, 2020, 1:36AM MST<br>

  Re-released to fix an overlooked bug in GBARunner2.</p>

  <p>Check here on how to update <strong>TW</strong>i<strong>L</strong>ight Menu++:</p>

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

  <li><strong>DS Phat/lite:</strong> You can now select a custom border to use in
  GBA mode!

  <ul>

  <li>Custom borders go in <code>/_nds/TWiLightMenu/gbaborders/</code>, and must be
  in <code>.png</code> format with the resolution of 256x192.</li>

  <li>Switch to the Games/Apps settings page to see the option.</li>

  </ul>

  </li>

  <li><a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/wavemotion-dave/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/wavemotion-dave">@wavemotion-dave</a>''s
  updated version (1.6) of StellaDS is now included!</li>

  </ul>

  <p><strong>Improvement (DS Phat/lite)</strong></p>

  <ul>

  <li>SRAM-patching GBA ROMs is no longer required!</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li><strong>DS Phat/lite:</strong> With native GBA ROM loading, most games will
  no longer crash after the GBA logo screen!

  <ul>

  <li><strong>NOTE:</strong> Before this version, your <code>.sav</code> file has
  became corrupted, if you used this feature. This is now fixed. To fix the corruption,
  grab a backup of the <code>.sav</code> file, if you have one.</li>

  </ul>

  </li>

  <li><strong>DS Phat/lite:</strong> Attempted to fix loading GBA ROMs above 16MB
  on EZ-Flash Slot-2 cards.</li>

  <li><strong>DS Phat/lite:</strong> Fixed non-GBA ROM being overwritten, when relaunching
  TWLMenu++ after launching a non-GBA game.</li>

  <li><strong>Flashcards:</strong> Fixed non-NDS games being moved to the <code>saves</code>
  folder, when relaunching TWLMenu++ after launching a non-NDS game.</li>

  <li><strong>DS Phat/lite:</strong> Fixed GBA border flickering before switching
  to GBA mode, when launching a GBA ROM.</li>

  </ul>

  <p><strong>Known bug (DS Phat/lite)</strong></p>

  <ul>

  <li>Due to SRAM size limitations, some GBA games with the save size of 128KB will
  show a message that the save is corrupt (ex. <em>Pokemon Emerald</em>).</li>

  </ul>'
updated: '2020-12-10T00:49:33Z'
version: v17.2.0
version_title: v17.2.0
wiki: https://github.com/DS-Homebrew/TWiLightMenu/wiki
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://github.com/DS-Homebrew/TWiLightMenu/wiki) for help installing.