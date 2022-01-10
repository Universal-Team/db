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
  open_agb_firm_alpha_20211224.7z:
    size: 174956
    size_str: 170 KiB
    url: https://github.com/profi200/open_agb_firm/releases/download/alpha_2021-12-24/open_agb_firm_alpha_20211224.7z
github: profi200/open_agb_firm
icon_index: 142
image: https://avatars.githubusercontent.com/u/7831477?v=4
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

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/b09e3a0eeebc3fc494df6a8c98da55573df7b3c3/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/b09e3a0eeebc3fc494df6a8c98da55573df7b3c3"><tt>b09e3a0</tt></a>
  Increased file browser entry limit to 1000 per folder(the real limit depends on
  the average file name length of all files).</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/37f3df4a522e8fcda23b8ee5e4a073b6febf2172/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/37f3df4a522e8fcda23b8ee5e4a073b6febf2172"><tt>37f3df4</tt></a>
  Autoboot support has been added. Place <code>autoboot.txt</code> in <code>/3ds/open_agb_firm</code>
  containing the ROM path in a single line. Example path: <code>sdmc:/rom.gba</code></li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/247cb19cb5cb0722edea7fc1cdb0681743989541/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/247cb19cb5cb0722edea7fc1cdb0681743989541"><tt>247cb19</tt></a>
  All savegames and per-game configs are now stored under <code>/3ds/open_agb_firm/saves</code>.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/15cf1bffd5ac186c2301f30f46ff2b1940b1c947/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/15cf1bffd5ac186c2301f30f46ff2b1940b1c947"><tt>15cf1bf</tt></a>
  Per game config support has been added and with it multiple savegame slot support
  (up to 10). Currently this is the only officially supported config option for games.
  Place <code>romName.ini</code> (replace romName with the ROM file name) in <code>/3ds/open_agb_firm/saves</code>.
  See the <a href="https://github.com/profi200/open_agb_firm#game">README</a> under
  the Game section.</li>

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

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/profi200/open_agb_firm/compare/alpha_2021-12-9...alpha_2021-12-24"><tt>alpha_2021-12-9...alpha_2021-12-24</tt></a></p>'
updated: '2021-12-24T14:52:47Z'
version: alpha_2021-12-24
version_title: open_agb_firm alpha build 2021-12-24
---
