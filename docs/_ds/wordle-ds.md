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
    size: 1264832
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v3.0.0/WordleDS.cia
  WordleDS.dsi:
    size: 1250240
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v3.0.0/WordleDS.dsi
  WordleDS.nds:
    size: 1250240
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v3.0.0/WordleDS.nds
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

  <li>The word order is now synchronized from the internet to remove the need to update
  the whole game frequently

  <ul dir="auto">

  <li>Unfortunately this requires a WEP router in-app, however 3DS users can use Universal-Updater
  (it''ll automatically download the latest list on update and there''s a manual entry
  for it too) and I also made a little <a href="https://github.com/Epicpkmn11/WordleDS/blob/main/resources/update-words.py">Python
  script</a> which you can just put in <code class="notranslate">sd:/_nds/WordleDS/Wordle
  DS</code> and run on PC, can always just manually <a href="https://wordle.xn--rck9c.xn--tckwe/words.php?mode=mod.json"
  rel="nofollow">download it</a> too</li>

  </ul>

  </li>

  <li>Attempting to enable hard mode while playing now has a popup explaining why
  you can''t</li>

  </ul>

  <p dir="auto">Wow I just noticed that the 1st birthday of Wordle DS was back on
  February 13th, when I started this it was supposed to be a little one off thing
  that I just had a little fun making, released, and never worked on again. And here
  I am making v3.0.0 a year later. It''s not really <em>thaaat</em> major of a change
  all things considered, but with it being such a major change to the usage of the
  app I figured I''d give it the v3. Also, Wordle DS has an <a href="https://wordle.xn--rck9c.xn--tckwe"
  rel="nofollow">official webpage</a> now ;P</p>

  <hr>

  <p dir="auto"><code class="notranslate">WordleDS.nds</code> and <code class="notranslate">WordleDS.dsi</code>
  are identical except that the <code class="notranslate">.dsi</code> build has a
  title ID so it can be installed using <a href="https://github.com/Epicpkmn11/NTM/releases">NTM</a>
  while the <code class="notranslate">.nds</code> build doesn''t so it works on flashcards.
  The <code class="notranslate">.cia</code> build can be used to install to the 3DS
  HOME Menu. Here''s QRs for FBI and dsidl:</p>

  <table role="table">

  <thead>

  <tr>

  <th>WordleDS.cia</th>

  <th>WordleDS.dsi</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/41608708/222622039-446b9781-01e9-498b-8ba0-cc2fb096ea7d.png"><img
  src="https://user-images.githubusercontent.com/41608708/222622039-446b9781-01e9-498b-8ba0-cc2fb096ea7d.png"
  alt="QR for WordleDS.cia" style="max-width: 100%;"></a></td>

  <td><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/41608708/222622042-213a850f-9879-4674-bb10-e73b202c2611.png"><img
  src="https://user-images.githubusercontent.com/41608708/222622042-213a850f-9879-4674-bb10-e73b202c2611.png"
  alt="QR for WordleDS.dsi" style="max-width: 100%;"></a></td>

  </tr>

  </tbody>

  </table>'
updated: '2023-03-03T03:12:28Z'
version: v3.0.0
version_title: Online word updates
website: https://wordle.xn--rck9c.xn--tckwe
wiki: https://github.com/Epicpkmn11/WordleDS/wiki
---
A clone of [Wordle](https://www.nytimes.com/games/wordle/index.html) for the Nintendo DS(i). It features the same word each day as the official Wordle and has most of the same features including statistics tracking, high contrast and hard mode options, and even sharable emoji grid via QR code or txt file. Also featuring custom original background music by Rocket Robz.