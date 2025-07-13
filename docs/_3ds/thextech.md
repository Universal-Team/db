---
author: TheXTech Developers
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/160427994?v=4
categories:
- game
color: '#5f6dc0'
color_bg: '#3f4880'
created: '2020-02-12T20:02:49Z'
description: The full port of the SMBX engine from VB6 into C++ and SDL2, FreeImage
  and MixerX
download_filter: 3ds
download_page: https://github.com/TheXTech/TheXTech/releases
downloads:
  thextech-3ds-assets-aod-v1.3.7.1.zip:
    size: 42509750
    size_str: 40 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.1/thextech-3ds-assets-aod-v1.3.7.1.zip
  thextech-3ds-assets-smbx13-v1.3.7.1.zip:
    size: 45872778
    size_str: 43 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.1/thextech-3ds-assets-smbx13-v1.3.7.1.zip
  thextech-3ds-v1.3.7.1.zip:
    size: 4237894
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.1/thextech-3ds-v1.3.7.1.zip
github: TheXTech/TheXTech
icon: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/icon/thextech_48.png
image: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/wiiu/wuhb-splash.png
image_length: 121515
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  downloads:
    thextech-3ds-main.zip:
      url: https://builds.wohlsoft.ru/3ds/thextech-3ds-main.zip
screenshots:
- description: Editor
  url: https://db.universal-team.net/assets/images/screenshots/thextech/editor.png
- description: Loading
  url: https://db.universal-team.net/assets/images/screenshots/thextech/loading.png
- description: Smbx menu
  url: https://db.universal-team.net/assets/images/screenshots/thextech/smbx-menu.png
- description: Smbx title
  url: https://db.universal-team.net/assets/images/screenshots/thextech/smbx-title.png
