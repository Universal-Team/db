---
author: SprtnDio
avatar: https://avatars.githubusercontent.com/u/183821772?v=4
categories:
- utility
color: '#444637'
color_bg: '#444637'
created: '2026-03-13T00:19:39Z'
description: Drawing and text Chat Rooms.
download_page: https://github.com/SprtnDio/NoteRoom/releases
downloads:
  NoteRoom.3dsx:
    size: 4980604
    size_str: 4 MiB
    url: https://github.com/SprtnDio/NoteRoom/releases/download/v3.5/NoteRoom.3dsx
  NoteRoom.cia:
    size: 5272512
    size_str: 5 MiB
    url: https://github.com/SprtnDio/NoteRoom/releases/download/v3.5/NoteRoom.cia
github: SprtnDio/NoteRoom
icon: https://raw.githubusercontent.com/SprtnDio/NoteRoom/main/icon.png
image: https://raw.githubusercontent.com/SprtnDio/NoteRoom/refs/heads/main/banner.png
image_length: 37065
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  NoteRoom.cia: https://db.universal-team.net/assets/images/qr/noteroom-cia.png
source: https://github.com/SprtnDio/NoteRoom
stars: 4
systems:
- 3DS
title: NoteRoom
unique_ids:
- '0xF9E3'
update_notes: '<h1 dir="auto">🌟 NoteRoom v3.5 Alpha – Release Notes</h1>

  <p dir="auto">Welcome to <strong>NoteRoom v3.5 Alpha</strong>! This is one of the
  largest updates yet, introducing doubled island and interior building space, block
  rotation, uncapped 60 FPS performance, an all-new HUD Overlay Studio, seamless dimensional
  portals, and persistent settings.</p>

  <hr>

  <h3 dir="auto">🗺️ Doubled Building Space (88x88 Islands &amp; 19x19 Interiors)</h3>

  <ul dir="auto">

  <li><strong>Massive 88x88 Islands:</strong> The buildable area has been more than
  doubled (from 3,600 to <strong>7,744 tiles</strong>)! Enjoy vast new space for towns,
  oceans, roads, and landscape creations.</li>

  <li><strong>Spacious 19x19 House Interiors:</strong> Interior rooms have expanded
  from 13x13 to <strong>19x19 tiles</strong>, giving you over twice the space to design
  mansions, taverns, dungeons, and shops.</li>

  <li><strong>100% Backward Compatible:</strong> All existing 60x60 player islands
  and Town Square maps are preserved and automatically expanded into the new territory
  without any data loss.</li>

  <li><strong>Complete Interior Floor Sync:</strong> Fixed interior tile synchronization
  so custom floors (wood, marble, carpet, or custom tiles) sync live and reliably
  for all players entering your house.</li>

  </ul>

  <hr>

  <h3 dir="auto">🔄 Block Rotation in Build Mode ([L] / [R])</h3>

  <ul dir="auto">

  <li><strong>Rotate Any Tile:</strong> Press <strong><code class="notranslate">[L]</code></strong>
  or <strong><code class="notranslate">[R]</code></strong> in Build Mode to rotate
  the currently selected block in 90-degree steps (<strong>0°, 90°, 180°, 270°</strong>)!</li>

  <li><strong>Live Menu Preview:</strong> Tiles in the Build Menu rotate in real time
  as you adjust the angle.</li>

  <li>Perfect for aligning corner walls, road curves, chair orientations, carpet borders,
  and angled water features.</li>

  </ul>

  <hr>

  <h3 dir="auto">⚡ True 60 FPS &amp; New 3DS 804 MHz Turbo</h3>

  <ul dir="auto">

  <li><strong>Uncapped 60 FPS:</strong> Removed internal VBlank bottlenecks—the game
  engine now runs at a silky-smooth, fluid <strong>60 frames per second</strong>.</li>

  <li><strong>New 3DS Hardware Boost:</strong> Automatically unlocks the <strong>804
  MHz CPU clock</strong> and extra L2 cache on New 3DS / New 2DS XL consoles for up
  to 3x processing throughput. (Old 3DS models remain completely supported and stable
  at stock speeds).</li>

  <li><strong>Zero SD Lag Spikes:</strong> Optimized map caching during online multiplayer
  so disk operations no longer cause periodic framerate hitches while people build.</li>

  </ul>

  <hr>

  <h3 dir="auto">📊 Performance &amp; HUD Overlay Studio</h3>

  <ul dir="auto">

  <li><strong>2-Page Settings Menu:</strong> Open <strong><code class="notranslate">[START]
  -&gt; SETTINGS &amp; FX</code></strong> and switch between <code class="notranslate">Page
  1: World &amp; FX</code> and <code class="notranslate">Page 2: HUD Studio</code>
  with <code class="notranslate">[L] / [R]</code> or Touch!</li>

  <li><strong>Modular Metrics (Individually Toggleable):</strong>

  <ul dir="auto">

  <li>🟢 <strong>Live FPS Counter</strong> (with dynamic green/yellow/red color-coding)</li>

  <li>⚡ <strong>Active CPU Clock Speed</strong> (real-time active MHz vs. hardware
  maximum)</li>

  <li>📈 <strong>CPU &amp; GPU Load %</strong></li>

  <li>💾 <strong>RAM &amp; Heap Usage in MB</strong></li>

  </ul>

  </li>

  <li><strong>Full Visual Customization:</strong>

  <ul dir="auto">

  <li><strong>5 Screen Anchor Positions:</strong> Top-Left, Top-Center, Top-Right,
  Bottom-Left, or Bottom-Right.</li>

  <li><strong>Smart Auto-Dodge:</strong> The HUD automatically adjusts position when
  notification banners appear at the top or chat messages appear at the bottom, preventing
  overlap.</li>

  <li><strong>Colors &amp; Opacity:</strong> Choose from multiple text colors (including
  Dynamic &amp; Live Rainbow), text opacities, and background box styles (from Dark
  Navy to 0% transparent).</li>

  </ul>

  </li>

  <li><strong>Permanent Settings Saving:</strong> All preferences are now automatically
  saved to <code class="notranslate">settings.cfg</code> on your SD card and remembered
  across game restarts.</li>

  </ul>

  <hr>

  <h3 dir="auto">🌀 Dimensional Portal Network &amp; Travel Rift</h3>

  <ul dir="auto">

  <li><strong>Interactive Time &amp; Space Transit:</strong> When stepping into a
  linked portal, players are immediately pulled into a cosmic transition dimension
  while the destination island loads in the background, eliminating awkward map pops.</li>

  <li><strong>Ultra-Fast Network Transfer:</strong> Rewritten map sync protocol using
  compressed streaming—islands now download up to <strong>70x faster</strong>, allowing
  instantaneous travel even on weak Wi-Fi connections.</li>

  <li><strong>Persistent Host Rights:</strong> Entering your island via portals correctly
  recognizes your hardware identity, guaranteeing full island ownership and building
  permissions.</li>

  </ul>

  <hr>

  <h3 dir="auto">🔮 Spell Wheel &amp; Fantasy Progression</h3>

  <ul dir="auto">

  <li><strong>Universal Spell Wheel (<code class="notranslate">[Y]</code>):</strong>
  Pressing <code class="notranslate">[Y]</code> in the 2D World View now reliably
  opens the radial Spell Wheel for all players.</li>

  <li><strong>7 Progression-Locked Player Spells:</strong> Advance through the new
  Fantasy Ranks (<em>Wanderer, Squire, Apprentice, Acolyte, Ranger, Mage, Sorcerer,
  etc.</em>) to unlock abilities like <em>Recall</em>, <em>Fairy Wisp Light</em>,
  <em>Heart Fountain</em>, <em>Wind Sprint</em>, <em>Fireworks Show</em>, <em>Slime
  Disguise</em>, and <em>Astral Step</em>.</li>

  <li><strong>Rebalanced Wind Sprint:</strong> Clearly separated speed tiers for natural
  walking, standard <code class="notranslate">[B]</code> running, and high-velocity
  wind sprinting.</li>

  <li><strong>Admin Wheel Toggle:</strong> Admins can tap the center node of the wheel
  to switch between Player Spells and Admin Spells (Tornado, Lightning Blink, Stealth,
  Aura, Summon, Teleport To, and Void Prison).</li>

  <li><strong>Visual Aura Independence:</strong> Spell auras (wisps, hearts, wind
  trails) now layer independently so players always retain their chosen character
  sprite.</li>

  </ul>

  <h3 dir="auto">Much more is coming...</h3>'
updated: '2026-10-31T01:27:05Z'
version: v3.5
version_title: NoteRoom v3.5 Alpha
---
NoteRoom is a real-time online drawing and text Chatroom messenger for the Nintendo 2/3DS, inspired by a well known chatroom. Connect globally across themed, dynamic lobbies, share hand-drawn doodles, and view live user counts.