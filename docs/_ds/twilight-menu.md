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
    size: 41893714
    size_str: 39 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v26.1.1/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 41945661
    size_str: 40 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v26.1.1/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 52863977
    size_str: 50 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v26.1.1/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 53067570
    size_str: 50 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v26.1.1/TWiLightMenu.7z
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
priority: true
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v1.0.1">nds-bootstrap
  v1.0.1</a></p>

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

  <li>Added a new feature where you can test out the upcoming GBARunner3!

  <ol dir="auto">

  <li>To enable it, set <code class="notranslate">GBARUNNER3_TEST</code> to <code
  class="notranslate">1</code> in <code class="notranslate">sd:/_nds/TWiLightMenu/settings.ini</code></li>

  <li>Build from source code here: <a href="https://github.com/Gericom/GBARunner3">https://github.com/Gericom/GBARunner3</a></li>

  <li>Copy <code class="notranslate">bootstrap.nds</code> to <code class="notranslate">sd:/_nds/TWiLightMenu/emulators/</code>,
  and rename to <code class="notranslate">GBARunner3.nds</code></li>

  <li>Put <code class="notranslate">bios.bin</code> in <code class="notranslate">sd:/_gba/</code></li>

  <li>Launch a GBA game, and report any issues you encounter to <a href="https://github.com/Gericom/GBARunner3/issues">https://github.com/Gericom/GBARunner3/issues</a></li>

  </ol>

  <ul dir="auto">

  <li>If you want good compatibility when playing GBA games, please stick to GBARunner2
  for now. Only use GBARunner3 for testing purposes.</li>

  </ul>

  </li>

  <li>A message will now appear when attempting to launch Pictochat or Download Play
  in the 3DS theme if their <code class="notranslate">.nds</code> files don''t exist
  in <code class="notranslate">/_nds/</code>.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed AP-fixes for

  <ul dir="auto">

  <li>Alice in Wonderland (Europe, Australia)</li>

  <li>Inazuma Eleven (All regions except Japan) (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  <li>Inazuma Eleven 2 (All regions except Japan) (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/DeadSkullzJr/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DeadSkullzJr">@DeadSkullzJr</a>)</li>

  <li>Tsukibito (RetroGameFan)</li>

  </ul>

  </li>

  <li>Fixed internet browser not launching correctly in 3DS theme when not in the
  same location as the <code class="notranslate">.nds</code> file of the browser.</li>

  <li>RAM disk setting is now changeable again.</li>

  <li>Launching <em>Mario &amp; Luigi: Partners in Time</em> on DS flashcards will
  no longer show the "known to not work" message when trying to run it with nds-bootstrap/B4DS.</li>

  </ul>'
updated: '2023-09-26T00:28:33Z'
version: v26.1.1
version_title: v26.1.1
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.