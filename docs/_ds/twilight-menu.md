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
    size: 32867717
    size_str: 31 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.6.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 32915396
    size_str: 31 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.6.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 43700419
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.6.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 43902058
    size_str: 41 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v25.6.0/TWiLightMenu.7z
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
update_notes: '<p dir="auto">Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.67.0">nds-bootstrap
  v0.67.0</a></p>

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

  <li>The first 32KB of both the arm9 &amp; arm7 DSi BIOS is now dumped to <code class="notranslate">sd:/_nds/</code>
  for use by nds-bootstrap.</li>

  <li><strong>TW</strong>i<strong>L</strong>ight Menu++ is no longer required to be
  installed on your flashcard in order to access it''s contents from DSi/3DS SD card
  with unlocked SCFG!

  <ul dir="auto">

  <li>It may still need to be installed there in order to run some retro games from
  the flashcard.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Mr. Start: The <em>Super Nintendo DS</em> splash screen (only viewable with
  Slot-2 flashcards which aren''t EZ-Flash) has been updated!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
  WAV header is now used for converted ADPCM music, in order to fix where the sample
  rate is wrong on second play of the music.</li>

  <li>The last 16KB of the DSi WRAM is no longer cleared in order for dsibiosdumper
  to work correctly.</li>

  <li>Fixed the SD removal check being tripped in DS Classic Menu (the result of the
  black screens with white text) depending on how much RAM is used.</li>

  <li>Fixed Slot-1 or some flashcards not booting with <code class="notranslate">Slot-1
  microSD access</code> turned off.</li>

  </ul>'
updated: '2022-11-25T02:47:35Z'
version: v25.6.0
version_title: 'v25.6.0: Thanksgiving release (2022)'
website: https://wiki.ds-homebrew.com/twilightmenu/
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.