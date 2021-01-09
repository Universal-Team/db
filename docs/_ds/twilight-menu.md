---
author: DS-Homebrew
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v18.2.0
downloads:
  TWiLightMenu-3DS.7z:
    size: 31701488
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.2.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 31705646
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.2.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 44804583
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.2.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 45202324
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.2.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
image: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/logo.png
image_length: 142608
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
    TWiLightMenu-Lite.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu-Lite.7z
    TWiLightMenu.7z:
      url: https://github.com/TWLBot/Builds/raw/master/TWiLightMenu.7z
source: https://github.com/DS-Homebrew/TWiLightMenu
systems:
- DS
title: TWiLight Menu++
update_notes: '<p>Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/installing-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/installing-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/installing-3ds.html" rel="nofollow">3DS</a>

  <ul>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/installing-3ds-manual.html"
  rel="nofollow">Manual</a></li>

  </ul>

  </li>

  </ul>

  <p><strong>NOTE:</strong> Some users have reported getting Guru Meditation Error
  in the DSi/3DS/Saturn/HBL themes in this version, during loading the ROM list.<br>

  If you get the same error, please switch the theme or downgrade to v18.1.0.</p>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>The Atari emulators have been updated to their latest versions!</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  You can now select a custom font. See <a href="https://wiki.ds-homebrew.com/twilightmenu/custom-fonts"
  rel="nofollow">here</a> on how to add one.</li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  More font data is now loaded, if running in DSi mode.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  <strong>DSi, 3DS, Saturn, and HBL themes:</strong> Selected item in the cheat list
  can now scroll.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li><strong>Native GBA ROM loader (DS Phat/lite):</strong>

  <ul>

  <li><em>Mario Kart: Super Circuit</em>, <em>Doom</em>, and <em>Doom II</em> now
  boot!</li>

  <li>The GBA GamePak Prefetch feature is now enabled before the game boots!<br>

  This fixes some slowdown in some games, which don''t occur in retail carts.<br>

  <strong>NOTE:</strong> Games already use this feature, but as the wait states are
  patched out in order for the games to boot, games would previously be unable to
  enable the feature.</li>

  </ul>

  </li>

  <li>Fixed 3D cubes not being rendered in the 3DS theme, if photo/boxart color de-banding
  is turned on.

  <ul>

  <li>This skips photo/boxart color de-banding, if the 3D cube video is found.</li>

  </ul>

  </li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Changed <code>Greyscale</code> to <code>Grayscale</code>.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed non-ASCII DSiWare path being passed to Unlaunch.</li>

  <li>Fixed cluster size warning being shown if cluster size is above 32KB.</li>

  </ul>'
updated: '2021-01-09T00:26:18Z'
version: v18.2.0
version_title: v18.2.0
wiki: https://wiki.ds-homebrew.com/twilightmenu
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu) for help installing.