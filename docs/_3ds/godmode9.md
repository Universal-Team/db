---
author: d0k3
avatar: https://avatars.githubusercontent.com/u/12467483?v=4
categories:
- utility
- firm
color: '#130000'
color_bg: '#130000'
created: '2016-01-22T18:00:30Z'
description: 'GodMode9 Explorer - A full access file browser for the Nintendo 3DS
  console :godmode:'
download_page: https://github.com/d0k3/GodMode9/releases
downloads:
  GodMode9-v2.1.1-20220322194259.zip:
    size: 2587358
    size_str: 2 MiB
    url: https://github.com/d0k3/GodMode9/releases/download/v2.1.1/GodMode9-v2.1.1-20220322194259.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
image_length: 9316
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/d0k3/GodMode9/releases/tag/v2.2.0
  downloads:
    GodMode9-v2.2.0-20250322140747.zip:
      size: 3180308
      size_str: 3 MiB
      url: https://github.com/d0k3/GodMode9/releases/download/v2.2.0/GodMode9-v2.2.0-20250322140747.zip
  update_notes: '<p dir="auto">On the faraway date of March 22nd, 2016, a simple ARM9-based
    file browser with one very cool feature (browsing your 3DS NAND file system) was
    released to the general public. At that point, no one would have thought that,
    nine years later, the project would be one of the most important 3DS homebrew
    tools—capable of doing basically everything—and, nonetheless, would still be alive
    and kicking. Still, on its 9th birthday, here''s GodMode9 v2.2.0, and it even
    comes with not one, but two major new features.</p>

    <p dir="auto">Here''s what you can expect:</p>

    <ul dir="auto">

    <li>[new] Translations support, thanks to <a class="user-mention notranslate"
    data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a></li>

    <li>[new] Lua scriping support, thanks to <a class="user-mention notranslate"
    data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a></li>

    <li>[improved?] A shiny new anniversary splash logo</li>

    <li>[fixed] Numerous bugfixes and small improvements</li>

    </ul>

    <p dir="auto">For this release, I decided to be lazy and asked the main authors
    of the two big new features to write their own introductions.</p>

    <p dir="auto"><strong>Lua scripting support</strong><br>

    This release implements Lua scripting! Compared to GM9Script, Lua brings numerous
    advantages, including functions, better control flow, tables, improved file I/O,
    floating point math, modules, error handling, and much more. Every GM9Script feature
    has an equivalent Lua API.</p>

    <p dir="auto">A simple <code class="notranslate">HelloScript.lua</code> is included
    in the release archive, as well as in the repo at <code class="notranslate">resources/sample</code>.
    This script demonstrates basic Lua (both stock and GM9) features. Full documentation
    for every GM9 function is available in <code class="notranslate">lua-doc.md</code>,
    also in the release archive and the repo under <code class="notranslate">resources</code>.
    For standard Lua functions, refer to the <a href="https://www.lua.org/manual/5.4/"
    rel="nofollow">Lua 5.4 Reference Manual</a>.</p>

    <p dir="auto">GM9Script is still included but is now considered legacy and will
    no longer be developed further.</p>

    <p dir="auto"><strong>Translations support</strong><br>

    GodMode9 now speaks your language! You no longer need to download a fork of GodMode9
    and wonder whether it''s up to date to get a different language. If you don’t
    see your language or notice issues and would like to help, head over to the <a
    href="https://crowdin.com/project/GodMode9" rel="nofollow">GodMode9 Crowdin project</a>.</p>

    <p dir="auto">A simple "TRF" format is used to store translations. If you want
    to test new translations, you’ll need to convert the file. Simply place your JSON
    file from Crowdin into the <code class="notranslate">resources/languages</code>
    folder and build GodMode9 to automatically convert and include the TRF in the
    output folder. Alternatively, you can use the <code class="notranslate">transriff.py</code>
    script directly from the <code class="notranslate">utils</code> folder.</p>

    <p dir="auto"><strong>How do I update GodMode9?</strong><br>

    Updating is actually very simple: Just replace <code class="notranslate">GodMode9.firm</code>
    on your SD card with the file from the release ZIP. If you want scripts and translations,
    you should also copy the full <code class="notranslate">./gm9</code> folder from
    inside the archive to the same folder on your SD card. While you''re at it, why
    not also grab <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>’s
    <code class="notranslate">HelloScript.lua</code> from the <code class="notranslate">samples</code>
    folder and tinker around with it?</p>

    <p dir="auto"><strong>Special thanks</strong><br>

    Let’s be honest: With a project running as long as GodMode9 and having as many
    contributors as it does, mentioning and crediting everyone—developers, bug reporters,
    feature suggesters, people who offer advice or web hosting—is an impossible task.
    Just know that I’m thankful to everyone who has supported the project over the
    years.</p>

    <p dir="auto">For this release, special thanks go out to:</p>

    <ul dir="auto">

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>,
    for making this release possible and being a main dev at my side for almost the
    entire lifetime of GodMode9</li>

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>,
    for adding Lua support and greatly expanding scripting capabilities</li>

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
    and all translation contributors, who have been working for years to make GodMode9
    available in multiple languages</li>

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/luigoalma/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/luigoalma">@luigoalma</a>,
    for improving things for devkit users by finally fixing an AES key-related bug</li>

    </ul>'
  update_notes_md: "On the faraway date of March 22nd, 2016, a simple ARM9-based file\
    \ browser with one very cool feature (browsing your 3DS NAND file system) was\
    \ released to the general public. At that point, no one would have thought that,\
    \ nine years later, the project would be one of the most important 3DS homebrew\
    \ tools—capable of doing basically everything—and, nonetheless, would still be\
    \ alive and kicking. Still, on its 9th birthday, here's GodMode9 v2.2.0, and it\
    \ even comes with not one, but two major new features.  \n\nHere's what you can\
    \ expect:\n* [new] Translations support, thanks to @Epicpkmn11\n* [new] Lua scriping\
    \ support, thanks to @ihaveamac\n* [improved?] A shiny new anniversary splash\
    \ logo\n* [fixed] Numerous bugfixes and small improvements\n\nFor this release,\
    \ I decided to be lazy and asked the main authors of the two big new features\
    \ to write their own introductions. \n\n**Lua scripting support**\nThis release\
    \ implements Lua scripting! Compared to GM9Script, Lua brings numerous advantages,\
    \ including functions, better control flow, tables, improved file I/O, floating\
    \ point math, modules, error handling, and much more. Every GM9Script feature\
    \ has an equivalent Lua API.  \n\nA simple `HelloScript.lua` is included in the\
    \ release archive, as well as in the repo at `resources/sample`. This script demonstrates\
    \ basic Lua (both stock and GM9) features. Full documentation for every GM9 function\
    \ is available in `lua-doc.md`, also in the release archive and the repo under\
    \ `resources`. For standard Lua functions, refer to the [Lua 5.4 Reference Manual](https://www.lua.org/manual/5.4/).\
    \  \n\nGM9Script is still included but is now considered legacy and will no longer\
    \ be developed further.  \n\n**Translations support**\nGodMode9 now speaks your\
    \ language! You no longer need to download a fork of GodMode9 and wonder whether\
    \ it's up to date to get a different language. If you don’t see your language\
    \ or notice issues and would like to help, head over to the [GodMode9 Crowdin\
    \ project](https://crowdin.com/project/GodMode9).  \n\nA simple \"TRF\" format\
    \ is used to store translations. If you want to test new translations, you’ll\
    \ need to convert the file. Simply place your JSON file from Crowdin into the\
    \ `resources/languages` folder and build GodMode9 to automatically convert and\
    \ include the TRF in the output folder. Alternatively, you can use the `transriff.py`\
    \ script directly from the `utils` folder.  \n\n**How do I update GodMode9?**\n\
    Updating is actually very simple: Just replace `GodMode9.firm` on your SD card\
    \ with the file from the release ZIP. If you want scripts and translations, you\
    \ should also copy the full `./gm9` folder from inside the archive to the same\
    \ folder on your SD card. While you're at it, why not also grab @ihaveamac’s `HelloScript.lua`\
    \ from the `samples` folder and tinker around with it?  \n\n**Special thanks**\n\
    Let’s be honest: With a project running as long as GodMode9 and having as many\
    \ contributors as it does, mentioning and crediting everyone—developers, bug reporters,\
    \ feature suggesters, people who offer advice or web hosting—is an impossible\
    \ task. Just know that I’m thankful to everyone who has supported the project\
    \ over the years.  \n\nFor this release, special thanks go out to:  \n* @Wolfvak,\
    \ for making this release possible and being a main dev at my side for almost\
    \ the entire lifetime of GodMode9  \n* @ihaveamac, for adding Lua support and\
    \ greatly expanding scripting capabilities  \n* @Epicpkmn11 and all translation\
    \ contributors, who have been working for years to make GodMode9 available in\
    \ multiple languages  \n* @luigoalma, for improving things for devkit users by\
    \ finally fixing an AES key-related bug  \n"
  updated: '2025-03-22T13:24:01Z'
  version: v2.2.0
  version_title: GodMode9 v2.2.0 Ninth Anniversary Release
