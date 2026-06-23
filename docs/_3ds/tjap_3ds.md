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
    size: 10392592
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.2.3/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 10568640
    size_str: 10 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.2.3/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
llm_generation: unknown
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v2.3.0-pre
  downloads:
    TJAP_3DS.3dsx:
      size: 10392792
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.3.0-pre/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 10568640
      size_str: 10 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.3.0-pre/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>HBSCROLLの試験的実装<br>

    太鼓さん次郎のHBSCROLLを真似て実装する予定なのでかなりの時間と協力が必要です。<br>

    <a href="https://github.com/LuMariGames/TJAP_3DS/fork">Fork</a>を使用して実装の協力をしてくれた人にはゲーム内クレジットに記載をします。</li>

    </ul>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Experimental implementation of HBSCROLL.<br>

    I plan to implement this by imitating Taiko-san Jiro''s HBSCROLL, so it will require
    a considerable amount of time and cooperation.<br>

    Those who helped implement the project using <a href="https://github.com/LuMariGames/TJAP_3DS/fork">Fork</a>
    will be credited in-game.</li>

    </ul>'
  update_notes_md: '## チェンジログ

    - HBSCROLLの試験的実装

    太鼓さん次郎のHBSCROLLを真似て実装する予定なのでかなりの時間と協力が必要です。

    [Fork](https://github.com/LuMariGames/TJAP_3DS/fork)を使用して実装の協力をしてくれた人にはゲーム内クレジットに記載をします。


    ## Changelog

    - Experimental implementation of HBSCROLL.

    I plan to implement this by imitating Taiko-san Jiro''s HBSCROLL, so it will require
    a considerable amount of time and cooperation.

    Those who helped implement the project using [Fork](https://github.com/LuMariGames/TJAP_3DS/fork)
    will be credited in-game.'
  updated: '2026-06-19T23:23:10Z'
  version: v2.3.0-pre
  version_title: TJAPlayer for 3DS v2.3.0-pre
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

  <li>複素数スクロールの対応</li>

  </ul>

  <pre class="notranslate"><code class="notranslate">#SCROLL (Signed float)(Signed
  float)i

  </code></pre>

  <ul dir="auto">

  <li>前回のプレイを記録&amp;再生出来るようになりました。<br>

  プレイを終わらせた後に「実験的設定」の「プレイヤー(双打用)」を<br>

  PLAYに変更すると、前回のプレイを再生出来ます。<br>

  記録を消したい場合はSELECTを押しながらXボタンを押して下さい。</li>

  <li>オプション「曲のはやさ」を1倍以外にするとJPOSSCROLLの終了タイミングがズレる不具合の修正</li>

  <li>編集可能な譜面の最大容量を64KBに増やしました。</li>

  <li>HBSCROLLの試験的対応</li>

  <li>その他一部動作の高速化をしました。</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>support for complex number scrolling.</li>

  </ul>

  <pre class="notranslate"><code class="notranslate">#SCROLL (Signed float)(Signed
  float)i

  </code></pre>

  <ul dir="auto">

  <li>You can now record and replay your previous gameplay.<br>

  After finishing a game, changing the "Player (for dual-wielding)" setting in<br>

  "Experimental Settings" to PLAY will allow you to replay your previous play.<br>

  To erase your record, press the SELECT button while holding down the X button.</li>

  <li>Fixed a bug that caused the end timing of JPOSSCROLL to shift if the option
  "song so fastness" was not 1x.</li>

  <li>The maximum size of editable charts has been increased to 64KB.</li>

  <li>Experimental response to HBSCROLL.</li>

  <li>We have also sped up some other operations.</li>

  </ul>'
updated: '2026-06-02T03:51:14Z'
version: v2.2.3
version_title: TJAPlayer for 3DS v2.2.3
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