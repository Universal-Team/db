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
    size: 257024
    size_str: 251 KiB
    url: https://github.com/Epicpkmn11/NTM/releases/download/v0.1.6/NTM.dsi
github: Epicpkmn11/NTM
icon: https://db.universal-team.net/assets/images/icons/ntm.png
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

  <li>Now checks if Unlaunch''s launcher patches are enabled and doesn''t warn about
  TMDs if they are</li>

  <li>Adds an option to remove a region patched DSi Menu file (<code class="notranslate">sd:/Launcher.dsi</code>)</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixes failing to work with dev apps where the app version is over <code class="notranslate">000000ff</code></li>

  <li>Fixes a null pointer dereference that was sometimes making NTM crash on load</li>

  <li>Fixes a typo in the NAND write warning message</li>

  </ul>'
updated: '2022-11-09T03:12:49Z'
version: v0.1.6
version_title: Bug fixes and minor improvements
wiki: https://github.com/Epicpkmn11/NTM/wiki
---
NAND Title Manager, NTM for short, is an application for the Nintendo DSi that allows you to manage titles on your NAND. It can manage titles on both [hiyaCFW](https://wiki.ds-homebrew.com/hiyacfw/)'s SDNAND and your actual internal memory, typically called SysNAND. **When using in SysNAND mode please use with caution**.

Please see the [guide on the wiki](https://github.com/Epicpkmn11/NTM/wiki/How-to-Install-DSiWare) for how to properly and safely use NTM.