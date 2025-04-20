---
author: AJ Walter
avatar: https://avatars.githubusercontent.com/u/6108605?v=4
categories:
- game
color: '#6d190a'
color_bg: '#6d190a'
created: '2016-06-11T03:45:12Z'
description: A Super Hexagon Clone
download_filter: SuperHaxagon-3DS-armhf\.(3dsx|cia)\.zip
download_page: https://github.com/RedTopper/Super-Haxagon/releases
downloads:
  SuperHaxagon-3DS-armhf.3dsx.zip:
    size: 20933359
    size_str: 19 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.9.0/SuperHaxagon-3DS-armhf.3dsx.zip
  SuperHaxagon-3DS-armhf.cia.zip:
    size: 21667974
    size_str: 20 MiB
    url: https://github.com/RedTopper/Super-Haxagon/releases/download/3.9.0/SuperHaxagon-3DS-armhf.cia.zip
github: RedTopper/Super-Haxagon
icon: https://raw.githubusercontent.com/RedTopper/Super-Haxagon/master/media/icon-3ds.png
image: https://raw.githubusercontent.com/RedTopper/Super-Haxagon/master/media/banner.png
image_length: 114192
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
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
stars: 135
systems:
- 3DS
title: Super-Haxagon
unique_ids:
- '0x99AA'
update_notes: '<h1 dir="auto">GitHub Actions Edition</h1>

  <p dir="auto">GitHub Actions is now the primary way to build and release SuperHaxagon!</p>

  <p dir="auto">(This may break automated releases! Sorry about that!)</p>

  <p dir="auto">This release finishes out the last few non-major features. As such,
  this is likely the last non-patch release in the 3.x.x series.</p>

  <h2 dir="auto">Changelog</h2>

  <p dir="auto">New features:</p>

  <ul dir="auto">

  <li>macos: new platform!

  <ul dir="auto">

  <li>GitHub Actions will now build a macOS (M1) bundle automatically for new PRs
  going forward!</li>

  <li>Intel-based macOS devices should still build, but there is no automated builds
  at this time.</li>

  <li>Thanks <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/adc-ax/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/adc-ax">@adc-ax</a>
  for helping out with macOS bugs!</li>

  <li>(macOS support was previously added by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/mathieudel/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/mathieudel">@mathieudel</a>,
  but unfortunately I did not maintain it.)</li>

  </ul>

  </li>

  <li>steamdeck: new platform!

  <ul dir="auto">

  <li>The SDL2 flatpak build will auto-detect SteamDeck and enter fullscreen.</li>

  <li>Switched to SDL2 for controller support in flatpak.</li>

  <li>Tested on hardware!</li>

  <li>(Technically you could install the flatpak on SteamDeck, but the experience
  wasn''t very good.)</li>

  </ul>

  </li>

  <li>all: License change to GPLv3 (or later) for the core game.

  <ul dir="auto">

  <li>Drivers are dual licensed under GPLv3-or-later OR MIT.</li>

  <li>All downloads now include a copy of the license AND licenses for all dependencies.</li>

  </ul>

  </li>

  <li>all: Levels no longer speed up during "level ups"

  <ul dir="auto">

  <li>Instead, one big speedup happens at 60 seconds.</li>

  <li>Thanks <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/zaphod77/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/zaphod77">@zaphod77</a>
  (Fixes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="2889932849" data-permission-text="Title is private" data-url="https://github.com/RedTopper/Super-Haxagon/issues/34"
  data-hovercard-type="issue" data-hovercard-url="/RedTopper/Super-Haxagon/issues/34/hovercard"
  href="https://github.com/RedTopper/Super-Haxagon/issues/34">#34</a>)</li>

  </ul>

  </li>

  <li>all: LAST Major driver refactor, ALL platform specific files are now located
  in <code class="notranslate">driver</code></li>

  <li>all: All platforms now build with GitHub actions!</li>

  </ul>

  <h2 dir="auto">Install</h2>

  <p dir="auto">Please see the <a href="https://github.com/RedTopper/Super-Haxagon/blob/master/README.md">README.md</a>
  to install SuperHaxagon for your platform.</p>

  <h2 dir="auto">Tested Platforms</h2>

  <ul dir="auto">

  <li>3DS (Lime3DS 2119.1)</li>

  <li>3DS (Physical o3DSXL 11.15.0-47U)</li>

  <li>LinuxSDL2 (Fedora 41)</li>

  <li>LinuxSFML (Fedora 41)</li>

  <li>MiyooMini Plus (OnionOS 4.3.1-1)</li>

  <li>TI Nspire (4.5.3.14)</li>

  <li>PortMaster (Knulli 2024/12/04)</li>

  <li>Switch (Physical 11.0.1)</li>

  <li>Switch (Yuzu 1734)</li>

  <li>SteamDeck (SteamOS 3.6.24)</li>

  <li>Windows 11 (QEMU VM)</li>

  </ul>'
updated: '2025-04-18T03:32:37Z'
version: 3.9.0
version_title: SuperHaxagon v3.9.0
---
SuperHaxagon, like the original game Super Hexagon by Terry Cavanagh, has only one goal. Survive as long as possible by avoiding the falling walls in a trippy, spinny frenzy!