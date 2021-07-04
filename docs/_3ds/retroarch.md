---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.6/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: 72377914
    size_str: 69 MiB
    url: https://buildbot.libretro.com/stable/1.9.6/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: 72974048
    size_str: 69 MiB
    url: https://buildbot.libretro.com/stable/1.9.6/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
image: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/libretro_banner.png
image_length: 3154
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/libretro/RetroArch
systems:
- 3DS
title: RetroArch
update_notes: '<ul>

  <li>ARCHIVE: Fix archive delimiter detection when file path contains no slashes</li>

  <li>ANDROID: Do not duplicate port 0 mouse and gun inputs to other ports</li>

  <li>AUDIO/XAUDIO2: Fail instead of crashing when disconnecting an audio device</li>

  <li>CHEEVOS: Reset cached progress each time menu is opened</li>

  <li>CRT/SWITCHRES: Add support for switchres.ini core and directory overrides</li>

  <li>D3D11: Don''t use allow tearing flag with blit swap chains. Also disables the
  flip model if the allow tearing flag is not supported.</li>

  <li>D3D11: Disable DXGI''s ALT+ENTER handling</li>

  <li>D3D11: Don''t pass ALLOW_TEARING when unsupported</li>

  <li>D3D11: Fix non-vsynced output without flip, black screens in fullscreen</li>

  <li>D3D12: Relocated ''d3d12_gfx_sync''</li>

  <li>D3D12: Fixed swap interval option</li>

  <li>GFX: Fix uninitialized variables in gfx_display_draw_cursor</li>

  <li>HISTORY: Hide ''Add to Favorites'' when viewing an entry of the favorites playlist</li>

  <li>INPUT: ''Analog to Digital Type'' usability improvements</li>

  <li>INPUT: Add support for mapping multiple controllers to a single input device</li>

  <li>INPUT/REMAPPING: Add support for mapping multiple controllers to a single input
  device</li>

  <li>INPUT/LIGHTGUN: Bind lightgun trigger to first mouse button by default</li>

  <li>INPUT/WINDOWS/RAWINPUT: Mouse access violation fix</li>

  <li>INPUT/UDEV: Only add mouse if it has buttons and add vebose device friendly
  names</li>

  <li>INPUT/UDEV: Skip mouse with no button errors and keep the rest</li>

  <li>INPUT/UDEV: Fix Game Focus mode</li>

  <li>INPUT/UDEV/X11: Change udev driver for dual lightgun support in X11</li>

  <li>LIBNX/SWITCH: Update to libnx 4.0.0</li>

  <li>LOCALIZATION: Fetch translations from Crowdin</li>

  <li>LOCALIZATION: Fix Switchres menu texts</li>

  <li>MENU/OZONE: Ensure sidebar display status is updated correctly when performing
  rapid menu navigation</li>

  <li>MENU/XMB: Dynamic wallpaper fix</li>

  <li>MENU/XMB: Icon opacity fix</li>

  <li>MENU/QT/WIMP: Fix default core detection when playlist file name does not match
  ''db_name''</li>

  <li>PLAYLISTS: Optimise scanning of large rom sets</li>

  <li>SECURITY: Plug so-called high-risk vulnerability related to Powershell - avoid
  injection - don''t send speech input as commandline argument</li>

  <li>UWP/XBOX: Add expanded resources Rescap to increase performance of UWP version
  in app mode on Xbox</li>

  <li>WINDOWS/INSTALLER: Add smarter isEmptyDir reference implementation that looks
  for subdirectories from NSIS documentation</li>

  <li>WINDOWS/INSTALLER: Register new function DirectorySet that is called when pressing
  the "Next" button on the MUI_PAGE_DIRECTORY, aka the install folder selection GUI.
  DirectorySet contains the criteria for an acceptable folder, which are:

  <ul>

  <li><code>IfFileExists "$INSTDIR\retroarch.exe"</code> returns 1</li>

  <li><code>IfFileExists "$INSTDIR\*.*</code> returns 0, there is no existing folder</li>

  <li><code>IfFileExists "$INSTDIR\*.*"</code> returns 1, there is a folder, and <code>isEmptyDir</code>
  returns 1, therefore the folder is empty, including of subdirectories</li>

  </ul>

  </li>

  <li>X11: Fix threaded video segfault</li>

  </ul>'
updated: '2021-07-04T00:40:35Z'
version: v1.9.6
version_title: v1.9.6
website: http://www.libretro.com
---
