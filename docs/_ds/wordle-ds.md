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
    size: 1209536
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v2.2.0/WordleDS.cia
  WordleDS.dsi:
    size: 1194944
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v2.2.0/WordleDS.dsi
  WordleDS.nds:
    size: 1194944
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/WordleDS/releases/download/v2.2.0/WordleDS.nds
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

  <li>(<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ItsSiem/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ItsSiem">@ItsSiem</a>
  and me) Added infinite mode

  <ul dir="auto">

  <li>Randomly picks words instead of daily</li>

  <li>Stats are stored separately from daily mode</li>

  <li>Streak only breaks on fail/skip, not missing a day</li>

  </ul>

  </li>

  <li>The Times has hired an editor<sup><a href="https://www.theverge.com/2022/11/7/23445167/wordle-the-new-york-times-editor-tracy-bennett"
  rel="nofollow">[1]</a></sup> so now words are no longer completely random

  <ul dir="auto">

  <li>Currently words until Christmas Eve are public, so expect an update by Christmas</li>

  </ul>

  </li>

  <li>The timer now pauses when sleeping and works on non-no$gba emulators</li>

  <li>There is now a fade effect between all menus to hide any glitchy texture changes</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li>Fixed a regression where it failed to load before Wordle 0

  <ul dir="auto">

  <li>Note: Negative Wordles are not guaranteed to stay the same between versions,
  especially with the now more frequent word list updates</li>

  </ul>

  </li>

  </ul>

  <hr>

  <p dir="auto"><code class="notranslate">WordleDS.nds</code> and <code class="notranslate">WordleDS.dsi</code>
  are identical except that the <code class="notranslate">.dsi</code> build has a
  title ID so it can be installed using <a href="https://github.com/JeffRuLz/TMFH/releases">TMFH</a>
  or <a href="https://github.com/Epicpkmn11/NTM/releases">NTM</a> while the <code
  class="notranslate">.nds</code> build doesn''t so it works on flashcards. The <code
  class="notranslate">.cia</code> build can be used to install to the 3DS HOME Menu,
  here''s a QR:</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/41608708/200749765-89d48516-6e2c-4601-9723-b82d6e1c5b14.png"><img
  src="https://user-images.githubusercontent.com/41608708/200749765-89d48516-6e2c-4601-9723-b82d6e1c5b14.png"
  alt="QR code for WordleDS.cia" style="max-width: 100%;"></a></p>'
updated: '2022-11-09T05:53:18Z'
version: v2.2.0
version_title: Infinite mode and word list update
wiki: https://github.com/Epicpkmn11/WordleDS/wiki
---
A clone of [Wordle](https://www.nytimes.com/games/wordle/index.html) for the Nintendo DS(i). It features the same word each day as the official Wordle and has most of the same features including statistics tracking, high contrast and hard mode options, and even sharable emoji grid via QR code or txt file. Also featuring custom original background music by Rocket Robz.