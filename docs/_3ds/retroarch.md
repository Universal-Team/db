---
author: libretro
avatar: https://avatars.githubusercontent.com/u/1812827?v=4
categories:
- emulator
color: '#484848'
created: '2010-05-27T14:47:40Z'
description: Cross-platform, sophisticated frontend for the libretro API. Licensed
  GPLv3.
download_page: https://buildbot.libretro.com/stable/1.9.9/nintendo/3ds
downloads:
  RetroArch_3dsx.7z:
    url: https://buildbot.libretro.com/stable/1.9.9/nintendo/3ds/RetroArch_3dsx.7z
  RetroArch_cia.7z:
    url: https://buildbot.libretro.com/stable/1.9.9/nintendo/3ds/RetroArch_cia.7z
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

  <li>3DS: Add bottom touchscreen menu</li>

  <li>3DS/SAVESTATES: Save and load save states to and from RAM</li>

  <li>AUDIO/MIXER: Ensure than menu sounds are re-enabled when calling CMD_EVENT_AUDIO_REINIT</li>

  <li>AUDIO/RESAMPLER/MIXER: Fix menu sounds (audio mixing) when using the ''sinc''
  resampler with quality lower than ''normal''</li>

  <li>AUDIO/CONVERSION/ARM NEON: Add intrinsic NEON versions for float_to_s16/s16_to_float
  - should lead to optimized codepaths for AArch64/ARMv7 architectures without being
  dependent on ASM codepaths.</li>

  <li>AUDIO/RESAMPLER/ARM NEON: Add intrinsic NEON version for lanczos sinc function
  - should lead to optimized codepaths for AArch64/ARMv7 architectures without being
  dependent on ASM codepaths.</li>

  <li>CHEEVOS: Upgrade to rcheevos 10.2</li>

  <li>CHEATS: Add enhanced search functionality to the ''Cheats'' menu</li>

  <li>CHEATS/RUNAHEAD: Fix cheats when using second instance runahead</li>

  <li>CONFIG: Add option to (force-)write current core options to disk (Quick Menu)</li>

  <li>CORE INFO CACHE: Remove core path from core info cache. Should make core info
  caches portable now (for example: you can move RetroArch to a separate dir and they
  would still work).</li>

  <li>D3D11: Use Shader Model 5.0 for frontend shaders if D3D11 Feature level is at
  least 11.0 or higher. Should fix some new shaders that require SM 5.0 (like AMD
  FSR)</li>

  <li>D3D11: Add HDR support (disabled for UWP for now)</li>

  <li>D3D12: Add HDR support (disabled for UWP for now)</li>

  <li>EMSCRIPTEN: Fixed web player bug with filesystem and runtime</li>

  <li>INPUT/OVERLAY: Fix overlay input when analog to digital mapping is enabled</li>

  <li>INPUT/UDEV: Look for "ID_INPUT_KEY", not "ID_INPUT_KEYBOARD"</li>

  <li>INPUT/WINRAW: Fix crash when overlay is enabled</li>

  <li>MAC/METAL: Add Discord RPC support</li>

  <li>MENU: Allow ''Custom Aspect Ratio (X Position)/(Y Position)/(Width)/(Height)''
  to be entered manually via keyboard</li>

  <li>MENU: Allow ''Vertical Refresh Rate'' to be entered manually via keyboard</li>

  <li>MENU/SHADERS: Highlight currently selected value in Shader Parameter drop-down
  lists</li>

  <li>STABILITY: Safer way of avoiding the race condition in<br>

  audio_driver_sample/audio_driver_sample_batch - we can check<br>

  audio-suspended to see if we''re doing a fs/windowed toggle - enhances stability
  when fullscreen toggling/tearing down context</li>

  <li>STABILITY: When audio driver write callback function fails, don''t<br>

  turn audio off completely - look if audio_driver_output_samples_conv_buf<br>

  is non-NULL first before we attempt to write audio - enhances stability when fullscreen
  toggling/tearing down context</li>

  <li>STABILITY: Input robustness for cores that use internal threading<br>

  (full teardown/setup), no audio should be processed at this point in<br>

  time</li>

  <li>VIDEO: Screen resolution list sanitizing</li>

  <li>VULKAN: Fix some Vulkan validation layer errors</li>

  <li>UWP: Updated icons courtesy of Danp142</li>

  <li>UWP/XBOX: Disable CPU model check on Xbox as it doesn''t work and can even crash</li>

  <li>UWP/VFS/XBOX: Code cleanup and simplification of UWP VFS driver</li>

  </ul>'
updated: '2021-09-05T02:00:50Z'
version: v1.9.9
version_title: v1.9.9
website: http://www.libretro.com
---
