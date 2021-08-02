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
    size: 370979
    size_str: 362 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.46.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 900535
    size_str: 879 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.46.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://raw.githubusercontent.com/DS-Homebrew/nds-bootstrap/master/retail/assets/icon.bmp
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
update_notes: '<p><a target="_blank" rel="noopener noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/HGSS-Electricwifi.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/HGSS-Electricwifi.png"
  alt="screenshot1" style="max-width:100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/SonicColors.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/SonicColors.png"
  alt="screenshot2" style="max-width:100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/ProfLayton.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/ProfLayton.png"
  alt="screenshot3" style="max-width:100%;"></a><br>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/MKDS.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/MKDS.png"
  alt="screenshot4" style="max-width:100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/KH-358-2-Days.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/KH-358-2-Days.png"
  alt="screenshot5" style="max-width:100%;"></a> <a target="_blank" rel="noopener
  noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/StyleSavvy.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/raw/master/screenshots/v0.46.0/StyleSavvy.png"
  alt="screenshot6" style="max-width:100%;"></a></p>

  <p>Instructions:</p>

  <ol>

  <li>Download the <code>.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code>.nds</code> files, to <code>root:/_nds</code>.</li>

  <li><strong>TWLMenu++ users:</strong> Extract the <code>.ver</code> file to <code>root:/_nds/TWiLightMenu</code>.</li>

  </ol>

  <p>Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v21.3.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v21.3.0</a></p>

  <p><strong>What''s new?</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and Rocket Robz) You can now take screenshots of DS games!

  <ul>

  <li>Screenshots will be saved to <code>screenshots.tar</code> in <code>sd:/_nds/nds-bootstrap/</code>.</li>

  <li>Due to hardware limitations, only screenshots of the main-set screen will be
  taken.</li>

  <li>Open the in-game menu, and select <code>Screenshots...</code></li>

  <li>Select the VRAM bank, in case if the screenshot looks incorrect.</li>

  <li>Limit is 50 screenshots. After reaching the limit, you cannot take any more,
  until you delete <code>screenshots.tar</code> in <code>sd:/_nds/nds-bootstrap/</code>,
  where it''ll be re-created on next boot.</li>

  </ul>

  </li>

  <li>You can now step 1 frame, while in the in-game menu.

  <ul>

  <li>Useful for getting frame-perfect screenshots!</li>

  </ul>

  </li>

  </ul>

  <p><strong>Improvements</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>
  and various) Updated in-game menu translations!</li>

  <li>The <code>Date modified</code> flag in the <code>.sav</code> file is now updated,
  when booting the game.</li>

  <li>The in-game menu button combo now does nothing in DSi mode, since it''s already
  inaccessible.</li>

  <li>Asynch card read is now disabled in DSi mode, regardless of settings.</li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>Fixed some DSi mode compatibility on DSi consoles (at the cost of card data
  cache size).</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Fixed where the in-game menu would sometimes be blank.</li>

  </ul>

  <p><strong>Known bugs</strong></p>

  <ul>

  <li>Screenshots of ActImagine/MobiClip videos contain only black screens.</li>

  <li>Screenshots of moonshineDS will only contain half the screen on either horizontal
  side.</li>

  <li>The frame-stepping feature will not always work properly.</li>

  </ul>'
updated: '2021-08-02T08:19:37Z'
version: v0.46.0
version_title: 'v0.46.0: Screenshots are here!'
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.