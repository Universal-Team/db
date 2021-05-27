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
icon: https://raw.githubusercontent.com/Epicpkmn11/NitroHax3DS/master/icon.bmp
image: https://db.universal-team.net/assets/images/images/nitrohax3ds-usrcheat.dat.png
image_length: 354
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  NitroHax-usrcheat.cia: https://db.universal-team.net/assets/images/qr/nitrohax-usrcheat.cia.png
source: https://github.com/Epicpkmn11/NitroHax3DS
systems:
- DS
title: NitroHax3DS (usrcheat.dat)
update_notes: '<p>This is a fork of NitroHax3DS that loads cheats from a <code>usrcheat.dat</code>
  file instead of <code>cheats.xml</code>. If you want to use a cheats.xml, then use
  <a href="https://github.com/ahezard/NitroHax3DS/releases">ahezard/NitroHax3DS</a>.</p>

  <p>Cheats will be loaded from the following files in this order:</p>

  <ul>

  <li><code>usrcheat.dat</code> (in the current directory)</li>

  <li><code>/DS/NitroHax/usrcheat.dat</code></li>

  <li><code>/NitroHax/usrcheat.dat</code></li>

  <li><code>/data/NitroHax/usrcheat.dat</code></li>

  <li><code>/usrcheat.dat</code></li>

  <li><code>/_nds/usrcheat.dat</code></li>

  <li><code>/_nds/TWiLightMenu/extras/usrcheat.dat</code> (this is the same place
  TWiLight Menu++ uses)</li>

  </ul>

  <p>If you don''t have a cheat database, I recommend using <a href="https://gbatemp.net/threads/deadskullzjrs-nds-cheat-databases.488711/"
  rel="nofollow">DeadSkullzJr''s</a>.</p>

  <p>Use <code>NitroHax-usrcheat.cia</code> to install to the 3DS home menu.<br>

  Use <code>NitroHax.dsi</code> with TWiLight Menu++ or with <a href="https://github.com/JeffRuLz/TMFH/releases">TMFH</a>
  to install to hiyaCFW''s SDNAND.</p>

  <p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/0b07e9088ed15399c468ed8566f9128e64ff6885f439eb1613b547afb123dc02/68747470733a2f2f64622e756e6976657273616c2d7465616d2e6e65742f6173736574732f696d616765732f71722f6e6974726f6861782d75737263686561742e6369612e706e67"><img
  src="https://camo.githubusercontent.com/0b07e9088ed15399c468ed8566f9128e64ff6885f439eb1613b547afb123dc02/68747470733a2f2f64622e756e6976657273616c2d7465616d2e6e65742f6173736574732f696d616765732f71722f6e6974726f6861782d75737263686561742e6369612e706e67"
  alt="QR code for the CIA" data-canonical-src="https://db.universal-team.net/assets/images/qr/nitrohax-usrcheat.cia.png"
  style="max-width:100%;"></a></p>'
updated: '2021-01-11T07:44:59Z'
version: '0.100'
version_title: Load cheats from usrcheat.dat instead of cheats.xml
---
This is a fork of [ahezard/NitroHax3DS](nitrohax3ds) that switches the cheat database format to `usrcheat.dat`. If you want to use `cheats.xml`, then use the original.