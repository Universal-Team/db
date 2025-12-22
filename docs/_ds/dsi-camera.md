---
author: Pk11
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- utility
color: '#676967'
color_bg: '#676967'
created: '2020-08-03T07:14:58Z'
description: A simple example homebrew app that can use the DSi's cameras
download_page: https://github.com/Epicpkmn11/dsi-camera/releases
downloads:
  dsi-camera.cia:
    size: 302336
    size_str: 295 KiB
    url: https://github.com/Epicpkmn11/dsi-camera/releases/download/v1.1.0/dsi-camera.cia
  dsi-camera.nds:
    size: 287744
    size_str: 281 KiB
    url: https://github.com/Epicpkmn11/dsi-camera/releases/download/v1.1.0/dsi-camera.nds
github: Epicpkmn11/dsi-camera
icon: https://db.universal-team.net/assets/images/icons/dsi-camera.png
image: https://db.universal-team.net/assets/images/icons/dsi-camera.png
image_length: 630
layout: app
license: unlicense
license_name: The Unlicense
qr:
  dsi-camera.cia: https://db.universal-team.net/assets/images/qr/dsi-camera-cia.png
  dsi-camera.nds: https://db.universal-team.net/assets/images/qr/dsi-camera-nds.png
screenshots:
- description: Taking a picture
  url: https://db.universal-team.net/assets/images/screenshots/dsi-camera/taking-a-picture.png
source: https://github.com/Epicpkmn11/dsi-camera
stars: 50
systems:
- DS
title: dsi-camera
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Photos are now saved at 640×480! (Thanks to <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Arisotura/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Arisotura">@Arisotura</a>
  once again for pointing out the obvious fix lol)</li>

  <li>Photos are now saved as 24-bit PNGs instead of 15-bit BMPs, as YUV mode is now
  used for higher quality</li>

  <li>Photos are new saved to <code class="notranslate">sd:/DCIM/100DSI00/IMG_####.PNG</code>,
  allowing for multiple images to be taken</li>

  <li>Changed the source to be 100% C, since it was already effectively C but using
  C++ files</li>

  </ul>'
updated: '2022-04-19T06:56:09Z'
version: v1.1.0
version_title: 640×480
---
This is just a simple proof of concept/example to show off the DSi's cameras being used in a homebrew app, and an open-source example for initializing the cameras in C/C++. Currently it can show both cameras and save a picture as to `sd:/DCIM/100DSI00/IMG_####.PNG`.

![Example image](https://github.com/Epicpkmn11/dsi-camera/raw/master/resources/example.png)