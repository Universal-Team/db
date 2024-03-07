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
downloads: {}
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
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
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v1.3.1">nds-bootstrap
  v1.3.1</a></p>

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

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>:
  Updated AP-fix for <em>Pokémon: Refined Gold Overhaul</em> (v3.2).</li>

  <li>Moved color mode tables from NitroFS to <code class="notranslate">sd:/_nds/colorLut/</code>.

  <ul dir="auto">

  <li>This means custom tables can now be added (ex. redshift), as well as your own
  homebrew supporting color modes!</li>

  <li>To implement it into your homebrew, see this code for loading the LUT file:
  <a href="https://github.com/RocketRobz/SuperPhotoStudio/blob/master/nds/arm9/source/gui.cpp#L142">https://github.com/RocketRobz/SuperPhotoStudio/blob/master/nds/arm9/source/gui.cpp#L142</a></li>

  <li>Add something like <code class="notranslate">palette[i] = colorTable[palette[i]];</code>
  into your palette and/or 16-bit image loading code(s) for the color LUT to take
  effect.</li>

  </ul>

  </li>

  <li>Various: Updated translations and added Galician language!</li>

  <li>SEGA Genesis/Mega Drive ROMs with the <code class="notranslate">.md</code> extension
  are now supported!</li>

  <li>Genesis/Mega Drive and SNES ROMs are no longer displayed on flashcards, as the
  emulators (except for new SNEmulDS versions) which run them do not support arguments.</li>

  <li>If GBARunner3 is set to be used, the BIOS message is now displayed for all GBA
  games.</li>

  <li>DSiWare titles with <code class="notranslate">NTRJ</code> TID now launch on
  flashcards, regardless if compatible or not.

  <ul dir="auto">

  <li>Implemented because of some DSiWare prototypes using said TID, as well as some
  being supported by nds-bootstrap.</li>

  </ul>

  </li>

  <li>On DSi/3DS, NDMA is now used to clear RAM slightly faster when transitioning
  between TWLMenu++ screen modes, as well as loading <code class="notranslate">.nds</code>
  files.</li>

  <li><code class="notranslate">SCSD</code> string is now checked within the DLDI
  name for SuperCard MiniSD support as well.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DieGo367/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DieGo367">@DieGo367</a>:
  Changed font palette of disabled buttons in DS Classic Menu. (<a href="https://github.com/DS-Homebrew/TWiLightMenu/issues/2358"
  data-hovercard-type="pull_request" data-hovercard-url="/DS-Homebrew/TWiLightMenu/pull/2358/hovercard">#2358</a>)</li>

  <li>Added a setting to hide the Rocket Robz logo.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed GBA <em>Fire Emblem</em> games not booting when using the native GBA mode.</li>

  <li>Fixed Classic NES Series stuck on white screen when using the native GBA mode.

  <ul dir="auto">

  <li>Only early Famicom Mini games and the iQue collection are known to boot properly.</li>

  </ul>

  </li>

  <li>Fixed <em>Iridion II</em> freeze bug when using the native GBA mode. (Patch
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dartz150/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dartz150">@Dartz150</a>)</li>

  <li>Rapid presses now work again in the 3DS theme!</li>

  </ul>'
updated: '2024-03-07T06:09:55Z'
version: v26.7.0
version_title: v26.7.0
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.