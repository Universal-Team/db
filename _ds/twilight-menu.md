---
author: DS-Homebrew
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v16.5.0
downloads:
  TWiLightMenu-3DS.7z:
    size: 28260477
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v16.5.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 28238711
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v16.5.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 41309820
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v16.5.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 41921296
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v16.5.0/TWiLightMenu.7z
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
  TWiLight Menu++ Nightly:
  - file: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-3DS.7z
    message: Downloading TWiLight Menu++ (Nightly)...
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
  TWiLight Menu++ Nightly (Lite):
  - file: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Lite.7z
    message: Downloading TWiLight Menu++ Nightly (Lite)...
    output: /TWiLightMenu.7z
    type: downloadFile
  - file: /TWiLightMenu.7z
    input: TWiLightMenu/_nds/
    message: Extracting TWiLight Menu++ Nightly (Lite)...
    output: /_nds/
    type: extractFile
  - file: /TWiLightMenu.7z
    input: TWiLightMenu/3DS - CFW users/
    message: Extracting TWiLight Menu++ Nightly (Lite)...
    output: /
    type: extractFile
  - file: /TWiLightMenu.7z
    input: TWiLightMenu/DSi&3DS - SD card users/
    message: Extracting TWiLight Menu++ Nightly (Lite)...
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
  TWiLight Menu++ Release:
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
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
updated: '2020-10-14T01:34:25Z'
version: v16.5.0
version_title: 'Hacktober (2020) release #2'
wiki: https://github.com/DS-Homebrew/TWiLightMenu/wiki
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://github.com/DS-Homebrew/TWiLightMenu/wiki) for help installing.