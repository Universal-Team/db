---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.14/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: 73704675
    size_str: 70 MiB
    url: https://buildbot.libretro.com/stable/1.9.14/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: 74195684
    size_str: 70 MiB
    url: https://buildbot.libretro.com/stable/1.9.14/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
icon_index: 161
image: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/libretro_banner.png
image_length: 3154
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://buildbot.libretro.com/nightly/nintendo/3ds/
  downloads:
    RetroArch_3dsx.7z:
      url: https://buildbot.libretro.com/nightly/nintendo/3ds/RetroArch_3dsx.7z
    RetroArch_cia.7x:
      url: https://buildbot.libretro.com/nightly/nintendo/3ds/RetroArch_cia.7z
source: https://github.com/libretro/RetroArch
systems:
- 3DS
title: RetroArch
update_notes: '<ul dir="auto">

  <li>ANDROID/PLAYSTORE: Implement MANAGE_EXTERNAL_STORAGE permission</li>

  <li>ANDROID/PLAYSTORE: Bump up SDK level to 30 to comply with Play Store policies</li>

  <li>AUDIO/MIXER: Increase sample buffer padding</li>

  <li>CHEEVOS: Disallow achievements when spectating netplay</li>

  <li>CHEEVOS: Fix need-to-activate achievement logic for non-hardcore</li>

  <li>CHEEVOS: Don''t queue rewind re-init if already on main thread</li>

  <li>CHEEVOS: Ignore unofficial achievements unless setting is enabled</li>

  <li>CHEEVOS: Use SSL host when available</li>

  <li>CHEEVOS: Validate hashes for secondary discs in multi-disc games</li>

  <li>CHEEVOS: Ensure placard is initialized on main thread when game has no achievements</li>

  <li>CHEEVOS: Audit achievement settings defaults and visibility</li>

  <li>CHEEVOS: Show error message when no password provided</li>

  <li>CHEEVOS: Use widget for game loaded achievement progress</li>

  <li>CONFIG: Honor config_save_on_exit when Reboot/Shutdown is called</li>

  <li>DISK CONTROL: Focus on current content entry in Disk Control append/insert</li>

  <li>FRAMEDELAY: Auto Frame Delay Improvements - swap interval handling, D3DX handling,
  and delay target resets also on core restart. It should now work with high refresh
  rates and also with Direct3D 10/11/12 drivers</li>

  <li>INPUT/GYRO/ACCELEROMETER/ANDROID: Re-enable Gyroscope &amp; Accelerometer when
  RetroArch resumes or regains focus</li>

  <li>INPUT/HID: Fix gamepad disconnect on unrecognized HID device</li>

  <li>LAKKA: Patch to fix keyboard typing</li>

  <li>LAKKA: CD-ROM eject menu item</li>

  <li>LAKKA/BLUETOOTH: Add option to remove pairing</li>

  <li>LAKKA/SWITCH: Disable rumble gain</li>

  <li>LAKKA/SWITCH: Disable cpu scaling, uses its own CPU governor</li>

  <li>LOGGING: Logging cleanups. A bunch of unifications and reformattings (capitalizations,
  dots, quotes, prefixes etc). Also added a few missing things, such as Run-Ahead
  error logging and LED interface init logging when it is enabled.</li>

  <li>NETPLAY: Networking - should not print country for a local lobby</li>

  <li>NETPLAY: Added setting to allow/disallow players other than the host from pausing
  the game.</li>

  <li>NETPLAY: Added a sublabel for netplay max connections.</li>

  <li>NETPLAY: Fixed port override macro from not being set immediately after the
  port setting.</li>

  <li>NETPLAY: Show passworded rooms on lobby</li>

  <li>NETWORK: Make HTTP header parsing case insensitive</li>

  <li>NETWORK/UPNP: Fixed memory leaks</li>

  <li>NETWORK/UPNP: Added a task_queue_wait to prevent executing two nat tasks at
  once, so it''s also thread safe now</li>

  <li>NETWORK/UPNP: Switch to a permanent lease time, but request it to be removed
  when we do netplay_free. Switch to a permanent lease time, but request it to be
  removed when we do netplay_free.</li>

  <li>NETWORK/UPNP: Only use a single interface for UPnP, return on the first one
  found instead of iterating over all of them and opening them one by one</li>

  <li>OVERLAYS: Revert changes</li>

  <li>RETROFW: Add OSS audio</li>

  <li>VIDEO/ROTATION: Always return false if rotation can''t occur. RETRO_ENVIRONMENT_SET_ROTATION
  should return false when rotation has been forcefully disabled in frontend, that
  way the core can decide if aspect ratio should be rotated or not for vertical games.
  Useful for FBNeo for instance.</li>

  <li>VULKAN: Avoid hard crash when capturing screenshot in emulating mailbox.</li>

  <li>WIIU: Make wiiu_gfx_load_texture code safer</li>

  <li>WIIU: Fix keyboard support.</li>

  </ul>'
updated: '2021-12-05T23:06:30Z'
version: v1.9.14
version_title: v1.9.14
website: http://www.libretro.com
wiki: https://github.com/libretro/RetroArch/wiki
---
