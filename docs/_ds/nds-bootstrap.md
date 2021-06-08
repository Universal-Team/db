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
    size: 363214
    size_str: 354 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.42.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 883630
    size_str: 862 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.42.0/nds-bootstrap.zip
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

  <p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v20.4.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v20.4.0</a></p>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li><strong>B4DS mode:</strong> ROMs up to 8MB can now be loaded into the DS Memory
  Expansion Pak for faster loading!

  <ul>

  <li>If an M3, G6, or SuperCard GBA flashcard containing 32MB of RAM is detected,
  then the ROM size limit is 32MB.

  <ul>

  <li>You''ll need to launch the DS ROM via TWLMenu++ for this feature to work.</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><strong>B4DS mode:</strong> You can now press SELECT+Down to lower sound volume
  range to half. Press SELECT+Up to revert back to normal.</li>

  <li>You can now have DSiWare read TWLNAND contents (or just <code>photo</code> folder)
  from the SD card.</li>

  <li>Pre-set default settings are now implemented, if some aren''t detected in <code>sd:/_nds/nds-bootstrap.ini</code>.</li>

  </ul>

  <p><strong>Improvement</strong></p>

  <ul>

  <li>The main arm9 code (first run when nds-bootstrap is booted by .nds loaders)
  has been recompiled as ARM code instead of THUMB, so boot speed should be improved
  a bit.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>By correcting and adding the remaining device list entries, DSiWare titles that
  read photos taken by the DSi or 3DS camera will now work properly (ex. <em>Hidden
  Photo</em> (DSiWare version), <em>Sparkle Snapshots</em>, etc.).</li>

  <li>Fixed nds-bootstrap exiting out, if running from a Slot-2 flashcard.</li>

  <li>Fixed local WiFi being locked to 0 bars, so local multiplayer now works again.

  <ul>

  <li>As a result, WiFi should no longer crash the game or cause an error, if running
  on DSi without Unlaunch.</li>

  <li>Once again, this does not mean that cloneboot support is fixed. When it eventually
  does get fixed, it''ll be stated in the changelog.</li>

  </ul>

  </li>

  </ul>

  <p><strong>Bug fix &amp; Regression</strong></p>

  <ul>

  <li>The top &amp; bottom main screen options no longer work properly, with the game
  once again changing where the main screen is set.

  <ul>

  <li>This is done to hopefully fix unexpected issues (such as corrupt graphics and/or
  random freezes) when running DSi-Enhanced games in DSi mode.</li>

  </ul>

  </li>

  </ul>'
updated: '2021-06-08T02:40:21Z'
version: v0.42.0
version_title: v0.42.0
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.