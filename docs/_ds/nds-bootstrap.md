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
    size: 834890
    size_str: 815 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.15.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1210089
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.15.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1354
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.23.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.23.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <p dir="auto"><strong>B4DS</strong> = nds-bootstrap on DS flashcards</p>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS:</strong> Removed the Memory Expansion Pak requirement for these
  DSiWare titles:

  <ul dir="auto">

  <li>5 in 1 Solitaire (Music is now streamed instead of being pre-loaded)</li>

  <li>Word Searcher (USA) (Music is now streamed instead of being pre-loaded)</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> Added support for these DSiWare titles on DS &amp; DS
  Lite, bringing the amount of supported titles to 501!

  <ul dir="auto">

  <li>Neko Reversi

  <ul dir="auto">

  <li>Previously only booted on debug DS consoles.</li>

  <li>Audio is disabled due to memory limitations (but will still play on debug consoles).</li>

  <li>Does not save.</li>

  </ul>

  </li>

  <li>Saikyou Ginsei Igo

  <ul dir="auto">

  <li>Audio is disabled due to memory limitations (but will play on debug consoles).</li>

  <li>Requires the Memory Expansion Pak to run.</li>

  <li>Does not save.</li>

  </ul>

  </li>

  <li>Shawn Johnson Gymnastics

  <ul dir="auto">

  <li>Previously only booted on debug DS consoles.</li>

  <li>Music is disabled due to memory limitations (but will still play on debug consoles).</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> The full version of <em>Digidrive</em> now runs on DS
  &amp; DS Lite!

  <ul dir="auto">

  <li>Due to memory limitations, audio will not play.</li>

  <li>For sound effects to play, you''ll need to insert the Memory Expansion Pak.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> <em>Yummy Yummy Cooking Jam</em> now plays music if a
  16MB+ RAM expansion cart is inserted. This means the regular Memory Expansion Pak
  will not work.</li>

  <li><strong>B4DS:</strong> Due to memory limitations (crashing when getting past
  title screen), the DSiWare version of <em>Fizz</em> now only runs on debug DS consoles.</li>

  <li><strong>DSi/3DS:</strong> Added <code class="notranslate">banner.sav</code>
  redirection for the few DSiWare titles which support it (ex. <em>Brain Age Express</em>).
  This means any nds-bootstrap frontend which support <code class="notranslate">banner.sav</code>
  (such as TWLMenu++) will now report how far you progressed and/or how well you did
  in those games!</li>

  <li>Various: Updated in-game menu translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> Fixed <em>Dragon Quest IX</em> not playing cutscene
  audio.</li>

  <li><strong>DSi/3DS:</strong> Added ROM pre-load settings for <em>Tak: The Great
  Juju Challenge</em> in order to fix the game crashing after the tutorial.</li>

  <li><strong>DSi/3DS:</strong> Fixed an overlooked bug which caused nds-bootstrap
  to not boot a game that''s on the console''s SD card when running from a flashcard.</li>

  <li><strong>3DS:</strong> Fixed in-game menu option descriptions (after <code class="notranslate">Main
  Screen</code>) being incorrectly assigned.</li>

  <li><strong>B4DS:</strong> Fixed crashing in <em>Saikyou Ginsei Shougi</em>.</li>

  <li><strong>B4DS:</strong> Fixed touch screen flashing black when touching a button
  in <em>Sudoku Challenge!</em></li>

  <li>Fixed sleep mode not working when using an Acekard 2(i)/R4(i) Ultra flashcard
  (the latter where if it autoboots to TWLMenu++).</li>

  </ul>'
updated: '2026-03-17T22:03:17Z'
version: v2.15.0
version_title: v2.15.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.