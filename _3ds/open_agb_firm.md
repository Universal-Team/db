---
author: profi200
categories:
- emulator
- firm
color: '#c2e5d8'
created: '2020-04-15T21:49:42Z'
description: open_agb_firm is a bare metal app for running GBA homebrew/games using
  the 3DS builtin GBA hardware.
download_page: https://github.com/profi200/open_agb_firm/releases/tag/alpha_2020-10-26
downloads:
  open_agb_firm_alpha_20201026.7z:
    size: 93876
    url: https://github.com/profi200/open_agb_firm/releases/download/alpha_2020-10-26/open_agb_firm_alpha_20201026.7z
github: profi200/open_agb_firm
image: https://avatars0.githubusercontent.com/u/7831477?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  Download open_agb_firm.firm:
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
  Download open_agb_firm_no_bios.firm:
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
updated: '2020-10-26T00:10:31Z'
version: alpha_2020-10-26
version_title: open_agb_firm alpha build 2020-10-26
wiki: https://github.com/profi200/open_agb_firm/wiki
---
