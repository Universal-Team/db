---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
- save-tool
color: '#be8345'
created: '2018-10-02T16:59:38Z'
description: 'GodMode9i Explorer - A full access file browser for the Nintendo DS
  and DSi consoles :godmode:'
download_page: https://github.com/DS-Homebrew/GodMode9i/releases
downloads:
  GodMode9i.7z:
    size: 177027
    size_str: 172 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v2.7.0/GodMode9i.7z
github: DS-Homebrew/GodMode9i
icon: https://raw.githubusercontent.com/DS-Homebrew/GodMode9i/master/icon.bmp
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
source: https://github.com/DS-Homebrew/GodMode9i
systems:
- DS
title: GodMode9i
update_notes: '<p><strong>What''s new?</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Hex editor has been added!</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Peter0x44/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Peter0x44">@Peter0x44</a>)
  Implemented calculating SHA1 hash of files.</li>

  <li>B4DS is no longer booted on flashcards, as it got merged with the main nds-bootstrap
  build.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/spellboundtriangle/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/spellboundtriangle">@spellboundtriangle</a>)
  Added save restoration support for sav1-sav9 filetypes.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>RSA key is now preserved when dumping a trimmed DS ROM.

  <ul>

  <li>If you previously dumped your trimmed ROM using a previous version of GM9<strong>i</strong>,
  please redump using this version, in order for cloneboot to work.</li>

  </ul>

  </li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed 128KiB EEPROM save dumping.</li>

  <li>Fix <code>D</code> first appearing in the filename, when dumping GBA ROM.</li>

  <li>Cleared SD IRQ stat and mask registers on boot.

  <ul>

  <li>Should (hopefully) fix NAND init being stuck, if booted via hiyaCFW.</li>

  </ul>

  </li>

  </ul>'
updated: '2021-07-14T05:09:58Z'
version: v2.7.0
version_title: v2.7.0
wiki: https://wiki.ds-homebrew.com/other/godmode9i
---
### Installation:
- TWiLight Menu++: Use either the `GodMode9i.nds` or `GodMode9i.dsi` file, they function identically with TWiLight Menu++
   - The only difference is that `GodMode9i.dsi` has a Title ID
- Flashcard: Use the `GodMode9i.nds` file
- hiyaCFW SDNAND: Install the `GodMode9i.dsi` file with [TMFH](/ds/tmfh)
- 3DS HOME Menu: Install the `GodMode9i.cia` file with [FBI](/3ds/fbi)

### Features:
- Dump GameBoy Advance cartridges on the original Nintendo DS and Nintendo DS Lite consoles.
- Dump Nintendo DS/DSi cartridges on Nintendo DSi and Nintendo 3DS consoles (if GodMode9i is ran on the console SD card).
- Copy, move, delete, rename files/folders and create folders.
- Mount the NitroFS of .nds files.
- Browse files on supported flashcards when running GM9i from the NAND or SD Card. (`AceKard 2(i)` & `R4 Ultra (r4ultra.com)`)