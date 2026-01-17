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
  GodMode9-v2.2.1-20251024082253.zip:
    size: 3362618
    size_str: 3 MiB
    url: https://github.com/d0k3/GodMode9/releases/download/v2.2.1/GodMode9-v2.2.1-20251024082253.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
image_length: 9316
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/d0k3/GodMode9
stars: 2416
systems:
- 3DS
title: GodMode9
update_notes: '<p dir="auto"><em>Didn''t we already have a Ninth Anniversary Release</em>?
  That''s what you''d be asking if you closely followed the GodMode9 repo and noticed
  the prerelease that came out on the proper anniversary day (March 22nd) this year.
  Most users, however, are still using the now three-year-old GodMode9 v2.1.1 and
  didn''t have their ninth anniversary update yet. This release aims to bring the
  new goodies to a wider audience. It fixes bugs, and it even brings two small new
  features with it.</p>

  <p dir="auto">Here''s what was new with v2.2.0:</p>

  <ul dir="auto">

  <li>[new] Translation support, thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Epicpkmn11/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a></li>

  <li>[new] Lua scripting support, thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ihaveamac/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a></li>

  <li>[improved?] A shiny new anniversary splash logo</li>

  <li>[fixed] Numerous bug fixes and small improvements</li>

  </ul>

  <p dir="auto">And here''s what''s new in v2.2.1:</p>

  <ul dir="auto">

  <li>[new] Optional signature checking when verifying NCSD &amp; NCCH</li>

  <li>[new] Ability to restore original encryption in NCSD &amp; NCCH</li>

  <li>[new] Lua support for optional signature checking, thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a></li>

  <li>[improved] Updated translations and fonts, thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a></li>

  <li>[fixed] Numerous bug fixes and small improvements</li>

  </ul>

  <p dir="auto">For this release, I also suggest you read the <a href="https://github.com/d0k3/GodMode9/releases/tag/v2.2.0">GodMode9
  v2.2.0 release notes</a>. As for the two new features: Keep in mind that signature
  checking verification will always fail for modified dumps, which would be the case
  for Azahar-supported CCI as well (we''ll get to that).  Restoring the original encryption
  (via the <code class="notranslate">Encrypt file (...)</code> submenu entry) will
  effectively fix signatures, but this feature has limits and won''t repair completely
  borked files.</p>

  <p dir="auto"><strong>Why doesn''t GodMode9 dump .CCI files?</strong><br>

  You may want to dump your game carts in a CCI format compatible with <a href="https://github.com/azahar-emu/azahar">Azahar</a>,
  and you may have noticed GodMode9 only offers 3DS files. Spoiler alert: <em>3DS
  is the exact same format as CCI</em>. The only thing you need to pay attention to
  is that Azahar expects decrypted files. So, use the <code class="notranslate">Decrypt
  file (...)</code> submenu entry to let GodMode9 handle the heavy lifting. And don''t
  forget to rename your dumped files, as Azahar will only accept files with <code
  class="notranslate">.CCI</code> extension. You''re a GodMode9-wielding power user,
  you can do that, right?</p>

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

  And here''s to the part that always gives me the biggest headache. Because, with
  a project running as long as GodMode9 and having as many contributors as it does,
  mentioning and crediting everyone — developers, bug reporters, feature suggesters,
  people who offer advice or web hosting—is an impossible task. Just know that I’m
  thankful to everyone who has supported the project over the years.</p>

  <p dir="auto">For this release, special thanks go out to:</p>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>,
  for being a main dev at my side for almost the entire lifetime of GodMode9</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>,
  for adding Lua support and greatly expanding scripting capabilities, also for giving
  me the original idea for encryption restoration</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and all translation contributors, who have been working for years to make GodMode9
  available in multiple languages</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/luigoalma/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/luigoalma">@luigoalma</a>,
  for improving things for devkit users by finally fixing an AES key-related bug</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ZeroSkill1/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ZeroSkill1">@ZeroSkill1</a>,
  for helping me a great deal understanding signature checking</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/MisterSheeple/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/MisterSheeple">@MisterSheeple</a>,
  for helping me out with some testing</li>

  <li>The fine folks on the <a href="https://discord.gg/BRcbvtFxX4" rel="nofollow">GodMode9
  Discord</a></li>

  <li>All <a href="https://www.3dbrew.org/wiki/Main_Page" rel="nofollow">3dbrew.org</a>
  contributors</li>

  <li>Martin Korth for <a href="https://problemkaputt.de/gbatek.htm" rel="nofollow">GBATEK</a></li>

  </ul>'
updated: '2025-10-24T09:29:03Z'
version: v2.2.1
version_title: GodMode9 v2.2.1 Ninth Anniversary Release
wiki: https://github.com/d0k3/GodMode9/wiki
---
