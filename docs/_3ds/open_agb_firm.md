---
author: profi200
avatar: https://avatars.githubusercontent.com/u/7831477?v=4
categories:
- emulator
- firm
color: '#c2e5d8'
created: '2020-04-15T21:49:42Z'
description: open_agb_firm is a bare metal app for running GBA homebrew/games using
  the 3DS builtin GBA hardware.
download_page: https://github.com/profi200/open_agb_firm/releases
downloads:
  open_agb_firm_alpha_20201224.7z:
    size: 50931
    size_str: 49 KiB
    url: https://github.com/profi200/open_agb_firm/releases/download/alpha_2020-12-24/open_agb_firm_alpha_20201224.7z
github: profi200/open_agb_firm
image: https://avatars.githubusercontent.com/u/7831477?v=4
image_length: 1560
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/profi200/open_agb_firm
systems:
- 3DS
title: open_agb_firm
update_notes: '<p>This is a build from the kernel_experiments branch for the impatient.</p>

  <ul>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/5f257392863a807a4c1b70f836d99cb656c931b7/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/5f257392863a807a4c1b70f836d99cb656c931b7"><tt>5f25739</tt></a>
  Proper ROM mirroring for all 8 Mbit games and direct boot (no BIOS intro) should
  have perfect compatibility now. This breaks mGBA''s test suite ROM out of bounds
  tests again because the ROM is treated as 8 Mbit ROM (different padding from what
  it expects).</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/dd68d381ac7af12803e0826778a869347d28fb06/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/dd68d381ac7af12803e0826778a869347d28fb06"><tt>dd68d38</tt></a>
  <a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/31bbcbfe2593d407525c2c2bb4c7a58201dc6e1c/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/31bbcbfe2593d407525c2c2bb4c7a58201dc6e1c"><tt>31bbcbf</tt></a>
  <a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/29413979fa2589e1cb9ba332b2332141659bf85e/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/29413979fa2589e1cb9ba332b2332141659bf85e"><tt>2941397</tt></a>
  Basic config file support. A few settings can be changed in "/3ds/open_agb_firm/config.ini"
  now. If you want the same gamma as previous releases change "outGamma=..." to "outGamma=1.21".
  Results may vary depending on what LCD panel your 3DS uses. The default of 1.54
  is tuned for the old 3DS Sharp panel.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/96eebb01db61f12f1bf52df093edcfafc1f08f14/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/96eebb01db61f12f1bf52df093edcfafc1f08f14"><tt>96eebb0</tt></a>
  fatfs got updated to R0.14.</li>

  </ul>

  <p>The screenshot/texture dump location is now "/3ds/open_agb_firm". This will change
  to a separate "screenshots" dir once screenshots are created by date. If the video
  output freezes after making a screenshot try pressing the HOME button. This works
  most of the time. This is due to a hard to track down bug and will be fixed later.</p>

  <p><strong>This can and will destroy savegames for a few games due to broken save
  type detection so backup your saves!</strong> You have been warned.<br>

  Also note that EEPROM savegames from some emulators or even flashcarts are incompatible
  because they are laid out wrong (every 8 bytes block of data is reversed). This
  <a href="https://gist.github.com/profi200/e06794d7561ed552c518b4b0b2f5f2f6">tool</a>
  can fix that.</p>

  <p>The used scale matrix is the default "Sharp interpolated" one.</p>'
updated: '2020-12-24T12:17:14Z'
version: alpha_2020-12-24
version_title: open_agb_firm alpha build 2020-12-24
---
