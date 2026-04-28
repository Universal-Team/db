---
author: DiscostewSM
avatar: https://avatars.githubusercontent.com/u/10163038?v=4
categories:
- app
color: '#463c35'
color_bg: '#463c35'
created: '2016-02-25T20:40:34Z'
description: Play SNES SPC-dumped files on your 3DS
download_page: https://github.com/DiscostewSM/blargSpc/releases
downloads:
  blargSpc.zip:
    size: 101793
    size_str: 99 KiB
    url: https://github.com/DiscostewSM/blargSpc/releases/download/v0.1/blargSpc.zip
github: DiscostewSM/blargSpc
image: https://avatars.githubusercontent.com/u/10163038?v=4&size=128
image_length: 29061
layout: app
screenshots:
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/blargspc/menu.png
source: https://github.com/DiscostewSM/blargSpc
stars: 3
systems:
- 3DS
title: blargSpc
update_notes: <p dir="auto">Play SNES SPC-dumped files on your 3DS</p>
updated: '2016-02-25T20:42:30Z'
version: v0.1
version_title: blargSpc
---
BlargSPC is a homebrew SPC player that is capable to play SNES SPC-dumped files on the 3DS. It is based on the SPC/DSP cores og blargSNES.

### FAQ

Q. This can play SPC files of games that currently have no audio in blargSNES. Does that mean a fix for blargSNES is coming soon?

Unfortunately, no, not because of this anyways. The reason why blargSNES has trouble with some audio in games is because of communication/sync problems (among other things) between the main CPU and SPC cores.

SPC files you may find online were dumped by other emulators that don't have this problem. But, at least this shows that the audio can process/play once this issue with blargSNES is resolved.

Q. Wait, I can play SPC files of games with enhancement chips in them. Does that mean...

No, it does not. The SPC/DSP cores are completely independant from the rest of the system with the exception of a couple of lines to the main CPU used for SPC uploading/downloading.