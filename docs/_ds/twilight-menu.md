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
downloads: {}
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
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.59.0">nds-bootstrap
  v0.59.0</a></p>

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

  <li>Added AP-fixes for <em>Inazuma Eleven 3</em> and <em>Ni no Kuni</em> (Spanish
  translations).</li>

  <li>nds-bootstrap-hb''s bootloader is now directly loaded, eliminating the middleman,
  so booting old DS homebrew is now 2 seconds faster!

  <ul dir="auto">

  <li>Currently only applies to DSi-based themes and the DS Classic Menu, the latter
  of which pre-loads the homebrew''s ARM9 binary for a slightly faster boot.</li>

  </ul>

  </li>

  <li>The <code class="notranslate">Direct boot</code> setting has been removed for
  console SD users.

  <ul dir="auto">

  <li>Pre-2009 DS homebrew will now always use nds-bootstrap, and 2009 or later homebrew
  will use nds-bootstrap if either DS mode or a RAM disk is set.</li>

  </ul>

  </li>

  <li>For homebrew with large ARM9 binaries (ex. SM64DSi), all per-game settings except
  <code class="notranslate">Language</code> and <code class="notranslate">Region</code>
  are now hidden.</li>

  <li>(<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/chishm/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/chishm">@chishm</a>)
  With FastVideoDS still to come in the future, an old obscure video player, tuna-viDS,
  has been added for Xvid (.avi) video playback!

  <ul dir="auto">

  <li>See <a href="https://gbatemp.net/threads/tuna-vids-guide-for-dsi.613493/" rel="nofollow">this</a>
  guide for how to convert a video, starting from Step 2.</li>

  </ul>

  </li>

  <li>SNEmulDS has been reverted to the legacy pre-TGDS build to work around a few
  bugs.

  <ul dir="auto">

  <li>As the TGDS build is still bundled, you can switch to it by setting <code class="notranslate">NEW_SNES_EMU_VER</code>
  to <code class="notranslate">1</code> in <code class="notranslate">sd:/_nds/TWiLightMenu/settings.ini</code>.</li>

  </ul>

  </li>

  <li>The VRAM mode setting can now be changed for when running NTR games in DSi mode.</li>

  </ul>'
updated: '2022-06-21T22:19:22Z'
version: v24.10.0
version_title: 'v24.10.0: TWL Summer Solstice Release'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.