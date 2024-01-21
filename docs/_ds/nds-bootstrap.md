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
    size: 784023
    size_str: 765 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.2.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1907159
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.2.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.5.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.5.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> 12 more DSiWare titles are now playable on DS and
  DS Lite consoles (plus 3 more titles for debug units)!

  <ul dir="auto">

  <li>Scroll down to see which titles are now supported.</li>

  <li>Click &gt;<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/a779c935d3409dfcf61c64e194b6ceff4c2741bd/universal/include/compatibleDSiWareMap.h">here</a>&lt;
  for the full list of supported titles.</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> DSiWare version of <em>Fashion Tycoon</em> now saves!

  <ul dir="auto">

  <li>EUR version is now also supported.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations, and added Vietnamese, Czech, and Finnish languages!</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>The game will no longer crash sometimes when exiting the in-game menu.

  <ul dir="auto">

  <li>The bug was caused by a timing issue which made the console still think it was
  running the in-game menu.</li>

  </ul>

  </li>

  <li>Updated last year text in the nds-bootstrap screen.</li>

  <li>Other minor fixes.</li>

  </ul>

  <h3 dir="auto">Regression (B4DS mode)</h3>

  <ul dir="auto">

  <li>Due to memory limitations which will never get fixed, <em>Flipnote Studio</em>
  will no longer boot on DS and DS Lite consoles.

  <ul dir="auto">

  <li>If your console is a debug unit, you''ll still be able to boot it with the same
  issues from the previous version of nds-bootstrap.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite</h3>

  <p dir="auto">Titles marked in <strong>Bold</strong> will only boot on debug/dev
  consoles.</p>

  <ul dir="auto">

  <li><strong>Academy Tic-Tac-Toe</strong>

  <ul dir="auto">

  <li>Does not save.</li>

  </ul>

  </li>

  <li>ACT Series: Tangocho: Ni Chi Hen

  <ul dir="auto">

  <li>Does not save.</li>

  </ul>

  </li>

  <li>ACT Series: Tangocho: Ni Chu Hen

  <ul dir="auto">

  <li>Does not save.</li>

  </ul>

  </li>

  <li>ACT Series: Tangocho: Ni Kan Hen

  <ul dir="auto">

  <li>Does not save.</li>

  </ul>

  </li>

  <li>Antipole

  <ul dir="auto">

  <li>Audio does not play due to memory limitations.</li>

  </ul>

  </li>

  <li><strong>Cat Frenzy</strong></li>

  <li>Chronos Twins: One Hero in Two Times</li>

  <li>Cosmos X2</li>

  <li><strong>Defense of the Middle Kingdom</strong></li>

  <li>Elite Forces: Unit 77 (Adds multiplayer, which is not in the original physical
  release.)</li>

  <li>Hellokids: Vol. 1: Coloring and Painting!</li>

  <li>Invasion of the Alien Blobs!</li>

  <li>Jump Trials</li>

  <li>Jump Trials Extreme</li>

  <li>Puffins: Let''s Roll!</li>

  </ul>'
updated: '2024-01-16T06:44:14Z'
version: v1.2.0
version_title: v1.2.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.