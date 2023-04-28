---
author: LumaTeam
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/65085206?v=4
categories:
- utility
- firm
- luma3ds
color: '#82e5d9'
color_bg: '#488079'
created: '2016-02-08T02:26:12Z'
description: Noob-proof (N)3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases
downloads:
  Luma3DSv12.0.zip:
    size: 395119
    size_str: 385 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v12.0/Luma3DSv12.0.zip
github: LumaTeam/Luma3DS
image: https://avatars.githubusercontent.com/u/65085206?v=4&size=128
image_length: 7260
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LumaTeam/Luma3DS
systems:
- 3DS
title: Luma3DS
update_notes: '<ul dir="auto">

  <li><strong>Add a new "advanced configuration" submenu for screen filters, allowing
  for far more customization (notably, increasing gamma)</strong>. It allows setting
  different filters for top and bottom screen separately, and all settings can be
  saved to the ini configuration file</li>

  <li><strong>Implement autobooting into Homebrew Menu, both in 3DS mode and in DSi
  mode:</strong>

  <ul dir="auto">

  <li>DSi modes uses <a href="https://github.com/devkitPro/nds-hb-menu/releases/latest">nds-hb-menu
  bootstrap</a>''s TID by default, and is a bit slow to start as it needs to go through
  the native 3DS OS first no matter what</li>

  <li>Homebrew needs to be compiled with libctru v2.0.0 at a minimum, and libctru
  v2.1.2 is highly recommended to a bug fix</li>

  </ul>

  </li>

  <li><strong>Move "Save settings" to top-level menu</strong></li>

  <li>Add ability to force routing audio to headphones. This is targeted to Bluetooth
  hardware mod users

  <ul dir="auto">

  <li>One limitation is that this option gets undone if you actually insert then remove
  headphones in the headphones port, closing and re-opening the lid fixes this</li>

  </ul>

  </li>

  <li>Add ability to redirect application core1 threads to core2, on N3DS:

  <ul dir="auto">

  <li>Only useful in very demanding games like Pokémon (Ultra) Sun/Moon where it nets
  approx. a 10% gain, due to how the 3DS OS works</li>

  <li>Might break some games and homebrew applications</li>

  </ul>

  </li>

  <li>Add external *.cxi non-KIP sysmodule loading (from <code class="notranslate">/luma/sysmodules</code>),
  when the "Enable loading external FIRMs and modules" option is enabled

  <ul dir="auto">

  <li>The expected format is {titleId}.cxi (not the name, unlike KIPs), with {titleId}
  being a string of 16 hexadecimal digits, and with the N3DS bit taken into account</li>

  <li><code class="notranslate">code.bin</code> loading for sysmodules is still kept
  as a feature, but you now need to enable both this option and "Enable game patching"
  (for non-sysmodules only "Enable game patching" suffices)</li>

  </ul>

  </li>

  <li>Enable "game patching" features for all applets (not extensively tested), not
  just games or applications. This being said, LayeredFs might not work on things
  like the software keyboard, but "locale emulation" is expected to always work</li>

  <li>Remove kernel check for creating core2/core3 threads. This has no bearing on
  homebrew being able to access core2, as it always has had the proper access bits.
  Moreover, you should not create threads on core3 as head-tracking takes most of
  the CPU time there &amp; the graphics driver depends on head-tracking</li>

  <li>Grant full DSP RAM access to all 3dsx homebrew</li>

  <li>Move <code class="notranslate">hb:ldr</code> from Rosalina to loader reimplementation</li>

  <li>Add disabled-by-default PASLR support in our custom loader reimplementation;
  this should match what the official sysmodule does 1:1</li>

  <li>Fix a bug where an error telling the MCU firmware version was too low, even
  if this was always incorrect</li>

  <li>Fix a very long-standing bug where sysmodules could incorrectly be killed when
  using the "Switch the hb. title to the current app." feature followed by closing
  the current app. This might have been causing issues with this feature and N3DS
  Health&amp;Safety app in the past</li>

  <li>Display the proper error messages when removing the gamecart or the SD card
  while playing a game on either medium, instead of a cryptic error code. Also add
  datetime information to <code class="notranslate">errdisp.txt</code> entries</li>

  <li>General system stability improvements to enhance the user''s experience</li>

  </ul>

  <p dir="auto">(libctru v2.1.2 and 3ds-hbmenu v2.4.1 will officially release later
  this week)</p>'
updated: '2023-02-09T01:33:55Z'
version: v12.0
version_title: v12.0
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
