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
    size: 1494780
    size_str: 1 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.12.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 1049536
    size_str: 1 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v3.12.0/Checkpoint.cia
github: BernardoGiordano/Checkpoint
icon: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/icon.png
image: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/banner.png
image_length: 5618
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: undisclosed
qr:
  Checkpoint.cia: https://db.universal-team.net/assets/images/qr/checkpoint-cia.png
source: https://github.com/BernardoGiordano/Checkpoint
stars: 2959
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<p dir="auto">This release adds support for previously unsupported
  save types on the Switch. I didn''t have any need to support them at the time because
  I didn''t play any of these kind of games. After all these years, I still don''t
  play them, but I felt it was time to properly support them into Checkpoint.</p>

  <p dir="auto"><strong>Important notice:</strong> I wasn''t able to test backup and/or
  restore these new save types first-hand. Use the new features carefully and <em>please</em>
  report back! That''s why this new version is currently in pre-release.</p>

  <p dir="auto"><em><strong>2026-04-26 update</strong></em>: I haven''t heard about
  any regression or issue feedbacks, so I''m changing the status of this version from
  pre-release to release.</p>

  <h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li>Added: <strong>support BCAT saves</strong> on the Switch version of the app.</li>

  <li>Added: <strong>support device saves</strong> on the Switch version of the app.</li>

  <li>Added: <strong>support system saves</strong> on the Switch version of the app.

  <ul dir="auto">

  <li>The UI of the app has been slightly upgraded to account for these new save types.</li>

  </ul>

  </li>

  <li>Added: per-file progress bar.

  <ul dir="auto">

  <li>The UI will now display two progress bars, one for the overall save progress
  and one for each file in the save archive.</li>

  </ul>

  </li>

  <li>Fixed: occasional crash when loading NAND saves on the 3DS version of the app.</li>

  <li>Fixed: Checkpoint should not freeze anymore when performing backup or restore
  operations.</li>

  <li>Fixed: support asian system fonts in the Switch version of the app.

  <ul dir="auto">

  <li>This solves an issue where special characters were not rendered in the UI.</li>

  </ul>

  </li>

  <li>Fixed: add not-empty validation for backup names.</li>

  <li>Fixed: file paths could contain multiple <code class="notranslate">/</code>
  characters one after the other, causing folder deletion issues.</li>

  <li>Fixed: undefined behaviour when trying to close directories that were not opened.</li>

  <li>Fixed: undefined behaviour could occur when reading a file''s size.</li>

  <li>Fixed: log directory read errors.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/79d23fc1-e0f4-4171-aaf9-30a219a64006"><img
  width="218" height="217" alt="Screenshot From 2026-03-12 20-58-51" src="https://github.com/user-attachments/assets/79d23fc1-e0f4-4171-aaf9-30a219a64006"
  style="max-width: 100%; height: auto; max-height: 217px;; aspect-ratio: 218 / 217;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-03-12T19:56:00Z'
version: v3.12.0
version_title: Checkpoint 3.12.0
---
