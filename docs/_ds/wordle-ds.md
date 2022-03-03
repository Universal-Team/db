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
    size: 1097984
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v1.2.0/WordleDS.cia
  WordleDS.dsi:
    size: 1083392
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v1.2.0/WordleDS.dsi
  WordleDS.nds:
    size: 1083392
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v1.2.0/WordleDS.nds
github: Epicpkmn11/WordleDS
icon: https://db.universal-team.net/assets/images/icons/wordle-ds.png
icon_index: 201
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
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>There are now the proper messages on winning instead of just a generic "Congratulations!"

  <ul dir="auto">

  <li>I was originally too lazy to add proper text rending but then I did it anyways
  for the stats menu so there wasn''t a reason for that anymore</li>

  <li>The loss message is still different since I really like the animation I did
  for that ;P</li>

  </ul>

  </li>

  <li>Proper Unicode handling

  <ul dir="auto">

  <li>Doesn''t affect English Wordle at all, but if anyone wants to modify this for
  another language or such it''ll now be much easier; any European language should
  be as simple as editing a couple images, the keyboard layout, and the word lists</li>

  </ul>

  </li>

  <li>The current version number is now shown in the settings menu</li>

  </ul>

  <hr>

  <p dir="auto"><code>WordleDS.nds</code> and <code>WordleDS.dsi</code> are identical
  except that the <code>.dsi</code> build has a title ID so it can be installed using
  <a href="https://github.com/JeffRuLz/TMFH/releases">TMFH</a> or <a href="https://github.com/Epicpkmn11/NTM/releases">NTM</a>
  while the <code>.nds</code> build doesn''t so it works on flashcards. The <code>.cia</code>
  build can be used to install to the 3DS HOME Menu, here''s a QR:</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/41608708/156544809-7631253e-1372-4550-b06c-a06f258c96b1.png"><img
  src="https://user-images.githubusercontent.com/41608708/156544809-7631253e-1372-4550-b06c-a06f258c96b1.png"
  alt="QR code for WordleDS.cia" style="max-width: 100%;"></a></p>'
updated: '2022-03-03T10:42:58Z'
version: v1.2.0
version_title: Proper win messages
---
A clone of [Wordle](https://www.nytimes.com/games/wordle/index.html) for the Nintendo DS(i). It features the same word each day as the official Wordle and has most of the same features including statistics tracking, high contrast and hard mode options, and even makes a txt file with a sharable emoji grid.