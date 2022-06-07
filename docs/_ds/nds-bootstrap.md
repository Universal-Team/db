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
    size: 431613
    size_str: 421 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.58.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1044496
    size_str: 1020 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.58.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 139
image: https://i.imgur.com/BFIu7xX.png
image_length: 5116
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.9.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.9.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
  Brightness and volume adjust options have been added to the in-game menu!

  <ul dir="auto">

  <li>Only DSi has both, 3DS only has volume and DS (Lite) only have brightness.</li>

  </ul>

  </li>

  <li>When detecting rumble for DSiWare titles, it no longer checks for TIDs of GBA
  games, in order for custom GBA carts with rumble to work as well.</li>

  </ul>

  <h4 dir="auto">What''s new?/Bug fixes</h4>

  <ul dir="auto">

  <li>For all you Smash fans out there, and/or if you''re looking for a good homebrew
  game to play, <em>Super Smash Bros. Crash</em> is now playable!

  <ul dir="auto">

  <li>This also means that old loaders such as DSi4DS will now work properly as well.</li>

  </ul>

  </li>

  <li>Most homebrew before 2009/2010 (such as SSBC, MegaETk, etc.) will now work properly
  in DSiWarehax!</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Patch offsets are now cached for homebrew!

  <ul dir="auto">

  <li>This makes homebrew boot faster after the first boot, though it may depend on
  the homebrew.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><em>The Legend of Zelda: Four Swords: Anniversary Edition</em> and <em>Phantasy
  Star 0 Mini</em> now boot with Memory Pit!</li>

  <li>Card read DMA is now automatically turned off when wireless/WiFi operations
  are occurring.

  <ul dir="auto">

  <li>While this should fix connection interruptions, it may not fix some of them.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li>Background music in <em>Super Smash Bros. Crash</em> does not play while running
  via DSiWarehax.</li>

  <li>Loaders such as DSi4DS do not work properly with RAM disks.</li>

  <li>Not an nds-bootstrap issue, but <em>Super Smash Bros. Crash</em> will freeze
  after fighting the new approaching challenger. When that happens, just restart the
  game, as the data has already been saved.</li>

  </ul>

  <h2 dir="auto">FAQs</h2>

  <ul dir="auto">

  <li><strong>Q:</strong> Does Wii connectivity with <em>Pokemon</em> work now?<br>

  <strong>A:</strong> Nope, not yet. The function that starts the SRL executable file
  sent from the Wii is not yet patched.</li>

  <li><strong>Q:</strong> Does <em>Golden Sun: Dark Dawn</em> work now?<br>

  <strong>A:</strong> Nope. At this rate, it''s going to be a <em>long</em> while
  until it finally works.</li>

  </ul>'
updated: '2022-06-07T01:31:31Z'
version: v0.58.0
version_title: 'v0.58.0: TWL Summer Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.