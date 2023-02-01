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
  Luma3DSv11.0.zip:
    size: 390048
    size_str: 380 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v11.0/Luma3DSv11.0.zip
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

  <li>Migrate the configuration to <strong>INI format</strong> (<code class="notranslate">config.bin</code>
  becomes <code class="notranslate">config.ini</code>)

  <ul dir="auto">

  <li>This means that configuration is now human-readable, and makes situations like
  wanting to modify Rosalina''s combo without opening its menu much easier to resolve</li>

  <li>The following options have been removed from the config menu and moved to be
  exclusively in the INI file:

  <ul dir="auto">

  <li>"Splash duration": this is because it can now be configured to take any 32-bit
  value (default: 3 seconds)</li>

  <li>"Set developer UNITINFO",</li>

  <li>"Disable Arm11 exception handlers"</li>

  <li>"Enable Rosalina on SAFE_FIRM"</li>

  </ul>

  </li>

  <li>"Show NAND or user string in System Settings" is now enabled by default, when
  auto-generating a blank configuration file</li>

  </ul>

  </li>

  <li>Essential system files (bootROMs, OTP, HWCAL, LCFS, SecureInfo) are now automatically
  backed up to <code class="notranslate">/luma/backups</code> (upon upgrading Luma3DS,
  if not already present at that location)</li>

  <li>Upon upgrading Luma3DS, <code class="notranslate">boot.firm</code> is now automatically
  copied to the root of the CTRNAND partition</li>

  <li>Restore extended-remote support (this was broken with recent versions of GDB).
  <strong>Breaking change</strong>: use <code class="notranslate">attach &lt;PID+1&gt;</code>
  (e.g 1 for <code class="notranslate">fs</code>) to attach to a process, as GDB doesn''t
  support PID 0.</li>

  <li>Add option to toggle card slot (<a aria-label="Issue #1202" class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="379507464" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1202" data-hovercard-type="issue"
  data-hovercard-url="/LumaTeam/Luma3DS/issues/1202/hovercard" href="https://github.com/LumaTeam/Luma3DS/issues/1202">#1202</a>)</li>

  <li>Screen filters can now be saved to <code class="notranslate">config.ini</code>
  and restored at boot (you need to go to "Miscellaneous options &gt; Save settings").
  You can now even manually edit <code class="notranslate">config.ini</code> to use
  custom values for those (within the 1000 to 25100K range)</li>

  <li>NTP timezone can also now be saved to <code class="notranslate">config.ini</code>;
  also fix a bug where some timezones would not be reachable</li>

  <li>Fix a long-standing issue where some system calls took longer than they should,
  causing lags in some situations (thanks <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/PabloMK7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/PabloMK7">@PabloMK7</a>)</li>

  <li>Fix calculation of displayed battery voltage (thanks nocash)</li>

  </ul>'
updated: '2022-06-04T23:27:32Z'
version: v11.0
version_title: v11.0
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
