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
    size: 371412
    size_str: 362 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.46.1/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 901872
    size_str: 880 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.46.1/nds-bootstrap.zip
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
update_notes: "<p><a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/metroidPrimeHunters.png\"\
  ><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/metroidPrimeHunters.png\"\
  \ alt=\"screenshot1\" style=\"max-width:100%;\"></a> <a target=\"_blank\" rel=\"\
  noopener noreferrer\" href=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/sonicColors.png\"\
  ><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/sonicColors.png\"\
  \ alt=\"screenshot2\" style=\"max-width:100%;\"></a> <a target=\"_blank\" rel=\"\
  noopener noreferrer\" href=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/sonicSegaRacing.png\"\
  ><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/sonicSegaRacing.png\"\
  \ alt=\"screenshot3\" style=\"max-width:100%;\"></a><br>\n<a target=\"_blank\" rel=\"\
  noopener noreferrer\" href=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/marioVsDk2.png\"\
  ><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/marioVsDk2.png\"\
  \ alt=\"screenshot4\" style=\"max-width:100%;\"></a> <a target=\"_blank\" rel=\"\
  noopener noreferrer\" href=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/styleSavvy.png\"\
  ><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.1/styleSavvy.png\"\
  \ alt=\"screenshot5\" style=\"max-width:100%;\"></a><br>\nThe above screenshots\
  \ are taken straight from real hardware, without a capture card or an emulator!</p>\n\
  <p>Instructions:</p>\n<ol>\n<li>Download the <code>.7z</code> file.</li>\n<li>Extract\
  \ the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n\
  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v21.4.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v21.4.0</a></p>\n<p><strong>Improvement</strong></p>\n\
  <ul>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated in-game menu translations.</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n\
  <ul>\n<li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a>) Screenshots\
  \ of ActImagine/MobiClip videos are no longer blank!</li>\n<li>Slot-1 will now remain\
  \ disabled, if DS game card with IR features isn't detected.\n<ul>\n<li>Fixes bug\
  \ where waking from sleep mode causes the console to power off, when running a ROM\
  \ of a game with IR features.</li>\n</ul>\n</li>\n</ul>\n<p><strong>Known bugs</strong></p>\n\
  <ul>\n<li>Screenshots of ActImagine/MobiClip will still appear blank for a few games\
  \ (ex. Mega Man ZX, Infinite Space).</li>\n<li>(As of v0.46.0) Gen 5 Pok\xE9mon\
  \ Games freeze when taking screenshots and don't advance a frame on R-button press.</li>\n\
  </ul>"
updated: '2021-08-11T07:56:37Z'
version: v0.46.1
version_title: v0.46.1
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.