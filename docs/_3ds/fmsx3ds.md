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
  fMSX3DS-1.42.zip:
    size: 3593840
    size_str: 3 MiB
    url: https://github.com/TomiokaH01/fMSX3DS/releases/download/v1.42/fMSX3DS-1.42.zip
  fMSX3DS-1.42Source.zip:
    size: 1330812
    size_str: 1 MiB
    url: https://github.com/TomiokaH01/fMSX3DS/releases/download/v1.42/fMSX3DS-1.42Source.zip
github: TomiokaH01/fMSX3DS
icon: https://raw.githubusercontent.com/TomiokaH01/fMSX3DS/main/icon.png
image: https://private-user-images.githubusercontent.com/168841671/331778903-f7ffcd0d-c1e9-4db4-a4ee-03b29ebc79b5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjM0MTcyNDAsIm5iZiI6MTcyMzQxNjk0MCwicGF0aCI6Ii8xNjg4NDE2NzEvMzMxNzc4OTAzLWY3ZmZjZDBkLWMxZTktNGRiNC1hNGVlLTAzYjI5ZWJjNzliNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgxMVQyMjU1NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ZjA3MjE1NGNhZTM1NmNjODQyOWI0NTU3ZGZmZjM4YzdiNzQyYzVlYTFjYjYwYzJjMzllZmIxZjIwZDlmN2M0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.hTvWFkt8-Lo3mxlhW7mNxgO6H6uXSIf_B7dfbUojzEc
layout: app
license: other
license_name: Other
source: https://github.com/TomiokaH01/fMSX3DS
stars: 12
systems:
- 3DS
title: fMSX3DS
unique_ids:
- '0x736E4'
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/30c514e3-7b1a-4a90-bc21-ff8f90a0018f"><img
  src="https://github.com/user-attachments/assets/30c514e3-7b1a-4a90-bc21-ff8f90a0018f"
  alt="ranma006" style="max-width: 100%;"></a><br>

  v1.42<br>

  -Add support for Hard Disk drive. It uses NEXTOR driver. Thanks for Konamiman, the
  auther of NEXTOR,<br>

  With that, you can use the hardDisk image with simply opening ".DSK" disk image
  files.<br>

  To manage HDD image, use DiskExplorer.<br>

  <a href="https://hp.vector.co.jp/authors/VA013937/editdisk/index_e.html" rel="nofollow">https://hp.vector.co.jp/authors/VA013937/editdisk/index_e.html</a></p>

  <p dir="auto">-Added debugger with dual screen of 3DS.<br>

  You can use it with choosing "/[Start Debugger]" item in the fMSX3DS system menu.<br>

  Then press A button to step over, B button to debugger menu.</p>

  <p dir="auto">-Fied bug that SCC sounds missing in MANBOW2.</p>

  <p dir="auto">-Fixed bug that fMSX3DS makes a undeletable(with Windows) file in
  "/FMSX3DS/SAVEDISK" folder in some case when you use ".gz" compressed disk files.<br>

  Sorry, if you troubled with this. If so, you can delete that file with FBI.<br>

  <a href="https://github.com/Steveice10/FBI">https://github.com/Steveice10/FBI</a></p>

  <p dir="auto">-Add support for 4MB RAM mapper(unsafe). But, it''s unsafe to use
  that, because same as real MSX machine with 4MB RAM, some games and applications
  do''nt work.</p>

  <p dir="auto">-Fixed bug that MSX0''s "IOTGET" command with "host/heap" node shows
  invalid values.</p>

  <p dir="auto">-Fixed bug that some disks with special header does''nt work(MSX-Fun
  Info-Disk etc).</p>

  <p dir="auto">-Add support for special disks with 81 Tracks.(Dummieland etc).</p>

  <p dir="auto">-Add support for new MEGAROM mapper for HolyQuran by Al Alamiah.</p>

  <p dir="auto">-Add support for The Curse Of Lies(MSXdev 2024).</p>

  <p dir="auto">-Small GUI improve.</p>

  <p dir="auto">-Small speed up with latest version of devkitpro.</p>

  <p dir="auto">-Fix Compile Error with latest version of devkitpro.</p>'
updated: '2024-12-19T14:22:28Z'
version: v1.42
version_title: v1.42
website: https://gbatemp.net/threads/release-fmsx3ds-msx-msx2-msx2-emulator-with-new-feature-for-3ds.637072/
---
fMSX(MSX emulator) port to 3DS. Add new feature such as MSXTurboR emulation and MSX0 emulation.
Also, it add various improvements based on recently analize of MSX hardware
include analize in Japan that is unknown in world wide.