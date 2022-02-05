---
author: lifehackerhansol
avatar: https://avatars.githubusercontent.com/u/37358975?v=4
categories:
- utility
color: '#90594d'
created: '2021-06-16T08:14:55Z'
description: Yet another nds-bootstrap forwarder. Runs from 3DS-mode!
download_page: https://github.com/lifehackerhansol/YANBF/releases
downloads:
  YANBF-Linux.zip:
    size: 79798063
    size_str: 76 MiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.0/YANBF-Linux.zip
  YANBF-Windows.zip:
    size: 55008221
    size_str: 52 MiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.0/YANBF-Windows.zip
  YANBF-macOS.zip:
    size: 81686585
    size_str: 77 MiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.0/YANBF-macOS.zip
  bootstrap.cia:
    size: 217344
    size_str: 212 KiB
    url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.0/bootstrap.cia
github: lifehackerhansol/YANBF
icon_index: 198
image: https://avatars.githubusercontent.com/u/37358975?v=4
image_length: 32023
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
prerelease:
  download_page: https://github.com/lifehackerhansol/YANBF/releases/tag/v1.1.1-b1
  downloads:
    YANBF-Linux.zip:
      size: 79756471
      size_str: 76 MiB
      url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.1-b1/YANBF-Linux.zip
    YANBF-Windows.zip:
      size: 54978806
      size_str: 52 MiB
      url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.1-b1/YANBF-Windows.zip
    YANBF-macOS.zip:
      size: 81643118
      size_str: 77 MiB
      url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.1-b1/YANBF-macOS.zip
    bootstrap.cia:
      size: 206080
      size_str: 201 KiB
      url: https://github.com/lifehackerhansol/YANBF/releases/download/v1.1.1-b1/bootstrap.cia
  qr:
    bootstrap.cia: https://db.universal-team.net/assets/images/qr/prerelease/bootstrap-cia.png
  update_notes: '<h2 dir="auto">The <code>bootstrap.cia</code> is a <em><strong>prerelease.</strong></em>
    The generator, however, is an update you won''t want to miss.</h2>

    <h3 dir="auto">What''s new?</h3>

    <ul dir="auto">

    <li><a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>:
    Preliminary widescreen support.

    <ul dir="auto">

    <li>This will not work until the <a href="https://github.com/RocketRobz/NTR_Forwarder/releases">SD
    Forwarder Pack</a> is updated. (Still works normally.)</li>

    <li>You can optionally compile the SD forwarder pack yourself, but no support
    will be provided at this time.</li>

    </ul>

    </li>

    </ul>

    <h3 dir="auto">Bug fix</h3>

    <ul dir="auto">

    <li>Fixed an issue where makerom may fail if the ROM path has spaces.</li>

    <li>Fixed some NDS ROMs only having a handful of languages. Now all languages
    are checked to make sure an out-of-bounds error doesn''t happen.</li>

    <li>Tried to make the unique ID more... unique. This should fix an issue where
    same game from different region replaces each other.</li>

    </ul>'
  update_notes_md: "## The `bootstrap.cia` is a _**prerelease.**_ The generator, however,\
    \ is an update you won't want to miss.\n\n### What's new?\n- @Epicpkmn11: Preliminary\
    \ widescreen support.\n    - This will not work until the [SD Forwarder Pack](https://github.com/RocketRobz/NTR_Forwarder/releases)\
    \ is updated. (Still works normally.)\n    - You can optionally compile the SD\
    \ forwarder pack yourself, but no support will be provided at this time.\n\n###\
    \ Bug fix\n- Fixed an issue where makerom may fail if the ROM path has spaces.\n\
    - Fixed some NDS ROMs only having a handful of languages. Now all languages are\
    \ checked to make sure an out-of-bounds error doesn't happen.\n- Tried to make\
    \ the unique ID more... unique. This should fix an issue where same game from\
    \ different region replaces each other.\n"
  updated: '2022-02-05T01:47:15Z'
  version: v1.1.1-b1
  version_title: 'v1.1.1-b1: generator fixes'
qr:
  bootstrap.cia: https://db.universal-team.net/assets/images/qr/bootstrap-cia.png
source: https://github.com/lifehackerhansol/YANBF
systems:
- 3DS
title: YANBF
update_notes: '<p dir="auto">New:</p>

  <ul dir="auto">

  <li><a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Olmectron/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Olmectron">@Olmectron</a>:
  a GUI is provided! <a href="https://github.com/Olmectron/Simple-Web-App-GUI-for-YANBF-Generator">https://github.com/Olmectron/Simple-Web-App-GUI-for-YANBF-Generator</a></li>

  </ul>

  <p dir="auto">This release was solely made to provide a graphical user interface
  for generating forwarders. Go wild!</p>'
updated: '2022-01-16T08:12:18Z'
version: v1.1.0
version_title: 'v1.1.0: wow a GUI to make this'
---
YANBF is a 3DS-mode nds-bootstrap forwarder, allowing for more than 40 forwarder titles as compared to the older forwarder template.