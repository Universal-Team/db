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
  GodMode9-v2.2.2-20260329220448.zip:
    size: 3493357
    size_str: 3 MiB
    url: https://github.com/d0k3/GodMode9/releases/download/v2.2.2/GodMode9-v2.2.2-20260329220448.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
image_length: 9316
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/d0k3/GodMode9
stars: 2479
systems:
- 3DS
title: GodMode9
update_notes: '<p dir="auto"><em>Is it really ten years already?</em> On March 22nd,
  2016, a simple ARM9-based file browser was first released to the public. Back then,
  it was little more than a nerdy tool for curious users wanting to explore the inner
  workings of their 3DS. Much has happened since, and GodMode9 has evolved into the
  Swiss army knife you know and (hopefully) love today.</p>

  <p dir="auto">Here''s what''s new in 2.2.2:</p>

  <ul dir="auto">

  <li>[new] Text editor replaces the text viewer (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/nevumx/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/nevumx">@nevumx</a>)</li>

  <li>[new] Ability to write to <code class="notranslate">nvram.mem</code> (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>)</li>

  <li>[new] Implemented Lua io <code class="notranslate">file:lines</code> function
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>)</li>

  <li>[new] I2C device read/write support from Lua (<a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/rosaage/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/rosaage">@rosaage</a>)</li>

  <li>[improved] Lua updated to 5.4.8 (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/MisterSheeple/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/MisterSheeple">@MisterSheeple</a>)</li>

  <li>[improved] Added gyro model detection to Lua and System Info (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/rosaage/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/rosaage">@rosaage</a>)</li>

  <li>[improved] Proper dumping of ID2 when dumping carts (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/AriA99/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/AriA99">@AriA99</a>)
  (<a href="https://github.com/d0k3/GodMode9/pull/862#issuecomment-3240213122" data-hovercard-type="pull_request"
  data-hovercard-url="/d0k3/GodMode9/pull/862/hovercard">explanation</a>)</li>

  <li>[fixed] Proper handling for the locale of file sizes in scripts (<a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)</li>

  <li>[fixed] <code class="notranslate">io.open</code> read mode ("r") works properly
  (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>)</li>

  <li>[fixed] <code class="notranslate">file:read</code> returns <code class="notranslate">nil</code>
  at end of file instead of an empty string (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ihaveamac/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>)</li>

  </ul>

  <p dir="auto"><code class="notranslate">file:read</code> now matches stock Lua io
  behavior. This improves compatibility with existing Lua modules, but it is technically
  a breaking change and may require script updates if they relied on the previous
  behavior. Please make sure to update your scripts if needed.</p>

  <p dir="auto"><strong>Trivia corner: GodMode9 origins</strong><br>

  <a href="https://github.com/d0k3/Decrypt9WIP">Decrypt9WIP</a> is the technical predecessor
  of GodMode9. It started as a fork of <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/archshift/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/archshift">@archshift</a>’s
  <a href="https://github.com/archshift/Decrypt9">Decrypt9</a>, which had its first
  commit on February 1st, 2015. My first contribution to the fork came on June 23rd,
  2015. Decrypt9WIP was a menu-based toolkit focused on ARM9-based decryption of gamecart
  dumps — essentially the foundation of many tasks you use GodMode9 for today. Over
  time, Decrypt9WIP fully superseded Decrypt9.<br>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/48e2db9e-b415-407e-b132-62889865aba3"><img
  width="400" height="240" alt="snap005" src="https://github.com/user-attachments/assets/48e2db9e-b415-407e-b132-62889865aba3"
  style="max-width: 100%; height: auto; max-height: 240px;"></a><a target="_blank"
  rel="noopener noreferrer" href="https://github.com/user-attachments/assets/fdeb6e2c-3d3a-4ba8-8e7c-0011c37004c6"><img
  width="400" height="240" alt="snap006" src="https://github.com/user-attachments/assets/fdeb6e2c-3d3a-4ba8-8e7c-0011c37004c6"
  style="max-width: 100%; height: auto; max-height: 240px;"></a></p>

  <p dir="auto"><a href="https://github.com/d0k3/CTRXplorer">CTRXplorer</a> is the
  conceptual predecessor of GodMode9, first released on June 7th, 2015. It is a simple,
  userland-based file browser (installable via CIA) with a design concept that will
  likely feel familiar to GodMode9 users today.<br>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/dd0f5f26-8e12-4d44-b768-6758a01dd15e"><img
  width="400" height="480" alt="h4CJ6SE" src="https://github.com/user-attachments/assets/dd0f5f26-8e12-4d44-b768-6758a01dd15e"
  style="max-width: 100%; height: auto; max-height: 480px;"></a><a target="_blank"
  rel="noopener noreferrer" href="https://github.com/user-attachments/assets/5b2afd83-bd04-4da9-88d8-b37654e63510"><img
  width="400" height="480" alt="wWe72jf" src="https://github.com/user-attachments/assets/5b2afd83-bd04-4da9-88d8-b37654e63510"
  style="max-width: 100%; height: auto; max-height: 480px;"></a></p>

  <p dir="auto"><strong>How to update GodMode9</strong><br>

  Updating is simple: replace <code class="notranslate">GodMode9.firm</code> on your
  SD card with the file from the release ZIP. If you want scripts and translations,
  copy the full <code class="notranslate">./gm9</code> folder from inside the archive
  to the same location on your SD card.</p>

  <p dir="auto"><strong>Special thanks</strong><br>

  Writing this part is always tricky — not because I’m ungrateful, quite the opposite.
  GodMode9 has been running for 10 years, and the true number of contributors is hard
  to capture. GitHub lists <a href="https://github.com/d0k3/GodMode9/graphs/contributors">58
  contributors</a>, but many others have helped with advice, documentation, hosting,
  testing, bug reports, and more. Every contribution is valuable and helped make GodMode9
  what it is today.</p>

  <p dir="auto">For this anniversary release, special thanks go out to:</p>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ihaveamac/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ihaveamac">@ihaveamac</a>
  — for ongoing work on Lua and countless other contributions</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  — for keeping GodMode9 available in multiple languages</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/nevumx/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/nevumx">@nevumx</a>
  — for contributing this release’s killer feature and for their patience</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>
  — as a core dev at my side for almost the entire lifetime of GodMode9</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/al3x10m/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/al3x10m">@al3x10m</a>
  — <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/al3x10m/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/al3x10m">@al3x10m</a>
  — for supporting the project from the beginning and helping me with many other things
  along the way</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/archshift/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/archshift">@archshift</a>
  — for laying the foundation of GodMode9</li>

  </ul>'
updated: '2026-03-29T20:07:32Z'
version: v2.2.2
version_title: GodMode9 v2.2.2 Tenth Anniversary Release
wiki: https://github.com/d0k3/GodMode9/wiki
---
