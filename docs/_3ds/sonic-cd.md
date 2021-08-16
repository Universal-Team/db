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
    size: 1432516
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.31/SonicCD_HW.3dsx
  SonicCD_HW.cia:
    size: 1359808
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.31/SonicCD_HW.cia
  SonicCD_SW.3dsx:
    size: 1440212
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.31/SonicCD_SW.3dsx
  SonicCD_SW.cia:
    size: 1364416
    size_str: 1 MiB
    url: https://github.com/SaturnSH2x2/Sonic-CD-11-3DS/releases/download/v1.31/SonicCD_SW.cia
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
update_notes: '<p>Minor update; basically stuff that should''ve gone into the previous
  release to begin with.</p>

  <h2>Changes:</h2>

  <h3>All builds:</h3>

  <ul>

  <li>Fix <code>modconfig.ini</code> not being properly written to; mod selections
  should no longer be reset on startup/entering the mod menu.</li>

  <li>Fix bug where the music wouldn''t play on the main menu upon switching soundtracks.</li>

  <li>Fix stage-specific sound effects not being properly loaded on stage reloads.</li>

  <li>Console output is now disabled on the bottom screen when the engine isn''t in
  debug mode.</li>

  <li>The engine now loads separate video files when using the US soundtrack; said
  files should have the extension <code>.us.ogv</code>. Again, pre-scaled versions
  can be found <a href="https://gamebanana.com/mods/313570" rel="nofollow">here</a>.</li>

  </ul>

  <h3>HW Build:</h3>

  <ul>

  <li>Fixed the depth value on sprite layers, certain objects should no longer go
  "into" the background.</li>

  <li>Fixed slight discoloration issues (most noticeable on the title screen).</li>

  </ul>'
updated: '2021-08-16T18:11:25Z'
version: v1.31
version_title: Minor Tweaks and Bugfixes
---
Port of Sonic CD to the 3DS, based on Rubberduckycooly's Sonic CD decompilation.

In order to run the game, you need to copy the "Data.rsdk" file from the Steam version of Sonic CD to "/3ds/SonicCD" on your SD card.