---
author: Lumi
avatar: https://avatars.githubusercontent.com/u/218291951?v=4
categories:
- app
color: '#8a8a8a'
color_bg: '#808080'
created: '2026-05-11T18:14:46Z'
description: A Homestuck (and in the future, other MSPA's) reader for the 3DS
download_page: https://github.com/Animalino5/MSPA-3DS/releases
downloads:
  MSPA-3DS.3dsx:
    size: 255900
    size_str: 249 KiB
    url: https://github.com/Animalino5/MSPA-3DS/releases/download/v0.5.0/MSPA-3DS.3dsx
  build_gui.py:
    size: 46821
    size_str: 45 KiB
    url: https://github.com/Animalino5/MSPA-3DS/releases/download/v0.5.0/build_gui.py
github: Animalino5/MSPA-3DS
icon: https://db.universal-team.net/assets/images/icons/mspa-3ds.png
image: https://db.universal-team.net/assets/images/icons/mspa-3ds.png
image_length: 763
layout: app
llm_generation: unknown
script_message: YOU NEED WIFI FOR THIS TO WORK
source: https://github.com/Animalino5/MSPA-3DS
stars: 2
systems:
- 3DS
title: MSPA-3DS
update_notes: "<p dir=\"auto\"><strong>What works</strong></p>\n<pre class=\"notranslate\"\
  ><code class=\"notranslate\"> Full comic reading -- navigate pages with A/B, scroll\
  \ text with D-pad\n Animated GIFs -- pre-converted to frame sequences, play smoothly\n\
  \ [S] pages -- converted to 6 FPS frame sequences with WAV audio\n Multi-image pages\
  \ -- automatically split into separate navigable pages\n Multiple comics -- Homestuck,\
  \ Jailbreak, and Problem Sleuth supported\n Pack system -- each comic pack is a\
  \ folder on SD, easy to add/remove\n PC bundle builder -- GUI tool downloads, converts,\
  \ and packages everything\n</code></pre>\n<p dir=\"auto\"><strong>Known issues</strong></p>\n\
  <pre class=\"notranslate\"><code class=\"notranslate\"> Audio quirks -- some [S]\
  \ pages may have audio sync or playback issues\n No Bard Quest -- excluded because\
  \ it has branching paths (multiple \"next\" links per page) which the reader doesn't\
  \ support\n No Homestuck Beta -- excluded because it's flash-only with no static\
  \ images\n [S] pages are 6 FPS -- smooth enough for reading, but not full video\
  \ quality\n Large [S] pages use more space -- frame sequences are bigger than video\
  \ files (roughly 300KB/frame at 320x240)\n</code></pre>\n<p dir=\"auto\"><strong>What\
  \ you need</strong></p>\n<pre class=\"notranslate\"><code class=\"notranslate\"\
  > A hacked 3DS with homebrew access (CFW + Luma3DS recommended)\n devkitARM + citro2d/citro3d\
  \ to compile the 3DS app\n Python 3.8+ + ffmpeg to run the bundle builder on your\
  \ PC\n An SD card with enough space (The entire ACT 1 of homestuck is around 1GB)\n\
  </code></pre>\n<p dir=\"auto\"><strong>How to use</strong></p>\n<pre class=\"notranslate\"\
  ><code class=\"notranslate\">Run build_gui.py on your PC\nEnter a comic (e.g. homestuck)\
  \ and page range\nClick Build Bundle\nCopy the output folder to sdmc:/3ds/MSPA-3DS/packs/\
  \ on your SD card\nLaunch MSPA-3DS on your 3DS\nSelect your pack and start reading!\n\
  </code></pre>"
updated: '2026-06-26T17:19:55Z'
version: v0.5.0
version_title: v0.5.0 -- Offline Bundles
---
This is a Homestuck 3DS reader which works by fetching data from a Homestuck Mirror then displaying said data. (YOU NEED WIFI FOR THIS TO WORK)