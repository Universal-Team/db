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
    size: 385250
    size_str: 376 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.50.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 935391
    size_str: 913 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.50.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 140
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
update_notes: '<p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v23.0.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v23.0.0</a></p>

  <p>Instructions:</p>

  <ol>

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>In the in-game menu''s RAM viewer, you can now switch between the ARM9 and ARM7
  memory maps by pressing SELECT!</li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>Donor ROMs are no longer needed in most cases!

  <ul>

  <li>One is no longer needed for games containing THUMB ARM7 binaries while in B4DS
  mode or when running from a CycloDS iEvolution.</li>

  <li>DSiWarehax users will still require one when running DSi-Enhanced titles in
  DSi mode, as well as a few DSiWare titles.</li>

  </ul>

  </li>

  <li>Future-proofed for some exploits of DSiWare titles containing MBK settings used
  for DSi-Enhanced games.</li>

  <li><strong>DSiWarehax users:</strong> If a DSiWare title uses a Donor ROM when
  running from the SD card, the traditional patch method is no longer used, allowing
  NAND files such as shared font to be read, thus allowing a few titles such as <em>Dr.
  Mario Express</em>, and the Japanese versions of <em>Bird &amp; Beans</em> and <em>Paper
  Plane</em> to boot.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated in-game menu translations.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>Fixed certain DSiWare titles not booting (as of v0.42.0), such as <em>Petit
  Computer</em> and <em>I am in the Movie</em>.</li>

  <li>The crash issue in <em>Tetris Party Deluxe</em> should now be fixed.</li>

  <li>Other minor fixes.</li>

  </ul>

  <p><strong>Known bugs</strong></p>

  <ul>

  <li>When scrolling through the ARM7 RAM, nds-bootstrap will crash after a few seconds.</li>

  <li>Certain games such as <em>Pokemon Dash</em> and <em>Golden Sun: Dark Dawn</em>,
  as well as DSiWare system titles such as <em>Nintendo DSi Camera</em> and <em>Nintendo
  DSi Sound</em> still won''t boot.

  <ul>

  <li>DSiWarehax users can still set <em>Nintendo DSi Sound</em> as a Donor ROM for
  DSi-Enhanced and certain DSiWare titles.</li>

  </ul>

  </li>

  </ul>'
updated: '2021-10-30T04:42:53Z'
version: v0.50.0
version_title: Halloween Eve release (2021)
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.