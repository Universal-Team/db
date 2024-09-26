---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 811807
    size_str: 792 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.0.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1167017
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.0.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1172
systems:
- DS
title: nds-bootstrap
update_notes: "<p align=\"center\" dir=\"auto\">\n   <a target=\"_blank\" rel=\"noopener\
  \ noreferrer\" href=\"https://github.com/DS-Homebrew/nds-bootstrap/blob/master/images/200th\
  \ Release/Logo.png\"><img src=\"https://github.com/DS-Homebrew/nds-bootstrap/blob/master/images/200th\
  \ Release/Logo.png\" style=\"max-width: 100%;\"></a><br>\n</p>\n<p dir=\"auto\"\
  >Welcome to nds-bootstrap's 200th release!<br>\nIn this new version, you'll find\
  \ many new improvements for game compatibility! Also, in B4DS mode, some games which\
  \ have not booted in a long time, now finally boot!</p>\n<p dir=\"auto\">Included\
  \ in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.8.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v27.8.0</a></p>\n<p dir=\"auto\"\
  >Instructions:</p>\n<ol dir=\"auto\">\n<li>Download the <code class=\"notranslate\"\
  >.7z</code> or <code class=\"notranslate\">.zip</code> file.</li>\n<li>Extract the\
  \ nds-bootstrap <code class=\"notranslate\">.nds</code> and <code class=\"notranslate\"\
  >.ver</code> files, to <code class=\"notranslate\">root:/_nds/</code>.</li>\n</ol>\n\
  <h3 dir=\"auto\">What's new?</h3>\n<ul dir=\"auto\">\n<li>Remember <em>Foto Showdown</em>?\
  \ The <em>Pokémon</em> clone where you get new monsters using your DSi or 3DS camera,\
  \ and use them in battles?<br>\nYou can now play it on your DS Phat or DS Lite console,\
  \ with one difference!<br>\nThe camera lens will either be substituted with a video\
  \ (Place the video file in <code class=\"notranslate\">fat:/_nds/nds-bootstrap/dsiCamera/</code>\
  \ and name it <code class=\"notranslate\">default.bin</code>, must be recorded using\
  \ dsi-camcorder), or it'll just be covered and you'll see nothing.</li>\n<li>If\
  \ you use a debug/dev model of the DS, you can now also play <em>System Flaw</em>\
  \ &amp; <em>System Flaw: Recruit</em>!</li>\n<li>The ROM pre-load settings from\
  \ the nds-bootstrap-extras repo are now part of nds-bootstrap itself, as they'll\
  \ help reduce some ROM load issues causing some frame flickers and/or slowdown in\
  \ certain games, regardless of which frontend you use!</li>\n<li>Card Read DMA patching\
  \ is now implemented in B4DS mode, making more games such as <em>Army Men: Soldiers\
  \ of Misfortune</em>, <em>The Magic School Bus: Oceans</em>, and <em>Ultimate Mortal\
  \ Kombat</em> now work on DS flashcards!</li>\n<li><em>Minna no Mahjong DS</em>,\
  \ <em>Diddy Kong Racing DS</em>, and <em>Golden Sun: Dark Dawn</em> now work in\
  \ B4DS mode, as their save functions are now directly patched on arm9.</li>\n<li><em>Mario\
  \ Hoops 3-on-3</em> now works in B4DS mode, as a missing patch has been added.</li>\n\
  <li>The Kiosk Demo version of <em>Mario Kart DS</em> now boots on DS and DSi consoles!</li>\n\
  <li><em>Nintendo DS Guide Server</em> now boots!</li>\n<li>If your DSi console no\
  \ longer has LEDs powering on (as a result of a bricked BPTWL I2C chip), but can\
  \ still manage to boot it using ntrboot, patches are now implemented to allow games\
  \ to work properly!</li>\n<li>Card Read DMA patching has been re-enabled for TWL\
  \ titles running in DSi mode.</li>\n<li>Improved the ROM pre-loading feature on\
  \ DSi/3DS, as it now tries to pre-load only the NitroFS data, if the ROM is slightly\
  \ too big to fit in the console's RAM.\n<ul dir=\"auto\">\n<li>In addition, for\
  \ full ROM pre-loading, 480KB of DSi WRAM are now allocated for a few more ROMs\
  \ to be pre-loaded.</li>\n</ul>\n</li>\n<li>The Sound/Mic frequency setting now\
  \ works in homebrew!</li>\n</ul>\n<h3 dir=\"auto\">Bug fixes</h3>\n<ul dir=\"auto\"\
  >\n<li>On DSi consoles, in <em>Pokémon Black &amp; White 1&amp;2</em> running in\
  \ DSi mode, scrolling in the bag menu no longer has slowdown.\n<ul dir=\"auto\"\
  >\n<li>Hopefully, the random crashes are also gone.</li>\n</ul>\n</li>\n<li>On DSi\
  \ consoles, the intro of <em>MegaMan Battle Network 5: Double Team DS</em> no longer\
  \ has slight slowdowns.</li>\n<li>In B4DS mode, the European version of <em>Super\
  \ Princess Peach</em> now boots!</li>\n<li>On DSi/3DS consoles, flickering in the\
  \ title screens of <em>Dragon Quest IV</em> &amp; <em>VI</em> have been reduced.</li>\n\
  <li>On DSi consoles, <em>Nervous Brickdown</em> &amp; <em>Big Bang Mini</em> no\
  \ longer crash on black screens on startup!</li>\n<li>Fixed bugged music playback\
  \ in <em>Cooking Mama 2: Dinner with Friends</em> running in DSiWare exploits (such\
  \ as Memory Pit) and/or in DSi mode.</li>\n<li>In B4DS mode, due to the implementation\
  \ of Card Read DMA, <em>Tony Hawk's American Sk8land</em> no longer hangs when getting\
  \ into gameplay.</li>\n<li>In B4DS mode, due to the implementation of Card Read\
  \ DMA, <em>Call of Duty: Modern Warfare 3</em> no longer crashes during a cutscene.</li>\n\
  <li><em>Nintendo DSi Shop</em> &amp; <em>System Settings</em> no longer crash on\
  \ white screens.</li>\n<li>Optimized touch screen mode switching code to fix where\
  \ the sound would no longer play on certain DSi/3DS consoles.</li>\n<li>Other minor\
  \ fixes.</li>\n</ul>\n<h3 dir=\"auto\">Known bugs</h3>\n<ul dir=\"auto\">\n<li>As\
  \ both <em>Nintendo DSi Shop</em> &amp; <em>System Settings</em> no longer show\
  \ white screens, they'll instead show the stock DSi error screen. This is due to\
  \ them being unable to read the version data from TWLNAND, but the fix for this\
  \ is unknown.</li>\n<li><em>Viva Piñata: Pocket Paradise</em> now also works in\
  \ B4DS mode, but does not save.</li>\n</ul>\n<p dir=\"auto\">A special wallpaper\
  \ featuring 5 games that now work in B4DS mode has been made available here!:<br>\n\
  <a href=\"https://github.com/DS-Homebrew/nds-bootstrap/blob/master/images/200th%20Release/Wallpaper.png\"\
  >https://github.com/DS-Homebrew/nds-bootstrap/blob/master/images/200th%20Release/Wallpaper.png</a></p>"
updated: '2024-09-17T03:37:56Z'
version: v2.0.0
version_title: 'v2.0.0: 200th Release'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.