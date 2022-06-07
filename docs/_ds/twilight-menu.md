---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
color: '#464061'
color_bg: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases
downloads:
  TWiLightMenu-3DS.7z:
    size: 28767725
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.9.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 28820146
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.9.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 40618454
    size_str: 38 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.9.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 40827622
    size_str: 38 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.9.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_index: 138
icon_static: https://db.universal-team.net/assets/images/icons/twilight-menu.png
image: https://db.universal-team.net/assets/images/images/twilight-menu.png
image_length: 12520
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    TWiLightMenu-3DS.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-3DS.7z
    TWiLightMenu-DSi.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-DSi.7z
    TWiLightMenu-Flashcard.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Flashcard.7z
    TWiLightMenu.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu.7z
priority: true
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.58.0">nds-bootstrap
  v0.58.0</a> (which is out of date, so please update nds-bootstrap to <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.58.1">v0.58.1</a>
  after installing this TWLMenu++ version)</p>

  <p dir="auto">Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul dir="auto">

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Added AP-fixes for <em>Pokemon HeartGold</em> &amp; <em>SoulSilver</em> (Latin
  Spanish translation).</li>

  <li>When detecting rumble, it no longer checks for TIDs of GBA games, in order for
  custom GBA carts with rumble to work as well.</li>

  <li>Updated ESRB game list to add more games. (<a class="commit-link" data-hovercard-type="commit"
  data-hovercard-url="https://github.com/DS-Homebrew/TWiLightMenu/commit/c0645f63c0d115588e9975d98ad08ef6aea7ae14/hovercard"
  href="https://github.com/DS-Homebrew/TWiLightMenu/commit/c0645f63c0d115588e9975d98ad08ef6aea7ae14"><tt>c0645f6</tt></a>)</li>

  <li>The <code class="notranslate">External FIRMs and modules</code> setting in Luma
  config is now checked before rebooting to widescreen.

  <ul dir="auto">

  <li>Make sure Luma is on v11 or later for this to work.</li>

  </ul>

  </li>

  <li>The brightness can now be changed in the DS Classic Menu on DS lite consoles!</li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Improved translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed a long-standing bug where sleep mode would not work and/or cause a crash
  (with a glitched top screen) after exiting.

  <ul dir="auto">

  <li>This is achieved by implementing a custom sleep mode handler, as the one in
  libnds is bugged.</li>

  </ul>

  </li>

  <li>Fixed another long-standing bug where a certain area of RAM gets cleared while
  using Memory Pit.

  <ul dir="auto">

  <li>This allows the complete font set to be loaded without issues in Memory Pit.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  The flashcard kernel (Wood, in this case) now uses the correct save file extension
  (being <code class="notranslate">.sav</code> instead of <code class="notranslate">.nds.sav</code>).</li>

  <li>The brightness level on DS lite no longer self-changes while using the flashcard
  kernel (Wood, in this case) to run games!</li>

  <li>Fixed AP warning not shown for <em>Mario &amp; Luigi RPG: Siganui Partner</em>
  (Korea), if AP-fix doesn''t exist.</li>

  <li><strong>DSi-based themes:</strong> Fixed crash when opening per-game settings
  for a DS(i) ROM with no icon.</li>

  <li>Fixed TWLMenu++ not starting via hiyaCFW, by having Unlaunch start it instead.</li>

  </ul>'
updated: '2022-06-07T02:07:07Z'
version: v24.9.0
version_title: 'v24.9.0: TWL Summer Release'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.