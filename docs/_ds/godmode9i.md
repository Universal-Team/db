---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
- save-tool
color: '#be8345'
color_bg: '#80582e'
created: '2018-10-02T16:59:38Z'
description: 'GodMode9i Explorer - A full access file browser for the Nintendo DS
  and DSi consoles :godmode:'
download_page: https://github.com/DS-Homebrew/GodMode9i/releases
downloads:
  GodMode9i.7z:
    size: 345769
    size_str: 337 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.0/GodMode9i.7z
  GodMode9i.cia:
    size: 947456
    size_str: 925 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.0/GodMode9i.cia
  GodMode9i.dsi:
    size: 932864
    size_str: 911 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.0/GodMode9i.dsi
  GodMode9i.nds:
    size: 932864
    size_str: 911 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.0/GodMode9i.nds
github: DS-Homebrew/GodMode9i
icon: https://db.universal-team.net/assets/images/icons/godmode9i.png
image: https://raw.githubusercontent.com/DS-Homebrew/GodMode9i/master/resources/logo2.png
image_length: 44248
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds/blob/master/extras/GodMode9i.7z
  downloads:
    GodMode9i.7z:
      url: https://github.com/TWLBot/Builds/raw/master/extras/GodMode9i.7z
qr:
  GodMode9i.cia: https://db.universal-team.net/assets/images/qr/godmode9i-cia.png
  GodMode9i.dsi: https://db.universal-team.net/assets/images/qr/godmode9i-dsi.png
  GodMode9i.nds: https://db.universal-team.net/assets/images/qr/godmode9i-nds.png
source: https://github.com/DS-Homebrew/GodMode9i
systems:
- DS
title: GodMode9i
update_notes: '<p dir="auto">All changes by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a></p>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Updated to match GodMode9''s new font (<a href="https://github.com/DS-Homebrew/GodMode9i/issues/219"
  data-hovercard-type="pull_request" data-hovercard-url="/DS-Homebrew/GodMode9i/pull/219/hovercard">#219</a>).</li>

  <li>Made GBA RTC dumping optional.</li>

  <li>Made <code class="notranslate">X</code> button clear string in keyboard.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Only dump the RSA key on trimmed DS(i) ROMs when it exists. (Thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/bWFpbA/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/bWFpbA">@bWFpbA</a>)</li>

  <li>Fixed dumping EEPROM registers in 32 MB GBA ROMs.</li>

  </ul>'
updated: '2024-01-01T23:11:05Z'
version: v3.5.0
version_title: 'v3.5.0: New Years release'
website: https://wiki.ds-homebrew.com/godmode9i/
wiki: https://wiki.ds-homebrew.com/other/godmode9i
---
### Installation:
- TWiLight Menu++: Use either the `GodMode9i.nds` or `GodMode9i.dsi` file, they function identically with TWiLight Menu++
   - The only difference is that `GodMode9i.dsi` has a Title ID
- Flashcard: Use the `GodMode9i.nds` file
- hiyaCFW SDNAND: Install the `GodMode9i.dsi` file with [NTM](/ds/NTM)
- 3DS HOME Menu: Install the `GodMode9i.cia` file with [FBI](/3ds/fbi)

### Features:
- Dump GameBoy Advance cartridges on the original Nintendo DS and Nintendo DS Lite consoles.
- Dump Nintendo DS/DSi cartridges on Nintendo DSi and Nintendo 3DS consoles (if GodMode9i is ran on the console SD card).
- Copy, move, delete, rename files/folders and create folders.
- Mount the NitroFS of .nds files.
- Browse files on supported flashcards when running GM9i from the NAND or SD Card. (`AceKard 2(i)` & `R4 Ultra (r4ultra.com)`)