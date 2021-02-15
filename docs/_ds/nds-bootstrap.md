---
author: DS-Homebrew
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.36.0
downloads:
  nds-bootstrap.7z:
    size: 446338
    size_str: 435 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.36.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1094642
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.36.0/nds-bootstrap.zip
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
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: "<p>Some of you might've heard that the 100th release will bring one\
  \ or all of these features:</p>\n<ol>\n<li>DSi mode, which will allow:\n<ol>\n<li>Booting\
  \ DSi-Enhanced games with DSi features, such as WPA1/2 and camera.</li>\n<li>Booting\
  \ DSiWare games without the need for Unlaunch, or installing the game as a CIA.</li>\n\
  </ol>\n</li>\n<li>Fixed cloneboot support, which will allow multiplayer via Download\
  \ Play to work for the games that currently don't work the feature.</li>\n<li>Slot-2\
  \ emulation for games such as <em>MegaMan ZX</em>, <em>Pok\xE9mon</em> Gen 4, and\
  \ more.</li>\n</ol>\n<p>Unfortunately, due to my failed attempts of implementing\
  \ those (thus lacking the knowledge how to do so), and the devs like <a class=\"\
  user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ahezard/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ahezard\">@ahezard</a> (the main dev) and <a class=\"\
  user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/shutterbug2000/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/shutterbug2000\">@shutterbug2000</a> not being around\
  \ for a while, those features have not been implemented, and this release was solely\
  \ made to bring nds-bootstrap out of the stealth release state, bringing some features\
  \ and fixes that have only been in stealth and nightly builds.</p>\n<p>For a bit\
  \ of news:</p>\n<ol>\n<li>A month ago, shutterbug has began work on DSi mode once\
  \ again, and he plans to commit the changes soon<g-emoji class=\"g-emoji\" alias=\"\
  tm\" fallback-src=\"https://github.githubassets.com/images/icons/emoji/unicode/2122.png\"\
  >\u2122\uFE0F</g-emoji>.</li>\n<li>A while back, ahezard has stated that he will\
  \ return to coding at some point.</li>\n</ol>\n<p>With all that said, it'll be a\
  \ while before we see those features implemented, and even fixing some broken games,\
  \ such as <em>Pok\xE9mon Dash</em> and <em>Golden Sun: Dark Dawn</em>, as well as\
  \ fixing cheat support (some E-type codes don't work).</p>\n<p>Instructions:</p>\n\
  <ol>\n<li>Download the .7z file.</li>\n<li>Extract the nds-bootstrap (or B4DS, for\
  \ DS-mode flashcards) .nds files, to <code>root:/_nds</code>.</li>\n<li>Extract\
  \ the .ver file to <code>root:/_nds/TWiLightMenu</code>.</li>\n</ol>\n<p><strong>Reg</strong>\
  \ = Only for nds-bootstrap for DSi/3DS<br>\n<strong>B4DS</strong> = Only for nds-bootstrap\
  \ for DS flashcards</p>\n<p><strong>What's new?</strong></p>\n<ul>\n<li>Two DSiWare\
  \ games now boot in their DS mode demo versions!\n<ul>\n<li>Pop Island</li>\n<li>Pop\
  \ Island: Paperfield</li>\n</ul>\n</li>\n<li><strong>Reg:</strong> (<a class=\"\
  user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/xonn83/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/xonn83\">@xonn83</a> and me) You can now swap the screens\
  \ by holding L+R+UP+X for 1 second. Useful for consoles with the GameBoy Macro mod.\n\
  <ul>\n<li>Note that this doesn't work for all games (or all areas of the game),\
  \ and some games that do work with this feature, will corrupt some graphics.</li>\n\
  <li>This will also not work with B4DS, due to memory limitations.</li>\n</ul>\n\
  </li>\n<li><strong>Reg:</strong> Added a <code>Hi</code> heap shrink setting.\n\
  <ul>\n<li>Set this, if there's a cheat code not working. If this does not fix it,\
  \ then wait for a fix.</li>\n<li>Set by setting <code>CARDENGINE_CACHED</code> to\
  \ <code>2</code> in <code>nds-bootstrap.ini</code>.</li>\n</ul>\n</li>\n</ul>\n\
  <p><strong>Improvements (Reg)</strong></p>\n<ul>\n<li>ARM7 binary is now stripped\
  \ when pre-loading a ROM into RAM (as it's already loaded).\n<ul>\n<li>This allows\
  \ more 28MB (or 12MB for DSi) ROMs to fit into RAM.</li>\n</ul>\n</li>\n<li>FAT\
  \ table cache is now copied to DSi WRAM, if:\n<ul>\n<li>DSi WRAM is not mirrored\
  \ (DSiWarehax not used, in other words)</li>\n<li>Game is running in DS mode</li>\n\
  <li>Game is on the console's SD card</li>\n</ul>\n</li>\n</ul>\n<p><strong>Bug fixes</strong></p>\n\
  <ul>\n<li><strong>Reg:</strong> Slot-1 is now disabled, in order for sleep mode\
  \ to work with any card inserted in Slot-1!\n<ul>\n<li>Ejecting the Slot-1 card\
  \ will also no longer cause the console to reboot or shut down!</li>\n<li>This does\
  \ not affect IR games such as <em>Pok\xE9mon HGSS</em>, if Slot-1 isn't empty.</li>\n\
  </ul>\n</li>\n<li><strong>Reg:</strong> Fixed sound in <em>Dragon Ball Z: Goku Densetsu</em>\
  \ and some SDK5 THUMB games, if using DSiWarehax (e.g. Memory Pit).</li>\n<li><strong>Reg:</strong>\
  \ Fixed a bug with reading a pre-loaded 28.5MB (or 12.5MB for DSi) ROM from RAM.</li>\n\
  <li>Fix long-standing bug with overlay pack size calculation.</li>\n</ul>\n<p><strong>Regression</strong></p>\n\
  <ul>\n<li>Some games have stopped booting, such as <em>Mario &amp; Sonic at the\
  \ Olympic Winter Games</em>.</li>\n</ul>"
updated: '2021-02-15T07:34:32Z'
version: v0.36.0
version_title: 'v0.36.0: 100th release!'
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.