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
  thextech-3ds-assets-aod-v1.3.7.2.zip:
    size: 41307411
    size_str: 39 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.2/thextech-3ds-assets-aod-v1.3.7.2.zip
  thextech-3ds-assets-smbx13-v1.3.7.2.zip:
    size: 46188245
    size_str: 44 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.2/thextech-3ds-assets-smbx13-v1.3.7.2.zip
  thextech-3ds-v1.3.7.2.zip:
    size: 4271317
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7.2/thextech-3ds-v1.3.7.2.zip
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
stars: 366
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">There are many important bugfixes introduced since the
  previous 1.3.7.1 release, and implemented some more of convenience.</p>

  <p dir="auto">And also, since this version, the loading screen is now fully localisable,
  and the rest of mainstream TheXTech-based games already introduced translated loading
  screen into Russian, Chinese and Japanese languages! (<a href="https://github.com/orgs/TheXTech/discussions/1024#discussioncomment-14065643">Details
  here</a>)</p>

  <h1 dir="auto">Full changelog for 1.3.7.2</h1>

  <details><summary>Details</summary>

  <h2 dir="auto">New features:</h2>

  <h3 dir="auto">Video system</h3>

  <ul dir="auto">

  <li>Added an ability to assign some TTF font per language (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Internationalisation</h3>

  <ul dir="auto">

  <li>i18n: Added support for the localisation of the loading screen (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>i18n: Removed the support for legacy placement of translations outside the i18n
  sub-directory since no production projects used it. (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Controls</h3>

  <ul dir="auto">

  <li>Controls: add Alt Menu Controls option to controller profiles, which makes Jump
  act as Back and Alt Jump act as Confirm, to improve experience on Japanese-layout
  controllers (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h3 dir="auto">Behaviour changes</h3>

  <ul dir="auto">

  <li>Vanilla mode: reset score between gameplay sessions, like SMBX 1.3 (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Modern mode: allow static, always-shown NPCs (eg, O or bullet shooters) to deactivate
  while onscreen (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Menus: Alt Run is now used to erase options, instead of Alt Jump (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Menus: Alt Jump may now advance message boxes and start levels, guarded by existing
  compat flag "multiplayer-pause-controls" [Modern/Classic Mode] (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Controls: re-use controller profile when connected on different interfaces (<a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Controls: remove ability to load controller profiles saved by versions before
  v1.3.6 (2022) (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Controls: allow deleting a profile in use. This will allow the controller''s
  profile to be reset. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Logic change: when modern (LVLX) autoscroll hits the end of the section, it
  now keeps the current camera size instead of resetting the camera to 800x800 as
  in SMBX 1.3 (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Logic change: the terminal velocity for rail/lineguide platforms has been increased
  from 16 to 40 to address compatibility issues at some levels where falling speed
  is not enough to beat the challenge. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h2 dir="auto">Hardware support</h2>

  <ul dir="auto">

  <li>Controls: adjusted support for Wii Remote and Wii Remote with Nunchuk controllers
  on Wii U. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h2 dir="auto">New vanilla bugfixes</h2>

  <ul dir="auto">

  <li>Fixed the SMBX 1.3 bug where the engine would appear to break if an AutoStart
  event (other than "Level - Start") changed section bounds, guarded by compat flag
  "modern-section-change" [Modern/Classic Mode] (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix SMBX 1.3 crash caused by hitting a coin switch while on a slope (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to Peter Smith for the report)</li>

  <li>Fixed vanilla crash bug caused by division by zero on rendering of Background2-25
  with a texture width smaller than 800 and when the section has an exact width of
  800 (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed vanilla bug from the SMBX 1.3 that caused Character 5 to render an incorrect
  (mostly empty) frame while passing vertical pipes. (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h2 dir="auto">TheXTech bugfixes</h2>

  <ul dir="auto">

  <li>Fonts: Fixed the incorrect vertical alignment of some TTF glyph. (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Controls: fix v1.3.6 bug where controller was assigned the wrong profile after
  its original profile was deleted (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Controls: fix face button labels on Switch port. (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Controls: fix v1.3.6 bug where closing the Enter Code screen with the Start
  button might prevent successful code entry (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Visuals: fix v1.3.7.1 bug where there was a black frame during the transition
  from the main menu to the asset pack select screen (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix v1.3.7.1 bug where npc-300.txt was not loaded properly - fixes spinning
  platforms in Lowser''s Conquest (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix v1.3.7.1 bug where default masks/outlines were not loaded for custom GIF
  player sprites, resulting in black boxes (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix v1.3.7.1 Modern/Classic bug where it was not safe to run on a series of
  fall blocks with gaps between them, caused by the downward clip fix introduced in
  v1.3.7.1 (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Desktop: fix a minor cosmetic bug where the screen could flicker when resizing
  the window (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fixed the v1.3.6 bug where skull raft with modern logic enabled will glitch
  when impacts a barrier being in a water (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix v1.3.1 inaccuracy where NPCs 69 and 70 were one pixel shorter than they
  are in SMBX 1.3 (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Fixed an inability to auto-create the screenshots directory on macOS (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix v1.3.7 bug where the engine would fail to load if the first encountered
  asset pack was invalid (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix v1.3.6 inaccuracy where warp-spawned NPCs would fail to be hidden if their
  layer was hidden immediately following spawn (their layer is set to "Spawned NPCs"
  when warp is complete) (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix v1.3.7.1 bug where static NPCs spawned by a generator could despawn while
  onscreen (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix v1.3.1 bug where whipping a turtle (with leaf power) would kill the turtle
  as well as releasing it from its shell (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  bug caught by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
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

  <li>On old 3DS the out-of-memory crash might happen with the stable version of the
  game. The solution is not yet backported from the devel branch.</li>

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
updated: '2025-12-26T22:21:13Z'
version: v1.3.7.2
version_title: 'TheXTech v1.3.7.2: Happy upcoming New 2026''th Year!'
website: https://wohlsoft.ru/projects/TheXTech/
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features. The original SMBX assets are not included, but a compatible preservation asset packs are available from wohlsoft.ru.