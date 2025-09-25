---
author: Pretendo Network
avatar: https://avatars.githubusercontent.com/u/36684034?v=4
categories:
- utility
color: '#2b2952'
color_bg: '#2b2952'
created: '2022-01-08T01:36:02Z'
download_page: https://github.com/PretendoNetwork/nimbus/releases
downloads:
  3dsx.1.6.1.zip:
    size: 407820
    size_str: 398 KiB
    url: https://github.com/PretendoNetwork/nimbus/releases/download/v1.6.1/3dsx.1.6.1.zip
  cia.1.6.1.zip:
    size: 642456
    size_str: 627 KiB
    url: https://github.com/PretendoNetwork/nimbus/releases/download/v1.6.1/cia.1.6.1.zip
  combined.1.6.1.zip:
    size: 1043340
    size_str: 1018 KiB
    url: https://github.com/PretendoNetwork/nimbus/releases/download/v1.6.1/combined.1.6.1.zip
github: PretendoNetwork/nimbus
icon: https://db.universal-team.net/assets/images/icons/nimbus.png
image: https://db.universal-team.net/assets/images/images/nimbus.png
image_length: 6460
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/PretendoNetwork/nimbus/releases/tag/v2.0.0-rc1
  downloads:
    3dsx.2.0.0-rc1.zip:
      size: 723732
      size_str: 706 KiB
      url: https://github.com/PretendoNetwork/nimbus/releases/download/v2.0.0-rc1/3dsx.2.0.0-rc1.zip
    cia.2.0.0-rc1.zip:
      size: 956427
      size_str: 934 KiB
      url: https://github.com/PretendoNetwork/nimbus/releases/download/v2.0.0-rc1/cia.2.0.0-rc1.zip
    combined.2.0.0-rc1.zip:
      size: 1373548
      size_str: 1 MiB
      url: https://github.com/PretendoNetwork/nimbus/releases/download/v2.0.0-rc1/combined.2.0.0-rc1.zip
  update_notes: '<h2 dir="auto">BREAKING CHANGES <g-emoji class="g-emoji" alias="warning">⚠️</g-emoji></h2>

    <p dir="auto">This new release requires user intervention for existing installations.
    Please check below for how to install this update. <strong>You MUST follow this
    procedure EXACTLY, or your PNID will be removed and you''ll have to take some
    recovery steps</strong>.</p>

    <ul dir="auto">

    <li>If you are installing Nimbus for the first time, you can skip this section.</li>

    <li>If you have connected to Pretendo in the past but don''t have a PNID linked
    to your console, you MUST still follow these steps, or you will have problems
    when linking one in the future.</li>

    </ul>

    <h3 dir="auto">Update steps</h3>

    <ol dir="auto">

    <li>Install the <code class="notranslate">nimbus.3dsx</code> or <code class="notranslate">nimbus.cia</code>
    file <strong>ONLY. DO NOT COPY ANY OTHER FILES YET!</strong></li>

    <li>Launch the new version of Nimbus<br>

    2.1. The new version of Nimbus should show the version <code class="notranslate">2.0.0</code>
    on the bottom-right corner of the top screen. If this isn''t the case, verify
    that you are launching the correct version and you have installed everything properly.</li>

    <li>Press the B button to save your PNID</li>

    <li>If everything goes well, Nimbus will show a success message<br>

    4.1. If Nimbus shows an error, ask on our <a href="https://discord.gg/pretendo"
    rel="nofollow">Discord</a> or the <a href="https://forum.pretendo.network/" rel="nofollow">forum</a>
    for assistance</li>

    <li>Press START to exit Nimbus and copy all of the other files for the update.
    You should now be good to go!</li>

    </ol>

    <h3 dir="auto">Recovery steps</h3>

    <p dir="auto">If you have copied all of the Nimbus files and you haven''t saved
    your PNID, you have to follow these recovery steps:</p>

    <ol dir="auto">

    <li><strong>Ensure you have installed Nimbus 2.0.0 correctly and that the version
    shows on screen when opening it</strong></li>

    <li>If you are connected to Pretendo, open Nimbus and switch to the Nintendo account.
    If you are already connected to Nintendo, skip to the next step<br>

    2.1. This is required because the Pretendo account is now in a bugged state where
    it has a Pretendo Friend Code but it''s linked to your <strong>Nintendo NNID</strong>,
    because the <strong>Pretendo PNID</strong> was deleted from the system</li>

    <li>Open Nimbus and switch to the Pretendo account<br>

    3.1. This will recreate the Pretendo PNID and link the Pretendo account back to
    it</li>

    <li>After this, opening the NNID settings should now show the account creation
    and linking screen properly</li>

    </ol>

    <h2 dir="auto">What''s New</h2>

    <ul dir="auto">

    <li><strong>Improvements on account management and error handling.</strong> If
    an error happens while switching accounts, they will be reported on screen for
    easier debugging.</li>

    <li><strong>New multi-purpose plugin.</strong> This plugin bundles patches for
    game exploits, a PID logger for a bunch of games and HokakuCTR. This plugin must
    be activated each time you want to use it from the Nimbus app by pressing the
    Y button.</li>

    </ul>

    <h3 dir="auto">FAQ: When switching accounts I sometimes get the following error:
    d8a0c4e5</h3>

    <p dir="auto"><strong>Short explanation:</strong> This error is very uncommon,
    but it can be fixed by trying again or disabling Wi-Fi to ensure it doesn''t happen.</p>

    <p dir="auto"><strong>Long explanation:</strong></p>

    <p dir="auto">Before switching accounts, the system must be logged out from any
    accounts to be able to switch to another one. However, the friends sysmodule requires
    to be disconnected from the friends server in order to log out, or it will throw
    <code class="notranslate">FPD::Connected</code>, the error from above. There isn''t
    any API available to "disconnect" from the server, so the way it works is by blocking
    the network connection (in a similar way as when switching from Internet to Local
    Play) to get the friends sysmodule to disconnect from the server.</p>

    <p dir="auto">Our code checks for when the friends sysmodule actually gets disconnected,
    so this error shouldn''t in theory happen, but there have been very rare instances
    of this error popping up despite the fact. As mentioned, this issue can be fixed
    by retrying the account switch or disabling Wi-Fi on the console full stop to
    ensure it always disconnects successfully.</p>

    <h2 dir="auto">What''s Changed</h2>

    <ul dir="auto">

    <li>[Important] Fix Miiverse patch misattribution and missing license by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/TraceEntertains/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TraceEntertains">@TraceEntertains</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="2543543281" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/51"
    data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/51/hovercard"
    href="https://github.com/PretendoNetwork/nimbus/pull/51">#51</a></li>

    <li>feat: Improve account management by <a class="user-mention notranslate" data-hovercard-type="user"
    data-hovercard-url="/users/DaniElectra/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="2892197672" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/54"
    data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/54/hovercard"
    href="https://github.com/PretendoNetwork/nimbus/pull/54">#54</a></li>

    <li>feat: Add PNID migration tool and bump version to 2.0.0 by <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/DaniElectra/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="3226007444" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/63"
    data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/63/hovercard"
    href="https://github.com/PretendoNetwork/nimbus/pull/63">#63</a></li>

    <li>feat: Add Nimbus plugin by <a class="user-mention notranslate" data-hovercard-type="user"
    data-hovercard-url="/users/DaniElectra/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
    in <a class="issue-link js-issue-link" data-error-text="Failed to load title"
    data-id="3311691806" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/65"
    data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/65/hovercard"
    href="https://github.com/PretendoNetwork/nimbus/pull/65">#65</a></li>

    </ul>

    <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/PretendoNetwork/nimbus/compare/v1.6.1...v2.0.0-rc1"><tt>v1.6.1...v2.0.0-rc1</tt></a></p>'
  update_notes_md: "## BREAKING CHANGES :warning:\n\nThis new release requires user\
    \ intervention for existing installations. Please check below for how to install\
    \ this update. **You MUST follow this procedure EXACTLY, or your PNID will be\
    \ removed and you'll have to take some recovery steps**.\n - If you are installing\
    \ Nimbus for the first time, you can skip this section.\n - If you have connected\
    \ to Pretendo in the past but don't have a PNID linked to your console, you MUST\
    \ still follow these steps, or you will have problems when linking one in the\
    \ future.\n\n### Update steps\n\n1. Install the `nimbus.3dsx` or `nimbus.cia`\
    \ file **ONLY. DO NOT COPY ANY OTHER FILES YET!**\n2. Launch the new version of\
    \ Nimbus\n  2.1. The new version of Nimbus should show the version `2.0.0` on\
    \ the bottom-right corner of the top screen. If this isn't the case, verify that\
    \ you are launching the correct version and you have installed everything properly.\n\
    3. Press the B button to save your PNID\n4. If everything goes well, Nimbus will\
    \ show a success message\n  4.1. If Nimbus shows an error, ask on our [Discord](https://discord.gg/pretendo)\
    \ or the [forum](https://forum.pretendo.network/) for assistance\n5. Press START\
    \ to exit Nimbus and copy all of the other files for the update. You should now\
    \ be good to go!\n\n### Recovery steps\n\nIf you have copied all of the Nimbus\
    \ files and you haven't saved your PNID, you have to follow these recovery steps:\n\
    \n1. **Ensure you have installed Nimbus 2.0.0 correctly and that the version shows\
    \ on screen when opening it**\n2. If you are connected to Pretendo, open Nimbus\
    \ and switch to the Nintendo account. If you are already connected to Nintendo,\
    \ skip to the next step\n  2.1. This is required because the Pretendo account\
    \ is now in a bugged state where it has a Pretendo Friend Code but it's linked\
    \ to your **Nintendo NNID**, because the **Pretendo PNID** was deleted from the\
    \ system\n3. Open Nimbus and switch to the Pretendo account\n  3.1. This will\
    \ recreate the Pretendo PNID and link the Pretendo account back to it\n4. After\
    \ this, opening the NNID settings should now show the account creation and linking\
    \ screen properly\n\n## What's New\n\n- **Improvements on account management and\
    \ error handling.** If an error happens while switching accounts, they will be\
    \ reported on screen for easier debugging.\n- **New multi-purpose plugin.** This\
    \ plugin bundles patches for game exploits, a PID logger for a bunch of games\
    \ and HokakuCTR. This plugin must be activated each time you want to use it from\
    \ the Nimbus app by pressing the Y button.\n\n### FAQ: When switching accounts\
    \ I sometimes get the following error: d8a0c4e5\n\n**Short explanation:** This\
    \ error is very uncommon, but it can be fixed by trying again or disabling Wi-Fi\
    \ to ensure it doesn't happen.\n\n**Long explanation:**\n\nBefore switching accounts,\
    \ the system must be logged out from any accounts to be able to switch to another\
    \ one. However, the friends sysmodule requires to be disconnected from the friends\
    \ server in order to log out, or it will throw `FPD::Connected`, the error from\
    \ above. There isn't any API available to \"disconnect\" from the server, so the\
    \ way it works is by blocking the network connection (in a similar way as when\
    \ switching from Internet to Local Play) to get the friends sysmodule to disconnect\
    \ from the server.\n\nOur code checks for when the friends sysmodule actually\
    \ gets disconnected, so this error shouldn't in theory happen, but there have\
    \ been very rare instances of this error popping up despite the fact. As mentioned,\
    \ this issue can be fixed by retrying the account switch or disabling Wi-Fi on\
    \ the console full stop to ensure it always disconnects successfully.\n\n## What's\
    \ Changed\n* [Important] Fix Miiverse patch misattribution and missing license\
    \ by @TraceEntertains in https://github.com/PretendoNetwork/nimbus/pull/51\n*\
    \ feat: Improve account management by @DaniElectra in https://github.com/PretendoNetwork/nimbus/pull/54\n\
    * feat: Add PNID migration tool and bump version to 2.0.0 by @DaniElectra in https://github.com/PretendoNetwork/nimbus/pull/63\n\
    * feat: Add Nimbus plugin by @DaniElectra in https://github.com/PretendoNetwork/nimbus/pull/65\n\
    \n\n**Full Changelog**: https://github.com/PretendoNetwork/nimbus/compare/v1.6.1...v2.0.0-rc1"
  updated: '2025-08-18T21:25:39Z'
  version: v2.0.0-rc1
  version_title: v2.0.0-rc1
screenshots:
- description: Nintendo
  url: https://db.universal-team.net/assets/images/screenshots/nimbus/nintendo.png
- description: Pretendo
  url: https://db.universal-team.net/assets/images/screenshots/nimbus/pretendo.png
source: https://github.com/PretendoNetwork/nimbus
stars: 180
systems:
- 3DS
title: Nimbus
unique_ids:
- '0xD40D2'
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>fix(patches/http): Close frd:u handle upon successful request by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DaniElectra/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2308566628"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/43"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/43/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/43">#43</a>

  <ul dir="auto">

  <li>Fixes shutdown time being longer than usual</li>

  </ul>

  </li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/PretendoNetwork/nimbus/compare/v1.6.0...v1.6.1"><tt>v1.6.0...v1.6.1</tt></a></p>'
updated: '2024-07-02T20:57:06Z'
version: v1.6.1
version_title: v1.6.1
---
#### Usage
- Run the Nimbus homebrew and choose to use either a Pretendo or Nintendo account

If the app doesn't work, try the following steps:
- Reboot your 3DS while holding SELECT and make sure "Enable loading external FIRMs and modules" and "Enable game patching" are both turned on
- Ensure that your Luma3DS version is 13.0 or higher