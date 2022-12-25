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
    size: 32856164
    size_str: 31 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.7.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 32902763
    size_str: 31 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.7.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 43690997
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.7.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 43894249
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.7.0/TWiLightMenu.7z
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
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.68.0">nds-bootstrap
  v0.68.0</a></p>

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

  <li>When started via flashcard, in order to use the settings from the console''s
  SD card slot, a file called <code class="notranslate">primary</code> must now be
  created in <code class="notranslate">sd:/_nds/</code>.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/quiple/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/quiple">@quiple</a>:
  Updated font used in the DS Classic Menu.</li>

  <li>Updated AP-fix for <em>Anpanman to Touch de Waku Waku Training</em> in order
  to work properly with nds-bootstrap v0.68.0.</li>

  <li>Finally updated NitroGrafx to v0.9.0.</li>

  <li>Support for the EZ-Flash RAM is now disabled by default.

  <ul dir="auto">

  <li>In order to use it again, <code class="notranslate">EZ_FLASH_RAM</code> must
  be set to <code class="notranslate">1</code> in <code class="notranslate">fat:/_nds/TWiLightMenu/settings.ini</code>.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed games not booting in widescreen, as well as all of DS(i) mode being stuck
  in widescreen after launching a game with widescreen.

  <ul dir="auto">

  <li>If you''ve been affected by this bug prior to this version, delete <code class="notranslate">TwlBg.cxi</code>
  in <code class="notranslate">sd:/luma/sysmodules/</code>, and re-follow the widescreen
  guide.</li>

  <li>This also fixes games from the console SD not booting after the flashcard is
  mounted via SCFG access.</li>

  </ul>

  </li>

  <li>Fixed white screen crash caused by hiyaCFW (again).

  <ul dir="auto">

  <li>Will not be reverted due to inevitable bugs related to NAND init/read code.</li>

  </ul>

  </li>

  </ul>'
updated: '2022-12-25T04:31:33Z'
version: v25.7.0
version_title: 'v25.7.0: TWL Christmas Release'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.