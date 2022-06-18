---
author: Coto
avatar: https://bytebucket.org/ravatar/%7B9cf0f24a-1db9-40d3-b6f4-116761b7fe0b%7D?ts=default
bitbucket:
  branch: master
  repo: Coto88/snemulds
categories:
- emulator
color: '#848383'
color_bg: '#807f7f'
created: '2018-06-04T05:11:19.373852+00:00'
description: SnemulDS 0.6 [Revival]
icon: https://db.universal-team.net/assets/images/icons/snemulds.png
icon_index: 19
image: https://db.universal-team.net/assets/images/images/snemulds.png
image_length: 342
layout: app
nightly:
  download_page: https://bitbucket.org/Coto88/snemulds/src/master/release
  downloads:
    arm7dldi-ntr/SNEmulDS.nds:
      url: https://bitbucket.org/Coto88/snemulds/raw/master/release/arm7dldi-ntr/SNEmulDS.nds
    arm7dldi-twl/SNEmulDS.srl:
      url: https://bitbucket.org/Coto88/snemulds/raw/master/release/arm7dldi-twl/SNEmulDS.srl
    arm7dldi-twl/ToolchainGenericDS-multiboot.srl:
      url: https://bitbucket.org/Coto88/snemulds/raw/master/release/arm7dldi-twl/ToolchainGenericDS-multiboot.srl
    arm7dldi-twl/tgds_multiboot_payload_twl.bin:
      url: https://bitbucket.org/Coto88/snemulds/raw/master/release/arm7dldi-twl/tgds_multiboot_payload_twl.bin
    snemul.cfg:
      url: https://bitbucket.org/Coto88/snemulds/raw/master/release/snemul.cfg
  qr:
    arm7dldi-ntr/SNEmulDS.nds: https://db.universal-team.net/assets/images/qr/nightly/arm7dldi-ntrsnemulds-nds.png
source: https://bitbucket.org/Coto88/snemulds
systems:
- DS
title: SnemulDS
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