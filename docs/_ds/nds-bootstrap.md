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
    size: 374537
    size_str: 365 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.47.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 910667
    size_str: 889 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.47.0/nds-bootstrap.zip
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
update_notes: '<p><a target="_blank" rel="noopener noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/blob/8380002905becb9cb8f79b7ae353eb88d15aa3f1/screenshots/v0.47.0/AssassinsCreed2Discovery.png?raw=true"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/blob/8380002905becb9cb8f79b7ae353eb88d15aa3f1/screenshots/v0.47.0/AssassinsCreed2Discovery.png?raw=true"
  alt="screenshot1" style="max-width: 100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/blob/8380002905becb9cb8f79b7ae353eb88d15aa3f1/screenshots/v0.47.0/FotoShowdown.png?raw=true"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/blob/8380002905becb9cb8f79b7ae353eb88d15aa3f1/screenshots/v0.47.0/FotoShowdown.png?raw=true"
  alt="screenshot2" style="max-width: 100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/blob/806a594fa68bab1d60647fd17af2ff86cd214378/screenshots/v0.47.0/PokemonB2W2.png?raw=true"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/blob/806a594fa68bab1d60647fd17af2ff86cd214378/screenshots/v0.47.0/PokemonB2W2.png?raw=true"
  alt="screenshot3" style="max-width: 100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/blob/8380002905becb9cb8f79b7ae353eb88d15aa3f1/screenshots/v0.47.0/SystemFlaw.png?raw=true"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/blob/8380002905becb9cb8f79b7ae353eb88d15aa3f1/screenshots/v0.47.0/SystemFlaw.png?raw=true"
  alt="screenshot4" style="max-width: 100%;"></a><br>

  The above screenshots are taken straight from real hardware, without a capture card
  or an emulator!</p>

  <p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v21.5.1"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v21.5.1</a></p>

  <p>Instructions:</p>

  <ol>

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>You can now access the in-game menu, while running DSi-Enhanced/Exclusive games
  in DSi mode!</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>The patch offset cache from the previous nds-bootstrap version for each launched
  ROM should now be properly cleared without having to manually delete the <code>patchOffsetCache</code>
  folder in <code>sd:/_nds/nds-bootstrap/</code>.</li>

  <li>Fixed an overlooked bug that broke some homebrew compatibility.</li>

  </ul>'
updated: '2021-09-15T08:57:31Z'
version: v0.47.0
version_title: v0.47.0
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.