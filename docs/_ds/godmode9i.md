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
    size: 348894
    size_str: 340 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.2/GodMode9i.7z
  GodMode9i.cia:
    size: 952576
    size_str: 930 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.2/GodMode9i.cia
  GodMode9i.dsi:
    size: 937984
    size_str: 916 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.2/GodMode9i.dsi
  GodMode9i.nds:
    size: 937984
    size_str: 916 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v3.5.2/GodMode9i.nds
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
update_notes: '<h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>Fixed an overlooked bug which caused game dumping to crash.</li>

  </ul>

  <h3 dir="auto">Known bug</h3>

  <ul dir="auto">

  <li>Booting a <code class="notranslate">.nds</code> file will cause a Guru Meditation
  Error to appear. To boot <code class="notranslate">.nds</code> files again, please
  downgrade to v3.5.0.</li>

  </ul>'
updated: '2024-02-28T03:26:57Z'
version: v3.5.2
version_title: v3.5.2
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