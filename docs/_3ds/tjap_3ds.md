---
author: TogeToge & MarioGames
avatar: https://avatars.githubusercontent.com/u/176740851?v=4
categories:
- game
color: '#9e4d4d'
color_bg: '#803e3e'
created: '2024-07-27T07:58:35Z'
description: TJAPlayer for 3DS - Music game of the TJA file.
download_page: https://github.com/LuMariGames/TJAP_3DS/releases
downloads:
  TJAP_3DS.3dsx:
    size: 9465924
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.8.1/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 9753536
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.8.1/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v1.8.2
  downloads:
    TJAP_3DS.3dsx:
      size: 9467592
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.8.2/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 9753536
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.8.2/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>爆弾音符の実装<br>

    <code class="notranslate">C</code>という文字を譜面の中に記述すると爆弾音符が出現します。<br>

    正確に叩いても判定文字は現れませんが不可判定になり、無視する事で対処出来ます。</li>

    </ul>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Bomb Note Implementation<br>

    Writing the letter <code class="notranslate">C</code> in a Chart will cause a
    bomb note to appear.<br>

    Even if you hit it correctly, the Judgment Text won''t appear, but it will still
    be judged as a BAD note, which you can ignore.</li>

    </ul>'
  update_notes_md: '## チェンジログ

    - 爆弾音符の実装

    `C`という文字を譜面の中に記述すると爆弾音符が出現します。

    正確に叩いても判定文字は現れませんが不可判定になり、無視する事で対処出来ます。


    ## Changelog

    - Bomb Note Implementation

    Writing the letter `C` in a Chart will cause a bomb note to appear.

    Even if you hit it correctly, the Judgment Text won''t appear, but it will still
    be judged as a BAD note, which you can ignore.'
  updated: '2025-09-22T04:43:17Z'
  version: v1.8.2
  version_title: TJAPlayer for 3DS v1.8.2
qr:
  TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/tjap_3ds-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-2.png
source: https://github.com/LuMariGames/TJAP_3DS
stars: 8
systems:
- 3DS
title: TJAP_3DS
unique_ids:
- '0xB7655'
update_notes: '<h2 dir="auto">チェンジログ</h2>

  <ul dir="auto">

  <li><code class="notranslate">#GOGOSTART</code>等の命令のタイミングが一致していなかったのを修正</li>

  <li>譜面の長さに応じて配点が正しく計算出来なくなる不具合の修正</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Fixed inconsistent timing for commands such as <code class="notranslate">#GOGOSTART</code>.</li>

  <li>Fixed a bug that caused points to be calculated incorrectly depending on the
  length of charts.</li>

  </ul>'
updated: '2025-09-20T05:14:02Z'
version: v1.8.1
version_title: TJAPlayer for 3DS v1.8.1
wiki: https://github.com/LuMariGames/TJAP_3DS/wiki
---
TJAPlayer for 3DSを約2年ぶりにTogeToge公認の上、更新しました。
This software is produced under the official authorization of TogeToge.

・太鼓タワーと段位道場の実装
・一部オプションの追加
・その他一部の不具合修正

・Implementation of Taiko Tower and Rank Dojo
・Addition of some options
・FIXES OF OTHER FAILURE