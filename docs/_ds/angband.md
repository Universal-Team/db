---
author: The Angband team
avatar: https://avatars.githubusercontent.com/u/458884?v=4
categories:
- game
color: '#858585'
color_bg: '#808080'
created: '2010-10-29T01:17:48Z'
description: A free, single-player roguelike dungeon exploration game
download_filter: -(3ds|nds)\.zip
download_page: https://github.com/angband/angband/releases
downloads: {}
github: angband/angband
icon: https://github.com/angband.png?size=48
image: https://github.com/angband.png
image_length: 3366
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
prerelease:
  download_page: https://github.com/angband/angband/releases/tag/4.2.6-57-g8e22bb81c
  downloads:
    Angband-4.2.6-57-g8e22bb81c-3ds.zip:
      size: 24669672
      size_str: 23 MiB
      url: https://github.com/angband/angband/releases/download/4.2.6-57-g8e22bb81c/Angband-4.2.6-57-g8e22bb81c-3ds.zip
    Angband-4.2.6-57-g8e22bb81c-nds.zip:
      size: 23330146
      size_str: 22 MiB
      url: https://github.com/angband/angband/releases/download/4.2.6-57-g8e22bb81c/Angband-4.2.6-57-g8e22bb81c-nds.zip
  update_notes: '<h2 dir="auto">What''s Changed</h2>

    <ul dir="auto">

    <li>ci: replace autotools builds with CMake in release.yaml by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/klaasvanaarsen/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/klaasvanaarsen">@klaasvanaarsen</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="3863072015" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6509"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6509/hovercard"
    href="https://github.com/angband/angband/pull/6509">#6509</a></li>

    <li>X11: avoid using uninitialized data after memory allocation failure by <a
    class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="3887363477" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6513"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6513/hovercard"
    href="https://github.com/angband/angband/pull/6513">#6513</a></li>

    <li>X11: free class and size hints immediately after sending them to the server
    by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="3887468303" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6514"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6514/hovercard"
    href="https://github.com/angband/angband/pull/6514">#6514</a></li>

    <li>borg: fix waiting for a monster to approach by <a class="user-mention notranslate"
    data-hovercard-type="user" data-hovercard-url="/users/agoodman00/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/agoodman00">@agoodman00</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="3902932066" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6516"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6516/hovercard"
    href="https://github.com/angband/angband/pull/6516">#6516</a></li>

    </ul>

    <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/angband/angband/compare/4.2.6-53-g6bf9d6f43...4.2.6-57-g8e22bb81c"><tt>4.2.6-53-g6bf9d6f43...4.2.6-57-g8e22bb81c</tt></a></p>'
  update_notes_md: '## What''s Changed

    * ci: replace autotools builds with CMake in release.yaml by @klaasvanaarsen in
    https://github.com/angband/angband/pull/6509

    * X11: avoid using uninitialized data after memory allocation failure by @backwardsEric
    in https://github.com/angband/angband/pull/6513

    * X11: free class and size hints immediately after sending them to the server
    by @backwardsEric in https://github.com/angband/angband/pull/6514

    * borg: fix waiting for a monster to approach by @agoodman00 in https://github.com/angband/angband/pull/6516



    **Full Changelog**: https://github.com/angband/angband/compare/4.2.6-53-g6bf9d6f43...4.2.6-57-g8e22bb81c'
  updated: '2026-02-10T15:02:12Z'
  version: 4.2.6-57-g8e22bb81c
  version_title: 4.2.6-57-g8e22bb81c
