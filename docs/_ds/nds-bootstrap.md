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
    size: 632995
    size_str: 618 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.70.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1500783
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.70.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.8.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.8.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <p dir="auto">Do you love the Nintendo DS? Do you love the Nintendo DSi? Do you
  love (or like) some of it''s DSiWare library?<br>

  If you''ve answered <em>yes</em> to all (or for some reason, just No. 1 &amp; No.
  3) of those questions, then Happy Valentine''s Day! This nds-bootstrap release is
  for you!</p>

  <ul dir="auto">

  <li>Why? Because we''ve added support for 43 more DSiWare titles to play on your
  DS and/or DS lite (plus 4 more for debug consoles)!

  <ul dir="auto">

  <li>Scroll down to see which titles are now supported.</li>

  <li>Click &gt;<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/6adc82f05a5e09ce2ecfda33be56a7ec77db4f36/universal/include/compatibleDSiWareMap.h">here</a>&lt;
  for the full list of supported titles.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and <a href="https://crowdin.com/profile/earedguitr" rel="nofollow">вухаста гітара</a>:
  Updated Ukranian in-game menu translation.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed 0xC1 and 0xC2 cheat types causing a crash.</li>

  <li>Tried fixing Japanese DSi/3DS consoles using external <code class="notranslate">TWLFontTable.dat</code>
  (which isn''t CHN or KOR), despite the same one existing in TWLNAND.</li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite</h3>

  <ul dir="auto">

  <li>1st Class Poker &amp; BlackJack</li>

  <li>101 Pinball World

  <ul dir="auto">

  <li>Previously only booted on debug consoles</li>

  <li>Audio is disabled to fit within RAM limitations on retail consoles</li>

  <li>Opening one of the pinball stages will cause a crash</li>

  </ul>

  </li>

  <li>18th Gate

  <ul dir="auto">

  <li>Exclusive to debug consoles</li>

  </ul>

  </li>

  <li>1001 Crystal Mazes Collection

  <ul dir="auto">

  <li>Music is disabled to fit within RAM limitations on retail consoles</li>

  </ul>

  </li>

  <li>200 Vmaja: Charen Ji Supirittsu</li>

  <li>24/7 Solitaire</li>

  <li>3D Mahjong</li>

  <li>3D Twist Match

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>3 Punten Katou Itsu: Bakumatsu Kuizu He</li>

  <li>3 Punten Katou Itsu: Higashi Nihon Sengoku Kuizu He</li>

  <li>3 Punten Katou Itsu: Nishinihon Sengoku Kuizu He</li>

  <li>3450 Algo</li>

  <li>4 Elements</li>

  <li>5 in 1 Mahjong</li>

  <li>7 Card Games</li>

  <li>7 Wonders II</li>

  <li>90''s Pool

  <ul dir="auto">

  <li>Audio is disabled to fit within RAM limitations on retail consoles</li>

  </ul>

  </li>

  <li>Abyss</li>

  <li>Animal Boxing

  <ul dir="auto">

  <li>Exclusive to debug consoles, but retail console users can still play the DS
  version</li>

  </ul>

  </li>

  <li>Around the World in 80 Days</li>

  <li>Arrow of Laputa

  <ul dir="auto">

  <li>Audio is disabled to fit within RAM limitations on retail consoles</li>

  </ul>

  </li>

  <li>Aru Seishun no Monogatari: Kouenji Joshi Sakka

  <ul dir="auto">

  <li>Requires Memory Expansion Pak to launch on retail consoles</li>

  <li>FMVs are disabled on retail consoles</li>

  </ul>

  </li>

  <li>Atama o Yoku Suru Anzan DS: Zou no Hana Fuusen</li>

  <li>Ball Fighter</li>

  <li>Boardwalk Ball Toss</li>

  <li>Bookstore Dream</li>

  <li>Boom Boom Squaries

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Bounce &amp; Break</li>

  <li>Box Pusher</li>

  <li>Dancing Academy</li>

  <li>Deep Sea Creatures

  <ul dir="auto">

  <li>Exclusive to debug consoles</li>

  </ul>

  </li>

  <li>Dekisugi Tingle Pack

  <ul dir="auto">

  <li>A crash will occur when exiting the Dance menu for an unknown reason</li>

  </ul>

  </li>

  <li>Devil Band: Rock the Underworld

  <ul dir="auto">

  <li>Exclusive to debug consoles</li>

  </ul>

  </li>

  <li>Divergent Shift</li>

  <li>Furo Jump!! Girutegia Gaiden! (ARC Style)

  <ul dir="auto">

  <li>Exclusive to debug consoles</li>

  </ul>

  </li>

  <li>Go! Go! Kokopolo

  <ul dir="auto">

  <li>Previously only booted on debug consoles</li>

  </ul>

  </li>

  <li>Hachiwandaiba DS: Naru Zouku Ha Samishougi</li>

  <li>Halloween Trick or Treat

  <ul dir="auto">

  <li>Music is disabled to fit within RAM limitations on retail consoles</li>

  </ul>

  </li>

  <li>Handy Hockey</li>

  <li>Handy Mahjong</li>

  <li>Hearts Spades Euchre</li>

  <li>Hell''s Kitchen VS</li>

  <li>High Stakes Texas Hold''em</li>

  <li>Hints Hunter</li>

  <li>Legendary Wars: T-Rex Rumble</li>

  <li>Metal Torrent

  <ul dir="auto">

  <li>Previously only booted on debug consoles</li>

  <li>Music is disabled to fit within RAM limitations on retail consoles</li>

  <li>The Japanese version has a weird bug where in menus, almost all of the bottom
  screen is covered by a black rectangle. This does not occur during gameplay</li>

  </ul>

  </li>

  <li>Spot the Difference

  <ul dir="auto">

  <li>Exclusive to debug consoles</li>

  </ul>

  </li>

  <li>Touch Solitaire</li>

  <li>Whack-A-Friend

  <ul dir="auto">

  <li>As the DSi Camera does not exist on DS or DS lite, the photo feature will redirect
  you to gameplay</li>

  </ul>

  </li>

  </ul>'
updated: '2023-02-15T04:54:58Z'
version: v0.70.0
version_title: 'v0.70.0: I ❤️ DS⁽ⁱ⁾Ware'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.