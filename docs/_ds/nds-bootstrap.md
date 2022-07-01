---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 431831
    size_str: 421 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.60.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1039670
    size_str: 1015 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.60.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 139
image: https://i.imgur.com/BFIu7xX.png
image_length: 5116
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v24.11.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v24.11.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>7MB SDK5 ROMs are now pre-loaded into RAM on DSi consoles.</li>

  <li>DSi mode heap size is now shrunk further for <em>Power Pro Kun Pocket 12 &amp;
  13</em> AP-fixes to work on DSi consoles.</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Overlays are now only loaded into RAM if AP-fix .ips file contains overlay patching.

  <ul dir="auto">

  <li>This avoids having to shrink the DSi mode heap size further than needed, if
  no patches are to be applied to the overlays.</li>

  </ul>

  </li>

  <li>Improved MPU patching code to be slightly faster, along with adding a new patch
  method for SDK5 titles.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>DSi mode heap size is now only shrunk by 256KB on 3DS consoles.

  <ul dir="auto">

  <li>This fixes <em>Hidden Photo</em> (EUR) crashing during loading after selecting
  a photo.</li>

  </ul>

  </li>

  <li>Fixed <em>Power Pro Kun Pocket 12</em> not booting in DSi mode.</li>

  <li>Fixed <em>Rabbids Go Home</em> not booting in DSi mode on 3DS consoles.</li>

  <li>SDK5.4 &amp; 5.5 games now properly soft-reset without rebooting the console.

  <ul dir="auto">

  <li>As a result, <em>SD Gundam Sangoku Den - Brave Battle Warriors - Shin Militia
  Taisen</em> now boots!</li>

  </ul>

  </li>

  <li>Fixed card read DMA auto-disable not working in SDK1-4 games when using wireless
  features.</li>

  </ul>'
updated: '2022-07-01T21:24:06Z'
version: v0.60.0
version_title: 'v0.60.0: TWL Summer Release #3'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.