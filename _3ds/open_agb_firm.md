---
author: profi200
categories:
- emulator
created: '2020-04-15T21:49:42Z'
description: open_agb_firm is a bare metal app for running GBA homebrew/games using
  the 3DS builtin GBA hardware.
download_page: https://github.com/profi200/open_agb_firm/releases/tag/alpha_2020-09-08
downloads:
  open_agb_firm_alpha_20200908.7z: https://github.com/profi200/open_agb_firm/releases/download/alpha_2020-09-08/open_agb_firm_alpha_20200908.7z
github: profi200/open_agb_firm
image: https://avatars0.githubusercontent.com/u/7831477?v=4
layout: app
scripts:
  Release:
  - file: open_agb_firm.*.7z
    message: Downloading open_agb_firm 7z...
    output: /open_agb_firm.7z
    repo: profi200/open_agb_firm
    type: downloadRelease
  - file: /open_agb_firm.7z
    input: open_agb_firm.firm
    message: Extracting open_agb_firm.firm...
    output: /luma/payloads/open_agb_firm.firm
    type: extractFile
  - file: /open_agb_firm.7z
    message: Deleting open_agb_firm.7z...
    type: deleteFile
  Release (no BIOS intro):
  - file: open_agb_firm.*.7z
    message: Downloading open_agb_firm 7z...
    output: /open_agb_firm.7z
    repo: profi200/open_agb_firm
    type: downloadRelease
  - file: /open_agb_firm.7z
    input: open_agb_firm_no_bios.firm
    message: Extracting open_agb_firm_no_bios.firm...
    output: /luma/payloads/open_agb_firm_no_bios.firm
    type: extractFile
  - file: /open_agb_firm.7z
    message: Deleting open_agb_firm.7z...
    type: deleteFile
source: https://github.com/profi200/open_agb_firm
systems:
- 3DS
title: open_agb_firm
updated: '2020-09-08T14:51:24Z'
version: alpha_2020-09-08
version_title: open_agb_firm alpha build 2020-09-08
wiki: https://github.com/profi200/open_agb_firm/wiki
---
