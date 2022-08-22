---
author: Pk11
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- game
color: '#9cc898'
color_bg: '#638061'
created: '2022-02-14T05:51:08Z'
description: A clone of Wordle for the Nintendo DS(i)
download_page: https://github.com/Epicpkmn11/WordleDS/releases
downloads:
  WordleDS.cia:
    size: 1110208
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v2.1.0/WordleDS.cia
  WordleDS.dsi:
    size: 1095616
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v2.1.0/WordleDS.dsi
  WordleDS.nds:
    size: 1095616
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v2.1.0/WordleDS.nds
github: Epicpkmn11/WordleDS
icon: https://db.universal-team.net/assets/images/icons/wordle-ds.gif
icon_static: https://raw.githubusercontent.com/Epicpkmn11/WordleDS/master/resources/icon/icon.0.png
image: https://db.universal-team.net/assets/images/icons/wordle-ds.gif
image_length: 3957
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  WordleDS.cia: https://db.universal-team.net/assets/images/qr/wordleds-cia.png
  WordleDS.dsi: https://db.universal-team.net/assets/images/qr/wordleds-dsi.png
  WordleDS.nds: https://db.universal-team.net/assets/images/qr/wordleds-nds.png
screenshots:
- description: How to play
  url: https://db.universal-team.net/assets/images/screenshots/wordle-ds/how-to-play.png
- description: Main menu
  url: https://db.universal-team.net/assets/images/screenshots/wordle-ds/main-menu.png
- description: Settings
  url: https://db.universal-team.net/assets/images/screenshots/wordle-ds/settings.png
- description: Statistics
  url: https://db.universal-team.net/assets/images/screenshots/wordle-ds/statistics.png
source: https://github.com/Epicpkmn11/WordleDS
systems:
- DS
title: Wordle DS
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Wordle DS now tracks how long it takes you finish

  <ul dir="auto">

  <li>Your average completion time will be displayed in the statistics menu</li>

  <li>It can also optionally be included in the share message thanks to...</li>

  </ul>

  </li>

  <li>Added a new option to the settings menu for customizing the share message, allowing
  you to include your completion time and/or current streak</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed a bug in the image reading that was slowing it down and making Wordle
  DS fail crash from GodMode9i and melonDS</li>

  <li>Fixed a bug where it was attempting to create its folders even when it had no
  SD card causing a crash in melonDS without DLDI/SD</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>Completion time tracking doesn''t work on any emulator besides no$gba unless
  you close and open the lid before inputting your answer</li>

  </ul>

  <hr>

  <p dir="auto"><code class="notranslate">WordleDS.nds</code> and <code class="notranslate">WordleDS.dsi</code>
  are identical except that the <code class="notranslate">.dsi</code> build has a
  title ID so it can be installed using <a href="https://github.com/JeffRuLz/TMFH/releases">TMFH</a>
  or <a href="https://github.com/Epicpkmn11/NTM/releases">NTM</a> while the <code
  class="notranslate">.nds</code> build doesn''t so it works on flashcards. The <code
  class="notranslate">.cia</code> build can be used to install to the 3DS HOME Menu,
  here''s a QR:</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/41608708/185937357-a2c904ec-91d9-4af6-8fce-ab663549aacf.png"><img
  src="https://user-images.githubusercontent.com/41608708/185937357-a2c904ec-91d9-4af6-8fce-ab663549aacf.png"
  alt="QR code for WordleDS.cia" style="max-width: 100%;"></a></p>'
updated: '2022-08-22T13:53:29Z'
version: v2.1.0
version_title: Completion timer
wiki: https://github.com/Epicpkmn11/WordleDS/wiki
---
A clone of [Wordle](https://www.nytimes.com/games/wordle/index.html) for the Nintendo DS(i). It features the same word each day as the official Wordle and has most of the same features including statistics tracking, high contrast and hard mode options, and even sharable emoji grid via QR code or txt file. Also featuring custom original background music by Rocket Robz.