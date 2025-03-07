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
    size: 1442920
    size_str: 1 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.5.0/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 1766336
    size_str: 1 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.5.0/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v1.5.1
  downloads:
    TJAP_3DS.3dsx:
      size: 1442932
      size_str: 1 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.5.1/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 1766336
      size_str: 1 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.5.1/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>演奏中に発生するカクつきの修正</li>

    </ul>

    <p dir="auto">多分これが最後のアップデートになります。約8ヶ月間ありがとうございました。<br>

    今後はTouch Keysの開発を進めて行きます。</p>

    <h2 dir="auto">Change log</h2>

    <ul dir="auto">

    <li>Correction of the kaku that occurs during the performance.</li>

    </ul>

    <p dir="auto">This will probably be the last update. Thank you for about 8 months.<br>

    From now on, we will continue to develop Touch Keys.</p>'
  update_notes_md: "## チェンジログ\n - 演奏中に発生するカクつきの修正\n\n多分これが最後のアップデートになります。約8ヶ月間ありがとうございました。\n\
    今後はTouch Keysの開発を進めて行きます。\n\n## Change log\n - Correction of the kaku that occurs\
    \ during the performance.\n\nThis will probably be the last update. Thank you\
    \ for about 8 months.\nFrom now on, we will continue to develop Touch Keys."
  updated: '2025-03-07T00:08:59Z'
  version: v1.5.1
  version_title: 【Last Update】TJAPlayer for 3DS v1.5.1
qr:
  TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/tjap_3ds-cia.png
source: https://github.com/LuMariGames/TJAP_3DS
stars: 2
systems:
- 3DS
title: TJAP_3DS
unique_ids:
- '0xB7655'
update_notes: '<h2 dir="auto">チェンジログ</h2>

  <ul dir="auto">

  <li>上画面下部に出る踊り子の実装<br>

  dancer.t3x と 設定済みの config.json を以下のように置けば出来ます。</li>

  </ul>

  <pre class="notranslate"><code class="notranslate">sdmc:/tjafiles/theme/↓

  　　　　　　　　　　config.json ⇒ スキン全体の設定

  　　　　　　　　　　dancer.t3x  ⇒ 踊り子を表示する部分

  </code></pre>

  <p dir="auto">因みに今回のバージョンから自動でconfig.jsonが出なくなるので、<br>

  踊り子を実装したい場合は↓のテンプレートをコピーして作成して下さい。</p>

  <div class="highlight highlight-source-json" dir="auto"><pre class="notranslate">{<span
  class="pl-ent">"don_x"</span>: <span class="pl-c1">76</span>, <span class="pl-ent">"don_y"</span>:
  <span class="pl-c1">43</span>, <span class="pl-ent">"don_go_x"</span>: <span class="pl-c1">76</span>,
  <span class="pl-ent">"don_go_y"</span>: <span class="pl-c1">43</span>, <span class="pl-ent">"d1anime"</span>:
  <span class="pl-s"><span class="pl-pds">"</span>0,1,2,3<span class="pl-pds">"</span></span>,
  <span class="pl-ent">"d2anime"</span>: <span class="pl-s"><span class="pl-pds">"</span>0,1,2,3<span
  class="pl-pds">"</span></span>, <span class="pl-ent">"d3anime"</span>: <span class="pl-s"><span
  class="pl-pds">"</span>0,1,2,3<span class="pl-pds">"</span></span>}</pre></div>

  <p dir="auto">新オプションの d1anime, d2anime, d3anime は踊り子の何コマ目を表示するかを最大128コマ指定出来ます。<br>

  4小節1ループの為<del>調整がかなり面倒くさいですが</del>ボカロキャラの踊り子も可能です。<br>

  ※「さちさちにしてあげる♪」の様なクリア達成時のモーション変更は出来ません。</p>

  <ul dir="auto">

  <li>ロード中に演奏できる様に(※曲は流れません)</li>

  <li>コンボボイスの実装</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Implementation of a dancer that appears at the bottom of the upper screen.<br>

  You can do this by placing dancer.t3x and the configured config.json as shown below.</li>

  </ul>

  <pre class="notranslate"><code class="notranslate">sdmc:/tjafiles/theme/↓

  　　　　　　　　　　config.json ⇒ Global Skin Settings

  　　　　　　　　　　dancer.t3x  ⇒ Dancer''s Assets

  </code></pre>

  <p dir="auto">Incidentally, config.json will no longer be displayed automatically
  from this version onwards,<br>

  so if you want to implement a dancer, please copy and create the template below.</p>

  <div class="highlight highlight-source-json" dir="auto"><pre class="notranslate">{<span
  class="pl-ent">"don_x"</span>: <span class="pl-c1">76</span>, <span class="pl-ent">"don_y"</span>:
  <span class="pl-c1">43</span>, <span class="pl-ent">"don_go_x"</span>: <span class="pl-c1">76</span>,
  <span class="pl-ent">"don_go_y"</span>: <span class="pl-c1">43</span>, <span class="pl-ent">"d1anime"</span>:
  <span class="pl-s"><span class="pl-pds">"</span>0,1,2,3<span class="pl-pds">"</span></span>,
  <span class="pl-ent">"d2anime"</span>: <span class="pl-s"><span class="pl-pds">"</span>0,1,2,3<span
  class="pl-pds">"</span></span>, <span class="pl-ent">"d3anime"</span>: <span class="pl-s"><span
  class="pl-pds">"</span>0,1,2,3<span class="pl-pds">"</span></span>}</pre></div>

  <p dir="auto">The new options d1anime, d2anime, and d3anime allow you to specify
  how many frames of the dancer should be displayed, up to 128 frames.<br>

  Since it is a 4-measure 1-loop <del>although the adjustment is quite troublesome</del>,
  it is also possible to use Vocaloid character dancers.<br>

  ※You cannot change the motion when you achieve clear like “I''ll make you Sachi
  Sachi”.</p>

  <ul dir="auto">

  <li>You can play music while it loads. (※music will not play)</li>

  <li>Addition of ComboVoice</li>

  </ul>'
updated: '2025-02-07T05:08:59Z'
version: v1.5.0
version_title: TJAPlayer for 3DS v1.5.0
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