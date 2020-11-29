---
author: RedShyGuy
categories:
- utility
color: '#947677'
created: '2019-08-22T07:15:13Z'
description: Animal Crossing NL Vapecord Public Plugin WIP
download_page: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/tag/v1.8.1
downloads:
  Vapecord.Public.zip:
    size: 4330434
    url: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/download/v1.8.1/Vapecord.Public.zip
github: RedShyGuy/Vapecord-ACNL-Plugin
image: https://avatars1.githubusercontent.com/u/43783060?v=4
layout: app
scripts:
  For ACNL EUR:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086400/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086400/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL JPN:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086200/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086200/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL KOR:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086500/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086500/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL USA:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000086300/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000086300/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL WA EUR:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198f00/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000198f00/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL WA JPN:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198d00/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000198d00/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL WA USA:
  - file: Vapecord.Public.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/0004000000198e00/
    message: Extracting Vapecord...
    output: /luma/plugins/0004000000198e00/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
  For ACNL Welcome Luxury:
  - file: Vapecord.Luxury.zip
    message: Downloading Vapecord.Public.zip...
    output: /Vapecord.zip
    repo: RedShyGuy/Vapecord-ACNL-Plugin
    type: downloadRelease
  - file: /Vapecord.zip
    input: luma/plugins/00040000004C5700/
    message: Extracting Vapecord...
    output: /luma/plugins/00040000004C5700/
    type: extractFile
  - file: /Vapecord.zip
    input: boot.firm
    message: Extracting boot.firm...
    output: /boot.firm
    type: extractFile
  - file: sdmc:/Vapecord.zip
    message: Deleting Vapecord.zip...
    type: deleteFile
source: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin
systems:
- 3DS
title: Vapecord-ACNL-Plugin
update_notes: "# New Update!!\r\nTook again some time but here a new update! [Edited\
  \ for newest boot.firm so plugin works with newest 3DS Firmware]\r\n\r\n## The update\
  \ has those features:\r\n> Grass Editor (lets you edit the grass state at your coordinates)\r\
  \n> Chat Text2Item\r\n> Language Picker overhaul\r\n> Player Loader\r\n> Player\
  \ Selector overhaul\r\n> Everything Seeder\r\n> and more!\r\n\r\n## There are also\
  \ some bug fixes:\r\n> Player Randomizer fixed\r\n> Text2Item doesn't crash on the\
  \ island while the chat is open anymore\r\n> Other players shouldn't be able to\
  \ crash you anymore\r\n> If Language file is missing plugin doesn't abort anymore\r\
  \n> Anti Animation is now 100% Bug-Free (it should)\r\n> Item Sequence is now 100%\
  \ crash-free\r\n> and more!\r\n\r\n## How to use:\r\nunzip `Vapecord.Public.zip`\
  \ and put everything on it in the root of your SD-Card\r\nThen open the Rosalina\
  \ Menu and press `Plugin Loader: [Disabled]` (after you pressed it will say `Plugin\
  \ Loader: \r\n[Enabled]`)\r\n(If you only update the plugin delete all old `.3gx`\
  \ files and copy the new ones at those places instead)\r\nThen just start your game!\r\
  \nIf you encounter any bugs feel free to report them on the official [Vapecord Discord\
  \ Server](https://discord.gg/w9nvqjW).\r\n\r\n#### And I think that was it :)\r\n\
  #### Have fun with the update!!"
updated: '2020-11-10T22:24:13Z'
version: v1.8.1
version_title: ACNL Vapecord Public Plugin [v.1.8.1][EDIT]
wiki: https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/wiki
---
