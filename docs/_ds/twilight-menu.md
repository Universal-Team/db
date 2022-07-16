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
    size: 30961695
    size_str: 29 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.0.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 31014568
    size_str: 29 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.0.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 41764518
    size_str: 39 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.0.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 41973206
    size_str: 40 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.0.0/TWiLightMenu.7z
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
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.61.3">nds-bootstrap
  v0.61.3</a></p>

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

  <li>With a video player (tuna-viDS) being bundled, TWLMenu++ now has a feature to
  view image files as well!

  <ul dir="auto">

  <li>The addition of tuna-viDS and this feature brings <strong>TW</strong>i<strong>L</strong>ight
  Menu++ close to it''s goal to be the next Moonshell!</li>

  <li><code class="notranslate">.bmp</code>, <code class="notranslate">.gif</code>,
  and <code class="notranslate">.png</code> files are supported.</li>

  <li>Trying to load an image containing a width larger than 256px and/or height larger
  than 192px will be displayed as a black screen instead.</li>

  <li>Listen to the menu music from <em>Nintendo DSi Camera</em> while viewing the
  image!</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  The Acekard 2i, R4 Ultra and R4iTT flashcart loaders have been rolled into one!

  <ul dir="auto">

  <li>The BL2CK loader is now used.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  Updated <code class="notranslate">ak2_sd.dldi</code> to support R4iDSN/R4 Ultra
  as well.

  <ul dir="auto">

  <li>As a result, <code class="notranslate">r4idsn_sd.dldi</code> has been deleted.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>PPSEDS r11 now runs in DS mode by default.</li>

  <li><strong>DSi-based themes:</strong> A non-ADPCM .wav file contained in a custom
  skin should now be read properly.</li>

  <li>Fixed not booting via hiyaCFW, depending on the <code class="notranslate">SysNAND
  Region</code>/<code class="notranslate">Launcher</code> settings.</li>

  <li>Other minor fixes.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>4-bit <code class="notranslate">.bmp</code> files are not supported. A black
  screen will be shown instead.</li>

  <li>Trying to launch a title stored on an Acekard 2(i) with <code class="notranslate">Slot-1
  microSD access</code> enabled will still crash on white screens.</li>

  </ul>'
updated: '2022-07-16T04:42:54Z'
version: v25.0.0
version_title: 'v25.0.0: More than just games! (TWL Summer Release #5)'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.