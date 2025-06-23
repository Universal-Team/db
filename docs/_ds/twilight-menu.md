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
  AddOn-ExtraUIMusic.7z:
    size: 8420943
    size_str: 8 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/AddOn-ExtraUIMusic.7z
  AddOn-Multimedia.7z:
    size: 2383856
    size_str: 2 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/AddOn-Multimedia.7z
  AddOn-VirtualConsole.7z:
    size: 3619674
    size_str: 3 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/AddOn-VirtualConsole.7z
  TWiLightMenu-3DS.7z:
    size: 28950314
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 29003402
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 40028513
    size_str: 38 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 51352864
    size_str: 48 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.15.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_static: https://db.universal-team.net/assets/images/icons/twilight-menu.png
image: https://db.universal-team.net/assets/images/images/twilight-menu.png
image_length: 12520
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/TWiLightMenu
stars: 3537
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v2.6.0">nds-bootstrap
  v2.6.0</a></p>

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

  <li>In order to reduce bloat, the non-default DSi/3DS UI music + HBL music, emulators
  (considered as TWLMenu++ Virtual Console) and multimedia features (image viewing
  and video playing) have now been split into three separate add-ons, and are no longer
  bundled by default.

  <ul dir="auto">

  <li>To restore these features, follow the steps for <a href="https://wiki.ds-homebrew.com/twilightmenu/installing-addons"
  rel="nofollow">installing add-ons</a>.</li>

  <li>GBARunner2 (to be replaced with GBARunner3 in the future) will remain bundled
  for playing GBA games as an essential feature.</li>

  </ul>

  </li>

  <li><code class="notranslate">dsiware</code> folder has been renamed to <code class="notranslate">dsi</code>
  in order to be a folder for any DSi ROM (both from game cards and as DSiWare).</li>

  <li><strong>DSi/3DS:</strong> When launching a DS(i) game via nds-bootstrap with
  screen filter and/or DS Phat colors enabled, TWL clock speed will now be used by
  default in order to speed up the filter processing (mainly for Actimagine/Mobiclip
  videos), unless the game is blacklisted from using TWL clock speed.</li>

  <li>tuna-viDS now supports screen filters!</li>

  <li>Both AmEDS and CrocoDS (outdated Amstrad CPC emulators) have been replaced with
  <a href="https://github.com/wavemotion-dave/SugarDS">SugarDS</a> (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/wavemotion-dave/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/wavemotion-dave">@wavemotion-dave</a>)!</li>

  <li>Slightly increased the volume of the DS &amp; DSi splash sounds to closely match
  their original volumes.</li>

  <li>The DS tap sound in the DS &amp; DSi splash screens has been replaced with the
  DSi version.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mentusfentus/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mentusfentus">@mentusfentus</a>:
  <strong>DS Classic Menu:</strong> Calendar and top-bar datetime are now drawn using
  monospaced characters. (<a href="https://github.com/DS-Homebrew/TWiLightMenu/pull/2534"
  data-hovercard-type="pull_request" data-hovercard-url="/DS-Homebrew/TWiLightMenu/pull/2534/hovercard">What
  this means</a>)</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mentusfentus/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mentusfentus">@mentusfentus</a>:
  <strong>DS Classic Menu:</strong> Calendar weekdays are now translatable!</li>

  <li>Various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi-based UIs:</strong> The checks for DSi binaries and AP-patch now
  reset when swiping icons or dragging scroll bar.</li>

  <li><strong>R4 and Wood UIs:</strong> Fixed the per-game settings menu not appearing
  for ROMs with a custom banner.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/mentusfentus/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mentusfentus">@mentusfentus</a>:
  <strong>DS Classic Menu:</strong> Fixed black background when using Saturn &amp;
  HBL UIs.</li>

  <li><strong>DS:</strong> Fixed white screen crash on SuperCard CF flashcards (not
  to be confused with SuperCard MiniSD).</li>

  </ul>'
updated: '2025-06-18T07:02:10Z'
version: v27.15.0
version_title: v27.15.0
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch games for the Nintendo DS, Nintendo DSi, and GameBoy Advance, as well as DSTWO plugins (if you use a DSTWO).

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.