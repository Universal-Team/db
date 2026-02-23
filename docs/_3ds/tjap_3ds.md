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
    size: 9730084
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.1.0/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 9929664
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.1.0/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v2.1.1
  downloads:
    TJAP_3DS.3dsx:
      size: 9785916
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.1.1/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 9970624
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.1.1/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>段位道場モードの新条件「最大コンボ数」の実装</li>

    <li>一部の不具合修正と仕様変更</li>

    </ul>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Implemented new condition "MAX Combo" in Dan-i Dojo mode</li>

    <li>Some bug fixes and specification changes</li>

    </ul>'
  update_notes_md: '## チェンジログ

    - 段位道場モードの新条件「最大コンボ数」の実装

    - 一部の不具合修正と仕様変更


    ## Changelog

    - Implemented new condition "MAX Combo" in Dan-i Dojo mode

    - Some bug fixes and specification changes'
  updated: '2026-02-22T21:50:44Z'
  version: v2.1.1
  version_title: TJAPlayer for 3DS v2.1.1
qr:
  TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/tjap_3ds-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-2.png
source: https://github.com/LuMariGames/TJAP_3DS
stars: 12
systems:
- 3DS
title: TJAP_3DS
unique_ids:
- '0xB7655'
update_notes: '<h2 dir="auto">チェンジログ</h2>

  <ul dir="auto">

  <li>ダミーノーツの実装<br>

  <code class="notranslate">#DUMMYSTART</code>を<code class="notranslate">#BARLINEON</code>の様に使うと叩いてもスルーされるノーツが出ます。<br>

  有効化されてる間はスコアの計算や判定等もされません。<br>

  無効化する際は<code class="notranslate">#DUMMYEND</code>を使用して下さい。</li>

  <li><code class="notranslate">#JPOSSCROLL (Travel_time(float)) (position(int)) (direction(int))</code>の仮実装</li>

  <li>譜面終了時の処理を一部変更</li>

  <li>コンボアニメーションの追加</li>

  <li>一部テキストの視認性向上</li>

  <li><code class="notranslate">#LEVELHOLD</code>が正しく動作していなかった不具合を修正</li>

  </ul>

  <h2 dir="auto">changelog</h2>

  <ul dir="auto">

  <li>Implementation of Dummy Notes<br>

  If you use <code class="notranslate">#DUMMYSTART</code> like <code class="notranslate">#BARLINEON</code>,
  you will get notes that will be passed even if you hit it.<br>

  While it is activated, the score will not be calculated or judged.<br>

  Please use <code class="notranslate">#DUMMYEND</code> to disable it.</li>

  <li>Temporary implementation of <code class="notranslate">#JPOSSCROLL Travel_time(float)
  position(int) direction(int)</code></li>

  <li>Partial change in the processing at the end of the score</li>

  <li>Adding combo animations</li>

  <li>Improved visibility of some texts</li>

  <li>Fixed a bug where <code class="notranslate">#LEVELHOLD</code> was not working
  properly.</li>

  </ul>'
updated: '2026-01-19T06:15:58Z'
version: v2.1.0
version_title: TJAPlayer for 3DS v2.1.0
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