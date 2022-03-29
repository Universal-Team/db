---
author: Nutez
avatar: https://gbatemp.net/data/avatars/l/439/439371.jpg?1618764346
categories:
- utility
- firm
- luma3ds
color: '#957d64'
color_bg: '#806b56'
created: '2020-05-08T09:27:29Z'
description: Return of the customisable screen filter & other QoL improvements
download_page: https://gbatemp.net/download/35619/
downloads:
  luma1030_QuickSwitchers - NightLight .zip:
    size: 196867
    url: https://gbatemp.net/download/luma-10-3-with-night-light-and-quick-switchers.35619/download
github: DullPointer/Luma3DS
icon_index: 183
image: https://gbatemp.net/data/avatars/l/439/439371.jpg?1618764346
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DullPointer/Luma3DS
systems:
- 3DS
title: Luma with Night/Light and Quick-Switchers
update_notes: '<p dir="auto">Official Luma version number bump</p>

  <ul dir="auto">

  <li>Recent official Luma changes e.g. improved system time setting and "Wait for
  B release before exiting rosalina menu".<br>

  -Pixel-Pop''s feature to load custom logo.bin from "/luma/logo.bin" (example: rename
  this file to "logo.bin" or create your own).</li>

  </ul>'
updated: '2022-03-24T20:27:00Z'
version: 10.3 2022-03-24
version_title: Luma 10.3 with Night/Light and Quick-Switchers
website: https://gbatemp.net/download/35619/
---
[Discussion/question thread](https://gbatemp.net/threads/573617/)

[Source](https://github.com/DullPointer/Luma3DS)

### Features:

#### Luma 10.3

- Thank you to the Luma developers [official github](https://github.com/LumaTeam/Luma3DS/wiki)

#### [Redshift](https://gbatemp.net/threads/493736/page-5) custom screen filter (thanks to Sono):

- Tweak screens individually (not possible for o2DS due to single screen hardware)
- Dimming effect for additional brightness reduction
- Much greater range of filter customisation
- Reapplies saved filter on awaken from sleep
- Automatic LED suppression when filter applied

#### Night/Light on-boot screen filters (Sono discovery):

- Apply custom screen filter and adjust brightness on-boot/awaken depending on time of day!
- Access Night/Light Config and Edit Filters via Screen filters menu. Config saved in "/luma/" as "configBootshift.bin", "lightshift.bin" and "nightshift.bin".
- Temporarily disable Night/Light time check via X button in menus. Manual application of screen filters also disables Night/Light.

### Extra Config sub menu to manage optional features:

- Automatically suppress LEDs on boot
- Automatic cut to slot power when booted with DS/TWL game cartridge inserted. This stops DS flashcarts from [leeching power](https://github.com/LumaTeam/Luma3DS/issues/1202#issuecomment-449624237) when not in use. You will need to force boot into DS game cartridge by using the CIA from [here](https://gbatemp.net/threads/414501/), with [TWiLightMenu](https://github.com/DS-Homebrew/TWiLightMenu/releases) or reinsert the cartridge
- Automatic cut 3DS WiFi in sleep mode
- Open Rosalina menu with Home Button
- Toggle bottom LCD backlight from menus with Y button (also exits menu)

#### Quick-Switchers sub menu:

- Quick-Switch between your preferred filters/config for DS/i games ([TwlBg](https://gbatemp.net/threads/542694/)) and GBA games ([AgbBg](https://gbatemp.net/threads/542694/page-71#post-9143128), [open_agb_firm](https://github.com/profi200/open_agb_firm), [Open AGB Launcher](https://gbatemp.net/download/36828/))
- TwlBg option displays ".cxi" files from "/luma/sysmodules/TwlBg" and persists selected file name to "/luma/sysmodules/twlbgName.txt"
- [Widescreen](https://wiki.ds-homebrew.com/twilightmenu/playing-in-widescreen.html) option displays ".cxi" files from "/luma/sysmodules/Widescreen" and persists selected file name to "/luma/sysmodules/widescreenName.txt"
- AgbBg option displays ".cxi" files from "/luma/sysmodules/AgbBg" and persists selected file name to "/luma/sysmodules/agbbgName.txt"
- Open_AGB option displays ".ini" files from "/3ds/open_agb_firm" and persists selected file name to "/3ds/open_agb_firm/configName.txt"
- Works best with meaningful file names e.g. "redshiftWideMode.cxi", "pixelPerfect.cxi", "lowBrightness.ini"
- Delete the .txt file when creating new TwlBg/AgbBg patches to avoid the persisted name being incorrect
- Option to force revert TWiLightMenu widescreen patch

#### Plugin loader:

- All credit to Nanquitas and PabloMK7 and anyone else involved in the CTRPF project!
- Not backwards compatible with .plg or old .3gx
- Supports new CTRPF v0.6.0 and v0.7.0 .3GX format (header 3GX$0002) plugin
- Default plugin available from [CTRPF thread](https://gbatemp.net/threads/487729/page-68#post-9343144) or [Nanquitas' Playground](https://discord.com/invite/z4ZMh27) announcements channel
- "default.3gx" goes in "/luma/plugins" directory

#### Enhanced brightness adjustment interface:

- Adjust brightness of top and bottom screens independently (not possible for o2DS due to single screen hardware)
- Option to use hidden true maximum brightness (at your own risk?)
- Option to use hidden true minimum brightness
- Option to switch off bottom screen backlight entirely

#### Software volume control interface (thanks again to [Sono](https://gbatemp.net/threads/474817/#post-8699169)):

- Accessible from System Configuration sub menu
- Change volume in 1/64 steps without using physical volume slider
- Volume percentage now displayed in sub menus

#### Permanent brightness recalibration:

- Recalibration is applied for 3DS, DS/i and GBA modes
- Accessible from System Configuration sub menu
- Edit the values behind the 5 selectable brightness levels
- Changes are saved to NAND so use sparingly to avoid wearing out the memory
- Upper limit of 172 is found in code so it is presumed to be safe but may reduce LCD lifespan

#### Title specific N3DS settings:

- Automatically launch chosen titles with N3DS 804MHz cpu & L2 cache enabled - option available in N3DS menu when title is running (config file saved to "/luma/n3ds" folder).

#### Misc/QoL:

- Quick toggle LEDs from menus by pressing SELECT
- Quick toggle WiFi from menus by pressing START
- New3DS clock/cache status visible on main menu
- [Allow Patches in the Home Menu](https://github.com/LumaTeam/Luma3DS/pull/1634) e.g. place files from [BetterBatteryColors](https://gbatemp.net/threads/523138/) or another [example](https://gbatemp.net/threads/573617/page-5#post-9540802) in /luma/titles/\*YourRegionHomeMenuTitleId\*/romfs - thank you [gabe565](https://github.com/gabe565)
- Merged in [enhancements](https://github.com/LumaTeam/Luma3DS/pull/1623) to Luma cheats system - thank you [s5bug](https://github.com/s5bug)
- Option to toggle [rehid](https://github.com/hax0kartik/rehid) folder System configuration sub menu (folder must be disabled before loading game to not have rehid apply)