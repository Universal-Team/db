---
author: Cavv
avatar: https://avatars.githubusercontent.com/u/65863280?v=4
categories:
- utility
color: '#4a4a85'
color_bg: '#474780'
created: '2025-03-13T02:12:55Z'
description: Easy-to-use content downloader for Nintendo DS(i) consoles
download_page: https://github.com/cavv-dev/Kekatsu-DS/releases
downloads:
  Kekatsu.nds:
    size: 1884160
    size_str: 1 MiB
    url: https://github.com/cavv-dev/Kekatsu-DS/releases/download/v1.2.0/Kekatsu.nds
  version.txt:
    size: 6
    size_str: 6 Bytes
    url: https://github.com/cavv-dev/Kekatsu-DS/releases/download/v1.2.0/version.txt
github: cavv-dev/Kekatsu-DS
icon: https://github.com/cavv-dev/Kekatsu-DS/raw/main/icon.png
image: https://github.com/cavv-dev/Kekatsu-DS/raw/main/icon.png
image_length: 265
layout: app
license: mit
license_name: MIT License
qr:
  Kekatsu.nds: https://db.universal-team.net/assets/images/qr/kekatsu-nds.png
screenshots:
- description: Kekatsu ds 1
  url: https://db.universal-team.net/assets/images/screenshots/kekatsu/kekatsu-ds-1.png
- description: Kekatsu ds 2
  url: https://db.universal-team.net/assets/images/screenshots/kekatsu/kekatsu-ds-2.png
- description: Kekatsu ds 3
  url: https://db.universal-team.net/assets/images/screenshots/kekatsu/kekatsu-ds-3.png
source: https://github.com/cavv-dev/Kekatsu-DS
stars: 39
systems:
- DS
title: Kekatsu
update_notes: '<h2 dir="auto">Changes</h2>

  <ul dir="auto">

  <li>The main SDK is now BlocksDS. Support for DevkitPro has been removed. Check
  the new instructions for building</li>

  <li>Added pagination for database list section, removing the limit of 8 databases</li>

  <li>Temporarily removed speed information from download screen since it was mostly
  inaccurate</li>

  <li>The file name <code class="notranslate">databases.txt.txt</code> is checked
  too other than <code class="notranslate">databases.txt</code> for loading the database
  list.<br>

  This has been done to handle the frequent mistake of creating a new text file as
  <code class="notranslate">databases.txt</code> and having it saved as <code class="notranslate">databases.txt.txt</code>
  by the OS</li>

  </ul>

  <p dir="auto"><strong>Full changelog</strong>: <a class="commit-link" href="https://github.com/cavv-dev/Kekatsu-DS/compare/v1.1.0...v1.2.0"><tt>v1.1.0...v1.2.0</tt></a></p>'
updated: '2025-10-19T19:10:55Z'
version: v1.2.0
version_title: v1.2.0
---
*Kekatsu* is a straightforward content downloader for DS and DSi consoles.
The main feature of this app is the use of content databases to download apps and games on the fly for any platform.
### Key features
- Standalone
- Multi-platform content
- Custom databases
- Color scheme customization
- Localization support

An already available database to use with Kekatsu is [UDB-Kekatsu-DS](https://github.com/cavv-dev/UDB-Kekatsu-DS), which is an updated selection of DS and DSi apps from [Universal-DB](https://db.universal-team.net/).
Check out the [Databases setup](https://github.com/cavv-dev/Kekatsu-DS?tab=readme-ov-file#databases-setup) section for info on how to set it up.