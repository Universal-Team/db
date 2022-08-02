---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
color: '#666666'
color_bg: '#666666'
created: '2017-07-24T04:43:30Z'
description: World's FIRST Nintendo DSi CFW!
download_page: https://github.com/RocketRobz/hiyaCFW/releases
downloads:
  HiyaCFW.7z:
    size: 848138
    size_str: 828 KiB
    url: https://github.com/DS-Homebrew/hiyaCFW/releases/download/v1.3.2/HiyaCFW.7z
github: RocketRobz/hiyaCFW
icon: https://db.universal-team.net/assets/images/icons/hiyacfw.png
image: https://raw.githubusercontent.com/RocketRobz/hiyaCFW/unlaunch/logo/logo.png
image_length: 26522
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds/blob/master/extras/hiyaCFW.7z
  downloads:
    hiyaCFW.7z:
      url: https://github.com/TWLBot/Builds/raw/master/extras/hiyaCFW.7z
source: https://github.com/DS-Homebrew/hiyaCFW
systems:
- DS
title: hiyaCFW
unistore_exclude: true
update_notes: '<p>UPDATE 8/31/2019: Added .ips patch for Chinese iQue consoles! Note
  that touch input does not work.<br>

  UPDATE 11/6/2018: Renamed <code class="notranslate">bootcode.dsi</code> to <code
  class="notranslate">hiya.dsi</code> for Unlaunch 1.8 (and later).<br>

  UPDATE 6/6/2018: Added AUS Launcher .tmd.<br>

  UPDATE 7/5/2018: Added Unlaunch 0.9 compatible <code class="notranslate">bootcode.dsi</code></p>

  <p>ATTENTION UNLAUNCH 0.9 (and later) USERS!</p>

  <p>bootcode.dsi has been updated for HiyaCFW to work on latest Unlaunch! As of Unlaunch
  0.9, Unlaunch now loads arm9 binary in a similar manner to official software. This
  means we can''t skip loading something to the area reserved for arm9''s decrypted
  secure area in arm9 ram. I''ve added a bootstub to arm9 binary and loaded the arm9
  binary to a higher ram address (the bootstub moves it back minus the blank secure
  area data) to get around the issue.</p>

  <p>Hopefully at some point in the near future we can just have it compile to use
  a slightly higher entry point in arm9 ram so we don''t have to use a bootstub post
  compile. We''ll probably wait until the next Unlaunch update to determine if we
  need to do this or not.</p>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>Now checks for the size of Launcher''s .tmd.<br>

  If it bigger than 0x208 bytes (can be caused by having Unlaunch in the .tmd), a
  message will be shown, saying to <code class="notranslate">replace it with a clean
  one</code>.</li>

  <li>EUR and JPN Launcher .tmds now bundled!</li>

  <li>Now reads <code class="notranslate">bootloader.nds</code> from the <code class="notranslate">hiya</code>
  folder.<br>

  If you have <code class="notranslate">bootloader.nds</code> on the SD card root,
  please move it into the <code class="notranslate">hiya</code> folder.</li>

  </ul>'
updated: '2018-06-05T23:29:42Z'
version: v1.3.2
wiki: https://wiki.ds-homebrew.com/hiyacfw/
---
**Note:** For the initial install, please follow [this guide](https://wiki.ds-homebrew.com/hiyacfw/installing). If you are updating, then simply replace `sd:/hiya.dsi` from the `for SDNAND SD card` in the 7z.