source: https://github.com/d0k3/GodMode9
stars: 2290
systems:
- 3DS
title: GodMode9
update_notes: '<p dir="auto">Is it really that time of the year again? Six years ago,
  on March 22nd of the faraway year of 2016, GodMode9 was first released to the public.
  It has come a long way, reaching high stability and amassing features. Right now,
  there''s not much left that GodMode9 can''t do, and there''s only the odd bug coming
  in from time to time. As such, this release is a rather small one, with only bugfixes
  and maintenance stuff.</p>

  <p dir="auto">I still wanted to celebrate the day with a release, so here is GodMode9
  v2.1.1 with these changes:</p>

  <ul dir="auto">

  <li>[improved] Improved installation of DSiWare games (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)</li>

  <li>[scripting] Faster script loading as well as other improvements and fixes (thanks
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

  <li>[fixed] Fixed a nasty bug when trimming certain DS cart dumps</li>

  <li>[fixed] Some smaller bugfixes and general code maintenance</li>

  </ul>

  <p dir="auto"><strong>How do I update GodMode9?</strong><br>

  (This may be the last time I tell you how to in the release notes, so please remember)
  You wouldn''t believe how often we get that question when we do a new release. It''s
  actually very simple: Just replace <code class="notranslate">GodMode9.firm</code>
  on your SD card with the file found in the release ZIP. You may also want to update
  scripts, which are found in the <code class="notranslate">./gm9</code> folder inside
  the archive and go to the same folder on your SD card.</p>

  <p dir="auto"><strong>Special thanks</strong><br>

  I''ll be honest, I''ve long given up mentioning everyone here. The sheer number
  of contributors (developers, people who report bugs or suggest features, people
  who help with advice or web hosting...) after 6 years of development is just too
  big. Just know, each and every contribution, no matter how big or small is highly
  appreciated. For this release, special thanks go to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>,
  who''s been a main dev with me for almost all of the lifetime of GodMode9, to <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>
  who did maintenance and fixed bugs, to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>,
  who improved the save game generation and thus the installation for DSiWare CIAs
  and dumps and to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/giiutfff/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/giiutfff">@giiutfff</a>
  who catched a really nasty bug happening when trimming certain DS cart dumps in
  GodMode9 (great catch!).</p>'
updated: '2022-03-22T19:11:38Z'
version: v2.1.1
version_title: GodMode9 v2.1.1 Sixth Anniversary Release
wiki: https://github.com/d0k3/GodMode9/wiki
---
