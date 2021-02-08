---
author: DS-Homebrew
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v18.4.0
downloads:
  TWiLightMenu-3DS.7z:
    size: 32759563
    size_str: 31 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.4.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 32764083
    size_str: 31 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.4.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 45915477
    size_str: 43 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.4.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 46405533
    size_str: 44 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v18.4.0/TWiLightMenu.7z
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
priority: true
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

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/installing-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>Added <code>Hi</code> heap shrink setting.

  <ul>

  <li>Switch from <code>Lo</code> to <code>Hi</code>, if there''s a cheat that isn''t
  working for you.<br>

  If it still doesn''t work, then wait for a fix in nds-bootstrap.</li>

  <li>Currently only works with nightly nds-bootstrap build.</li>

  </ul>

  </li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Pressing START now skips the DSi splash screen!</li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Added special DSi splash screen for widescreen mode.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Clarified Nintendo logo description, as it''s only shown when there''s something
  inserted in Slot-1.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>PCE/TG16 game now boots through NitroGrafx.

  <ul>

  <li>You no longer need to manually navigate to the game again.</li>

  <li>NitroGrafx is directly booted, instead of through nds-bootstrap.</li>

  </ul>

  </li>

  <li>Fixed autoboot file for Original R4, by using the one from v15.3.0.</li>

  <li>Fixed volume positions from the theme <code>.ini</code> files not being used.

  <ul>

  <li>You''ll need to update any non-included skins from <a href="http://skins.ds-homebrew.com/"
  rel="nofollow">http://skins.ds-homebrew.com/</a> or the TWiLight skins UniStore
  in Universal-Updater, or the volume position will be wrong.</li>

  </ul>

  </li>

  <li>Fixed wrong top message shown when creating DSiWare save.</li>

  <li>Current directory path(s) is now reset, if not in their correct drives.</li>

  </ul>'
updated: '2021-01-30T06:00:34Z'
version: v18.4.0
version_title: v18.4.0
wiki: https://wiki.ds-homebrew.com/twilightmenu
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu) for help installing.