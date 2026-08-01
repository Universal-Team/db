---
author: Bernardo Giordano
avatar: https://avatars.githubusercontent.com/u/17624378?v=4
categories:
- utility
color: '#40576f'
color_bg: '#40576f'
created: '2017-09-06T17:20:55Z'
description: Fast and simple homebrew save management framework for 3DS and Switch.
download_page: https://github.com/BernardoGiordano/Checkpoint/releases
downloads:
  Checkpoint.3dsx:
    size: 3312036
    size_str: 3 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.0.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 2368448
    size_str: 2 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.0.0/Checkpoint.cia
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
stars: 3018
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<p dir="auto">Checkpoint 4.0.0 was the largest update the app ever
  had. Version 5.0.0 redefines what the app <em><strong>is</strong></em>.</p>

  <p dir="auto">Checkpoint is now a save management <strong>framework</strong>: everything
  it can do to a save is also reachable from scripts you write yourself and drop on
  the SD card, so your console can do things no release of Checkpoint ever shipped
  with. The cheat manager is back as one of those scripts, and so is cloud save sync,
  to Google Drive, or to any WebDAV server you already run.</p>

  <p dir="auto">Enjoy!</p>

  <h3 dir="auto">Scripting: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>a scripting engine</strong>. Checkpoint runs C scripts, interpreted
  on the console. A script is a single <code class="notranslate">.c</code> file on
  the SD card: no compiler, no rebuild, no reflash.

  <ul dir="auto">

  <li>Scripts live in <code class="notranslate">sdmc:/&lt;3ds|switch&gt;/Checkpoint/scripts/universal</code>
  to be offered for every title, or in <code class="notranslate">scripts/&lt;title
  id&gt;</code> to be offered for that title only.</li>

  <li>Added: a new <strong>Scripts menu</strong>, reachable with <strong>SELECT</strong>
  on 3DS and <strong>Minus</strong> on Switch.</li>

  <li>Scripts get a native API through <code class="notranslate">#include &lt;checkpoint.h&gt;</code>,
  reaching the same functions the app itself uses: the title catalog, save archives
  (3DS extdata and shared extdata included) to read, write, delete, list and commit
  files into, SD card I/O, zip pack and unpack, HTTP requests and streamed file uploads,
  JSON parsing, and UI dialogs rendered by Checkpoint itself.</li>

  <li>Added: <strong>a console UI for scripts</strong>. A running script owns the
  screen: its output streams into a scrollable log pane, while its messages, confirmations,
  pickers, keyboards and nested progress bars take the other screen on 3DS, or a card
  over the transcript on Switch.</li>

  <li>Added: <strong>script cancellation</strong>. Holding <strong>B</strong> aborts
  any script, even one stuck in an infinite loop, without rebooting the console.</li>

  <li>Added: <strong>a sealing API</strong>, to let scripts store secrets like tokens
  and passwords on the SD card encrypted with a console-bound key, and optionally
  with a passphrase of your choice.</li>

  <li>Scripts also get picoc''s C standard library: <code class="notranslate">stdio</code>,
  <code class="notranslate">stdlib</code>, <code class="notranslate">string</code>,
  <code class="notranslate">unistd</code>, <code class="notranslate">ctype</code>,
  <code class="notranslate">math</code> and <code class="notranslate">time</code>.</li>

  </ul>

  </li>

  <li>Added: <strong>full scripting documentation</strong>, in <a href="https://github.com/FlagBrew/Checkpoint/blob/master/scripts/README.md"><code
  class="notranslate">scripts/README.md</code></a>: the API reference, the interpreter''s
  limits, recipes, and a checklist for both human and AI script authors.

  <ul dir="auto">

  <li><a href="https://github.com/FlagBrew/Checkpoint/blob/master/scripts/examples/example.c"><code
  class="notranslate">scripts/examples/example.c</code></a> is a runnable guided tour
  of the API, one menu entry per area.</li>

  <li><code class="notranslate">tools/scriptlint.sh</code> parse-checks your scripts
  on your PC, before you copy them onto the SD card.</li>

  </ul>

  </li>

  <li>Fixed: exceptions thrown while a script runs are caught and reported to you,
  instead of terminating the app non-deterministically.</li>

  </ul>

  <h3 dir="auto">Bundled scripts</h3>

  <ul dir="auto">

  <li>Added: <strong>sharkive</strong>, and with it the <strong>cheat manager is back</strong>.

  <ul dir="auto">

  <li>It downloads the latest <a href="https://github.com/FlagBrew/Sharkive">Sharkive</a>
  database, lets you pick cheats per title, and writes the cheat files Luma3DS (3DS)
  and Atmosphere (Switch) expect.</li>

  <li>Because it is a script now, the cheat database follows Sharkive instead of waiting
  for a Checkpoint release. This solves one of the maintenance problems that made
  the feature go away in 4.0.0.</li>

  <li>Note: if you''re not satisfied with the cheats distributed in Sharkive, you
  can submit issues and patches to the repo itself, or contribute by writing a script
  that downloads cheats from another provider. Checkpoint is really open to contributions.</li>

  </ul>

  </li>

  <li>Added: <strong>googledrive</strong>, to sync your save backups to your own Google
  Drive.

  <ul dir="auto">

  <li>Sign-in happens through Google''s device flow: the console shows a code, you
  type it on your phone or PC.</li>

  <li>Sync everything, a single title, or a single backup. Each backup is uploaded
  as a zip, and already uploaded backups are skipped.</li>

  <li>Your credentials are sealed with the new encryption API, so they never sit on
  the SD card in the clear. Setup instructions are in <a href="https://github.com/FlagBrew/Checkpoint/blob/master/scripts/googledrive.md"><code
  class="notranslate">scripts/googledrive.md</code></a>.</li>

  </ul>

  </li>

  <li>Added: <strong>webdav</strong>, to sync those same backups to any WebDAV server
  you already run: Nextcloud, ownCloud, Synology, Apache <code class="notranslate">mod_dav</code>,
  <code class="notranslate">rclone serve webdav</code>, most NAS "personal cloud"
  apps.

  <ul dir="auto">

  <li>Upload every title, one title, or a single backup, skipping what is already
  on the server. It can also pull a backup back down onto the console, where Checkpoint''s
  usual Restore takes over.</li>

  <li>Credentials are sealed with the encryption API, like Drive''s. Setup, with the
  right base URL for each common server, is in <a href="https://github.com/FlagBrew/Checkpoint/blob/master/scripts/webdav.md"><code
  class="notranslate">scripts/webdav.md</code></a>; <code class="notranslate">tools/webdav-testserver.py</code>
  gives you a throwaway server on your PC to try the whole round trip against first.</li>

  </ul>

  </li>

  <li>Added: <strong>playcoins</strong>, to set the console''s Play Coins (3DS).

  <ul dir="auto">

  <li>Note: the play coins management feature is now available via scripts only.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">3DS: What''s new</h3>

  <ul dir="auto">

  <li>Added: a menu overlay to reach Settings and Scripts.</li>

  <li>Fixed: <strong>GBA Virtual Console saves now move between consoles</strong>
  (<a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4877717415"
  data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/557"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/557/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/557">#557</a>). A backup
  used to be the whole console-side container, signed for the console that made it,
  so restoring it anywhere else failed, or reported success and left the game''s own
  save untouched.

  <ul dir="auto">

  <li>A backup is now the bare save file, the same 512 B to 128 KB <code class="notranslate">.sav</code>
  an emulator or GodMode9 reads, and restoring writes it back into the container and
  re-signs it for the console doing the restoring.</li>

  <li>Backups taken by older versions of Checkpoint still restore.</li>

  </ul>

  </li>

  <li>Fixed: Checkpoint now runs on emulators. The Rosalina <code class="notranslate">hb:ldr</code>
  check is skipped when an emulator is detected, instead of refusing to boot.</li>

  <li>Fixed: modal dialogs now measure and lay out their text properly, so larger
  text and translated strings are not clipped anymore.</li>

  <li>Fixed: a memory corruption in the choice overlay''s callback.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">Switch: What''s new</h3>

  <ul dir="auto">

  <li>Added: a Scripts entry in the sidebar, and a menu overlay to reach Settings
  and Scripts.</li>

  <li>Fixed: the app doesn''t hang anymore when the account selector is opened while
  backup sizes are still being computed. The size worker now pauses while the applet
  is up.</li>

  <li>Fixed: truncated backup names in the backup list.</li>

  <li>Fixed: modal dialogs now measure and lay out their text properly, so larger
  text and translated strings are not clipped anymore.</li>

  <li>Fixed: threads are torn down properly when the app is forced to exit.</li>

  <li>Fixed: unhandled exceptions are logged with far more detail, so crashes can
  actually be diagnosed from the log.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">chlink: What''s new</h3>

  <ul dir="auto">

  <li>Fixed: a backup that travels as a single file instead of a zip -- a DS cart
  save, a GBA VC save -- arrived with the dot stripped out of its name (<code class="notranslate">00000001
  sav</code>), and nothing could restore it afterwards. The receiving side keeps the
  extension now, on both consoles and in chlink.

  <ul dir="auto">

  <li>Backups already received with a mangled name are not lost: a raw backup folder
  holding a single file is restored whatever that file is called.</li>

  </ul>

  </li>

  <li>Added: the receiver logs each stored file with its size and destination, and
  says how far it got when a transfer fails.</li>

  </ul>

  <h3 dir="auto">Translations</h3>

  <ul dir="auto">

  <li>Added: <strong>Simplified Chinese</strong> translation (thanks <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/JeanPhoenixWong/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/JeanPhoenixWong">@JeanPhoenixWong</a>)

  <ul dir="auto">

  <li>Current language support includes English, Italian, French, German, Portuguese,
  Spanish, Dutch, Japanese and Simplified Chinese.</li>

  <li>If you''re a native speaker and think that text wording and appearance in the
  UI can be improved, please submit a pull request or open an issue on this repository.</li>

  </ul>

  </li>

  </ul>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/b41a4bcd-a995-4f50-8a15-e8d0b73fdcb4"><img
  width="194" height="190" alt="qr" src="https://github.com/user-attachments/assets/b41a4bcd-a995-4f50-8a15-e8d0b73fdcb4"
  style="max-width: 100%; height: auto; max-height: 190px;; aspect-ratio: 194 / 190;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-07-26T09:35:31Z'
version: v5.0.0
version_title: Checkpoint 5.0.0
---
