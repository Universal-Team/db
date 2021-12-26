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
    size: 399976
    size_str: 390 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.53.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 966862
    size_str: 944 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.53.0/nds-bootstrap.zip
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v23.3.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v23.3.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p dir="auto"><strong>What''s new?</strong></p>

  <ul dir="auto">

  <li><strong>B4DS mode:</strong> Support for more DSiWare titles have been added,
  making them playable on DS/DS lite consoles!<br>

  (For a complete list of supported titles, see this list <a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/3c3663d499b22effe92a5c3304836a8a9def549e/universal/include/incompatibleGameMap.h#L49">here</a>.)

  <ul dir="auto">

  <li>Flipper (music disabled)</li>

  <li>Art Style: PiCTOBiTS</li>

  <li>(For Debug DS consoles:)

  <ul dir="auto">

  <li>Cake Ninja</li>

  <li>Flipper 2: Flush the Goldfish</li>

  <li>Shantae: Risky''s Revenge (music disabled)</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><strong>In-game menu:</strong> The <code>Reset Game</code> option no longer
  reboots the console.</li>

  <li>An ESRB rating screen will now be shown, if <code>esrb.bin</code> is found in
  <code>sd:/_nds/nds-bootstrap/</code>.</li>

  <li>B4DS mode can now be enabled on flashcards with unlocked SCFG! Only use this
  for testing purposes. (.ini setting: <code>B4DS_MODE</code>)

  <ul dir="auto">

  <li>Setting to <code>1</code> will set the RAM to 4MB.</li>

  <li>Setting to <code>2</code> will set the RAM to the console''s maximum amount.
  Some games will not work with this setting.</li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Trivia</strong><br>

  <em>Flipper</em> was originally going to be released on a DS cartridge, but the
  original publisher went bankrupt, and was released as DSiWare instead. See this
  page <a href="https://goodbyegalaxygames.blogspot.com/2009/04/flipper-development.html?m=1"
  rel="nofollow">here</a> for more information.</p>'
updated: '2021-12-25T22:23:48Z'
version: v0.53.0
version_title: TWL Christmas Release (2021)
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.