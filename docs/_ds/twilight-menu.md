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
  AddOn-BetterDSiMenuMusic.7z:
    size: 22208058
    size_str: 21 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/AddOn-BetterDSiMenuMusic.7z
  AddOn-ExtraUIMusic.7z:
    size: 8420942
    size_str: 8 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/AddOn-ExtraUIMusic.7z
  AddOn-Multimedia.7z:
    size: 809129
    size_str: 790 KiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/AddOn-Multimedia.7z
  AddOn-VirtualConsole.7z:
    size: 3752956
    size_str: 3 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/AddOn-VirtualConsole.7z
  TWiLightMenu-3DS.7z:
    size: 29266262
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 29348328
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 40799186
    size_str: 38 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 72288103
    size_str: 68 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.20.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_static: https://db.universal-team.net/assets/images/icons/twilight-menu.png
image: https://db.universal-team.net/assets/images/images/twilight-menu.png
image_length: 12520
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/TWiLightMenu
stars: 3745
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v2.11.0">nds-bootstrap
  v2.11.0</a></p>

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

  <li><strong>Flashcard users:</strong> A third game loader option has been added!
  Pico Loader can now be used for fast boot times of DS games, along with improved
  compatibility over nds-bootstrap''s B4DS mode (with a few incompatible games)!

  <ul dir="auto">

  <li>Pico Loader can be downloaded <a href="https://github.com/LNH-team/pico-loader/releases">here</a>.
  Make sure to download the correct one for your flashcard, and place the <code class="notranslate">.bin</code>
  files in the <code class="notranslate">_pico</code> folder on the flashcard''s SD
  root.</li>

  <li>Due to the <code class="notranslate">Game Loader</code> setting getting a new
  name within <code class="notranslate">settings.ini</code> (<code class="notranslate">FC_GAME_LOADER</code>
  instead of <code class="notranslate">USE_BOOTSTRAP</code>), the default setting
  (<code class="notranslate">nds-bootstrap</code>) will be re-set after updating to
  this version.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lorenzooone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lorenzooone">@Lorenzooone</a>:
  DSi-Enhanced/Exclusive game cards will now run in DSi mode on DSi &amp; 3DS consoles!

  <ul dir="auto">

  <li>If cheats (such as widescreen) are detected, the game will run in DS mode instead.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Ported from melonDS, the save types for <em>Puzzler World USA</em> &amp; <em>Legacy
  of Ys: Books I &amp; II</em> have been fixed!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lorenzooone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lorenzooone">@Lorenzooone</a>:
  Fixed some bugs when reading DS(i) game cards and/or flashcards.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
  Dictionary size of 16MB is now set within the 3DS-specific 7z file in order for
  Universal-Updater to properly update TWLMenu++ to this and future versions.</li>

  <li><strong>DSi-based UIs:</strong> Fixed positioning of the <code class="notranslate">Press
  B to return.</code> text in the <code class="notranslate">Start failed. Error ?</code>
  screen.</li>

  </ul>'
updated: '2025-12-13T01:14:34Z'
version: v27.20.0
version_title: v27.20.0
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch games for the Nintendo DS, Nintendo DSi, and GameBoy Advance, as well as DSTWO plugins (if you use a DSTWO).

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.