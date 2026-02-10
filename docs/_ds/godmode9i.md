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
    size: 372620
    size_str: 363 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.9.0/GodMode9i.7z
  GodMode9i.cia:
    size: 1008896
    size_str: 985 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.9.0/GodMode9i.cia
  GodMode9i.dsi:
    size: 994304
    size_str: 971 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.9.0/GodMode9i.dsi
  GodMode9i.nds:
    size: 994304
    size_str: 971 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.9.0/GodMode9i.nds
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
stars: 604
systems:
- DS
title: GodMode9i
update_notes: '<h3 dir="auto">🎁 What''s new? 🎁</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ApacheThunder/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ApacheThunder">@ApacheThunder</a>:
  Added support for mounting these flashcards without the need to launch them first:

  <ul dir="auto">

  <li>CycloDS Evolution</li>

  <li>DSpico</li>

  <li>DSTT</li>

  <li>Demon/DSTTi clones</li>

  <li>EZ Flash Parellel</li>

  <li>Games n'' Music</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/edo9300/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/edo9300">@edo9300</a>
  &amp; <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lorenzooone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lorenzooone">@Lorenzooone</a>:
  TWLNAND contents can now be read from 3DS consoles!</li>

  <li>Various: Updated translations.</li>

  </ul>

  <h3 dir="auto">🎁 Bug fixes 🎁</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Lorenzooone/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Lorenzooone">@Lorenzooone</a>:
  Fixed NAND mounting on dev 3DS consoles.</li>

  <li>Fixed libfat to properly read and write files above 2GB.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>When booting a <code class="notranslate">.nds</code> file without launching
  the above flashcards first, they''ll be stuck on white screens.</li>

  </ul>'
updated: '2025-12-25T10:39:19Z'
version: v3.9.0
version_title: 'v3.9.0: TWL Christmas Release 🎄'
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