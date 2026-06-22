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
  thextech-3ds-assets-aod-v1.3.7.3.zip:
    size: 60025376
    size_str: 57 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.3/thextech-3ds-assets-aod-v1.3.7.3.zip
  thextech-3ds-assets-smbx13-v1.3.7.3.zip:
    size: 48012828
    size_str: 45 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.3/thextech-3ds-assets-smbx13-v1.3.7.3.zip
  thextech-3ds-v1.3.7.3.zip:
    size: 4224904
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.3/thextech-3ds-v1.3.7.3.zip
github: TheXTech/TheXTech
icon: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/icon/thextech_48.png
image: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/wiiu/wuhb-splash.png
image_length: 121515
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
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
stars: 395
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">Yesterday (The 19''th of June) I had the birthday. Today
  I releasing a new update of TheXTech for you all! In this release a set of bugs
  found during the 1.3.7.2 release has been fixed including some vanilla, including
  the cursed printing of the Chinese text. In addition, the file library has been
  optimised.</p>

  <p dir="auto"><a href="https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7.3-1">A
  HOTFIX RELEASE 1.3.7.3-1 IS OUT, USE IT INSTEAD OF THIS</a></p>

  <h1 dir="auto">Full changelog for 1.3.7.3</h1>

  <details><summary>Details</summary>

  <h2 dir="auto">New features:</h2>

  <h3 dir="auto">General</h3>

  <ul dir="auto">

  <li>Update LVLX/WLDX/SAVX loader to use new MDX file parser by ds-sloth (speeds
  up level/world loads on slow devices) (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Enabled running of Layers, Events, and LunaScript loops at the Outro screen
  to allow more dynamics (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Internationalisation</h3>

  <ul dir="auto">

  <li>Added localisation support for custom stars requirement messages shown when
  player attempts to enter a warp and they don''t have enough stars (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Behaviour changes</h3>

  <ul dir="auto">

  <li>Logic change for TheXTech-exclusive feature: portal warps will not trigger until
  the player has spent 10 frames without overlapping any portal warps (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h2 dir="auto">New vanilla bugfixes</h2>

  <ul dir="auto">

  <li>Fix SMBX 1.3 peculiarity where frozen NPCs would sometimes be rendered incorrectly,
  guarded by compat flag "fix-visual-bugs" [Modern Mode] (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix SMBX 1.3 bug where the swap power (ID 273) could result in unexpected deaths
  or softlocks if the players were in different sections, guarded by compat flag "fix-multiplayer-targeting"
  [Modern/Classic Mode] (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Shadowblitz16/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Shadowblitz16">@Shadowblitz16</a>
  for the report)</li>

  <li>Fix SMBX 1.3 bug where character passthrough blocks treated char 2-4''s ice
  balls as belonging to char 1, guarded by compat flag "fix-char-pass-balls" [Modern
  Mode] (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>
  for the report)</li>

  <li>Fix SMBX 1.3 bug where character passthrough blocks did not allow char 5''s
  fire/ice balls to pass through, guarded by compat flag "fix-char-pass-balls" [Modern
  Mode] (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix SMBX 1.3 bug where jumping out of a shoe above the section could cause it
  to despawn, guarded by compat flag "fix-npc-camera-logic" [Modern/Classic Mode]
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Fix SMBX 1.3 bug where player could get stuck in fairy state if they hit a fairy
  power while stoned, guarded by compat flag "fix-fairy-stuck-in-pipe" [Modern/Classic
  Mode] (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Fire-Ball54322/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Fire-Ball54322">@Fire-Ball54322</a>
  for the report)</li>

  </ul>

  <h2 dir="auto">TheXTech bugfixes</h2>

  <ul dir="auto">

  <li>Fixed an inability to save the state of the collected medals on triggering the
  game beat (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>,
  thanks to @Liebning for the report)</li>

  <li>Fixed a TTF text print bug from the version 1.3.7.2 that caused missing vertical
  offset on line breaking (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>,
  thanks to 呜哩哇啦 for the report)</li>

  <li>Wii: fix v1.3.7.2 bug where deleting an in-use controls profile could lead to
  a crash (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech v1.3.7 bug where popping an empty bubble (ID 283) could harm the
  player (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Fixed an inability to load a game pack from command line by path without slash
  ending (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>3DS: fix v1.3.7 bug where the title screen could get stuck at the right of the
  level (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fixed a crash caused by hit of invisible Block-88 with a coin inside while the
  Coin Swtich is active (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Bugfix: don''t continually loop if a load failure occurs when the restart level
  flag is set (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Bugfix: quit the episode if the hub level can''t be reloaded (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fixed an unexpected going to the last sub-hub level instead of the world map
  even explicit coordinates are been specified (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>,
  thanks to @Liebning for the report)</li>

  <li>Fixed the case when checkpoints won''t reset when successfully quitting a level
  via warp exits, guarded by compat flag "fix-warp-exit-checkpoints" [Modern Mode]
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed the unwanted triggering of the IME candidates window during the gameplay
  use of the keyboard when PinYin or any other IME method is enabled. (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
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

  <li>On Windows XP SP0 that uses <strong>S3 Savage 4</strong> video card is impossible
  to dynamically switch video modes: the game just crashes (blame video drivers by
  theme selves as they were always very bad, according to <a href="https://www.kv.by/forum/forum1000000590.htm"
  rel="nofollow">random talk of people from the 2000s</a> (in Russian) ).</li>

  <li>On Linux/Wayland, Window icon can''t be changed while running game. (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2973606814" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/939" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/939/hovercard" href="https://github.com/TheXTech/TheXTech/issues/939">#939</a>)</li>

  <li>On Linux/Wayland, Mouse cursor doesn''t gets unlocked from window on toggling
  windowed mode after fullscreen. (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2965199291" data-permission-text="Title is private" data-url="https://github.com/TheXTech/TheXTech/issues/937"
  data-hovercard-type="issue" data-hovercard-url="/TheXTech/TheXTech/issues/937/hovercard"
  href="https://github.com/TheXTech/TheXTech/issues/937">#937</a>)</li>

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
updated: '2026-06-19T22:26:38Z'
version: v1.3.7.3
version_title: 'TheXTech v1.3.7.3: A release done in my birthday!'
website: https://wohlsoft.ru/projects/TheXTech/
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features. The original SMBX assets are not included, but a compatible preservation asset packs are available from wohlsoft.ru.