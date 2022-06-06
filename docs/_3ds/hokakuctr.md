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
  Hokaku3DS.3gx:
    size: 277493
    size_str: 270 KiB
    url: https://github.com/PretendoNetwork/HokakuCTR/releases/download/v1.0/Hokaku3DS.3gx
github: PretendoNetwork/HokakuCTR
icon_index: 205
image: https://avatars.githubusercontent.com/u/36684034?v=4&size=128
image_length: 2746
layout: app
source: https://github.com/PretendoNetwork/HokakuCTR
systems:
- 3DS
title: HokakuCTR
update_notes: <p dir="auto">Initial release, will probably have many compatibility
  issues and bugs, but at least it works!</p>
updated: '2022-02-17T00:23:41Z'
version: v1.0
version_title: Initial Release
website: https://pretendo.network/
---
## Usage

1. Install the [Luma3DS 3GX plugin loader](https://github.com/Nanquitas/Luma3DS/releases/latest).
2. Navigate to **luma/plugins** and copy the **.3gx** file as **default.3gx** to load it for all game or place it inside a folder with the game *titleID* you want to use.
3. Open the Rosalina menu and enable the plugin loader.
4. Launch the game to dump traffic from. The screen should flash blue and some text will display on the screen. If it says **Not Ready**, it means this game is not compatible. If it says **Ready**, you can go online to dump the traffic.

The dumps will be placed inside the **HokakuCTR** folder in the SD card root.