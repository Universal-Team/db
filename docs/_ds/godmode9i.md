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
    size: 364458
    size_str: 355 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.7.0/GodMode9i.7z
  GodMode9i.cia:
    size: 987904
    size_str: 964 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.7.0/GodMode9i.cia
  GodMode9i.dsi:
    size: 973312
    size_str: 950 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.7.0/GodMode9i.dsi
  GodMode9i.nds:
    size: 973312
    size_str: 950 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.7.0/GodMode9i.nds
github: DS-Homebrew/GodMode9i
icon: https://db.universal-team.net/assets/images/icons/godmode9i.png
image: https://raw.githubusercontent.com/DS-Homebrew/GodMode9i/master/resources/logo2.png
image_length: 44248
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  GodMode9i.cia: https://db.universal-team.net/assets/images/qr/godmode9i-cia.png
  GodMode9i.dsi: https://db.universal-team.net/assets/images/qr/godmode9i-dsi.png
  GodMode9i.nds: https://db.universal-team.net/assets/images/qr/godmode9i-nds.png
source: https://github.com/DS-Homebrew/GodMode9i
stars: 520
systems:
- DS
title: GodMode9i
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Expanded DLDI driver space to 32KB by using libnds32 (by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/lifehackerhansol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/lifehackerhansol">@lifehackerhansol</a>)!</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ApacheThunder/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ApacheThunder">@ApacheThunder</a>:
  Added support for mounting the N-Card and original R4 DLDI drivers when launched
  from DSi/3DS NAND or SD card!</li>

  <li>Added workaround to make homebrew only supporting up to 16KB DLDI drivers, now
  working with 32KB DLDI drivers!

  <ul dir="auto">

  <li>Has not been tested with homebrew built with libnds v2.</li>

  </ul>

  </li>

  </ul>'
updated: '2024-11-15T22:52:50Z'
version: v3.7.0
version_title: v3.7.0
website: https://wiki.ds-homebrew.com/godmode9i/
wiki: https://wiki.ds-homebrew.com/other/godmode9i
---
### Installation:
- TWiLight Menu++: Use either the `GodMode9i.nds` or `GodMode9i.dsi` file, they function identically with TWiLight Menu++
   - The only difference is that `GodMode9i.dsi` has a Title ID
- Flashcard: Use the `GodMode9i.nds` file
- hiyaCFW SDNAND: Install the `GodMode9i.dsi` file with [NTM](/ds/ntm)
- 3DS HOME Menu: Install the `GodMode9i.cia` file with [FBI](/3ds/fbi-nh)

### Features:
- Dump GameBoy Advance cartridges on the original Nintendo DS and Nintendo DS Lite consoles.
- Dump Nintendo DS/DSi cartridges on Nintendo DSi and Nintendo 3DS consoles (if GodMode9i is ran on the console SD card).
- Copy, move, delete, rename files/folders and create folders.
- Mount the NitroFS of .nds files.
- Browse files on supported flashcards when running GM9i from the NAND or SD Card. (`AceKard 2(i)` & `R4 Ultra (r4ultra.com)`)