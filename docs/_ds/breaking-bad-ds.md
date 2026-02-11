---
author: William278
avatar: https://avatars.githubusercontent.com/u/31187453?v=4
categories:
- game
color: '#483326'
color_bg: '#483326'
created: '2023-07-06T00:11:28Z'
description: Breaking Bad, as a Nintendo DS game! Master the art of the cook and prepare
  the perfect batch—lest you meet the wrong end of Gus. Hone your cook in both Singleplayer
  and Local Multiplayer Vs.
download_page: https://github.com/WiIIiam278/breaking-bad-ds/releases
downloads:
  breaking-bad-ds.nds:
    size: 5284864
    size_str: 5 MiB
    url: https://github.com/WiIIiam278/breaking-bad-ds/releases/download/1.0.6/breaking-bad-ds.nds
github: WiIIiam278/breaking-bad-ds
icon: https://raw.githubusercontent.com/WiIIiam278/breaking-bad-ds/main/icon.png
image: https://raw.githubusercontent.com/WiIIiam278/breaking-bad-ds/main/banner-art.png
image_length: 50995
layout: app
license: apache-2.0
license_name: Apache License 2.0
nightly:
  download_page: https://github.com/WiIIiam278/breaking-bad-ds/actions
  downloads:
    Breaking Bad DS.zip:
      url: https://nightly.link/WiIIiam278/breaking-bad-ds/workflows/ci/main/Breaking%20Bad%20DS.zip
qr:
  breaking-bad-ds.nds: https://db.universal-team.net/assets/images/qr/breaking-bad-ds-nds.png
screenshots:
- description: Hanks minerals
  url: https://db.universal-team.net/assets/images/screenshots/breaking-bad-ds/hanks-minerals.png
- description: In the lab
  url: https://db.universal-team.net/assets/images/screenshots/breaking-bad-ds/in-the-lab.png
- description: Minigame
  url: https://db.universal-team.net/assets/images/screenshots/breaking-bad-ds/minigame.png
- description: Multiplayer vs
  url: https://db.universal-team.net/assets/images/screenshots/breaking-bad-ds/multiplayer-vs.png
- description: Story mode
  url: https://db.universal-team.net/assets/images/screenshots/breaking-bad-ds/story-mode.png
- description: Title screen
  url: https://db.universal-team.net/assets/images/screenshots/breaking-bad-ds/title-screen.png
