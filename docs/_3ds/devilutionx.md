---
author: diasurgical
avatar: https://avatars.githubusercontent.com/u/40645014?v=4
categories:
- game
color: '#695d5d'
color_bg: '#695d5d'
created: '2018-08-02T17:19:01Z'
description: Diablo build for modern operating systems
download_page: https://github.com/diasurgical/devilutionX/releases
downloads:
  devilutionx-3ds.3dsx:
    size: 13545168
    size_str: 12 MiB
    url: https://github.com/diasurgical/devilutionX/releases/download/1.5.0/devilutionx-3ds.3dsx
  devilutionx-3ds.cia:
    size: 12809152
    size_str: 12 MiB
    url: https://github.com/diasurgical/devilutionX/releases/download/1.5.0/devilutionx-3ds.cia
  devilutionx-amiga-m68k.zip:
    size: 6652944
    size_str: 6 MiB
    url: https://github.com/diasurgical/devilutionX/releases/download/1.5.0/devilutionx-amiga-m68k.zip
  devilutionx-miyoo-mini-miniui.zip:
    size: 5806915
    size_str: 5 MiB
    url: https://github.com/diasurgical/devilutionX/releases/download/1.5.0/devilutionx-miyoo-mini-miniui.zip
  devilutionx-miyoo-mini-onion-os.zip:
    size: 6010716
    size_str: 5 MiB
    url: https://github.com/diasurgical/devilutionX/releases/download/1.5.0/devilutionx-miyoo-mini-onion-os.zip
github: diasurgical/devilutionX
icon: https://raw.githubusercontent.com/diasurgical/devilutionX/master/Packaging/ctr/icon.png
image: https://raw.githubusercontent.com/diasurgical/devilutionX/master/Packaging/ctr/banner.png
image_length: 37280
layout: app
license: other
license_name: Other
qr:
  devilutionx-3ds.cia: https://db.universal-team.net/assets/images/qr/devilutionx-3ds-cia.png
