---
author: profi200
avatar: https://avatars.githubusercontent.com/u/7831477?v=4
categories:
- emulator
- firm
color: '#c2e5d8'
color_bg: '#6c8078'
created: '2020-04-15T21:49:42Z'
description: open_agb_firm is a bare metal app for running GBA homebrew/games using
  the 3DS builtin GBA hardware.
download_page: https://github.com/profi200/open_agb_firm/releases
downloads:
  open_agb_firm_beta_20240730.7z:
    size: 141520
    size_str: 138 KiB
    url: https://github.com/profi200/open_agb_firm/releases/download/beta_2024-07-30/open_agb_firm_beta_20240730.7z
github: profi200/open_agb_firm
image: https://avatars.githubusercontent.com/u/7831477?v=4&size=128
image_length: 1560
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/profi200/open_agb_firm
stars: 883
systems:
- 3DS
title: open_agb_firm
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/5356e5c89a8f85b708fa498a2ead70b3a8368021/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/5356e5c89a8f85b708fa498a2ead70b3a8368021"><tt>5356e5c</tt></a>
  Implemented full gamma correction for top LCDs which improves colors noticeably
  without crushing details in shadows. Colors should no longer look too dark regardless
  of the colorProfile setting. Note that due to wildly varying color temperatures
  and LCD types this will not make GBA games look exactly like on your monitor with
  or without color correction. Also note that the gamma curve is not a perfect fit
  for IPS New 3DS XL consoles since they have very bad gamma near shadows but it''s
  a very noticeable improvement nonetheless.</li>

  <li>A side effect of the new gamma correction is that the gbaGamma, lcdGamma, brightness
  and contrast settings are disabled for now. They will be reimplemented in the color
  profile settings later.</li>

  </ul>

  <p dir="auto">Example of what the gamma curve correction does. The brighter version
  is roughly how the top LCD shows colors without correction.<br>

  </p>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/profi200/open_agb_firm/compare/beta_2024-07-25...beta_2024-07-30"><tt>beta_2024-07-25...beta_2024-07-30</tt></a></p>'
updated: '2024-07-30T14:51:11Z'
version: beta_2024-07-30
version_title: open_agb_firm beta build 2024-07-30
---
