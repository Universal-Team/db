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
    size: 1027489
    size_str: 1003 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.4.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1491795
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.4.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1218
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.12.5"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.12.5</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wokann/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wokann">@Wokann</a>:
  Added support for using direction sensor from the <em>Hoshizora Navi</em> cartridge
  in said game.</li>

  <li>Card Read DMA is no longer configurable and now disabled on flashcards (due
  to slowdown and/or crashes in certain games), except for these games which still
  require it:

  <ul dir="auto">

  <li>Army Men: Soldiers of Misfortune</li>

  <li>Call of Duty: Modern Warfare 3: Defiance</li>

  <li>The Magic School Bus: Oceans</li>

  <li>Tony Hawk''s American Sk8land</li>

  <li>Ultimate Mortal Kombat</li>

  </ul>

  </li>

  <li>Fixed AP-fix for <em>KuruKuru Princess: Tokimeki Figure: Mezase! Vancouver</em>.</li>

  <li>Removed AP-fix for <em>Super Kaseki Horider</em>, as it had no effect, and it
  is unknown how to fix it.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed where taking a screenshot or pressing <code class="notranslate">B</code>
  button after changing the main screen setting would cause a data abort error on
  flashcards in B4DS mode.</li>

  <li>Fixed a somewhat long-standing bug where the function which ends the current
  card read DMA operation is not called when running a DSi-Enhanced/Exclusive game
  in DSi mode.</li>

  </ul>'
updated: '2025-02-26T01:45:17Z'
version: v2.4.1
version_title: 'v2.4.1: Day 25 (2/25) in 2025 Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.