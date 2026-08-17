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
    size: 3452680
    size_str: 3 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.1.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 2487232
    size_str: 2 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.1.0/Checkpoint.cia
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
stars: 3050
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<h3 dir="auto">FTP: What''s new</h3>

  <ul dir="auto">

  <li>Fixed: <strong>the FTP server is a new implementation</strong>. The old core
  is gone, replaced with the latest source code from <a href="https://github.com/mtheall">mtheall</a>''s
  <a href="https://github.com/mtheall/ftpd">ftpd</a>, which has been adapted to properly
  fit in Checkpoint.</li>

  <li>Fixed: <strong>3DS transfers are roughly 4x faster on upload and 2x on download</strong>.
  The bottleneck was synchronous socket calls stalling the transfer thread, so the
  console now overlaps disk and network work instead of alternating between them.

  <ul dir="auto">

  <li>You''ll notice the UI being a bit less responsive on the 3DS when FTP transfers
  are running: this is completely normal.</li>

  </ul>

  </li>

  <li>Fixed: the Switch server no longer exhausts the system''s socket buffers during
  a folder upload, which left it unable to accept new data connections until it timed
  out.</li>

  <li>Fixed: turning FTP off in Settings now closes the listening socket and drops
  the sessions, instead of leaving the port open.</li>

  </ul>

  <h3 dir="auto">Scripting: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>browser</strong>, a file browser for the SD card <em>and</em>
  for a title''s live save archive.

  <ul dir="auto">

  <li>It supports copy, move, rename, delete, make folders, read properties, zip and
  unzip, one item or a batch at a time.</li>

  <li>It is the practical way to reach into a save without a PC: pull one file out
  of an archive onto the card, drop an edited one back in, or move a folder between
  two titles.</li>

  </ul>

  </li>

  <li>Added: <strong>extdata</strong> (3DS), to create the extdata archive a title
  never made (<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="5096195299" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/576"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/576/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/576">#576</a>).

  <ul dir="auto">

  <li>This script solves an issue where game mods use extdata for a title that never
  creates them. The script allows to artificially create a new extdata archive for
  that title.</li>

  <li>It also inspects any extdata id, including one a mod wrote under an id Checkpoint
  does not derive from the title id, and deletes an archive when you mean to.</li>

  </ul>

  </li>

  <li>Added: new API calls, all documented in <a href="https://github.com/FlagBrew/Checkpoint/blob/master/scripts/README.md"><code
  class="notranslate">scripts/README.md</code></a>.

  <ul dir="auto">

  <li><code class="notranslate">sav_mkdir</code>, <code class="notranslate">sav_rmdir</code>
  and <code class="notranslate">sav_rename</code>: scripts can now shape the folder
  structure inside a save archive, not just read and write files in it.</li>

  <li><code class="notranslate">sav_open_extdata</code>, to open a per-title extdata
  archive by its raw id.</li>

  <li><code class="notranslate">extdata_default_id</code>, <code class="notranslate">extdata_create</code>
  and <code class="notranslate">extdata_delete</code> (3DS; they return <code class="notranslate">-1</code>
  on Switch). <code class="notranslate">extdata_create</code> refuses to touch an
  archive that already exists, so a mistyped id cannot erase a save.</li>

  </ul>

  </li>

  <li>Fixed: the 3DS title catalog handed to scripts now also holds the titles that
  appear in the Extdata list alone.</li>

  <li>Fixed: <code class="notranslate">strdup</code> allocates on the same run-scoped
  heap as <code class="notranslate">malloc</code>, so <code class="notranslate">free()</code>
  releases it and an aborted run reclaims it.</li>

  </ul>

  <h3 dir="auto">Wireless transfer: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>a fixed Receive PIN</strong>, in Settings &gt; Network (3DS)
  / Connectivity (Switch).

  <ul dir="auto">

  <li>The PIN is still random per receive by default. Pin one and a <code class="notranslate">chlink
  send --pin 1234</code> baked into a script keeps working run after run, which is
  what makes unattended batch transfers from the PC possible.</li>

  </ul>

  </li>

  <li>Fixed: <strong><code class="notranslate">chlink send</code> failing with "receiver
  rejected the PIN (403): Invalid token"</strong> (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4952089417" data-permission-text="Title
  is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/561"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/561/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/561">#561</a>). Go canonicalises
  header names before writing them, so the console''s case-sensitive lookup never
  found the token header and rejected every upload.</li>

  <li>Fixed: a backup received from a sender that identifies no installed title no
  longer lands in an "Unknown title" folder (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5041235284" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/572"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/572/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/572">#572</a>). It goes
  to the title whose backup list you opened Receive from, which is the one you pointed
  at.</li>

  <li>Fixed: the receiver no longer logs a connection in progress as an error, and
  no longer floods the log during a transfer.</li>

  </ul>

  <h3 dir="auto">3DS: What''s new</h3>

  <ul dir="auto">

  <li>Fixed: <strong>a restore that cannot fit the console''s path limit is refused
  before anything is deleted</strong>. It used to wipe the save archive first and
  die afterwards, on a backup folder the filesystem was never going to accept. Both
  the copy roots and every entry under them are checked up front, and the message
  names the offending path.</li>

  <li>Fixed: <strong>files a desktop OS left next to your backup no longer break a
  restore</strong> (<a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="5100258737" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/577"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/577/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/577">#577</a>). macOS
  stores a file''s extended attributes in a <code class="notranslate">._</code> sidecar
  next to it on FAT/exFAT, and drops <code class="notranslate">.DS_Store</code> in
  every folder Finder opens; a restore hit one <em>after</em> it had already cleared
  the console-side save. Those, and the equivalents Windows leaves behind, are now
  filtered out of the copy.</li>

  <li>Fixed: <strong>carts whose save lives in on-cart NAND are now identified</strong>
  (<a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4867794223"
  data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/553"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/553/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/553">#553</a>, WarioWare:
  D.I.Y. and friends). They have no SPI save chip, so the probe used to report a bogus
  capacity and back up whatever the bus returned. Checkpoint now says what the cart
  is and points at GodMode9i in DS mode, rather than failing with a save archive error.</li>

  <li>Fixed: <strong>the progress modal no longer looks frozen while a restore clears
  the destination</strong> (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4914938003" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/559"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/559/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/559">#559</a>). Clearing
  an extdata archive of thousands of files is now its own progress stage, and the
  stage labels (Backup, Restore, Clearing, Sending...) are translated.</li>

  <li>Fixed: buttons no longer do anything while the title list is still loading (<a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4980056966"
  data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/565"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/565/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/565">#565</a>). You
  could back up or restore a title you could not see yet, against a selection that
  was about to move.</li>

  <li>Added: <strong>Simplified Chinese is selectable in Settings</strong> (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4985763939" data-permission-text="Title
  is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/566"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/566/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/566">#566</a>, thanks
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/dragonflylee/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dragonflylee">@dragonflylee</a>).
  The translation shipped in 5.0.0 but the 3DS language list never offered it.</li>

  <li>Added: New 3DS consoles also run their application cores at 804 MHz now. This
  is a no-op on Old 3DS and 2DS.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">Switch: What''s new</h3>

  <ul dir="auto">

  <li>Fixed: <strong>restoring a save of tens of thousands of small files no longer
  stalls near the end</strong>.

  <ul dir="auto">

  <li>The save data area is extended when the backup needs more room than it has.</li>

  <li>Files are preallocated instead of being grown block by block, and the free space
  is checked against the cluster-rounded requirement after the wipe, so the restore
  refuses up front instead of dying at 95%.</li>

  <li>The copy is counted against the pre-flight scan: a restore that reports success
  but moved fewer files than the backup holds is now reported as the failure it is.</li>

  <li>Save partition space is logged at every step, so a restore that still fails
  can be diagnosed from the log.</li>

  </ul>

  </li>

  <li>Fixed: <strong>restore verification is about twice as fast</strong>. The CRC
  of each file is taken from the bytes already in the copy buffer, so the verify pass
  re-reads only the committed save instead of both sides.</li>

  <li>Fixed: <strong>the console no longer goes to sleep in the middle of a backup,
  restore or transfer</strong> (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5041455898" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/574"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/574/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/574">#574</a>). Sleeping
  suspended the process mid-copy, on the save filesystem, with a journal half committed.
  Only auto-sleep is held off: the screen still dims on its usual idle delay.</li>

  <li>Added: the selection ring and the grid now animate between tiles instead of
  jumping, and snap when what is underneath changes (a different save type filter,
  a different account).</li>

  <li>Fixed: the same progress and stage-label work as the 3DS side (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4914938003" data-permission-text="Title
  is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/559"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/559/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/559">#559</a>).</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">Translations</h3>

  <ul dir="auto">

  <li>Added: <strong>Russian</strong> translation (thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Waleri228/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Waleri228">@Waleri228</a>)

  <ul dir="auto">

  <li>Current language support includes English, Italian, French, German, Portuguese,
  Spanish, Dutch, Japanese, Simplified Chinese and Russian.</li>

  <li>If you''re a native speaker and think that text wording and appearance in the
  UI can be improved, please submit a pull request or open an issue on this repository.</li>

  </ul>

  </li>

  </ul>

  <hr>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/45e2f983-428f-46eb-aeba-109ee8ca2f86"><img
  width="190" height="195" alt="qr" src="https://github.com/user-attachments/assets/45e2f983-428f-46eb-aeba-109ee8ca2f86"
  style="max-width: 100%; height: auto; max-height: 195px;; aspect-ratio: 190 / 195;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-08-12T09:57:55Z'
version: v5.1.0
version_title: Checkpoint 5.1.0
---
