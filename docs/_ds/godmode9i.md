---
author: DS-Homebrew
categories:
- utility
- save-tool
color: '#be8345'
created: '2018-10-02T16:59:38Z'
description: 'GodMode9i Explorer - A full access file browser for the Nintendo DS
  and DSi consoles :godmode:'
download_page: https://github.com/DS-Homebrew/GodMode9i/releases/tag/v2.6.0
downloads:
  GodMode9i.7z:
    size: 175923
    size_str: 171 KiB
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v2.6.0/GodMode9i.7z
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

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/unresolvedsymbol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/unresolvedsymbol">@unresolvedsymbol</a>)
  Added .nds ROM booting with nds-bootstrap!<br>

  It is done by selecting <code>Bootstrap file</code> after selecting a <code>.nds</code>
  file.</li>

  <li>Filename of the GBA or NDS ROM is now shown when dumping, so you''ll know what
  to look for.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/unresolvedsymbol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/unresolvedsymbol">@unresolvedsymbol</a>
  and <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Separate the selection and the clipboard like GM9.

  <ul>

  <li>Added selecting while holding L.</li>

  <li>The first 5 paths that will be deleted, will be printed on the bottom screen.</li>

  </ul>

  </li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/urmum-69/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/urmum-69">@urmum-69</a>)
  The free space on each drive in the root menu is now shown!</li>

  <li>GitHub page link has been updated.</li>

  <li>The regular <code>.nds</code> file has been renamed to <code>.dsi</code>.

  <ul>

  <li>A new <code>.nds</code> file has been added for flashcard compatibility.</li>

  </ul>

  </li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>(me and <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed some known issues when dumping ROMs.</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed getting EEPROM size when the first is all 0.</li>

  </ul>'
updated: '2021-01-28T01:47:13Z'
version: v2.6.0
version_title: v2.6.0
wiki: https://github.com/DS-Homebrew/GodMode9i/wiki
---
Features:
- Dump GameBoy Advance cartridges on the original Nintendo DS and Nintendo DS Lite consoles.
- Dump Nintendo DS/DSi cartridges on Nintendo DSi and Nintendo 3DS consoles (if GodMode9i is ran on the console SD card).
- Copy, move, delete, rename files/folders and create folders.
- Mount the NitroFS of .nds files.
- Browse files on supported flashcards when running GM9i from the NAND or SD Card. (`AceKard 2(i)` & `R4 Ultra (r4ultra.com)`)