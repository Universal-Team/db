---
author: SNBeast
avatar: https://avatars.githubusercontent.com/u/21327530?v=4
categories:
- utility
color: '#f79e69'
color_bg: '#805236'
created: '2026-01-19T18:04:47Z'
description: A patch to bypass qtm error 0xf9605002
download_page: https://github.com/SNBeast/qtmStub/releases
downloads:
  0004013000004202.ips:
    size: 23
    size_str: 23 Bytes
    url: https://github.com/SNBeast/qtmStub/releases/download/v1.0.0/0004013000004202.ips
github: SNBeast/qtmStub
icon: https://raw.githubusercontent.com/SNBeast/qtmStub/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/SNBeast/qtmStub/refs/heads/main/icon.png
image_length: 3202
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/SNBeast/qtmStub
stars: 1
systems:
- 3DS
title: qtmStub
update_notes: <p dir="auto">Patch for error 0xf9605002</p>
updated: '2026-01-19T18:06:38Z'
version: v1.0.0
version_title: Initial Release
---
# qtmStub

A patch to bypass qtm error 0xf9605002 for cases where servicing the camera hardware is not feasible.

## Effects

If qtm was broken without this patch applied, it will still be broken with this patch applied, and so Super-Stable 3D will not work. From my case, the 3D projection with this patch applied will behave as if Super-Stable 3D is turned off. Additionally, your cameras are unlikely to work and software which attempts to use them will likely crash or hang.

## Installation

Made for the latest version of qtm, v3072. That comes with a system firmware of at least 11.5.0-38, released July 10<sup>th</sup>, 2017.

If you believe your firmware may be too out of date, you can run System Update in Safe Mode by holding `L + R + Up + A` on boot. Safe Mode does not load qtm, so it can work without this patch.

### Luma3DS v13 or newer

1. Download `0004013000004202.ips` from the latest release.
1. Copy `0004013000004202.ips` into `SD:/luma/sysmodules/`, creating folders as necessary. Ensure that its filename is preserved.
1. Enable the Luma setting `Enable loading external FIRMs and modules`, such as by using the menu accessed by holding Select on boot.

### Older Luma3DS versions

1. Download `0004013000004202.ips` from the latest release.
1. Rename `0004013000004202.ips` to `code.ips`.
1. Copy `code.ips` into `SD:/luma/titles/0004013000004202/`, creating folders as necessary.
1. Enable *both* of the Luma settings `Enable loading external FIRMs and modules` and `Enable game patching`.