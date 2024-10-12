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
  fMSX3DS-1.41.zip:
    size: 3188066
    size_str: 3 MiB
    url: https://github.com/TomiokaH01/fMSX3DS/releases/download/v1.41/fMSX3DS-1.41.zip
  fMSX3DS-1.41Source.zip:
    size: 1212403
    size_str: 1 MiB
    url: https://github.com/TomiokaH01/fMSX3DS/releases/download/v1.41/fMSX3DS-1.41Source.zip
github: TomiokaH01/fMSX3DS
icon: https://raw.githubusercontent.com/TomiokaH01/fMSX3DS/main/icon.png
image: https://private-user-images.githubusercontent.com/168841671/331778903-f7ffcd0d-c1e9-4db4-a4ee-03b29ebc79b5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM0MTcyNDAsIm5iZiI6MTcyMzQxNjk0MCwicGF0aCI6Ii8xNjg4NDE2NzEvMzMxNzc4OTAzLWY3ZmZjZDBkLWMxZTktNGRiNC1hNGVlLTAzYjI5ZWJjNzliNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxMVQyMjU1NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZjA3MjE1NGNhZTM1NmNjODQyOWI0NTU3ZGZmZjM4YzdiNzQyYzVlYTFjYjYwYzJjMzllZmIxZjIwZDlmN2M0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.hTvWFkt8-Lo3mxlhW7mNxgO6H6uXSIf_B7dfbUojzEc
layout: app
license: other
license_name: Other
source: https://github.com/TomiokaH01/fMSX3DS
stars: 8
systems:
- 3DS
title: fMSX3DS
unique_ids:
- '0x736E4'
update_notes: '<p dir="auto">-Add support for Dual Screen for V9990!(Codename INTRUDER,
  2 Screen Demo by N.I etc).<br>

  To use this, select "[V9990 Dual Screen]" item in the fMSX3DS system menu, and select
  "On".</p>

  <p dir="auto">-Update "emu2149.c" by Mitsutaka Okazaki to latest version(v1.42).</p>

  <p dir="auto">-Add support for LED light analog output for MSX0.<br>

  To use this, Choose "[Option]" item in the fMSX3DS system menu, and change option
  item "/Use MSX0" to "On",<br>

  and "/MSX Analog Output" to "LED(3DS PowerLED)".<br>

  Caution! it use Nintendo3DS''s real LED. Your 3DS is not breakdown while LED blinking.</p>

  <p dir="auto">-Add support for overlay for reference image.<br>

  It''s usefull for MSX graphic apps such as Graph Saurus etc. and MSX sprite editor
  app such as S.S.T etc.<br>

  To use this,  Choose "<a href="Overlay">Load Reference Image</a>" item in the fMSX3DS
  system menu, and select reference image file.<br>

  And choose "[Adjust Reference Image]" item in the fMSX3DS system menu to enter adjust
  reference image menu.<br>

  In this menu, you can change reference image''s position, size, and transparent
  rate with Nintendo3DS''s keys.<br>

  PAD:adjust position  LR key:change size of reference image  XY key:change transparent
  rate</p>

  <p dir="auto">-Fixed bug that some disk games does''nt work on MSXTurboR(Breaker(JAST)
  etc).</p>

  <p dir="auto">-Add support for TC8566AF FDC emulation for MSXTurboR.<br>

  With this more games/apps become works correct(ksaver.com etc).</p>

  <p dir="auto">-Fix bug that boot with ctrl key does''nt work on MSXTurboR(Many KOEI
  game of disk version(Ishin no Arashi , Sangokushi, Sangokushi2 etc) etc).</p>

  <p dir="auto">-Improve emulation of MSXTurboR Pause. (Networkers Gift Disk etc).</p>

  <p dir="auto">-Fix graphic glitches of Screen mode 10 (Intro of Shin kugyoku den
  etc).</p>

  <p dir="auto">-Fixed bug that fMSX3DS get''s error when you power off Nintendo 3DS
  while displaying "[Frequently Used Folder]" system menu.</p>

  <p dir="auto">-Add support for ".der" copy protected disk files made by Disk-Manager.<br>

  <a href="http://www.lexlechz.at/en/software/DiskMgr.html" rel="nofollow">http://www.lexlechz.at/en/software/DiskMgr.html</a></p>

  <p dir="auto">-Add support for ESE-RAM.<br>

  <a href="https://www.msx.org/wiki/ESE-RAM" rel="nofollow">https://www.msx.org/wiki/ESE-RAM</a><br>

  <a href="http://www.hat.hi-ho.ne.jp/tujikawa/ese/eseram.html" rel="nofollow">http://www.hat.hi-ho.ne.jp/tujikawa/ese/eseram.html</a><br>

  you can use it with selecting menu item "[Load Ese RAM 512k ROM]" in the fMSX3DS''s
  system menu.</p>'
updated: '2024-10-11T12:35:55Z'
version: v1.41
website: https://gbatemp.net/threads/release-fmsx3ds-msx-msx2-msx2-emulator-with-new-feature-for-3ds.637072/
---
fMSX(MSX emulator) port to 3DS. Add new feature such as MSXTurboR emulation and MSX0 emulation.
Also, it add various improvements based on recently analize of MSX hardware
include analize in Japan that is unknown in world wide.