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
    size: 3652156
    size_str: 3 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.3.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 2646976
    size_str: 2 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.3.0/Checkpoint.cia
github: BernardoGiordano/Checkpoint
icon: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/icon.png
image: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/banner.png
image_length: 5618
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  Checkpoint.cia: https://db.universal-team.net/assets/images/qr/checkpoint-cia.png
source: https://github.com/BernardoGiordano/Checkpoint
stars: 3110
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<h3 dir="auto">3DS: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>WarioWare: D.I.Y. save backup and restore</strong>. Its 16 MB
  save lives in NAND inside the cartridge instead of on a save chip, where no 3DS
  save interface can reach it. Checkpoint now talks to the cartridge directly, so
  you back it up and restore it from the title list like any other DS cart: no GodMode9i,
  no rebooting into DS mode.

  <ul dir="auto">

  <li>This is particularly exciting because the strategy used to allow this functionality
  without rebooting in DS mode is brand new and this was thought to be impossible
  to achieve in the past.</li>

  <li>A backup takes about a minute. A restore only rewrites the pages that differ
  from what is already on the cartridge, and reads every page it writes back to verify
  it. Restoring the backup you just made writes nothing at all; the worst case, where
  every page differs, takes about 6.5 minutes.</li>

  <li>Checkpoint''s dumps were checked byte for byte against GodMode9i''s dumps of
  the same cartridge.</li>

  <li><strong>The CIA build is required.</strong> The 3DSX build can''t reach the
  cartridge controller, so it refuses instead of reading.</li>

  <li>So far this has been tested on one European cartridge. Other regions, and the
  other carts that save the same way, are recognised but not verified yet: <em>please</em>
  report back.</li>

  <li>Don''t remove the cartridge or turn off the console during a restore. Pages
  that were already written stay written, so an interrupted restore leaves the save
  half old and half new until you run it again.</li>

  </ul>

  </li>

  <li>Fixed: DS cart backups no longer fail at random while writing to the SD card.</li>

  <li>Fixed: backing up the extdata of the theme entries no longer fails.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">Switch: What''s new</h3>

  <ul dir="auto">

  <li>Fixed: <strong>restoring a save no longer inflates it to over 64 MB</strong>.
  Since 5.1.0, every restore extended the save data area by its safety margin even
  when the backup already fit, so a 2 MB save came back at 65 MB. The area is now
  extended only when the backup actually needs more room than it has.</li>

  <li>Fixed: <strong>Checkpoint now opens on the profile it was launched under</strong>,
  instead of always starting on the first user. A title override uses the profile
  you picked at launch; applet mode uses the profile that last opened a game.</li>

  <li>Fixed: <strong>the account picker can now be reached with the controller</strong>.
  The avatar at the bottom of the sidebar is part of the sidebar cursor now: press
  Down past the settings gear. ZL still opens it too.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">Wireless transfer: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>a configurable server port</strong>, in Settings &gt; Network
  (3DS) / Connectivity (Switch), under <strong>Server port</strong>.

  <ul dir="auto">

  <li>8000 is still the default. Change it when another program already holds that
  port.</li>

  <li>The port is shared by the wireless receiver and the log server, and takes effect
  the next time Checkpoint starts. Anything from 1024 to 65535 is accepted.</li>

  <li>The Receive screen shows the port, as before. chlink takes it with <code class="notranslate">--port</code>,
  or as <code class="notranslate">--to &lt;ip&gt;:&lt;port&gt;</code>.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Scripting: What''s new</h3>

  <ul dir="auto">

  <li>Fixed: <strong>webdav now works with Synology''s WebDAV Server</strong>. Synology
  accepted the login and then answered the folder check with a 403, because the request
  named the folder without its trailing <code class="notranslate">/</code>. Folders
  are now always requested with the slash, which is the form the WebDAV spec tells
  clients to use.</li>

  </ul>

  <hr>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/ad244d64-c211-43d7-802f-d734e2c06ce8"><img
  width="200" height="200" alt="qr" src="https://github.com/user-attachments/assets/ad244d64-c211-43d7-802f-d734e2c06ce8"
  style="max-width: 100%; height: auto; max-height: 200px;; aspect-ratio: 200 / 200;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-10-13T19:22:44Z'
version: v5.3.0
version_title: Checkpoint 5.3.0
---
