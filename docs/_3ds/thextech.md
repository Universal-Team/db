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
  thextech-3ds-assets-aod-v1.7.4.zip:
    size: 60781909
    size_str: 57 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.7.4/thextech-3ds-assets-aod-v1.7.4.zip
  thextech-3ds-assets-smbx13-v1.7.4.zip:
    size: 48045837
    size_str: 45 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.7.4/thextech-3ds-assets-smbx13-v1.7.4.zip
  thextech-3ds-v1.7.4.zip:
    size: 4227637
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.7.4/thextech-3ds-v1.7.4.zip
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
stars: 417
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">This is not a usual update. While it offers several bugfixes
  and features, it has three significant changes:</p>

  <ul dir="auto">

  <li>The first release with the official iOS and tvOS support!</li>

  <li>Compiled Haiku binary releases are now available!</li>

  <li>We changing the versioning model!</li>

  </ul>

  <h1 dir="auto">iOS and tvOS support</h1>

  <p dir="auto">Since the foundation of the project of TheXTech it was never available
  at Apple mobile platforms such as iOS. And since this release it''s now possible
  to build and install the engine on iOS-powered devices such as iPhone, iPad, and
  iPod Touch. However, this doesn''t means the game app will be available at the AppStore.
  Instead it''s available in a form of the IPA package that you need to install on
  your device using the Sideload method or build it from the source code using suitable
  Xcode kit on your Mac. All the details you can find at the TheXTech''s Wiki documentation.</p>

  <h1 dir="auto">Haiku binary releases</h1>

  <p dir="auto">Before this release it was a challenge to build the suitable CI image
  to automatise producing of binary release for the Haiku platform. And thanks to
  the <a href="https://github.com/cross-platform-actions">Cross-platform Actions</a>
  project, this became easy, and now TheXTech finally has the binary release for the
  Haiku operating system!</p>

  <h1 dir="auto">Versioning system change</h1>

  <p dir="auto">The old format of versioning of "1.3.x.y" was <a href="https://github.com/orgs/TheXTech/discussions/353">a
  major problem for a while</a>. It sets a lot of limits and prevents to properly
  release important hotfixes and let several package managers to properly handle them.
  Since this version the ".3." part of the version gets completely removed, and instead
  of "1.3.7.4" we are releasing "1.7.4"!</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/33d6875c-6856-4ee7-a747-141e41126061"><img
  width="228" height="88" alt="thextech-1 7 4" src="https://github.com/user-attachments/assets/33d6875c-6856-4ee7-a747-141e41126061"
  style="max-width: 100%; height: auto; max-height: 88px;; aspect-ratio: 228 / 88;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <h1 dir="auto">Full changelog for 1.7.4</h1>

  <details><summary>Details</summary>

  <h2 dir="auto">New features:</h2>

  <h3 dir="auto">General</h3>

  <ul dir="auto">

  <li>Versioning system has been changed, now next releases will be done without the
  ".3." midfix (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Platforms support</h3>

  <ul dir="auto">

  <li>Added support for the iOS platform (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Added support for the tvOS platform (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Internationalisation</h3>

  <ul dir="auto">

  <li>i18n: On-screen warning messages (such as bitmask render warnings) are now translatable!
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">Controls</h3>

  <ul dir="auto">

  <li>Controls: Added an ability to configure offsets for buttons at the touch-screen
  controller (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h3 dir="auto">LunaScript</h3>

  <ul dir="auto">

  <li>LunaScript: Added the "ShakeScreen" command to trigger the screen shaking without
  using of boom blocks (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>LunaScript: Added the "SpawnEffect" command to spawn a simple static graphical
  effect (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>LunaScript: Added SFX commands "PlaySFXPausable", "PlaySFXSection", and "PlaySFXSctPausable"
  to allow pause during dialogues and pause menu, and lock at the specific section.
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  </ul>

  <h2 dir="auto">New vanilla bugfixes</h2>

  <ul dir="auto">

  <li>Fix SMBX 1.3 bug where items on top of a vehicle could be lost when entering
  it, guarded by compat flag "fix-vehicle-item-loss" [Modern/Classic Mode] (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix SMBX 1.3 bug where a climbable NPC spawner (eg, vine top) would deactivate
  if the player left the section, guarded by compat flag "fix-npc-camera-logic" [Modern/Classic
  Mode] (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>
  for the report)</li>

  <li>Fix SMBX 1.3 bug where the players could disappear if a tape exit was touched
  while a player was eaten or dead. (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h2 dir="auto">TheXTech bugfixes</h2>

  <ul dir="auto">

  <li>Fix TheXTech 1.3.6.1 bug where Toothy (NPC ID 50) would sometimes become invisible
  while the player is holding the toothy pipe (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to @Liebning for the report)</li>

  <li>Controls: Fixed the problem of touch-screen controller''s defaults are not loaded
  when profile gets just created (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed broken user directory handling on the Haiku (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix TheXTech 1.3.7 bug where ghosts could follow the direction of an eaten player
  instead of the active player. [Modern Mode] (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.5.3 bug where an extra line of pixels was rarely drawn below
  the player. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where fonts could get corrupted after unloading a customized
  level font. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ChristianSilvermoon/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ChristianSilvermoon">@ChristianSilvermoon</a>
  for the report)</li>

  <li>Emscripten: fix TheXTech 1.3.7.3 bug where the game could crash when selecting
  an episode. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>OpenGL: fix TheXTech 1.3.6.6 bug where the game might hang on exit on some systems.
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Wii: add overscan compensation options (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/TheEeveeLovers/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TheEeveeLovers">@TheEeveeLovers</a>
  for the report)</li>

  <li>Vita / PSTV: fix TheXTech bug where multiplayer splitscreen could be rendered
  incorrectly. (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/birtkyle-cell/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/birtkyle-cell">@birtkyle-cell</a>
  for the report)</li>

  <li>Editor: allow placing NPCs in front of semisolid blocks. (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Trickiy/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Trickiy">@Trickiy</a>
  for the report)</li>

  <li>Fixed a bug from TheXTech 1.3.7.3 that caused world map paths to never open
  when warping to the world map from a sub-hub. (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fixed a misorder of player start points loaded from LVLX files (They never guarantee
  a sort by player number, instead they has a Player ID field to distinguish point
  roles without sorting requirement). (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

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

  <li>The LunaDLL''s timer gets overlapped with the medals tracker. (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3890223500" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/1102" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/1102/hovercard" href="https://github.com/TheXTech/TheXTech/issues/1102">#1102</a>)</li>

  <li>On iOS devices (iPhone 6S and newer that has the Taptic Engine equipped), when
  the tactile vibration is activated while playing using touch screen, the device
  might start to infinitely buzz at any random moment. To escape this problem it''s
  need to switch from the game app to any other or to the main screen using home button
  or the home bar (depending on the device model) and wait when vibration will stop,
  and then, return to the game. (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5703832487" data-permission-text="Title is private" data-url="https://github.com/TheXTech/TheXTech/issues/1189"
  data-hovercard-type="issue" data-hovercard-url="/TheXTech/TheXTech/issues/1189/hovercard"
  href="https://github.com/TheXTech/TheXTech/issues/1189">#1189</a>)</li>

  </ul>'
updated: '2026-10-05T21:01:25Z'
version: v1.7.4
version_title: 'TheXTech v1.7.4: A small release, but Big Changes!'
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features. The original SMBX assets are not included, but a compatible preservation asset packs are available from wohlsoft.ru.

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>[assets] Adventures of Demo</summary>
<ol>
<li>Download <code>thextech-adventure-of-demo-assets-full-3ds.zip</code></li>
<li>Extract <code>/thextech-adventure-of-demo-assets-full-3ds.romfs</code> from the zip to <code>/3ds/thextech/assets-aod.romfs</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>thextech.3dsx</summary>
<ol>
<li>Download <code>thextech-3ds-v1.7.4.zip</code></li>
<li>Extract <code>/thextech-3ds/thextech.3dsx</code> from the zip to <code>/3ds/thextech.3dsx</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[git] thextech.3dsx</summary>
<ol>
<li>Download <code>thextech-3ds-main.zip</code></li>
<li>Extract <code>/thextech-3ds/thextech.3dsx</code> from the zip to <code>/3ds/thextech.3dsx</code> on your SD card</li>
</ol>
</details>

