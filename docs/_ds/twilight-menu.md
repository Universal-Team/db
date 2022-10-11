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
    size: 32134445
    size_str: 30 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.4.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 32183128
    size_str: 30 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.4.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 42925825
    size_str: 40 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.4.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 43134514
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.4.0/TWiLightMenu.7z
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
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.65.0">nds-bootstrap
  v0.65.0</a></p>

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

  <li><a href="https://github.com/Gericom/FastVideoDSPlayer">FastVideoDSPlayer</a>
  (by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Gericom/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Gericom">@Gericom</a>)
  is now bundled! Play videos as high as 60FPS on DSi, 30FPS on DS, and with any length!

  <ul dir="auto">

  <li>See <a href="https://wiki.ds-homebrew.com/ds-index/videoplayers" rel="nofollow">this</a>
  page for more information, as well as how to convert a video.</li>

  </ul>

  </li>

  <li>Added logging! Open <code class="notranslate">sd:/_nds/TWiLightMenu/log.txt</code>
  to see what TWLMenu++ has printed out while it was running a certain theme.

  <ul dir="auto">

  <li>Only very minimal information is printed out for now.</li>

  </ul>

  </li>

  <li>nds-bootstrap pre-load settings are now bundled!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
  Added extension blocking INI-only setting. (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1396978934" data-permission-text="Title
  is private" data-url="https://github.com/DS-Homebrew/TWiLightMenu/issues/2061" data-hovercard-type="pull_request"
  data-hovercard-url="/DS-Homebrew/TWiLightMenu/pull/2061/hovercard" href="https://github.com/DS-Homebrew/TWiLightMenu/pull/2061">#2061</a>)</li>

  <li>Box art is now turned off by default for first-time users.</li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Improved translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixes a bug which caused DSi-based themes to crash on white screens during font
  loading, when running on CycloDS iEvolution in DSi mode.</li>

  <li>DSiWare booter per-game setting is no longer ignored when booting Last-run ROM.</li>

  <li>Fixed where pressing <code class="notranslate">A</code>, <code class="notranslate">X</code>,
  or <code class="notranslate">Y</code> would not work in DSi-based themes with box
  art turned off, if Left or Right aren''t pressed on D-Pad.</li>

  <li>Loading screen is no longer shown when skipping to the end of a page in DSi-based
  themes.</li>

  <li>Fixed touch frame delay.</li>

  </ul>'
updated: '2022-10-11T05:03:23Z'
version: v25.4.0
version_title: 'v25.4.0: Canadian Thanksgiving 10/10 Release'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.