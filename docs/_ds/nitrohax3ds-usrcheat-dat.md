---
author: Pk11
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- utility
color: '#750000'
created: '2019-10-17T22:38:27Z'
description: NitroHax cheat tool for Nintendo DS games, ported to Nintendo DSi / 3DS
  and modified to load from a usrcheat.dat database
download_page: https://github.com/Epicpkmn11/NitroHax3DS/releases
downloads:
  NitroHax-usrcheat.cia:
    size: 1368320
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/NitroHax3DS/releases/download/0.100/NitroHax-usrcheat.cia
  NitroHax.dsi:
    size: 1353728
    size_str: 1 MiB
    url: https://github.com/Epicpkmn11/NitroHax3DS/releases/download/0.100/NitroHax.dsi
github: Epicpkmn11/NitroHax3DS
icon: https://db.universal-team.net/assets/images/icons/nitrohax3ds-usrcheat-dat.png
icon_index: 26
image: https://db.universal-team.net/assets/images/icons/nitrohax3ds-usrcheat-dat.png
image_length: 630
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  NitroHax-usrcheat.cia: https://db.universal-team.net/assets/images/qr/nitrohax-usrcheat-cia.png
source: https://github.com/Epicpkmn11/NitroHax3DS
systems:
- DS
title: NitroHax3DS (usrcheat.dat)
update_notes: '<p dir="auto">This is a fork of NitroHax3DS that loads cheats from
  a <code>usrcheat.dat</code> file instead of <code>cheats.xml</code>. If you want
  to use a cheats.xml, then use <a href="https://github.com/ahezard/NitroHax3DS/releases">ahezard/NitroHax3DS</a>.</p>

  <p dir="auto">Cheats will be loaded from the following files in this order:</p>

  <ul dir="auto">

  <li><code>usrcheat.dat</code> (in the current directory)</li>

  <li><code>/DS/NitroHax/usrcheat.dat</code></li>

  <li><code>/NitroHax/usrcheat.dat</code></li>

  <li><code>/data/NitroHax/usrcheat.dat</code></li>

  <li><code>/usrcheat.dat</code></li>

  <li><code>/_nds/usrcheat.dat</code></li>

  <li><code>/_nds/TWiLightMenu/extras/usrcheat.dat</code> (this is the same place
  TWiLight Menu++ uses)</li>

  </ul>

  <p dir="auto">If you don''t have a cheat database, I recommend using <a href="https://gbatemp.net/threads/deadskullzjrs-nds-cheat-databases.488711/"
  rel="nofollow">DeadSkullzJr''s</a>.</p>

  <p dir="auto">Use <code>NitroHax-usrcheat.cia</code> to install to the 3DS home
  menu.<br>

  Use <code>NitroHax.dsi</code> with TWiLight Menu++ or with <a href="https://github.com/JeffRuLz/TMFH/releases">TMFH</a>
  to install to hiyaCFW''s SDNAND.</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/633446f3c15b624cda625813b2f305338e7b85dc68712da43c79d9f8cc8d4ec9/68747470733a2f2f64622e756e6976657273616c2d7465616d2e6e65742f6173736574732f696d616765732f71722f6e6974726f6861782d75737263686561742d6369612e706e67"><img
  src="https://camo.githubusercontent.com/633446f3c15b624cda625813b2f305338e7b85dc68712da43c79d9f8cc8d4ec9/68747470733a2f2f64622e756e6976657273616c2d7465616d2e6e65742f6173736574732f696d616765732f71722f6e6974726f6861782d75737263686561742d6369612e706e67"
  alt="QR code for the CIA" data-canonical-src="https://db.universal-team.net/assets/images/qr/nitrohax-usrcheat-cia.png"
  style="max-width: 100%;"></a></p>'
updated: '2021-01-11T07:44:59Z'
version: '0.100'
version_title: Load cheats from usrcheat.dat instead of cheats.xml
---
This is for use on DSi/3DS from internal SD, if using a flashcard see [NitroHax](nitrohax). This fork uses a `usrcheat.dat` database, see [the original](nitrohax3ds) to use a `cheats.xml` database.

If using on DSi make sure you have [Unlaunch installed](https://dsi.cfw.guide/installing-unlaunch.html)