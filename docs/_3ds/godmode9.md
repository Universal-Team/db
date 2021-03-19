---
author: d0k3
avatar: https://avatars.githubusercontent.com/u/12467483?v=4
categories:
- utility
- firm
color: '#130000'
created: '2016-01-22T18:00:30Z'
description: 'GodMode9 Explorer - A full access file browser for the Nintendo 3DS
  console :godmode:'
download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.1
downloads:
  GodMode9-v1.9.1-20200110121417.zip:
    size: 1840083
    size_str: 1 MiB
    url: https://github.com/d0k3/GodMode9/releases/download/v1.9.1/GodMode9-v1.9.1-20200110121417.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
image_length: 9316
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.3pre1
  downloads:
    GodMode9-v1.9.3pre1-20210222175159.zip:
      size: 2341086
      size_str: 2 MiB
      url: https://github.com/d0k3/GodMode9/releases/download/v1.9.3pre1/GodMode9-v1.9.3pre1-20210222175159.zip
  update_notes: '<p>Has it really been half a year since the last prerelease and more
    than one year since the last proper release? Obviously it has, so a new one is
    overdue. This is another prerelease, with a lot of new stuff:</p>

    <ul>

    <li>[new] Completely rewritten MCU event handler (fixes a lot of stuff) (thanks
    <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>)</li>

    <li>[new] Ability to install, build CIA from, verify, identify DSi CDN content
    (read below)</li>

    <li>[new] Title manager available via HOME menu (read below)</li>

    <li>[new] NDS carts can be dumped with secure area encrypted (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/mariomadproductions/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mariomadproductions">@mariomadproductions</a>
    for testing)</li>

    <li>[new] Gamecart drive <code>G:/</code> now includes an info text file (thanks
    <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/GerbilSoft/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/GerbilSoft">@GerbilSoft</a>)</li>

    <li>[new] Tickets can now be verified, installed and identified</li>

    <li>[new] Trimming functionality for GBA rom dumps</li>

    <li>[improved] Improved title info functionality, now compatible with more files</li>

    <li>[improved] Several improvements to the GM9 MegaScript (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

    <li>[improved] Several improvements to the game image installer</li>

    <li>[improved] Improved CIA builder, with stricter checks for legit builds</li>

    <li>[improved] Better handling of special cases in cart dumper (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/GerbilSoft/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/GerbilSoft">@GerbilSoft</a>)</li>

    <li>[fixed] Proper seed handling when installing game images to the system</li>

    <li>[fixed] Countless smaller fixes and improvements, too many to list</li>

    <li>[scripting] <code>install</code> command for installing game images</li>

    <li>[scripting] Quotes can be escaped (<code>\"</code>) in variables</li>

    </ul>

    <p><strong>A prerelease again?</strong><br>

    I know what you''re thinking: you want a proper release, with no strings attached.
    In fact, this will be coming, too, and very soon. We''re doing a prerelease now
    so the testing can start. This might be a little rough around the edges, and we''re
    hoping the community will help us get rid of any quirks left. Everything in GM9
    needs testing, but especially the new stuff mentioned in the changelog above.
    Looking forward to your bug reports!</p>

    <p><strong>Title manager</strong><br>

    The title manager may be the one feature most relevant to our users in this release.
    It enables you to get an overview of your installed titles, build CIAs and even
    (batch-) uninstall stuff from your system. To enter the title manager, press  and
    select <code>Title manager</code>. SD installed titles are found on the <code>A:/</code>
    drive, system titles and DSiWare titles are found on the <code>1:/</code> drive.</p>

    <p><strong>Handling DSi CDN content</strong><br>

    The other killer feature in this release is the ability to handle contents from
    the DSi CDN. That means you are now able to install, build a CIA from, verify
    or identify any title that was in the DSi eShop. You''re on your own providing
    these files, of course. The <code>Nintendo DSi (Digital) (CDN)</code> dat-file
    over on <a href="https://datomatic.no-intro.org/" rel="nofollow">No-Intro</a>
    may help you get your CDN files in order. You will also need to provide a <code>decTitlekeys.bin</code>
    file (with DSi titlekeys included) inside the <code>0:/GM9/support/</code> folder.</p>'
  update_notes_md: 'Has it really been half a year since the last prerelease and more
    than one year since the last proper release? Obviously it has, so a new one is
    overdue. This is another prerelease, with a lot of new stuff:

    * [new] Completely rewritten MCU event handler (fixes a lot of stuff) (thanks
    @Wolfvak)

    * [new] Ability to install, build CIA from, verify, identify DSi CDN content (read
    below)

    * [new] Title manager available via HOME menu (read below)

    * [new] NDS carts can be dumped with secure area encrypted (thanks @mariomadproductions
    for testing)

    * [new] Gamecart drive `G:/` now includes an info text file (thanks @GerbilSoft)

    * [new] Tickets can now be verified, installed and identified

    * [new] Trimming functionality for GBA rom dumps

    * [improved] Improved title info functionality, now compatible with more files

    * [improved] Several improvements to the GM9 MegaScript (thanks @aspargas2)

    * [improved] Several improvements to the game image installer

    * [improved] Improved CIA builder, with stricter checks for legit builds

    * [improved] Better handling of special cases in cart dumper (thanks @GerbilSoft)

    * [fixed] Proper seed handling when installing game images to the system

    * [fixed] Countless smaller fixes and improvements, too many to list

    * [scripting] `install` command for installing game images

    * [scripting] Quotes can be escaped (`\"`) in variables


    **A prerelease again?**

    I know what you''re thinking: you want a proper release, with no strings attached.
    In fact, this will be coming, too, and very soon. We''re doing a prerelease now
    so the testing can start. This might be a little rough around the edges, and we''re
    hoping the community will help us get rid of any quirks left. Everything in GM9
    needs testing, but especially the new stuff mentioned in the changelog above.
    Looking forward to your bug reports!


    **Title manager**

    The title manager may be the one feature most relevant to our users in this release.
    It enables you to get an overview of your installed titles, build CIAs and even
    (batch-) uninstall stuff from your system. To enter the title manager, press <HOME>
    and select `Title manager`. SD installed titles are found on the `A:/` drive,
    system titles and DSiWare titles are found on the `1:/` drive.


    **Handling DSi CDN content**

    The other killer feature in this release is the ability to handle contents from
    the DSi CDN. That means you are now able to install, build a CIA from, verify
    or identify any title that was in the DSi eShop. You''re on your own providing
    these files, of course. The `Nintendo DSi (Digital) (CDN)` dat-file over on [No-Intro](https://datomatic.no-intro.org/)
    may help you get your CDN files in order. You will also need to provide a `decTitlekeys.bin`
    file (with DSi titlekeys included) inside the `0:/GM9/support/` folder. '
  updated: '2021-02-22T16:56:59Z'
  version: v1.9.3pre1
  version_title: GodMode9 v1.9.3pre1
source: https://github.com/d0k3/GodMode9
systems:
- 3DS
title: GodMode9
update_notes: '<p>Time for a new GodMode9 release. The last major release, v1.9.0,
  was a pretty solid release to begin with, but as always there is room for improvement.
  This one focuses on bugfixes, fixing stuff that v1.9.0 did not do right. This is
  new:</p>

  <ul>

  <li>[new] On verification, offer fixing for badly decrypted NCCH/NCSD</li>

  <li>[improved] Much faster scrolling speeds in wordwrapped text view</li>

  <li>[improved] Largely improved method of GBA VC save injection (thanks <a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/TurdPooCharger/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TurdPooCharger">@TurdPooCharger</a>)</li>

  <li>[fixed] Fixed the .BPS code in scripting (thanks <a class="user-mention" data-hovercard-type="user"
  data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>)</li>

  <li>[fixed] Fixed a crash in the DISA/DIFF handling code (thanks <a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

  <li>[fixed] Actually allow decrypting N3DS NATIVE_FIRM on O3DS</li>

  <li>[fixed] Last search drive is back again</li>

  <li>[fixed] Cart drive checking (don''t show empty when it isn''t</li>

  <li>[fixed] Notification light handling</li>

  </ul>

  <p><strong>Did you know?</strong><br>

  This marks the 40th release of GodMode9, with a whopping 1260 commits leading up
  to here. GodMode9 is now in it''s fourth year of development and still going strong,
  thanks to all of my fellow developers, bug reporters and feature requesters.</p>

  <p><strong>Tsktsktsk</strong><br>

  We''ve been seeing a lot of bug reports these days with people telling us they can''t
  convert their NCSD (".3DS") files to CIA in GodMode9. It can be assumed that <em>all
  of them</em> got their <em>badly decrypted</em> .3DS files from some shady source.
  Shady source: please at least provide proper decrypted files. <a class="user-mention"
  data-hovercard-type="organization" data-hovercard-url="/orgs/citra-emu/hovercard"
  href="https://github.com/citra-emu">@citra-emu</a>: maybe stop supporting these
  files or at least give a warning to users? We, for our part, now properly detect
  these files and offer fixing. To use the new fixer, just verify your files.</p>

  <p><strong>Credits</strong><br>

  As always this wouldn''t have been possible without some help. Thanks go to <a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>,
  <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>
  and <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/TurdPooCharger/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TurdPooCharger">@TurdPooCharger</a>
  for actively contributing to development. I also thank everyone submitting bug reports
  and feature requests. A special mention goes to <a class="user-mention" data-hovercard-type="user"
  data-hovercard-url="/users/HIDE810/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/HIDE810">@HIDE810</a>
  who finally pointed out that text viewer scrolling is awfully slow in some cases
  and needs some work. Thanks, all of you!</p>'
updated: '2020-01-10T18:33:56Z'
version: v1.9.1
version_title: GodMode9 v1.9.1
wiki: https://github.com/d0k3/GodMode9/wiki
---
