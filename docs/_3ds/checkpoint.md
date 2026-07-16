---
author: Bernardo Giordano
avatar: https://avatars.githubusercontent.com/u/17624378?v=4
categories:
- utility
color: '#40576f'
color_bg: '#40576f'
created: '2017-09-06T17:20:55Z'
description: Fast and simple homebrew save manager for 3DS and Switch.
download_page: https://github.com/BernardoGiordano/Checkpoint/releases
downloads:
  Checkpoint.3dsx:
    size: 1559596
    size_str: 1 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v4.0.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 1020864
    size_str: 996 KiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v4.0.0/Checkpoint.cia
github: BernardoGiordano/Checkpoint
icon: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/icon.png
image: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/banner.png
image_length: 5618
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  Checkpoint.cia: https://db.universal-team.net/assets/images/qr/checkpoint-cia.png
source: https://github.com/BernardoGiordano/Checkpoint
stars: 3000
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<p dir="auto">This is genuinely the largest Checkpoint update since
  its original release 9 years ago.</p>

  <p dir="auto">Working on it was fun and rewarding. Enjoy!</p>

  <h3 dir="auto">3DS: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>GBA Virtual Console save backup and restore</strong> (thanks
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/LiquidFenrir/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/LiquidFenrir">@LiquidFenrir</a>)</li>

  <li>Added: <strong>DSiWare save backup and restore</strong> (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/SNBeast/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SNBeast">@SNBeast</a>
  for the feature PoC)</li>

  <li>Added: <strong>complete UI/UX redesign</strong></li>

  <li>Added: <strong>background FTP server</strong>. Access your save backups from
  the PC directly through Checkpoint</li>

  <li>Added: a brand new <strong>Settings section</strong>: it is now possible to
  edit Checkpoint''s config.json file directly from the console with a nice settings
  interface.

  <ul dir="auto">

  <li>Added: <strong>light and dark mode</strong> theming</li>

  <li>Added: a folder browser to navigate the SD card and choose additional save folders
  on device</li>

  <li>Added: quick backup toggle to use the default backup name without any prompt</li>

  <li>Added: confirm restore toggle to avoid being asked for confirmation for save
  restore operations</li>

  </ul>

  </li>

  <li>Added: it is now possible to configure additional save folders for DS titles.</li>

  <li>Added: internazionalization support.

  <ul dir="auto">

  <li>Translations have been done through the use of LLMs. If you''re a native speaker
  and think that text wording and appearance in the UI can be improved, please submit
  a pull request or open an issue on this repository.</li>

  <li>Current language support includes English, Italian, French, German, Portuguese,
  Spanish, Dutch, Japanese and Chinese</li>

  </ul>

  </li>

  <li>Added: backup cancellation by holding B during backup</li>

  <li>Fixed: backup list navigation is now massively more intuitive</li>

  <li>Fixed: async IO makes file operations faster and more efficient by running them
  in a worker thread, separated from the main UI thread</li>

  <li>Fixed: greatly improved cached and uncached title loading times</li>

  <li>Fixed: cached text storage now allows faster rendering for all the text in the
  interface</li>

  <li>Fixed: the project''s code architecture has been greatly improved.

  <ul dir="auto">

  <li>The codebase is now 9 years old and has never seen an architecture overhaul
  like this before.</li>

  <li>Dozens of performance, security and safety bugfixes have been pushed to the
  project, making the app more secure and efficient.</li>

  </ul>

  </li>

  <li>Fixed: an issue where swapping DS carts would crash Checkpoint because of a
  stack-smashing bug</li>

  <li>Removed: <strong>cheats feature</strong>.

  <ul dir="auto">

  <li>The cheat database required constant updates to stay in sync with game updates,
  and its maintenance wasn''t sustainable.</li>

  </ul>

  </li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">Switch: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>complete UI/UX redesign</strong></li>

  <li>Added: internazionalization support.

  <ul dir="auto">

  <li>Translations have been done through the use of LLMs. If you''re a native speaker
  and think that text wording and appearance in the UI can be improved, please submit
  a pull request or open an issue on this repository.</li>

  <li>Current language support includes English, Italian, French, German, Portuguese,
  Spanish, Dutch, Japanese and Chinese</li>

  </ul>

  </li>

  <li>Added: a brand new <strong>Settings section</strong>: it is now possible to
  edit Checkpoint''s config.json file directly from the console with a nice settings
  interface.

  <ul dir="auto">

  <li>Added: <strong>light and dark mode</strong> theming</li>

  <li>Added: a folder browser to navigate the SD card and choose additional save folders
  on device</li>

  <li>Added: quick backup toggle to use the default backup name without any prompt</li>

  <li>Added: confirm restore toggle to avoid being asked for confirmation for save
  restore operations</li>

  <li>Added: file-by-file verification after restore</li>

  </ul>

  </li>

  <li>Added: <strong>complete graphics backend migration from SDL2 to deko3d</strong>

  <ul dir="auto">

  <li>Among all the benefits that the rewrite brought to the software, the application
  size is now <strong>~70% smaller</strong></li>

  </ul>

  </li>

  <li>Added: <strong>HTTP log server on port 8000</strong> — view logs in real-time
  from any browser on your network.

  <ul dir="auto">

  <li>Logs can now be accessed from the application directly via Settings &gt; Connectivity
  &gt; Logs.</li>

  </ul>

  </li>

  <li>Added: 1080p docked mode support (alongside 720p handheld).</li>

  <li>Fixed: async IO makes file operations faster and more efficient by running them
  in a worker thread, separated from the main UI thread</li>

  <li>Fixed: backup list navigation is now massively more intuitive</li>

  <li>Added: large save restore with journal pre-extend and mid-file commits,<br>

  preventing out-of-space failures (fixes <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4780027894" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/541"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/541/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/541">#541</a>).</li>

  <li>Fixed: avoid restoring files after a corruption error occurred during copy.</li>

  <li>Fixed: the project''s code architecture has been greatly improved.

  <ul dir="auto">

  <li>The codebase is now 9 years old and has never seen an architecture overhaul
  like this before.</li>

  <li>Dozens of performance, security and safety bugfixes have been pushed to the
  project, making the app more secure and efficient.</li>

  </ul>

  </li>

  <li>Removed: <strong>pksmbridge save transfer feature</strong></li>

  <li>Removed: <strong>cheats feature</strong>.

  <ul dir="auto">

  <li>The cheat database required constant updates to stay in sync with game updates,
  and its maintenance wasn''t sustainable.</li>

  </ul>

  </li>

  <li>Removed: the HTML settings page accessible through local network, and all its
  dependencies</li>

  <li>Removed: unneeded dependencies like the SDL2 suite and libpng.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">chlink: a new companion app</h3>

  <ul dir="auto">

  <li>Added: <strong>chlink</strong>, a companion command line app for your PC that
  works together with Checkpoint''s wireless save transfer feature.

  <ul dir="auto">

  <li>Send save backups from your PC to the console, or receive them from the console
  to your PC, over your local network.</li>

  <li>Transfers are protected by a 4-digit PIN displayed on the console.</li>

  <li>chlink automatically recognizes backups stored in a Checkpoint SD card layout,
  so title and backup information are inferred for you.</li>

  <li>It ships as a single, dependency-free executable for Windows, macOS and Linux,
  attached to this release.</li>

  </ul>

  </li>

  </ul>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/b261080b-ef0d-4a2f-a711-207a4554d311"><img
  width="181" height="183" alt="qr" src="https://github.com/user-attachments/assets/b261080b-ef0d-4a2f-a711-207a4554d311"
  style="max-width: 100%; height: auto; max-height: 183px;; aspect-ratio: 181 / 183;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-07-11T14:15:55Z'
version: v4.0.0
version_title: Checkpoint 4.0.0
---
