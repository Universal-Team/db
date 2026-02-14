---
author: Pretendo Network
avatar: https://avatars.githubusercontent.com/u/36684034?v=4
categories:
- utility
color: '#5e586c'
color_bg: '#5e586c'
created: '2022-02-16T15:25:17Z'
description: A 3DS game plugin (3GX) to dump the RMC communication between 3DS games
  and NEX. The traffic is dumped to the SD into pcap files.
download_page: https://github.com/PretendoNetwork/HokakuCTR/releases
downloads:
  HokakuCTR.3gx:
    size: 293838
    size_str: 286 KiB
    url: https://github.com/PretendoNetwork/HokakuCTR/releases/download/v1.0.3/HokakuCTR.3gx
github: PretendoNetwork/HokakuCTR
image: https://avatars.githubusercontent.com/u/36684034?v=4&size=128
image_length: 3197
layout: app
source: https://github.com/PretendoNetwork/HokakuCTR
stars: 44
systems:
- 3DS
title: HokakuCTR
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>Fix packet dumping on games with blank process names (Sonic Generations, Style
  Savvy: Trendsetters, etc.) by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Nasina7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Nasina7">@Nasina7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2219451950"
  data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/HokakuCTR/issues/13"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/HokakuCTR/pull/13/hovercard"
  href="https://github.com/PretendoNetwork/HokakuCTR/pull/13">#13</a></li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Nasina7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Nasina7">@Nasina7</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2219451950" data-permission-text="Title is private" data-url="https://github.com/PretendoNetwork/HokakuCTR/issues/13"
  data-hovercard-type="pull_request" data-hovercard-url="/PretendoNetwork/HokakuCTR/pull/13/hovercard"
  href="https://github.com/PretendoNetwork/HokakuCTR/pull/13">#13</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/PretendoNetwork/HokakuCTR/compare/v1.0.2...v1.0.3"><tt>v1.0.2...v1.0.3</tt></a></p>'
updated: '2024-04-02T17:28:11Z'
version: v1.0.3
version_title: v1.0.3
website: https://pretendo.network/
---
## Usage

1. Install the latest [Luma3DS](luma3ds).
2. Navigate to **luma/plugins** and copy the **.3gx** file as **default.3gx** to load it for all game or place it inside a folder with the game *titleID* you want to use.
3. Open the Rosalina menu and enable the plugin loader.
4. Launch the game to dump traffic from. The screen should flash blue and some text will display on the screen. If it says **Not Ready**, it means this game is not compatible. If it says **Ready**, you can go online to dump the traffic.

The dumps will be placed inside the **HokakuCTR** folder in the SD card root.