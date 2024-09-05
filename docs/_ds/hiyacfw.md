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
  hiyaCFW.7z:
    size: 221761
    size_str: 216 KiB
    url: https://github.com/DS-Homebrew/hiyaCFW/releases/download/v1.5.1/hiyaCFW.7z
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
stars: 126
systems:
- DS
title: hiyaCFW
unistore_exclude: true
update_notes: '<p>To update:</p>

  <ul>

  <li>If you''re using v1.5.0, replace <code class="notranslate">hiya.dsi</code> on
  the SD root, with the one from the 7z file, in <code class="notranslate">for SDNAND
  SD card</code>.</li>

  <li>If you''re using v1.4.1 or prior, re-run hiyaCFW Helper.</li>

  </ul>

  <h3>Bug fix</h3>

  <ul>

  <li>Changing the region on a JPN NAND will no longer cause touch input to not work!

  <ul>

  <li>This is achieved by clearing the TWLCFG files, which as a result, will cause
  the system settings to reset.</li>

  <li>If the issue is still occurring, change the region to a different one, save,
  reboot, and then switch back.</li>

  </ul>

  </li>

  </ul>'
updated: '2024-03-31T03:46:27Z'
version: v1.5.1
version_title: v1.5.1
wiki: https://wiki.ds-homebrew.com/hiyacfw/
---
**Note:** For the initial install, please follow [this guide](https://wiki.ds-homebrew.com/hiyacfw/installing). If you are updating, then simply replace `sd:/hiya.dsi` from the `for SDNAND SD card` in the 7z.