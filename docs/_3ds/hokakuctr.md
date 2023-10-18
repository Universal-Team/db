---
author: Pretendo Network
avatar: https://avatars.githubusercontent.com/u/36684034?v=4
categories:
- utility
color: '#2b2952'
color_bg: '#2b2952'
created: '2022-02-16T15:25:17Z'
description: A 3DS game plugin (3GX) to dump the RMC communication between 3DS games
  and NEX. The traffic is dumped to the SD into pcap files.
download_page: https://github.com/PretendoNetwork/HokakuCTR/releases
downloads:
  HokakuCTR.3gx:
    size: 293726
    size_str: 286 KiB
    url: https://github.com/PretendoNetwork/HokakuCTR/releases/download/v1.0.2/HokakuCTR.3gx
github: PretendoNetwork/HokakuCTR
image: https://avatars.githubusercontent.com/u/36684034?v=4&size=128
image_length: 2746
layout: app
source: https://github.com/PretendoNetwork/HokakuCTR
systems:
- 3DS
title: HokakuCTR
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>Update 3gx.ld based on latest one in testplugin by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/TraceEntertains/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TraceEntertains">@TraceEntertains</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1936238983"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/HokakuCTR/issues/5"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/HokakuCTR/pull/5/hovercard"
  href="https://github.com/PretendoNetwork/HokakuCTR/pull/5">#5</a></li>

  <li>Add title ID and metadata version to start of packets by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/jonbarrow/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/jonbarrow">@jonbarrow</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1936340593"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/HokakuCTR/issues/6"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/HokakuCTR/pull/6/hovercard"
  href="https://github.com/PretendoNetwork/HokakuCTR/pull/6">#6</a></li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/TraceEntertains/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/TraceEntertains">@TraceEntertains</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1936238983" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/HokakuCTR/issues/5"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/HokakuCTR/pull/5/hovercard"
  href="https://github.com/PretendoNetwork/HokakuCTR/pull/5">#5</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/jonbarrow/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/jonbarrow">@jonbarrow</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1936340593" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/HokakuCTR/issues/6"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/HokakuCTR/pull/6/hovercard"
  href="https://github.com/PretendoNetwork/HokakuCTR/pull/6">#6</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/PretendoNetwork/HokakuCTR/compare/v1.0.1...v1.0.2"><tt>v1.0.1...v1.0.2</tt></a></p>'
updated: '2023-10-16T22:50:41Z'
version: v1.0.2
version_title: v1.0.2
website: https://pretendo.network/
---
## Usage

1. Install the latest [Luma3DS](luma3ds).
2. Navigate to **luma/plugins** and copy the **.3gx** file as **default.3gx** to load it for all game or place it inside a folder with the game *titleID* you want to use.
3. Open the Rosalina menu and enable the plugin loader.
4. Launch the game to dump traffic from. The screen should flash blue and some text will display on the screen. If it says **Not Ready**, it means this game is not compatible. If it says **Ready**, you can go online to dump the traffic.

The dumps will be placed inside the **HokakuCTR** folder in the SD card root.