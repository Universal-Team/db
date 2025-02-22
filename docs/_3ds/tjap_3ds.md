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
    size: 692976
    size_str: 676 KiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.4.6B/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 1008576
    size_str: 984 KiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.4.6B/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v1.5.0
  downloads:
    TJAP_3DS.3dsx:
      size: 1443428
      size_str: 1 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.5.0/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 1766336
      size_str: 1 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.5.0/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
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

    You can do this by placing dancer.t3x and the configured config.json as shown
    below.</li>

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
  update_notes_md: "## チェンジログ\n - 上画面下部に出る踊り子の実装\ndancer.t3x と 設定済みの config.json を以下のように置けば出来ます。\n\
    ```\nsdmc:/tjafiles/theme/↓\n　　　　　　　　　　config.json ⇒ スキン全体の設定\n　　　　　　　　　　dancer.t3x\
    \  ⇒ 踊り子を表示する部分\n```\n因みに今回のバージョンから自動でconfig.jsonが出なくなるので、\n踊り子を実装したい場合は↓のテンプレートをコピーして作成して下さい。\n\
    ```json\n{\"don_x\": 76, \"don_y\": 43, \"don_go_x\": 76, \"don_go_y\": 43, \"\
    d1anime\": \"0,1,2,3\", \"d2anime\": \"0,1,2,3\", \"d3anime\": \"0,1,2,3\"}\n\
    ```\n新オプションの d1anime, d2anime, d3anime は踊り子の何コマ目を表示するかを最大128コマ指定出来ます。\n4小節1ループの為~調整がかなり面倒くさいですが~ボカロキャラの踊り子も可能です。\n\
    ※「さちさちにしてあげる♪」の様なクリア達成時のモーション変更は出来ません。\n\n - ロード中に演奏できる様に(※曲は流れません)\n - コンボボイスの実装\n\
    ## Changelog\n - Implementation of a dancer that appears at the bottom of the\
    \ upper screen.\nYou can do this by placing dancer.t3x and the configured config.json\
    \ as shown below.\n```\nsdmc:/tjafiles/theme/↓\n　　　　　　　　　　config.json ⇒ Global\
    \ Skin Settings\n　　　　　　　　　　dancer.t3x  ⇒ Dancer's Assets\n```\nIncidentally, config.json\
    \ will no longer be displayed automatically from this version onwards, \nso if\
    \ you want to implement a dancer, please copy and create the template below.\n\
    ```json\n{\"don_x\": 76, \"don_y\": 43, \"don_go_x\": 76, \"don_go_y\": 43, \"\
    d1anime\": \"0,1,2,3\", \"d2anime\": \"0,1,2,3\", \"d3anime\": \"0,1,2,3\"}\n\
    ```\nThe new options d1anime, d2anime, and d3anime allow you to specify how many\
    \ frames of the dancer should be displayed, up to 128 frames.\nSince it is a 4-measure\
    \ 1-loop ~although the adjustment is quite troublesome~, it is also possible to\
    \ use Vocaloid character dancers.\n※You cannot change the motion when you achieve\
    \ clear like “I'll make you Sachi Sachi”.\n\n - You can play music while it loads.\
    \ (※music will not play)\n - Addition of ComboVoice"
  updated: '2025-02-07T05:08:59Z'
  version: v1.5.0
  version_title: TJAPlayer for 3DS v1.5.0
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

  <li>OLD3DSでプレイすると演奏中fpsが低下する不具合の修正</li>

  <li>譜面分岐が実行されない不具合の修正 (2025/02/04追記)</li>

  <li>特定の譜面にて譜面分岐が正常に実行されない不具合の修正 (2025/02/05追記)</li>

  </ul>

  <h2 dir="auto">change log</h2>

  <ul dir="auto">

  <li>Fixed a bug that caused fps to drop when playing on OLD3DS.</li>

  <li>Fixed a bug where music sheet branching was not executed. (Added 2025/02/04)</li>

  <li>Fixed a bug that caused the score branching not to be executed properly on a
  specific score (Added 2025/02/05)</li>

  </ul>'
updated: '2025-01-31T23:51:00Z'
version: v1.4.6B
version_title: TJAPlayer for 3DS v1.4.6(B)
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