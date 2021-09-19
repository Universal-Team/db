---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.10/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    size: 72886162
    size_str: 69 MiB
    url: https://buildbot.libretro.com/stable/1.9.10/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    size: 73419865
    size_str: 70 MiB
    url: https://buildbot.libretro.com/stable/1.9.10/nintendo/3ds/RetroArch_cia.7z
eval_downloads: true
eval_notes_md: true
github: libretro/RetroArch
icon: https://raw.githubusercontent.com/libretro/RetroArch/master/pkg/ctr/assets/default.png
icon_index: 162
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
update_notes: '<ul>

  <li>3DS: Add bottom screen idle state</li>

  <li>3DS: Add unique IDs for Gearboy/Gearcoleco/Gearsystem, correct CAP32 code</li>

  <li>3DS/SAVESTATES: Fix RAM states to file when core deinits</li>

  <li>AUDIO/MIXER: Pad sample buffers to prevent potential heap-buffer-overflows when
  resampling (fixes crash when using 30 kHz menu audio files)</li>

  <li>AUDIO/LINUX/SNAP: Add JACK support</li>

  <li>CHEEVOS: Don''t write achievement credentials to overrides</li>

  <li>CHEEVOS: Disable slowmotion when enabling hardcore mode</li>

  <li>D3D9: Fixed MVP matrix issue for RGUI texture (main game frame still won''t
  show up though)</li>

  <li>D3D11/D3D12/HDR: Fixed contrast to be more correct - now scales from 0-10 linearly
  and behaves more the way you''d expect it to - changed name to ditch legacy settings
  users may have</li>

  <li>D3D11/HDR: Fixed D3D11''s blend, rasterizer and topology states not being set
  to the sames when using HDR and leaving the menu - caused issues with PCSX2''s Shadow
  of the Colossus</li>

  <li>D3D11/D3D12/HDR: Added ability to skip inverse tonemapper to the shader via
  the constant buffer using ''inverse_tonemap'' - set to 0.0f to skip</li>

  <li>D3D11/D3D12/HDR: Fixed potential bug when swapping between hdr and sdr and the
  bit depth not being set correctly</li>

  <li>D3D11/D3D12/HDR: Added numerous helper functions to help create the correct
  values to colour the UI - normally the white UI elements should be rendered at paper
  white not max brightness for various reasons</li>

  <li>BUGFIX/ANDROID: Fix crash that could happen on Android with Sameboy core - would
  crash on rumble function</li>

  <li>GFX/WIDGETS: New regular widget message appearance</li>

  <li>INPUT/MOUSE: Add distinct mouse zero index label for drivers that do not support
  multimouse</li>

  <li>INPUT/RUMBLE: Add generic rumble gain to input settings</li>

  <li>INPUT/UDEV/X11: Add workaround to fix keyboard input when using X11 + Udev</li>

  <li>LIBNX/SWITCH: Add Video Filters support</li>

  <li>LOCALIZATION: Fetch translations from Crowdin</li>

  <li>OPENDINGUX/BETA: Disable OpenAL</li>

  <li>PLAYLISTS: Add ''Refresh Playlist'' option</li>

  <li>STEAM: Initial release on Steam</li>

  <li>UWP/VFS/XBOX: Improvements and bugfixes to UWP VFS driver</li>

  <li>VIDEO/REFRESH RATE: Automatic PAL/NTSC refresh rate switch where available -
  as long as the platform display server allows changing refresh rates and the display
  has the desired refresh rate</li>

  <li>VIDEO FILTERS: Add ''Picoscale_256x-320x240'' video filter</li>

  <li>WIIU/HID: Fix analog inputs on HID devices</li>

  </ul>'
updated: '2021-09-19T03:22:03Z'
version: v1.9.10
version_title: v1.9.10
website: http://www.libretro.com
---
