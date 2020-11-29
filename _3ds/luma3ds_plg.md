---
author: jbmagination
categories:
- utility
- firm
- luma3ds
color: '#877346'
created: '2020-04-21T05:08:56Z'
description: Noob-proof (N)3DS "Custom Firmware" [plugin loader]
download_page: https://github.com/jbmagination/Luma3DS_plg/releases/tag/10.1.3
downloads:
  boot.firm:
    size: 236544
    url: https://github.com/jbmagination/Luma3DS_plg/releases/download/10.1.3/boot.firm
github: jbmagination/Luma3DS_plg
image: https://avatars3.githubusercontent.com/u/26027089?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  boot.firm:
  - count: 1
    message: 'Warning: This version of Luma3DS is not

      compatible with system version 11.14.0-46 or newer,

      please only use on older system versions'
    type: promptMessage
  - file: boot.firm
    message: Downloading boot.firm...
    output: /boot.firm
    repo: jbmagination/Luma3DS_plg
    type: downloadRelease
source: https://github.com/jbmagination/Luma3DS_plg
systems:
- 3DS
title: Luma3DS_plg
update_notes: <p><strong>This is for use with Universal Updater.</strong> If you are
  currently using Universal Updater, you can continue. Otherwise, <em><a href="https://github.com/jbmagination/Luma3DS">please
  use my other fork.</a></em> It has much more features.</p>
updated: '2020-06-03T20:32:38Z'
version: 10.1.3
version_title: For use with Universal Updater.
wiki: https://github.com/jbmagination/Luma3DS_plg/wiki
---
