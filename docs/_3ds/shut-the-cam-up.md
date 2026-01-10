---
author: TehFridge
avatar: https://avatars.githubusercontent.com/u/85436576?v=4
categories:
- utility
color: '#b19bc7'
color_bg: '#716380'
created: '2023-08-22T17:07:42Z'
description: Removes the camera shutter and high-pitched beep sound from the Nintendo
  3DS (works on all 3ds apps that use the camera)
download_page: https://github.com/TehFridge/ShutTheCamUp/releases
downloads:
  new3ds.ips:
    size: 76
    size_str: 76 Bytes
    url: https://github.com/TehFridge/ShutTheCamUp/releases/download/main/new3ds.ips
  old3ds.ips:
    size: 76
    size_str: 76 Bytes
    url: https://github.com/TehFridge/ShutTheCamUp/releases/download/main/old3ds.ips
github: TehFridge/ShutTheCamUp
image: https://avatars.githubusercontent.com/u/85436576?v=4&size=128
image_length: 33969
layout: app
source: https://github.com/TehFridge/ShutTheCamUp
stars: 46
systems:
- 3DS
title: Shut The Cam Up
update_notes: '<p dir="auto">Yea here are the patches.<br>

  Have fun taking photos and recording videos in peace and quiet.</p>'
updated: '2023-08-22T17:19:59Z'
version: main
version_title: Initial release lol.
---
# DISCLAIMER
I do not condone any misuses of this patch for malicious purposes or whatever.

# Why tho?
Imagine you are playing your 3ds in a cafe or smt, you need to use the camera feature in some game (for example. Face Raiders) and suddenly the shutter sound bursts out of the speakers and people look at you weirdly, we wouldnt want that. 

Also like... phones don't do that sort of thing (well maybe in japan, china cause there the law demands that anything with a camera has to have a shutter sound)

I mostly created this patch cause i like the vibe of vlogging with a 3ds. It has its charm you know.

# How is it possible?!
The shutter sound was embedded in some system process, we just discovered it now lol. So i just decided to null the bytes with audio data, and it worked!

# Does it work on both Old and New 3DS?
Yup. there are two seperate patches individually for the new and old model of the console.