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
    size: 10275596
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.4.3/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 10437568
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.4.3/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
llm_generation: unknown
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v2.4.3A
  downloads:
    TJAP_3DS.3dsx:
      size: 10277708
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.4.3A/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 10441664
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.4.3A/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>「互換モード」をONにした際の演奏処理の軽量化<br>

    Newシリーズなら1万コンボの譜面も軽快に動くはずです。</li>

    <li>小節線と連打音符の出現数に上限があったのを引き上げました。<br>

    同時に512小節まで表示出来たのが1024小節分表示出来る様に。<br>

    連打音符も同様に同時に512回までしか召喚できなかったのを1024回まで可能に。</li>

    <li>「段位道場」等でどれくらい達成出来たかをゲージで表示出来る様に</li>

    </ul>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Improved performance processing when "Comp Mode" is ON.<br>

    With the New Series, even 10,000-combo charts should run smoothly.</li>

    <li>Increased the upper limit on the number of bar lines and rapid-fire notes
    that can appear.<br>

    The ability to display up to 512 bars simultaneously has been increased to 1024
    bars.<br>

    Similarly, the ability to summon rapid-fire notes simultaneously has been increased
    from 512 to 1024.</li>

    <li>It would be possible to display a gauge showing how much progress has been
    made in "Dan-i Dojo," etc.</li>

    </ul>'
  update_notes_md: '## チェンジログ

    - 「互換モード」をONにした際の演奏処理の軽量化

    Newシリーズなら1万コンボの譜面も軽快に動くはずです。

    - 小節線と連打音符の出現数に上限があったのを引き上げました。

    同時に512小節まで表示出来たのが1024小節分表示出来る様に。

    連打音符も同様に同時に512回までしか召喚できなかったのを1024回まで可能に。

    - 「段位道場」等でどれくらい達成出来たかをゲージで表示出来る様に


    ## Changelog

    - Improved performance processing when "Comp Mode" is ON.

    With the New Series, even 10,000-combo charts should run smoothly.

    - Increased the upper limit on the number of bar lines and rapid-fire notes that
    can appear.

    The ability to display up to 512 bars simultaneously has been increased to 1024
    bars.

    Similarly, the ability to summon rapid-fire notes simultaneously has been increased
    from 512 to 1024.

    - It would be possible to display a gauge showing how much progress has been made
    in "Dan-i Dojo," etc.'
  updated: '2026-11-14T04:50:08Z'
  version: v2.4.3A
  version_title: TJAPlayer for 3DS v2.4.3(A)
qr:
  TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/tjap_3ds-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-2.png
source: https://github.com/LuMariGames/TJAP_3DS
stars: 17
systems:
- 3DS
title: TJAP_3DS
unique_ids:
- '0xB7655'
update_notes: '<h2 dir="auto">チェンジログ</h2>

  <ul dir="auto">

  <li>段位道場において個別条件の対応</li>

  <li>「互換モード」の実装<br>

  譜面を先読みして動かない処理を正常に動かすモードです。<br>

  先読みする関係上安定性は上がりますが処理が重くなるのでご注意下さい。</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Handling individual conditions at Dan-i Dojo.</li>

  <li>Implementation of "Comp Mode"<br>

  This mode allows processes that previously wouldn''t run due to pre-loading the
  score to function correctly.<br>

  While stability is improved due to the pre-loading, please note that processing
  load will increase.</li>

  </ul>'
updated: '2026-11-09T11:35:32Z'
version: v2.4.3
version_title: TJAPlayer for 3DS v2.4.3
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