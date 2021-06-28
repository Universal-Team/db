---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 365988
    size_str: 357 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.43.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 889464
    size_str: 868 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.43.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://raw.githubusercontent.com/DS-Homebrew/nds-bootstrap/master/retail/assets/icon.bmp
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
update_notes: '<p>Instructions:</p>

  <ol>

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li>Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v21.0.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v21.0.0</a></p>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>The method used for the card read DMA alternative has been re-added as a new
  feature called <code>Asynch Card Read</code>!

  <ul>

  <li>This should remove some card-read-related lag that even TWL clock speed doesn''t
  completely remove.</li>

  <li>This is turned off by default, but TWLMenu++ turns it on by default, as it has
  a blacklist for some games to not use the feature.</li>

  </ul>

  </li>

  </ul>

  <p><strong>Improvement</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated in-game menu translations.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>Fixed where the system language would still be used in some DSiWare titles,
  such as <em>A Little Bit of... Nintendo Touch Golf</em>, regardless of set language
  setting.</li>

  <li>Fixed slowdown in <em>Tony Hawk''s American Sk8land</em>.

  <ul>

  <li>The asynch card read feature is required.</li>

  </ul>

  </li>

  <li><em>Jam with the Band</em> now boots!

  <ul>

  <li>The game may encounter an error after entering your information.</li>

  </ul>

  </li>

  <li>The precise volume control feature can now be used if one or both of the card
  read LEDs are enabled.</li>

  <li>Fixed <code>NDSBTSRP.LOG</code> not being written to the SD card, if both flashcard
  and SD card are mounted, and if the game is being run from the flashcard.</li>

  <li>Some other minor fixes.</li>

  </ul>'
updated: '2021-06-28T15:22:42Z'
version: v0.43.0
version_title: v0.43.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.