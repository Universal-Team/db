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
  download_page: https://github.com/angband/angband/releases/tag/4.2.6-117-gf1f841fe7
  downloads:
    Angband-4.2.6-117-gf1f841fe7-3ds.zip:
      size: 24671230
      size_str: 23 MiB
      url: https://github.com/angband/angband/releases/download/4.2.6-117-gf1f841fe7/Angband-4.2.6-117-gf1f841fe7-3ds.zip
    Angband-4.2.6-117-gf1f841fe7-nds.zip:
      size: 23328934
      size_str: 22 MiB
      url: https://github.com/angband/angband/releases/download/4.2.6-117-gf1f841fe7/Angband-4.2.6-117-gf1f841fe7-nds.zip
  update_notes: '<p dir="auto">Because of a bug in the check_break() changes, this
    release will hang if there is input queued while it is the monsters'' turn to
    act or when generating a new level.  Use one of the other prereleases instead.</p>

    <h2 dir="auto">What''s Changed</h2>

    <ul dir="auto">

    <li>Plug leak of monster''s shape name if it specifies a monster base by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4276108663" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6595"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6595/hovercard"
    href="https://github.com/angband/angband/pull/6595">#6595</a></li>

    <li>Be more specific about the hitpoints drained by Vampire Strike by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4285535924" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6596"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6596/hovercard"
    href="https://github.com/angband/angband/pull/6596">#6596</a></li>

    <li>Correct out-of-date comment in Makefile.std by <a class="user-mention notranslate"
    data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4288139969" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6597"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6597/hovercard"
    href="https://github.com/angband/angband/pull/6597">#6597</a></li>

    <li>cmake: fix SUPPORT_STATS_BACKEND=ON by <a class="user-mention notranslate"
    data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4289006606" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6598"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6598/hovercard"
    href="https://github.com/angband/angband/pull/6598">#6598</a></li>

    <li>cmake:  macro arguments can not be used as variables with if() by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4291212402" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6601"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6601/hovercard"
    href="https://github.com/angband/angband/pull/6601">#6601</a></li>

    <li>docs:  rearrange compiling instructions by <a class="user-mention notranslate"
    data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4292305786" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6602"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6602/hovercard"
    href="https://github.com/angband/angband/pull/6602">#6602</a></li>

    <li>workflows: hw.activecpu better choice than hw.ncpu for macOS parallel builds
    by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4292503565" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6603"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6603/hovercard"
    href="https://github.com/angband/angband/pull/6603">#6603</a></li>

    <li>cmake: fix copy of generated user manual to the self-contained game by <a
    class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4292607731" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6604"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6604/hovercard"
    href="https://github.com/angband/angband/pull/6604">#6604</a></li>

    <li>Add check_break() to help keep the game responsive during long calculations
    by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4298743450" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6607"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6607/hovercard"
    href="https://github.com/angband/angband/pull/6607">#6607</a></li>

    <li>Expeditiously shut down in response to SIGPWR and SIGDANGER by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/backwardsEric/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/backwardsEric">@backwardsEric</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="4309232351" data-permission-text="Title is private" data-url="https://github.com/angband/angband/issues/6610"
    data-hovercard-type="pull_request" data-hovercard-url="/angband/angband/pull/6610/hovercard"
    href="https://github.com/angband/angband/pull/6610">#6610</a></li>

    </ul>

    <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/angband/angband/compare/4.2.6-107-g64d78d7f6...4.2.6-117-gf1f841fe7"><tt>4.2.6-107-g64d78d7f6...4.2.6-117-gf1f841fe7</tt></a></p>'
  update_notes_md: 'Because of a bug in the check_break() changes, this release will
    hang if there is input queued while it is the monsters'' turn to act or when generating
    a new level.  Use one of the other prereleases instead.


    ## What''s Changed

    * Plug leak of monster''s shape name if it specifies a monster base by @backwardsEric
    in https://github.com/angband/angband/pull/6595

    * Be more specific about the hitpoints drained by Vampire Strike by @backwardsEric
    in https://github.com/angband/angband/pull/6596

    * Correct out-of-date comment in Makefile.std by @backwardsEric in https://github.com/angband/angband/pull/6597

    * cmake: fix SUPPORT_STATS_BACKEND=ON by @backwardsEric in https://github.com/angband/angband/pull/6598

    * cmake:  macro arguments can not be used as variables with if() by @backwardsEric
    in https://github.com/angband/angband/pull/6601

    * docs:  rearrange compiling instructions by @backwardsEric in https://github.com/angband/angband/pull/6602

    * workflows: hw.activecpu better choice than hw.ncpu for macOS parallel builds
    by @backwardsEric in https://github.com/angband/angband/pull/6603

    * cmake: fix copy of generated user manual to the self-contained game by @backwardsEric
    in https://github.com/angband/angband/pull/6604

    * Add check_break() to help keep the game responsive during long calculations
    by @backwardsEric in https://github.com/angband/angband/pull/6607

    * Expeditiously shut down in response to SIGPWR and SIGDANGER by @backwardsEric
    in https://github.com/angband/angband/pull/6610



    **Full Changelog**: https://github.com/angband/angband/compare/4.2.6-107-g64d78d7f6...4.2.6-117-gf1f841fe7'
  updated: '2026-04-28T13:06:31Z'
  version: 4.2.6-117-gf1f841fe7
  version_title: 4.2.6-117-gf1f841fe7
source: https://github.com/angband/angband
stars: 1505
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