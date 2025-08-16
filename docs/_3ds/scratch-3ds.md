---
author: NateXS
avatar: https://avatars.githubusercontent.com/u/149607394?v=4
categories:
- emulator
- utility
color: '#b2a2a3'
color_bg: '#807475'
created: '2025-05-01T16:11:42Z'
description: Play Scratch games on your 3DS!
download_page: https://github.com/NateXS/Scratch-3DS/releases
downloads:
  Scratch.3dsx:
    size: 3166760
    size_str: 3 MiB
    url: https://github.com/NateXS/Scratch-Everywhere/releases/download/0.17/Scratch.3dsx
github: NateXS/Scratch-3DS
icon: https://raw.githubusercontent.com/NateXS/Scratch-3DS/refs/heads/main/gfx/icon.png
image: https://raw.githubusercontent.com/NateXS/Scratch-3DS/refs/heads/main/gfx/logo.png
image_length: 39081
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
screenshots:
- description: Screenshot1
  url: https://db.universal-team.net/assets/images/screenshots/scratch-3ds/screenshot1.png
- description: Screenshot2
  url: https://db.universal-team.net/assets/images/screenshots/scratch-3ds/screenshot2.png
- description: Screenshot3
  url: https://db.universal-team.net/assets/images/screenshots/scratch-3ds/screenshot3.png
source: https://github.com/NateXS/Scratch-Everywhere
stars: 266
systems:
- 3DS
title: Scratch 3DS
update_notes: '<h2>New Features</h2>

  <p><strong>Scratch Everywhere!</strong></p>

  <ul>

  <li>The name has been changed to Scratch Everywhere!</li>

  <li>That''s Scratch Everywhere! with the exclamation point btw..</li>

  <li>It made 0 sense to keep the name Scratch 3DS as this is now on 5 different platforms...</li>

  <li>speaking of which...</li>

  </ul>

  <p><strong>Switch Port!</strong></p>

  <ul>

  <li>For all 1.5 people who own a modded Switch, you can now enjoy Scratch games!</li>

  <li>Via pull request (#97)!</li>

  </ul>

  <p><strong>All new main menu screen!</strong></p>

  <ul>

  <li>The Main Menu has gone through a huge refactor under the hood!</li>

  <li>It should be a smoother and better experience overall!</li>

  <li>It''s still a work in progress, but now it should be a little easier to add
  stuff to it in the future!</li>

  </ul>

  <p><strong>Custom controls!</strong></p>

  <ul>

  <li>In the Project menu is a new option to remap the controls of any project!</li>

  <li>Control mappings get loaded and saved to <code class="notranslate">scratch-everywhere/''project_name''.json</code></li>

  <li>

  <ul>

  <li>Wii U is <code class="notranslate">sd:/wiiu/scratch-wiiu/''project_name.json''</code></li>

  </ul>

  </li>

  </ul>

  <h2>Runtime changes</h2>

  <ul>

  <li>Sprite fencing has been implemented!</li>

  <li>

  <ul>

  <li>Can be disabled with TurboWarp or other Scratch mods.</li>

  </ul>

  </li>

  <li>The <code class="notranslate">Stop ''All''</code> block now takes you back to
  the Main Menu instead of the homebrew menu!</li>

  <li>

  <ul>

  <li>Note: The Wii U will still exit the app, as it would freeze when going back
  to the Main Menu for some reason.</li>

  </ul>

  </li>

  <li>Booleans (anything set to <code class="notranslate">true</code> or <code class="notranslate">false</code>)
  now doesn''t get set to <code class="notranslate">1</code> or <code class="notranslate">0</code>
  by the runtime mistakenly</li>

  <li>Fixed a couple of crashes that could happen while loading</li>

  <li>Custom blocks with no definition now works as intended</li>

  <li>

  <ul>

  <li>Logging blocks created by Scratch Addons Debugging Addon can now be used.</li>

  </ul>

  </li>

  <li>The runtime can now be compiled with <code class="notranslate">ENABLE_AUDIO=0</code>.</li>

  <li>

  <ul>

  <li>For the 3DS, this means smaller file size, and you no longer need SDL2 to compile.</li>

  </ul>

  </li>

  </ul>

  <h2>3DS Changes</h2>

  <ul>

  <li>Fixed crash when closing the app</li>

  <li>Fixed audio cracking issue</li>

  <li>Sprites are no longer rendered in fractional positions, fixing some image weirdness</li>

  <li>Changed image filtering from <code class="notranslate">nearest</code> to <code
  class="notranslate">linear</code></li>

  <li>

  <ul>

  <li>This fixes the image fuzziness and weirdness issues, with a tradeoff to some
  images looking slightly blurry. I might add a filtering option to the Main Menu
  in the future.</li>

  </ul>

  </li>

  </ul>

  <h2>Wii Changes</h2>

  <ul>

  <li>Fixed projects not showing up in Main Menu</li>

  <li>Fixed images sometimes not being able to load</li>

  <li>[Quick Edit 16 Aug 2025] Fixed meta.xml showing the wrong date</li>

  </ul>

  <h2>Wii U Changes</h2>

  <ul>

  <li>Fixed projects not showing up in Main Menu</li>

  </ul>

  <h2>About Gamecube</h2>

  <ul>

  <li>Currently on Gamecube there is no way for you to play any Scratch projects using
  the Main Menu. This is a bug that I''ve been trying to investigate, and have had
  no luck in finding anyone who is knowledgeable on the situation. So for now, I will
  not be including the Gamecube release here, and you will need to compile it yourself
  with a Scratch project in the <code class="notranslate">RomFS</code>. Instructions
  how are in the README.  Gamecube release will come back once the bug has been fixed.</li>

  </ul>'
updated: '2025-08-16T00:06:30Z'
version: '0.17'
version_title: Beta Build 17
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!