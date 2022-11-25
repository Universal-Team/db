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
    size: 589115
    size_str: 575 KiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.67.0/nds-bootstrap.7z
  nds-bootstrap.zip:
    size: 1386853
    size_str: 1 MiB
    url: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.67.0/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://db.universal-team.net/assets/images/icons/nds-bootstrap.png
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
update_notes: '<p dir="auto">Included in <a href="https://github.com/DS-Homebrew/TWiLightMenu/releases/tag/v25.6.0"><strong>TW</strong>i<strong>L</strong>ight
  Menu++ v25.6.0</a></p>

  <p dir="auto">Instructions:</p>

  <ol dir="auto">

  <li>Download the <code class="notranslate">.7z</code> file.</li>

  <li>Extract the nds-bootstrap <code class="notranslate">.nds</code> and <code class="notranslate">.ver</code>
  files, to <code class="notranslate">root:/_nds</code>.</li>

  </ol>

  <h3 dir="auto">What''s new?</h3>

  <h4 dir="auto">DS &amp; DS lite (B4DS mode)</h4>

  <ul dir="auto">

  <li>Added support for 24 more DSiWare titles, bringing the amount of supported DSiWare
  on DS/DS lite (not counting debug consoles), up to a grand total of 200 titles!

  <ul dir="auto">

  <li>Scroll down to see which titles are now supported.</li>

  <li>Click &gt;<a href="https://github.com/DS-Homebrew/TWiLightMenu/blob/79602be985add9d24562b532bb216b0b1792a241/universal/include/compatibleDSiWareMap.h">here</a>&lt;
  for the full list of supported titles.</li>

  </ul>

  </li>

  <li>A few DSiWare can now read the TWL font table!

  <ul dir="auto">

  <li>Currently, only <em>4 Travellers</em>, <em>Chuck E. Cheese''s Arcade Room</em>,
  <em>Chuck E. Cheese''s Alien Defense Force</em>, <em>Flashlight</em>, <em>Gunjin
  Shougi</em>, and <em>Sea Battle</em> use it (mainly for the help/instruction manual
  screen).</li>

  <li>Place <code class="notranslate">TWLFontTable.dat</code> (Non-CHN/KOR) in <code
  class="notranslate">sd:/_nds/nds-bootstrap/</code>.</li>

  </ul>

  </li>

  <li>FAT cluster cache is now compressed to reduce heap shrink.

  <ul dir="auto">

  <li>Should increase game compatibility, as well as fix support for SD cards with
  cluster size less than 32KB.</li>

  </ul>

  </li>

  </ul>

  <h4 dir="auto">DSi &amp; 3DS</h4>

  <ul dir="auto">

  <li>If booted from flashcard, nds-bootstrap data will now be read from or saved
  to the flashcard.</li>

  <li><strong>DSi only:</strong> FAT cluster cache is now compressed to reduce heap
  shrink while in DSi mode.

  <ul dir="auto">

  <li>Should reduce crashes in some DSi-Enhanced games.</li>

  </ul>

  </li>

  <li>When booting a TWL title from a DS flashcard booted with unlocked SCFG access,
  DSi BIOS dumps are now loaded from <code class="notranslate">sd:/_nds/</code> in
  order to fix some bugs such as WPA1/2 crashing the console.

  <ul dir="auto">

  <li>Either <code class="notranslate">bios9i.bin</code> &amp; <code class="notranslate">bios7i.bin</code>,
  or <code class="notranslate">bios9i_part1.bin</code> &amp; <code class="notranslate">bios7i_part2.bin</code>
  (the <code class="notranslate">part</code> files are dumped by TWLMenu++) are used.</li>

  </ul>

  </li>

  <li>Added external <code class="notranslate">TWLFontTable.dat</code> loading, needed
  for some out of region DSiWare to boot!

  <ul dir="auto">

  <li>Place <code class="notranslate">TWLFontTable.dat</code> (Non-CHN/KOR) in <code
  class="notranslate">sd:/_nds/nds-bootstrap/</code>.</li>

  <li>Place CHN (iQue) <code class="notranslate">TWLFontTable.dat</code> renamed to
  <code class="notranslate">CHNFontTable.dat</code> in <code class="notranslate">sd:/_nds/nds-bootstrap/</code>.</li>

  <li>Place KOR <code class="notranslate">TWLFontTable.dat</code> renamed to <code
  class="notranslate">KORFontTable.dat</code> in <code class="notranslate">sd:/_nds/nds-bootstrap/</code>.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <h4 dir="auto">DS &amp; DS lite (B4DS mode)</h4>

  <ul dir="auto">

  <li>Fixed <em>Nintendo DSi + Internet</em> (USA) not booting.</li>

  </ul>

  <h4 dir="auto">DSi &amp; 3DS</h4>

  <ul dir="auto">

  <li>Fixed TWL titles not booting in DSi mode from a DS flashcard booted with unlocked
  SCFG access.</li>

  <li>Fixed <em>Kim Possible: Kimmunicator</em> not booting.</li>

  <li>Fixed in-game menu not controllable when red screen error occurred in DSiWare
  booted from SD.</li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite</h3>

  <ul dir="auto">

  <li>4 Travellers: Play French</li>

  <li>4 Travellers: Play Spanish</li>

  <li>505 Tangram</li>

  <li>Bloons TD

  <ul dir="auto">

  <li>Audio is disabled on non-debug consoles to fit within RAM limitations</li>

  <li>Does not save</li>

  </ul>

  </li>

  <li>Captain Sub (GO Series)</li>

  <li>Fall in the Dark

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Farm Frenzy</li>

  <li>Fizz</li>

  <li>Fuuu! Dairoujou Kai</li>

  <li>Maestro! Green Groove

  <ul dir="auto">

  <li>Does not save</li>

  </ul>

  </li>

  <li>Music on: Drums</li>

  <li>My Aquarium: Seven Oceans</li>

  <li>My Asian Farm</li>

  <li>My Australian Farm</li>

  <li>My Exotic Farm</li>

  <li>My Farm</li>

  <li>Pop+ Solo</li>

  <li>Puffins: Let''s Fish!</li>

  <li>Puffins: Let''s Race!</li>

  <li>Sea Battle</li>

  <li>Simply Mahjong</li>

  <li>Simply Minesweeper</li>

  <li>Simply Solitaire</li>

  <li>Simply Sudoku</li>

  </ul>

  <h3 dir="auto">DSiWare titles now supported on DS &amp; DS lite debug consoles only</h3>

  <ul dir="auto">

  <li>Bloons TD 4

  <ul dir="auto">

  <li>Audio is disabled to fit within RAM limitations</li>

  </ul>

  </li>

  <li>Shawn Johnson Gymnastics</li>

  </ul>'
updated: '2022-11-25T02:27:21Z'
version: v0.67.0
version_title: 'v0.67.0: Thanksgiving release (2022)'
website: https://wiki.ds-homebrew.com/nds-bootstrap/
wiki: https://wiki.ds-homebrew.com/nds-bootstrap/
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.