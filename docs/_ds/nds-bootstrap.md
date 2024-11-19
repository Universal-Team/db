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
    size: 1117653
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.2.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1671046
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.2.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1193
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.12.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.12.1</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Sound data is now pre-loaded for Gen 4 mainline Pokemon games!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  Removed unused code.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/edo9300/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/edo9300">@edo9300</a>
  &amp; <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Gericom/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Gericom">@Gericom</a>:
  <strong>B4DS mode:</strong> Patch mpu configurations when running off SLOT-2 (<a
  href="https://github.com/DS-Homebrew/nds-bootstrap/issues/1748" data-hovercard-type="pull_request"
  data-hovercard-url="/DS-Homebrew/nds-bootstrap/pull/1748/hovercard">#1748</a>)

  <ul dir="auto">

  <li>Change the mpu settings when a SLOT-2 device is being used, fixes issues with
  games like gen5 pokemon, that block the whole address space beyond 0x08000000 when
  not in use</li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> Selecting <code class="notranslate">Reset Game</code>
  or <code class="notranslate">Quit Game</code> will no longer cause the console to
  power off (on DS/DS Lite) or reboot (on DSi/3DS)!

  <ul dir="auto">

  <li>Does not apply to DSiWare.</li>

  </ul>

  </li>

  <li>Fixed pre-loaded ROM data not being loaded or read correctly.

  <ul dir="auto">

  <li>Applies to games which have nds-bootstrap pre-load the data after boot.</li>

  <li>Fixes music not playing in <em>SaGa 3</em>, the <em>Dragon Quest</em> games,
  <em>Style Savvy</em>, and other games which have sdat files pre-loaded.</li>

  <li>Also fixes T-posed characters in <em>Phantasy Star 0</em> on 3DS, and crashing
  after starting <em>Final Fantasy III</em>.</li>

  </ul>

  </li>

  </ul>'
updated: '2024-11-18T22:11:43Z'
version: v2.2.1
version_title: v2.2.1
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.