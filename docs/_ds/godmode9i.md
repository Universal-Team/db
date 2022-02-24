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
    size: 340724
    size_str: 332 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.2.0/GodMode9i.7z
github: DS-Homebrew/GodMode9i
icon: https://db.universal-team.net/assets/images/icons/godmode9i.png
icon_index: 11
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
update_notes: '<p dir="auto"><strong>What''s new?</strong> (<a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)</p>

  <ul dir="auto">

  <li>Added restoring DS saves on DS/DS Lite.</li>

  <li>Added dumping DS saves using GBA cart save data.</li>

  <li>Added title manager menu for easier DSiWare dumping.</li>

  <li>Metadata dumping has been added.</li>

  <li>Slot-2 RAM can now be used as RAM drives. (ex. DS Memory Expansion Pak, Supercard
  MiniSD, etc.)</li>

  <li>NitroFS can now be mounted from SysNAND and SDNAND.</li>

  </ul>

  <p dir="auto"><strong>Improvements</strong></p>

  <ul dir="auto">

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  DSi &amp; 3DS RAM drives have been combined into one.</li>

  <li>Increased DSi/3DS RAM drive size by 3MB.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated translations.</li>

  </ul>

  <p dir="auto"><strong>Bug fix</strong></p>

  <ul dir="auto">

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed remounting SD card.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Writing actions are now hidden when drive is read-only.</li>

  <li>Other minor fixes.</li>

  </ul>'
updated: '2022-02-15T04:44:40Z'
version: v3.2.0
version_title: Valentine's Day Release (2022)
website: https://wiki.ds-homebrew.com/godmode9i/
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