source: https://github.com/angband/angband
stars: 1479
systems:
- 3DS
- DS
title: Angband
unique_ids:
- '0x616E6'
update_notes: '<p dir="auto">This version includes changes to device activation, many
  corrections and improvements to the borg automatic player, and several bug fixes.  Changes
  affecting gameplay are:</p>

  <ul dir="auto">

  <li>Like digging, failure to activate a magical device automatically retries the
  activation until successful or disturbed.  Make utility devices, elemental rings,
  and dragon armor easier to activate.  Devices to slow monsters, wands of fire balls
  and dragon''s flame, rods of fire bolts, and rods of treasure location are now more
  difficult to activate.  Change the activation difficulties for artifacts so they
  are better aligned with the nature of the activation.  Change a constant in the
  failure rate calculation to tighten the transition from high to low failure rates:  effects
  that change a player''s device skill will have more of an impact if the skill is
  close to the activation difficulty for the device.</li>

  <li>When following a precomputed path (moving to a grid designated by the mouse,
  targeting interface, or autoexplore commands) automatically open doors or clear
  impassable rubble and continue moving when the neighbors of the door or rubble are
  known.</li>

  <li>Object descriptions now include the effect of curses in the displayed hit, damage,
  and armor class values.</li>

  <li>Messages for detection now distinguish between gold on the floor and other objects
  (thanks to PowerDiver).</li>

  <li>Objects and spells that used SPOT effects with LIGHT_WEAK or DARK_WEAK now use
  SPHERE instead so they can not damage the player.</li>

  <li>Change the target handling for a druid''s Lightning Strike:  do not require
  a known grid and target the player if the target is given as a direction or is not
  a passable grid in the line of sight.</li>

  <li>If a necromancer''s Command spell is resisted, deduct mana and take a turn (thanks
  to RegalStar).</li>

  <li>Mithril arrows and shots weigh 50% less; mithril shots ignore acid and fire
  (thanks to edz314).</li>

  <li>Increase the curse removal power of staves of remove curse to distinguish them
  from scrolls of remove curse (thanks to Mitze).</li>

  <li>Increase the escorts for Grishnákh and Golfimbul:  both can also have cave orcs
  as escorts.</li>

  <li>Change the edges of the Cracks of Doom vault so magic mapping clearly identifies
  the entrances (thanks to Mikolaj).</li>

  <li>Change handling of keymaps so the keymap aborts when the next key does not correspond
  to a command, a command fails due to a missing prerequisite or to a player confirmation
  from an inscription check.  Rework how directions are extracted from a keymap.  Allow
  for a keymap trigger whose action starts with ESCAPE to break out of many prompts
  (thanks to PowerWyrm).</li>

  <li>Add an option, autoexplore_commands, to have ''p'' move to the player to the
  nearest unexplored location and modify the existing ''&gt;'' and ''&lt;'' commands
  to move the player to the nearest staircase of the appropriate type when not on
  a staircase (thanks to memmaker).  Whether or not that option is set, add to the
  looking or targeting interface so ''&gt;'' or ''&lt;'' move the cursor to the nearest
  appropriate staircase from where the cursor was and ''x'' moves the cursor to the
  nearest unexplored location to where the cursor was (thanks to Gwarl).</li>

  <li>The notifications shown when the show_damage option is on now include information
  about damage due to effects from spells or magic devices.  Notifications about damage
  to the player now take into account damage reduction and invulnerability.</li>

  </ul>

  <p dir="auto">There are a handful of notable changes to the Windows front end (thanks
  to Klaas van Aarsen):</p>

  <ul dir="auto">

  <li>With tiles, the map displayed by ''M'' now uses the algorithm that Options-&gt;Map
  used.  Options-&gt;Map has been removed.</li>

  <li>Subwindows can have more than 256 rows or columns without drawing artifacts.</li>

  </ul>

  <p dir="auto">The handling of the SDL2 frontend''s menus has been rewritten.  Game
  controller events are now mapped to keystrokes to invoke commands in the game (thanks
  to Alberto Mardegan).</p>

  <p dir="auto">The changes for the borg automatic player are too numerous to list
  individually.  They correct many crashes, instances where manual intervention was
  needed to allow the borg to make progress, jumping into lava, or cases where the
  borg misused a spell (thanks to Adam Goodman, Aodhlin, Jordan Philyaw, and NetBrian).</p>

  <p dir="auto">There is one change that can break compatibility with a game in progress
  or prevent reuse of a randart file from earlier versions of 4.2:  the misnamed FIRE_BOLT72
  activation is now FIRE_BALL72.  If a game in progress uses randarts and an artifact
  has that activation, the randart file will fail to load.  A workaround is to edit
  the randart file and replace FIRE_BOLT72 with FIRE_BALL72.</p>

  <p dir="auto">Prebuilt binaries for NDS and 3ds are no longer available.  Patches
  to restore building Angband for those systems are welcome.</p>'
updated: '2025-12-16T06:19:40Z'
version: 4.2.6
version_title: Release 4.2.6
---
Angband is a graphical dungeon adventure game that uses textual characters to represent the walls and floors of a dungeon and the inhabitants therein, in the vein of games like NetHack and Rogue. If you need help in-game, press ?.