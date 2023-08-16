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
  Luma3DSv13.0.1.zip:
    size: 419052
    size_str: 409 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v13.0.1/Luma3DSv13.0.1.zip
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

  <li>Fix a v13.0 regression where external FIRM module loading (such as TwlBg) was
  broken</li>

  </ul>

  <p dir="auto"><strong>v13.0 changelog:</strong></p>

  <ul dir="auto">

  <li><strong>Merged <a href="https://github.com/PabloMK7/Luma3DS_3GX">@PabloMK7 and
  @Nanquitas ''s fork</a>, adding plugin support. This allows mods like CTGP-7 to
  be played</strong>

  <ul dir="auto">

  <li>NOTE: Due to planned changes (such as kernel reimplementation) older no longer
  maintained plugins or closed source ones may suddenly stop working at some point
  in the future. We advise to use open source and/or actively maintained plugins from
  trusted sources instead</li>

  </ul>

  </li>

  <li><strong>Added support to replace the default TWL_FIRM (i.e. DS(i) software)
  convolution-based upscaling filter by the contents of <code class="notranslate">/luma/twl_upscaling_filter.bin</code></strong>

  <ul dir="auto">

  <li>You can find matrix examples <a href="https://github.com/DullPointer/TWPatch_a/blob/master/soos/krnlist_all.h#L192">here</a>
  and Python code to convert them to the expected format <a href="https://github.com/LumaTeam/Luma3DS/blob/master/arm9/source/patches.c#L774">there</a></li>

  </ul>

  </li>

  <li>Added support to allow Left+Right and Up+Down key combos in TWL_FIRM, although
  commercial DS(i) games usually prevent these combos on their own too</li>

  <li>Added support for arbitrarily-sized and uncompressed TWL_FIRM and AGB_FIRM,
  when externally loaded from the <code class="notranslate">/luma</code> folder</li>

  <li>Simplify sysmodule CXI loading and IPS/BPS patching: N3DS bit is now cleared
  when considering which CXI file to load from <code class="notranslate">/luma/sysmodules</code>.
  The path for IPS/BPS patches for sysmodules, and sysmodules only, has been moved
  to <code class="notranslate">/luma/sysmodules/&lt;titleId without N3DS bit&gt;.ips</code>
  (resp. <code class="notranslate">.bps</code>). This is a breaking change</li>

  <li>Remove the "Use EmuNAND FIRM if booting with R" option and all related logic.
  This was a leftover of the Gateway era that has no place in 2023</li>

  <li>Fixed a rare bug where the console would boot into 2 white screens</li>

  <li>Other minor changes</li>

  </ul>'
updated: '2023-07-21T09:40:52Z'
version: v13.0.1
version_title: v13.0.1
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
