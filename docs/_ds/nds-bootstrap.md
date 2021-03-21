---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 430759
    size_str: 420 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.37.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1231363
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.37.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://raw.githubusercontent.com/DS-Homebrew/nds-bootstrap/master/retail/assets/icon.bmp
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
update_notes: '<p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v19.0.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v19.0.0</a></p>

  <p>Instructions:</p>

  <ol>

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li>Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>(me and <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  An in-game menu similar to Luma''s Rosalina menu has been added!<br>

  You can dump the RAM, view/edit RAM, swap screens (which can still done by holding
  L+R+UP+X for 1 sec), reset the game, and exit the game.

  <ul>

  <li>It can be opened with the same button combo: L+DOWN+SELECT</li>

  <li>This replaces the L+R+DOWN+B button combo, as you can exit the game in the menu.</li>

  <li>Cannot be opened, if <code>Expand ROM space in RAM</code> is turned on, and
  if the game uses that feature (check TWLMenu++ per-game settings to see).</li>

  <li>Cannot be opened, if the flashcard is running without access to the DSi hardware.</li>

  </ul>

  </li>

  <li>Cheat versions of AP fixes are now supported!

  <ul>

  <li>Detected by checking for the <code>.bin</code> extension in the filename.</li>

  </ul>

  </li>

  <li>Screens can now be swapped on flashcards!</li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>nds-bootstrap and B4DS have been merged into one .nds file! (HB is still separate.)

  <ul>

  <li>As a result, regular nds-bootstrap will now be used on flashcards, if DSi hardware
  is accessible (via SCFG), thus increasing game compatibility to nearly the same
  as when running from the console''s SD card!</li>

  </ul>

  </li>

  <li>Heap shrink has been removed!<br>

  Now all games will run fast as if it were turned on, but now no crashes will occur
  (and if they still occur, at least it''s unrelated to shrinking the game''s heap)!</li>

  <li>Cache block size is now hardcoded to 32KB.</li>

  <li>The card engine arm9 code is now moved to uncached memory, in case if a ROM
  hack makes use of the extra memory of the DSi in DSi mode.</li>

  <li>Some minor optimizations.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>Fixed some bugs related to soft-resetting, when using forwarders on 3DS consoles.</li>

  <li>Slot-1 is now disabled, if not in use. Fixes some bugs, if the frontend does
  not disable Slot-1.</li>

  </ul>

  <p><strong>Known bug</strong></p>

  <ul>

  <li>The in-game menu will appear as only a black screen in some areas of some games.</li>

  </ul>

  <p><strong>Regression</strong></p>

  <ul>

  <li>Some games that use DMA for card reads, will now either crash at some point,
  or not boot at all.</li>

  </ul>'
updated: '2021-03-17T06:34:01Z'
version: v0.37.0
version_title: v0.37.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.