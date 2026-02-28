---
author: Voxel
avatar: https://avatars.githubusercontent.com/u/16278868?v=4
categories:
- game
color: '#515c7b'
color_bg: '#515c7b'
created: '2023-02-02T06:44:28Z'
description: An updated 3DS port of the Sonic CD (2011) Decompilation
download_page: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux/releases
downloads:
  SonicCD.3dsx:
    size: 1314036
    size_str: 1 MiB
    url: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux/releases/download/v1.2.0/SonicCD.3dsx
  SonicCD.cia:
    size: 1257408
    size_str: 1 MiB
    url: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux/releases/download/v1.2.0/SonicCD.cia
github: Voxel9/Sonic-CD-11-3DS-Redux
icon: https://raw.githubusercontent.com/Voxel9/Sonic-CD-11-3DS-Redux/refs/heads/3ds-2025/RSDKv3.3DS/res/icon.png
image: https://raw.githubusercontent.com/Voxel9/Sonic-CD-11-3DS-Redux/refs/heads/3ds-2025/RSDKv3.3DS/res/banner.png
image_length: 61771
layout: app
license: other
license_name: Other
qr:
  SonicCD.cia: https://db.universal-team.net/assets/images/qr/soniccd-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/sonic-cd/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/sonic-cd/gameplay-2.png
- description: Gameplay 3
  url: https://db.universal-team.net/assets/images/screenshots/sonic-cd/gameplay-3.png
- description: Gameplay 4
  url: https://db.universal-team.net/assets/images/screenshots/sonic-cd/gameplay-4.png
- description: Title screen
  url: https://db.universal-team.net/assets/images/screenshots/sonic-cd/title-screen.png
script_message: 'Note: You will need "Data.rsdk" from

  the Steam, Android, or iOS version in

  "sdmc:/3ds/SonicCD" to play the game.'
source: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux
stars: 29
systems:
- 3DS
title: Sonic CD
unique_ids:
- '0x72F03'
update_notes: '<p dir="auto">This is the third release of the updated Sonic CD 3DS
  port.</p>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Now built on the most recent decomp source, as of Feb 2025</li>

  <li>FMV playback (Currently slow on O3DS and choppy on N3DS, use ffmpeg to scale
  down OGVs)</li>

  <li>Mods are now fully supported, install them the same way you would usually (in
  the mods folder)

  <ul dir="auto">

  <li>Also copy the decompiled scripts to the Scripts folder from here:</li>

  <li><a href="https://github.com/RSDKModding/RSDKv3-Script-Decompilation">https://github.com/RSDKModding/RSDKv3-Script-Decompilation</a></li>

  </ul>

  </li>

  <li>Software renderer now supported, but slow special stages on N3DS, and slow in
  general on O3DS

  <ul dir="auto">

  <li>This isn''t really useful when the hardware renderer exists, but is just nice
  to have</li>

  </ul>

  </li>

  <li>Navigation is now bound to both the circle pad and the dpad by default</li>

  <li>Fixed special stage backgrounds rendering incorrect when stereo 3D was on</li>

  <li>Fixed rendering in the game pause menu</li>

  </ul>

  <p dir="auto">If you''re upgrading from an older version, delete the existing settings.ini
  to ensure stability.</p>

  <p dir="auto">Refer to the <a href="https://github.com/Voxel9/Sonic-CD-11-3DS-Redux#readme">README</a>
  for further instructions.</p>

  <h3 dir="auto">FBI QR code (for remote install)</h3>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/16278868/216816089-7fa60ff0-3ea5-4dd2-b27b-2c2d5ea3fc4e.png"><img
  src="https://user-images.githubusercontent.com/16278868/216816089-7fa60ff0-3ea5-4dd2-b27b-2c2d5ea3fc4e.png"
  alt="qr-code" style="max-width: 100%;"></a></p>'
updated: '2025-02-02T03:57:25Z'
version: v1.2.0
version_title: v1.2.0
---
Port of Sonic CD to the 3DS, based on Rubberduckycooly's Sonic CD decompilation.

In order to run the game, you need to copy the "Data.rsdk" file from the Steam, Android, or iOS version of Sonic CD to "/3ds/SonicCD" on your SD card.