---
author: badda71
avatar: https://avatars.githubusercontent.com/u/11392517?v=4
categories:
- emulator
color: '#a4897c'
color_bg: '#806b60'
created: '2020-02-18T23:04:48Z'
description: Port of Chui's UAE4ALL Amiga 500 emulator to Nintendo 3DS
download_page: https://github.com/badda71/uae3DS/releases
downloads:
  uae3DS.3dsx:
    size: 2478228
    size_str: 2 MiB
    url: https://github.com/badda71/uae3DS/releases/download/1.0/uae3DS.3dsx
  uae3DS.cia:
    size: 1975232
    size_str: 1 MiB
    url: https://github.com/badda71/uae3DS/releases/download/1.0/uae3DS.cia
github: badda71/uae3DS
icon: https://raw.githubusercontent.com/badda71/uae3DS/master/meta/icon.png
image: https://raw.githubusercontent.com/badda71/uae3DS/master/meta/banner.png
image_length: 28872
layout: app
qr:
  uae3DS.cia: https://db.universal-team.net/assets/images/qr/uae3ds-cia.png
script_message: 'You will need a "kick.rom" file in sdmc:/3ds/uae3DS.


  It must be called "kick.rom", be a kickstart 1.3 image,

  and be the 512KB overdumped version.'
source: https://github.com/badda71/uae3DS
systems:
- 3DS
title: uae3DS
update_notes: '<p dir="auto">This is the first (hopefully) stable version of uae3DS,
  the Amiga 500 emulator for Nintendo 3DS.<br>

  Save state handling changed a bit, so if you''re upgrading from a previous version,
  you need to migrate your save state files (*.asf):</p>

  <ol dir="auto">

  <li>Move all save state files to directory /3ds/uae3DS/save/ on your SD card</li>

  <li>Rename the files to <code class="notranslate">&lt;ADF file name&gt;-&lt;NR&gt;.asf</code>
  where <code class="notranslate">&lt;ADF file name&gt;</code> is the name of the
  disc image in drive DF0 at the time of writing the state file and <code class="notranslate">&lt;NR&gt;</code>
  is the save state number (0 - 3), e.g. <code class="notranslate">Chaos Engine, The_Disk1.adf-0.asf</code></li>

  </ol>

  <p dir="auto"><strong>Installation:</strong></p>

  <ul dir="auto">

  <li>Put your kick.rom file in directory /3ds/uae3DS on your 3DS SD-card. It must
  be called kick.rom, be a kickstart 1.3 image, and be the 512KB overdumped version.</li>

  <li>Install CIA with <a href="https://github.com/Steveice10/FBI/releases">FBI</a>,
  run 3dsx from homebrew launcher (put 3dsx file in /3ds/uae3DS dir) or run 3ds from
  flash card.<br>

  Apart from this, a DSP-dump is required for sound to work correctly in the CIA version.<br>

  <a href="https://gbatemp.net/threads/dsp1-a-new-dsp-dumper-cia-for-better-stability.469461/"
  rel="nofollow">https://gbatemp.net/threads/dsp1-a-new-dsp-dumper-cia-for-better-stability.469461/</a></li>

  </ul>

  <p dir="auto"><strong>Emulator usage:</strong></p>

  <ul dir="auto">

  <li>SELECT: open menu</li>

  <li>START: Toggle SuperThrottle</li>

  <li>Bottom Screen: Virtual Keyboard / Touchpad (tap-to-click, double-tap-to-double-click,
  tap-and-drag)</li>

  <li>A button: joystick fire</li>

  <li>B button: joystick UP</li>

  <li>R button: joystick autofire</li>

  <li>X button / ZL-button / tap touchpad: left mouse button</li>

  <li>Y button / L button: right mouse button</li>

  <li>DPad: joystick</li>

  <li>CPad: joystick or mouse (configurable in menu)</li>

  <li>CStick up/down: adjust vertical image position</li>

  <li>CStick left/right: adjust zoom</li>

  </ul>

  <p dir="auto"><strong>Menu usage:</strong></p>

  <ul dir="auto">

  <li>CPad / DPad: Navigate cursor</li>

  <li>A button: select current entry</li>

  <li>B button: cancel / back</li>

  <li>X button: delete save state in "Load state"-menu</li>

  <li>other button functions given in parentheses in menu</li>

  </ul>

  <p dir="auto"><a href="https://gbatemp.net/threads/release-uae3ds-amiga-500-emulator-for-nintendo-3ds.558577/"
  rel="nofollow">https://gbatemp.net/threads/release-uae3ds-amiga-500-emulator-for-nintendo-3ds.558577/</a></p>

  <p dir="auto"><strong>Changes to last release are:</strong></p>

  <ul dir="auto">

  <li>enhancement: Save state handling revamp: screenshots, config saved in save states,
  ...</li>

  <li>enhancement: SHIFT, Amiga &amp; ALT keys now differentiate left and right press</li>

  <li>enhancement: option to move mouse with C-Pad, configurable in main menu</li>

  <li>enhancement: added list of 10 last used disk images in "Load disk image"-menu</li>

  <li>optimization: settings are autosaved on exit</li>

  <li>optimization: removed sound settings from main menu</li>

  <li>bugfix: fixed sound speed</li>

  <li>lots of other small optimizations and bugfixes</li>

  </ul>

  <p dir="auto">Have fun!</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/11392517/85423689-49ac8480-b577-11ea-9693-440e3d212b8c.png"><img
  src="https://user-images.githubusercontent.com/11392517/85423689-49ac8480-b577-11ea-9693-440e3d212b8c.png"
  alt="grafik" style="max-width: 100%;"></a></p>'
updated: '2020-06-23T15:01:36Z'
version: '1.0'
version_title: uae3DS v1.0 Pancit
website: https://gbatemp.net/threads/release-uae3ds-amiga-500-emulator-for-nintendo-3ds.558577/
---
Port of Chui's UAE4ALL Amiga 500 emulator (http://chui.dcemu.co.uk/uae4all.html) to Nintendo 3DS