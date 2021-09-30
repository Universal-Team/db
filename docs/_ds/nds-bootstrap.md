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
    size: 381708
    size_str: 372 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.48.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 924569
    size_str: 902 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.48.0/nds-bootstrap.zip
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
update_notes: "<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v22.0.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v22.0.0</a></p>\n<p>Instructions:</p>\n\
  <ol>\n<li>Download the <code>.7z</code> file.</li>\n<li>Extract the nds-bootstrap\
  \ <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n<li><strong>TWLMenu++\
  \ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p><strong>NOTE:</strong> The .ini settings listed below can be set using\
  \ <strong>TW</strong>i<strong>L</strong>ight Menu++, if installed.</p>\n<p><strong>What's\
  \ new?</strong></p>\n<ul>\n<li>When starting a DSi-Enhanced game in DSi mode in\
  \ DSiWarehax, a DSi-Exclusive/DSiWare title set as a donor ROM (.ini setting: <code>DONOR_TWLONLY_PATH</code>)\
  \ will now be used in order for the game to boot!</li>\n<li>When starting a DSi-Exclusive/DSiWare\
  \ game from a CycloDS iEvolution running in DSi mode, a DSi-Enhanced game set as\
  \ a donor ROM (.ini setting: <code>DONOR_TWL_PATH</code>) will now be used in order\
  \ for the game to boot!\n<ul>\n<li>Please note that DSiWare will run the same as\
  \ when support for it first got added in nds-bootstrap, so saving will not work,\
  \ except in the DSiWare version of <em>Advance Wars: Days of Ruin</em>.</li>\n</ul>\n\
  </li>\n<li>DSiWare now boots in DSiWarehax (without Unlaunch, in other words)!\n\
  <ul>\n<li>If using Memory Pit, some titles may not work or will crash later on.\
  \ The TWLMenu++ version listed above contains a list of incompatible DSiWare for\
  \ Memory Pit, and will prevent launching, if incompatible title is found.</li>\n\
  </ul>\n</li>\n<li>A new MPU configuration is now in use for DS mode, and is the\
  \ same one used in DSi mode!</li>\n<li>SWI Halt hooking can now be disabled! (.ini\
  \ setting: <code>SWI_HALT_HOOK</code>).\n<ul>\n<li>Disabling will fix slowdown that\
  \ occur in some games, such as <em>Mario Kart DS</em>, <em>Sonic Rush</em>, and\
  \ more.</li>\n</ul>\n</li>\n<li>If a ROM gets pre-loaded to RAM, the unpatched ARM9\
  \ and ARM7 binaries will now be placed in the DS debug RAM area, in order for more\
  \ of the ROM data to be loaded.</li>\n<li>The in-game menu is now accessible in\
  \ B4DS mode!</li>\n<li>When booting a game in DSi mode from a CycloDS iEvolution,\
  \ the TWLCFG is reconstructed, as the flashcard clears it from RAM when it's menu\
  \ opens.</li>\n</ul>\n<p><strong>Improvements</strong></p>\n<ul>\n<li><strong>3DS/2DS:</strong>\
  \ For SDK1-4 games, the last 24MB of RAM is now used again for card data cache.</li>\n\
  <li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated in-game menu translations.</li>\n<li>Other minor improvements.</li>\n\
  </ul>\n<p><strong>Bug fixes</strong></p>\n<ul>\n<li>The RTC glitches that occur\
  \ on DSi are finally fixed!\n<ul>\n<li>No need to hear the bell over and over in\
  \ <em>Animal Crossing: Wild World</em>!</li>\n<li><em>Face Training</em> can now\
  \ be played properly.</li>\n<li>The quick day/night swap and the crashes will no\
  \ longer occur in the Gen 4 <em>Pok\xE9mon</em> games!</li>\n</ul>\n</li>\n<li>(<a\
  \ class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/Epicpkmn11/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a>) Fixed bugged pixels appearing\
  \ in DSi mode screenshots.</li>\n<li>Fixed some DSi mode games not running from\
  \ a flashcard on 3DS.</li>\n<li>Forced DSi mode now works again!</li>\n<li>Fixed\
  \ broken sound in some games running in DSiWarehax or forced DSi mode.</li>\n<li>Fixed\
  \ SDK5 games loaded into RAM rebooting the console when trying to open in-game menu.</li>\n\
  <li>Fixed flashcard games running in DSi mode rebooting the console when trying\
  \ to open in-game menu.</li>\n<li>Fixed games not starting if EZ-Flash 3-in-1 is\
  \ inserted.</li>\n<li>Other minor fixes.</li>\n</ul>\n<p><strong>Known bugs</strong></p>\n\
  <ul>\n<li>Due to the new MPU configuration, a few SDK2 games may not work. The few\
  \ that didn't work such as <em>Trauma Center: Under the Knife</em> and <em>Lost\
  \ in Blue</em> have already been fixed.</li>\n<li>The B4DS in-game menu will not\
  \ work in some games.</li>\n</ul>"
updated: '2021-09-29T05:07:10Z'
version: v0.48.0
version_title: v0.48.0
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.