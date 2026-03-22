---
author: bubble2k16 / matbo87 / willjow / Xeddius-Network
avatar: https://avatars.githubusercontent.com/u/4026393?v=4
categories:
- emulator
color: '#635e5e'
color_bg: '#635e5e'
created: '2019-01-15T09:19:13Z'
description: SNES9x Port for 3DS / 2DS
download_page: https://github.com/matbo87/snes9x_3ds/releases
downloads:
  snes9x_3ds.3dsx:
    size: 2405472
    size_str: 2 MiB
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v1.60/snes9x_3ds.3dsx
  snes9x_3ds.cia:
    size: 2347968
    size_str: 2 MiB
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v1.60/snes9x_3ds.cia
github: matbo87/snes9x_3ds
icon: https://raw.githubusercontent.com/matbo87/snes9x_3ds/master/resources/icon.png
image: https://raw.githubusercontent.com/matbo87/snes9x_3ds/master/resources/icon.png
image_length: 3285
layout: app
license: other
license_name: Other
qr:
  snes9x_3ds.cia: https://db.universal-team.net/assets/images/qr/snes9x_3ds-cia.png
source: https://github.com/matbo87/snes9x_3ds
stars: 49
systems:
- 3DS
title: Snes9x (updated fork)
unique_ids:
- '0x3849'
update_notes: '<h2 dir="auto">Major release with deep rendering and architecture changes.</h2>

  <ul dir="auto">

  <li>Migrated rendering from legacy GPU code to <code class="notranslate">citro3d</code>.</li>

  <li>Fewer draw calls via batched rendering and XOR-based packed render-state diffing.</li>

  <li>SNES-accurate refresh-rate matching: when gameplay starts/resumes, 3DS LCD timing
  is set to the game''s native SNES rate (NTSC ~60.1 Hz / PAL 50 Hz).</li>

  <li>Thumbnail system rewritten: on-demand loading from cache files (faster and more
  reliable).</li>

  <li>Asset pipeline improved: 16-bit RGB565 backgrounds; decode path using a shared
  file scratch buffer and aligned shared stream buffer to reduce heap churn/fragmentation.</li>

  <li>Large code-quality pass and strict warning cleanup across frontend + core.</li>

  </ul>

  <h3 dir="auto">Breaking changes (config/assets)</h3>

  <ul dir="auto">

  <li><code class="notranslate">settings.cfg</code> may not migrate cleanly in all
  cases; if so, defaults will be used.</li>

  <li>Legacy thumbnail image folders can be deleted; only the <code class="notranslate">*.cache</code>
  files are used now (<code class="notranslate">boxart.cache</code>, <code class="notranslate">gameplay.cache</code>,
  <code class="notranslate">title.cache</code>).</li>

  <li>Background paths changed:

  <ul dir="auto">

  <li><code class="notranslate">snes9x_3ds/borders</code> -&gt; <code class="notranslate">snes9x_3ds/backgrounds/game_screen</code></li>

  <li><code class="notranslate">snes9x_3ds/covers</code> -&gt; <code class="notranslate">snes9x_3ds/backgrounds/second_screen</code></li>

  </ul>

  </li>

  <li>See <a href="https://github.com/matbo87/snes9x_3ds-assets?tab=readme-ov-file">snes9x_3ds-assets
  README</a> for full setup details and folder layout.</li>

  </ul>

  <p dir="auto">For more information, see <a href="https://github.com/matbo87/snes9x_3ds/blob/master/CHANGELOG.md">Changelog</a>.</p>

  <p dir="auto"><em>Install snes9x_3ds.cia via FBI -&gt; Remote Install -&gt; Scan
  QR Code</em></p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/1248945e-cf8a-46a6-b17a-a6cdc7f17c73"><img
  width="180" height="180" alt="qr-v1 60" src="https://github.com/user-attachments/assets/1248945e-cf8a-46a6-b17a-a6cdc7f17c73"
  style="max-width: 100%; height: auto; max-height: 180px;"></a>'
updated: '2026-03-22T12:46:51Z'
version: v1.60
version_title: v1.60
---
fork of [bubble2k's Snes9x for 3DS](https://github.com/bubble2k16/snes9x_3ds), giving you more options to enjoy your SNES game collection.