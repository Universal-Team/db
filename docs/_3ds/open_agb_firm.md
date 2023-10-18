---
author: profi200
avatar: https://avatars.githubusercontent.com/u/7831477?v=4
categories:
- emulator
- firm
color: '#c2e5d8'
color_bg: '#6c8078'
created: '2020-04-15T21:49:42Z'
description: open_agb_firm is a bare metal app for running GBA homebrew/games using
  the 3DS builtin GBA hardware.
download_page: https://github.com/profi200/open_agb_firm/releases
downloads:
  open_agb_firm_alpha_20231006.7z:
    size: 136979
    size_str: 133 KiB
    url: https://github.com/profi200/open_agb_firm/releases/download/alpha_2023-10-6/open_agb_firm_alpha_20231006.7z
github: profi200/open_agb_firm
image: https://avatars.githubusercontent.com/u/7831477?v=4&size=128
image_length: 1560
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/profi200/open_agb_firm
systems:
- 3DS
title: open_agb_firm
update_notes: '<p dir="auto">It''s been a while since i made a new release. Quite
  a few small changes have been made underneath since last year.<br>

  If you have a bit of free time please participate in this little poll: <a href="https://github.com/profi200/open_agb_firm/discussions/135">https://github.com/profi200/open_agb_firm/discussions/135</a></p>

  <h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/78fd101c6634dcc18da6f77b0e6c52bdc967d9bb/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/78fd101c6634dcc18da6f77b0e6c52bdc967d9bb"><tt>78fd101</tt></a>
  ROMs bigger than 32 MiB are now allowed but data beyond 32 MiB is cut off and a
  warning is displayed. This will make certain ROM hacks load at the cost of likely
  crashing later on. You have been warned.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/9bd949731523c7881c649f73d990056c68b2601c/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/9bd949731523c7881c649f73d990056c68b2601c"><tt>9bd9497</tt></a>
  Taking screenshots no longer freeze occasionally and they are created with date
  and time in the name.</li>

  <li>Brightness Control by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/spitzeqc/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/spitzeqc">@spitzeqc</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1281653348"
  data-permission-text="Title is private" data-url="https://github.com/profi200/open_agb_firm/issues/74"
  data-hovercard-type="pull_request" data-hovercard-url="/profi200/open_agb_firm/pull/74/hovercard"
  href="https://github.com/profi200/open_agb_firm/pull/74">#74</a></li>

  <li>Automatic ROM Patching by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/spitzeqc/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/spitzeqc">@spitzeqc</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1291802279"
  data-permission-text="Title is private" data-url="https://github.com/profi200/open_agb_firm/issues/75"
  data-hovercard-type="pull_request" data-hovercard-url="/profi200/open_agb_firm/pull/75/hovercard"
  href="https://github.com/profi200/open_agb_firm/pull/75">#75</a></li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/a70673dea7a1c46d5d41690475aedb58ddefb185/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/a70673dea7a1c46d5d41690475aedb58ddefb185"><tt>a70673d</tt></a>
  Added a tool that can simulate hardware scaling for those who want to experiment
  with the hardware scaling on PC.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/726a4f3355f2547ccf75410da68c86de814b7557/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/726a4f3355f2547ccf75410da68c86de814b7557"><tt>726a4f3</tt></a>
  Headphone detection should no longer fail if there is an integrated microphone/buttons
  (4 pole TRRS plugs).</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/014c341e675be9c3c1da03ba1b9d136cfb69e980/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/014c341e675be9c3c1da03ba1b9d136cfb69e980"><tt>014c341</tt></a>
  Button remapping has been added. See the <a href="https://github.com/profi200/open_agb_firm#input">README</a>
  for details. Circle-Pad mappings are no longer enabled by default to reduce input
  lag.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/8ecc7ce4589004bb9dab8abe4f53c30f5bb9f444/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/8ecc7ce4589004bb9dab8abe4f53c30f5bb9f444"><tt>8ecc7ce</tt></a>
  Added border support for 1:1 scaling mode. I didn''t document this in the README
  yet, sorry. Refer to <a href="https://github.com/profi200/open_agb_firm/issues/44#issuecomment-1674007705"
  data-hovercard-type="issue" data-hovercard-url="/profi200/open_agb_firm/issues/44/hovercard">this
  post</a> for instructions in the meantime.</li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/cf7d1915e0a1dad773cf9e419b9f01343fac68b0/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/cf7d1915e0a1dad773cf9e419b9f01343fac68b0"><tt>cf7d191</tt></a>
  Added software volume control and audio output override. See the <a href="https://github.com/profi200/open_agb_firm#audio">README</a>
  for details.</li>

  <li>GBA database updates by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/HTV04/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/HTV04">@HTV04</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1857022917"
  data-permission-text="Title is private" data-url="https://github.com/profi200/open_agb_firm/issues/128"
  data-hovercard-type="pull_request" data-hovercard-url="/profi200/open_agb_firm/pull/128/hovercard"
  href="https://github.com/profi200/open_agb_firm/pull/128">#128</a></li>

  <li><a class="commit-link" data-hovercard-type="commit" data-hovercard-url="https://github.com/profi200/open_agb_firm/commit/dc5ac1749f9976956ec01ee926c6fb5b7865729f/hovercard"
  href="https://github.com/profi200/open_agb_firm/commit/dc5ac1749f9976956ec01ee926c6fb5b7865729f"><tt>dc5ac17</tt></a>
  Fixed ROM mirroring for 8 mbit games. Thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/endrift/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/endrift">@endrift</a>.</li>

  <li><a href="https://github.com/profi200/libn3ds/commit/451971bbd0cda318cf1189cb9da5af21949e0dcf">An
  audio filter that distorted GBA sound slightly has been disabled</a>. In practice
  this change makes only a minor difference and does not fix the aliasing.</li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/spitzeqc/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/spitzeqc">@spitzeqc</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1281653348" data-permission-text="Title is private" data-url="https://github.com/profi200/open_agb_firm/issues/74"
  data-hovercard-type="pull_request" data-hovercard-url="/profi200/open_agb_firm/pull/74/hovercard"
  href="https://github.com/profi200/open_agb_firm/pull/74">#74</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/profi200/open_agb_firm/compare/alpha_2022-4-25...alpha_2023-10-6"><tt>alpha_2022-4-25...alpha_2023-10-6</tt></a></p>'
updated: '2023-10-06T14:22:33Z'
version: alpha_2023-10-6
version_title: open_agb_firm alpha build 2023-10-6
---