source: https://github.com/WiIIiam278/breaking-bad-ds
stars: 183
systems:
- DS
title: Breaking Bad DS
update_notes: '<h2 dir="auto">Change notes</h2>

  <ul dir="auto">

  <li>Updated dialogue with Gus and Gale

  <ul dir="auto">

  <li>Fixed a few spelling mistakes (addage -&gt; adage, apologise -&gt; apologize)</li>

  <li>Fixed Gale''s introductory text implying you have already turned the ventilation
  valve</li>

  </ul>

  </li>

  <li>Fixed save data sometimes not correctly tracking the state of the game</li>

  <li>Improved the stability of the game ending logic

  <ul dir="auto">

  <li>Added a failsafe dialogue state check before end-of-day dialogue on Day 5</li>

  <li>The game will now forcibly defrag the VRAM sprite buffers before displaying
  the End Screen</li>

  <li>The game will now award the "Completed Story Mode" mineral achievement before
  displaying the End Screen</li>

  </ul>

  </li>

  <li>Fixed a bug where the mineral selection sound effect on Hank''s Minerals screen
  would play multiple times, would still play if a mineral was not selected, and would
  also still play if the same mineral was selected</li>

  <li>Added sound effects to the "cracking" minigame; the "pestle hit" effect will
  now also play when a critical hit/golden hammer hit is landed on a section or crystal
  of methamphetamine product</li>

  </ul>

  <h2 dir="auto">Playing</h2>

  <p dir="auto">For the absolute best experience, pop the ROM on a flashcart and enjoy!</p>

  <h3 dir="auto">On an Emulator</h3>

  <p dir="auto">But if you''re not as bothered as Walter is about doing things with
  the proper gear, <a href="https://github.com/melonDS-emu/melonDS/releases/latest">melonDS</a>
  is the recommended emulator for play due to its accuracy and performance. Alternatively,
  the latest release of <a href="https://github.com/TASEmulators/desmume/releases/latest">DeSmuME</a>
  is slightly easier to setup and supports <a href="#ds-rumble-pak-support">emulating
  rumble</a>.</p>

  <p dir="auto">To run this on melonDS, you''ll need to go into the Emulator Config
  -&gt; DLDI -&gt; Enable DLDI, since this uses the homebrew nitrofile system.  I
  recommend the Software video emulator for best results to make the models pop, as
  the OpenGL backend doesn''t quite support the DS''s hardware-accelerated outlines
  just yet.</p>

  <h3 dir="auto">On a modded DSi/3DS</h3>

  <p dir="auto">You can also run this on a modded DSi or 3DS with Twilight Menu++
  (other game loaders have not been tested). You can download the game ROM by scanning
  the QR code below in your loader''s menu, if your system supports this. Please make
  sure you use v1.0.3+, or your game may crash on startup!</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/43c4d7e2-0813-4d9c-b284-22e655e8f4f1"><img
  src="https://github.com/user-attachments/assets/43c4d7e2-0813-4d9c-b284-22e655e8f4f1"
  alt="QR code for installing the game on a DSi/3DS with TwilightMenu" style="max-width:
  100%;"></a></p>

  <h3 dir="auto">Unsupported platforms</h3>

  <p dir="auto">This <em>won''t work on the Wii U Virtual Console emulator</em>. I''m
  sorry to ruin your dreams. If you run this on a cool setup, take a picture and <a
  href="mailto:will27528+brbads@gmail.com">email me</a>.</p>'
updated: '2023-11-23T18:49:44Z'
version: 1.0.6
version_title: Breaking Bad 1.0.6
website: https://william278.net/project/breaking-bad-ds
---
*Breaking Bad*, as a Nintendo DS game, complete with 3D graphics and models. Master the art of the cook on your Nintendo DS system and prepare the perfect batch&mdash;lest you meet the wrong end of Gus. Hone your cook in both Singleplayer and Local Multiplayer Vs.

## Instructions
### Tutorial (1P)
The Tutorial will teach you how to play! Gale will provide instructions on how to complete each Minigame. To access the Tutorial, select it from the Main Menu.

### Story Mode (1P)
To start story mode, start the game. Touch to start, then tap "Start Game → Story Mode."

Gus has appointed you Head Cook! Meet his ever-increasing demands by cooking against the clock in the Superlab. Each day, you'll be given a Quota you must complete within a set time limit to progress on to the next day. After each day, you'll receive your pay packet based on your performance and efficiency, which you can spend in Saul's shop!

Story mode lasts five days, and there are two possible endings ("Good" and "Bad"). Good luck!

### Local Multiplayer (2P)
Breaking Bad for Nintendo DS also supports up to two Nintendo DS systems playing together in a Multiplayer Vs. Battle to see who can complete their batches the quickest. To set this up:

* On the first system, launch the game. Touch to start, then tap "Start Game → Host."
* On the second system, launch the game, touch to start, then tap "Start Game → Join."
* Wait for the systems to establish communications.
* On the Host console, press the A Button to start the game.

The Host system will play as Walter, while the guest will play as Jesse. The magic that makes it work is thanks to the incredible [Fewnity](https://github.com/Fewnity/Nintendo-DS-Nifi-Template/)'s amazing NiFi scaffold!

### Hank's Minerals
By completing certain challenges, you'll find minerals! Hank will appraise minerals you find in the "Hank's Minerals" submenu, located in the Extras Menu. There are twelve minerals to find, and you can view how to get them by tapping on each `[?]` icon in the menu.

Once you've obtained a mineral, it will be displayed in the menu and selecting it will tell you what it is. Minerals marked with "??????" are a secret, so no hints there!

### Music Player
You can listen to the game music through the Music Player submenu, located in the Extras menu. Use the left and right buttons on the + Control Pad to change the track.