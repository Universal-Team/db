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
    size: 222231
    size_str: 217 KiB
    url: https://github.com/DS-Homebrew/hiyaCFW/releases/download/v1.5.0/hiyaCFW.7z
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
update_notes: '<p>To update, re-run hiyaCFW Helper.</p>

  <h3>What''s new?</h3>

  <ul>

  <li>RSA checking for <code class="notranslate">/sys/HWINFO_S.dat</code> has been
  patched out. This means the region can now be changed (for JPN, USA, EUR, and AUS
  NANDs), as well as NAND backups from any console now useable!

  <ul>

  <li>If you get <code class="notranslate">Error: 1-2435-8325</code>, the bootloader
  has not been updated with the new patch. If you have not re-run hiyaCFW Helper,
  please do so in order for the patch to take effect.</li>

  </ul>

  </li>

  <li>hiyaCFW will no longer function if SD card is write-locked.</li>

  </ul>

  <h3>Known bugs</h3>

  <ul>

  <li>Changing the region on a JPN NAND will cause touch input to not function.</li>

  <li>When using ntrboot, modcrypted DSiWare apps are not launchable. Non-modcrypted
  applications are still launchable, such as homebrew (ex. <strong>TW</strong>i<strong>L</strong>ight
  Menu++). This may be fixed in the future, either by hiyaCFW or an ntrboot <code
  class="notranslate">.gcd</code> file.</li>

  </ul>'
updated: '2024-01-30T01:45:01Z'
version: v1.5.0
version_title: v1.5.0
wiki: https://wiki.ds-homebrew.com/hiyacfw/
---
**Note:** For the initial install, please follow [this guide](https://wiki.ds-homebrew.com/hiyacfw/installing). If you are updating, then simply replace `sd:/hiya.dsi` from the `for SDNAND SD card` in the 7z.