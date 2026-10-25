---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
created: '2019-02-03T04:36:16Z'
description: SEGA Genesis/Mega Drive emulator for the Nintendo DS(i)
download_page: https://github.com/DS-Homebrew/PicoDriveTWL/releases
github: DS-Homebrew/PicoDriveTWL
icon: https://raw.githubusercontent.com/DS-Homebrew/PicoDriveTWL/master/genesis-32x32.bmp
image: https://db.universal-team.net/assets/images/images/picodrivetwl.png
image_length: 466
layout: app
llm_generation: 'no'
prerelease:
  download_page: https://github.com/DS-Homebrew/PicoDriveTWL/releases/tag/v2.1.0
  downloads:
    PicoDriveTWL.nds:
      size: 417792
      size_str: 408 KiB
      url: https://github.com/DS-Homebrew/PicoDriveTWL/releases/download/v2.1.0/PicoDriveTWL.nds
  qr:
    PicoDriveTWL.nds: https://db.universal-team.net/assets/images/qr/prerelease/picodrivetwl-nds.png
  update_notes: '<h3 dir="auto">What''s new?</h3>

    <ul dir="auto">

    <li>Ported to BlocksDS (v1.24.0 as of this release)!</li>

    <li>Switched to THUMB code instead of ARM for reduced filesize.</li>

    <li>Reduced filesize even further by updating the Cyclone 68k emulator from v0.084
    to v0.088 (ported from NeoDS).</li>

    <li>Enabled 6-button pad support!

    <ul dir="auto">

    <li><code class="notranslate">L</code> acts as <code class="notranslate">X</code>,
    <code class="notranslate">X</code> acts as <code class="notranslate">Y</code>,
    <code class="notranslate">R</code> acts as <code class="notranslate">Z</code>,
    and <code class="notranslate">SELECT</code> acts as <code class="notranslate">MODE</code>.</li>

    <li>To make room, scale mode changing (<code class="notranslate">L</code> button,
    along with <code class="notranslate">R</code> for changing position) and save
    state support (<code class="notranslate">X</code> button) have been removed, and
    the ROM list now opens by touching the touch screen.</li>

    </ul>

    </li>

    <li>Reverted ROM size limit in DS mode from 2.5MB to 3MB.</li>

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xonn83/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xonn83">@xonn83</a>:
    Converted some code from C to ARM.</li>

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xonn83/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xonn83">@xonn83</a>:
    Other minor improvements.</li>

    <li>Optimized frame drawing to use 8BPP mode instead of 16BPP (ARGB1555) mode,
    along with skipping some scanlines to fit into the DS(i) screen.</li>

    <li>On-screen colors now update when CRAM is written with new values.</li>

    <li>Removed external audio playback.</li>

    <li>Re-added version number display.</li>

    </ul>

    <h3 dir="auto">Bug fixes</h3>

    <ul dir="auto">

    <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xonn83/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xonn83">@xonn83</a>:
    Fixed varying speeds of emulation, and reduced max frameskip to 2.</li>

    <li>Fixed some pixels not displaying properly due to not flushing data cache containing
    the pixels.</li>

    <li>RAM is now allocated for the ROM instead of using hardcoded RAM offsets when
    running in DSi mode.</li>

    </ul>'
  update_notes_md: "### What's new?\n- Ported to BlocksDS (v1.24.0 as of this release)!\n\
    - Switched to THUMB code instead of ARM for reduced filesize.\n- Reduced filesize\
    \ even further by updating the Cyclone 68k emulator from v0.084 to v0.088 (ported\
    \ from NeoDS).\n- Enabled 6-button pad support!\n    - `L` acts as `X`, `X` acts\
    \ as `Y`, `R` acts as `Z`, and `SELECT` acts as `MODE`.\n    - To make room, scale\
    \ mode changing (`L` button, along with `R` for changing position) and save state\
    \ support (`X` button) have been removed, and the ROM list now opens by touching\
    \ the touch screen.\n- Reverted ROM size limit in DS mode from 2.5MB to 3MB.\n\
    - @xonn83: Converted some code from C to ARM.\n- @xonn83: Other minor improvements.\n\
    - Optimized frame drawing to use 8BPP mode instead of 16BPP (ARGB1555) mode, along\
    \ with skipping some scanlines to fit into the DS(i) screen.\n- On-screen colors\
    \ now update when CRAM is written with new values.\n- Removed external audio playback.\n\
    - Re-added version number display.\n\n### Bug fixes\n- @xonn83: Fixed varying\
    \ speeds of emulation, and reduced max frameskip to 2.\n- Fixed some pixels not\
    \ displaying properly due to not flushing data cache containing the pixels.\n\
    - RAM is now allocated for the ROM instead of using hardcoded RAM offsets when\
    \ running in DSi mode."
  updated: '2026-10-11T03:09:51Z'
  version: v2.1.0
  version_title: v2.1.0
source: https://github.com/DS-Homebrew/PicoDriveTWL
stars: 26
systems:
- DS
title: PicoDriveTWL
update_notes: '<h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>Ported to BlocksDS (v1.24.0 as of this release)!</li>

  <li>Switched to THUMB code instead of ARM for reduced filesize.</li>

  <li>Reduced filesize even further by updating the Cyclone 68k emulator from v0.084
  to v0.088 (ported from NeoDS).</li>

  <li>Enabled 6-button pad support!

  <ul dir="auto">

  <li><code class="notranslate">L</code> acts as <code class="notranslate">X</code>,
  <code class="notranslate">X</code> acts as <code class="notranslate">Y</code>, <code
  class="notranslate">R</code> acts as <code class="notranslate">Z</code>, and <code
  class="notranslate">SELECT</code> acts as <code class="notranslate">MODE</code>.</li>

  <li>To make room, scale mode changing (<code class="notranslate">L</code> button,
  along with <code class="notranslate">R</code> for changing position) and save state
  support (<code class="notranslate">X</code> button) have been removed, and the ROM
  list now opens by touching the touch screen.</li>

  </ul>

  </li>

  <li>Reverted ROM size limit in DS mode from 2.5MB to 3MB.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xonn83/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xonn83">@xonn83</a>:
  Converted some code from C to ARM.</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xonn83/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xonn83">@xonn83</a>:
  Other minor improvements.</li>

  <li>Optimized frame drawing to use 8BPP mode instead of 16BPP (ARGB1555) mode, along
  with skipping some scanlines to fit into the DS(i) screen.</li>

  <li>On-screen colors now update when CRAM is written with new values.</li>

  <li>Removed external audio playback.</li>

  <li>Re-added version number display.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/xonn83/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/xonn83">@xonn83</a>:
  Fixed varying speeds of emulation, and reduced max frameskip to 2.</li>

  <li>Fixed some pixels not displaying properly due to not flushing data cache containing
  the pixels.</li>

  <li>RAM is now allocated for the ROM instead of using hardcoded RAM offsets when
  running in DSi mode.</li>

  </ul>'
updated: '2026-10-11T03:09:51Z'
version: v2.1.0
version_title: v2.1.0
---
