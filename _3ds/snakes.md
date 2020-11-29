---
author: DDews
categories:
- game
color: '#00280e'
created: '2017-01-06T21:56:01Z'
description: Local play snake game for 3DS homebrew/cfw
download_page: https://github.com/DDews/Snakes/releases/tag/0.2.5
downloads:
  snakes.3dsx:
    size: 327356
    url: https://github.com/DDews/Snakes/releases/download/0.2.5/snakes.3dsx
  snakes.cia:
    size: 781248
    url: https://github.com/DDews/Snakes/releases/download/0.2.5/snakes.cia
github: DDews/Snakes
icon: https://raw.githubusercontent.com/DDews/Snakes/master/meta/icon.png
image: https://raw.githubusercontent.com/DDews/Snakes/master/meta/banner.png
layout: app
qr:
  snakes.cia: https://db.universal-team.net/assets/images/qr/snakes.cia.png
source: https://github.com/DDews/Snakes
systems:
- 3DS
title: Snakes
update_notes: "# Patch 0.2.5.2\n\n## Many bug fixes in this patch:\n- Game no longer\
  \ crashes randomly\n- Joining the game no longer causes strange anomalies.\n- Boundary\
  \ death now displays proper message during game \"you are dead (Boundary)\"\n- Snakes\
  \ no longer warp out of shape at the beginning of the round\n- When you die with\
  \ \"Disappear on death\", it will no longer erase part of the snake or boundary\
  \ you ran into.\n- Frame rate has been greatly improved\n- Enabling autopilot no\
  \ longer screws up the speed of other players\n- Autopilot no longer screws up the\
  \ lengths of certain players\n\n# 0.2.5 release!\n\n## New features:\n- **3 bot\
  \ opponents** with different difficulty settings for one-player experience.\n- **Autopilot\
  \ feature** (press L in-game or at end-of-round screen to toggle). Can be used in\
  \ local play.\n\n## Changes:\n- _Occasional holes_ game mode now makes holes more\
  \ common. Went from 1/80 chance of appearing to about 1/20.\n- _At least one bot\
  \ is required to play one-player_ while waiting for others to join. This is to make\
  \ highscore more fair. If you can play on your own without a bot, the highscore\
  \ would be easy to rig.\n- The game now goes back to the Start Menu when the game\
  \ ends. Press start to leave the game.\n- _The options menu has become a sub-menu_.\
  \ To access game modes, press Select at the Start Screen or End-of-Round Screen\
  \ to access the Options menu, then select Game Modes, and press A. Press B to exit\
  \ a menu.\n- _There is a Difficulty Menu for the bots_. From the new Options Menu,\
  \ select the 2nd option (highlight it in yellow), and press A. Try using direction\
  \ buttons and A to select and change things here. Press B to go back one scene.\n\
  - _There is a hidden bot settings menu_. Hold L and press R at the Difficulty Menu.\
  \ This will let you adjust fine details of each bot. However, if you go to the regular\
  \ Difficulty Menu, it will reset their settings to default.\n- _Autopilot_ is also\
  \ a bot, but it plays for you. Press L in-game to toggle. This bot has fixed settings:\
  \ 100% precision, 0% aggressiveness, 30% patience. This means it will never go fast,\
  \ but it is relatively difficult to kill in one-player. In local play, it can be\
  \ killed a little easier due to limitations of its algorithm. \n- Bots can't grasp\
  \ concepts like _Enable R_, but it utilizes common concepts like _holding A or B_,\
  \ _teleporting the apple with Y_, and going through holes in \"Occasional holes\"\
  . The precision of the bot determines the likelihood of turning precisely. Insane\
  \ and Autopilot share the highest precision, followed by Hard, Medium, then Easy\
  \ difficulty settings.\n\n## Bug fixes:\n- _Frame drop on o3ds has been fixed_\n\
  - _The rare crashing of the game has been fixed_\n- _Running into a boundary in\
  \ game mode \"Boundaries Kill\" now displays what killed you._\n- _Snakes are less\
  \ likely to cross paths now and live to tell the tale._\n- When you change your\
  \ name, _it only says \"Welcome, [name]\" once_.\n- _The screen score no longer\
  \ duplicates_ when text scrolls on the bottom screen console during gameplay.\n\
  - _Closing the lid on your console with Snakes running will not crash the game anymore_.\
  \ Pressing the Home button with the cia version running will not crash the game\
  \ anymore.\n- Going in reverse will no longer kill you.\n\n**Just a note**: this\
  \ game does not run very well on old 3ds models. It is playable, but with 3 bots\
  \ playing at once, the o3ds has severe frame-drop. I am trying to find the source\
  \ of this problem. It only occurs on the o3ds and o3dsxl. The n3ds and n3dsxl are\
  \ fine.\n"
updated: '2017-01-24T22:01:22Z'
version: 0.2.5
version_title: Version 0.2.5.2
wiki: https://github.com/DDews/Snakes/wiki
---
