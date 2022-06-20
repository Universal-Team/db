---
author: Pk11
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- utility
color: '#81de8e'
color_bg: '#4a8052'
created: '2022-01-09T06:28:39Z'
description: NAND Title Manager for DSi
download_page: https://github.com/Epicpkmn11/NTM/releases
downloads:
  NTM.dsi:
    size: 256512
    size_str: 250 KiB
    url: https://github.com/Epicpkmn11/NTM/releases/download/v0.1.5/NTM.dsi
github: Epicpkmn11/NTM
icon: https://db.universal-team.net/assets/images/icons/ntm.png
icon_index: 199
image: https://db.universal-team.net/assets/images/icons/ntm.png
image_length: 586
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  NTM.dsi: https://db.universal-team.net/assets/images/qr/ntm-dsi.png
source: https://github.com/Epicpkmn11/NTM
systems:
- DS
title: NTM
unistore_exclude: true
update_notes: '<table role="table">

  <thead>

  <tr>

  <th align="left"><g-emoji class="g-emoji" alias="exclamation" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2757.png">❗</g-emoji>
  Please see <a href="https://github.com/Epicpkmn11/NTM/wiki">the wiki</a> for information
  on how to use NTM.</th>

  </tr>

  </thead>

  </table>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Adds an option to the main menu to enable Data Management in System Settings

  <ul dir="auto">

  <li>This is done by simply creating an empty file for <code class="notranslate">/sys/dev.kp</code>,
  which causes Data Management to show up</li>

  <li>This could potentially interfere with usage of the DSi Shop, though I think
  the shop would just replace it with with a proper one, but as the shop is dead there''s
  not really any worry</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Changes the free space check to always leave at least 1 MiB free, hopefully
  this is enough margin for error as to prevent any more bricks, like the one reported
  by <a href="https://gbatemp.net/members/thesegakid.550754/" rel="nofollow">TheSegaKid</a>
  on GBAtemp

  <ul dir="auto">

  <li>I wish I knew exactly why that happened as I tested, using no$gba, down to the
  exact byte that my space calculations matched up iirc, but it''s likely I missed
  something and since I was allowing such tight margins that allowed it to mess up</li>

  <li>This shouldn''t be a major concern for users with Unlaunch, but especially if
  you don''t have Unlaunch I strongly recommend updating</li>

  </ul>

  </li>

  </ul>'
updated: '2022-06-20T23:00:04Z'
version: v0.1.5
version_title: Data Management enabled and improved safety
wiki: https://github.com/Epicpkmn11/NTM/wiki
---
NAND Title Manager, NTM for short, is an application for the Nintendo DSi that allows you to manage titles on your NAND. It can manage titles on both [hiyaCFW](https://wiki.ds-homebrew.com/hiyacfw/)'s SDNAND and your actual internal memory, typically called SysNAND. **When using in SysNAND mode please use with caution**.