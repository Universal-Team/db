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
    size: 398061
    size_str: 388 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.51.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 964203
    size_str: 941 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.51.0/nds-bootstrap.zip
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
update_notes: "<p dir=\"auto\"><a target=\"_blank\" rel=\"noopener noreferrer\" href=\"\
  https://github.com/DS-Homebrew/nds-bootstrap/blob/master/screenshots/v0.51.0/DSiWare%20on%20DS%20Phat.png?raw=true\"\
  ><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/blob/master/screenshots/v0.51.0/DSiWare%20on%20DS%20Phat.png?raw=true\"\
  \ alt=\"screenshots\" style=\"max-width: 100%;\"></a></p>\n<p dir=\"auto\">Included\
  \ in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v23.1.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v23.1.0</a></p>\n<p dir=\"auto\"\
  >Instructions:</p>\n<ol dir=\"auto\">\n<li>Download the <code>.7z</code> file.</li>\n\
  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n\
  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p dir=\"auto\"><strong>What's new?</strong></p>\n<ul dir=\"auto\">\n<li><strong>B4DS\
  \ mode:</strong> Support for up to 23 DSiWare titles have been added, making them\
  \ playable on DS/DS lite consoles for the first time ever!<br>\n(For a list of supported\
  \ titles, see this list <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/blob/c174faedd633b40b3e3ffa0368c2c8964e9ef16f/universal/include/incompatibleGameMap.h#L49\"\
  >here</a>.)\n<ul dir=\"auto\">\n<li>GO Series: 10 Second Run</li>\n<li>Ace Mathician</li>\n\
  <li>Art Style: Aquia</li>\n<li>Aura-Aura Climber</li>\n<li>Art Style: BASE 10</li>\n\
  <li>Dairojo! Samurai Defenders</li>\n<li>Dark Void Zero</li>\n<li>Dragon's Lair</li>\n\
  <li>Dragon's Lair II: Time Warp (USA version only)</li>\n<li>DS WiFi Settings</li>\n\
  <li>Famicom Wars DS: Ushinawareta Hikari</li>\n<li>GO Series: Defense Wars</li>\n\
  <li>Game &amp; Watch: Ball</li>\n<li>Game &amp; Watch: Chef</li>\n<li>Game &amp;\
  \ Watch: Donkey Kong Jr.</li>\n<li>Game &amp; Watch: Flagman</li>\n<li>Game &amp;\
  \ Watch: Helmet</li>\n<li>Game &amp; Watch: Judge</li>\n<li>Game &amp; Watch: Manhole</li>\n\
  <li>Game &amp; Watch: Mario's Cement Factory</li>\n<li>Game &amp; Watch: Vermin</li>\n\
  <li>Mighty Flip Champs!</li>\n<li>Space Ace</li>\n<li>(For Debug DS consoles, additional\
  \ support for 6 titles have been added.)\n<ul dir=\"auto\">\n<li>G.G. Series: All\
  \ Breaker</li>\n<li>G.G. Series: Assault Buster</li>\n<li>BlayzBloo: Super Melee\
  \ Brawlers Battle Royale</li>\n<li>Mighty Milky Way</li>\n<li>Nintendo DSi XL Demo\
  \ Video</li>\n<li>Nintendo DSi XL Demo Video: Volume 2</li>\n</ul>\n</li>\n</ul>\n\
  </li>\n<li>Soft-resetting speeds have improved, and no longer reboots the console!\n\
  <ul dir=\"auto\">\n<li>Shiny Pok\xE9mon hunters will find this feature useful, as\
  \ it'll speed up the hunting process!</li>\n</ul>\n</li>\n</ul>\n<p dir=\"auto\"\
  ><strong>Bug fixes</strong></p>\n<ul dir=\"auto\">\n<li>Fixed Banana Cup causing\
  \ a crash in <em>Mario Kart DS</em>.</li>\n<li>(Untested) The Power Washer minigame\
  \ crash in <em>Mario Party DS</em> should now be fixed.</li>\n<li>Fixed <em>Anno\
  \ 1701: Dawn of Discovery</em> not booting on 3DS.</li>\n<li>Fixed <em>Magic School\
  \ Bus: Oceans</em> not booting on 3DS.</li>\n<li><em>Brain Age Express: Sudoku</em>\
  \ no longer shows the <code>Download failed</code> message.</li>\n</ul>\n<p dir=\"\
  auto\"><strong>Known bugs</strong></p>\n<ul dir=\"auto\">\n<li><strong>B4DS mode:</strong>\
  \ None of the supported DSiWare titles (except <em>Famicom Wars DS: Ushinawareta\
  \ Hikari</em>) can save data.</li>\n<li><strong>B4DS mode:</strong> Due to memory\
  \ limitations of retail DS consoles, audio will not play in <em>Art Style: Aquia</em>.</li>\n\
  <li><strong>B4DS mode:</strong> In <em>Aura-Aura Climber</em>, depending on how\
  \ far you go in Endless Mode, the game will crash. Inserting a Memory Expansion\
  \ Pak may prolong how far you can go up before the crash.</li>\n<li><strong>B4DS\
  \ mode:</strong> The <em>Game &amp; Watch</em> DSiWare titles will softlock after\
  \ finishing a game or exiting (usually in Game A mode).</li>\n<li><strong>B4DS mode:</strong>\
  \ Connecting to WiFi in <em>Famicom Wars DS: Ushinawareta Hikari</em> will cause\
  \ the game to crash.</li>\n<li>Soft-resetting may not work properly in a few games,\
  \ causing a crash as a result.</li>\n</ul>"
updated: '2021-11-26T02:36:36Z'
version: v0.51.0
version_title: Thanksgiving release (2021)
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.