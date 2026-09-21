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
    size: 1313632
    size_str: 1 MiB
    url: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux/releases/download/v1.2.1/SonicCD.3dsx
  SonicCD.cia:
    size: 1259456
    size_str: 1 MiB
    url: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux/releases/download/v1.2.1/SonicCD.cia
github: Voxel9/Sonic-CD-11-3DS-Redux
icon: https://raw.githubusercontent.com/Voxel9/Sonic-CD-11-3DS-Redux/refs/heads/3ds-2025/RSDKv3.3DS/res/icon.png
image: https://raw.githubusercontent.com/Voxel9/Sonic-CD-11-3DS-Redux/refs/heads/3ds-2025/RSDKv3.3DS/res/banner.png
image_length: 61771
layout: app
license: other
license_name: Other
llm_generation: unknown
preinstall_message: 'Note: You will need "Data.rsdk" from

  the Steam, Android, or iOS version in

  "sdmc:/3ds/SonicCD" to play the game.'
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
source: https://github.com/Voxel9/Sonic-CD-11-3DS-Redux
stars: 34
systems:
- 3DS
title: Sonic CD
unique_ids:
- '0x72F03'
update_notes: '<p dir="auto">v1.2.1</p>

  <p dir="auto">This is a minor update to the previous release which addresses the
  following:</p>

  <ul dir="auto">

  <li>Fixes an issue where using the Data.rsdk of the PC version with hardware renderer
  enabled, then pausing and unpausing in any Tidal Tempest zone, would cause the entire
  screen to flash constantly.</li>

  <li>The fix has the added benefit of making Tidal Tempest visible with the PC Data.rsdk
  and HW renderer, however there are some slight visual errors, such as a lack of
  water discoloration and waterfalls not animating, but will not affect progression.
  To fix these errors, use the mobile Data.rsdk which, as a reminder, will also make
  the special stage floors draw correctly.</li>

  </ul>

  <p dir="auto">If you''re upgrading from an older version (pre-1.2.0), delete the
  existing settings.ini to ensure stability.</p>

  <p dir="auto">Refer to the <a href="https://github.com/Voxel9/Sonic-CD-11-3DS-Redux#readme">README</a>
  for further instructions.</p>

  <h3 dir="auto">FBI QR code (for remote install)</h3>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/16278868/216816089-7fa60ff0-3ea5-4dd2-b27b-2c2d5ea3fc4e.png"><img
  src="https://user-images.githubusercontent.com/16278868/216816089-7fa60ff0-3ea5-4dd2-b27b-2c2d5ea3fc4e.png"
  alt="qr-code" style="max-width: 100%;"></a></p>'
updated: '2026-09-21T18:48:53Z'
version: v1.2.1
version_title: v1.2.1
---
Port of Sonic CD to the 3DS, based on Rubberduckycooly's Sonic CD decompilation.

In order to run the game, you need to copy the "Data.rsdk" file from the Steam, Android, or iOS version of Sonic CD to "/3ds/SonicCD" on your SD card.