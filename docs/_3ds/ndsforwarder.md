---
author: MechanicalDragon
avatar: https://avatars.githubusercontent.com/u/43786828?v=4
categories:
- utility
color: '#82c3d7'
color_bg: '#4d7480'
created: '2021-04-12T08:12:05Z'
description: Generate and Install NDS Forwarders
download_page: https://github.com/MechanicalDragon0687/NDSForwarder/releases
downloads:
  ndsForwarder.3dsx:
    size: 1025260
    size_str: 1001 KiB
    url: https://github.com/MechanicalDragon0687/ndsForwarder/releases/download/1.4.3/ndsForwarder.3dsx
github: MechanicalDragon0687/NDSForwarder
icon_index: 173
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

  <li>Be sure to copy the <code class="notranslate">_nds</code> folder from the <code
  class="notranslate">for SD card root</code> folder to the sd card.</li>

  </ul>

  <h2 dir="auto">Features</h2>

  <ul dir="auto">

  <li>Custom dsiware banners! They must be named the same as the nds file. If your
  nds file is <code class="notranslate">Jamal''s Home Cooking.nds</code> your custom
  banner should be <code class="notranslate">Jamal''s Home Cooking.bin</code>.  Custom
  banners can be located with the nds file or in <code class="notranslate">/3ds/forwarder/banners/</code></li>

  <li>Custom Icons! They must be 4bit bmps and be named the same as the nds file.
  If your nds file is <code class="notranslate">Jamal''s Home Cooking.nds</code> your
  custom icon should be <code class="notranslate">Jamal''s Home Cooking.bmp</code>.  Custom
  icons can be located with the nds file or in <code class="notranslate">/3ds/forwarder/icons/</code></li>

  <li>Auto Random TID.  This allows separate forwarders for romhacks that dont change
  TIDs</li>

  <li>Custom Title. If you dont have a custom banner, or want one but need a different
  Title, check the box!</li>

  <li>Install all in folder. You can install forwarders for all nds files in any given
  folder</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <p dir="auto">1.4.3<br>

  remove rom type checking to allow dsiware installation</p>

  <p dir="auto">1.4.2<br>

  fix the problem with nds file loading introduced in 1.4.1</p>

  <p dir="auto">1.4.1<br>

  Actually fixed the CRC checking issues</p>'
updated: '2022-05-04T03:07:07Z'
version: 1.4.3
version_title: 1.4.3
---
### Installing
1. Download the [3DS SD card forwarder pack](https://github.com/RocketRobz/NTR_Forwarder/releases/latest/download/DS.Game.Forwarder.pack.DSi.3DS.SD.Card.7z)
1. Extract the contents of the `for SD card root` folder to the root of your SD card
1. Download [TWiLight Menu++'s apfix.pck](https://raw.githubusercontent.com/TWLBot/Builds/master/extras/apfix.pck)
1. Copy `apfix.pck` to `sdmc:/_nds/ntr-forwarder/apfix.pck` on your SD card

When installing with Universal-Updater this is done automatically.