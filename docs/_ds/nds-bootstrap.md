---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
color_bg: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 826979
    size_str: 807 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.12.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1193939
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.12.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1329
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v27.21.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v27.21.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> or <code class="notranslate">.zip</code>
  file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">🎁 What''s new? (B4DS mode) 🎁</h3>

  <ul dir="auto">

  <li>4 more DSiWare titles are now playable on DS &amp; DS Lite consoles! (<strong>Total:</strong>
  491 -&gt; 495)

  <ul dir="auto">

  <li>Absolute Chess (Does not save)</li>

  <li>Absolute Reversi (Does not save)</li>

  <li>Don''t Cross the Line</li>

  <li>Panewa!</li>

  </ul>

  </li>

  <li>The USA and European versions of <em>Treasure Hunter X</em> (aka <em>Fall in
  the Dark</em> in Japan) is now supported.

  <ul dir="auto">

  <li>Saving is still not implemented for this game.</li>

  </ul>

  </li>

  <li><em>Neko no Iru Tangram: Neko to Iyashi no Silhouette Puzzle</em> is now playable
  on DS &amp; DS Lite debug consoles!

  <ul dir="auto">

  <li>This means it will not run on a regular console, as the game requires more than
  4MB of RAM to run.</li>

  <li>Music does not play.</li>

  <li>Seems to not save data.</li>

  </ul>

  </li>

  <li><code class="notranslate">apFixOverlays.bin</code> is now only written if the
  AP-fix directly patches the ROM overlays. This provides a slight boot speed improvement
  if the AP-fix does not directly patch the overlays.</li>

  <li>Added detection of SuperCard SD Slot-2 flashcards for use as RAM expansion if
  SuperFW is installed.</li>

  </ul>

  <h3 dir="auto">🎁 Bug fixes 🎁</h3>

  <ul dir="auto">

  <li>Fixed a long-standing bug where both <em>Bleach: Dark Souls</em> &amp; <em>Madagascar</em>
  would fail to save data.

  <ul dir="auto">

  <li>If <em>Bleach: Dark Souls</em> still shows the message where save data is corrupted,
  try deleting the <code class="notranslate">.sav</code> file for the game, then try
  again.</li>

  </ul>

  </li>

  <li>Fixed an overlooked bug which caused the AP-fix for <em>Style Savvy</em>/<em>Style
  Boutique</em> to show a red error screen on boot.</li>

  <li>ARM9-only AP-fixes now apply to any ROM where the ARM9 binary offset is higher
  than offset <code class="notranslate">0x4000</code>.

  <ul dir="auto">

  <li>Fixes crashing in <em>Pokemon SoulSilver Deluxe</em>.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/taxicat1/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/taxicat1">@taxicat1</a>:
  Added a proper fix for the <em>Puppy Palace</em> boot issue without the need for
  nds-bootstrap-specific workarounds.</li>

  <li>VCOUNT register is no longer cleared before boot. Fixes a possible bug where
  a frame could be misrendered on 3DS consoles.</li>

  </ul>'
updated: '2025-12-25T08:58:04Z'
version: v2.12.0
version_title: 'v2.12.0: TWL Christmas Release 🎄'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.