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
    size: 833710
    size_str: 814 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.14.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1206748
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.14.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1349
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.22.2"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.22.2</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <p dir="auto"><strong>B4DS</strong> = nds-bootstrap on DS flashcards</p>

  <h3 dir="auto">💝 What''s new? 💝</h3>

  <ul dir="auto">

  <li><strong>B4DS:</strong> <em>The Legend of Zelda: Four Swords: Anniversary Edition</em>
  no longer requires a Memory Expansion Pak to run!

  <ul dir="auto">

  <li>Main and map data are no longer fully pre-loaded. (They are still pre-loaded
  to the Memory Expansion Pak if inserted.)</li>

  <li>Audio is disabled in order for data to fit within the 4MB of RAM. Insert the
  Memory Expansion Pak to re-enable audio.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> Four DSiWare titles which used to only boot on debug
  DS consoles, now boot on regular DS consoles as well! (<strong>Total:</strong> 495
  -&gt; 499)

  <ul dir="auto">

  <li>Dragon Quest Wars (Memory Expansion Pak required)</li>

  <li>Oscar''s World Tour</li>

  <li>Puzzler World XL (Requires a VRAM-WiFi Donor ROM such as <em>Lufia: Curse of
  the Sinistrals</em>)</li>

  <li>Trajectile / Reflect Missile

  <ul dir="auto">

  <li>Achieved by making use of unused RAM space (1MB+25KB) left in by the overlay
  code.</li>

  <li>Audio does not play due to RAM limitation.</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/taxicat1/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/taxicat1">@taxicat1</a>:
  Added AP-fix for <em>Imagine: Resort Owner</em>/<em>Dream Resort</em>.</li>

  <li>Various: Updated in-game menu translations.</li>

  </ul>

  <h3 dir="auto">💝 Bug fixes (B4DS) 💝</h3>

  <ul dir="auto">

  <li>Hovering over Realm of Memories in <em>Zelda: Four Swords</em> no longer causes
  a crash!</li>

  <li>Fixed where <em>Everyday Soccer</em> / <em>ARC Style: Soccer</em> would show
  a Data Abort error with a Memory Expansion Pak inserted.</li>

  <li>Selecting the DS Download Play option in <em>Everyday Soccer</em> / <em>ARC
  Style: Soccer</em> no longer causes a crash!</li>

  <li>Fixed a bug which caused a Data Abort error to appear for <em>Tony Hawk''s Downhill
  Jam</em>.</li>

  <li>Card read DMA patch is now enabled for <em>Tales of Innocence</em> as an attempt
  to fix the game not booting.</li>

  </ul>

  <h3 dir="auto">Known bugs (B4DS)</h3>

  <ul dir="auto">

  <li>Stages within Realm of Memories does not play music in <em>Zelda: Four Swords</em>
  due to RAM limitation.</li>

  <li><em>Dragon Quest Wars</em> is known to crash at Training Lv. 4 and/or after
  a Survival battle.</li>

  </ul>'
updated: '2026-02-15T03:46:52Z'
version: v2.14.0
version_title: 'v2.14.0: I ❤️ DS⁽ⁱ⁾Ware'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.