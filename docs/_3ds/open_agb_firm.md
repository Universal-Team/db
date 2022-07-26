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
  open_agb_firm_alpha_20220425.7z:
    size: 175207
    size_str: 171 KiB
    url: https://github.com/profi200/open_agb_firm/releases/download/alpha_2022-4-25/open_agb_firm_alpha_20220425.7z
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
update_notes: '<p dir="auto">This is a build from the master branch for the impatient.</p>

  <ul dir="auto">

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/9756e2eafcfe1a881ccebe8bf13fda4b8fb2122c/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/9756e2eafcfe1a881ccebe8bf13fda4b8fb2122c"><tt>9756e2e</tt></a>
  Added configurable scaling so only 1 build is needed instead of one per scaling
  method. See the <a href="https://github.com/profi200/open_agb_firm/blob/master/README.md#video">README</a>
  on how to configure this.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/a9fcf853bb2b21623f528ac23675c8af05180297/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/a9fcf853bb2b21623f528ac23675c8af05180297"><tt>a9fcf85</tt></a>
  Fixed the missing newline in the default config.ini.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/782596facd41a6e9e5e9018b34b8dfbb4788deec/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/782596facd41a6e9e5e9018b34b8dfbb4788deec"><tt>782596f</tt></a>
  firmtool support was added to the build system thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Midnoclose/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Midnoclose">@Midnoclose</a>.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/2222e54f0fb8e981cd6fc4df216b058b0974f07f/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/2222e54f0fb8e981cd6fc4df216b058b0974f07f"><tt>2222e54</tt></a>
  Fixed a bug that may cause the file browser not to display all 1000 files.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/4a6603d1104587fd7682854b794697c08f3f8a35/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/4a6603d1104587fd7682854b794697c08f3f8a35"><tt>4a6603d</tt></a>
  Added day of week calculation for the GBA RTC.</li>

  <li>Other non-user facing improvements/fixes.</li>

  </ul>

  <p dir="auto">The save type database was not created by me and i can''t vouch for
  its completeness or accuracy (i have not heard any complaints so far). Keep that
  in mind when using this build and backup your saves.<br>

  Also note that EEPROM savegames from some emulators or even flashcarts are incompatible
  because they are laid out wrong (every 8 bytes block of data is reversed). This
  <a href="https://gist.github.com/profi200/e06794d7561ed552c518b4b0b2f5f2f6">tool</a>
  can fix that.</p>

  <p dir="auto">The used scale matrix is the default "Sharp + edge enhance" one.</p>

  <p dir="auto"><strong>Known issues</strong><br>

  If the video output freezes after making a screenshot try pressing the HOME button.
  This works most of the time. This is due to a hard to track down bug and will be
  fixed later.</p>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/profi200/open_agb_firm/compare/alpha_2021-12-24...alpha_2022-4-25"><tt>alpha_2021-12-24...alpha_2022-4-25</tt></a></p>'
updated: '2022-04-25T19:33:22Z'
version: alpha_2022-4-25
version_title: open_agb_firm alpha build 2022-4-25
---
