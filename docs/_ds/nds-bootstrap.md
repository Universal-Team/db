---
author: DS-Homebrew
avatar: https://avatars.githubusercontent.com/u/46971470?v=4
categories:
- emulator
color: '#585758'
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases
downloads:
  nds-bootstrap.7z:
    size: 399105
    size_str: 389 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.52.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 963607
    size_str: 941 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.52.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
icon_index: 140
image: https://i.imgur.com/BFIu7xX.png
image_length: 5116
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds
  downloads:
    nds-bootstrap.7z:
      url: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
priority: true
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
update_notes: "<p dir=\"auto\">Included in <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v23.2.0\"\
  ><strong>TW</strong>i<strong>L</strong>ight Menu++ v23.2.0</a></p>\n<p dir=\"auto\"\
  >Instructions:</p>\n<ol dir=\"auto\">\n<li>Download the <code>.7z</code> file.</li>\n\
  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>\n\
  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>\n\
  </ol>\n<p dir=\"auto\"><strong>What's new?</strong></p>\n<ul dir=\"auto\">\n<li><strong>B4DS\
  \ mode:</strong> Support for more titles have been added, making them playable on\
  \ DS/DS lite consoles!<br>\n(For a complete list of supported titles, see this list\
  \ <a href=\"https://github.com/DS-Homebrew/TWiLightMenu/blob/3c3663d499b22effe92a5c3304836a8a9def549e/universal/include/incompatibleGameMap.h#L49\"\
  >here</a>.)\n<ul dir=\"auto\">\n<li>99Bullets</li>\n<li>99Moves</li>\n<li>ARC Style:\
  \ Soccer! (Korea)</li>\n<li>Kung Fu Dragon</li>\n<li>Mr. Brain (Japan)</li>\n<li>Rabi\
  \ Laby</li>\n<li>Rabi Laby 2</li>\n<li>(For Debug DS consoles:)\n<ul dir=\"auto\"\
  >\n<li>99Seconds</li>\n<li>Mixed Messages</li>\n<li>Phantasy Star 0 Mini</li>\n\
  <li>Space Invaders Extreme Z</li>\n</ul>\n</li>\n</ul>\n</li>\n</ul>\n<p dir=\"\
  auto\"><strong>Bug fixes</strong></p>\n<ul dir=\"auto\">\n<li>The applied AP-fix\
  \ will now persist when soft-resetting.\n<ul dir=\"auto\">\n<li><em>Pok\xE9mon HeartGold\
  \ &amp; SoulSilver Versions</em> will now use the fast soft-reset method again.</li>\n\
  </ul>\n</li>\n<li>Fixed sound in <em>Rainbow Islands Revolution</em> when using\
  \ DSiWarehax or DSi mode.</li>\n<li><strong>B4DS mode:</strong> Cloneboot now works\
  \ in <em>Art Style: BASE 10</em>.</li>\n</ul>\n<p dir=\"auto\"><strong>Known bug</strong></p>\n\
  <ul dir=\"auto\">\n<li>Sleep mode will not work in the 99Trilogy, due to their code\
  \ (possibly) taking place in the overlays.</li>\n</ul>"
updated: '2021-12-09T23:32:45Z'
version: v0.52.0
version_title: v0.52.0
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.