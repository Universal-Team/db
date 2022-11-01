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
    size: 560300
    size_str: 547 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.66.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1324406
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.66.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.5.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.5.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>25 more DSiWare titles are now playable on DS/DS lite, with 5 of those being
  the first to require the DS Memory Expansion Pak!

  <ul dir="auto">

  <li><em>Nintendo DS Browser</em> is no longer the only official DS(i) software to
  use the Memory Expansion Pak!</li>

  <li>An additional 3 are now supported for debug consoles as well.</li>

  <li>An additional one is also supported for both retail and debug consoles, but
  requires Slot-2 RAM expansion larger than the MEP (ex. M3, G6, SuperCard).</li>

  <li>Scroll down to see which titles are now supported.</li>

  </ul>

  </li>

  <li>Increased compatibility when running from Slot-2 flashcards, as ROMs up to 32MB
  can now be played properly!

  <ul dir="auto">

  <li>A few (if not all) ROMs above that size may work as well.</li>

  </ul>

  </li>

  <li>Special thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
  The red with white dots error screen has been replaced with a new detailed error
  screen taking place in the in-game menu!</li>

  <li>The in-game menu can now enter sleep mode by closing the console''s lid.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed some weird red screen crashes which wouldn''t occur in previous versions.</li>

  <li>Fixed some overlooked bugs which made some DSiWare titles not boot in B4DS mode.</li>

  <li>Fixed a B4DS mode crash which occurred later on in <em>Pinball Attack!</em>.</li>

  </ul>

  <h2 dir="auto">Newly supported DSiWare titles on retail &amp; debug DS consoles</h2>

  <p dir="auto">Click <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/77f1e23795bc3c65c2af181f0021f877f1e3df37/universal/include/compatibleDSiWareMap.h">here</a>
  for the full list.</p>

  <ul dir="auto">

  <li>Big Bass Arcade

  <ul dir="auto">

  <li>Will crash later on retail consoles</li>

  </ul>

  </li>

  <li>Cake Ninja 2

  <ul dir="auto">

  <li>Previously only supported on debug consoles</li>

  </ul>

  </li>

  <li>Castle Conqueror

  <ul dir="auto">

  <li>Previously only supported on debug consoles</li>

  <li>Only USA version is supported</li>

  </ul>

  </li>

  <li>Castle Conqueror: Heroes 2

  <ul dir="auto">

  <li>Previously only supported on debug consoles</li>

  <li>Memory Expansion Pak is required</li>

  </ul>

  </li>

  <li>The Legend of Zelda: Four Swords: Anniversary Edition

  <ul dir="auto">

  <li>Previously only supported on debug consoles</li>

  <li>Audio is disabled on retail consoles</li>

  <li>May crash after completing a stage</li>

  <li>Memory Expansion Pak is required</li>

  </ul>

  </li>

  <li>Motto Me de Unou o Kitaeru: DS Sokudoku Jutsu Light</li>

  <li>Music on: Playing Piano</li>

  <li>Music on: Retro Keyboard</li>

  <li>Nintendo Countdown Calendar

  <ul dir="auto">

  <li>Memory Expansion Pak is required</li>

  </ul>

  </li>

  <li>Nintendoji

  <ul dir="auto">

  <li>Will crash later on</li>

  <li>Audio is disabled due to memory limitations</li>

  <li>Memory Expansion Pak is required</li>

  </ul>

  </li>

  <li>Peg Solitaire</li>

  <li>Puzzler Brain Games</li>

  <li>Redau Shirizu: Gunjin Shougi</li>

  <li>Remote Racers

  <ul dir="auto">

  <li>Previously only supported on debug consoles</li>

  <li>Memory Expansion Pak is required</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Shougaku 1 Nensei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Shougaku 2 Nensei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Shougaku 3 Nensei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Shougaku 4 Nensei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Shougaku 5 Nensei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Shougaku 6 Nensei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Sokuren Keisa: Nanmon-Hen

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Space Invaders Extreme Z

  <ul dir="auto">

  <li>Previously only supported on debug consoles</li>

  <li>Game can be played without the Memory Expansion Pak, but is required for bottom
  screen backgrounds to be displayed</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Spin Six</li>

  <li>Wonderful Sports: Bowling

  <ul dir="auto">

  <li>Will crash later on retail consoles</li>

  <li>Music is disabled on retail consoles</li>

  </ul>

  </li>

  <li>Yummy Yummy Cooking Jam

  <ul dir="auto">

  <li>Music is disabled due to memory limitations</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Requiring Slot-2 RAM expansion larger than MEP</h3>

  <ul dir="auto">

  <li>Meikyou Kokugo: Rakubiki Jiten

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">Newly supported DSiWare titles only on debug DS consoles</h2>

  <ul dir="auto">

  <li>Mario vs. Donkey Kong: Minis March Again!

  <ul dir="auto">

  <li>Only USA version is supported</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Puzzler World 2013</li>

  <li>Puzzler World XL</li>

  </ul>'
updated: '2022-11-01T02:01:25Z'
version: v0.66.0
version_title: 'v0.66.0: Halloween (2022) release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.