source: https://github.com/diasurgical/devilutionX
systems:
- 3DS
title: devilutionX
unique_ids:
- '0x3F395'
update_notes: '<h3 dir="auto">Features</h3>

  <h4 dir="auto">Gameplay</h4>

  <ul dir="auto">

  <li>Floating damage numbers</li>

  <li>Option to auto-pick up oils</li>

  <li>Quest items now drop based on difficulty</li>

  </ul>

  <h4 dir="auto">Multiplayer</h4>

  <ul dir="auto">

  <li>All quests can now be played, enabled from settings menu</li>

  <li>Add chat commands, use <code class="notranslate">/help</code> for options</li>

  <li>Add PvP arenas that can be accessed via <code class="notranslate">/arena #</code></li>

  <li>Inspect other players'' items using <code class="notranslate">/inspect &lt;name&gt;</code></li>

  <li>Hellfire: Disabled The Cornerstone of the World</li>

  <li>Draw hostile players'' names in red in the chat panel</li>

  </ul>

  <h4 dir="auto">Platforms</h4>

  <ul dir="auto">

  <li>Added support for the original Xbox</li>

  <li>Added support for Android TV</li>

  <li>Added (experimental) support for RG99</li>

  <li>Provide virtual resolutions for systems with only one native resolution</li>

  <li>Android: Support loading data from external storage</li>

  <li>Android: Do not speed up game after suspending if playing alone</li>

  <li>Windows: Digitally signed executable</li>

  <li>Support demo playback on SDL1 versions</li>

  </ul>

  <h4 dir="auto">Graphics / Audio</h4>

  <ul dir="auto">

  <li>Option to show item graphics in stores</li>

  <li>More fluid lighting updates when moving</li>

  <li>Added map in town</li>

  <li>Add widescreen load screens (thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Chance4us/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Chance4us">@Chance4us</a>)</li>

  <li>Durability icon gradually changing to red</li>

  <li>Provide sound cue when gold is auto-placed into the open inventory</li>

  <li>Color inventory slot based on item quality</li>

  <li>Show cast animation in town</li>

  <li>Monsters end their invisibility on death</li>

  <li>Make the ground color of small rejuvenation potions distinct</li>

  <li>Add setting for choosing a different audio resampler</li>

  <li>Support for recoloring heroes using trn-files</li>

  <li>Indicate on which difficulty a hero has defeated Diablo</li>

  <li>Use decimal separators for gold and XP</li>

  <li>Improve the monster HP bar for some edge cases</li>

  <li>Only display resolution height when FitToScreen is enabled</li>

  <li>Various text rendering improvements</li>

  </ul>

  <h4 dir="auto">Controls</h4>

  <ul dir="auto">

  <li>Do not target monster when casting Heal Other and Resurrect</li>

  <li>Improve logic for belt auto-refill</li>

  <li>Adjust the info panel descriptions based on the input device</li>

  <li>keyboard/mouse: Additional mapping options</li>

  <li>keyboard/mouse: Support back button in menus</li>

  <li>gamepad/touch: Improve menu navigation</li>

  <li>gamepad: Controls can now be mapped</li>

  <li>gamepad: Autodetect button layout</li>

  </ul>

  <h4 dir="auto">Translations</h4>

  <ul dir="auto">

  <li>Update French translation</li>

  <li>Update Italian translation</li>

  <li>Update Japanese translation</li>

  <li>Update Polish translation</li>

  <li>Update Spanish translation</li>

  <li>Update Ukrainian translation</li>

  <li>Synchronize names of existing items with the current game language</li>

  <li>Xbox One/Series: Include translations</li>

  <li>Add <code class="notranslate">--lang</code> for specifying the language</li>

  </ul>

  <h4 dir="auto">Stability / Performance / System</h4>

  <ul dir="auto">

  <li>Create submenus for setting groups</li>

  <li>Date based screenshot names</li>

  <li>Performance improvement</li>

  <li>Reduce RAM usage</li>

  <li>Frame skipping on low end systems</li>

  <li>Setting for picking audio device</li>

  </ul>

  <h3 dir="auto">Bugfixes</h3>

  <h4 dir="auto">Gameplay</h4>

  <ul dir="auto">

  <li>Attack speed not always being accurate for specific combinations of effects
  and actions</li>

  <li>Hellfire: Books from Adria''s shop morphing</li>

  <li>Petrified monsters shifting position when hit after loading a save game</li>

  <li>Don''t consume mana when double casting Mana Shield</li>

  <li>Telekinesis respects the Disable Crippling Shrines setting</li>

  </ul>

  <h4 dir="auto">Multiplayer</h4>

  <ul dir="auto">

  <li>Items held by cursor lost due to lag cursor</li>

  <li>Items lost due to various desync issues</li>

  <li>Fix multiple desync issues</li>

  <li>Don''t show hostile players on the map</li>

  <li>Player animations sometimes not being in sync</li>

  <li>Better handling of latency</li>

  </ul>

  <h4 dir="auto">Platforms</h4>

  <ul dir="auto">

  <li>Windows: Fix ZeroTier always failing for Unicode usernames</li>

  <li>Vita: Items lost when tapping outside the inventory</li>

  <li>Fix gold withdrawal on SDL1 versions</li>

  <li>macOS/iOS translate system texts</li>

  <li>Translation support on BE systems</li>

  </ul>

  <h4 dir="auto">Graphics / Audio</h4>

  <ul dir="auto">

  <li>Top of screen not being rendered at some resolutions</li>

  <li>Correct alignment of lightning and inferno</li>

  <li>Make item labels take UI into consideration</li>

  <li>Adria''s "you have nothing to recharge" being misalignment on an empty list</li>

  <li>Monsters sometimes not being rendered</li>

  <li>Lighting missing for some areas after loading a saved game</li>

  <li>Hellfire quests being removed from the quest log when completed</li>

  </ul>

  <h4 dir="auto">Controls</h4>

  <ul dir="auto">

  <li>Hero sometimes not willing to drop an item even when there is still room on
  the ground</li>

  <li>touch: Missing buttons on low end devices</li>

  </ul>

  <h4 dir="auto">Stability / Performance / System</h4>

  <ul dir="auto">

  <li>Allow using the built-in screenshot function during text input</li>

  <li>Various crashes</li>

  <li>Resolve a few bugs and edge cases with the stash</li>

  <li>A rare freeze when loading hell levels</li>

  <li>Various issues with cursor rendering</li>

  <li>Some additional validation of items when converting saves from Hellfire to Diablo</li>

  </ul>

  <h3 dir="auto">Bugfixes for original Diablo bugs</h3>

  <h4 dir="auto">Gameplay</h4>

  <ul dir="auto">

  <li>Several issues that would cause missiles to miss when they shoudn''t</li>

  <li>Some wall tiles not blocking missiles and vision</li>

  <li>The player can spawn in an incorrect location on some levels</li>

  <li>Missing the extra stats at level 50</li>

  <li>Guardian not calculating its damage correctly</li>

  <li>Diablo not giving the intended XP on Hell difficulty</li>

  <li>Fireball/Elemental not doing damage when monster is not in line of sight</li>

  <li>Lightning spell being able to pass through some walls</li>

  <li>Double casting of spells</li>

  <li>Low quality items on quests after using a town portal</li>

  <li>Monsters on Nightmare and Hell having too little HP</li>

  <li>Monsters being immune to non-player missiles</li>

  <li>Stairs up to level 6 not working sometimes</li>

  <li>The Deadly Hunter bow not dealing the correct damage</li>

  <li>Spell remaining unavailable after using a stone shrine until reequipping the
  staff</li>

  <li>Fast and faster hit recovery stacking</li>

  <li>Incorrect calculation for max chages lost with when using the recharge skill</li>

  <li>Not getting XP after damaging a monster if it dies from a trap</li>

  <li>Fire Arrows causing monsters to stop healing</li>

  </ul>

  <h4 dir="auto">Multiplayer</h4>

  <ul dir="auto">

  <li>Trapped doors rearming themselves when returning to a level</li>

  <li>Resolve some sources of dsync</li>

  </ul>

  <h4 dir="auto">Graphics / Audio</h4>

  <ul dir="auto">

  <li>Incorrect Armor Class in Char Panel</li>

  <li>Petrified monsters turning to face the attacker</li>

  <li>Petrified monster sliding after having been stone cursed</li>

  <li>Show portal animation in town</li>

  <li>Broken corners on some cathedral levels</li>

  <li>Inconsistent lighting on quest levels</li>

  <li>Light smearing when walking in certain directions</li>

  <li>Unique monsters light not always following the monster</li>

  <li>Unique monster light being left behind when they are removed</li>

  <li>Minor rendering bugs in UI panels</li>

  <li>Center 2x2 items that go in 2x3 slots</li>

  <li>Player moonwalking when talking to monsters</li>

  <li>Tavern Sign playing the wrong sound when dropped on the floor</li>

  <li>Poisoned Water not appearing in the quest log if discovered before talking to
  Pepin</li>

  <li>Camera shaking when loading a save game after Diablo''s death</li>

  <li>Add scrollbar to help window</li>

  </ul>

  <h4 dir="auto">Controls</h4>

  <ul dir="auto">

  <li>Unable to pick Golem spawn location when right-clicking the scroll</li>

  <li>Casting spells during level transition will target the old position</li>

  <li>Help panel staying open while talking to NPCs</li>

  </ul>

  <h4 dir="auto">Stability / Performance / System</h4>

  <ul dir="auto">

  <li>Town portal not always returning to the correct quest level</li>

  <li>Items lost when triggering a portal while picking them up</li>

  <li>Optic Amulet and Arkaine''s Valor sometimes being misaligned</li>

  <li>Minor stability issues</li>

  </ul>

  <h3 dir="auto">Bugfixes for original Hellfire bugs</h3>

  <h4 dir="auto">Gameplay</h4>

  <ul dir="auto">

  <li>Prevent oil of death damage wrap around</li>

  <li>Reflected damage sometimes being too low</li>

  </ul>

  <h4 dir="auto">Multiplayer</h4>

  <ul dir="auto">

  <li>Desync in Nest when cow quest is enabled</li>

  <li>Being unable to pick up quest items if you didn''t start the game</li>

  <li>Quest going out of sync</li>

  </ul>

  <h4 dir="auto">Graphics / Audio</h4>

  <ul dir="auto">

  <li>Gillian saying the grave quest start line multiple times</li>

  <li>Buggy lighting in Nest and Crypt</li>

  <li>Description of jester''s item saying 500% instead of 600% damage</li>

  <li>Typos in subtitles</li>

  </ul>

  <h3 dir="auto">Known issues</h3>

  <ul dir="auto">

  <li>macOS build requires macOS 12+</li>

  <li>Level 4 with Snotspill generates an incompatible layout</li>

  <li>touch: There can be issues with activating scrolls using</li>

  </ul>'
updated: '2023-06-13T19:43:34Z'
version: 1.5.0
version_title: 1.5.0
wiki: https://github.com/diasurgical/devilutionX/wiki
---
