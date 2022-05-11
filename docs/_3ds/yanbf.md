---
author: YANBForwarder
avatar: https://avatars.githubusercontent.com/u/103953989?v=4
categories:
- utility
color: '#e9cdd1'
color_bg: '#807072'
created: '2021-06-16T08:14:55Z'
description: Yet another nds-bootstrap forwarder. Runs from 3DS-mode!
download_page: https://github.com/YANBForwarder/YANBF/releases
downloads:
  YANBF-Linux.zip:
    size: 96765831
    size_str: 92 MiB
    url: https://github.com/YANBForwarder/YANBF/releases/download/v1.6.0/YANBF-Linux.zip
  YANBF-Windows.zip:
    size: 70805542
    size_str: 67 MiB
    url: https://github.com/YANBForwarder/YANBF/releases/download/v1.6.0/YANBF-Windows.zip
  YANBF-macOS.zip:
    size: 88283800
    size_str: 84 MiB
    url: https://github.com/YANBForwarder/YANBF/releases/download/v1.6.0/YANBF-macOS.zip
  bootstrap.cia:
    size: 206080
    size_str: 201 KiB
    url: https://github.com/YANBForwarder/YANBF/releases/download/v1.6.0/bootstrap.cia
github: YANBForwarder/YANBF
icon_index: 197
image: https://avatars.githubusercontent.com/u/103953989?v=4
image_length: 1561
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
qr:
  bootstrap.cia: https://db.universal-team.net/assets/images/qr/bootstrap-cia.png
source: https://github.com/YANBForwarder/YANBF
systems:
- 3DS
title: YANBF
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>SD card dependency has been removed. (CLI only)

  <ul dir="auto">

  <li>Fixes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="1167716062" data-permission-text="Title is private" data-url="https://github.com/YANBForwarder/YANBF/issues/10"
  data-hovercard-type="issue" data-hovercard-url="/YANBForwarder/YANBF/issues/10/hovercard"
  href="https://github.com/YANBForwarder/YANBF/issues/10">#10</a></li>

  <li>You can now apply a custom ROM path that is different from the input ROM using
  <code class="notranslate">-p &lt;ROM path&gt;</code>

  <ul dir="auto">

  <li>This path must follow POSIX standards. This may be improved in the future.</li>

  </ul>

  </li>

  </ul>

  </li>

  <li>Unique ID is no longer based on the title''s gamecode.

  <ul dir="auto">

  <li>Fixes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="1217883897" data-permission-text="Title is private" data-url="https://github.com/YANBForwarder/YANBF/issues/20"
  data-hovercard-type="issue" data-hovercard-url="/YANBForwarder/YANBF/issues/20/hovercard"
  href="https://github.com/YANBForwarder/YANBF/issues/20">#20</a></li>

  <li>Unique ID 0xFF400-0xFF7FF is allocated for YANBF.</li>

  <li>A new <code class="notranslate">id.txt</code> file is created and is used as
  a counter for Unique IDs.

  <ul dir="auto">

  <li>Should this file be lost, you may potentially start replacing older forwarders.
  Which isn''t a huge loss, but annoying nonetheless.</li>

  </ul>

  </li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Some reworking of the code. Not visible to the end user, just made the thing
  more maintainable really.</li>

  <li>libscrc has been replaced with a custom CRC16 function

  <ul dir="auto">

  <li>GBATEK swiCRC16 pseudocode provided by nocash. Thanks nocash!</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fix</h3>

  <ul dir="auto">

  <li>The GameTDB access will ping the EN endpoint if the album artwork is not found
  on the correct region.

  <ul dir="auto">

  <li>Apparently this is intended behaviour. Weird but oh well, another ping isn''t
  taxing.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Known issues</h3>

  <ul dir="auto">

  <li>As is standard for YANBF releases, the GUI is always one step behind in functionality.
  So passing a custom ROM path will not work for now.</li>

  <li>DSiWare is not supported, as GameTDB does not provide box art for them (of course
  they don''t, they don''t come in a box.)</li>

  </ul>'
updated: '2022-05-11T01:56:36Z'
version: v1.6.0
version_title: 'v1.6.0: look ma, no SD card'
---
YANBF is a 3DS-mode nds-bootstrap forwarder, allowing for more than 40 forwarder titles as compared to the older forwarder template.