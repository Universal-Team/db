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
    size: 22143000
    size_str: 21 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/AddOn-BetterDSiMenuMusic.7z
  AddOn-ExtraUIMusic.7z:
    size: 8410144
    size_str: 8 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/AddOn-ExtraUIMusic.7z
  AddOn-Multimedia.7z:
    size: 804928
    size_str: 786 KiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/AddOn-Multimedia.7z
  AddOn-VirtualConsole-DSi-Flashcard.7z:
    size: 3748959
    size_str: 3 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/AddOn-VirtualConsole-DSi-Flashcard.7z
  AddOn-VirtualConsoleFull-3DS.7z:
    size: 3827367
    size_str: 3 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/AddOn-VirtualConsoleFull-3DS.7z
  AddOn-VirtualConsoleMinimal-3DS.7z:
    size: 3277311
    size_str: 3 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/AddOn-VirtualConsoleMinimal-3DS.7z
  TWiLightMenu-3DS.7z:
    size: 29206775
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 28780700
    size_str: 27 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 38854673
    size_str: 37 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 70154491
    size_str: 66 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v27.24.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_static: https://db.universal-team.net/assets/images/icons/twilight-menu.png
image: https://db.universal-team.net/assets/images/images/twilight-menu.png
image_length: 12520
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/TWiLightMenu
stars: 3959
systems:
- DS
title: TWiLight Menu++
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v2.16.0">nds-bootstrap
  v2.16.0</a></p>

  <p dir="auto">Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul dir="auto">

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <p dir="auto">To celebrate Rocket Robz'' birthday, the Rocket Robz logo (if enabled)
  has been updated with an improved background and text display (plus a shadow appearing
  underneath Robz for a 3D-like effect)!</p>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>As some of the emulators included in the Virtual Console add-on have better
  alternatives for 3DS users, the add-on has been split into Minimal and Full versions.

  <ul dir="auto">

  <li><strong>Minimal:</strong> Does not include NES/GEN/SNES/GBA emulators (recommended
  for most users)</li>

  <li><strong>Full:</strong> Does include NES/GEN/SNES/GBA emulators</li>

  <li>This change only applies to 3DS users. DSi and Flashcard users will still have
  a version of the add-on which includes all of the emulators (except for GBA, which
  comes with the default installation).</li>

  </ul>

  </li>

  <li><strong>3DS SD Card:</strong> The TID for TWLMenu++ is now written to both <code
  class="notranslate">srBackendId.bin</code> &amp; <code class="notranslate">srFrontendId.bin</code>
  (at <code class="notranslate">sd:/_nds/nds-bootstrap</code>) when launching a DS(i)
  game via nds-bootstrap. This will allow nds-bootstrap to reboot back to TWLMenu++
  when quitting a DS(i) game running in DS mode.</li>

  <li>Added cheat support for when Pico Loader is used as the flashcard game loader.</li>

  <li>Box art is now displayed for folders/directories!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  Re-enabled support for EZ-Flash Vi autoboot.</li>

  <li>If the alternate DSTWO DLDI driver is detected (when returning from nds-bootstrap),
  it''ll be switched to the normal one.</li>

  <li><strong>3DS UI:</strong> Updated the latest supported RVID version to v5.</li>

  <li>Various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Directories with <code class="notranslate">.</code> (dots) in their names are
  now properly supported in order for nds-bootstrap to run DSiWare from those kinds
  of directories.</li>

  <li>Fixed regression which caused some Slot-1 flashcards (and possibly game cards)
  to not boot.</li>

  </ul>'
updated: '2026-05-23T09:46:23Z'
version: v27.24.0
version_title: 'v27.24.0: Rocket Robz'' Birthday Release'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch games for the Nintendo DS, Nintendo DSi, and GameBoy Advance, as well as DSTWO plugins (if you use a DSTWO).

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.