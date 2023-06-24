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
    size: 724372
    size_str: 707 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.72.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1739971
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.72.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.11.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.11.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>The save soft-locking bug in <em>Pokemon B&amp;W 1&amp;2</em> and some other
  games has been fixed once again.</li>

  <li>Fixed communication errors when booting Pictochat or DLP apps.</li>

  <li><em>My Healthy Cooking Coach</em> has been blacklisted from using card read
  DMA, in order to boot.</li>

  <li>The patch offset cache should now be properly cleared, when found to be out
  of date.

  <ul dir="auto">

  <li>This should fix some games not booting, of which have previously been booted
  by a prior nds-bootstrap version.</li>

  </ul>

  </li>

  <li>After opening the in-game menu, and when closing the 3DS or 2DS console''s lid,
  it''ll no longer lock up on black screens.</li>

  <li>Attempted to add compatibility for SD cards of lesser-known brands, by disabling
  NDMA before the game boots.

  <ul dir="auto">

  <li>NDMA is now always disabled for homebrew.</li>

  </ul>

  </li>

  </ul>'
updated: '2023-06-24T03:54:58Z'
version: v0.72.1
version_title: v0.72.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.