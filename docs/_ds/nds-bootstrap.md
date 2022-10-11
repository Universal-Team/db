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
    size: 537458
    size_str: 524 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.65.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1257876
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.65.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.4.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.4.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>A whopping 51 new DSiWare titles are now supported on flashcards in B4DS mode,
  making them playable on DS and DS Lite!

  <ul dir="auto">

  <li>An additional 7 are now supported for debug consoles as well.</li>

  <li>Scroll down to see which titles are now supported.</li>

  </ul>

  </li>

  <li>1 or 2 parts of the launched ROM can now be pre-loaded into RAM to work around
  slowdown, flickers, and crashes in some games.

  <ul dir="auto">

  <li>Settings are read from <code class="notranslate">sd:/_nds/nds-bootstrap/preLoadSettingsDSi.pck</code>
  or <code class="notranslate">sd:/_nds/nds-bootstrap/preLoadSettings3DS.pck</code></li>

  <li>They can be downloaded from <a href="https://github.com/DS-Homebrew/nds-bootstrap-extras/tree/main/preLoadSettings">here</a>.
  The above TWiLight Menu++ version already bundles them.</li>

  </ul>

  </li>

  <li>Adding yet another advantage over flashcard firmwares/kernels, screenshots can
  now be taken via the in-game menu in B4DS mode!</li>

  <li>Text manuals can now be opened in the in-game menu in B4DS mode!</li>

  <li>The help button is now hidden in the title screens of <em>Mighty Flip Champs!</em>
  &amp; <em>Shantae: Risky''s Revenge</em> when running in B4DS mode, as the manuals
  cannot be opened.</li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li>Merged cardEngine9i SDK1-4 &amp; SDK5 binaries to save space.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed where the patch offset cache version wouldn''t save correctly.</li>

  <li>Fixed WiFi crashing <em>Bomberman Blitz</em> in B4DS mode.</li>

  <li>Fixed an overlooked bug where the DSiWare version of <em>Plants vs. Zombies</em>
  would crash in B4DS mode on debug DS consoles after going into gameplay.</li>

  </ul>

  <h2 dir="auto">Newly supported DSiWare titles on retail &amp; debug DS consoles</h2>

  <p dir="auto">Click <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/a236b80f1592df221043507a76f15fcafad1a88b/universal/include/compatibleDSiWareMap.h">here</a>
  for the full list.</p>

  <ul dir="auto">

  <li>Anne''s Doll Studio: Antique Collection*</li>

  <li>Anne''s Doll Studio: Gothic Collection*</li>

  <li>Anne''s Doll Studio: Lolita Collection*</li>

  <li>Anne''s Doll Studio: Princess Collection*</li>

  <li>Anne''s Doll Studio: Tokyo Collection*</li>

  <li>Bejeweled Twist (USA)</li>

  <li>Dreamwalker</li>

  <li>Electroplankton: Hanenbow</li>

  <li>Electroplankton: Luminarrow</li>

  <li>Electroplankton: Marine-Crystals</li>

  <li>Electroplankton: Nanocarp</li>

  <li>Electroplankton: Rec-Rec</li>

  <li>Electroplankton: Sun-Animalcule</li>

  <li>Electroplankton: Varvoice</li>

  <li>Littlest Pet Shop</li>

  <li>Lola''s Fruit Shop Sudoku</li>

  <li>Missy Mila Twisted Tales</li>

  <li>PictureBook Games: The Royal Bluff

  <ul dir="auto">

  <li>Audio does not play on retail consoles</li>

  </ul>

  </li>

  <li>Pinball Attack! (Part of GO Series in USA, Europe, and Australia)

  <ul dir="auto">

  <li>On retail consoles, it will crash later on in Stage 3</li>

  </ul>

  </li>

  <li>Plants vs. Zombies (Previously only booted on debug consoles)</li>

  <li>Prehistorik Man</li>

  <li>Puzzle to Go: Baby Animals</li>

  <li>Puzzle to Go: Diddl</li>

  <li>Puzzle to Go: Planets and Universe</li>

  <li>Puzzle to Go: Sightseeing</li>

  <li>Puzzle to Go: Wildlife</li>

  <li>Real Crimes: Jack the Ripper</li>

  <li>Renjuku Kanji: Shougaku 1 Nensei</li>

  <li>Renjuku Kanji: Shougaku 2 Nensei</li>

  <li>Renjuku Kanji: Shougaku 3 Nensei</li>

  <li>Renjuku Kanji: Shougaku 4 Nensei</li>

  <li>Renjuku Kanji: Shougaku 5 Nensei</li>

  <li>Renjuku Kanji: Shougaku 6 Nensei</li>

  <li>Renjuku Kanji: Chuugakusei</li>

  <li>Smart Girl''s Playhouse Mini</li>

  <li>Tales to Enjoy!: Little Red Riding Hood</li>

  <li>Tales to Enjoy!: Puss in Boots</li>

  <li>Tales to Enjoy!: The Three Little Pigs</li>

  <li>Tales to Enjoy!: The Ugly Duckling</li>

  <li>Tangrams</li>

  <li>Tantei Jinguuji Saburou: Tsubaki no Yukue</li>

  <li>Tantei Jinguuji Saburou: Akenaiyoru ni</li>

  <li>Tantei Jinguuji Saburou: Kadannoitte</li>

  <li>Tantei Jinguuji Saburou: Rensa Suru Noroi</li>

  <li>Tantei Jinguuji Saburou: Nakiko no Shouzou</li>

  <li>Tetris Party Live</li>

  <li>Turn: The Lost Artifact

  <ul dir="auto">

  <li>Does not save due to difficulty in implementation</li>

  </ul>

  </li>

  <li>Zombie Blaster</li>

  <li>Zombie Skape</li>

  <li>Zoonies: Escape from Makatu</li>

  <li>Zuma''s Revenge!</li>

  </ul>

  <p dir="auto">*As there''s no photo album in B4DS mode, you must use the screenshot
  feature in the in-game menu to take a picture in <em>Anne''s Doll Studio</em>.</p>

  <h2 dir="auto">Newly supported DSiWare titles only on debug DS consoles</h2>

  <ul dir="auto">

  <li>Bejeweled Twist (Europe, Australia)

  <ul dir="auto">

  <li>As the USA version is already supported on both retail and debug consoles, this
  one is not counted towards the total</li>

  </ul>

  </li>

  <li>Electroplankton: Beatnes</li>

  <li>Electroplankton: Lumiloop</li>

  <li>Electroplankton: Trapy</li>

  <li>Go! Go! Kokopolo</li>

  <li>Little Red Riding Hood''s Zombie BBQ</li>

  <li>Pirates Assault</li>

  <li>Remote Racers</li>

  </ul>'
updated: '2022-10-11T04:38:54Z'
version: v0.65.0
version_title: 'v0.65.0: Canadian Thanksgiving 10/10 Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.