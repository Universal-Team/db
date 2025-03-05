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
  thextech-3ds-assets-aod-v1.3.7.zip:
    size: 42536477
    size_str: 40 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7/thextech-3ds-assets-aod-v1.3.7.zip
  thextech-3ds-assets-smbx13-v1.3.7.zip:
    size: 45830866
    size_str: 43 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7/thextech-3ds-assets-smbx13-v1.3.7.zip
  thextech-3ds-v1.3.7.zip:
    size: 4242791
    size_str: 4 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7/thextech-3ds-v1.3.7.zip
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
stars: 322
systems:
- 3DS
title: TheXTech
update_notes: "<p dir=\"auto\">This is a large update. We worked long and hard on\
  \ this update, and we finally ready to present this big update for you all! This\
  \ update will be the biggest in TheXTech's history and features a huge set of features,\
  \ bugfixes, and improvements.</p>\n<p dir=\"auto\">Thank you to <a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/0lhi\">@0lhi</a> who served on our core development\
  \ team for design and quality assurance from version v1.3.4 (2021) to v1.3.7 (2025).\
  \ His contributions are much appreciated.</p>\n<p dir=\"auto\"><strong>EDIT: A small\
  \ hotfix for PortMaster has been released very soon: <a href=\"https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7-hotfix1\"\
  >https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7-hotfix1</a></strong></p>\n\
  <h1 dir=\"auto\">Most important changes</h1>\n<ul dir=\"auto\">\n<li>\n<p dir=\"\
  auto\"><strong>Widescreen and small-screen support, done right.</strong> No hacks,\
  \ no editing <code class=\"notranslate\">luna.lua</code>, no broken spawns. Play\
  \ all of your favorite SMBX 1.3 content at your device's native resolution for a\
  \ smooth and polished \"remaster\" experience, while the engine keeps track of which\
  \ important items would have been onscreen (or offscreen!) in SMBX 1.3.</p>\n</li>\n\
  <li>\n<p dir=\"auto\"><strong>Classic playstyle for classic content.</strong> Disable\
  \ TheXTech's unnecessary bugfixes and new features to play your SMBX 1.3 content\
  \ the way its authors intended it, or go totally Vanilla (at your own risk).</p>\n\
  </li>\n<li>\n<p dir=\"auto\"><strong>An options overhaul.</strong> No more editing\
  \ <code class=\"notranslate\">thextech.ini</code>, every single game setting can\
  \ be changed in the new in-game options menu.</p>\n</li>\n<li>\n<p dir=\"auto\"\
  ><strong>Refined player select.</strong> A huge thank you to Savby for reimagining\
  \ our text-based player select menus with an intuitive and colorful interface that\
  \ feels right at home on your TV.</p>\n</li>\n<li>\n<p dir=\"auto\"><strong>Multiple\
  \ asset packs.</strong> TheXTech is good for more than just SMBX, and now you can\
  \ conveniently switch between asset packs within the engine itself. Just add your\
  \ extra asset packs to the assets subdirectory in your TheXTech folder, and switch\
  \ by holding select at the main menu.</p>\n</li>\n<li>\n<p dir=\"auto\"><strong>Beta\
  \ 4P support.</strong> Ever wanted to play Battle Mode with 3 of your best frenemies?\
  \ Now you can! This version introduces shared and split screen 4-player co-op and\
  \ split screen 4-player battle. Please share your feedback and experiences with\
  \ us so we can make it better!</p>\n</li>\n</ul>\n<h1 dir=\"auto\">Full changelog\
  \ for 1.3.7</h1>\n<details>\n<h2 dir=\"auto\">New features:</h2>\n<h3 dir=\"auto\"\
  >The multi-res system</h3>\n<ul dir=\"auto\">\n<li>Added support for different display\
  \ resolutions (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Allow event logic NPCs to consider SMBX 1.3 camera when activating, guarded\
  \ by compat flag modern-npc-camera-logic (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add npc.txt attribute\
  \ \"usedefaultcam\"; set this to \"1\" to force NPCs to use the event logic camera\
  \ to activate and \"0\" to force them to use the visible camera (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add compat.ini setting\
  \ \"dynamic-camera-logic\" which may be disabled to force a level to use the 800x600\
  \ camera for all logic (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Added internal support for more than 2 cameras (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added backdrop for\
  \ levels smaller than the screen at <code class=\"notranslate\">graphics/ui/Backdrop.png</code>\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added\
  \ alternative format for world map frame with better support for various display\
  \ resolutions (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  </ul>\n<h3 dir=\"auto\">Menus</h3>\n<ul dir=\"auto\">\n<li>Redesigned character\
  \ select screen for multiplayer game start and player setup (@Savbyn, <a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Overhaul the Main\
  \ Menu and in-game Options menu with support for editing all \"thextech.ini\" options\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add\
  \ \"Modern\", \"Classic\", and \"Vanilla\" playstyles which determine which bugfixes\
  \ and gameplay updates are applied (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n<li>Add ability\
  \ to start speedrun in-game by pressing Select when making a new game save (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\" data-octo-click=\"\
  hovercard-link-click\" data-octo-dimensions=\"link_type:self\" href=\"https://github.com/0lhi\"\
  >@0lhi</a>)</li>\n<li>Add ability to change last warp resume setting on hub worlds.\
  \ This allows playing episodes incompatible with this behavior in Modern Mode. (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n</ul>\n<h3 dir=\"auto\">Asset\
  \ packs system</h3>\n<ul dir=\"auto\">\n<li>Game looks for extra asset packs in\
  \ the <code class=\"notranslate\">assets/</code> subdirectory of the user and system\
  \ directories (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Add ability to specify asset pack by ID in the command line (as well as by path)\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add\
  \ ability to switch asset pack at main menu screen by holding select button (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n\
  <h3 dir=\"auto\">New content</h3>\n<ul dir=\"auto\">\n<li>Added full game and in-game\
  \ editor support for world map sections that limit screen view (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add compat flag\
  \ \"disable-spin-jump\", which causes the AltJump key to map to a normal jump, but\
  \ still allows players to dismount. The flag replaces a hack used to force-disable\
  \ the key in Superb Demo Sisters. (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Added support for on-exit warp event. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Move the <code\
  \ class=\"notranslate\">[intro]</code> and <code class=\"notranslate\">[outro]</code>\
  \ sections of <code class=\"notranslate\">gameinfo.ini</code> to <code class=\"\
  notranslate\">[activity-setup]</code> in the <code class=\"notranslate\">compat.ini</code>\
  \ file for the intro/outro levels, for per-level configuration of these settings.\
  \ Setting the fields via <code class=\"notranslate\">gameinfo.ini</code> is deprecated\
  \ and may be removed in future asset pack formats. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Added support\
  \ for episodes to provide custom main menu intros. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Added support\
  \ for episodes to provide custom credits level. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Allow customization\
  \ of TTF colour of fonts (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  </ul>\n<h3 dir=\"auto\">Editor</h3>\n<ul dir=\"auto\">\n<li>Add ability to trigger\
  \ event layer smoke in the in-game editor (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add ability to edit\
  \ BGO sort layers and offset in the in-game editor (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add ability to resize\
  \ placed items, section boundaries, and event section boundaries in the editor (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n\
  <h3 dir=\"auto\">Cheats / codes</h3>\n<ul dir=\"auto\">\n<li>Added \"opensesame\"\
  \ world map cheat to unlock paths from level (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added code \"logicscreen\"\
  \ to view camera used by event logic NPCs (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add cheat \"edityourfriends\"\
  \ to experiment with compatibility settings (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add cheats \"4shared\"\
  \ and \"4split\" to test 4-player shared / split screen modes (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n<h3 dir=\"auto\"\
  >Other features</h3>\n<ul dir=\"auto\">\n<li>Add tracking for medals collected in\
  \ levels (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added\
  \ smooth path unlock animations at the world map (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Sounds now get quieter\
  \ when they are further from the screen (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Add hints system to the loading and pause screens (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add new item drop\
  \ system, used by default in Modern Mode at low resolutions (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ChristianSilvermoon/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ChristianSilvermoon\">@ChristianSilvermoon</a>, <a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n<li>Add option to always use\
  \ shared or split screen in 2P (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Add ability (beta status) to play &gt;2P mode with shared or split screen (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Implemented\
  \ the in-game assert failures will be shown as in-game message box until perform\
  \ an emergency close on platforms that doesn't have SDL's message box (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Update level loading\
  \ error screen to be more informative (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Add world loading error screen (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>3DS: add advanced option \"Inaccurate GIFs\" to allow playing in 3D on levels\
  \ with GIFs (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  </ul>\n<h2 dir=\"auto\">Other engine changes</h2>\n<ul dir=\"auto\">\n<li>Save the\
  \ number of medals / stars that exist in levels to speed up subsequent loads (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Internal\
  \ change: added draw plane system to track different object groups' scene depth\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Note:\
  \ screen-space autocode draws now occur in the HUD plane instead of the level plane\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Drop/add\
  \ screen renamed to \"Player Setup\"</li>\n<li>In modern gameplay, the main menu\
  \ now has a single \"Play Episode\" item instead of separate 1P/2P items</li>\n\
  <li>COMPATIBILITY CHANGE: remove automatic version targeting for pre-SMBX 1.3 content\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Very\
  \ long SFX are now played from disk to save memory (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Made some internal\
  \ memory optimizations to the Block and NPC objects, saving 360KB RAM (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>GIF recorder now\
  \ turns grey and skips frames when recording is slower than gameplay (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Update TheXTech's\
  \ logic for climbing moving fences (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Change cheat \"shadowstar\" to use a 75% black tint (instead of 100% as in SMBX\
  \ 1.3) for visibility against dark level backgrounds (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\" data-octo-click=\"\
  hovercard-link-click\" data-octo-dimensions=\"link_type:self\" href=\"https://github.com/0lhi\"\
  >@0lhi</a>, <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Update\
  \ TheXTech userdata locations to system-native locations on new installs. (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Speedrun timer\
  \ no longer permanently stops following initial game win, allowing speedruns of\
  \ postgame content (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>In Modern and Classic modes, now allow negative lives instead of game over (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n<li>Added support for error\
  \ boxes at the Wii U to explicitly show reasons of errors to users (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>System message\
  \ boxes will have their unique style that is different from the in-game one. (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Add\
  \ option (on-by-default) for gamepads to use simple editor controls. Prevents getting\
  \ locked in the editor. (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Improve the performance of levels with many climbable NPCs (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Refine GIF bitmask\
  \ detection and fallback algorithm (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>3DS/Wii: speed up graphics loading code (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>TheXTech-exclusive\
  \ events are now processed at the end of the frame they are triggered in (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>3DS: display system\
  \ and video memory usage in Debug Info screen (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add support for\
  \ TTF fonts up to 24x24 (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  </ul>\n<h2 dir=\"auto\">New vanilla bugfixes</h2>\n<ul dir=\"auto\">\n<li>Fix thrower\
  \ vertical position logic in split-screen, guarded by compat flag modern-npc-camera-logic\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
  \ SMBX 1.3 bug where camera would not track respawning player, guarded by compat\
  \ flag multiplayer-pause-controls (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix ghost, boss, and other NPC target player selection, guarded by compat flag\
  \ \"fix-multiplayer-targeting\" (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix vanilla peculiarity where plants would make a sound when dying in a no-turn-back\
  \ level, guarded by compat flag \"fix-visual-bugs\" [Modern Mode] (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix vanilla peculiarity\
  \ where the speed of blocks attached to an NPC would not be fully reset when the\
  \ NPC dies, guarded by compat flag \"fix-attlayer-reset\" [Modern Mode] (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix vanilla peculiarity\
  \ where some held NPCs would appear to move on the player's hands / feet, guarded\
  \ by compat flag \"fix-visual-bugs\" [Modern Mode] (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix vanilla editor\
  \ bug where NPC spawn logic might be inaccurate on level test (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix vanilla peculiarity\
  \ where medals were sometimes not collected when killed, guarded by \"fix-medal-kill\"\
  \ [Modern Mode] (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ thanks to <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Superbloxen/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Superbloxen\">@Superbloxen</a> for the\
  \ report)</li>\n</ul>\n<h2 dir=\"auto\">TheXTech bugfixes</h2>\n<ul dir=\"auto\"\
  >\n<li>Fix TheXTech 1.3.6.1 bug where level fadeout did not properly occur on fail\
  \ in 2P mode (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix TheXTech 1.3.6.1 peculiarity where a player could reach an inaccessible\
  \ location by respawning while another player was scrolling between warps (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Editor: fix TheXTech\
  \ 1.3.6 bug where level test might incorrectly start following text input (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.6\
  \ bug where an item could be cloned by changing characters during powerup animation\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
  \ TheXTech 1.3.6.1 OpenGL bug where a mask larger than its texture could be drawn\
  \ incorrectly (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ thanks to @AntonioGZZ96 for the report)</li>\n<li>Fix TheXTech 1.3.6.1 inaccuracy\
  \ affecting \"Endless Exploration\" where levels started via an invalid warp point\
  \ could not be played (in SMBX 1.3, the warp point is ignored) (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.1\
  \ bug where many max-ID custom GFX were not loaded (including player-5 map sprites)\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to @AntonioGZZ96\
  \ for the report)</li>\n<li>Fix TheXTech v1.3.6 editor bug where NPC properties\
  \ could change when their layer was hidden. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to @cre8iveexercise\
  \ for the report)</li>\n<li>Fix TheXTech v1.3.6.1 Android bug where the screen would\
  \ be black after switching applications. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.5.1\
  \ bug where the lower half of a player's sprite could be shown behind a shoe / sack\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fixed\
  \ the inability to close error LunaScript parse error box on Android when file contains\
  \ too long lines (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wohlstand\"\
  >@Wohlstand</a>)</li>\n<li>Fixed crash on attempt to execute the \"SetHits\" and\
  \ \"AllFace\" LunaScript commands (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wohlstand\"\
  >@Wohlstand</a>)</li>\n<li>Wii: fix TheXTech 1.3.6.1 inaccuracy in how very small\
  \ GIF bitmasks are rendered (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix TheXTech 1.3.6.1 bug where player-dependent event text could be inaccurate\
  \ if Autocode cancelled a different event (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.1\
  \ inaccuracy where a vanilla bug failed to replicate. This bug caused a pending\
  \ event to be overwritten when two events triggered in a single frame. The bugfix\
  \ now has compat flag \"fix-event-swap-bug\" (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fixed the random\
  \ crash and memory damaging during the load process (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/Wohlstand/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n<li>Fix TheXTech 1.3.6\
  \ bug where some controls profiles could not be deleted. (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to <a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/0lhi\">@0lhi</a> for the report)</li>\n</ul>\n<h2 dir=\"\
  auto\">TheXTech v1.3.7-beta bugfixes</h2>\n<ul dir=\"auto\">\n<li>Fix TheXTech 1.3.7-beta\
  \ visual glitch when the vanilla cam hotkey was pressed during the level intro scene\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
  \ TheXTech 1.3.7-beta bug where vanilla cam was not reset before entering credits\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>3DS/Wii:\
  \ fix TheXTech 1.3.7-beta bug where levels with 101 layers/events could not load\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Hints:\
  \ fix the graphical display of the surfing hint (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Refine the placement\
  \ of HUD items at low resolutions (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Don't allow pressing the vanilla cam hotkey during a camera pan event (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.7-beta\
  \ bug where battle levels could be created even if the asset pack disables battle\
  \ mode (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to <a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/LoveBodhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/LoveBodhi\">@LoveBodhi</a> for the report)</li>\n\
  <li>Fix TheXTech 1.3.7-beta bug where it was impossible to enter speedrun mode using\
  \ the main menu interface (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ thanks to <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a> for the report)</li>\n\
  <li>Fix TheXTech 1.3.7-beta bug where the modern lives count was shown at the title\
  \ screen for vanilla gamesaves (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ thanks to <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a> for the report)</li>\n\
  <li>Fix TheXTech 1.3.7-beta defect where it was not clear whether vanilla cam was\
  \ activated at high resolutions (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ thanks to <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a> for the report)</li>\n\
  <li>Fix TheXTech 1.3.7-beta inaccuracy in which an NPC that moves into a section\
  \ during gameplay might fail to spawn (this affected the final boss of Valtteri's\
  \ Island - Revisited) (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix TheXTech 1.3.7-beta bug where an assertion failure could be triggered when\
  \ a player went offscreen in shared screen multiplayer (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Ensure that the\
  \ player setup menu always remembers the most recently selected characters (<a class=\"\
  user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to <a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/0lhi/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/0lhi\">@0lhi</a> for the suggestion)</li>\n<li>Fix TheXTech\
  \ 1.3.7-beta bug where the logical screen could desync after dropping a player (<a\
  \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
  \ TheXTech 1.3.7-beta bug where menus could become unresponsive if a player had\
  \ been dropped while holding a button. (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>,\
  \ thanks to <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a> for the report)</li>\n\
  <li>Fix TheXTech 1.3.7-beta defect where character forced using Konami code would\
  \ be lost on menu quit (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix TheXTech 1.3.7-beta bug where the player start points were incorrect for\
  \ some content. This affected Adventures of Demo. (<a class=\"user-mention notranslate\"\
  \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.7-beta\
  \ bug where hitting Escape at the pause menu could return to menu (<a class=\"user-mention\
  \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
  \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
  \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to @sl4cer for the\
  \ report)</li>\n<li>Fix TheXTech 1.3.7-beta PortMaster peculiarity where the load\
  \ screen would be drawn too small (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
  user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix TheXTech 1.3.7-beta Wii bug where the no-assets screen would not display\
  \ correctly (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  <li>Fix TheXTech 1.3.7-beta Wii bug where unconverted UI assets could not be loaded\
  \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
  \ TheXTech 1.3.7-beta bug where the controller preview on the controls menu was\
  \ inaccurate (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
  \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
  \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n\
  </ul>\n</details>\n<h1 dir=\"auto\">Known issues</h1>\n<ul dir=\"auto\">\n<li>Audio\
  \ may be choppy on Old 3DS.</li>\n<li>Texture load stutter is present on Wii.</li>\n\
  <li>The screen may slightly judder during section resizes on 3DS and Wii.</li>\n\
  <li>Closing the game using the Home button or Power button occasionally causes crashes\
  \ on 3DS.</li>\n<li>The viewport is sometimes incorrect on Vita.</li>\n<li>On Windows\
  \ 10 when running OpenGL with some ~2006 Intel iGPU on laptop, game would crash\
  \ (possibly fixed).</li>\n</ul>\n<h1 dir=\"auto\">Screenshots</h1>\n  \n  \n  \n\
  \  \n  \n  "
updated: '2025-01-20T23:31:04Z'
version: v1.3.7
version_title: 'TheXTech v1.3.7: The biggest New Year Gift for everybody!'
website: https://wohlsoft.ru/projects/TheXTech/
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features.