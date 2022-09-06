---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 511883
    size_str: 499 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.64.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1205068
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.64.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
image_length: 5116
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.3.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.3.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>DSiWare playability on DS Phat/Lite is finally out of it''s proof-of-concept
  stage, as you can now save your data, along with 100 titles now supported (plus
  a few more, if you''re using a DS Debug console)!

  <ul dir="auto">

  <li>A custom <code class="notranslate">.sav</code> format is used for flashcard
  DSiWare save files (featuring a "save exist" flag and save size at the end of the
  file).</li>

  <li><em>Shantae: Risky''s Revenge</em> can now get past the first two battles using
  an existing save file!</li>

  <li>Scroll down to see which titles are now supported to play on DS Phat/Lite.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations and added Ryukyuan language.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Communication errors should no longer occur in games with local multiplayer
  (ex. <em>Mario Kart DS</em>)!</li>

  <li>Certain DS games no longer have issues with TWL clock speed!</li>

  <li>Fixed some pre-loadable ROMs not booting (ex. <em>Clubhouse Games</em>).</li>

  <li>Fixed some pre-loaded ROMs with the expanded space not reading split data properly.

  <ul dir="auto">

  <li><em>Mario Kart DS</em> no longer crashes when starting the Mushroom Cup.</li>

  </ul>

  </li>

  <li>Fixed more DS games with weird arm9 start address not booting (ex. <em>Spider-Man
  2</em>, <em>Urusei Yatsura: Endless Summer</em>, etc.).</li>

  <li>Other minor fixes.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>Not all DSiWare titles can save on the DS Phat/Lite, due to the difficulty of
  adding save support for them, and/or them storing more than one file in the save
  filesystem.</li>

  <li><em>WarioWare: Touched!</em> (DSiWare <em>DL</em> version) does not play audio
  on both DS retail and debug models due to it taking more than 4MB/8MB of RAM, using
  almost of the DSi''s RAM.</li>

  </ul>

  <h2 dir="auto">Newly supported DSiWare titles on retail &amp; debug DS consoles</h2>

  <p dir="auto">Click <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/5dce98a0ef0e73c5831b01a9841fcdef17d6c388/universal/include/compatibleDSiWareMap.h">here</a>
  for the full list.</p>

  <ul dir="auto">

  <li>40-in-1: Explosive Megamix</li>

  <li>Amakuchi! Dairoujou</li>

  <li>Anonymous Notes 1: From The Abyss</li>

  <li>Anonymous Notes 2: From The Abyss</li>

  <li>Anonymous Notes 3: From The Abyss</li>

  <li>Anonymous Notes 4: From The Abyss</li>

  <li>Beauty Academy</li>

  <li>Cake Ninja (Previously only supported on debug consoles)</li>

  <li>Chuukara! Dairoujou</li>

  <li>Fashion Tycoon (USA only)</li>

  <li>Model Academy</li>

  <li>Mr. Driller: Drill Till You Drop</li>

  <li>Orion''s Odyssey</li>

  <li>Paul''s Monster Adventure</li>

  <li>GO Series: Picdun</li>

  <li>Picture Perfect: Pocket Stylist</li>

  <li>SnowBoard Xtreme</li>

  <li>Unou to Sanougaren Sasuru: Uranoura</li>

  <li>VT Tennis</li>

  <li>WarioWare: Touched! DL</li>

  </ul>

  <h2 dir="auto">Newly supported DSiWare titles only on debug DS consoles</h2>

  <ul dir="auto">

  <li>Dragon Quest Wars</li>

  <li>Make Up &amp; Style</li>

  <li>Metal Torrent</li>

  <li>Plants vs. Zombies</li>

  </ul>'
updated: '2022-09-06T02:26:43Z'
version: v0.64.0
version_title: 'v0.64.0: Labor Day Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.