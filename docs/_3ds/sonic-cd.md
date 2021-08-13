---
author: SaturnSH2x2
avatar: https://avatars.githubusercontent.com/u/18273084?v=4
categories:
- game
color: '#4d5872'
created: '2021-01-22T22:40:50Z'
description: Port of Sonic CD to the 3DS, based on Rubberduckycooly's Sonic CD decompilation
download_page: https://github.com/SaturnSH2x2/Sonic-CD-11-Decompilation/releases
downloads:
  SonicCD_HW.3dsx:
    size: 1435056
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.30/SonicCD_HW.3dsx
  SonicCD_HW.cia:
    size: 1361856
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.30/SonicCD_HW.cia
  SonicCD_SW.3dsx:
    size: 1442732
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.30/SonicCD_SW.3dsx
  SonicCD_SW.cia:
    size: 1366464
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.30/SonicCD_SW.cia
github: SaturnSH2x2/Sonic-CD-11-Decompilation
icon: https://raw.githubusercontent.com/SaturnSH2x2/Sonic-CD-11-Decompilation/master/resources/48x48.png
image: https://raw.githubusercontent.com/SaturnSH2x2/Sonic-CD-11-Decompilation/master/resources/banner.png
image_length: 66191
layout: app
license: other
license_name: Other
qr:
  SonicCD_HW.cia: https://db.universal-team.net/assets/images/qr/soniccd_hw.cia.png
  SonicCD_SW.cia: https://db.universal-team.net/assets/images/qr/soniccd_sw.cia.png
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
source: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS
systems:
- 3DS
title: Sonic CD
update_notes: '<h2>Changelog:</h2>

  <ul>

  <li>Audio backend switched (again) to use SDL_mixer. This should get rid of any
  bugs where the audio thread would randomly hang, preventing music and sound effects
  from playing,</li>

  <li>Banner and icon were updated to match the 2011 promo materials, as well as to
  remain consistent with JeffRuLz''s decomp ports. The jingle was also fixed, and
  now plays properly on the home screen. You may need to uninstall older versions
  for this to fully take effect.</li>

  <li>Data Folder mode is now fixed.</li>

  <li>Mod loader support is now implemented. You can access the mod loader from the
  dev menu. Make sure you have your Scripts folder extracted to /3ds/SonicCD (you
  can download said folder from <a href="https://github.com/Rubberduckycooly/Sonic-CD-2011-Script-Decompilation">this</a>
  repo.</li>

  <li>Video support is now implemented via <a class="user-mention" data-hovercard-type="user"
  data-hovercard-url="/users/Oreo639/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Oreo639">@Oreo639</a>''s
  <a href="https://github.com/Oreo639/3ds-theoraplayer">3ds-theoraplayer</a>. Make
  sure you extract your videos to /3ds/SonicCD/videos. You might want to scale down
  your videos for them to run well, or download prescaled versions from <a href="https://gamebanana.com/mods/313570"
  rel="nofollow">here</a>.</li>

  </ul>

  <h2>Experimental HW Build Added:</h2>

  <ul>

  <li>A WIP custom render backend for the Retro Engine using Citro2D was added. A
  few effects aren''t yet implemented, but speed is good at O3DS clock.</li>

  <li>Much of the game is playable using this backend, however, Special Stages are
  still a WIP, and can''t be played unless you''re really good at playing through
  these without looking at the floor.</li>

  <li>Palette effects aren''t fully supported (i.e. palette cycling doesn''t work
  properly, and Tidal Tempest ends up resembling its Gems Collection counterpart using
  the Steam RSDK).</li>

  <li>Parallax is implemented, but a bit screwy at points, and per-scanline parallax
  isn''t yet implemented. That said, "It''s not a big problem really, most people
  won''t really notice the per tile parallax." <a href="https://web.archive.org/web/20071008215241/http://rsonic.randomsonicnet.org/features.htm#ports"
  rel="nofollow">Taxman''s words, not mine.</a></li>

  <li>Stereoscopic 3D is supported, and you can adjust the depth using the 3D slider.</li>

  </ul>

  <p>Attached to this release are two builds of the game, one using the software render
  backend, and one using the new custom hardware render backend. Keep in mind, stereoscopic
  3D is only supported on the HW build.</p>

  <p>O3DS owners should probably download the HW build. N3DS owners have the choice
  of downloading either, depending on whether or not they want to try out the stereoscopic
  3D feature, at the expense of palette/parallax effects and special stages.</p>'
updated: '2021-08-13T15:31:33Z'
version: v1.30
version_title: WIP O3DS Support, Stereoscopic 3D, Video Support, and more
---
Port of Sonic CD to the 3DS, based on Rubberduckycooly's Sonic CD decompilation.

In order to run the game, you need to copy the "Data.rsdk" file from the Steam version of Sonic CD to "/3ds/SonicCD" on your SD card.