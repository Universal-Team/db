---
author: FlagBrew
avatar: https://avatars.githubusercontent.com/u/42673825?v=4
categories:
- utility
color: '#749285'
color_bg: '#658074'
created: '2016-05-15T08:26:47Z'
description: Gen I to GenVIII save manager.
download_page: https://github.com/FlagBrew/PKSM/releases
downloads:
  PKSM.3dsx:
    size: 7531376
    size_str: 7 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.4.0/PKSM.3dsx
  PKSM.cia:
    size: 6267840
    size_str: 5 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.4.0/PKSM.cia
github: FlagBrew/PKSM
icon: https://raw.githubusercontent.com/FlagBrew/PKSM/master/assets/icon.png
image: https://raw.githubusercontent.com/FlagBrew/PKSM/master/assets/banner.png
image_length: 8070
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  PKSM.cia: https://db.universal-team.net/assets/images/qr/pksm-cia.png
source: https://github.com/FlagBrew/PKSM
stars: 2222
systems:
- 3DS
title: PKSM
unique_ids:
- '0xEC100'
update_notes: '<h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li>Added: <strong>wireless save transfer has been rebuilt on top of Checkpoint''s
  <code class="notranslate">chlink</code> protocol</strong>, replacing the old PKSM
  bridge protocol

  <ul dir="auto">

  <li>Both raw save files and the ZIP backups produced by Checkpoint and <code class="notranslate">chlink</code>
  are accepted</li>

  <li>If a send fails or is cancelled, a recovery copy is kept in <code class="notranslate">sdmc:/3ds/PKSM/backups/wireless</code></li>

  <li>The wiki has been updated with the new instructions. Official documentation
  for the <code class="notranslate">chlink</code> companion app is <a href="https://github.com/BernardoGiordano/Checkpoint/tree/master/tools/chlink#readme">here</a>.</li>

  <li>You can download <code class="notranslate">chlink</code> or latest Checkpoint
  <a href="https://github.com/BernardoGiordano/Checkpoint/releases/latest">here</a>.</li>

  </ul>

  </li>

  <li>Added: <strong>a much faster QR scanner</strong>, which also uses a fraction
  of the memory it used before</li>

  <li>Added: faster boot and smoother menus, with save directories indexed once instead
  of once per game, downloaded assets verified once instead of three times, and far
  fewer allocations while browsing boxes</li>

  <li>Added: a message while the language is being changed, so the app no longer looks
  frozen</li>

  <li>Added: a warning when the wonder card list is full, instead of silently doing
  nothing</li>

  <li>Added: cleaner and more consistent CJK typography across lists and menus (thank
  you <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/seien210300928/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/seien210300928">@seien210300928</a>)</li>

  <li>Added: French item names for Gen 1/2/3 and French location names for Gen 2/3
  (thank you <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SombrAbsol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SombrAbsol">@SombrAbsol</a>)</li>

  <li>Added: a new script to set Island Scan points to 100</li>

  <li>Fixed: DS cartridges and save files wrongly reported as the "wrong size" and
  refusing to load (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2781635211" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1492"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1492/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1492">#1492</a>, fix <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2949991678" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1517" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1517/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1517">#1517</a>,
  fix <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3197154692"
  data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1527"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1527/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1527">#1527</a>, fix <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="3628777831" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1541" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1541/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1541">#1541</a>)</li>

  <li>Fixed: DSi games not being read (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2940981514" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1515"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1515/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1515">#1515</a>)</li>

  <li>Fixed: freezes when opening valid DS saves, including ones dumped through TWiLight
  Menu++ (fix <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="4412318618" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1557"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1557/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1557">#1557</a>)</li>

  <li>Fixed: a crash when loading a Gen 3 Emerald save (fix <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2760092990" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1490" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1490/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1490">#1490</a>)</li>

  <li>Fixed: PKSM getting stuck on "Creating backup... Please wait..." when loading
  a manually added save file (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2433512802" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1475"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1475/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1475">#1475</a>)</li>

  <li>Fixed: extra saves being configurable from the settings but not from the main
  save loading screen (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5237629033" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1574"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1574/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1574">#1574</a>)</li>

  <li>Fixed: a crash while checking the SD card (fix <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4633353024" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1564" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1564/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1564">#1564</a>)</li>

  <li>Fixed: failure to launch with error <code class="notranslate">0xC8A04573</code>,
  as extdata is now reset when it is found in an invalid state (fix <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="4814161960" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1567" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1567/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1567">#1567</a>)</li>

  <li>Fixed: changing status conditions corrupting Pokémon data, along with mislabelled
  fields in the Gen 4/5 hex editors (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1641829628" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1366"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1366/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1366">#1366</a>)</li>

  <li>Fixed: Generation 1 saves only showing the last box you saved (fix <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2091257592" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1437" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1437/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1437">#1437</a>)</li>

  <li>Fixed: leftover garbage bytes after the terminator in Gen 1/2 OT names (fix
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2091875833"
  data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1438"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1438/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1438">#1438</a>)</li>

  <li>Fixed: injected wonder cards not showing up in HeartGold/SoulSilver, and gift
  Pokémon behaving incorrectly (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2116778745" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1439"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1439/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1439">#1439</a>, fix <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2019596586" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1425" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1425/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1425">#1425</a>)</li>

  <li>Fixed: geolocation and encounter data being mangled during Gen 6 transfers (fix
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2459027432"
  data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1476"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1476/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1476">#1476</a>)</li>

  <li>Fixed: Japanese Gen 6 mystery gift bugs (fix <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="2242736784" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1454" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1454/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1454">#1454</a>)</li>

  <li>Fixed: Gen 4 wonder card injection, and mystery gifts are now always injected
  as unused</li>

  <li>Fixed: save content is validated more strictly, so broken files are rejected
  instead of half-loading</li>

  <li>Fixed: countless GPSS bugs, as the two cloud browsers are now a single page
  browser

  <ul dir="auto">

  <li>No more crashes on empty searches, hangs on failed requests or garbled replies</li>

  </ul>

  </li>

  <li>Fixed: several rare freezes and race conditions around the QR scanner, the local
  server and font loading</li>

  <li>Fixed: failed downloads being saved as if they had succeeded</li>

  <li>Fixed: the legality check hanging for two minutes before giving up</li>

  <li>Fixed: missing Black/White and Black 2/White 2 scripts (fix PKSM-Scripts <a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="191791173"
  data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/60"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/60/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/60">#60</a>)</li>

  <li>Fixed: the Mesprit respawn script in Diamond/Pearl/Platinum (fix PKSM-Scripts
  <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="191254592"
  data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/51"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/51/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/51">#51</a>, fix PKSM-Scripts <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="191169723" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/49" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/49/hovercard" href="https://github.com/FlagBrew/PKSM/issues/49">#49</a>)</li>

  <li>Fixed: the Type: Null reset script in Sun/Moon and Ultra Sun/Ultra Moon (fix
  PKSM-Scripts <a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="191457048" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/56"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/56/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/56">#56</a>)</li>

  <li>Fixed: several inconsistencies in the legacy localization data</li>

  <li>Fixed: crash logs not being written correctly</li>

  <li>Removed: the old PKSM bridge, now superseded by wireless transfer</li>

  <li>Removed: the duplicate bank selection screen</li>

  <li>Removed: preloading of every language at boot, which slowed startup down for
  no benefit</li>

  <li>Removed: obsolete sound decoders, unused UI assets and a large amount of dead
  code</li>

  <li>All submodules and build dependencies updated to latest release</li>

  <li>General system stability improvements to enhance the user''s experience</li>

  </ul>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/653644a2-5861-4c04-9ff8-34d6003fa060"><img
  width="178" height="176" alt="immagine" src="https://github.com/user-attachments/assets/653644a2-5861-4c04-9ff8-34d6003fa060"
  style="max-width: 100%; height: auto; max-height: 176px;; aspect-ratio: 178 / 176;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-08-25T18:53:51Z'
version: 10.4.0
version_title: PKSM 10.4.0
wiki: https://github.com/FlagBrew/PKSM/wiki
---
