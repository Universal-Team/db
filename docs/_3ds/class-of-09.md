---
author: the gabe
avatar: https://avatars.githubusercontent.com/u/52845476?v=4
categories:
- game
color: '#747664'
color_bg: '#747664'
created: '2025-09-14T09:53:37Z'
description: 3DS port of the visual novel Class of '09
download_page: https://github.com/Bilbard/classof3ds/releases
downloads:
  classof3ds.3dsx:
    size: 186356820
    size_str: 177 MiB
    url: https://github.com/Bilbard/classof3ds/releases/download/v1.2/classof3ds.3dsx
  classof3ds.cia:
    size: 185840640
    size_str: 177 MiB
    url: https://github.com/Bilbard/classof3ds/releases/download/v1.2/classof3ds.cia
github: Bilbard/classof3ds
icon: https://raw.githubusercontent.com/Bilbard/classof3ds/refs/heads/master/3ds/icon.png
image: https://raw.githubusercontent.com/Bilbard/classof3ds/refs/heads/master/3ds/widebanner.png
image_length: 46438
layout: app
prerelease:
  download_page: https://github.com/Bilbard/classof3ds/releases/tag/v1.9
  downloads:
    classof3dsru.3dsx:
      size: 237896860
      size_str: 226 MiB
      url: https://github.com/Bilbard/classof3ds/releases/download/v1.9/classof3dsru.3dsx
    classof3dsru.cia:
      size: 236884992
      size_str: 225 MiB
      url: https://github.com/Bilbard/classof3ds/releases/download/v1.9/classof3dsru.cia
  qr:
    classof3dsru.cia: https://db.universal-team.net/assets/images/qr/prerelease/classof3dsru-cia.png
  update_notes: '<h1 dir="auto">v1.9</h1>

    <p dir="auto">The second game has reached an important milestone, as now the whole
    game is playable from top to bottom without missing anything crucial. Once the
    second game is ready to release properly, both versions will release at the same
    time under the same version, v2.0.</p>

    <p dir="auto">It''s still rough around the edges and is missing almost all of
    the special scene effects (eg. indoor smoke cloud, the laptop), almost all of
    the black fading, as well as missing a lot of emotion changes and even the ambience,
    but the scenes all still play out fine and allow you to enjoy the game.</p>

    <p dir="auto">I expect there will be bugs so please don''t report any bugs for
    this version. I promise you, if it''s a bug, right now I''m aware of it.</p>'
  update_notes_md: '# v1.9

    The second game has reached an important milestone, as now the whole game is playable
    from top to bottom without missing anything crucial. Once the second game is ready
    to release properly, both versions will release at the same time under the same
    version, v2.0.


    It''s still rough around the edges and is missing almost all of the special scene
    effects (eg. indoor smoke cloud, the laptop), almost all of the black fading,
    as well as missing a lot of emotion changes and even the ambience, but the scenes
    all still play out fine and allow you to enjoy the game.


    I expect there will be bugs so please don''t report any bugs for this version.
    I promise you, if it''s a bug, right now I''m aware of it.'
  updated: '2026-03-27T16:43:06Z'
  version: v1.9
  version_title: v1.9-prerelease
qr:
  classof3ds.cia: https://db.universal-team.net/assets/images/qr/classof3ds-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/class-of-09/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/class-of-09/gameplay-2.png
- description: Gameplay 3
  url: https://db.universal-team.net/assets/images/screenshots/class-of-09/gameplay-3.png
- description: Title screen
  url: https://db.universal-team.net/assets/images/screenshots/class-of-09/title-screen.png
source: https://github.com/Bilbard/classof3ds
stars: 11
systems:
- 3DS
title: Class of '09
unique_ids:
- '0xFA945'
update_notes: '<h1 dir="auto">v1.2</h1>

  <p dir="auto">With the second game around the corner, it''s time to release another
  feature update for the first game. I haven''t extensively tested the changes in
  the first game, but nothing catastrophic should happen.</p>

  <p dir="auto">In the process of finishing the second game, the engine has received
  the following notable changes:</p>

  <ul dir="auto">

  <li>The audio quality should be much better. In order to achieve this stereo sound
  was sacrificed, but there are only a couple scenes that make use of it, and it''s
  a very subtle effect. I think it''s worth it given how crisp everything sounds now.
  This also comes with a slight file size increase.</li>

  <li>The improved audio system along with other changes allows old 3DS models to
  run the game even smoother, to the point that I''m now considering allowing 3D functionality
  at 60 FPS by default on old models. This functionality can still be forced on via
  the argv trick discussed in v1.1.</li>

  <li>For 3DS consoles with washed out screens, I''ve implemented a filter system
  that can help mitigate the loss of detail, especially in things like faces. By default
  it is disabled and must be enabled by configuring the "screen_augmenter" argument.
  A profile I tuned for my launch model 3DS is supplied in this repository, which
  is just a 4 byte file with a red, green, blue and alpha control. For the best results
  you may have to make your own. When enabled, it can be toggled on and off by pressing
  select and start at the same time, mostly anywhere, and will always turn on at launch.</li>

  <li>That rare video crash bug is probably actually fixed now. Fingers crossed?</li>

  </ul>

  <p dir="auto">This is still not the end of performance gains for the first game,
  though the performance gains will mostly be in load times at this point.</p>

  <p dir="auto">I can''t figure out how to have Github display a release and a prerelease
  build at the same time, so check out the prerelease build of the second game, which
  can be found <a href="https://github.com/Bilbard/classof3ds/releases/tag/v1.9">here</a>.</p>'
updated: '2026-03-27T16:32:30Z'
version: v1.2
version_title: v1.2
---
A demake/port of the visual novel "Class of '09" to the 3DS. 

More than feature complete, you miss nothing playing this version over the PC version.