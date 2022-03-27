---
author: Pk11
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- game
color: '#96c392'
color_bg: '#62805f'
created: '2022-02-14T05:51:08Z'
description: A clone of Wordle for the Nintendo DS(i)
download_page: https://github.com/Epicpkmn11/WordleDS/releases
downloads:
  WordleDS.cia:
    size: 1133824
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v1.3.1/WordleDS.cia
  WordleDS.dsi:
    size: 1119232
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v1.3.1/WordleDS.dsi
  WordleDS.nds:
    size: 1119232
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v1.3.1/WordleDS.nds
github: Epicpkmn11/WordleDS
icon: https://db.universal-team.net/assets/images/icons/wordle-ds.png
icon_index: 200
image: https://db.universal-team.net/assets/images/icons/wordle-ds.png
image_length: 630
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  WordleDS.cia: https://db.universal-team.net/assets/images/qr/wordleds-cia.png
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
update_notes: '<h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixes hard mode letter counts not being reloaded on close and reopen, allowing
  for guesses that were missing letter you knew</li>

  <li>Fixes green letters not being counted correctly for the letter counts in hard
  mode, breaking when you have one green and one yellow of the same letter</li>

  <li>Fixes hard mode not allowing making guesses with more than the known amount
  of letters</li>

  </ul>

  <h3 dir="auto">Other changes</h3>

  <ul dir="auto">

  <li><code>WordleDS.json</code> is now minified to not waste SD space, you can prettify
  it with tools such as <a href="http://jsonprettify.com" rel="nofollow">json prettify</a>
  if you need to edit it for whatever reason</li>

  </ul>

  <hr>

  <p dir="auto"><code>WordleDS.nds</code> and <code>WordleDS.dsi</code> are identical
  except that the <code>.dsi</code> build has a title ID so it can be installed using
  <a href="https://github.com/JeffRuLz/TMFH/releases">TMFH</a> or <a href="https://github.com/Epicpkmn11/NTM/releases">NTM</a>
  while the <code>.nds</code> build doesn''t so it works on flashcards. The <code>.cia</code>
  build can be used to install to the 3DS HOME Menu, here''s a QR:</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/41608708/160292827-c1f310a0-aa26-4dd0-b9ff-40b06835adad.png"><img
  src="https://user-images.githubusercontent.com/41608708/160292827-c1f310a0-aa26-4dd0-b9ff-40b06835adad.png"
  alt="QR code for WordleDS.cia" style="max-width: 100%;"></a></p>'
updated: '2022-03-27T17:14:50Z'
version: v1.3.1
version_title: Hard mode fixes
---
A clone of [Wordle](https://www.nytimes.com/games/wordle/index.html) for the Nintendo DS(i). It features the same word each day as the official Wordle and has most of the same features including statistics tracking, high contrast and hard mode options, and even makes a txt file with a sharable emoji grid.