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
    size: 43111930
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.1.1/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 43191168
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.1.1/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 54085332
    size_str: 51 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.1.1/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 54348074
    size_str: 51 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.1.1/TWiLightMenu.7z
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
update_notes: '<p dir="auto">Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul dir="auto">

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>DSi-based themes:</strong> On DS flashcards, large cheat lists no longer
  cause a crash. To achieve this:

  <ul dir="auto">

  <li>SFX is now unloaded when opening the cheat menu.</li>

  <li>The complete font is no longer loaded, and instead will load font tiles into
  an LRU cache.</li>

  </ul>

  </li>

  <li>Due to the above feature freeing up plenty of RAM space, the DSi-type fonts
  will now be loaded on all consoles instead of the DS-type fonts.

  <ul dir="auto">

  <li>If you''re creating a custom font, you now just need <code class="notranslate">large.nftr</code>
  and/or <code class="notranslate">small.nftr</code>.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mentusfentus/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mentusfentus">@mentusfentus</a>:
  Page switch SFX now pans left and right. (<a href="https://github.com/DS-Homebrew/TWiLightMenu/issues/2396"
  data-hovercard-type="pull_request" data-hovercard-url="/DS-Homebrew/TWiLightMenu/pull/2396/hovercard">#2396</a>)</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Some weird bugs have appeared since v26.9.0 due to enabling LTO. To fix them,
  LTO has been disabled in areas where the bugs have occurred.</li>

  <li>Fixed an overlooked bug where the R4 and GBC themes would appear with a blank
  ROM list if the page number (for DSi-based themes) is not the first.</li>

  </ul>'
updated: '2024-04-26T06:03:09Z'
version: v27.1.1
version_title: v27.1.1
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.