---
author: JeffRuLz
avatar: https://avatars.githubusercontent.com/u/14222721?v=4
categories:
- game
color: '#8b948e'
color_bg: '#78807a'
created: '2021-01-28T00:52:25Z'
description: Port of Sonic 1 and 2 to the 3DS, based on Rubberduckycooly's Sonic 1/2
  (2013) decompilation
download_page: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases
downloads:
  Sonic1.3dsx:
    size: 1051460
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic1.3dsx
  Sonic1.cia:
    size: 1057216
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic1.cia
  Sonic1_rev01.3dsx:
    size: 1051676
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic1_rev01.3dsx
  Sonic1_rev01.cia:
    size: 1057728
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic1_rev01.cia
  Sonic2.3dsx:
    size: 1051460
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic2.3dsx
  Sonic2.cia:
    size: 1072576
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic2.cia
  Sonic2_rev01.3dsx:
    size: 1051676
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic2_rev01.3dsx
  Sonic2_rev01.cia:
    size: 1072576
    size_str: 1 MiB
    url: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/releases/download/v1.3.0/Sonic2_rev01.cia
github: JeffRuLz/Sonic-1-2-2013-Decompilation
icon: https://raw.githubusercontent.com/JeffRuLz/Sonic-1-2-2013-Decompilation/main/Sonic1Decomp.3DS/banner/icon.png
image: https://raw.githubusercontent.com/JeffRuLz/Sonic-1-2-2013-Decompilation/main/Sonic1Decomp.3DS/banner/banner.png
image_length: 35081
layout: app
license: other
license_name: Other
qr:
  Sonic1.cia: https://db.universal-team.net/assets/images/qr/sonic1-cia.png
  Sonic1_rev01.cia: https://db.universal-team.net/assets/images/qr/sonic1_rev01-cia.png
  Sonic2.cia: https://db.universal-team.net/assets/images/qr/sonic2-cia.png
  Sonic2_rev01.cia: https://db.universal-team.net/assets/images/qr/sonic2_rev01-cia.png
screenshots:
- description: Sonic 1 green hill zone
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-1-green-hill-zone.png
- description: Sonic 1 special stage
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-1-special-stage.png
- description: Sonic 1 star light zone
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-1-star-light-zone.png
- description: Sonic 1 title screen
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-1-title-screen.png
- description: Sonic 2 casino night zone
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-2-casino-night-zone.png
- description: Sonic 2 emeral hill zone
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-2-emeral-hill-zone.png
- description: Sonic 2 special stage
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-2-special-stage.png
- description: Sonic 2 title screen
  url: https://db.universal-team.net/assets/images/screenshots/sonic-1--2/sonic-2-title-screen.png
script_message: 'Note: You will need "Data.rsdk" from

  the Steam, Android, or iOS version in

  "/3ds/Sonic1" / "/3ds/Sonic2" to play the game.'
source: https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation
stars: 52
systems:
- 3DS
title: Sonic 1 / 2
unique_ids:
- '0x479B'
- '0x479C'
update_notes: '<h1 dir="auto"><a href="https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation/tree/main#requirements">!!!
  Read the Setup Guide !!!</a></h1>

  <h1 dir="auto">A New 3DS is required</h1>

  <h3 dir="auto">Updates</h3>

  <ul dir="auto">

  <li>Now based on RSDKv4 version 1.3.0</li>

  <li>Mods can now be used. (Read: <a href="https://github.com/JeffRuLz/Sonic-1-2-2013-Decompilation#about-mods">About
  Mods</a>)</li>

  <li>REV01 builds are now provided

  <ul dir="auto">

  <li>Adds compatibility for certain data files.</li>

  <li>Only use if you''re having issues with the normal builds.</li>

  </ul>

  </li>

  <li>Audio processing is now done in a separate thread on a separate core</li>

  <li>Performance boost to special stages, due to the new audio thread

  <ul dir="auto">

  <li>Sonic 1 special stages run at 30-60fps</li>

  <li>Sonic 2 special stages run 15-30fps</li>

  </ul>

  </li>

  <li>Added warning screens for some common user errors</li>

  <li><strong>October 9th Hotfix: Fixed a bug that prevented multiple mods from loading.</strong></li>

  <li><strong>October 11th: Debug text is no longer displayed when debug mode is disabled.
  (Except for specific situations.)</strong></li>

  <li><strong>November 4th: Fixed game options not working properly (Thanks to <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MegAmi24/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MegAmi24">@MegAmi24</a>)</strong></li>

  </ul>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/14222721/194726393-d59587cf-1530-46f5-850c-ef33c3a882ff.png"><img
  src="https://user-images.githubusercontent.com/14222721/194726393-d59587cf-1530-46f5-850c-ef33c3a882ff.png"
  alt="sonic1qr" style="max-width: 100%;"></a></p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/14222721/194726395-24f5fa12-421f-4dc2-82bc-7e4d81c5281b.png"><img
  src="https://user-images.githubusercontent.com/14222721/194726395-24f5fa12-421f-4dc2-82bc-7e4d81c5281b.png"
  alt="sonic2qr" style="max-width: 100%;"></a></p>'
updated: '2022-10-08T20:05:50Z'
version: v1.3.0
version_title: New 3DS v1.3.0
---
Port of Sonic 1 and 2 to the 3DS, based on Rubberduckycooly's Sonic 1/2 (2013) decompilation.

In order to run the game, you need to get the "Data.rsdk.xmf" file from a copy of Sonic 1 or 2 (2013), rename it to "Data.rsdk", and copy it to "/3ds/Sonic1" or "/3ds/Sonic2" respectively on your SD card.

Official video guide on how to get the "Data.rsdk.xmf" file from each game: <https://www.youtube.com/watch?v=gzIfRW91IxE>