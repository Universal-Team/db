---
author: lifehackerhansol
avatar: https://avatars.githubusercontent.com/u/37358975?v=4
categories:
- utility
color: '#a262de'
color_bg: '#5d3880'
created: '2022-01-13T20:14:48Z'
description: A basic nds-bootstrap forwarder generator for DSi SDNAND.
download_page: https://github.com/lifehackerhansol/NDSForwarder-DSi/releases
downloads:
  NDSForwarder.dsi:
    size: 483328
    size_str: 472 KiB
    url: https://github.com/lifehackerhansol/NDSForwarder-DSi/releases/download/v0.2.2/NDSForwarder.dsi
github: lifehackerhansol/NDSForwarder-DSi
icon: https://db.universal-team.net/assets/images/icons/ndsforwarder-dsi.png
icon_index: 203
image: https://db.universal-team.net/assets/images/icons/ndsforwarder-dsi.png
image_length: 2102
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/lifehackerhansol/NDSForwarder-DSi/actions
  downloads:
    build.zip:
      url: https://nightly.link/lifehackerhansol/NDSForwarder-DSi/workflows/nightly/master/build.zip
source: https://github.com/lifehackerhansol/NDSForwarder-DSi
systems:
- DS
title: NDSForwarder-DSi
unistore_exclude: true
update_notes: '<p dir="auto"><strong>Improvements</strong>:</p>

  <ul dir="auto">

  <li>More sanity checks are done.

  <ul dir="auto">

  <li>Header CRC is now checked before install.</li>

  <li>Banner CRC, if the game is not DSi-Enhanced, is now checked before install.

  <ul dir="auto">

  <li>If any of the checks fail, the installation will fail entirely.</li>

  <li>DSi-Enhanced games are checked separately, as this can be fixed by removing
  all DSi icon related data. The rest of them should have no reason to be corrupt,
  and will be checked accordingly.</li>

  </ul>

  </li>

  </ul>

  </li>

  </ul>'
updated: '2022-02-18T23:45:41Z'
version: v0.2.2
version_title: 'v0.2.2: sanity checks'
---
# NDSForwarder for hiyaCFW
A basic nds-bootstrap forwarder generator for DSi SDNAND.

## Usage
- https://wiki.ds-homebrew.com/ds-index/forwarders.html?tab=tab-dsi-sd-card