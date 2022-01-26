---
author: Pk11
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- utility
color: '#81de8e'
created: '2022-01-09T06:28:39Z'
description: NAND Title Manager for DSi
download_page: https://github.com/Epicpkmn11/NTM/releases
downloads:
  NTM.dsi:
    size: 253440
    size_str: 247 KiB
    url: https://github.com/Epicpkmn11/NTM/releases/download/v0.1.0/NTM.dsi
github: Epicpkmn11/NTM
icon: https://db.universal-team.net/assets/images/icons/ntm.png
icon_index: 199
image: https://db.universal-team.net/assets/images/icons/ntm.png
image_length: 586
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/Epicpkmn11/NTM
systems:
- DS
title: NTM
unistore_exclude: true
update_notes: '<blockquote>

  <p dir="auto">Please see <a href="https://github.com/Epicpkmn11/NTM/wiki">the wiki</a>
  for information on how to use NTM.</p>

  </blockquote>

  <p dir="auto">As this is the first release of NTM and it''s a fork of TMFH, this
  is a changelog from <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/JeffRuLz/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/JeffRuLz">@JeffRuLz</a>''s
  TMFH <a href="https://github.com/JeffRuLz/TMFH/releases/tag/v0.7.0">v0.7.0</a>.</p>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Added SysNAND title management

  <ul dir="auto">

  <li>Many safety features have been implemented, however this has potential to be
  <strong>dangerous</strong>, please use with caution</li>

  <li>Thanks to <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/DesperateProgrammer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DesperateProgrammer">@DesperateProgrammer</a>
  for the correct NAND writing code from <a href="https://github.com/DesperateProgrammer/DSiLanguagePacher">DSi
  Language Patcher</a></li>

  </ul>

  </li>

  <li>Save files and legit TMD files can now be installed alongside their app file</li>

  <li>A ticket will now be created if a legit TMD is given allowing apps to be used
  without RSA patches</li>

  <li>File lists are now sorted alphabetically</li>

  <li>ROM size is now shown in blocks in addition to bytes</li>

  <li>Added an option to fix a "mismatch in FAT copies" error</li>

  <li>Titles can now have their files marked as read-only to prevent the DSi Menu
  from automatically deleting them</li>

  </ul>

  <h3 dir="auto">Changes</h3>

  <ul dir="auto">

  <li>Renamed to NAND Title Manager, or NTM for short</li>

  <li>Icon recolored to green to look distinct from TMFH, feel free to PR if anyone
  has better icon ideas</li>

  <li>Files starting with <code>.</code> are no longer shown in the file list</li>

  <li>Options to override the space and icon limits have been removed</li>

  <li>File related errors are now shown before asking if you''re sure you want to
  install</li>

  <li>Backups have been reworked so that they dump to <code>.nds</code>, <code>.tmd</code>,
  <code>.pub</code>, <code>.prv</code>, and <code>.bnr</code> files instead of copying
  the folder directly from NAND</li>

  <li>"Shut Down" menu option was renamed to "Exit"</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed some issues in the free space calculation that could result in overinstalling
  by a few kilobytes

  <ul dir="auto">

  <li>This has not been thoroughly tested in SDNAND mode so it may still need tweaking
  there, in SysNAND mode it shouldn''t be possible to overflow (though I don''t recommend
  stress testing it)</li>

  </ul>

  </li>

  <li>Fixed the DSi header check to use the CRC16 instead of comparing the title ID
  as the title ID can differ</li>

  </ul>'
updated: '2022-01-16T01:49:25Z'
version: v0.1.0
version_title: Initial release
wiki: https://github.com/Epicpkmn11/NTM/wiki
---
NAND Title Manager, NTM for short, is an application for the Nintendo DSi that allows you to manage titles on your NAND. It can manage titles on both [hiyaCFW](https://wiki.ds-homebrew.com/hiyacfw/)'s SDNAND and your actual internal memory, typically called SysNAND. **When using in SysNAND mode please use with caution**.