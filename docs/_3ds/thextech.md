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
  thextech-3ds-assets-aod-v1.3.6.6.zip:
    size: 44255803
    size_str: 42 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.6.6/thextech-3ds-assets-aod-v1.3.6.6.zip
  thextech-3ds-assets-smbx13-v1.3.6.6.zip:
    size: 48793840
    size_str: 46 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.6.6/thextech-3ds-assets-smbx13-v1.3.6.6.zip
  thextech-3ds-v1.3.6.6.zip:
    size: 4077109
    size_str: 3 MiB
    url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.6.6/thextech-3ds-v1.3.6.6.zip
github: TheXTech/TheXTech
icon: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/icon/thextech_48.png
image: https://raw.githubusercontent.com/TheXTech/TheXTech/main/resources/wiiu/wuhb-splash.png
image_length: 121515
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/TheXTech/TheXTech/releases/tag/v1.3.7-beta
  downloads:
    thextech-3ds-assets-aod-v1.3.7-beta.zip:
      size: 44533570
      size_str: 42 MiB
      url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7-beta/thextech-3ds-assets-aod-v1.3.7-beta.zip
    thextech-3ds-assets-smbx13-v1.3.7-beta.zip:
      size: 48776365
      size_str: 46 MiB
      url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7-beta/thextech-3ds-assets-smbx13-v1.3.7-beta.zip
    thextech-3ds-v1.3.7-beta.zip:
      size: 4244628
      size_str: 4 MiB
      url: https://github.com/TheXTech/TheXTech/releases/download/v1.3.7-beta/thextech-3ds-v1.3.7-beta.zip
  update_notes: "<p dir=\"auto\">This is a BETA version for the upcoming v1.3.7 release.\
    \ We worked long and hard on this update, however, we still need additional testing\
    \ before we can release a stable version. This update will be the biggest in TheXTech's\
    \ history and features a huge set of features, bugfixes, and improvements.</p>\n\
    <h1 dir=\"auto\">Most important changes</h1>\n<ul dir=\"auto\">\n<li>\n<p dir=\"\
    auto\"><strong>Widescreen and small-screen support, done right.</strong> No hacks,\
    \ no editing <code class=\"notranslate\">luna.lua</code>, no broken spawns. Play\
    \ all of your favorite SMBX 1.3 content at your device's native resolution for\
    \ a smooth and polished \"remaster\" experience, while the engine keeps track\
    \ of which important items would have been onscreen (or offscreen!) in SMBX 1.3.</p>\n\
    </li>\n<li>\n<p dir=\"auto\"><strong>Classic playstyle for classic content.</strong>\
    \ Disable TheXTech's unnecessary bugfixes and new features to play your SMBX 1.3\
    \ content the way its authors intended it, or go totally Vanilla (at your own\
    \ risk).</p>\n</li>\n<li>\n<p dir=\"auto\"><strong>An options overhaul.</strong>\
    \ No more editing <code class=\"notranslate\">thextech.ini</code>, every single\
    \ game setting can be changed in the new in-game options menu.</p>\n</li>\n<li>\n\
    <p dir=\"auto\"><strong>Refined player select.</strong> A huge thank you to Savby\
    \ for reimagining our text-based player select menus with an intuitive and colorful\
    \ interface that feels right at home on your TV.</p>\n</li>\n<li>\n<p dir=\"auto\"\
    ><strong>Multiple asset packs.</strong> TheXTech is good for more than just SMBX,\
    \ and now you can conveniently switch between asset packs within the engine itself.\
    \ Just add your extra asset packs to the assets subdirectory in your TheXTech\
    \ folder, and switch by holding select at the main menu.</p>\n</li>\n<li>\n<p\
    \ dir=\"auto\"><strong>Beta 4P support.</strong> Ever wanted to play Battle Mode\
    \ with 3 of your best frenemies? Now you can! This version introduces shared and\
    \ split screen 4-player co-op and split screen 4-player battle. Please share your\
    \ feedback and experiences with us so we can make it better!</p>\n</li>\n</ul>\n\
    <h1 dir=\"auto\">Full changelog for 1.3.7</h1>\n<details>\n<h2 dir=\"auto\">New\
    \ features:</h2>\n<h3 dir=\"auto\">The multi-res system</h3>\n<ul dir=\"auto\"\
    >\n<li>Added support for different display resolutions (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Allow event logic\
    \ NPCs to consider SMBX 1.3 camera when activating, guarded by compat flag modern-npc-camera-logic\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add\
    \ npc.txt attribute \"usedefaultcam\"; set this to \"1\" to force NPCs to use\
    \ the event logic camera to activate and \"0\" to force them to use the visible\
    \ camera (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add\
    \ compat.ini setting \"dynamic-camera-logic\" which may be disabled to force a\
    \ level to use the 800x600 camera for all logic (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added internal\
    \ support for more than 2 cameras (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Added backdrop for levels smaller than the screen at\
    \ <code class=\"notranslate\">graphics/ui/Backdrop.png</code> (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added alternative\
    \ format for world map frame with better support for various display resolutions\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n\
    <h3 dir=\"auto\">Menus</h3>\n<ul dir=\"auto\">\n<li>Redesigned character select\
    \ screen for multiplayer game start and player setup (@Savbyn, <a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Overhaul the Main\
    \ Menu and in-game Options menu with support for editing all \"thextech.ini\"\
    \ options (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
    \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add \"Modern\", \"Classic\", and \"Vanilla\" playstyles\
    \ which determine which bugfixes and gameplay updates are applied (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n<li>Add ability\
    \ to start speedrun in-game by pressing Select when making a new game save (<a\
    \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n</ul>\n<h3\
    \ dir=\"auto\">Asset packs system</h3>\n<ul dir=\"auto\">\n<li>Game looks for\
    \ extra asset packs in the <code class=\"notranslate\">assets/</code> subdirectory\
    \ of the user and system directories (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add ability to specify asset pack by ID in the command\
    \ line (as well as by path) (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add ability to switch asset pack at main menu screen\
    \ by holding select button (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n</ul>\n<h3 dir=\"auto\">New content</h3>\n<ul dir=\"auto\"\
    >\n<li>Added full game and in-game editor support for world map sections that\
    \ limit screen view (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add compat flag \"disable-spin-jump\", which causes\
    \ the AltJump key to map to a normal jump, but still allows players to dismount.\
    \ The flag replaces a hack used to force-disable the key in Superb Demo Sisters.\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n\
    <h3 dir=\"auto\">Editor</h3>\n<ul dir=\"auto\">\n<li>Add ability to trigger event\
    \ layer smoke in the in-game editor (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add ability to edit BGO sort layers and offset in the\
    \ in-game editor (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add ability to resize placed items, section boundaries,\
    \ and event section boundaries in the editor (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n<h3 dir=\"\
    auto\">Cheats / codes</h3>\n<ul dir=\"auto\">\n<li>Added \"opensesame\" world\
    \ map cheat to unlock paths from level (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Added code \"\
    logicscreen\" to view camera used by event logic NPCs (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add cheat \"edityourfriends\"\
    \ to experiment with compatibility settings (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add cheats \"\
    4shared\" and \"4split\" to test 4-player shared / split screen modes (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n\
    <h3 dir=\"auto\">Other features</h3>\n<ul dir=\"auto\">\n<li>Add tracking for\
    \ medals collected in levels (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Added smooth path unlock animations at the world map\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Sounds\
    \ now get quieter when they are further from the screen (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add hints system\
    \ to the loading and pause screens (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Add new item drop system, used by default in Modern\
    \ Mode at low resolutions (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>, <a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
    \ data-hovercard-url=\"/users/ChristianSilvermoon/hovercard\" data-octo-click=\"\
    hovercard-link-click\" data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ChristianSilvermoon\"\
    >@ChristianSilvermoon</a>, <a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n\
    <li>Add option to always use shared or split screen in 2P (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Add ability (beta\
    \ status) to play &gt;2P mode with shared or split screen (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n<h2 dir=\"\
    auto\">Other engine changes</h2>\n<ul dir=\"auto\">\n<li>Save the number of medals\
    \ / stars that exist in levels to speed up subsequent loads (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Internal change:\
    \ added draw plane system to track different object groups' scene depth (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Note:\
    \ screen-space autocode draws now occur in the HUD plane instead of the level\
    \ plane (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Drop/add\
    \ screen renamed to \"Player Setup\"</li>\n<li>In modern gameplay, the main menu\
    \ now has a single \"Play Episode\" item instead of separate 1P/2P items</li>\n\
    <li>COMPATIBILITY CHANGE: remove automatic version targeting for pre-SMBX 1.3\
    \ content (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
    \ data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Very long SFX are now played from disk to save memory\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Made\
    \ some internal memory optimizations to the Block and NPC objects, saving 360KB\
    \ RAM (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>GIF\
    \ recorder now turns grey and skips frames when recording is slower than gameplay\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Update\
    \ TheXTech's logic for climbing moving fences (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Change cheat \"\
    shadowstar\" to use a 75% black tint (instead of 100% as in SMBX 1.3) for visibility\
    \ against dark level backgrounds (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a>,\
    \ <a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Update\
    \ TheXTech userdata locations to system-native locations on new installs. (<a\
    \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, <a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/Wohlstand\">@Wohlstand</a>)</li>\n\
    <li>Speedrun timer no longer permanently stops following initial game win, allowing\
    \ speedruns of postgame content (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>In Modern and Classic modes, now allow negative lives\
    \ instead of game over (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>, <a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
    \ data-hovercard-url=\"/users/0lhi/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/0lhi\">@0lhi</a>)</li>\n\
    <li>Added support for error boxes at the Wii U to explicitly show reasons of errors\
    \ to users (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\"\
    \ data-hovercard-url=\"/users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wohlstand\"\
    >@Wohlstand</a>)</li>\n<li>System message boxes will have their unique style that\
    \ is different from the in-game one. (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wohlstand\"\
    >@Wohlstand</a>)</li>\n<li>Add option (on-by-default) for gamepads to use simple\
    \ editor controls. Prevents getting locked in the editor. (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n<h2 dir=\"\
    auto\">New vanilla bugfixes</h2>\n<ul dir=\"auto\">\n<li>Fix thrower vertical\
    \ position logic in split-screen, guarded by compat flag modern-npc-camera-logic\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
    \ SMBX 1.3 bug where camera would not track respawning player, guarded by compat\
    \ flag multiplayer-pause-controls (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Fix ghost, boss, and other NPC target player selection,\
    \ guarded by compat flag \"fix-multiplayer-targeting\" (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix vanilla peculiarity\
    \ where plants would make a sound when dying in a no-turn-back level, guarded\
    \ by compat flag \"fix-visual-bugs\" [Modern Mode] (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix vanilla peculiarity\
    \ where the speed of blocks attached to an NPC would not be fully reset when the\
    \ NPC dies, guarded by compat flag \"fix-attlayer-reset\" [Modern Mode] (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
    \ vanilla peculiarity where some held NPCs would appear to move on the player's\
    \ hands / feet, guarded by compat flag \"fix-visual-bugs\" [Modern Mode] (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
    \ vanilla editor bug where NPC spawn logic might be inaccurate on level test (<a\
    \ class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n</ul>\n\
    <h2 dir=\"auto\">TheXTech bugfixes</h2>\n<ul dir=\"auto\">\n<li>Fix TheXTech 1.3.6.1\
    \ bug where level fadeout did not properly occur on fail in 2P mode (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
    \ TheXTech 1.3.6.1 peculiarity where a player could reach an inaccessible location\
    \ by respawning while another player was scrolling between warps (<a class=\"\
    user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Editor:\
    \ fix TheXTech 1.3.6 bug where level test might incorrectly start following text\
    \ input (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix\
    \ TheXTech 1.3.6 bug where an item could be cloned by changing characters during\
    \ powerup animation (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/ds-sloth\"\
    >@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.6.1 OpenGL bug where a mask larger\
    \ than its texture could be drawn incorrectly (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to @AntonioGZZ96\
    \ for the report)</li>\n<li>Fix TheXTech 1.3.6.1 inaccuracy affecting \"Endless\
    \ Exploration\" where levels started via an invalid warp point could not be played\
    \ (in SMBX 1.3, the warp point is ignored) (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.1\
    \ bug where many max-ID custom GFX were not loaded (including player-5 map sprites)\
    \ (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to\
    \ @AntonioGZZ96 for the report)</li>\n<li>Fix TheXTech v1.3.6 editor bug where\
    \ NPC properties could change when their layer was hidden. (<a class=\"user-mention\
    \ notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>, thanks to @cre8iveexercise\
    \ for the report)</li>\n<li>Fix TheXTech v1.3.6.1 Android bug where the screen\
    \ would be black after switching applications. (<a class=\"user-mention notranslate\"\
    \ data-hovercard-type=\"user\" data-hovercard-url=\"/users/ds-sloth/hovercard\"\
    \ data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"link_type:self\"\
    \ href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fix TheXTech 1.3.5.1\
    \ bug where the lower half of a player's sprite could be shown behind a shoe /\
    \ sack (<a class=\"user-mention notranslate\" data-hovercard-type=\"user\" data-hovercard-url=\"\
    /users/ds-sloth/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
    link_type:self\" href=\"https://github.com/ds-sloth\">@ds-sloth</a>)</li>\n<li>Fixed\
    \ the inability to close error LunaScript parse error box on Android when file\
    \ contains too long lines (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wohlstand\"\
    >@Wohlstand</a>)</li>\n<li>Fixed crash on attempt to execute the \"SetHits\" and\
    \ \"AllFace\" LunaScript commands (<a class=\"user-mention notranslate\" data-hovercard-type=\"\
    user\" data-hovercard-url=\"/users/Wohlstand/hovercard\" data-octo-click=\"hovercard-link-click\"\
    \ data-octo-dimensions=\"link_type:self\" href=\"https://github.com/Wohlstand\"\
    >@Wohlstand</a>)</li>\n</ul>\n</details>\n<h1 dir=\"auto\">Known issues</h1>\n\
    <ul dir=\"auto\">\n<li>Audio may be choppy on Old 3DS.</li>\n<li>Texture load\
    \ stutter is present on Wii.</li>\n<li>The viewport is sometimes incorrect on\
    \ Vita.</li>\n<li>On Windows 10 when running OpenGL with some ~2006 Intel iGPU\
    \ on laptop, game would crash (possibly fixed).</li>\n</ul>\n<h1 dir=\"auto\"\
    >Screenshots</h1>\n  \n  \n  \n  \n  \n  "
  update_notes_md: "This is a BETA version for the upcoming v1.3.7 release. We worked\
    \ long and hard on this update, however, we still need additional testing before\
    \ we can release a stable version. This update will be the biggest in TheXTech's\
    \ history and features a huge set of features, bugfixes, and improvements.\n\n\
    # Most important changes\n\n* **Widescreen and small-screen support, done right.**\
    \ No hacks, no editing `luna.lua`, no broken spawns. Play all of your favorite\
    \ SMBX 1.3 content at your device's native resolution for a smooth and polished\
    \ \"remaster\" experience, while the engine keeps track of which important items\
    \ would have been onscreen (or offscreen!) in SMBX 1.3.\n\n* **Classic playstyle\
    \ for classic content.** Disable TheXTech's unnecessary bugfixes and new features\
    \ to play your SMBX 1.3 content the way its authors intended it, or go totally\
    \ Vanilla (at your own risk).\n\n* **An options overhaul.** No more editing `thextech.ini`,\
    \ every single game setting can be changed in the new in-game options menu.\n\n\
    * **Refined player select.** A huge thank you to Savby for reimagining our text-based\
    \ player select menus with an intuitive and colorful interface that feels right\
    \ at home on your TV.\n\n* **Multiple asset packs.** TheXTech is good for more\
    \ than just SMBX, and now you can conveniently switch between asset packs within\
    \ the engine itself. Just add your extra asset packs to the assets subdirectory\
    \ in your TheXTech folder, and switch by holding select at the main menu.\n\n\
    * **Beta 4P support.** Ever wanted to play Battle Mode with 3 of your best frenemies?\
    \ Now you can! This version introduces shared and split screen 4-player co-op\
    \ and split screen 4-player battle. Please share your feedback and experiences\
    \ with us so we can make it better!\n\n# Full changelog for 1.3.7\n\n<details>\n\
    \n## New features:\n\n### The multi-res system\n\n* Added support for different\
    \ display resolutions (@ds-sloth)\n* Allow event logic NPCs to consider SMBX 1.3\
    \ camera when activating, guarded by compat flag modern-npc-camera-logic (@ds-sloth)\n\
    * Add npc.txt attribute \"usedefaultcam\"; set this to \"1\" to force NPCs to\
    \ use the event logic camera to activate and \"0\" to force them to use the visible\
    \ camera (@ds-sloth)\n* Add compat.ini setting \"dynamic-camera-logic\" which\
    \ may be disabled to force a level to use the 800x600 camera for all logic (@ds-sloth)\n\
    * Added internal support for more than 2 cameras (@ds-sloth)\n* Added backdrop\
    \ for levels smaller than the screen at `graphics/ui/Backdrop.png` (@ds-sloth)\n\
    * Added alternative format for world map frame with better support for various\
    \ display resolutions (@ds-sloth)\n\n### Menus\n\n* Redesigned character select\
    \ screen for multiplayer game start and player setup (@Savbyn, @ds-sloth)\n* Overhaul\
    \ the Main Menu and in-game Options menu with support for editing all \"thextech.ini\"\
    \ options (@ds-sloth)\n* Add \"Modern\", \"Classic\", and \"Vanilla\" playstyles\
    \ which determine which bugfixes and gameplay updates are applied (@ds-sloth,\
    \ @0lhi)\n* Add ability to start speedrun in-game by pressing Select when making\
    \ a new game save (@ds-sloth, @0lhi)\n\n### Asset packs system\n\n* Game looks\
    \ for extra asset packs in the `assets/` subdirectory of the user and system directories\
    \ (@ds-sloth)\n* Add ability to specify asset pack by ID in the command line (as\
    \ well as by path) (@ds-sloth)\n* Add ability to switch asset pack at main menu\
    \ screen by holding select button (@ds-sloth)\n\n### New content\n\n* Added full\
    \ game and in-game editor support for world map sections that limit screen view\
    \ (@ds-sloth)\n* Add compat flag \"disable-spin-jump\", which causes the AltJump\
    \ key to map to a normal jump, but still allows players to dismount. The flag\
    \ replaces a hack used to force-disable the key in Superb Demo Sisters. (@ds-sloth)\n\
    \n### Editor\n\n* Add ability to trigger event layer smoke in the in-game editor\
    \ (@ds-sloth)\n* Add ability to edit BGO sort layers and offset in the in-game\
    \ editor (@ds-sloth)\n* Add ability to resize placed items, section boundaries,\
    \ and event section boundaries in the editor (@ds-sloth)\n\n### Cheats / codes\n\
    \n* Added \"opensesame\" world map cheat to unlock paths from level (@ds-sloth)\n\
    * Added code \"logicscreen\" to view camera used by event logic NPCs (@ds-sloth)\n\
    * Add cheat \"edityourfriends\" to experiment with compatibility settings (@ds-sloth)\n\
    * Add cheats \"4shared\" and \"4split\" to test 4-player shared / split screen\
    \ modes (@ds-sloth)\n\n### Other features\n\n* Add tracking for medals collected\
    \ in levels (@ds-sloth)\n* Added smooth path unlock animations at the world map\
    \ (@ds-sloth)\n* Sounds now get quieter when they are further from the screen\
    \ (@ds-sloth)\n* Add hints system to the loading and pause screens (@ds-sloth)\n\
    * Add new item drop system, used by default in Modern Mode at low resolutions\
    \ (@ds-sloth, @ChristianSilvermoon, @0lhi)\n* Add option to always use shared\
    \ or split screen in 2P (@ds-sloth)\n* Add ability (beta status) to play >2P mode\
    \ with shared or split screen (@ds-sloth)\n\n## Other engine changes\n\n* Save\
    \ the number of medals / stars that exist in levels to speed up subsequent loads\
    \ (@ds-sloth)\n* Internal change: added draw plane system to track different object\
    \ groups' scene depth (@ds-sloth)\n* Note: screen-space autocode draws now occur\
    \ in the HUD plane instead of the level plane (@ds-sloth)\n* Drop/add screen renamed\
    \ to \"Player Setup\"\n* In modern gameplay, the main menu now has a single \"\
    Play Episode\" item instead of separate 1P/2P items\n* COMPATIBILITY CHANGE: remove\
    \ automatic version targeting for pre-SMBX 1.3 content (@ds-sloth)\n* Very long\
    \ SFX are now played from disk to save memory (@ds-sloth)\n* Made some internal\
    \ memory optimizations to the Block and NPC objects, saving 360KB RAM (@ds-sloth)\n\
    * GIF recorder now turns grey and skips frames when recording is slower than gameplay\
    \ (@ds-sloth)\n* Update TheXTech's logic for climbing moving fences (@ds-sloth)\n\
    * Change cheat \"shadowstar\" to use a 75% black tint (instead of 100% as in SMBX\
    \ 1.3) for visibility against dark level backgrounds (@0lhi, @ds-sloth)\n* Update\
    \ TheXTech userdata locations to system-native locations on new installs. (@ds-sloth,\
    \ @Wohlstand)\n* Speedrun timer no longer permanently stops following initial\
    \ game win, allowing speedruns of postgame content (@ds-sloth)\n* In Modern and\
    \ Classic modes, now allow negative lives instead of game over (@ds-sloth, @0lhi)\n\
    * Added support for error boxes at the Wii U to explicitly show reasons of errors\
    \ to users (@Wohlstand)\n* System message boxes will have their unique style that\
    \ is different from the in-game one. (@Wohlstand)\n* Add option (on-by-default)\
    \ for gamepads to use simple editor controls. Prevents getting locked in the editor.\
    \ (@ds-sloth)\n\n## New vanilla bugfixes\n\n* Fix thrower vertical position logic\
    \ in split-screen, guarded by compat flag modern-npc-camera-logic (@ds-sloth)\n\
    * Fix SMBX 1.3 bug where camera would not track respawning player, guarded by\
    \ compat flag multiplayer-pause-controls (@ds-sloth)\n* Fix ghost, boss, and other\
    \ NPC target player selection, guarded by compat flag \"fix-multiplayer-targeting\"\
    \ (@ds-sloth)\n* Fix vanilla peculiarity where plants would make a sound when\
    \ dying in a no-turn-back level, guarded by compat flag \"fix-visual-bugs\" [Modern\
    \ Mode] (@ds-sloth)\n* Fix vanilla peculiarity where the speed of blocks attached\
    \ to an NPC would not be fully reset when the NPC dies, guarded by compat flag\
    \ \"fix-attlayer-reset\" [Modern Mode] (@ds-sloth)\n* Fix vanilla peculiarity\
    \ where some held NPCs would appear to move on the player's hands / feet, guarded\
    \ by compat flag \"fix-visual-bugs\" [Modern Mode] (@ds-sloth)\n* Fix vanilla\
    \ editor bug where NPC spawn logic might be inaccurate on level test (@ds-sloth)\n\
    \n## TheXTech bugfixes\n\n* Fix TheXTech 1.3.6.1 bug where level fadeout did not\
    \ properly occur on fail in 2P mode (@ds-sloth)\n* Fix TheXTech 1.3.6.1 peculiarity\
    \ where a player could reach an inaccessible location by respawning while another\
    \ player was scrolling between warps (@ds-sloth)\n* Editor: fix TheXTech 1.3.6\
    \ bug where level test might incorrectly start following text input (@ds-sloth)\n\
    * Fix TheXTech 1.3.6 bug where an item could be cloned by changing characters\
    \ during powerup animation (@ds-sloth)\n* Fix TheXTech 1.3.6.1 OpenGL bug where\
    \ a mask larger than its texture could be drawn incorrectly (@ds-sloth, thanks\
    \ to @AntonioGZZ96 for the report)\n* Fix TheXTech 1.3.6.1 inaccuracy affecting\
    \ \"Endless Exploration\" where levels started via an invalid warp point could\
    \ not be played (in SMBX 1.3, the warp point is ignored) (@ds-sloth)\n* Fix TheXTech\
    \ 1.3.1 bug where many max-ID custom GFX were not loaded (including player-5 map\
    \ sprites) (@ds-sloth, thanks to @AntonioGZZ96 for the report)\n* Fix TheXTech\
    \ v1.3.6 editor bug where NPC properties could change when their layer was hidden.\
    \ (@ds-sloth, thanks to @cre8iveexercise for the report)\n* Fix TheXTech v1.3.6.1\
    \ Android bug where the screen would be black after switching applications. (@ds-sloth)\n\
    * Fix TheXTech 1.3.5.1 bug where the lower half of a player's sprite could be\
    \ shown behind a shoe / sack (@ds-sloth)\n* Fixed the inability to close error\
    \ LunaScript parse error box on Android when file contains too long lines (@Wohlstand)\n\
    * Fixed crash on attempt to execute the \"SetHits\" and \"AllFace\" LunaScript\
    \ commands (@Wohlstand)\n\n</details>\n\n# Known issues\n* Audio may be choppy\
    \ on Old 3DS.\n* Texture load stutter is present on Wii.\n* The viewport is sometimes\
    \ incorrect on Vita.\n* On Windows 10 when running OpenGL with some ~2006 Intel\
    \ iGPU on laptop, game would crash (possibly fixed).\n\n# Screenshots\n\n  <img\
    \ src=\"https://github.com/user-attachments/assets/3b5f6d45-5cb4-4a4f-90ef-7cfbb782472d\"\
    \ width=\"640\" height=\"360\">\n  <img src=\"https://github.com/user-attachments/assets/a2892a41-e3b5-4447-aec1-bf3b8e19e5f8\"\
    \ width=\"400\" height=\"300\">\n  <img src=\"https://github.com/user-attachments/assets/3603ee2e-6161-4b12-8103-ed6bcef0a9d0\"\
    \ width=\"320\" height=\"240\">\n  <img src=\"https://github.com/user-attachments/assets/d5713d7e-ef32-4e0b-827d-d3452c91b16d\"\
    \ width=\"640\" height=\"360\">\n  <img src=\"https://github.com/user-attachments/assets/b9569604-d15b-4c83-9b6e-bd8d23362485\"\
    \ width=\"320\" height=\"240\">\n  <img src=\"https://github.com/user-attachments/assets/ea94e678-f606-4ae5-85b0-3067b9ece034\"\
    \ width=\"640\" height=\"360\">\n"
  updated: '2024-11-17T09:16:16Z'
  version: v1.3.7-beta
  version_title: ' TheXTech v1.3.7-beta: prelude to the big one'
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
stars: 297
systems:
- 3DS
title: TheXTech
update_notes: '<p dir="auto">This release fixes several bugs that was found in the
  previous release of 1.3.6.5 as the possible final release of the 1.3.6.x branch.
  So, the next station is "1.3.7"!</p>

  <h1 dir="auto">Changelog for 1.3.6.6</h1>

  <h2 dir="auto">New vanilla bugfixes:</h2>

  <ul dir="auto">

  <li>Fix vanilla bug where vehicle could be vulnerable if player entered it during
  AltJump (requires frame perfect down press), guarded by compat flag "fix-vehicle-altjump-bug"
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix vanilla bug where vehicle could not be exited if player entered it while
  holding AltJump key, guarded by compat flag "fix-vehicle-altjump-lock" (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix vanilla bug where player can get softlocked if hit by a grabbable NPC while
  digging dirt, guarded by compat flag "fix-player-stuck-on-dirt" (Classic Mode) (<a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h2 dir="auto">TheXTech bugfixes:</h2>

  <ul dir="auto">

  <li>Fixed the problem when a touch screen is not detected on some Android devices
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix minor bug that caused certain configurations on macOS to crash on startup
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix Wii U bug where resizing the game screen could cause the game to crash (<a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 crash caused when a pet mount is eating the last NPC in
  the level and the eaten NPC is killed (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fixed Wii U bug where game quits into the black screen instead of the Wii U''s
  main menu when game started from the Aroma (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wohlstand/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wohlstand">@Wohlstand</a>)</li>

  <li>Fix TheXTech 1.3.6.1 inaccuracy allowing the player to dismount a vehicle when
  blocked by an NPC (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where conveyor belts would sometimes not activate correctly
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 OpenGL bug where the shadow effect interacted inaccurately
  with bitmasked textures (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ds-sloth/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6 bug where it was impossible to unpause while holding an item
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>,
  thanks to SimplyMav for the report)</li>

  <li>Fix TheXTech 1.3.6.1 bug where GIF masks for sizable block 261 were not loaded
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where SMBX level version autodetection did not work
  for platforms (note that this logic will be fully removed in 1.3.7) (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Fix TheXTech 1.3.6.1 bug where NPCs on hidden layers were incorrectly allowed
  to chain-activate (The bug affected the outro scene of Dynamite Grotto in SRW2).
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  <li>Add workaround for TheXTech 1.3.6.1 Modern Mode inaccuracy where NPC clipping
  did not match SMBX 1.3 (This bug affected the same scene). (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ds-sloth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ds-sloth">@ds-sloth</a>)</li>

  </ul>

  <h2 dir="auto">Known issues</h2>

  <ul dir="auto">

  <li>3DS and Wii ports do not run at the native system resolution.</li>

  <li>Audio may be choppy on Old 3DS.</li>

  <li>On Windows 10 when running OpenGL with some ~2006 Intel iGPU on laptop, game
  would crash (possibly fixed).</li>

  <li>Edit 2024-11-02: the included source package will fail to build for an arm64
  Linux target (<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="2630908630" data-permission-text="Title is private" data-url="https://github.com/TheXTech/TheXTech/issues/855"
  data-hovercard-type="issue" data-hovercard-url="/TheXTech/TheXTech/issues/855/hovercard"
  href="https://github.com/TheXTech/TheXTech/issues/855">#855</a>). Tag <code class="notranslate">v1.3.6.6-1</code>
  fixes this issue.</li>

  </ul>

  <h2 dir="auto">Source code: Important note</h2>

  <p dir="auto">If you want to obtain the source code pacakge, please take one of
  three archives named <code class="notranslate">thextech-full-src-v1.3.6.6</code>.
  Don''t download the default source package as it will miss submodules. And because
  of that, it''s unbuildable.</p>

  <p dir="auto">Edit 2024-11-02: if you are building for arm64 Linux, your build is
  likely to fail due to an incompatible ASM file mistakenly included in the build.
  As a workaround, you can modify <code class="notranslate">3rdparty/AudioCodecs/libopus/CMakeLists.txt</code>.
  Replace the line <code class="notranslate">if(OPUS_ARM_ASM AND CMAKE_COMPILER_IS_GNUCC)</code>
  with <code class="notranslate">if(0)</code>. See <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2630908630" data-permission-text="Title
  is private" data-url="https://github.com/TheXTech/TheXTech/issues/855" data-hovercard-type="issue"
  data-hovercard-url="/TheXTech/TheXTech/issues/855/hovercard" href="https://github.com/TheXTech/TheXTech/issues/855">#855</a>
  for details.</p>'
updated: '2024-09-24T02:47:49Z'
version: v1.3.6.6
version_title: 'TheXTech v1.3.6.6: now it''s just a bugfix update'
website: https://wohlsoft.ru/projects/TheXTech/
wiki: https://github.com/TheXTech/TheXTech/wiki
---
This is a direct continuation of the SMBX 1.3 engine. Originally it was written in VB6 for Windows, and later, it got ported/rewritten into C++ and became a cross-platform engine. It completely reproduces the old SMBX 1.3 engine (aside from its Editor), includes many of its logical bugs (critical bugs that lead the game to crash or freeze got fixed), and also adds a lot of new updates and features.