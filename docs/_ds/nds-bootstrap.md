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
    size: 859332
    size_str: 839 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.1.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1331462
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.1.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1185
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.11.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.11.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Re-added support for 16KB DLDI drivers, and for
  the first time ever, 32KB DLDI drivers are now supported!

  <ul dir="auto">

  <li>This basically means that old flashcards such as the N-Card will now work with
  nds-bootstrap!</li>

  <li>libnds32 (by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/lifehackerhansol/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>)
  is used along with shrinking the game''s heap (starting with SDK 2.1) in order to
  achieve this. (See "<strong>Known bug</strong>".)</li>

  </ul>

  </li>

  <li>Some games will now have ROM data pre-loaded after boot instead of before boot,
  speeding up boot times for such games.</li>

  <li><strong>B4DS mode:</strong> Two ROMs will now have some data pre-loaded into
  the Memory Expansion Pak before boot (<em>Base 10</em> &amp; <em>Sonic Rush Adventure</em>)
  in order to reduce screen flickering and slightly improve speed!</li>

  <li><strong>B4DS mode:</strong> In an attempt to reduce crashing in the following
  DSiWare titles, the DLDI driver has been moved to ITCM to make as much of the console''s
  4MB of RAM available as possible.

  <ul dir="auto">

  <li>AiRace: Tunnel (limited up to 16KB DLDI drivers)</li>

  <li>Need for Speed: Nitro-X (limited up to 16KB DLDI drivers)</li>

  <li>Orion''s Odyssey</li>

  <li>Phantasy Star 0 Mini</li>

  <li>Picture Perfect: Pocket Stylist</li>

  <li>Tales to Enjoy!: Little Red Riding Hood</li>

  <li>Tales to Enjoy!: Puss in Boots</li>

  <li>Tales to Enjoy!: The Three Little Pigs</li>

  <li>Tales to Enjoy!: The Ugly Duckling</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Added ROM pre-load settings for <em>MegaMan Battle Network 5: Double Team DS</em>
  (Undub) on DSi consoles to reduce slowdown in the opening intro.</li>

  <li><strong>B4DS mode:</strong> Fixed a long-standing bug (since v0.73.0) which
  caused SDK5.5 DSiWare titles containing cloneboot (ex. <em>Box Pusher</em>) to not
  boot.</li>

  <li>Fixed an overlooked bug which caused <em>KORG DS-10+ Synthesizer</em> to not
  boot in DSi mode on DSi consoles.</li>

  <li><strong>B4DS mode:</strong> Fixed VS mode in <em>Base 10</em> causing a crash.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>:
  Minor improvements.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>Some games may not boot with 16KB or 32KB DLDI drivers (used by N-Card or a
  few other old flashcards). If you are playing a DSiWare title on DS or DS Lite,
  make sure to set <em>Lufia: Curse of the Sinistrals</em> as a donor ROM in order
  to reduce crashing.</li>

  </ul>'
updated: '2024-10-31T06:56:37Z'
version: v2.1.0
version_title: 'v2.1.0: Halloween Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.