source: https://github.com/TheXTech/TheXTech
stars: 337
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">This update features a lot of platform-related improvements
  and stabilisation. Since this update the exclusive full-screen modes on some platforms
  (such as retro computers) are supported to maintain the graphics performance which
  is impossible with the regular configuration and windowed mode.</p>

  <h1 dir="auto">Full changelog for 1.3.7.1</h1>

  <details>

  <h2 dir="auto">New features:</h2>

  <h3 dir="auto">Video system</h3>

  <ul dir="auto">

  <li>Implemented support for Power-of-Two only textures on some platforms via SDL
  Render (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Added exclusive full-screen mode support to maintain good performance on weak
  devices (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Add 3x scale mode (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Yave-Yu/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Yave-Yu">@Yave-Yu</a>
  for the request)</li>

  </ul>

  <h3 dir="auto">Gameplay settings</h3>

  <ul dir="auto">

  <li>Added compat flag "no-shell-grab-top" to disable grabbing shells while falling
  from above, for compatibility with pre-SMBX 1.3 content (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Behaviour changes</h3>

  <ul dir="auto">

  <li>Advanced options are now applied only when hitting Select or returning to the
  previous screen. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>
  for the suggestion)</li>

  <li>The mouse can now be used to click through message boxes in the main menu. (<a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Agatha/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Agatha">@Agatha</a>
  for the suggestion)</li>

  <li>Refine Magic Block handling of lava next to slopes (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ChristianSilvermoon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ChristianSilvermoon">@ChristianSilvermoon</a>
  for the report)</li>

  <li>Adjusted the frame-skip behaviour to address the performance slowdown on some
  systems (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Windows: use SDL2 renderer on video cards without OpenGL acceleration (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Added an explicit indication that game is suspended when window is out of focus
  by showing the "Paused" label over the gray filter. (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Rapidly clicking on menu items no longer toggles fullscreen. (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Agatha/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Agatha">@Agatha</a>
  for the suggestion)</li>

  <li>On failures while using interprocess-based level testing, the explicit error
  messages will be shown (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h2 dir="auto">Hardware support</h2>

  <ul dir="auto">

  <li>Add GameCube controller support for Wii (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>3DS: fix bug where gameplay could slow down when audio performance is reduced
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Wii: fix bug where Wiimote could get stuck in Rumble state (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fixed the viewport problem on non-SMBX resolutions at the PS Vita (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h2 dir="auto">New vanilla bugfixes</h2>

  <ul dir="auto">

  <li>Fix vanilla bug where chars 3 and 4 could clip downwards if they powered up
  while digging, guarded by "fix-player-grab-clip" [Classic Mode] (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix SMBX 1.3 crash caused by freezing a bubble when the NPC with index 3 is
  an ice ball (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix vanilla bug where the player could clip downwards when hurt or running into
  a block while on a platform, guarded by existing compat flag "fix-player-downward-clip"
  [Classic Mode] (affected Frozen Valley in Fallen Spirits and Mushroom Heights in
  Princess Cliche) (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Agatha/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Agatha">@Agatha</a>
  for the report)</li>

  <li>Fix vanilla editor peculiarity where the order of overlapping blocks might change.
  Note that overlapping blocks larger than 1 tile are still sorted according to SMBX
  rules. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h2 dir="auto">TheXTech bugfixes</h2>

  <ul dir="auto">

  <li>Fix TheXTech 1.3.7 peculiarity where NPCs that hid themselves on activation
  would be shown before coming onscreen (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.7 peculiarity where player preview sprites in the main menu
  would not use the correct death effects (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where a plant on a hidden moving layer would sometimes
  not appear after showing the layer (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed a bug from the TheXTech 1.3.6 where music of a wrong section gets started
  when player enters level by a warp into section with no music (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix TheXTech 1.3.7 bug where rail platforms could get stuck below the current
  section (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Fix TheXTech 1.3.5.3 visual bug where P2''s screen fader was not reset when
  P1 gets a level exit (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 visual change in the width of spaces in the in-game message
  box (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.7 visual change in the line-breaking algorithm for the in-game
  message box (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Tune TheXTech v1.3.7 Modern/Classic Mode logic for when to activate NPCs shown
  by events to better match Vanilla. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Resolved the pool allocator memory overflow crash problem (Caused by LunaScript''s
  render operations with frame skipping enabled on slow devices) (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where setting width or height to 0 in npc.txt would
  prevent the NPC from spawning (this affected the boss of Hall of Masks in MM4) (<a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where colored platform NPCs could mistakenly trigger
  activation events (this affected The Sinister Side in SRW) (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.1 inaccuracy where certain internal values were not rounded
  correctly (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.1 bug where characters 2 and 5 couldn''t release all coins
  in a block if the block was in front of another sizable block (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix loading of custom resolution specified in thextech.ini (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.7 bug where medals were incorrectly tracked after using Coin
  Switch in Classic Mode (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Agatha/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Agatha">@Agatha</a>
  for the report)</li>

  <li>Fix TheXTech 1.3.7 editor bug where sizable block priority was not used when
  resizing sizable blocks (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ChristianSilvermoon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ChristianSilvermoon">@ChristianSilvermoon</a>
  for the report)</li>

  <li>Fix TheXTech v1.3.7 change to the timing of events triggered by warp enter/exit
  events (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ChristianSilvermoon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ChristianSilvermoon">@ChristianSilvermoon</a>
  for the report)</li>

  <li>Fix TheXTech v1.3.6.1 inaccuracy where generator NPCs with IDs 57, 60, 62, 64,
  and 66 could not be walked on in their generator state (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.7-beta bug which prevented the compat flag "fix-player-clip-wall-at-npc"
  from working as intended (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech v1.3.7-beta visual bug in which the backdrop did not have proper
  borders in 4P split screen at 1440p. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech v1.3.7 bug in which input methods might get disconnected when switching
  between battle leves in 3/4-player mode. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech v1.3.7-beta bug in which bullet generators not facing the player
  could become inactive. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Fix critical TheXTech v1.3.6 editor bug where swapping the order of layers resulting
  in objects losing their layers. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ChristianSilvermoon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ChristianSilvermoon">@ChristianSilvermoon</a>
  for the report)</li>

  <li>Fix TheXTech v1.3.6 editor bug where world music tiles would move a tiny bit
  when the world was saved (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ChristianSilvermoon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ChristianSilvermoon">@ChristianSilvermoon</a>
  for the report)</li>

  <li>Fixed the early interrupting of the level workflow when going to the inter-level
  warp on some platforms (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed the visual glitch of the last screen fade out frame being frozen instead
  of complete going into darkness (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed the bug that causes gamesave''s fails counter not being copied or removed
  via game menu (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix TheXTech 1.3.7-beta editor bug where a player object could become deselected
  when closing the editor pane (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @fbitninja for the report)</li>

  <li>Fixed the incorrect work of the Java-coded INI parser on Android that led some
  properties being loaded incorrectly (for example, valid background picture fails
  to load) (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  </details>

  <h1 dir="auto">Known issues</h1>

  <ul dir="auto">

  <li>Audio may be choppy on Old 3DS.</li>

  <li>Texture load stutter is present on Wii.</li>

  <li>The screen may slightly judder during section resizes on 3DS and Wii.</li>

  <li>On 3DS, background texture may start to flashing. (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2501320790" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/816" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/816/hovercard" href="https://github.com/TheXTech/TheXTech/issues/816">#816</a>)
  (Possibly solved, the primary reason of this is an out of memory).</li>

  <li>On 3DS the crash happens on attempt to quit by the home menu. (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2165417679" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/738" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/738/hovercard" href="https://github.com/TheXTech/TheXTech/issues/738">#738</a>)</li>

  <li>On Windows 10 when running OpenGL with some ~2006 Intel iGPU on laptop, game
  would crash (possibly fixed).</li>

  <li>On Windows 10 with the Intel Iris Xe graphics, textures gets drawn corrupted.
  (github.com/<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="2666816824" data-permission-text="Title is private" data-url="https://github.com/TheXTech/TheXTech/issues/859"
  data-hovercard-type="issue" data-hovercard-url="/TheXTech/TheXTech/issues/859/hovercard"
  href="https://github.com/TheXTech/TheXTech/issues/859">/issues/859</a>)</li>

  <li>On Windows XP SP0 that uses <strong>S3 Savage 4</strong> video card is impossible
  to dynamically switch video modes: the game just crashes (blame video drivers by
  theme selves as they were always very bad, accordign to <a href="https://www.kv.by/forum/forum1000000590.htm"
  rel="nofollow">random talk of people from the 2000s</a> (in Russian) ).</li>

  <li>On Linux/Wayland, Window icon can''t be changed while running game. (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2973606814" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/939" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/939/hovercard" href="https://github.com/TheXTech/TheXTech/issues/939">#939</a>)</li>

  <li>On Linux/Wayland, Mouse cursor doesn''t gets unlocked from window on toggling
  windowed mode after fullscreen. (github.com/<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2965199291" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/937" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/937/hovercard" href="https://github.com/TheXTech/TheXTech/issues/937">/issues/937</a>)</li>

  <li>Editor doesn''t supports large fonts (I.e. Chinese, Korean, etc). (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2791602944" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/884" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/884/hovercard" href="https://github.com/TheXTech/TheXTech/issues/884">#884</a>)</li>

  <li>At Web version (Emscripten-built) the framerate may go incorrectly. (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2628102912" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/851" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/851/hovercard" href="https://github.com/TheXTech/TheXTech/issues/851">#851</a>)</li>

  <li>On some hardware, randomly and rare, alpha-channel might me messed up when using
  OpenGL render backend. (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2213103655" data-permission-text="Title is private" data-url="https://github.com/TheXTech/TheXTech/issues/743"
  data-hovercard-type="issue" data-hovercard-url="/TheXTech/TheXTech/issues/743/hovercard"
  href="https://github.com/TheXTech/TheXTech/issues/743">#743</a>)</li>

  </ul>'
updated: '2025-07-13T00:24:59Z'
version: v1.3.7.1
version_title: 'TheXTech v1.3.7.1: A large pile of bugfixes with a taste of new features
  has arrived!'
website: https://wohlsoft.ru/projects/TheXTech/
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features. The original SMBX assets are not included, but a compatible preservation asset packs are available from wohlsoft.ru.