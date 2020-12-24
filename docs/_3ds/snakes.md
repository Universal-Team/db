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
image_length: 9681
layout: app
qr:
  snakes.cia: https://db.universal-team.net/assets/images/qr/snakes.cia.png
source: https://github.com/DDews/Snakes
systems:
- 3DS
title: Snakes
update_notes: '<h1>Patch 0.2.5.2</h1>

  <h2>Many bug fixes in this patch:</h2>

  <ul>

  <li>Game no longer crashes randomly</li>

  <li>Joining the game no longer causes strange anomalies.</li>

  <li>Boundary death now displays proper message during game "you are dead (Boundary)"</li>

  <li>Snakes no longer warp out of shape at the beginning of the round</li>

  <li>When you die with "Disappear on death", it will no longer erase part of the
  snake or boundary you ran into.</li>

  <li>Frame rate has been greatly improved</li>

  <li>Enabling autopilot no longer screws up the speed of other players</li>

  <li>Autopilot no longer screws up the lengths of certain players</li>

  </ul>

  <h1>0.2.5 release!</h1>

  <h2>New features:</h2>

  <ul>

  <li><strong>3 bot opponents</strong> with different difficulty settings for one-player
  experience.</li>

  <li><strong>Autopilot feature</strong> (press L in-game or at end-of-round screen
  to toggle). Can be used in local play.</li>

  </ul>

  <h2>Changes:</h2>

  <ul>

  <li><em>Occasional holes</em> game mode now makes holes more common. Went from 1/80
  chance of appearing to about 1/20.</li>

  <li><em>At least one bot is required to play one-player</em> while waiting for others
  to join. This is to make highscore more fair. If you can play on your own without
  a bot, the highscore would be easy to rig.</li>

  <li>The game now goes back to the Start Menu when the game ends. Press start to
  leave the game.</li>

  <li><em>The options menu has become a sub-menu</em>. To access game modes, press
  Select at the Start Screen or End-of-Round Screen to access the Options menu, then
  select Game Modes, and press A. Press B to exit a menu.</li>

  <li><em>There is a Difficulty Menu for the bots</em>. From the new Options Menu,
  select the 2nd option (highlight it in yellow), and press A. Try using direction
  buttons and A to select and change things here. Press B to go back one scene.</li>

  <li><em>There is a hidden bot settings menu</em>. Hold L and press R at the Difficulty
  Menu. This will let you adjust fine details of each bot. However, if you go to the
  regular Difficulty Menu, it will reset their settings to default.</li>

  <li><em>Autopilot</em> is also a bot, but it plays for you. Press L in-game to toggle.
  This bot has fixed settings: 100% precision, 0% aggressiveness, 30% patience. This
  means it will never go fast, but it is relatively difficult to kill in one-player.
  In local play, it can be killed a little easier due to limitations of its algorithm.</li>

  <li>Bots can''t grasp concepts like <em>Enable R</em>, but it utilizes common concepts
  like <em>holding A or B</em>, <em>teleporting the apple with Y</em>, and going through
  holes in "Occasional holes". The precision of the bot determines the likelihood
  of turning precisely. Insane and Autopilot share the highest precision, followed
  by Hard, Medium, then Easy difficulty settings.</li>

  </ul>

  <h2>Bug fixes:</h2>

  <ul>

  <li><em>Frame drop on o3ds has been fixed</em></li>

  <li><em>The rare crashing of the game has been fixed</em></li>

  <li><em>Running into a boundary in game mode "Boundaries Kill" now displays what
  killed you.</em></li>

  <li><em>Snakes are less likely to cross paths now and live to tell the tale.</em></li>

  <li>When you change your name, <em>it only says "Welcome, [name]" once</em>.</li>

  <li><em>The screen score no longer duplicates</em> when text scrolls on the bottom
  screen console during gameplay.</li>

  <li><em>Closing the lid on your console with Snakes running will not crash the game
  anymore</em>. Pressing the Home button with the cia version running will not crash
  the game anymore.</li>

  <li>Going in reverse will no longer kill you.</li>

  </ul>

  <p><strong>Just a note</strong>: this game does not run very well on old 3ds models.
  It is playable, but with 3 bots playing at once, the o3ds has severe frame-drop.
  I am trying to find the source of this problem. It only occurs on the o3ds and o3dsxl.
  The n3ds and n3dsxl are fine.</p>'
updated: '2017-01-24T22:01:22Z'
version: 0.2.5
version_title: Version 0.2.5.2
wiki: https://github.com/DDews/Snakes/wiki
---
