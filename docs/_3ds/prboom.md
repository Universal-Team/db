---
author: Voxel
avatar: https://avatars.githubusercontent.com/u/16278868?v=4
categories:
- game
color: '#4d200e'
color_bg: '#4d200e'
created: '2023-06-11T17:58:31Z'
description: A port of PrBoom+ for the Nintendo 3DS
download_page: https://github.com/Voxel9/PrBoom-Plus-3DS/releases
downloads:
  PrBoom-Plus-3DS.zip:
    size: 31489159
    size_str: 30 MiB
    url: https://github.com/Voxel9/PrBoom-Plus-3DS/releases/download/v1.0.0/PrBoom-Plus-3DS.zip
  PrBoom-Plus.3dsx:
    size: 2328352
    size_str: 2 MiB
    url: https://github.com/Voxel9/PrBoom-Plus-3DS/releases/download/v1.0.0/PrBoom-Plus.3dsx
  PrBoom-Plus.cia:
    size: 1596864
    size_str: 1 MiB
    url: https://github.com/Voxel9/PrBoom-Plus-3DS/releases/download/v1.0.0/PrBoom-Plus.cia
github: Voxel9/PrBoom-Plus-3DS
icon: https://raw.githubusercontent.com/Voxel9/PrBoom-Plus-3DS/refs/heads/3ds/build/3ds/res/icon.png
image: https://raw.githubusercontent.com/Voxel9/PrBoom-Plus-3DS/refs/heads/3ds/build/3ds/res/banner.png
image_length: 37543
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
qr:
  PrBoom-Plus.cia: https://db.universal-team.net/assets/images/qr/prboom-plus-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/prboom/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/prboom/gameplay-2.png
- description: Gameplay 3
  url: https://db.universal-team.net/assets/images/screenshots/prboom/gameplay-3.png
- description: Gameplay 4
  url: https://db.universal-team.net/assets/images/screenshots/prboom/gameplay-4.png
- description: Gameplay 5
  url: https://db.universal-team.net/assets/images/screenshots/prboom/gameplay-5.png
- description: Title
  url: https://db.universal-team.net/assets/images/screenshots/prboom/title.png
source: https://github.com/Voxel9/PrBoom-Plus-3DS
stars: 42
systems:
- 3DS
title: PrBoom+
unique_ids:
- '0x5A9BB'
update_notes: '<p dir="auto">This is the first release of the PrBoom+ 3DS port.<br>

  Refer to the <a href="https://github.com/Voxel9/PrBoom-Plus-3DS#readme">README</a>
  for instructions on how to get the game up and running, as well as what is and isn''t
  supported.</p>

  <h3 dir="auto">FBI QR code (for remote install)</h3>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/96e09b2a-7111-4051-a3f5-9d616bf088f6"><img
  src="https://github.com/user-attachments/assets/96e09b2a-7111-4051-a3f5-9d616bf088f6"
  alt="PrBoom-Plus-3DS-QR" style="max-width: 100%;"></a></p>'
updated: '2023-07-10T14:40:04Z'
version: v1.0.0
version_title: v1.0.0
---
Hi all. After much arduous work, I'm thrilled to finally share a brand new port of PrBoom+ to the 3DS!

This is more or less a straight port of PrBoom+ 2.6.66, with some extra added enhancements exclusive to the system.
Just about everything you'd expect desktop PrBoom+ to do, this port should also be able to do.
The only things it can't do are a few unsupported renderer features (which have been stripped out anyway) and networking features.
In addition, all video modes apart from 8-bit are supported. By default, the GPU-accelerated OpenGL mode is enabled, though the other software-rendering modes are also available should you wish to fall back on them (so far, all modes produce roughly similar performance, with OpenGL being moderately faster)

Features:
-PrBoom+ 2.6.66
-Features both GPU-accelerated OpenGL mode, and software-renderer modes
-Great performance on New 3DS, decent-ish performance on Old 3DS
-Good quality stereoscopic 3D (OpenGL mode only)
-Interchangeable touchscreen mouse and keyboard
(with touchscreen mouse, you can drag to look around, tap the screen to fire, and double-tap and hold to keep firing - ideal for Old 3DS)