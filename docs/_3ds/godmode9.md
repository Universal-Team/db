---
author: d0k3
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
    url: https://github.com/d0k3/GodMode9/releases/download/v1.9.1/GodMode9-v1.9.1-20200110121417.zip
github: d0k3/GodMode9
image: https://raw.githubusercontent.com/d0k3/GodMode9/master/resources/logo.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/d0k3/GodMode9/releases/tag/v1.9.2pre1
  downloads:
    GodMode9-v1.9.2pre1-20200820205253.zip:
      size: 2243273
      url: https://github.com/d0k3/GodMode9/releases/download/v1.9.2pre1/GodMode9-v1.9.2pre1-20200820205253.zip
  update_notes: '<p>Yup, we''re pretty late for this. Real life(tm) got in the way,
    and we didn''t make the anniversary release on time this year. With the recent
    influx of screeninit relate bug reports we got another very good reason to finally
    give you this. Here''s the new GodMode9 release and this is what you get:</p>

    <ul>

    <li>[new] Mount support for title.db (thanks <a class="user-mention" data-hovercard-type="user"
    data-hovercard-url="/users/aspargas2/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

    <li>[new] Support for handling variable sized tickets (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/luigoalma/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/luigoalma">@luigoalma</a>)</li>

    <li>[improved] Proper mount support for ticket.db (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

    <li>[improved] Various improvements to the CIA builder, mostly for CIA from NCSD</li>

    <li>[improved] Tons of small performance improvements (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>)</li>

    <li>[improved] Much smaller firm size (thanks <a class="user-mention" data-hovercard-type="user"
    data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>)</li>

    <li>[fixed] Fixed screen init (for real this time!) (thanks <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>)</li>

    <li>[fixed] Tons of small bug fixes</li>

    <li>[preview] Possibility to install NCCH, NCSD (.3DS), DSiWare NDS, CIA, NUS/CDN
    to the system</li>

    </ul>

    <p><strong>Did you know?</strong><br>

    The actual first public release of GodMode9 was GodMode9 v0.2.0, which was released
    on March 22nd, 2016. A lot has happened since then, and a lot of people contributed
    to this with code, bug reports and testing. GodMode9 transitioned from early entrypoints
    (Brahma anyone?) to the modern FIRM sighax entrypoint and gained more and more
    functionality, leading it to be what it is today - one of the most important swiss
    army knife utilities for the Nintendo 3DS console.</p>

    <p><strong>A prerelease?</strong><br>

    While this has undergone basic testing, and we made sure nothing bad will happen,
    it is still considered beta state. New stuff may still be a little rough around
    the edges. Your feedback will help us to improve on what''s left to do. We already
    know, turning off the backlight on a closed lid does no more work (a fix is in
    the works). We also included a preview of what we''re currently working on - installing
    game images (directly from game cartridges works, too) to your system. This feature
    should still be used with caution (not marked as preview for no reason, maybe
    have a NAND backup ready?). Game installing will be improved and extended upon
    in the coming release.</p>

    <p><strong>GodMode9 bootloader</strong><br>

    When we introduced the GodMode9 bootloader, there was basically just one other
    alternative, which was <a href="https://github.com/SciresM/boot9strap">boot9strap</a>.
    We intended to provide the user with an alternative, providing more customization
    and possibilities. Nowadays, we got <a href="https://github.com/derrekr/fastboot3DS">fastboot3ds</a>
    (which coincidentally is also coauthored by d0k3), and, if we''re honest, the
    GodMode9 bootloader just can''t hold the candle to fastboot3DS (not as a bootloader,
    that is). For this reason, the GodMode9 bootloader will be removed starting with
    the next major release. If you feel that decision is not right, you''re free to
    discuss with us. We''re available in the <a href="https://discord.gg/EGu6Qxw"
    rel="nofollow">GodMode9 Discord channel</a>.</p>

    <p><strong>Credits</strong><br>

    GodMode9 is not a one man project, it wouldn''t have gotten anywhere near what
    it is today without the help of numerous people. A big thank you for this release
    goes to <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>,
    who provided a ton of code, including support for <code>ticket.db</code> and <code>title.db</code>
    manipulation (laying the base for game image installing) and lots of other, smaller
    bugfixes. Another big thank you goes to <a class="user-mention" data-hovercard-type="user"
    data-hovercard-url="/users/profi200/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/profi200">@profi200</a>,
    who provided the solution to our screen init issues and to <a class="user-mention"
    data-hovercard-type="user" data-hovercard-url="/users/Wolfvak/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/Wolfvak">@Wolfvak</a>,
    for porting that solution to GodMode9, in addition to all the work he''s putting
    into improvements of the GodMode9 code base and performance. I also thank everyone
    who helped us out with bug reports, testing and all members of the <a href="https://discord.gg/EGu6Qxw"
    rel="nofollow">official GodMode9 Discord channel</a>.</p>'
  updated: '2020-08-22T10:18:04Z'
  version: v1.9.2pre1
  version_title: GodMode9 v1.9.2pre1 Fourth Anniversary Edition
scripts:
  GodMode9.firm:
  - file: GodMode9.*.zip
    message: Downloading GodMode9 zip...
    output: /GodMode9.zip
    repo: d0k3/GodMode9
    type: downloadRelease
  - file: /GodMode9.zip
    input: GodMode9.firm
    message: Extracting the GodMode9.firm...
    output: /luma/payloads/GodMode9.firm
    type: extractFile
  - file: /GodMode9.zip
    input: gm9/
    message: Extracting the /gm9/ directory...
    output: /gm9/
    type: extractFile
  - file: /luma/payloads/GodMode9.firm.sha
    message: Deleting a stowaway file...
    type: deleteFile
  - file: /GodMode9.zip
    message: Deleting the downloaded ZIP file...
    type: deleteFile
  '[prerelease] GodMode9.firm':
  - file: GodMode9.*.zip
    includePrereleases: true
    message: Downloading GodMode9 zip...
    output: /GodMode9.zip
    repo: d0k3/GodMode9
    type: downloadRelease
  - file: /GodMode9.zip
    input: GodMode9.firm
    message: Extracting the GodMode9.firm...
    output: /luma/payloads/GodMode9.firm
    type: extractFile
  - file: /GodMode9.zip
    input: gm9/
    message: Extracting the /gm9/ directory...
    output: /gm9/
    type: extractFile
  - file: /luma/payloads/GodMode9.firm.sha
    message: Deleting a stowaway file...
    type: deleteFile
  - file: /GodMode9.zip
    message: Deleting the downloaded ZIP file...
    type: deleteFile
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
