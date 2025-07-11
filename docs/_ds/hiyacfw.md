---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- utility
color: '#666666'
color_bg: '#666666'
created: '2017-07-24T04:43:30Z'
description: World's FIRST Nintendo DSi CFW!
download_page: https://github.com/DS-Homebrew/hiyaCFW/releases
downloads:
  hiyaCFW.7z:
    size: 225233
    size_str: 219 KiB
    url: https://github.com/DS-Homebrew/hiyaCFW/releases/download/v1.6.1/hiyaCFW.7z
github: DS-Homebrew/hiyaCFW
icon: https://db.universal-team.net/assets/images/icons/hiyacfw.png
image: https://raw.githubusercontent.com/DS-Homebrew/hiyaCFW/unlaunch/logo/logo.png
image_length: 26522
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/hiyaCFW
stars: 151
systems:
- DS
title: hiyaCFW
unistore_exclude: true
update_notes: '<p dir="auto">To update:</p>

  <ul dir="auto">

  <li>If you''re using v1.6.0, replace <code class="notranslate">hiya.dsi</code> on
  the SD root, with the one from the 7z file, in <code class="notranslate">for SDNAND
  SD card</code>.</li>

  <li>If you''re using v1.5.1 or prior, (re-)run <a href="https://gitlab.com/R-YaTian/twlmagician/-/releases"
  rel="nofollow">TWLMagician</a>, which will fix the free space bug.</li>

  </ul>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>RGB565 <code class="notranslate">.bmp</code> splash screen images will now display
  properly!

  <ul dir="auto">

  <li>If the opposite splash screen image is in <code class="notranslate">.gif</code>
  format, the <code class="notranslate">.bmp</code> splash will be displayed in RGB555
  mode to prevent flickering when displaying the <code class="notranslate">.gif</code>
  splash.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed a bug where the DSi Shop and the 3DS Transfer Tool would still display
  an error after changing the region back to the original in the hiyaCFW config menu.

  <ul dir="auto">

  <li>For the fix to take effect, change the region to a different one, save, and
  change the region back to the one you normally use.</li>

  </ul>

  </li>

  <li>Fixed where either the regular hiyaCFW splash, or a splash screen consisting
  of only one or two <code class="notranslate">.bmp</code> files, is not displayed
  at all if the splash screen setting is enabled.</li>

  </ul>'
updated: '2025-07-04T07:04:29Z'
version: v1.6.1
version_title: 'v1.6.1: 4th of July Release'
wiki: https://wiki.ds-homebrew.com/hiyacfw/
---
**Note:** For the initial install, please follow [this guide](https://wiki.ds-homebrew.com/hiyacfw/installing). If you are updating, then simply replace `sd:/hiya.dsi` from the `for SDNAND SD card` in the 7z.