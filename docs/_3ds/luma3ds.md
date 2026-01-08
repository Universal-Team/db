---
author: LumaTeam
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/65085206?v=4
categories:
- utility
- firm
color: '#82e5d9'
color_bg: '#488079'
created: '2016-02-08T02:26:12Z'
description: Nintendo 3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases
downloads:
  Luma3DSv13.3.3.zip:
    size: 551822
    size_str: 538 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v13.3.3/Luma3DSv13.3.3.zip
github: LumaTeam/Luma3DS
image: https://avatars.githubusercontent.com/u/65085206?v=4&size=128
image_length: 7260
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LumaTeam/Luma3DS
stars: 6128
systems:
- 3DS
title: Luma3DS
update_notes: '<ul dir="auto">

  <li>Fix screen-flickering and burn-in issues sometimes happening on IPS screens
  (usually after using the splash screen feature)

  <ul dir="auto">

  <li>This was caused by the very old code we were using disabling PWM and signal
  on screen "deinit" but forgetting to cut off the voltage to the LCD panel and to
  the backlight(s), causing official driver to misdetect state. This is now fixed</li>

  <li>Improved LCD controller initialization. While some technical debt remains, this
  fix should cover the vast majority of issues people were having</li>

  </ul>

  </li>

  <li>In "Change screen brightness" submenu, fix limit calculation errors. Additionally,
  because the underlying GSP allows it, <strong>allow luminance slightly above preset
  5</strong>

  <ul dir="auto">

  <li>This is because the fact that even though only the OG O3DS model has a feature
  where luminance is increase when plugging the adapter in, all models have an extra
  (unused) brigthness level provisioned for this</li>

  </ul>

  </li>

  <li>Fix N3DS-only issue where using "DSi Autoboot" + power-saving mode both enabled
  would lead to the DSi software "rave party" effects

  <ul dir="auto">

  <li>This is fixed by zerofilling N3DS-only adaptive backlight registers that are
  active even when the SoC is in O3DS mode, contrary to what Nintendo''s drivers expect
  (and thus leave the registers uninitialized in TWL_ and AGB_FIRM). This bug can
  only happen with Luma3DS''s "autoboot" feature as the registers <em>are</em> initialized
  by NATIVE_FIRM and survive reboot</li>

  </ul>

  </li>

  <li>Further improvements to overall system stability and other minor adjustments
  have been made to enhance the user experience</li>

  </ul>'
updated: '2025-07-15T19:36:12Z'
version: v13.3.3
version_title: v13.3.3
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
