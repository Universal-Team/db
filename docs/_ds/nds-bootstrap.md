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
    size: 841360
    size_str: 821 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.17.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1212693
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v2.17.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
source: https://github.com/DS-Homebrew/nds-bootstrap
stars: 1407
systems:
- DS
title: nds-bootstrap
update_notes: '<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/DS-Homebrew/nds-bootstrap/blob/master/images/Anniversaries/10th/Logo.png"><img
  src="https://github.com/DS-Homebrew/nds-bootstrap/blob/master/images/Anniversaries/10th/Logo.png"
  alt="logo" style="max-width: 100%;"></a></p>

  <p dir="auto">On October 4th, 2016, nds-bootstrap has released, making it''s way
  onto the 3DS homebrew scene, and later on, the DSi homebrew scene.<br>

  And now recently, as of October 4th, 2026, nds-bootstrap has turned 10 years old!</p>

  <p dir="auto">The goal of nds-bootstrap was to run DS(i) games and old DS homebrew
  from the DSi &amp; 3DS SD card, a feature which many have thought to be impossible
  at the time.<br>

  This project has been started by (former lead dev.) <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/ahezard/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ahezard">@ahezard</a>,
  and later continued by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/shutterbug2000/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/shutterbug2000">@shutterbug2000</a>
  and (current lead dev.) <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/RocketRobz/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/RocketRobz">@RocketRobz</a>
  (me).</p>

  <p dir="auto">The first few releases have only supported some homebrew titles, but
  later releases have added support for official/commercial DS games, along with:</p>

  <ol dir="auto">

  <li>DS game compatibility improvements, along with occasional homebrew compatibility
  improvements.</li>

  <li>Support for cheats.</li>

  <li>Flashcard support (known as B4DS mode), allowing DS games to run on any flashcard
  (even those such as <em>Games n Music</em>, which normally don''t support those
  games!)</li>

  <li>An in-game menu similar to Luma''s Rosalina menu.</li>

  <li>DSi mode support, allowing DSi-Enhanced games to use DSi features such as doubled
  clock speed, camera, and/or WPA1/2 WiFi networks, along with running DSi-Exclusive
  and DSiWare titles.</li>

  <li>A screenshot feature, which can be accessed through the in-game menu.</li>

  <li>Support for a <em>lot</em> of DSiWare titles (plus a few DSi-Exclusives) on
  flashcards (via B4DS mode) on DS &amp; DS Lite consoles (another feature which was
  thought to be impossible).</li>

  <li>Support for custom/DS Phat screen color filters, changing the on-screen colors
  of games (though the code which applies them causes issues in some games).</li>

  <li>Changing the screen''s refresh rate, affecting the game''s speed as a result.</li>

  </ol>

  <p dir="auto">We are also aware of users wanting WPA1/2 WiFi support in non-DSi-Enhanced
  DS games.<br>

  While this feature would be perfect for a release such as this, it is unfortunately
  difficult to implement due to lack of knowledge on how to find the code which handles
  WiFi in those games.</p>

  <p dir="auto">Over the years, we have improved nds-bootstrap based on compatibility
  and bug reports from users like you!<br>

  Without such reports, this project would likely not be running as good as it is
  now.</p>

  <p dir="auto">Here''s to 10 years of playing games from the DSi &amp; 3DS SD card
  with nds-bootstrap!<br>

  And now, onto this anniversary release''s changelog...</p>

  <h1 dir="auto">Changelog</h1>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS SD Card:</strong> Homebrew compatibility has been improved once
  again!

  <ul dir="auto">

  <li>Both <em>jEnesisDS</em> and <em>SNEmulDS</em> now read from the SD card slot,
  and can now save data (where with a RAM disk, data would be cleared after rebooting
  or powering off)!</li>

  <li>Homebrew made with <em>DS Game Maker</em> now boot and/or read from NitroFS
  properly!</li>

  <li>The Bullet Bill version of <em>Mario Paint Composer DS</em> now boots!</li>

  </ul>

  </li>

  <li><strong>DSi/3DS SD Card:</strong> Implemented a DSi-Enhancement patch for <em>jEnesisDS</em>,
  where it increases the ROM size limit from 3MB (<code class="notranslate">0x306800</code>
  bytes) to 4MB (<code class="notranslate">0x400000</code> bytes). This means <em>jEnesisDS</em>
  (running in DSi mode) can now boot games such as:

  <ul dir="auto">

  <li>Sonic 3 &amp; Knuckles</li>

  <li>Sonic 3D Blast/Flickies'' Island</li>

  <li>Toy Story</li>

  <li>and more!</li>

  </ul>

  </li>

  <li><strong>DSi/3DS SD Card:</strong> <em>Super Smash Bros. Crash! DS</em> and other
  (pre-2010) DS homebrew which reset into another <code class="notranslate">.nds</code>
  file, will now boot straight into one instead of rebooting the console first.</li>

  <li><strong>DSi/3DS:</strong> Added a Slot-1 mode setting for DSiWare, allowing
  them to boot faster than with the original SD/MMC code from those titles used!

  <ul dir="auto">

  <li>As a side effect, the original <code class="notranslate">.pub</code>/<code class="notranslate">.prv</code>
  save files will not be used, and will instead use the <code class="notranslate">.sav</code>
  files normally used in B4DS mode.</li>

  <li>Previously, this would only activate if SD/MMC access is disabled in SCFG.</li>

  <li>Regardless if this setting is turned off or on, it will automatically activate
  if a booted DSiWare ROM is larger than 64MB, as loading would be slightly slow without
  that setting.</li>

  </ul>

  </li>

  <li>AP-fixes for <em>Digimon Story: Super Xros Wars</em> are now applied to modified
  ROMs such as ROM hacks and translations!</li>

  <li><strong>DSi/3DS:</strong> Added ROM pre-load settings for:

  <ul dir="auto">

  <li>MegaMan Star Force</li>

  <li>MegaMan Star Force 2</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Wokann/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Wokann">@Wokann</a>:
  Dragon Quest IX Chinese fan-translation</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Title screen music for all <em>MegaMan Star Force</em>
  games are now asynchronously loaded.</li>

  <li><strong>DSi/3DS:</strong> Added minimal async card read setting.

  <ul dir="auto">

  <li>Turning off the async card read setting will now turn off asynchronous (non-DMA)
  Mobiclip and STRM file reads.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS:</strong> Added Slot-1 mode save support for <em>Starship Defense</em>
  &amp; <em>X-Scape</em>!</li>

  <li>Various: Updated in-game menu translations.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> By disabling SWI halt hook for the following games,
  these issues are fixed:

  <ul dir="auto">

  <li>Occasional slowdowns in <em>Mario Kart DS</em></li>

  <li>Random freezing in <em>Pokémon</em> Gen 4 games</li>

  <li><em>Soma Bringer</em> 3D graphical glitch in save selection menu</li>

  <li>This is done automatically, and will not need any settings changed.</li>

  </ul>

  </li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/taxicat1/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/taxicat1">@taxicat1</a>:
  Adjusted race condition fix for <em>Akumajou Dracula: Gallery of Labyrinth</em>
  (Rev 1), fixing a bug which caused a red error screen to appear after boot.</li>

  <li><strong>DSi/3DS:</strong> Fixed <em>Lux-Pain</em> freezing at some point in
  the opening cutscene.</li>

  <li><strong>DSi/3DS:</strong> Fixed <em>CSI: Unsolved!</em> not playing audio and
  freezing at the logo.</li>

  <li><strong>DSi/3DS:</strong> Fixed <em>Need for Speed Carbon: Own the City</em>
  freezing on loading screen when using a screen color filter and/or DS Phat colors.</li>

  <li><strong>DSi/3DS:</strong> Both AES keys 1 &amp; 2 are now set (if they aren''t)
  when booting a DSi title.

  <ul dir="auto">

  <li>Setting AES KEY2 fixes photos not being read in the DSi Camera app.</li>

  </ul>

  </li>

  <li><strong>DSi/3DS SD Card:</strong> Fixed homebrew not booting in DSi mode and/or
  via DSiWarehax (ex. Memory Pit, Flipnote Lenny, etc.).</li>

  <li><strong>DSi/3DS SD Card:</strong> Fixed/improved ARGV passing for homebrew,
  allowing the Bullet Bill version of <em>Mario Paint Composer DS</em> to boot.</li>

  <li><strong>3DS:</strong> Fixed returning to loader not working for some 3DS consoles.</li>

  </ul>

  <h3 dir="auto">Known bugs</h3>

  <ul dir="auto">

  <li><strong>DSi/3DS:</strong> Due to the Slot-1 mode setting using <code class="notranslate">.sav</code>
  save files normally used in B4DS mode, some DSiWare titles will not save, and NAND
  files cannot be accessed (aside from <code class="notranslate">TWLFontTable.dat</code>/<code
  class="notranslate">CHNFontTable.dat</code>/<code class="notranslate">KORFontTable.dat</code>
  placed in <code class="notranslate">sd:/_nds/nds-bootstrap/</code>).</li>

  <li><strong>DSi/3DS SD Card:</strong> Due to a bug within jEnesisDS, it will not
  boot <em>Toy Story</em> without correcting the region field in the ROM''s header,
  as it''ll show a region lockout screen otherwise.

  <ul dir="auto">

  <li>This can be done by opening the ROM in a hex editor, going to offset <code class="notranslate">0x1F0</code>,
  and writing either the letter <code class="notranslate">U</code> (for the USA version)
  or <code class="notranslate">E</code> (for the European version).</li>

  </ul>

  </li>

  </ul>'
updated: '2026-10-11T03:54:03Z'
version: v2.17.0
version_title: 'v2.17.0: 10th Anniversary Release'
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>nds-bootstrap</summary>
<ol>
<li>Download <code>nds-bootstrap.7z</code></li>
<li>Extract everything from the 7z to <code>/_nds/</code> on your SD card</li>
</ol>
</details>

