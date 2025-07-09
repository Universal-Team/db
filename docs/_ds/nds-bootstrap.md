---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 1065544
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.7.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1543948
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.7.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1267
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.16.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.16.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed an overlooked bug which caused some games to either not boot or show a
  save corrupted message on DSi/3DS consoles.

  <ul dir="auto">

  <li>If this bug has caused your save data to be erased, make sure you have backups
  ready. If you have not tried v2.7.0, please update to this version immediately just
  in case.</li>

  </ul>

  </li>

  </ul>

  <h2 dir="auto">v2.7.0 Changelog</h2>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wokann/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wokann">@Wokann</a>:
  Added an option to disable save relocation, so that games still save within their
  original game cards. Useful for trying to run game translations, but still want
  to using the original game card for save data.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>B4DS:</strong> Successfully fixed the in-game menu not opening on Ace3DS+
  flashcards and its clones! (Yup, it''s fixed for real this time!)

  <ul dir="auto">

  <li>The fix has not been applied to DSi/3DS users outside of B4DS mode, as it is
  unknown if the same bug occurs outside of B4DS mode.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Fixed an overlooked bug which caused color LUT/screen
  filter to not apply for DSi-Enhanced/Exclusive games in DSi mode.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li><strong>B4DS:</strong> In order for the in-game menu to now open on Ace3DS+
  flashcards and its clones, it no longer checks for active wireless communications.
  As a result, the in-game menu can now be opened during active wireless communications
  as well, which can cause the connection to drop, depending on the game.</li>

  </ul>'
updated: '2025-07-04T09:23:21Z'
version: v2.7.1
version_title: v2.7.1 (hotfix)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.