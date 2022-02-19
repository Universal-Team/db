---
author: MechanicalDragon
avatar: https://avatars.githubusercontent.com/u/43786828?v=4
categories:
- utility
color: '#82c3d7'
created: '2021-04-12T08:12:05Z'
description: Generate and Install NDS Forwarders
download_page: https://github.com/MechanicalDragon0687/NDSForwarder/releases
downloads:
  ndsForwarder.3dsx:
    size: 1024560
    size_str: 1000 KiB
    url: https://github.com/MechanicalDragon0687/ndsForwarder/releases/download/1.4.0/ndsForwarder.3dsx
github: MechanicalDragon0687/NDSForwarder
icon_index: 174
image: https://avatars.githubusercontent.com/u/43786828?v=4
image_length: 30859
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/MechanicalDragon0687/ndsForwarder
systems:
- 3DS
title: ndsForwarder
update_notes: '<p dir="auto">Requires full CFW via Rosalina (b9s+luma3ds)</p>

  <h2 dir="auto">Usage</h2>

  <p dir="auto">Put in /3ds/<br>

  Open with homebrew launcher</p>

  <ul dir="auto">

  <li>note: you also need the nds-bootstrap forwarder pack from <a href="https://github.com/RocketRobz/NTR_Forwarder/releases">here</a>.</li>

  <li>Be sure to copy the <code>_nds</code> folder from the <code>for SD card root</code>
  folder to the sd card.</li>

  </ul>

  <h2 dir="auto">Features</h2>

  <ul dir="auto">

  <li>Custom dsiware banners! They must be named the same as the nds file. If your
  nds file is <code>Jamal''s Home Cooking.nds</code> your custom banner should be
  <code>Jamal''s Home Cooking.bin</code>.  Custom banners can be located with the
  nds file or in <code>/3ds/forwarder/banners/</code></li>

  <li>Custom Icons! They must be 4bit bmps and be named the same as the nds file.
  If your nds file is <code>Jamal''s Home Cooking.nds</code> your custom icon should
  be <code>Jamal''s Home Cooking.bmp</code>.  Custom icons can be located with the
  nds file or in <code>/3ds/forwarder/icons/</code></li>

  <li>Auto Random TID.  This allows separate forwarders for romhacks that dont change
  TIDs</li>

  <li>Custom Title. If you dont have a custom banner, or want one but need a different
  Title, check the box!</li>

  <li>Install all in folder. You can install forwarders for all nds files in any given
  folder</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <p dir="auto">1.4.0</p>

  <ul dir="auto">

  <li>Support srl extension</li>

  <li>block dsiware and system apps</li>

  <li>add crc checks to header and banners</li>

  <li>support ids extension</li>

  <li>support widescreen (thanks hansol). note: you will have to remake your forwarders
  for this to work.</li>

  <li>Fix unicode title support (thanks pks11)</li>

  </ul>

  <p dir="auto">1.3.0-beta<br>

  I dont even remember anymore....</p>

  <p dir="auto">1.2.0-beta</p>

  <ul dir="auto">

  <li>Supports BMP files for custom icons

  <ul dir="auto">

  <li>4 bit</li>

  <li>32x32 pixels</li>

  <li>No Colorspace info (Compatibility options when exporting in GIMP)</li>

  <li>color at index 0 will be transparent/white. You have been warned.</li>

  </ul>

  </li>

  </ul>

  <p dir="auto">1.1.0-beta</p>

  <ul dir="auto">

  <li>Warns user when reaching the limit of dsiware installed</li>

  <li>No longer brown, now blue</li>

  <li>Version is displayed on the bottom screen</li>

  <li>_nds folder is hidden</li>

  <li>if more than one template exists, can select which template to use</li>

  </ul>'
updated: '2022-02-18T22:11:23Z'
version: 1.4.0
version_title: 1.4.0
---
### Installing
1. Download the [3DS SD card forwarder pack](https://github.com/RocketRobz/NTR_Forwarder/releases/latest/download/DS.Game.Forwarder.pack.DSi.3DS.SD.Card.7z)
1. Extract the contents of the `for SD card root` folder to the root of your SD card
1. Download [TWiLight Menu++'s apfix.pck](https://raw.githubusercontent.com/TWLBot/Builds/master/extras/apfix.pck)
1. Copy `apfix.pck` to `sdmc:/_nds/ntr-forwarder/apfix.pck` on your SD card

When installing with Universal-Updater this is done automatically.