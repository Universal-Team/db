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
    size: 728870
    size_str: 711 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.71.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1739246
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.71.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.9.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.9.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Added support for a <em>huge</em> number of 152
  more DSiWare titles to be playable on DS/DS lite (plus 4 more for debug consoles)!

  <ul dir="auto">

  <li>Scroll down to see which titles are now supported.</li>

  <li>Click &gt;<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/3afc1f67c6fad5ab314d477a257e861e16aa6bfe/universal/include/compatibleDSiWareMap.h">here</a>&lt;
  for the full list of supported titles.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> <em>Castle Conqueror: Heroes 2</em> no longer requires
  a Memory Expansion Pak to run!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated in-game menu translations.</li>

  <li>Some minor code optimization.</li>

  </ul>

  <h3 dir="auto">Bug fixes (DSi/3DS)</h3>

  <ul dir="auto">

  <li><em>Fossil Fighters</em> fans will no longer need to wait or worry, as <em>Fossil
  Fighters Champions</em> now boots again!

  <ul dir="auto">

  <li>As a result, other THUMB DSi-Enhanced ROMs such as <em>Bejeweled Twist</em>
  also boot again.</li>

  </ul>

  </li>

  <li>The SDNAND/Photo location setting should now work properly.

  <ul dir="auto">

  <li>It''ll no longer attempt to mount the actual SysNAND, if an SDNAND is found.</li>

  </ul>

  </li>

  <li>Only necessary devices are added to device list for DSiWare.

  <ul dir="auto">

  <li>Should hopefully fix some weird save-related issues with certain ones.</li>

  </ul>

  </li>

  <li>Both <em>Starship Defense</em> &amp; <em>Trajectile</em> now boot via Memory
  Pit.</li>

  <li>Fixed <em>Panewa!</em> not booting.</li>

  <li>Fixed <em>Super Smash Bros. Crash</em> not switching between menus.</li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite</h3>

  <p dir="auto">Titles marked in <em>Italics</em> will require either a Memory Expansion
  Pak or debug console.<br>

  Titles marked in <strong>Bold</strong> will only boot on debug consoles.</p>

  <ul dir="auto">

  <li><em>21 Blackjack</em>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li><em>5 in 1 Solitaire</em>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Bridge</li>

  <li>Castle Conqueror: Against</li>

  <li>Castle Conqueror: Revolution</li>

  <li><em>Chess Challenge!</em>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Chotto DS Bun ga Kuzenshuu: Sekai no Bungaku 20</li>

  <li>Christmas Wonderland

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Christmas Wonderland 2

  <ul dir="auto">

  <li>On non-debug consoles, music is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Chronicles of Vampires: Origins</li>

  <li>Chronicles of Vampires: Awakening</li>

  <li>Chuugaku Eijukugo: Kiho 150 Go Master</li>

  <li>Chuugaku Eitango: Kiho 400 Go Master</li>

  <li>Chuuga Kukihon'' Eitango: Wado Pazuru</li>

  <li>Commando: Steel Disaster</li>

  <li>Coropata</li>

  <li>Cosmo Fighters

  <ul dir="auto">

  <li>The demo version is booted due to RAM limitations, and thus does not save</li>

  </ul>

  </li>

  <li>Crazy Golf

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Crazy Sudoku

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Crystal Adventure</li>

  <li>Crystal Caverns of Amon-Ra</li>

  <li>Decathlon 2012

  <ul dir="auto">

  <li>Audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Deep Sea Creatures</li>

  <li>Art Style: DIGIDRIVE / INTERSECT

  <ul dir="auto">

  <li>Limited to button mode, title music does not play, and multiplayer mode does
  not work</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Easter Eggztravaganza

  <ul dir="auto">

  <li>On non-debug consoles, the game crashes after the first stage, due to RAM limitations</li>

  </ul>

  </li>

  <li>EJ Puzzles: Hooked</li>

  <li>Fieldrunners

  <ul dir="auto">

  <li>Previously only booted on debug consoles</li>

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Flip the Core</li>

  <li>Flips: The Bubonic Builders</li>

  <li>Flips: The Enchanted Wood</li>

  <li>Flips: The Folk of the Faraway Tree</li>

  <li>Flips: The Magic Faraway Tree</li>

  <li>Flips: More Bloody Horowitz</li>

  <li>Flips: Silent But Deadly</li>

  <li>Flips: Terror in Cubicle Four</li>

  <li>Fire Panic</li>

  <li>Frenzic

  <ul dir="auto">

  <li>Does not save</li>

  <li>Will crash after changing settings</li>

  </ul>

  </li>

  <li>Gaia''s Moon</li>

  <li>Ginsei Tsume-Shougi</li>

  <li>Go Fetch!</li>

  <li>Go Fetch! 2</li>

  <li>Go! Go! Island Rescue!</li>

  <li>Ideyou Sukeno: Kenkou Maja DSi

  <ul dir="auto">

  <li>Does not save</li>

  <li>Immediately starts the gameplay mode with <code class="notranslate">?</code>-faced
  players</li>

  </ul>

  </li>

  <li>Ivy the Kiwi? mini</li>

  <li>Jazzy Billiards

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Jewel Adventures</li>

  <li>Jewel Keepers: Easter Island</li>

  <li>Jewel Legends: Tree of Life</li>

  <li><em>Jinia Supasonaru: Eiwa Rakubiki Jiten</em>

  <ul dir="auto">

  <li>16MB+ RAM expansion required</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li><em>Jinia Supasonaru: Waei Rakubiki Jiten</em>

  <ul dir="auto">

  <li>MEP required, regardless if using a retail or debug console</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Just SING! 80''s

  <ul dir="auto">

  <li>Crashes at some point for an unknown reason</li>

  </ul>

  </li>

  <li>Kazu De Asobu: Mahoujin To Imeji Kei-san</li>

  <li>Keibadou Uma no Suke 2012</li>

  <li>Keisan 100 Renda</li>

  <li>Kemonomix</li>

  <li>Kokoro no Herusumeta: Kokoron

  <ul dir="auto">

  <li>Will not boot without <code class="notranslate">TWLFontTable.dat</code> in <code
  class="notranslate">fat:/_nds/nds-bootstrap/</code></li>

  </ul>

  </li>

  <li>Koneko no ie: Kiri Shima Keto-San Biki no Koneko</li>

  <li>Koukou Eijukugo: Kiho 200 Go Master</li>

  <li>Koukou Eitango: Kiho 400 Go Master</li>

  <li>Letter Challenge</li>

  <li>Link ''n'' Launch

  <ul dir="auto">

  <li>On non-debug consoles, music is disabled due to RAM limitations</li>

  <li><code class="notranslate">TWLFontTable.dat</code> is required in <code class="notranslate">fat:/_nds/nds-bootstrap/</code>
  (and a MEP inserted, for the EUR/AUS version) for the tutorial text to display</li>

  </ul>

  </li>

  <li><em>Make Up &amp; Style</em>

  <ul dir="auto">

  <li>Previously only booted on debug consoles</li>

  <li>On non-debug consoles, the title FMV is disabled due to a weird bug (TWLMenu++
  will report RAM limitations)</li>

  </ul>

  </li>

  <li>Master of Illusion Express: Deep Psyche / A Little Bit of... Magic Made Fun:
  Deep Psyche</li>

  <li>Master of Illusion Express: Funny Face / A Little Bit of... Magic Made Fun:
  Funny Face

  <ul dir="auto">

  <li>Versions which aren''t the English or Japanese versions will not boot</li>

  </ul>

  </li>

  <li>Master of Illusion Express: Matchmaker / A Little Bit of... Magic Made Fun:
  Matchmaker</li>

  <li>Master of Illusion Express: Mind Probe / A Little Bit of... Magic Made Fun:
  Mind Probe</li>

  <li>Master of Illusion Express: Shuffle Games / A Little Bit of... Magic Made Fun:
  Shuffle Games</li>

  <li><em>Match Up!</em>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li><em>Mega Words</em>

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Mehr Kreuzwortratsel: Welt Edition</li>

  <li>Music on: Learning Piano</li>

  <li>Music on: Learning Piano Vol. 2</li>

  <li>Nandoku 500 Kanji: Wado Pazuru</li>

  <li>Nazo no Mini Game

  <ul dir="auto">

  <li>On non-debug consoles, music is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Neko Neko Bakery: Pan de Pazurunya!

  <ul dir="auto">

  <li>On non-debug consoles, music is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Noroi no Game: Chi</li>

  <li>Noroi no Game: Oku</li>

  <li>Oscar in Toyland</li>

  <li>Oscar in Toyland 2

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Otegaru Pazuru Shirizu: Yurito Fushigina Meikyuu</li>

  <li>Othello</li>

  <li>Otona no Nihonshi Pazuru</li>

  <li>Otona no Sekaishi Pazuru</li>

  <li>Otona no Tame no: Kei-san Training DS</li>

  <li>Otona no Tame no: Renjuku Kanji</li>

  <li>Pirates Assault

  <ul dir="auto">

  <li>Previously only booted on debug consoles</li>

  </ul>

  </li>

  <li>PlayLearn Chinese</li>

  <li>PlayLearn Spanish</li>

  <li>Pocket Pack: Strategy Games</li>

  <li>Pocket Pack: Words &amp; Numbers</li>

  <li>Pomjong</li>

  <li>The Price Is Right</li>

  <li>Primrose</li>

  <li>Publisher Dream

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Pucca: Noodle Rush</li>

  <li>Puzzle Rocks

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>QuickPick Farmer</li>

  <li>Roller Angels</li>

  <li>RPG Dashutsu Game</li>

  <li>Saikyou Ginsei Shougi

  <ul dir="auto">

  <li>Crashes at some point due to RAM limitations</li>

  </ul>

  </li>

  <li>Sakurai Miho No Kouno: Megami Serapi Uranai</li>

  <li><strong>Save the Turtles</strong></li>

  <li>The Seller</li>

  <li>Kakitori Rekishi: Shouga Kusei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Chiri Kuizu: Shouga Kusei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Koumin Kuizu: Shouga Kusei

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Rika Kuizu Shouga Kusei: Seibutsu Chigaku He

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Jukugo Kuizu

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Slingo Supreme

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Snapdots</li>

  <li>Sokomania</li>

  <li>Sokomania 2: Cool Job

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Sora Kake Girl: Shojo Shooting</li>

  <li>Spot It! Challenge</li>

  <li>Spot It! Challenge: Mean Machines</li>

  <li>Successfully Learning: English, Year 2</li>

  <li>Successfully Learning: English, Year 3</li>

  <li>Successfully Learning: English, Year 4</li>

  <li>Successfully Learning: English, Year 5</li>

  <li>Successfully Learning: German, Year 2</li>

  <li>Successfully Learning: German, Year 3</li>

  <li>Successfully Learning: German, Year 4</li>

  <li>Successfully Learning: German, Year 5</li>

  <li>Successfully Learning: Mathematics, Year 2</li>

  <li>Successfully Learning: Mathematics, Year 3</li>

  <li>Successfully Learning: Mathematics, Year 4</li>

  <li>Successfully Learning: Mathematics, Year 5</li>

  <li>Sudoku &amp; Kakuro: Welt Edition</li>

  <li><em>Sudoku Challenge!</em>

  <ul dir="auto">

  <li>The feature to zoom-in on a letter is bugged due to bus issues with Slot-2,
  and will show glitched pixels</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Surfacer+</li>

  <li><strong>Super Swap</strong></li>

  <li><strong>Super Yum Yum: Puzzle Adventures</strong></li>

  <li><em>Sutanoberuzu: Kono Hareta Sora no Shita de</em>

  <ul dir="auto">

  <li>On non-debug consoles, music is disabled due to RAM limitations, and opening
  FMV is disabled due to bus issues with Slot-2</li>

  </ul>

  </li>

  <li><em>Sutanoberuzu: Shirogane no Torikago</em>

  <ul dir="auto">

  <li>On non-debug consoles, opening FMV is disabled due to bus issues with Slot-2</li>

  </ul>

  </li>

  <li>Telegraph Crosswords</li>

  <li>Telegraph Sudoku &amp; Kakuro</li>

  <li>Tell me Darling (JAP title: Oshiete Darling)</li>

  <li>Thorium Wars

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>The Tower DS: Classic</li>

  <li>The Tower DS: Hotel</li>

  <li>The Tower DS: Shopping Santa</li>

  <li><strong>Trajectile / Reflect Missile</strong></li>

  <li>Trollboarder

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>True Swing Golf Express / A Little Bit of... Nintendo Touch Golf

  <ul dir="auto">

  <li>On non-debug consoles, audio is disabled due to RAM limitations</li>

  </ul>

  </li>

  <li>Ubongo</li>

  <li>Uchi Makure!: Touch the Chameleon</li>

  <li>Viking Invasion

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li><em>Word Searcher</em></li>

  <li><em>Word Searcher II</em></li>

  <li><em>Word Searcher III</em></li>

  <li><em>Word Searcher IV</em></li>

  <li>WordJong Arcade</li>

  <li>Working Dawgs: A-maze-ing Pipes</li>

  <li>Working Dawgs: Rivet Retriever</li>

  <li>Za Curosu</li>

  <li>Zimo: Mahjong Fanatic</li>

  </ul>'
updated: '2023-03-31T01:58:07Z'
version: v0.71.0
version_title: 'v0.71.0: Conquest of the DS⁽ⁱ⁾Ware'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.