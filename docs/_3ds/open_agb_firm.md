---
author: profi200
categories:
- emulator
- firm
color: '#c2e5d8'
created: '2020-04-15T21:49:42Z'
description: open_agb_firm is a bare metal app for running GBA homebrew/games using
  the 3DS builtin GBA hardware.
download_page: https://github.com/profi200/open_agb_firm/releases/tag/alpha_2020-10-26
downloads:
  open_agb_firm_alpha_20201026.7z:
    size: 93876
    url: https://github.com/profi200/open_agb_firm/releases/download/alpha_2020-10-26/open_agb_firm_alpha_20201026.7z
github: profi200/open_agb_firm
image: https://avatars0.githubusercontent.com/u/7831477?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/profi200/open_agb_firm
systems:
- 3DS
title: open_agb_firm
update_notes: '<p>This is a build from the kernel_experiments branch for the impatient.</p>

  <ul>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/8fdc74a3c486af86416bf37505144dc03da66a14/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/8fdc74a3c486af86416bf37505144dc03da66a14"><tt>8fdc74a</tt></a>
  A temporary workaround has been put in place to prevent panics using bootloaders
  with incompatible screen init.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/07f6f01d921696c890f828f94289426eb64957d0/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/07f6f01d921696c890f828f94289426eb64957d0"><tt>07f6f01</tt></a>
  Mimic ROM out-of-bounds reads more accurately (may fix games relying on it) including
  mirroring needed for the Classic NES Series games.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/179ea504d0f29fbf529a21227ce3aaeabd5d73ce/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/179ea504d0f29fbf529a21227ce3aaeabd5d73ce"><tt>179ea50</tt></a>
  You can now dump the GBA frame texture (pre-GPU processing) to "texture_dump.bmp"
  on the root of your SD card by pressing Y.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/ac33d98ad5d03887e0dc1da2a2eab459b33b812c/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/ac33d98ad5d03887e0dc1da2a2eab459b33b812c"><tt>ac33d98</tt></a>
  Fixed broken file browser sorting.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/c87769a06e7dd4e2c11bc485e55f99cacee05b97/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/c87769a06e7dd4e2c11bc485e55f99cacee05b97"><tt>c87769a</tt></a>
  open_agb_firm now remembers the last dir you launched a ROM from.</li>

  </ul>

  <p><strong>This can and will destroy savegames for a few games due to broken save
  type detection so backup your saves!</strong> You have been warned.<br>

  Also note that EEPROM savegames from some emulators or even flashcarts are incompatible
  because they are laid out wrong (every 8 bytes block of data is reversed). This
  <a href="https://gist.github.com/profi200/e06794d7561ed552c518b4b0b2f5f2f6">tool</a>
  can fix that.</p>

  <p>In the archive included are 2 builds. One with BIOS intro and one without. The
  used scale matrix is the default "Sharp interpolated" one.</p>'
updated: '2020-10-26T00:10:31Z'
version: alpha_2020-10-26
version_title: open_agb_firm alpha build 2020-10-26
wiki: https://github.com/profi200/open_agb_firm/wiki
---
