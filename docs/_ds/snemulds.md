---
author: cotodevel
avatar: https://avatars.githubusercontent.com/u/12502589?v=4
categories:
- emulator
color: '#848383'
color_bg: '#807f7f'
created: '2025-06-05T04:39:38Z'
github: cotodevel/snemulds
icon: https://db.universal-team.net/assets/images/icons/snemulds.png
image: https://db.universal-team.net/assets/images/images/snemulds.png
image_length: 342
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
source: https://github.com/cotodevel/snemulds
stars: 8
systems:
- DS
title: snemulds
updated: '---'
---
Usage:
- Download and copy all files starting arm7dldi-[ntr/twl] and `snemul.cfg` to the SD root
   - [NTR] is for DS mode, and [TWL] is for DSi mode
   - If it prompts for overwrite: Yes to All
   - Create a `snes` folder in the SD root, and put your games in it
- SPC Playback: Optionally, create an `spc` folder in the SD root, and put your SPC files in it
   - You can choose and play an SPC File in the "SPC Jukebox" option
- [NTR]: Now open loader (internal, hbmenu or other), and run `ToolchainGenericDS-multiboot.nds`. Then select `SnemulDS.nds` from the menu, choose ARG (A button) and select the SNES file to run
- [TWL]: Now open TWiLight Menu++ (you must set it up first, so you can run TWL mode apps), and run `ToolchainGenericDS-multiboot.srl`. Then select `SnemulDS.srl` from the menu, choose ARG (A button) and select the snes file to run