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
    size: 465627
    size_str: 454 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.63.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1115713
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.63.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.2.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.2.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>More DSiWare titles are now playable on DS Phat/Lite consoles! (<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/9523f9a6be16aab5e2499028d47db8fe42cfd931/universal/include/compatibleDSiWareMap.h">Full
  list of compatible titles</a>)

  <ul dir="auto">

  <li><strong>Debug units only</strong> (Total: 21 -&gt; 22) (<em>Absolute Baseball</em>
  &amp; <em>Candle Route</em> did not boot, so they got removed.)

  <ul dir="auto">

  <li>Cake Ninja 2</li>

  <li>Cake Ninja: XMAS</li>

  <li>The Legend of Zelda: Four Swords: Anniversary Edition</li>

  </ul>

  </li>

  </ul>

  </li>

  <li>On DSi consoles, AP-patched overlays are now saved to a separate file in order
  to avoid shrinking the heap size beyond how much the title would allocate, when
  running DSi-Enhanced titles in DSi mode.

  <ul dir="auto">

  <li>This allows the AP-fix (bundled with TWLMenu++) for <em>Mario vs. Donkey Kong:
  Mini-Land Mayhem</em> to work properly in DSi mode on DSi consoles.</li>

  </ul>

  </li>

  <li><em>Dragon Quest V</em> no longer uses card data cache.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Added Catalan language.</li>

  </ul>

  <h3 dir="auto">Improvement</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various: Updated translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed <em>Pokémon Black &amp; White Versions 2</em> (untrimmed) running very
  slow on SD cards formatted with 4KB cluster size.</li>

  <li>Fixed <em>Kirby: Canvas Curse</em> not reading save data.</li>

  <li>Fixed the <em>Cake Ninja</em> titles freezing on top black screen.

  <ul dir="auto">

  <li>This is achieved by clearing the R0-R11 registers before booting the set <code
  class="notranslate">.nds</code> file.</li>

  </ul>

  </li>

  <li>As a result of disabling card data cache for <em>Dragon Quest V</em>, the intro
  no longer loops back to the logos at the start.</li>

  <li>Fixed sleep mode crashing the DS Phat/Lite console in <em>99Bullets</em>, <em>99Moves</em>,
  and <em>99Seconds</em>.</li>

  <li>Fixed known issues related to running DSiWare titles only supported on DS Debug
  units.</li>

  <li>Some other minor fixes, as well as removing unused code.</li>

  </ul>

  <h3 dir="auto">FAQ</h3>

  <ul dir="auto">

  <li><strong>Q:</strong> Any updates on support for <em>Golden Sun: Dark Dawn</em>?

  <ul dir="auto">

  <li><strong>A:</strong> We have found why the game does not boot, as the crash occurs
  in one of the game''s overlay files. However, even after setting breakpoints in
  the NO$GBA debugger, it is still unclear as to how the game boots successfully outside
  of nds-bootstrap. <a href="https://github.com/DS-Homebrew/nds-bootstrap/issues/252#issuecomment-1206101918"
  data-hovercard-type="issue" data-hovercard-url="/DS-Homebrew/nds-bootstrap/issues/252/hovercard">More
  information...</a></li>

  </ul>

  </li>

  </ul>'
updated: '2022-08-09T01:48:36Z'
version: v0.63.0
version_title: 'v0.63.0: TWL Summer Release #7'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.