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
    size: 383310
    size_str: 374 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.49.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 925697
    size_str: 904 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.49.0/nds-bootstrap.zip
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
update_notes: "<p>Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v22.1.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v22.1.0</a></p>\n<p>Instructions:</p>\n\
  <ol>\n<li>Download the <code>.7z</code> file.</li>\n<li>Extract the nds-bootstrap\
  \ <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n<li><strong>TWLMenu++\
  \ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p><strong>What's new?</strong></p>\n<ul>\n<li>Another DSiWare title, <em>Glory\
  \ Days: Tactical Defense</em> (from the devs who made <em>Pop Island</em> and <em>Pop\
  \ Island: Paperfield</em>), is now playable on original/lite DS models!\n<ul>\n\
  <li>To play it, a DSi-Enhanced ROM needs to be set as a Donor ROM.</li>\n</ul>\n\
  </li>\n</ul>\n<p><strong>Improvements</strong></p>\n<ul>\n<li>Replaced CycloDSi\
  \ check with an arm7 MBK check, should there be any more future DSi mode flashcards.</li>\n\
  <li>(<a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Epicpkmn11/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Epicpkmn11\">@Epicpkmn11</a> and various)\
  \ Updated in-game menu translations.</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n\
  <ul>\n<li>Fixed DSi mode WiFi only working on regular DSi models, if using a DSiWare\
  \ exploit containing MiniTWLPayload (ex. Memory Pit, Flipnote Lenny), or a CycloDS\
  \ iEvolution flashcard, so DSi mode WiFi will now work on all DSi and 3DS models!\n\
  <ul>\n<li>(In case you're wondering, this does not make DSi mode WiFi work in original\
  \ DS/NTR games.)</li>\n</ul>\n</li>\n<li>The sprite glitch + crash bug should now\
  \ be fixed in <em>Pok\xE9mon HeartGold &amp; SoulSilver Versions</em>!</li>\n<li>Fixed\
  \ <em>WarioWare DIY</em> not booting on 3DS in DS mode.</li>\n<li>Fixed AP-patching\
  \ not working properly for ROMs pre-loaded into RAM.</li>\n<li>(Untested!) Fixed\
  \ soft-resetting for forwarders in hiyaCFW.</li>\n<li>Fixed nds-bootstrap logo always\
  \ showing in B4DS mode, if the patch offsets for set ROM are already cached.</li>\n\
  </ul>"
updated: '2021-10-05T22:36:03Z'
version: v0.49.0
version_title: v0.49.0
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.