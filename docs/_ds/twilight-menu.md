---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
color: '#464061'
created: '2017-05-06T05:28:36Z'
description: DSi Menu replacement for DS/DSi/3DS/2DS
download_page: https://github.com/DS-Homebrew/TWiLightMenu/releases
downloads:
  TWiLightMenu-3DS.7z:
    size: 34848793
    size_str: 33 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v23.0.0/TWiLightMenu-3DS.7z
  TWiLightMenu-DSi.7z:
    size: 34869392
    size_str: 33 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v23.0.0/TWiLightMenu-DSi.7z
  TWiLightMenu-Flashcard.7z:
    size: 46187835
    size_str: 44 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v23.0.0/TWiLightMenu-Flashcard.7z
  TWiLightMenu.7z:
    size: 46377899
    size_str: 44 MiB
    url: https://github.com/DS-Homebrew/TWiLightMenu/releases/download/v23.0.0/TWiLightMenu.7z
github: DS-Homebrew/TWiLightMenu
icon: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/booter/Twilight%2B%2B-animated%20icon-fix.gif
icon_index: 139
image: https://raw.githubusercontent.com/DS-Homebrew/TWiLightMenu/master/logo.png
image_length: 167469
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
update_notes: '<p>Check here on how to update <strong>TW</strong>i<strong>L</strong>ight
  Menu++:</p>

  <ul>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-flashcard.html"
  rel="nofollow">Flashcard</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-dsi.html" rel="nofollow">DSi</a></li>

  <li><a href="https://wiki.ds-homebrew.com/twilightmenu/updating-3ds.html" rel="nofollow">3DS</a></li>

  </ul>

  <p>Includes <a href="https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.50.0">nds-bootstrap
  v0.50.0</a></p>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>Donor ROMs are now only settable when

  <ol>

  <li>Running from a flashcard in DS mode, in order to run the few B4DS-supported
  DSi-Exclusives.</li>

  <li>Running from the console''s SD card while in DSiWarehax, in order to run DSi-Enhanced
  titles in DSi mode, as well as a few certain DSiWare titles.</li>

  </ol>

  </li>

  <li>When you get a message saying to set a Donor ROM, you can now press Right on
  the D-Pad to see how to set a Donor ROM.</li>

  <li>In per-game settings, a title''s SDK sub-version is now displayed!</li>

  <li>In per-game settings, when setting DSi mode for a DSi-Enhanced title, <code>VRAM
  mode</code> is now shown as <code>Auto</code>, as depending on the title, it may
  or may not use it.</li>

  <li>The used DSiWare exploit on DSi consoles is now automatically detected.</li>

  <li>The latest version of S8DS is now included!</li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>The settings description text is slightly smaller.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations.</li>

  <li>Some more DSiWare ROMs can now be set as a Donor ROM (ex. <em>DSi Sound</em>,
  <em>DSi Browser</em>, <em>DS WiFi Settings</em>, <em>Bejeweled Twist</em>, etc.).</li>

  <li>Changed <code>DSi mode</code> to <code>Auto</code>, and changed <code>DSi mode
  (Forced)</code> to <code>DSi mode</code>, both to avoid some confusion.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>Fixed the long-standing bug of lockups during reading/writing of either the
  console''s SD card or the CycloDS iEvolution, so you no longer need to close and
  open the console''s lid (or press HOME and B buttons) whenever a lockup would occur!

  <ul>

  <li>IPC Sync is now used instead of FIFO.</li>

  <li>CycloDS iEvolution''s DLDI code now runs from ARM7 (in DSi mode).</li>

  </ul>

  </li>

  <li>Fixed the AP-fix for <em>Anpanman to Touch de Waku Waku Training</em> to not
  require a Donor ROM.</li>

  <li>Other minor fixes.</li>

  </ul>'
updated: '2021-10-30T05:20:44Z'
version: v23.0.0
version_title: Halloween Eve release (2021)
wiki: https://wiki.ds-homebrew.com/twilightmenu/
---
TWiLight Menu++ is an open-source DSi Menu upgrade/replacement for the Nintendo DSi, the Nintendo 3DS, and Nintendo DS flashcards. It can launch Nintendo DS, SNES, NES, GameBoy (color), GameBoy Advance, Sega GameGear/Master System & Mega Drive/Genesis ROMs, as well as DSTWO plugins (if you use a DSTWO) and videos.

Please check the [wiki](https://wiki.ds-homebrew.com/twilightmenu/) for help installing.