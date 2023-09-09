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
    size: 762668
    size_str: 744 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.0.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1850990
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v1.0.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
image: https://i.imgur.com/BFIu7xX.png
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v26.1.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v26.1.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds/</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <ul dir="auto">

  <li>nds-bootstrap has supported many popular DS games, such as <em>Super Mario 64
  DS</em>, <em>New Super Mario Bros.</em>, the <em>Kirby</em> games, the <em>MegaMan
  ZX</em> games, the <em>Castlevania</em> games, the <em>Sonic Rush</em> series of
  games, <em>The Legendary Starfy</em>, and many more!<br>

  For a long time though, one of them has not been supported... until now.<br>

  That''s right! You''ve asked and we listened, and now, <em>Golden Sun: Dark Dawn</em>
  is finally supported!

  <ul dir="auto">

  <li>To know how it''s finally supported, scroll down below.</li>

  <li>This does not apply to B4DS mode.</li>

  </ul>

  </li>

  <li>Nintendo programs such as NTR EVA/Aging and Wii Sequencer are now supported.</li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>The heap of TWL titles is no longer shrunk in order to maintain compatibility!

  <ul dir="auto">

  <li>This does not apply to B4DS mode.</li>

  <li>On DSi, for cart-based games, only 128KB of heap is shrunk if the game is running
  from the SD card, and/or if cheats are enabled.</li>

  <li>ce7i binary has been moved to DSi WRAM for a minor speed boost.</li>

  </ul>

  </li>

  <li>To fit a bit more small ROMs into RAM, those which do not contain overlays are
  now loaded without the arm7 binary.</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed certain SDK3-4 games not booting, due to the cluster cache of the save
  file being compressed.</li>

  <li>Fixed an overlooked bug where TWL (DSi-Enhanced/Exclusive) games would crash
  later on 3DS consoles.</li>

  <li>Error exception screen is now triggered for NTR-type games running in DSi mode,
  or if using DSiWarehax.</li>

  <li>Fixed certain games not booting by improving MPU search code.</li>

  <li>Fixed soft-reset button combo not working in <em>Foto Showdown</em>.

  <ul dir="auto">

  <li>The game actually uses the soft-reset function meant to be used in DSiWare titles,
  rather than the normal cart version.</li>

  </ul>

  </li>

  <li>On DSi, TWLCFG from TWLNAND is now re-loaded, if it''s not detected in RAM.</li>

  <li>Fixed an overlooked bug which went unnoticed since DSiWare got supported on
  DS &amp; DS Lite. The bug being where on DS or DS Lite, starting a DSiWare title
  which has WiFi support would wipe the WiFi data off of the console.</li>

  <li>The EUR/AUS version of <em>Bomberman Blitz</em> now boots on DS &amp; DS Lite.</li>

  </ul>

  <hr>

  <h3 dir="auto">How is <em>Golden Sun: Dark Dawn</em> working now? What has been
  done?</h3>

  <p dir="auto"><strong>NOTE:</strong> This is a lengthy read. If you don''t want
  to know the full specifics, scroll down to <strong>In short</strong>.</p>

  <p dir="auto">For the longest time since nds-bootstrap''s first release supporting
  retail/commercial games, one of those games has never worked, despite the many compatibility
  fixes implemented throughout each later release.<br>

  That game is <em>Golden Sun: Dark Dawn</em>. When trying to boot it, it would only
  show two black screens.</p>

  <p dir="auto">The reason for that, is due to an AP measure in the game itself, and
  the AP-fix included with <strong>TW</strong>i<strong>L</strong>ight Menu++ has unfortunately
  never patched it out, despite it being known to work with flashcards.<br>

  You might be wondering, but then how does the demo version boot sucessfully? It
  simply didn''t include any AP measures.</p>

  <p dir="auto">After a long wait, and gaining a little bit of ARM ASM knowledge from
  playing around with it and getting DSiWare games working on DS/DS Lite, I''ve decided
  to implement a new AP-fix for <em>Golden Sun: Dark Dawn</em>, with some help from
  Gericom (the GBARunner2/3 developer) and the NO$GBA debugging emulator.</p>

  <p dir="auto">The first AP measure takes place in overlay 335, which contains DSProtect
  v2.01s.<br>

  By comparing what happens in the game''s code with and without nds-bootstrap, I
  was able to patch the overlay to reproduce what occurs without nds-bootstrap.<br>

  As a result, the game now boots into the company logos and the title screen.<br>

  From there, the name entry menu would appear, and after entering the name, the company
  logos would then appear again, and after fading out, the game crashes.</p>

  <p dir="auto">The next step was to patch overlay 334, which contains DSProtect v2.01
  (with no s at the end, and works differently from the other one).<br>

  After applying the patch, as well as a new checksum for the overlay, the game no
  longer crashes, and the title screen appears once again.</p>

  <p dir="auto">To make the company logos and title screen not appear again after
  entering the character''s name, the next step was to make the patch for overlay
  334 return the proper value the game expects (which is 0x11F).<br>

  As a result, the game''s opening cutscene now plays. Unfortunately, after it has
  played, the game once again goes back to the company logos and title screen.<br>

  To fix that, the patch for overlay 334 has been made to only return the 0x11F after
  name entry, and the game''s first cutscene after the opening one now plays.</p>

  <p dir="auto">After going through the dialog boxes, the game''s main protagonist
  can now be moved in the overworld, right? Well, sort of.<br>

  The overworld is nothing but a black screen and a few icons at the screen corners.<br>

  The protagonist can be moved to the right for him to appear, and the background
  of Haidhia Lookout will shift in close to him as a flat texture.<br>

  Touching the bottom-left icon (or pressing the X button) will open the main menu,
  and can be navigated normally, but when exiting the menu, a battle against Dim Dragon
  will trigger.<br>

  The battle gets triggered because there''s still an instance of the overlay 334
  checksum which hasn''t been patched with the new one.<br>

  Patching the checksum instances found in the USA ROM has not removed the battle
  encounter, but it has been sucessfully removed in the European ROM.<br>

  Apparently, some checksum instances are encrypted along with the overlay''s code.<br>

  To remove the battle encounter in the USA ROM, the patch code has been made so that
  it looks for an instance of the checksum, once an overlay has loaded.</p>

  <p dir="auto">Furthermore, when I tried a save file which gets past the black area,
  some features wouldn''t work correctly, such as using Psynergy.<br>

  It would only work when one is assigned to either the L or R buttons.<br>

  Getting an item would also either appear as the wrong one, or crash the game.</p>

  <p dir="auto">The final step is to fix those remaining AP issues, and to do that,
  the patch code has been slightly reworked to not affect the checksum, but that alone
  will not fix it.<br>

  After some more looking into and patching, the patch code for overlay 335 has been
  ported over to 334.</p>

  <p dir="auto">For those who understand ASM code, here''s what nds-bootstrap does
  to the overlay code (offsets are for the USA/AUS region, but the patch works with
  other regions):</p>

  <p dir="auto"><strong>Overlay 335 (DSProtect v2.01s)</strong></p>

  <ol dir="auto">

  <li>At <code class="notranslate">0x021F8284</code>, change the <code class="notranslate">beq</code>
  instruction (<code class="notranslate">0A000005</code>) to <code class="notranslate">b</code>.</li>

  <li>At <code class="notranslate">0x021F82D8</code>, change the <code class="notranslate">ldr</code>
  instruction (<code class="notranslate">E59D1028</code>) to <code class="notranslate">mov
  r1, 0h</code>.</li>

  <li>At <code class="notranslate">0x021F82DC</code>, change the <code class="notranslate">ldr</code>
  instruction (<code class="notranslate">E59D0040</code>) to <code class="notranslate">mov
  r0, 0h</code>.</li>

  <li>Change instructions at <code class="notranslate">021F82E4</code> &amp; <code
  class="notranslate">021F82E8</code> to <code class="notranslate">nop</code>.</li>

  </ol>

  <p dir="auto"><strong>Overlay 334 (DSProtect v2.01)</strong></p>

  <ol dir="auto">

  <li>At <code class="notranslate">0x021F910C</code>, change the <code class="notranslate">beq</code>
  instruction (<code class="notranslate">0A00000E</code>) to <code class="notranslate">b</code>.</li>

  <li>At <code class="notranslate">0x021F91A8</code>, change the <code class="notranslate">ldr</code>
  instruction (<code class="notranslate">E59D102C</code>) to <code class="notranslate">mov
  r1, 0h</code>.</li>

  <li>At <code class="notranslate">0x021F91AC</code>, change the <code class="notranslate">ldr</code>
  instruction (<code class="notranslate">E59D0044</code>) to <code class="notranslate">mov
  r0, 0h</code>.</li>

  <li>Change instructions at <code class="notranslate">021F91B4</code> &amp; <code
  class="notranslate">021F91B8</code> to <code class="notranslate">nop</code>.</li>

  </ol>

  <p dir="auto">After all of this looking into and fixing/patching, <em>Golden Sun:
  Dark Dawn</em> is finally supported by nds-bootstrap!</p>

  <h3 dir="auto">In short</h3>

  <p dir="auto">The AP-fix that has been included with TWLMenu++ for a while was broken,
  so a new &amp; better AP-fix has been implemented into nds-bootstrap. It has taken
  8 days with lots of changes &amp; improvements to the code to ensure that everything
  was working properly.</p>'
updated: '2023-09-09T03:23:51Z'
version: v1.0.0
version_title: 'v1.0.0: Rise of The Sun'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.