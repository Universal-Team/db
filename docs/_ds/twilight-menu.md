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
    size: 28459358
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.3.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 28476081
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.3.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 40169225
    size_str: 38 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.3.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 40365480
    size_str: 38 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v24.3.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_index: 139
image: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/logo.png
image_length: 203427
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
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.55.2">nds-bootstrap
  v0.55.2</a></p>

  <p dir="auto">Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul dir="auto">

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/lmazet/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lmazet">@lmazet</a>)
  Added Amstrad CPC to TWLMenu++ Virtual Console!

  <ul dir="auto">

  <li>This has only been tested on flashcards.</li>

  </ul>

  </li>

  <li>The DSi binary message is now displayed before the Donor ROM message, when running
  via DSiWarehax (such as Memory Pit, Flipnote Lenny, etc.), and if the DSi binaries
  are missing from a DSi-Enhanced ROM.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Swapped 1st and 2nd banner lines, in order for Unlaunch to display which .srldr
  files are which, without looking at the bottom screen.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  To save a couple of MB (megabytes), all bundled skins has been removed.

  <ul dir="auto">

  <li>They can still be downloaded from the <a href="https://skins.ds-homebrew.com/"
  rel="nofollow">TWiLight Menu++ Skins</a> site.</li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Improvement</strong></p>

  <ul dir="auto">

  <li>With the release of <em>Pokémon Blaze Black 2 Redux</em> &amp; <em>Pokémon Volt
  White 2 Redux</em>, which cannot boot in DSi mode, the DSi binary check has been
  improved further.</li>

  </ul>

  <p dir="auto"><strong>Bug fixes</strong></p>

  <ul dir="auto">

  <li>RTC fix has been ported from nds-bootstrap, when running Slot-1 cartridges.</li>

  <li>Fixed Error 1 when launching Slot-1 game in widescreen or through the Last-run
  ROM title.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>)
  Fixed R4iDSN autoboot and flashcart loaders.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>)
  Fixed Ace3DS+ autoboot.</li>

  <li><strong>3DS theme:</strong> Fixed rotating cubes sometimes not disappearing
  before displaying box art.</li>

  <li>Fixed SD writes causing random lockups.

  <ul dir="auto">

  <li>This has not been fully tested, so there''s a very low chance that lockups will
  still occur.</li>

  </ul>

  </li>

  <li>Fixed nds-bootstrap-specific per-game settings not saving for DSi-Enhanced/Exclusive
  titles, if nds-bootstrap is turned off for flashcards.</li>

  <li>Fixed nds-bootstrap settings not saving, if running from flashcard with SCFG
  enabled.</li>

  <li>Photo/box art color de-band has been defaulted to off to fix black lines appearing.

  <ul dir="auto">

  <li>If you installed a TWLMenu++ version before this one, you''ll need to manually
  turn it off, if you want to remove the black lines.</li>

  </ul>

  </li>

  </ul>'
updated: '2022-03-27T03:26:30Z'
version: v24.3.0
version_title: v24.3.0
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.