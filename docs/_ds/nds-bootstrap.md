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
    size: 837105
    size_str: 817 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.16.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1204507
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.16.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1371
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.24.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.24.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <p dir="auto"><strong>B4DS</strong> = nds-bootstrap on DS flashcards</p>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>3DS SD Card:</strong> When quitting the game from the in-game menu when
  running a DS(i) game in DS mode, it''ll no longer return to TWLMenu++ by default.
  A file called <code class="notranslate">srFrontendId.bin</code> is now read from
  <code class="notranslate">sd:/_nds/nds-bootstrap/</code> to determine which frontend
  to boot (ex. TWLMenu++ or akmenu-next) when quitting the game.

  <ul dir="auto">

  <li><code class="notranslate">srBackendId.bin</code> is used for resetting a few
  games/apps such as <em>Nintendo DS Browser</em>.</li>

  <li>If <code class="notranslate">srFrontendId.bin</code> is not found, it''ll return
  to the 3DS HOME Menu.</li>

  </ul>

  </li>

  <li><strong>B4DS:</strong> The original <em>Bloons</em> now runs on DS &amp; DS
  Lite consoles! (Saving does not work.) (DSiWare Total: 501 -&gt; 502)</li>

  <li><strong>3DS:</strong> Added ROM pre-load settings for <em>Retro Game Challenge</em>
  (USA).</li>

  <li>DSi-Exclusive/DSiWare ROMs are no longer used as donor ROMs for DSi-Enhanced
  games (outside of DSiWare exploits where they''re still used there).</li>

  <li>Various: Updated in-game menu translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/taxicat1/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/taxicat1">@taxicat1</a>:
  New "AP-fix" for <em>Houkago Shounen</em> which fixes soft-locking after saving.</li>

  <li>Fixed a (somewhat) long-standing bug which caused DSi sound data to not be detected
  in apps such as <em>Mario Clock</em> &amp; <em>Animal Crossing Clock</em>.</li>

  <li><strong>B4DS:</strong> Added alternate DSTWO DLDI driver to work around red
  error screen. (Thanks to stl25 for letting me know about that driver!)</li>

  <li>Fixed <em>Disgaea DS</em> having these issues when using a screen color filter
  and/or DS Phat colors:

  <ul dir="auto">

  <li>Top screen not refreshing</li>

  <li>Bottom screen displaying nothing</li>

  </ul>

  </li>

  </ul>'
updated: '2026-05-23T07:18:51Z'
version: v2.16.0
version_title: 'v2.16.0: Rocket Robz'' Birthday Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.