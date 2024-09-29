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
description: Nintendo 3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases
downloads:
  Luma3DSv13.2.zip:
    size: 546724
    size_str: 533 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v13.2/Luma3DSv13.2.zip
github: LumaTeam/Luma3DS
image: https://avatars.githubusercontent.com/u/65085206?v=4&size=128
image_length: 7260
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LumaTeam/Luma3DS
stars: 5228
systems:
- 3DS
title: Luma3DS
update_notes: '<ul dir="auto">

  <li>Add "System Information" Rosalina submenu, displaying various system information,
  in particular screen types (TN/IPS, for each screen)</li>

  <li>In Rosalina''s "Screen Filters" submenu, add a new option to "fix" the top screen''s
  color curve. This <strong>significantly</strong> improves the color output of <strong>IPS</strong>
  top screens, bringing them fairly close to normal sRGB displays (though the colors
  will look slightly dimmer):

  <ul dir="auto">

  <li>all 3DS screens (TN and IPS) are calibrated to a color curve unique to 3DS systems
  that accomodates the TN screens'' poor color gamut</li>

  <li>this option is hit-and-miss on TN screens and often leads to weird results.
  This is because TN screens on 3DS have terrible color gamut, in particular in the
  greens and yellows, even by 2011 standards (and 3DS TN screens have much worse response
  time than 3DS IPS screens, as well)</li>

  <li>this does not fix the black crush on 3DS IPS screens, in some instances this
  might make it slightly worse</li>

  <li>this option can be persisted in Luma3DS config via "Save settings"</li>

  <li>open_agb_firm has the same feature, this is where the LUT used here comes from</li>

  </ul>

  </li>

  <li>Following <a href="https://github.com/devkitPro/libctru/commit/8e55cdf05d1f2c07f350ec678d0f0d6a7a2df214">my
  reverse engineering work on QTM</a> (face tracking, super-stable 3D), in the "New
  3DS" Rosalina submenu:

  <ul dir="auto">

  <li>add a submenu to temporarily enable/disable the "super-stable 3D" (SS3D) feature
  of New 3DSes. The changes made there do not persist, to change the behavior at boot,
  you should still go to System Settings like before</li>

  <li>add a submenu to test all 12 parallax barrier positions used when SS3D is active.
  Changes revert when exiting the submenu</li>

  <li>add a submenu to calibrate SS3D. Even though System Settings has a similar function,
  this has fewer limitations and displays more information about the process on screen</li>

  </ul>

  </li>

  <li>Reorder Rosalina menu top screen entries to facilitate usage of the most commonly
  used options; merge "Power off" and "Reboot" into a single menu</li>

  <li>Allow plugins to use PRIVATE memory instead of SHARED on requests (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2553275060" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/2086" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/2086/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/2086">#2086</a>,
  bug report and original PR thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/LittlestCube/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/LittlestCube">@LittlestCube</a>).
  This allows plugins to access the network more easily. Only download plugin from
  trusted sources.</li>

  <li>During the "first time booting Luma3DS/Luma3DS upgrade" process, create the
  payloads directory if it does not exist. This should make the 3DS hacking process
  even more streamlined</li>

  <li>Further improvements to overall system stability and other minor adjustments
  have been made to enhance the user experience</li>

  </ul>'
updated: '2024-09-27T22:00:09Z'
version: v13.2
version_title: v13.2
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
