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
  app-release.txt:
    size: 12
    size_str: 12 Bytes
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v2.0/app-release.txt
  snes9x_3ds.3dsx:
    size: 9848220
    size_str: 9 MiB
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v2.0/snes9x_3ds.3dsx
  snes9x_3ds.cia:
    size: 3855296
    size_str: 3 MiB
    url: https://github.com/matbo87/snes9x_3ds/releases/download/v2.0/snes9x_3ds.cia
github: matbo87/snes9x_3ds
icon: https://raw.githubusercontent.com/matbo87/snes9x_3ds/master/resources/icon.png
image: https://raw.githubusercontent.com/matbo87/snes9x_3ds/master/resources/icon.png
image_length: 3285
layout: app
license: other
license_name: Other
llm_generation: 'yes'
qr:
  snes9x_3ds.cia: https://db.universal-team.net/assets/images/qr/snes9x_3ds-cia.png
screenshots:
- description: Loading a game
  url: https://db.universal-team.net/assets/images/screenshots/snes9x-updated-fork/loading-a-game.png
- description: Menu
  url: https://db.universal-team.net/assets/images/screenshots/snes9x-updated-fork/menu.png
- description: Playing a game
  url: https://db.universal-team.net/assets/images/screenshots/snes9x-updated-fork/playing-a-game.png
source: https://github.com/matbo87/snes9x_3ds
stars: 85
systems:
- 3DS
title: Snes9x (updated fork)
unique_ids:
- '0x3849'
update_notes: '<h3 dir="auto">Features</h3>

  <ul dir="auto">

  <li>Added RetroAchievements support (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5356402731" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/82"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/82/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/82">#82</a>)

  <ul dir="auto">

  <li>Log in from the Emulator tab and browse achievements with badges and progress.</li>

  <li>Softcore only: hardcore mode and leaderboards are not supported. See <a href="https://github.com/matbo87/snes9x_3ds/blob/v2.0/README.md#retroachievements">RetroAchievements</a>.</li>

  </ul>

  </li>

  <li>Added Online Updater (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5801035080" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/90"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/90/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/90">#90</a>)

  <ul dir="auto">

  <li>Updates snes9x_3ds to the latest release. See <a href="https://github.com/matbo87/snes9x_3ds/blob/v2.0/README.md#online-updater">Online
  Updater</a>.</li>

  <li>Downloads thumbnails, backgrounds and cheats from <a href="https://github.com/matbo87/snes9x_3ds-assets/releases/tag/v2.0">snes9x_3ds-assets
  v2.0</a>.</li>

  </ul>

  </li>

  <li>Added Enhanced Resolution setting (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4812504686" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/78"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/78/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/78">#78</a>)

  <ul dir="auto">

  <li>2x Screen uses 800px wide mode to show full horizontal hi-res (all models except
  Old 2DS).</li>

  </ul>

  </li>

  <li>Reworked cheat menu; multi-part cheats can now be enabled with a single toggle</li>

  </ul>

  <h3 dir="auto">Performance</h3>

  <ul dir="auto">

  <li>Optimized SuperFX emulation (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5437912120" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/85"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/85/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/85">#85</a>)

  <ul dir="auto">

  <li>On Old 3DS, Yoshi''s Island runs at full speed in-game most of the time.</li>

  <li>On New 3DS, SuperFX games should now run at full speed.</li>

  </ul>

  </li>

  <li>Smoother gameplay in demanding games thanks to improved frame pacing</li>

  <li>Quick save, SRAM saves and screenshots no longer freeze the game while writing
  to the SD card (<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="6105474318" data-permission-text="Title is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/92"
  data-hovercard-type="pull_request" data-hovercard-url="/matbo87/snes9x_3ds/pull/92/hovercard"
  href="https://github.com/matbo87/snes9x_3ds/pull/92">#92</a>)</li>

  <li>Added per-game option to reduce layer draws on mid-frame palette changes; can
  increase FPS in games like Top Gear, but may cause visual glitches. See <a href="https://github.com/matbo87/snes9x_3ds/blob/v2.0/README.md#a-game-runs-slow-how-can-i-improve-performance">Performance
  tips</a>.</li>

  </ul>

  <h3 dir="auto">Menu &amp; UI</h3>

  <ul dir="auto">

  <li>Overhauled menu and dialogs: Save/Load moved to its own page, settings were
  reordered and relabelled</li>

  <li>Resuming from HOME or sleep returns directly to the game</li>

  </ul>

  <h3 dir="auto">Removed</h3>

  <ul dir="auto">

  <li>Frame Sync setting, no longer needed with the improved frame pacing</li>

  <li>Force SRAM Write and Auto-Save Delay settings; SRAM is now always saved on game
  switch and exit</li>

  <li>Legacy <code class="notranslate">.cht</code> cheat files; use <code class="notranslate">.chx</code>
  instead</li>

  <li>Arial font option</li>

  <li>Separate PNG savestate previews; previews are now stored in the savestate. Re-save
  a slot to get its preview back.</li>

  <li><code class="notranslate">_default.png</code> overrides, replaced by images
  in the <code class="notranslate">defaults/</code> folder; see <a href="https://github.com/matbo87/snes9x_3ds-assets#default-images">Default
  images</a></li>

  </ul>

  <h3 dir="auto">Credits</h3>

  <p dir="auto">Big thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Wyatt-James/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Wyatt-James">@Wyatt-James</a>
  for the SuperFX optimizations and accuracy fixes in <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5437912120" data-permission-text="Title
  is private" data-url="https://github.com/matbo87/snes9x_3ds/issues/85" data-hovercard-type="pull_request"
  data-hovercard-url="/matbo87/snes9x_3ds/pull/85/hovercard" href="https://github.com/matbo87/snes9x_3ds/pull/85">#85</a>.</p>

  <p dir="auto">Frame pacing is inspired by the pacer in <a href="https://github.com/skyfloogle/red-viper">red-viper</a>.</p>

  <p dir="auto">For more information, see <a href="https://github.com/matbo87/snes9x_3ds/blob/v2.0/CHANGELOG.md">Changelog</a>.</p>

  <p dir="auto">Install snes9x_3ds.cia via FBI -&gt; Remote Install -&gt; Scan QR
  Code</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/5bdbd129-974d-457b-b45a-120e211e96a0"><img
  width="180" height="180" alt="v2 0" src="https://github.com/user-attachments/assets/5bdbd129-974d-457b-b45a-120e211e96a0"
  style="max-width: 100%; height: auto; max-height: 180px;; aspect-ratio: 180 / 180;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>'
updated: '2026-11-09T18:51:22Z'
version: v2.0
version_title: v2.0
---
fork of [bubble2k's Snes9x for 3DS](https://github.com/bubble2k16/snes9x_3ds), giving you more options to enjoy your SNES game collection.