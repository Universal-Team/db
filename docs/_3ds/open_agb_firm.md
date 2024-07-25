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
  open_agb_firm_beta_20240725.7z:
    size: 141257
    size_str: 137 KiB
    url: https://github.com/profi200/open_agb_firm/releases/download/beta_2024-07-25/open_agb_firm_beta_20240725.7z
github: profi200/open_agb_firm
image: https://avatars.githubusercontent.com/u/7831477?v=4&size=128
image_length: 1560
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/profi200/open_agb_firm
systems:
- 3DS
title: open_agb_firm
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>Refactor IPS patching by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Nemris/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Nemris">@Nemris</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2145350529"
  data-permission-text="Title is private" data-url="https://github.com/profi200/open_agb_firm/issues/163"
  data-hovercard-type="pull_request" data-hovercard-url="/profi200/open_agb_firm/pull/163/hovercard"
  href="https://github.com/profi200/open_agb_firm/pull/163">#163</a></li>

  <li>Video dithering has been fully disabled.</li>

  <li>[libn3ds] Fixed a GPIO handling bug that may or may not degrade New 3DS hardware.</li>

  <li>Screenshots now only contain the frame data itself and screenshots are in 5-bit
  RGB format which means they are 100% lossless. Beware of rounding errors when converting
  the .bmp files. GIMP is one program that converts them correctly. ImageMagick does
  <strong>not</strong>.</li>

  <li>Added experimental support for true color correction thanks to hunterk and Pokefan531
  for their amazing <a href="https://forums.libretro.com/t/real-gba-and-ds-phat-colors/1540/220"
  rel="nofollow">libretro shaders</a>. Please note that 2/3DS LCDs are generally poor
  quality and don''t come correctly calibrated from factory so the actual look might
  not match the LCD on a GBA but it''s a real improvement for games like Golden Sun
  which look awful otherwise (see below). Also note that enabling color correction
  will shorten battery runtime (Testers welcome. I didn''t measure battery runtime
  with and without.). For more instructions refer to the colorProfile setting in the
  <a href="https://github.com/profi200/open_agb_firm?tab=readme-ov-file#video">README</a>.<br>

  <br>

  More comparisons: <a href="https://i.ibb.co/6Z8tx29/all-sbs.png" rel="nofollow">https://i.ibb.co/6Z8tx29/all-sbs.png</a></li>

  <li>Other small changes under the hood which don''t affect users.</li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Nemris/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Nemris">@Nemris</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2145350529" data-permission-text="Title is private" data-url="https://github.com/profi200/open_agb_firm/issues/163"
  data-hovercard-type="pull_request" data-hovercard-url="/profi200/open_agb_firm/pull/163/hovercard"
  href="https://github.com/profi200/open_agb_firm/pull/163">#163</a></li>

  </ul>'
updated: '2024-07-25T15:57:03Z'
version: beta_2024-07-25
version_title: open_agb_firm beta build 2024-07-25
---
