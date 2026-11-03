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
  Luma3DSv13.5.zip:
    size: 545619
    size_str: 532 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v13.5/Luma3DSv13.5.zip
github: LumaTeam/Luma3DS
image: https://avatars.githubusercontent.com/u/65085206?v=4&size=128
image_length: 7217
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
source: https://github.com/LumaTeam/Luma3DS
stars: 6837
systems:
- 3DS
title: Luma3DS
update_notes: '<p dir="auto">This release of Luma3DS brings many quality-of-life improvements
  and lays the groundwork for future releases.</p>

  <p dir="auto">First, several settings have been moved from <code class="notranslate">config.ini</code>
  to unused MCU registers. These settings can now be changed directly through Rosalina
  and are <strong>saved automatically</strong>. Some of them are new:</p>

  <ul dir="auto">

  <li>"Enhance top/bottom screen colors" in the Screen Filters menu</li>

  <li>Audio routing (automatic, force speakers, force headphones)</li>

  <li>Volume slider override and left/right audio balance</li>

  <li>LED master brightness override (0% to 100%)</li>

  <li>Celsius/Fahrenheit toggle for battery temperature</li>

  </ul>

  <p dir="auto">Now, the rest of the changelog:</p>

  <ul dir="auto">

  <li>Rosalina: significant improvements to screen filters:

  <ul dir="auto">

  <li>

  <strong>Add support for per-channel (red, green, blue) gamma and contrast adjustments</strong>,
  allowing for more precise screen color calibration</li>

  <li>By continuity in gamma, we now define <math-renderer class="js-inline-math"
  style="display: inline-block" data-run-id="1c10105eb58813c920330b8cf62deb1d">$0^0
  = 0$</math-renderer>, as this provides a useful result instead of turning the entire
  screen white</li>

  <li>Greatly optimize color correction LUT generation (from ~700 µs to ~75 µs), and
  synchronize LUT writes with VBlank to prevent graphical glitches</li>

  <li>Remove the "brightness" adjustment from advanced screen filter settings as it
  prevents optimization</li>

  </ul>

  </li>

  <li>Rosalina: rework and extend several options in the "System configuration" menu

  <ul dir="auto">

  <li>Rework "Control volume" into "Set volume slider override...", adding stereo
  balance control (left/right, for I2S1 audio)

  <ul dir="auto">

  <li>The UI for this has been reworked</li>

  <li>Audio balance can only apply if the override is enabled, <em>and does not apply
  to applets</em> (I2S2)</li>

  </ul>

  </li>

  <li>Add "Set audio routing..." to force audio output through speakers or headphones,
  or leave it on automatic</li>

  <li>Replace "Toggle LEDs" with "Set LED master brightness override...", allowing
  brightness adjustment from 0% to 100%

  <ul dir="auto">

  <li>The red POWER LED is not dimmable. While it can be disabled, we deliberately
  leave it on even at 0% to allow the user to be notified of the battery level being
  low</li>

  <li>The "charging" LED is not dimmable</li>

  <li>Setting LED brightness to 0% also keeps the LEDs off during sleep, except for
  the red POWER LED and the charging LED. Otherwise, the usual "breathing" pattern
  (alternating between 4% and 100% brightness) is used</li>

  </ul>

  </li>

  </ul>

  </li>

  <li><strong>Rosalina: display the current date and time in the top-right corner
  of the menu when the IP address isn''t being displayed</strong></li>

  <li>Rosalina: add an option to display the battery temperature in Fahrenheit instead
  of Celsius</li>

  <li>Loader: improve game and sysmodule patching:

  <ul dir="auto">

  <li>

  <strong>Add support for UPS patches</strong> (<code class="notranslate">code.ups</code>),
  in addition to IPS and BPS patches. Note that UPS CRC checks are currently skipped</li>

  <li>

  <strong>Massively speed up IPS patch loading</strong>, especially for patches containing
  large numbers of small records (from several minutes to less than 50 ms in some
  cases)</li>

  <li>Improve IPS handling of file size changes, zero-filled gaps, and the optional
  size field after the EOF marker</li>

  <li>Properly propagate the resulting code size between BPS, IPS and UPS patches,
  allowing multiple patches to be applied together (the application order is deliberately
  unspecified and should not be relied upon)</li>

  <li>Fix BPS patches failing on sysmodules due to excessive temporary memory allocation</li>

  </ul>

  </li>

  <li>Improve 3DS homebrew autoboot:

  <ul dir="auto">

  <li>Use the HOME Menu reboot mechanism by default, instead of directly launching
  the configured title through NS</li>

  <li>This fixes issues with the HOME/POWER buttons when using non-default application
  memory layouts, and allows normal booting if the configured title cannot be found</li>

  <li>

  <strong>Note:</strong> Due to a bug in older versions of libctru, using memory modes
  that provide more RAM to applications (such as Dev1) requires rebuilding homebrew
  applications with libctru v2.7.1 or later. The Homebrew Menu (<code class="notranslate">boot.3dsx</code>)
  included in this release archive has already been built with a compatible version</li>

  <li>The previous behavior can still be enabled through <code class="notranslate">autoboot_3ds_use_ns
  = 1</code> in <code class="notranslate">config.ini</code>

  </li>

  </ul>

  </li>

  <li>LayeredFS: Fix patching of games that do not contain the <code class="notranslate">fsUnmountArchive</code>
  symbol, such as <em>Metroid: Samus Returns</em> (by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/R-YaTian/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/R-YaTian">@R-YaTian</a>,
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4501738684"
  data-permission-text="Title is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/2245"
  data-hovercard-type="pull_request" data-hovercard-url="/LumaTeam/Luma3DS/pull/2245/hovercard"
  href="https://github.com/LumaTeam/Luma3DS/pull/2245">#2245</a>)</li>

  <li>Plugin loader: Fix issues with plugin cleanup on process termination, which
  could leave plugin memory mapped and prevent subsequent applications from starting</li>

  <li>This release archive ships with an updated <code class="notranslate">cacert.pem</code>
  which does not contain the compromised eMudhra and Sectigo certificates. <code class="notranslate">cacert.pem</code>
  is used by homebrew that uses cURL</li>

  <li>Further improvements to overall system stability and other minor adjustments
  have been made to enhance the user experience</li>

  </ul>'
updated: '2026-11-02T00:07:07Z'
version: v13.5
version_title: v13.5
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>boot.firm</summary>
<ol>
<li>Download <code>Luma3DSv13.5.zip</code></li>
<li>Extract <code>/boot.firm</code> from the zip to <code>/boot.firm</code> on your SD card</li>
<li>Extract <code>/config</code> from the zip to <code>/config</code> on your SD card</li>
</ol>
</details>

