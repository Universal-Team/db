---
author: Charles Averill
avatar: https://avatars.githubusercontent.com/u/46544495?v=4
categories:
- app
color: '#bf6b3c'
color_bg: '#804728'
created: '2025-11-17T10:26:49Z'
description: An interpreter and text editor for a subset of the Caml Programming Language
  for the Nintendo 3DS
download_page: https://github.com/CharlesAverill/SuperML/releases
downloads:
  SuperML.3dsx:
    size: 996452
    size_str: 973 KiB
    url: https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML.3dsx
  SuperML.cia:
    size: 1205184
    size_str: 1 MiB
    url: https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML.cia
  SuperML_3DSX_QR.png:
    size: 548
    size_str: 548 Bytes
    url: https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML_3DSX_QR.png
  SuperML_CIA_QR.png:
    size: 549
    size_str: 549 Bytes
    url: https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML_CIA_QR.png
github: CharlesAverill/SuperML
icon: https://raw.githubusercontent.com/CharlesAverill/SuperML/refs/heads/main/resources/icon.png
image: https://raw.githubusercontent.com/CharlesAverill/SuperML/refs/heads/main/resources/banner/banner.png
image_length: 15042
layout: app
license: mit
license_name: MIT License
qr:
  SuperML.cia: https://db.universal-team.net/assets/images/qr/superml-cia.png
screenshots:
- description: Script code
  url: https://db.universal-team.net/assets/images/screenshots/superml/script-code.png
- description: Script run
  url: https://db.universal-team.net/assets/images/screenshots/superml/script-run.png
- description: Title screen
  url: https://db.universal-team.net/assets/images/screenshots/superml/title-screen.png
source: https://github.com/CharlesAverill/SuperML
stars: 6
systems:
- 3DS
title: SuperML
unique_ids:
- '0x3F9AD'
update_notes: '<h2 dir="auto">SuperML build-46</h2>

  <h3 dir="auto">CIA</h3>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML_CIA_QR.png"><img
  src="https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML_CIA_QR.png"
  alt="CIA QR" style="max-width: 100%;"></a></p>

  <h3 dir="auto">3DSX</h3>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML_3DSX_QR.png"><img
  src="https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML_3DSX_QR.png"
  alt="3DSX QR" style="max-width: 100%;"></a></p>

  <h3 dir="auto">Download</h3>

  <ul dir="auto">

  <li><strong>CIA:</strong>  <a href="https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML.cia">SuperML.cia</a></li>

  <li><strong>3DSX:</strong> <a href="https://github.com/CharlesAverill/SuperML/releases/download/build-46/SuperML.3dsx">SuperML.3dsx</a></li>

  </ul>'
updated: '2025-11-27T08:09:46Z'
version: build-46
version_title: SuperML build b6e761276769df7b85bedc8b439da151e327ea3d
---
An interpreter and text editor for a subset of the [Caml Programming Language](https://en.wikipedia.org/wiki/Caml) for the Nintendo 3DS.

Great thanks to
- [Notepad3DS](https://github.com/MaeveMcT/Notepad3DS) as a jumping-off point for the text editor segment of this project.
- [min-caml](https://esumii.github.io/min-caml/index-e.html) as a minimal Caml implementation I've based mine on

## Progress

### Application Features

### Language Features

- Parser bulit with Flex+Bison
- Hindley-Milner Type Inference (slightly janky)
- Rudimentary builtin functions for input and output

### Application Features

- Text editing
- Development interpreter target for host system
- Load/Save on SD Card