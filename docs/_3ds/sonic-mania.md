---
author: SaturnSH2x2
avatar: https://avatars.githubusercontent.com/u/18273084?v=4
categories:
- game
color: '#989e7f'
color_bg: '#7b8066'
created: '2022-08-16T22:06:31Z'
description: Sonic Mania (n3DS only)
download_page: https://github.com/SaturnSH2x2/RSDKv5-Decompilation/releases
downloads:
  SonicMania.3dsx:
    size: 3015400
    size_str: 2 MiB
    url: https://github.com/SaturnSH2x2/RSDKv5-Decompilation/releases/download/v1.1.0/SonicMania.3dsx
  SonicMania.cia:
    size: 2268096
    size_str: 2 MiB
    url: https://github.com/SaturnSH2x2/RSDKv5-Decompilation/releases/download/v1.1.0/SonicMania.cia
github: SaturnSH2x2/RSDKv5-Decompilation
icon: https://raw.githubusercontent.com/SaturnSH2x2/RSDKv5-Decompilation/3ds-main/3ds/48x48.png
image: https://raw.githubusercontent.com/SaturnSH2x2/RSDKv5-Decompilation/3ds-main/3ds/banner.png
image_length: 61351
layout: app
license: other
license_name: Other
qr:
  SonicMania.cia: https://db.universal-team.net/assets/images/qr/sonicmania-cia.png
screenshots:
- description: Green hill
  url: https://db.universal-team.net/assets/images/screenshots/sonic-mania/green-hill.png
- description: Mirage saloon
  url: https://db.universal-team.net/assets/images/screenshots/sonic-mania/mirage-saloon.png
- description: Special stage
  url: https://db.universal-team.net/assets/images/screenshots/sonic-mania/special-stage.png
- description: Studiopolis
  url: https://db.universal-team.net/assets/images/screenshots/sonic-mania/studiopolis.png
script_message: 'Note: You will need "Data.rsdk" from

  an official version in

  "/3ds/SonicMania" to play the game.'
source: https://github.com/SaturnSH2x2/RSDKv5-Decompilation
stars: 100
systems:
- 3DS
title: Sonic Mania
unique_ids:
- '0x308200'
update_notes: '<p dir="auto">It''s been a while.</p>

  <p dir="auto">Changes since the last release:</p>

  <ul dir="auto">

  <li>Game now runs on engine version v5U, however, without v3/v4 Legacy support.
  This engine version is referred to as v5C internally.</li>

  <li>Dev menu now displays extra information regarding memory usage, as well as if
  the game is running on a N3DS.</li>

  <li>Audio thread now runs on core 1, with support for asynchronous file loading,
  alleviating microloads during gameplay and resulting in speedup in certain sections
  (start of Studiopolis Act 2, parts of Flying Battery Act 1). Additionally, the game
  no longer suffers from delayed audio.</li>

  <li>Engine now supports loading assets from an external RomFS file.</li>

  <li>Loading times improved significantly while using the Data file. Thanks to <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/davidgfnet/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/davidgfnet">@davidgfnet</a>
  for using setvbuf on Data file accesses. Additionally, all static object files and
  sprite bin files are cached. Loading times are ~30-40 seconds on initial boot, and
  ~5-10 seconds on stage load, however, YMMV.</li>

  <li>Port now incorporates more or less the latest version of both the RSDKv5 decomp
  and Mania decomp (thanks <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Mefiresu/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Mefiresu">@Mefiresu</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/c08oprkiua/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/c08oprkiua">@c08oprkiua</a>).</li>

  <li>Game now <em>boots</em> on O3DS. However, don''t expect full-speed frame rates.
  (thanks <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/smb123w64gb/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/smb123w64gb">@smb123w64gb</a>)
  A Citro2D/3D backend is still planned to get performance up to speed.</li>

  </ul>

  <p dir="auto">Installation process is the same as before. Copy the <code class="notranslate">Data.rsdk</code>
  or extracted <code class="notranslate">Data</code> folder to <code class="notranslate">/3ds/SonicMania</code>
  on your 3DS''s SD Card.</p>'
updated: '2025-05-08T00:17:23Z'
version: v1.1.0
version_title: v1.1.0
website: https://gbatemp.net/threads/release-sonic-mania-3ds-port.618771/
---
