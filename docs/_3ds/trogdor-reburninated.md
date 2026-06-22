---
author: Mode8fx
avatar: https://avatars.githubusercontent.com/u/57763469?v=4
categories:
- game
color: '#0a6c24'
color_bg: '#0a6c24'
created: '2021-11-13T05:10:52Z'
description: Burninate the countryside!
download_filter: 3ds
download_page: https://github.com/Mode8fx/Trogdor-Reburninated/releases
downloads:
  Trogdor-Reburninated-v2.4-3ds-cia.zip:
    size: 6496524
    size_str: 6 MiB
    url: https://github.com/Mode8fx/Trogdor-Reburninated/releases/download/v2.4/Trogdor-Reburninated-v2.4-3ds-cia.zip
  Trogdor-Reburninated-v2.4-3ds.zip:
    size: 6094663
    size_str: 5 MiB
    url: https://github.com/Mode8fx/Trogdor-Reburninated/releases/download/v2.4/Trogdor-Reburninated-v2.4-3ds.zip
github: Mode8fx/Trogdor-Reburninated
icon: https://raw.githubusercontent.com/Mode8fx/Trogdor-Reburninated/main/Trogdor-Reburninated/release-resources/logo_icon_android_48.png
image: https://raw.githubusercontent.com/Mode8fx/Trogdor-Reburninated/main/Trogdor-Reburninated/release-resources/background_psp.png
image_length: 14597
layout: app
license: mit
license_name: MIT License
llm_generation: null
screenshots:
- description: Gameplay
  url: https://db.universal-team.net/assets/images/screenshots/trogdor-reburninated/gameplay.png
source: https://github.com/Mode8fx/Trogdor-Reburninated
stars: 33
systems:
- 3DS
title: 'Trogdor: Reburninated'
unique_ids:
- '0xCB52C'
update_notes: '<p dir="auto"><a href="https://homestarrunner.com/sbemails/51-website"
  rel="nofollow">Oh you thought there was no more updates but guess what there''s
  an UPDATE!</a></p>

  <p dir="auto">What started as a few technical fixes spiraled into a bigger update
  tying up a bunch of loose ends. Check it out check it out check it out:</p>

  <h3 dir="auto">Changes</h3>

  <ul dir="auto">

  <li><strong>Added new "Reburninated" logo</strong> to instructions screen and icons
  (it’s about time!).</li>

  <li><strong>Added custom soundtrack support</strong>. Simply convert your music
  and put the WAV/OGG output in /music/custom. See the included README for more details.</li>

  <li><strong>Added volume controls</strong> for music, sound effects, and Strong
  Bad’s commentary.</li>

  <li><strong>Increased volume</strong> of most sound effects, and slightly increased
  volume of most voice clips. Additionally, music can now get much louder.</li>

  <li><strong>Reorganized Options menu</strong> (again) by splitting Cosmetic Settings
  into separate Audio and Video sections.</li>

  <li><strong>Reworked Options menu background</strong> to fill full (4:3) screen,
  and increased its resolution on most systems.</li>

  <li>Other assorted polish.</li>

  <li>[PSP] Music now fades out at the end of a level like on other systems.</li>

  </ul>

  <h3 dir="auto">Bug Fixes</h3>

  <ul dir="auto">

  <li><strong>Fixed movement being jittery</strong> at high framerates.</li>

  <li><strong>Fixed music not playing</strong> on levels 47 and 48.</li>

  <li>Fixed Theater and sound logic misclassifying some sound effects as music and
  vice-versa.</li>

  <li>Adjusted fire breath position by one pixel to match the Flash version more closely.</li>

  <li>[Android] <strong>Fixed game running too fast</strong> at &gt;60 Hz refresh
  rates.</li>

  <li>[PSP] <strong>Fixed audio popping</strong> (finally).</li>

  </ul>

  <h3 dir="auto">Technical Improvements</h3>

  <ul dir="auto">

  <li><strong>Overhauled audio</strong>, removing all stuttering, reducing file size
  for most systems, and usually reducing initial load time (depending on system).
  Every system now uses high-quality OGG except:

  <ul dir="auto">

  <li>[Gamecube, 3DS, FunKey] Low-quality OGG (Gamecube had to be dropped to low quality
  to make sure all common sounds could fit in RAM... sorry)</li>

  <li>[PSP] Low-quality OGG (music) and WAV (sound effects/voices, because OGG would
  greatly increase initial load time)</li>

  </ul>

  </li>

  <li><strong>Reduced audio latency</strong>.</li>

  <li>Optimized text rendering.</li>

  <li>Optimized border rendering on some systems.</li>

  <li>Other assorted minor optimizations.</li>

  <li>Updated SDL2 libraries on most systems.</li>

  <li>Removed OGG_SFX compiler flag since audio loading now supports OGG and WAV simultaneously.</li>

  <li>[Gamecube, Wii] Upgraded to libogc2, which introduces a variety of improvements
  including <strong>save/load support for FlippyDrive</strong> (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Extrems/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Extrems">@Extrems</a>!).</li>

  <li>[PSP] Removed OSLibAudio dependency; audio now uses SDL_mixer like every other
  system.</li>

  <li>[PSP] <strong>Upgraded PSPDEV</strong>, resulting in improved performance and
  stability.</li>

  </ul>

  <p dir="auto">Enjoy!</p>'
updated: '2026-05-17T15:24:11Z'
version: v2.4
version_title: v2.4
---
An enhanced recreation of the Homestar Runner Flash game, "Trogdor", expanded with new features.
- New Options menu to customize your game
- Level select
- New cheats
- Optional soundtrack from Stinkoman 20X6, another Homestar Runner game
- Multiple screen scaling options
- Bugs from the original game have been fixed