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
    size: 42806297
    size_str: 40 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.11.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 42845305
    size_str: 40 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.11.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 53927744
    size_str: 51 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.11.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 54156187
    size_str: 51 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.11.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_static: https://db.universal-team.net/assets/images/icons/twilight-menu.png
image: https://db.universal-team.net/assets/images/images/twilight-menu.png
image_length: 12520
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/TWiLightMenu
stars: 3286
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v2.1.0">nds-bootstrap
  v2.1.0</a></p>

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

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  Added AP-fix for <em>Pokémon Moon Black 2</em> (v4.2.4).</li>

  <li>Added AP-fix for <em>Kawaii Koinu DS 3</em> (Rev 1).</li>

  <li>Added support for 32KB DLDI drivers, allowing old flashcards such as the N-Card
  to work! (Thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ApacheThunder/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ApacheThunder">@ApacheThunder</a>
  for testing!)

  <ul dir="auto">

  <li>libnds32 (by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lifehackerhansol/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>)
  is used in order to achieve this.</li>

  </ul>

  </li>

  <li>Added autoboot files for the following flashcards:

  <ul dir="auto">

  <li>N-Card</li>

  <li>R4 3DS Gold RTS/PK3DS (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Deletecat/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Deletecat">@Deletecat</a>)</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Removed loading ARM binaries of booted <code class="notranslate">.nds</code>
  file to the Memory Expansion Pak, in order to avoid possible crashes.</li>

  <li>The default <code class="notranslate">Load Bootloader</code> setting has been
  reverted from <code class="notranslate">Direct</code> to <code class="notranslate">Thru
  nds-bs</code> in order to fix white screen crashes for some users when trying to
  play a GBA game via GBARunner2 or loading other DS homebrew.</li>

  <li>If the last-used folder is not found, TWLMenu++ will now start at the SD root
  on the first page and title.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>Modern homebrew will not init FAT/DLDI with old flashcards such as the N-Card,
  due to their DLDI drivers being larger than 16KB. This is caused by the homebrew
  and not TWLMenu++.</li>

  </ul>'
updated: '2024-10-31T07:12:40Z'
version: v27.11.0
version_title: 'v27.11.0: Halloween Release'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.