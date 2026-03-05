---
author: Pk11
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
    size: 972992
    size_str: 950 KiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v3.2.2/WordleDS.cia
  WordleDS.dsi:
    size: 958400
    size_str: 935 KiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v3.2.2/WordleDS.dsi
  WordleDS.nds:
    size: 958400
    size_str: 935 KiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v3.2.2/WordleDS.nds
github: Epicpkmn11/WordleDS
icon: https://db.universal-team.net/assets/images/icons/wordle-ds.gif
icon_static: https://raw.githubusercontent.com/Epicpkmn11/WordleDS/master/resources/icon/icon.0.png
image: https://db.universal-team.net/assets/images/icons/wordle-ds.gif
image_length: 3957
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/Epicpkmn11/WordleDS/releases/tag/dev
  downloads:
    WordleDS.cia:
      size: 972992
      size_str: 950 KiB
      url: https://github.com/Epicpkmn11/WordleDS/releases/download/dev/WordleDS.cia
    WordleDS.dsi:
      size: 958400
      size_str: 935 KiB
      url: https://github.com/Epicpkmn11/WordleDS/releases/download/dev/WordleDS.dsi
    WordleDS.nds:
      size: 958400
      size_str: 935 KiB
      url: https://github.com/Epicpkmn11/WordleDS/releases/download/dev/WordleDS.nds
  qr:
    WordleDS.cia: https://db.universal-team.net/assets/images/qr/git/wordleds-cia.png
    WordleDS.dsi: https://db.universal-team.net/assets/images/qr/git/wordleds-dsi.png
    WordleDS.nds: https://db.universal-team.net/assets/images/qr/git/wordleds-nds.png
  update_notes: '<p dir="auto">Pk11 - Download word list to RAM if no SD</p>

    <p dir="auto">Fixes melonDS (with DLDI off) and other environments with Wi-Fi
    but no SD when the words aren''t preloaded</p>'
  update_notes_md: 'Pk11 - Download word list to RAM if no SD


    Fixes melonDS (with DLDI off) and other environments with Wi-Fi but no SD when
    the words aren''t preloaded'
  updated: '2026-01-29T07:55:42Z'
  version: dev
  version_title: Continuous Build - 6fd6e63
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
stars: 67
systems:
- DS
title: Wordle DS
update_notes: '<p dir="auto">So uh, turns out due to the Times reusing a few words
  my API had fallen out of sync "^^. This release contains a few fixes to both rectify
  that and make sure it''s far less likely to ever happen again.</p>

  <ul dir="auto">

  <li>The word list in ROM is fixed to not be missing any words, and my server''s
  database has been fixed

  <ul dir="auto">

  <li>The database now keys on <code class="notranslate">days_since_launch</code>
  since that''s a true unique value, unlike word ID</li>

  </ul>

  </li>

  <li>Wordle DS now always downloads words from the current day, rather than the end
  of the list

  <ul dir="auto">

  <li>This is actually a huge improvement because the Times have actually changed
  words a few times after initially publishing them to the API, so this means that
  if you''re near Wi-Fi you can just always hit the update button before you play
  each day and it will 100% guarantee (barring my server breaking) that you''ve got
  the right word; while still keeping a cache so you can play without Wi-Fi</li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>If updating from an old version (unless using Universal-Updater
  which handles it automatically), make sure to do an update in app immediately or
  you may be playing from a messed up cache</strong></p>

  <hr>

  <p dir="auto"><code class="notranslate">WordleDS.nds</code> and <code class="notranslate">WordleDS.dsi</code>
  are identical except that the <code class="notranslate">.dsi</code> build has a
  title ID so it can be installed using <a href="https://github.com/Epicpkmn11/NTM/releases">NTM</a>
  while the <code class="notranslate">.nds</code> build doesn''t so it works on flashcards.
  The <code class="notranslate">.cia</code> build can be used to install to the 3DS
  HOME Menu. Here''s QRs for FBI and dsidl:</p>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>WordleDS.cia</th>

  <th>WordleDS.dsi</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/ac46ed86-5598-499d-ba0b-640b733b5710"><img
  src="https://github.com/user-attachments/assets/ac46ed86-5598-499d-ba0b-640b733b5710"
  alt="QR for WordleDS.cia" style="max-width: 100%;"></a></td>

  <td><a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/40cf7a85-49e3-4667-a01f-32662beded7d"><img
  src="https://github.com/user-attachments/assets/40cf7a85-49e3-4667-a01f-32662beded7d"
  alt="QR for WordleDS.dsi" style="max-width: 100%;"></a></td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>'
updated: '2026-01-19T04:22:39Z'
version: v3.2.2
version_title: Word list fixes
website: https://wordle.xn--rck9c.xn--tckwe
wiki: https://github.com/Epicpkmn11/WordleDS/wiki
---
A clone of [Wordle](https://www.nytimes.com/games/wordle/index.html) for the Nintendo DS(i). It features the same word each day as the official Wordle and has most of the same features including statistics tracking, high contrast and hard mode options, and even sharable emoji grid via QR code or txt file. Also featuring custom original background music by Rocket Robz.