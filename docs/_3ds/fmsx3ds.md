---
author: h.tomioka
avatar: https://avatars.githubusercontent.com/u/168841671?v=4
categories:
- emulator
color: '#2a3f9c'
color_bg: '#223380'
created: '2024-05-10T09:04:13Z'
description: fMSX(MSX emulator) port to 3DS. Add many new feature such as MSXTurboR
  emulation and MSX0 emulation.
download_page: https://github.com/TomiokaH01/fMSX3DS/releases
downloads:
  fMSX3DS-1.40.zip:
    size: 3172200
    size_str: 3 MiB
    url: https://github.com/TomiokaH01/fMSX3DS/releases/download/v1.40/fMSX3DS-1.40.zip
  fMSX3DS-1.40Source.zip:
    size: 1202531
    size_str: 1 MiB
    url: https://github.com/TomiokaH01/fMSX3DS/releases/download/v1.40/fMSX3DS-1.40Source.zip
github: TomiokaH01/fMSX3DS
icon: https://raw.githubusercontent.com/TomiokaH01/fMSX3DS/main/icon.png
image: https://private-user-images.githubusercontent.com/168841671/331778903-f7ffcd0d-c1e9-4db4-a4ee-03b29ebc79b5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM0MTcyNDAsIm5iZiI6MTcyMzQxNjk0MCwicGF0aCI6Ii8xNjg4NDE2NzEvMzMxNzc4OTAzLWY3ZmZjZDBkLWMxZTktNGRiNC1hNGVlLTAzYjI5ZWJjNzliNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxMVQyMjU1NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZjA3MjE1NGNhZTM1NmNjODQyOWI0NTU3ZGZmZjM4YzdiNzQyYzVlYTFjYjYwYzJjMzllZmIxZjIwZDlmN2M0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.hTvWFkt8-Lo3mxlhW7mNxgO6H6uXSIf_B7dfbUojzEc
layout: app
license: other
license_name: Other
source: https://github.com/TomiokaH01/fMSX3DS
stars: 6
systems:
- 3DS
title: fMSX3DS
unique_ids:
- '0x736E4'
update_notes: '<p dir="auto">v1.4<br>

  -Add support for V9990 and its clones(GFX9000 etc).<br>

  You can use it with chose "[Option]" item in the fMSX3DS system menu, and enable
  the "Use V9990" option item.<br>

  Good news for New3DS user. I tested almost all of homebrew games/apps that use V9990
  and all of them works full speed at 60fps on New3DS.<br>

  As to Old3DS, it has mixed results depends on homebrew. Some homebrew runs full
  speed even on Old3DS, but some homebrew runs too slow.</p>

  <p dir="auto">-Fixed konami SCC sound issue with miss detect of SCC and SCC+ in
  some cae<br>

  (Project Melancholia English translation patched SD Snatcher, TINY SLOT CHECKER
  etc.).</p>

  <p dir="auto">-Add new option item "Read SCC Plus Wave". Some games/apps requires
  this option item on to enable SCC sound.<br>

  (GEM(GameBoy emulator for MSXTurboR + V9990) etc).</p>

  <p dir="auto">-Update "emu8950.c" by Mitsutaka Okazaki to latest version.</p>

  <p dir="auto">-Add support fr new firmware(0.07.08) for MSX0.</p>

  <p dir="auto">-Add support for ASCII16 ROM Mapper with 4MB size(9Finger Demo by
  NOP, MSX in a Row!, MSX-Wings etc).</p>

  <p dir="auto">-Adjust posions of "No Scale" and "Keep Aspect" screen strech Mode.</p>

  <p dir="auto">-Fixed bug that you cann''t assign ":" key to 3DS''s button in keyconfig.</p>

  <p dir="auto">-Add ability to change RAM size of MSX.<br>

  You can do that with choosing "[Option]" item in the fMSX3DS system menu, and change
  value of "/RAM Size".<br>

  Caution that you must use same RAM size when you load saved state.</p>

  <p dir="auto">-Add ability to overclock R800 CPU for MSXTurboR.<br>

  You can use it with choosing "[OverClockR800(Unsafe)]" item in the fMSX3DS system
  menu, and select overclock rate.<br>

  Caution that it''s unsafe, and many games go wrong with overclock.</p>

  <p dir="auto">-Add suggestion message to restart when you change printer port.</p>'
updated: '2024-08-13T11:42:19Z'
version: v1.40
version_title: v1.40
website: https://gbatemp.net/threads/release-fmsx3ds-msx-msx2-msx2-emulator-with-new-feature-for-3ds.637072/
---
fMSX(MSX emulator) port to 3DS. Add new feature such as MSXTurboR emulation and MSX0 emulation.
Also, it add various improvements based on recently analize of MSX hardware
include analize in Japan that is unknown in world wide.