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
  3dsx.2.0.0.zip:
    size: 725083
    size_str: 708 KiB
    url: https://github.com/PretendoNetwork/nimbus/releases/download/v2.0.0/3dsx.2.0.0.zip
  cia.2.0.0.zip:
    size: 958561
    size_str: 936 KiB
    url: https://github.com/PretendoNetwork/nimbus/releases/download/v2.0.0/cia.2.0.0.zip
  combined.2.0.0.zip:
    size: 1377571
    size_str: 1 MiB
    url: https://github.com/PretendoNetwork/nimbus/releases/download/v2.0.0/combined.2.0.0.zip
github: PretendoNetwork/nimbus
icon: https://db.universal-team.net/assets/images/icons/nimbus.png
image: https://db.universal-team.net/assets/images/images/nimbus.png
image_length: 6460
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
screenshots:
- description: Nintendo
  url: https://db.universal-team.net/assets/images/screenshots/nimbus/nintendo.png
- description: Pretendo
  url: https://db.universal-team.net/assets/images/screenshots/nimbus/pretendo.png
source: https://github.com/PretendoNetwork/nimbus
stars: 190
systems:
- 3DS
title: Nimbus
unique_ids:
- '0xD40D2'
update_notes: '<h2 dir="auto">Important Note</h2>

  <p dir="auto">Unlike Nimbus v2.0.0-rc1, this release doesn''t require any special
  steps when upgrading from either v1.6.1 or older nor from this release candidate.
  When updating to this version, the patches will not be applied until you open the
  application, in which case it will deploy the update files on their proper location
  and handle any migration procedures automatically.</p>

  <h2 dir="auto">What''s New</h2>

  <ul dir="auto">

  <li><strong>Improvements on account management and error handling.</strong> If an
  error happens while switching accounts, they will be reported on screen for easier
  debugging.</li>

  <li><strong>New multi-purpose plugin.</strong> This plugin bundles patches for game
  exploits, a PID logger for a bunch of games and HokakuCTR. This plugin must be activated
  each time you want to use it from the Nimbus app by pressing the Y button.</li>

  </ul>

  <h3 dir="auto">FAQ: When switching accounts I sometimes get the following error:
  d8a0c4e5</h3>

  <p dir="auto"><strong>Short explanation:</strong> This error is very uncommon, but
  it can be fixed by trying again or disabling Wi-Fi to ensure it doesn''t happen.</p>

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
  by retrying the account switch or disabling Wi-Fi on the console full stop to ensure
  it always disconnects successfully.</p>

  <h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>[Important] Fix Miiverse patch misattribution and missing license by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/TraceEntertains/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TraceEntertains">@TraceEntertains</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2543543281"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/51"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/51/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/51">#51</a></li>

  <li>feat: Improve account management by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/DaniElectra/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2892197672"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/54"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/54/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/54">#54</a></li>

  <li>feat: Add PNID migration tool and bump version to 2.0.0 by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/DaniElectra/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3226007444"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/63"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/63/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/63">#63</a></li>

  <li>feat: Add Nimbus plugin by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/DaniElectra/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3311691806"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/65"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/65/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/65">#65</a></li>

  <li>chore: Point support to our Discord server by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/DaniElectra/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3476726087"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/67"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/67/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/67">#67</a></li>

  <li>feat: Make the Nimbus app deploy the update by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/DaniElectra/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/DaniElectra">@DaniElectra</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3696944389"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/nimbus/issues/68"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/nimbus/pull/68/hovercard"
  href="https://github.com/PretendoNetwork/nimbus/pull/68">#68</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/PretendoNetwork/nimbus/compare/v1.6.1...v2.0.0"><tt>v1.6.1...v2.0.0</tt></a></p>'
updated: '2025-12-09T00:34:40Z'
version: v2.0.0
version_title: v2.0.0
---
#### Usage
- Run the Nimbus homebrew and choose to use either a Pretendo or Nintendo account

If the app doesn't work, try the following steps:
- Reboot your 3DS while holding SELECT and make sure "Enable loading external FIRMs and modules" and "Enable game patching" are both turned on
- Ensure that your Luma3DS version is 13.0 or higher