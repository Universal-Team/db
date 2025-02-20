---
author: AJ Walter
avatar: https://avatars.githubusercontent.com/u/6108605?v=4
categories:
- game
color: '#6d190a'
color_bg: '#6d190a'
created: '2016-06-11T03:45:12Z'
description: A Super Hexagon Clone
download_page: https://github.com/RedTopper/Super-Haxagon/releases
downloads:
  SuperHaxagon-Linux.tar.gz:
    size: 18462931
    size_str: 17 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.7.0/SuperHaxagon-Linux.tar.gz
  SuperHaxagon-Windows.zip:
    size: 18991515
    size_str: 18 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.7.0/SuperHaxagon-Windows.zip
  SuperHaxagon.3dsx:
    size: 20183296
    size_str: 19 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.7.0/SuperHaxagon.3dsx
  SuperHaxagon.cia:
    size: 20591552
    size_str: 19 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.7.0/SuperHaxagon.cia
  SuperHaxagon.tns:
    size: 1088648
    size_str: 1 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.7.0/SuperHaxagon.tns
  net.awalter.SuperHaxagon.flatpak:
    size: 19871040
    size_str: 18 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.7.0/net.awalter.SuperHaxagon.flatpak
github: RedTopper/Super-Haxagon
icon: https://raw.githubusercontent.com/RedTopper/Super-Haxagon/master/media/icon-3ds.png
image: https://raw.githubusercontent.com/RedTopper/Super-Haxagon/master/media/banner.png
image_length: 114192
layout: app
license: mit
license_name: MIT License
qr:
  SuperHaxagon.cia: https://db.universal-team.net/assets/images/qr/superhaxagon-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/super-haxagon/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/super-haxagon/gameplay-2.png
- description: Gameplay 3
  url: https://db.universal-team.net/assets/images/screenshots/super-haxagon/gameplay-3.png
- description: Gameplay 4 horihd
  url: https://db.universal-team.net/assets/images/screenshots/super-haxagon/gameplay-4-horihd.png
- description: Gameplay 4
  url: https://db.universal-team.net/assets/images/screenshots/super-haxagon/gameplay-4.png
source: https://github.com/RedTopper/Super-Haxagon
stars: 130
systems:
- 3DS
title: Super-Haxagon
unique_ids:
- '0x99AA'
update_notes: '<p dir="auto">This release completes what I wanted to do for a long
  time - use linear algebra for all the transforms in the game! This allows for some
  fun things like panning the camera around and doing tilt properly. It also simplifies
  the game logic (in a crazy kind of way) so that the core logic doesn''t have to
  worry about rotations.</p>

  <p dir="auto">I tried implementing this a few years ago but ran into roadblocks,
  then abandoned the idea altogether. Since I''m active in this codebase again, I
  figured I''d give it a second shot!</p>

  <p dir="auto">Also, despite using the additional math for the matrix transformations,
  the Nspire release still runs great!</p>

  <p dir="auto">New features for this release:</p>

  <ul dir="auto">

  <li>all: New title menu before the level select</li>

  <li>all: Camera pans and color transitions between most states</li>

  <li>switch: You can now use "X" to rotate right, like the 3ds</li>

  </ul>

  <p dir="auto">Under the hood features:</p>

  <ul dir="auto">

  <li>all: Drivers cleaned up to officially use "Pimpl"</li>

  <li>all: Drivers no longer make excessive pointer de-references and instead direct
  calls to the Impl itself</li>

  <li>all: Drivers now have "Surface" classes that contain core rendering logic, split
  out from Platform</li>

  <li>all: Game uses new SurfaceGame class, which implements software matrix transforms</li>

  <li>all: Code cleanup, where applicable</li>

  </ul>

  <p dir="auto">Note: This was a large refactor. Please report any bugs found with
  this new release. Thanks!</p>'
updated: '2025-02-16T06:48:21Z'
version: 3.7.0
version_title: SuperHaxagon v3.7.0
---
