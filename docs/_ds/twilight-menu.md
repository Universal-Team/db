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
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/AddOn-BetterDSiMenuMusic.7z
  AddOn-ExtraUIMusic.7z:
    size: 8420942
    size_str: 8 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/AddOn-ExtraUIMusic.7z
  AddOn-Multimedia.7z:
    size: 806068
    size_str: 787 KiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/AddOn-Multimedia.7z
  AddOn-VirtualConsole.7z:
    size: 3739973
    size_str: 3 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/AddOn-VirtualConsole.7z
  TWiLightMenu-3DS.7z:
    size: 29233699
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 28756666
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 38895942
    size_str: 37 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 70215584
    size_str: 66 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.21.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_static: https://db.universal-team.net/assets/images/icons/twilight-menu.png
image: https://db.universal-team.net/assets/images/images/twilight-menu.png
image_length: 12520
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/TWiLightMenu
stars: 3761
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto"><strong>UPDATE 12/26/2025:</strong> Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v2.12.1">nds-bootstrap
  v2.12.1</a><br>

  <strong>UPDATE 12/30/2025:</strong> Updated Multimedia add-on to include <a href="https://github.com/RocketRobz/RocketVideoPlayer/releases/tag/v2.1.1">Rocket
  Video Player v2.1.1</a></p>

  <p dir="auto">Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul dir="auto">

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <p dir="auto"><strong>Reminder:</strong> If you have installed TWLMenu++ before
  the release of this update, some emulators have been updated later after the release
  of the TWLMenu++ version which introduced the Virtual Console add-on.<br>

  Please update the Virtual Console add-on to ensure you have the latest versions
  of the emulators installed.</p>

  <h3 dir="auto">🎁 What''s new? 🎁</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/edo9300/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/edo9300">@edo9300</a>:
  Improved the Games n'' Music DLDI driver.</li>

  <li>Swapped names of the flashcard <code class="notranslate">boot.nds</code> and
  <code class="notranslate">boot_alt.nds</code> files.</li>

  <li><strong>Multimedia add-on update:</strong> The image viewer now plays animated
  GIF files.</li>

  <li>Added detection of SuperCard SD Slot-2 flashcards for use as RAM expansion if
  SuperFW is installed.</li>

  <li>The SuperCard SD Slot-2 flashcard can now be launched from the DS Classic Menu,
  even when used as RAM expansion.

  <ul dir="auto">

  <li>Untested with M3 and G6 Slot-2 flashcards.</li>

  </ul>

  </li>

  <li>Various: Updated translations.</li>

  </ul>

  <h3 dir="auto">🎁 Bug fixes 🎁</h3>

  <ul dir="auto">

  <li>The <code class="notranslate">Touch the touch screen to continue...</code> message
  in the DSi splash screen now appears a few frames early, in order to match the original
  splash screen as closely as possible.</li>

  <li>The <code class="notranslate">Touch the touch screen to continue...</code> message
  now appears in the Super NDS splash screen without auto-skipping.</li>

  <li>The tap sound no longer plays when auto-skipping DS/DSi splash screen.</li>

  <li><strong>Flashcard users:</strong> The <code class="notranslate">Game Loader</code>
  setting is now shown even if kernel isn''t useable.</li>

  <li><strong>Flashcard users:</strong> Fixed nds-bootstrap per-game settings being
  shown if flashcard kernel isn''t useable, and if nds-bootstrap is not used as the
  game loader.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/DieGo367/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DieGo367">@DieGo367</a>:
  Fixed glitchy palettes for some animated icons. (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="3752533000" data-permission-text="Title
  is private" data-url="https://github.com/DS-Homebrew/TWiLightMenu/issues/2605" data-hovercard-type="pull_request"
  data-hovercard-url="/DS-Homebrew/TWiLightMenu/pull/2605/hovercard" href="https://github.com/DS-Homebrew/TWiLightMenu/pull/2605">#2605</a>)</li>

  <li>Fixed PNG files not appearing (if the Multimedia add-on is installed).</li>

  <li>Fixed DSi/3DS console not rebooting when running from DS(i) game card (aka Slot-1)
  and when trying to soft-reset.</li>

  <li>The DSi SD init code is no longer run on DS &amp; DS Lite consoles.

  <ul dir="auto">

  <li>Fixes white screen lockup in DeSmuME.</li>

  </ul>

  </li>

  <li>VCOUNT register is no longer cleared before boot. Fixes a possible bug where
  a frame could be misrendered on 3DS consoles.</li>

  </ul>'
updated: '2025-12-25T12:04:04Z'
version: v27.21.0
version_title: 'v27.21.0: TWL Christmas Release 🎄'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch games for the Nintendo DS, Nintendo DSi, and GameBoy Advance, as well as DSTWO plugins (if you use a DSTWO).

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.