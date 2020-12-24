---
author: DS-Homebrew
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v17.2.1
downloads:
  TWiLightMenu-3DS.7z:
    size: 30138581
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.1/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 30141219
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.1/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 43235195
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.1/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 43640160
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v17.2.1/TWiLightMenu.7z
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
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: '<p>Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul>

  <li><a href="https://github.com/DS-Homebrew/TWiLightMenu/wiki/updating-%28flashcard%29">Flashcard</a>
  (Strongly recommended!)</li>

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

  <li>Atari 7800 has been added to TWLMenu++ Virtual Console!

  <ul>

  <li>Included emulator is A7800DS, developed by Alekmaul, and improved by <a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/wavemotion-dave/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/wavemotion-dave">@wavemotion-dave</a></li>

  <li>ROMs must have the <code>.a78</code> file type.</li>

  </ul>

  </li>

  <li><strong>DS Phat/lite:</strong> If using an EZ-Flash Slot-2 card to run GBA games
  in native GBA mode, if the game does not use the SRAM save type, a message will
  be shown before the game boots, saying to SRAM-patch the ROM.</li>

  </ul>

  <p><strong>Improvement</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations!</li>

  </ul>

  <p><strong>Bug fixes (DS Phat/lite)</strong></p>

  <ul>

  <li>Fixed some GBA game compatibility in native mode (ex. <em>Namco Museum: 50th
  Anniversary</em>, <em>Kirby and the Amazing Mirror</em>).</li>

  <li>Fixed soft-lock sometimes occurring when restarting TWLMenu++ after running
  a GBA game in native mode.</li>

  <li>Fixed GBA games that are 16MB or less, not booting in native mode using an EZ-Flash
  Slot-2 card.

  <ul>

  <li>NOR flash is now always used, instead of PSRAM. PSRAM is now only used to store
  the rotating cube video for the 3DS theme.</li>

  </ul>

  </li>

  <li>Fixed slow patch speed when launching GBA games that use <code>FLASH512_V13X</code>
  save type.</li>

  </ul>'
updated: '2020-12-11T04:01:15Z'
version: v17.2.1
version_title: v17.2.1
wiki: https://github.com/DS-Homebrew/TWiLightMenu/wiki
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://github.com/DS-Homebrew/TWiLightMenu/wiki) for help installing.